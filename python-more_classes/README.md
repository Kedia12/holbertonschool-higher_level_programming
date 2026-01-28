CLASSES IN PYTHON


Object-oriented programming (OOP) is one of the most effective approaches to writing software. In OOP, you write classes that represent real-world things and situations, and you create objects based on these classes.

When you write a class, you define the general behavior (what it can do) and structure (what it knows) that a whole category of objects can have. When you create individual objects from the class, each object is automatically equipped with that shared behavior; you can then give each object whatever unique traits (data) you want. Real-world systems are often easier to design and understand when modeled this way.

Making an object from a class is called instantiation, and the resulting objects are called instances. Instances store their own data (like a specific dog’s name and age) while sharing the same set of behaviors defined by the class (like sit() or roll_over()). This lets you create many objects that behave consistently while still representing different real things.

Core Concepts (Quick Glossary)

Class: A blueprint (a type) that defines data + behavior.
Object: A value in memory. In Python, everything is an object.
Instance: An object created from a specific class.
Attribute: Data attached to an object or class (e.g., self.name, Dog.species).
Method: A function defined inside a class (e.g., Dog.sit()).

THE PARTS OF A CLASS

1) The constructor: __init__

__init__ runs automatically when you create an instance. It usually sets up instance attributes.
class Dog:
    def __init__(self, name, age):
        self.name = name     # instance attribute
        self.age = age       # instance attribute
name and age here are parameters.
self.name and self.age are attributes stored on the instance.

2) Instance methods (the “regular” methods)

Instance methods take self and act on the instance.
class Dog:
    def sit(self):
        print(f"{self.name} is sitting.")
Calling my_dog.sit() will run that method for that specific dog.

3) Class attributes vs instance attributes

Instance attributes belong to each instance.
Class attributes belong to the class and are shared.
class Dog:
    species = "canine"   # class attribute shared by all dogs

    def __init__(self, name):
        self.name = name # instance attribute unique to each dog

Types of Methods
Instance method
Uses self, works with per-object state.
Class method (@classmethod)
Uses cls (the class). Common for alternative constructors.
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def from_tuple(cls, t):
        return cls(*t)

Static method (@staticmethod)
No self or cls. Used for utility functions grouped with the class.
class Math:
    @staticmethod
    def clamp(x, lo, hi):
        return max(lo, min(x, hi))

Properties: Methods that Look Like Attributes
Use @property when you want “attribute-like” access with logic (validation, computed values).
class Celsius:
    def __init__(self, c):
        self._c = c

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._c = value

This lets you do temp.c = 20 while still enforcing rules.
Inheritance (Extending Classes)
Inheritance lets a new class reuse or override behavior from an existing class.

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "woof"
Dog inherits from Animal
Dog overrides speak
Use super() when extending methods cleanly:
class Base:
    def __init__(self, x):
        self.x = x

class Child(Base):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

Composition (Often Better Than Inheritance)

Sometimes it’s better to build classes out of other objects instead of inheriting.
Example idea: a Car has an Engine (composition) rather than Car is an Engine (inheritance).
Composition often makes designs more flexible and easier to change.
Common “Gotchas” (Worth Remembering)
Shared mutable class attribute
Don’t do this:

class Bad:
    items = []  # shared by all instances!
Do this instead:
class Good:
    def __init__(self):
        self.items = []  # unique per instance

Methods don’t run unless called
If you wrote prints in sit() or roll_over(), they won’t appear until you do:
my_dog.sit()
my_dog.roll_over()
Dataclasses (Modern, Practical Classes)
If your class mostly holds data, use @dataclass to remove boilerplate:
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
You automatically get __init__, a nice __repr__, and comparisons.
A Simple Class Example (Complete)
class Dog:
    species = "canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old."

    def sit(self):
        print(f"{self.name} is now sitting.")

my_dog = Dog("Willie", 6)
print(my_dog.describe())
my_dog.sit()
print(Dog.species)


Summary
Classes help you structure programs by grouping data and behavior into reusable, understandable units. They enable you to model real-world entities, build clean interfaces, reuse logic through inheritance or composition, and organize code into modules that scale well with complexity.
