class A(object):
    def __init__ (self, name):
        self.name = name
    def str(self):
        return "Name: " + str(self.name)
class B(A):
    def __init__ (self, name, age):
        A.__init__(self, name)
        self.age = age
    def str(self):
        return A.str(self) + "\n " + "Age: " + str(self.age)

x = B("Alexander Solomon", 20)
print (x.str())