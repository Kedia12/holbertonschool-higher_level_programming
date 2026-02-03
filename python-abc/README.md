ABSTRACT CLASSES AND INTERFACES (PYTHON OOP)

When your project grows, you often want a common “shape” (API) across multiple classes, while still allowing each class to implement details differently. That’s where abstract classes, interfaces, and subclassing come in.

ABSTRACT CLASS

An abstract class is a “partially complete” parent class that:
* provides a shared structure (common methods / attributes)
* can include real code (concrete methods)
* can also declare methods that must be implemented by subclasses (abstract methods)

In Python, abstract classes are commonly built using abc.ABC and 
@abstractmethod.

WHY USE AN ABSTRACT CLASS?

* Enforce that all child classes implement key behavior (e.g., area())
* Share common logic once (avoid duplication)
* Make code easier to extend safely

EXAMPLE IDEA

* Shape defines area() as required
* Rectangle and Circle implement their own area()

INTERFACE (PYTHON STYLE)

An interface is a contract: “Any class that wants to act like X must 
have these methods.”

Python doesn’t have “interfaces” as a separate keyword like Java, but you can achieve the same goal using:

1) Duck Typing (most Pythonic)

“If it quacks like a duck, it’s a duck.”
You don’t care about the class name, you care that the object supports 
the methods you need.

2) Abstract Base Classes (ABC)

This is the strict/explicit approach: enforce required methods via abstract classes.

3) Protocols (typing-based interfaces)

With type hints, Protocol can describe an interface-like shape for static checking.

SUBCLASSING (INHERITANCE)

Subclassing is when a child class inherits behavior from a parent class:

* child automatically gets parent methods/attributes
* child can extend (add new methods/attributes)
* child can override (replace parent behavior)

KEY TERMS

* Parent / Base / Superclass: the class being inherited from
* Child / Derived / Subclass: the class doing the inheriting
* Override: child defines a method with the same name to replace the 
parent version

HOW THEY WORK TOGETHER

A common pattern:

* Use an abstract class to define the required API (interface-like contract).
* Use subclassing so each concrete class implements the required methods.
* Write code that depends on the shared API, not on specific subclasses.

EXAMPLE CONCEPTUALLY:

* Abstract: BaseGeometry requires area()
* Concrete subclasses: Rectangle, Square implement area()

Then other code can do:

* “Call .area() on any geometry object”
* without caring whether it’s a rectangle or square

WHEN TO USE WHAT

* Use duck typing when you want flexibility and you only need a small method set.
* Use abstract classes (ABC) when you want strict enforcement and shared base behavior.
* Use subclassing when there’s a real “is-a” relationship and shared logic makes sense.
