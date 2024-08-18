# Method Overloading:
# Python does not support method overloading
# in the traditional sense.

# Method - overloading - Not supported!

class MathUtil(object):
    def add(self, a, b=0, c=0):
        return a+b+c

    # def add(self,a,b):
    #     pass
    #
    # def add(self, a, b, c, d):
    #     pass

math = MathUtil()
op_0 = math.add(1)
op_1 = math.add (1,2)
op_2 = math.add(1,2,3)
print(op_0)
print(op_1)
print(op_2)