# Python Objects, References, and Mutability

## Description

This project is about understanding how Python handles objects, variables, and memory. These ideas are very important because they explain why some values change when you do not expect them to, while others stay the same.

In Python, everything is an object. Numbers, strings, lists, tuples, dictionaries, and even functions are all objects. When you create a variable, the variable does not directly store the value itself. Instead, it stores a reference to an object somewhere in memory.

## Examples

when you write:

a = 1

Python creates the integer object 1, and the variable a refers to that object.

If you then write:

b = a

both a and b refer to the same object at that moment. However, if you later do:

a = 2

Python does not change the original integer object 1. Instead, it makes a refer to a new object, 2. That is why b still keeps the value 1.

This behavior is different with mutable objects.

## Mutable and Immutable Objects

A big part of this project is understanding the difference between mutable and immutable types.

## Immutable objects

Immutable objects cannot be changed after they are created.
Common built-in immutable types include:

• int
• float
• str
• tuple
• bool

If you seem to modify an immutable object, Python actually creates a new object instead of changing the old one.

## Mutable objects

Mutable objects can be changed after they are created.
Common built-in mutable types include:

list
dict
set

For example:

l = [1, 2, 3]
m = l
l[0] = 'x'

Here, l and m both refer to the same list object. Since lists are mutable, changing the list through l also changes what m sees. That is why m becomes:

['x', 2, 3]

This is called aliasing.

## Important Concepts in This Project

## Object

An object is a value stored in memory. Every value in Python is an object.

## Class

A class is like a blueprint or model used to create objects.

## Instance

An instance is a specific object created from a class.

Reference

A reference is the connection between a variable and an object.

## Assignment

Assignment means giving a variable a reference to an object.

Example:

x = [1, 2, 3]

This does not copy the list into x. It makes x refer to that list.

## Alias

An alias happens when two or more variables refer to the same object.

Example:

a = [1, 2]
b = a

Now a and b are aliases of the same list.

## Identity

Identity means checking whether two variables point to the exact same object in memory.

You can test this with:

a is b
## Equality

Equality means checking whether two objects have the same value.

You can test this with:

a == b

Two objects can be equal without being identical.

## How to Know if Two Variables Are the Same Object

Python gives you two useful tools for this:

is

The is operator checks whether two variables point to the same object.

id()

The id() function shows the identifier of an object. In CPython, this is related to the memory address.

Example:

print(id(a))
print(id(b))

If a and b have the same id, they refer to the same object.

## Why This Matters

This topic is important because it helps you avoid common mistakes. For example, you may think you are working with a new value, but in reality, you are modifying the same object through another variable name.

## Understanding this helps with:

• lists and dictionaries
• function arguments
• copying data
• debugging strange behavior
• writing cleaner Python code

## Python and Function Arguments

Python passes arguments to functions by object reference. This means the function receives a reference to the same object.

If the object is mutable, the function may change it.
If the object is immutable, it cannot be changed in place.

This is why lists can be modified inside a function, while integers and strings usually cannot be changed in the same way.

## Goal of This Project

The main goal of this project is to deeply understand how Python works with:

• objects
• references
• assignment
• aliasing
• identity
• equality
• mutable and immutable types

By learning these concepts, you become better at predicting Python’s behavior and explaining why a program gives a certain result.

This knowledge is also very useful in technical interviews, because many Python questions are based on how objects and references behave.

## Conclusion

This project teaches that Python variables are not boxes that store values directly. They are names that point to objects. Once you understand that idea, it becomes much easier to understand mutation, copying, aliasing, and object identity.

In simple terms:

immutable objects do not change
mutable objects can change
variables store references
multiple variables can point to the same object

That is the foundation of how Python handles data.
