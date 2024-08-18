# Multilevel Inheritance

class Grandparent():
    key_gold = "1 kg"
    def grandparent_method(self):
        return "Grandparent's method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"


class Child(Parent):
    mac_m3_apple = "M3 Max"
    def child_method(self):
        return "Child's method"


child = Child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
print(child.key_gold)
print(child.mac_m3_apple)

print("--------")

parent = Parent()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key_gold)


print("--------")
grandparent_ref = Grandparent()
print(grandparent_ref.grandparent_method())
print(grandparent_ref.key_gold)