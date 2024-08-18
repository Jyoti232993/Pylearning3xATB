from abc import ABC, abstractmethod

class PYATB(ABC):

    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class shubham(PYATB):
    def payfee(self):
        print("Paid")

shubham_obj_ref = shubham()
shubham_obj_ref.payfee()
shubham_obj_ref.enrolled()