# super()	Returns an object that represents the parent class

"""
class super(object)
 |  super() -> same as super(__class__, <first argument>)
 |  super(type) -> unbound super object
 |  super(type, obj) -> bound super object; requires isinstance(obj, type)
 |  super(type, type2) -> bound super object; requires issubclass(type2, type)
 |  Typical use to call a cooperative superclass method:
 |  class C(B):
 |      def meth(self, arg):
 |          super().meth(arg)
 |  This works for class methods too:
 |  class C(B):
 |      @classmethod
 |      def cmeth(cls, arg):
 |          super().cmeth(arg)
"""

class Animal():
    def __init__(self, Animal):
        print(Animal, "is an animal")

class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, "is a warm animal")
        super().__init__(mammalName)

class Dog(Mammal):
    def __init__(self, the_name):
        print(the_name + " dog has four legs")
        super().__init__("dog")


my_dog = Dog("Snoopy")

