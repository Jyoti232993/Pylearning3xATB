from abc import ABC, abstractmethod

class ATB(ABC):

    def enrolled(self):
        print("Enrolled")

    @abstractmethod
    def perform_task_1(self):
        pass

    @abstractmethod
    def perform_task_2(self):
        pass

class Amit(ATB):
    def perform_task_1(self):
        return "Done 1"

    def perform_task_2(self):
        return "Done 2"


amit = Amit()
print(amit.perform_task_1())
print(amit.perform_task_2())