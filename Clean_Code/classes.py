import csv
from importlib import metadata
from dataclasses import dataclass
from io import StringIO

# 14. Single Responsability Priciple (SRP)


# bad
class VersionCommentElement:
    """An element that renders an HTML comment with the program's version number"""

    def get_version(self) -> str:
        """Get the package version"""
        return metadata.version("pip")

    def render(self) -> None:
        print(f"<!-- Version: {self.get_version()} -->")


VersionCommentElement().render()

# best practice
from importlib import metadata


def get_version(pkg_name: str) -> str:
    """Retrieve the version of a given package"""
    return metadata.version(pkg_name)


class VersionCommentElement:
    """An element that renders an HTML comment with the program's version number"""

    def __init__(self, version: str):
        self.version = version

    def render(self) -> None:
        print(f"<!-- Version: {self.version} -->")


VersionCommentElement(get_version("pip")).render()

# 15 Open/Closed Principle (OCP)


@dataclass
class Response:
    """An HTTP response"""

    status: int
    content_type: str
    body: str


class View:
    """A simple view that returns plain text responses"""

    def get(self, request) -> Response:
        """Handle a GET request and return a message in the response"""
        return Response(
            status=200, content_type="text/plain", body="Welcome to my web site"
        )


class TemplateView(View):
    """A view that returns HTML responses based on a template file."""

    def get(self, request) -> Response:
        """Handle a GET request and return an HTML document in the response"""
        with open("index.html") as fd:
            return Response(status=200, content_type="text/html", body=fd.read())


# best practice
@dataclass
class Response:
    """An HTTP response"""

    status: int
    content_type: str
    body: str


class View:
    """A simple view that returns plain text responses"""

    content_type = "text/plain"

    def render_body(self) -> str:
        """Render the message body of the response"""
        return "Welcome to my web site"

    def get(self, request) -> Response:
        """Handle a GET request and return a message in the response"""
        return Response(
            status=200, content_type=self.content_type, body=self.render_body()
        )


class TemplateView(View):
    """A view that returns HTML responses based on a template file."""

    content_type = "text/html"
    template_file = "index.html"

    def render_body(self) -> str:
        """Render the message body as HTML"""
        with open(self.template_file) as fd:
            return fd.read()


# 16. Dependency Inversion Principle (DIP)


# bad
class StreamingHttpResponse:
    """A streaming HTTP response"""

    ...  # implementation code goes here


def some_view(request):
    rows = (
        ["First row", "Foo", "Bar", "Baz"],
        ["Second row", "A", "B", "C", '"Testing"', "Here's a quote"],
    )

    # Define a generator to stream data directly to the client
    def stream():
        buffer_ = StringIO()
        writer = csv.writer(buffer_, delimiter=";", quotechar='"')
        for row in rows:
            writer.writerow(row)
            buffer_.seek(0)
            data = buffer_.read()
            buffer_.seek(0)
            buffer_.truncate()
            yield data

    # Create the streaming response  object with the appropriate CSV header.
    response = StreamingHttpResponse(stream(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="somefilename.csv"'

    return response


# best practice
class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def some_streaming_csv_view(request):
    """A view that streams a large CSV file."""
    rows = (
        ["First row", "Foo", "Bar", "Baz"],
        ["Second row", "A", "B", "C", '"Testing"', "Here's a quote"],
    )
    writer = csv.writer(Echo(), delimiter=";", quotechar='"')
    return StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )
