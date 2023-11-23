# # NotificationService that sends messages, and initially,
# # it depends directly on a specific EmailSender class.
#
# class EmailSender:
#     def send_email(self, to, message):
#         print(f"Sending email to {to}: {message}")
#
#
# class NotificationService:
#     def __init__(self, email_sender):
#         self.email_sender = email_sender
#
#     def send_notification(self, to, message):
#         self.email_sender.send_email(to, message)

# define an abstraction, MessageSender,
# which both EmailSender and potentially other message sending classes will implement
from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send_message(self, to, message):
        pass


# Low-level module
class EmailSender(MessageSender):
    def send_message(self, to, message):
        print(f"Sending email to {to}: {message}")


# modify NotificationService to depend on the abstraction rather than the concrete EmailSender class:
# High-level module
class NotificationService:
    def __init__(self, message_sender):
        self.message_sender = message_sender

    def send_notification(self, to, message):
        self.message_sender.send_message(to, message)

# NotificationService doesn't depend directly on EmailSender!!  It depends on the abstraction MessageSender
# You can easily extend the system by adding new message sending classes that implement the MessageSender
# interface without modifying the high-level module.
