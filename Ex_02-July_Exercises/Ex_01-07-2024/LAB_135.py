class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2 BHK")

class Child(Parent):
    def BHK3(self):
        print("3 BHK")

child_object = Child()
child_object.BHK3()
child_object.BHK2()
print(child_object.gold)

print("------------")
father_obj_ref = Parent()
father_obj_ref.BHK2()
print(father_obj_ref.gold)
