INHERITANCE IN PYTHON CLASSES

Inheritance lets you create a new class (child/subclass) that reuses and extends behavior from an existing class (parent/superclass). It helps you avoid repeating code and model “is-a” relationships (e.g., an ElectricCar is a Car).

KEY IDEAS

* Parent class: defines shared attributes and methods.
* Child class: inherits everything from the parent, and can:
    * add new attributes/methods
    * override methods to change behavior
* super(): calls the parent’s version of a method (commonly used in __init__).

BASIC EXAMPLE

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}".title()

    def fill_energy(self):
        print("Filling gas tank...")


class ElectricCar(Car):  # Inherit from Car
    def __init__(self, make, model, year, battery_kwh=75):
        super().__init__(make, model, year)  # call parent constructor
        self.battery_kwh = battery_kwh       # new attribute

    # Override: electric cars fill energy differently
    def fill_energy(self):
        print(f"Charging battery ({self.battery_kwh} kWh)...")


Usage:

cars = [
    Car("toyota", "corolla", 2010),
    ElectricCar("tesla", "model 3", 2022, battery_kwh=60),
]

for car in cars:
    print(car.description())
    car.fill_energy()  # same method name, different behavior


OVERRIDING METHODS
Overriding means defining a method in the child class with the same name as a method in the parent class. When you call it on a child instance, Python uses the child’s version.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # overrides Parent.greet
        print("Hello from Child")

MULTIPLE INHERITANCE (OPTIONAL)
Python supports inheriting from more than one parent:

class A:
    def who(self): print("A")

class B:
    def who(self): print("B")

class C(A, B):
    pass

c = C()
c.who()  # uses Method Resolution Order (MRO)

print(C.mro())

Python resolves method lookups using the MRO (left-to-right through the base classes).

WHEN TO USE INHERITANCE VS COMPOSITION

* Use inheritance when the child truly is a parent (clear shared interface/behavior).
* Use composition when something has a other object (often more flexible).

Example composition idea: Car has a Battery, instead of being a special kind of Battery.

BEST PRACTICES

* Keep parent classes focused on shared behavior.
* Prefer overriding only when behavior genuinely differs.
* Use super() in subclasses to keep initialization consistent.
* Avoid deep inheritance trees unless they’re clearly justified.
