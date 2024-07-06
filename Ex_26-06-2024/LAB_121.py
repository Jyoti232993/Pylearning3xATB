class student:

    # Define the constructor
    def __init__(self):
        self.name = input("Enter the name:")
        self.age = int(input("Enter the age:"))

    def display(self):
        print(f"Name is {self.name}, Age is {self.age}")


# Create object of a "student" class
# objectRef = Object ->  ClassName()

student = student()
student.display()
