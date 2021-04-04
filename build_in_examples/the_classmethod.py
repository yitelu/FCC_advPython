# classmethod()	Converts a method into a class method

"""
class classmethod(object)
 |  classmethod(function) -> method
 |
 |  Convert a function to be a class method.
 |
 |  A class method receives the class as implicit first argument,
 |  just like an instance method receives the instance.
 |  To declare a class method, use this idiom:
 |
 |    class C:
 |        @classmethod
 |        def f(cls, arg1, arg2, ...):
 |            ...
 |
 |  It can be called either on the class (e.g. C.f()) or on an instance
 |  (e.g. C().f()).  The instance is ignored except for its class.
 |  If a class method is called for a derived class, the derived class
 |  object is passed as the implied first argument.
 |
 |  Class methods are different than C++ or Java static methods.
 |  If you want those, see the staticmethod builtin.
"""


class Car:
    def __init__(self, features):
        self.features = features

    def __repr__(self):
        return f"Car ({self.features})"

    @classmethod
    def truck(cls):
        return cls(["4x4", "big tire"])

    @classmethod
    def sport(cls, packages):
        if packages == "SRT":
            return cls(["300hp", "2x4", "sports tire"])
        elif packages == "ST":
            return cls(["ST", "2x4", "sports tire"])
        else:
            return cls(["boring", "ordinary tire"])


TruckCar = Car.truck()
sportCar = Car.sport("ST")
sportSRTCar = Car.sport("SRT")
basicSportCar = Car.sport("basic")


print("newCar", TruckCar.features)
print("newCar", sportCar.features)
print("newCar", sportSRTCar.features)
print("newCar", basicSportCar.features)
