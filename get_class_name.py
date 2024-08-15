#Python Program to Get the Class Name of an Instance.
class Car:
    def name(self, name):
        return name

v = Car()
print(v.__class__.__name__)