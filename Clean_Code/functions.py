from typing import Tuple, List, Dict, AnyStr
from tempfile import gettempdir
from pathlib import Path

# 8. Functions should do one thing


# bad
class Client:
    active: bool


def email(client: Client) -> None:
    pass


def email_clients(clients: List[Client]) -> None:
    for client in clients:
        if client.active:
            email(client)


from typing import Generator, Iterator


# best practice


class Client:
    active: bool


def email(client: Client):
    pass


def active_clients(clients: Iterator[Client]) -> Generator[Client, None, None]:
    """Only active clients"""
    return (client for client in clients if client.active)


def email_client(clients: Iterator[Client]) -> None:
    """Send an email to a given list of clients."""
    for client in active_clients(clients):
        email(client)


# 9. Function arguments -> 2 or fewer
# bad
def create_menu(title, body, button_text, cancellable):
    pass


# good
class Menu:
    def __init__(self, config: dict):
        self.title = config["title"]
        self.body = config["body"]
        # ...


menu = Menu(
    {
        "title": "My Menu",
        "body": "Something about my menu",
        "button_text": "OK",
        "cancellable": False,
    }
)

# best practice

from typing import NamedTuple


class MenuConfig(NamedTuple):
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """

    title: str
    body: str
    button_text: str
    cancellable: bool = False


def create_menu(config: MenuConfig):
    title, body, button_text, cancellable = config
    # ...


create_menu(
    MenuConfig(
        title="My delicious menu",
        body="A description of the various items on the menu",
        button_text="Order now!",
    )
)

# Function names should say what they do


# bad
class Email:
    def handle(self) -> None:
        pass


message = Email()
# What is this supposed to do again?
message.handle()


# best practice
class Email:
    def send(self) -> None:
        """Send this message"""


message = Email()
message.send()

# 11. Functions should only be one level of abstraction


# bad
def parse_better_js_alternative(code: str) -> None:
    regexes = [
        # ...
    ]

    statements = code.split("\n")
    tokens = []
    for regex in regexes:
        for statement in statements:
            pass

    ast = []
    for token in tokens:
        pass

    for node in ast:
        pass


# best practice

REGEXES: Tuple = (
    # ...
)


def tokenize(code: str) -> List:
    statements = code.split()
    tokens: List[Dict] = []
    for regex in REGEXES:
        for statement in statements:
            pass

    return tokens


def parse(tokens: List) -> List:
    syntax_tree: List[Dict] = []
    for token in tokens:
        pass

    return syntax_tree


def parse_better_js_alternative(code: str) -> None:
    tokens: List = tokenize(code)
    syntax_tree: List = parse(tokens)

    for node in syntax_tree:
        pass


# 12. Don't use flags as function parameters

# bad


def create_file(name: str, temp: bool) -> None:
    if temp:
        (Path(gettempdir()) / name).touch()
    else:
        Path(name).touch()


# best practice
def create_file(name: str) -> None:
    Path(name).touch()


def create_temp_file(name: str) -> None:
    (Path(gettempdir()) / name).touch()


# 13. Avoid side effects


# bad
fullname = "Ryan McDermott"


def split_into_first_and_last_name() -> None:
    global fullname
    fullname = fullname.split()


split_into_first_and_last_name()
print(fullname)

# best practice


def split_into_first_and_last_name(name: AnyStr) -> List[AnyStr]:
    return name.split()


fullname = "Ryan McDermott"
name, surname = split_into_first_and_last_name(fullname)

print(name, surname)
