# from abc import ABC, abstractmethod
#
#
# class Worker(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
#
# #  Manager class doesn't need to implement the eat method because managers
# #  don't necessarily have to eat as part of their job.
#
# #!!! This violates the Interface Segregation Principle because the Manager class is forced to implement the eat method,
# # even though it doesn't make sense for a manager.
# class Manager(Worker):
#     def work(self):
#         print("Manager is working")


from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Manager(Workable):
    def work(self):
        print("Manager is working")


class Engineer(Workable, Eatable):
    def work(self):
        print("Engineer is working")

    def eat(self):
        print("Engineer is eating")

