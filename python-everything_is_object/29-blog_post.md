## Python3: Mutable, Immutable… Everything Is Object!

## Introduction

When learning Python, one of the most confusing things for beginners is seeing that some values change “everywhere” while others do not. For example, changing an integer seems to create a new value, but changing a list can affect another variable unexpectedly. This happens because in Python, everything is an object, and variables do not store values directly. Instead, variables hold references to objects. 

Understanding this idea helps explain identity, assignment, mutability, function arguments, and many behaviors that often seem strange at first. In this article, I will explain the difference between mutable and immutable objects, how Python uses id() and type(), and why this matters when writing and debugging Python code.

## id and type
In Python, every object has an identity and a type. The identity of an object can be checked with id(), and the type of an object can be checked with type(). The id() function returns a unique identifier for an object during its lifetime, while type() tells us what kind of object it is.

a = 10
print(id(a))
print(type(a))

Example output:
140712193862096
<class 'int'>

Now let us try with a string:

s = "hello"
print(id(s))
print(type(s))

Example output:

140712193901104
<class 'str'>

And with a list:

l = [1, 2, 3]
print(id(l))
print(type(l))

Example output:
140712192145216
<class 'list'>

The exact numbers returned by id() may change from one machine to another, but the idea stays the same: each object has its own identity. Two variables can have the same value but still refer to different objects.

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
print(id(a))
print(id(b))

Output:

True
False
140712192145216
140712192144960

Here, a == b is True because both lists contain the same values. But a is b is False because they are two different objects in memory.

## Mutable objects

A mutable object is an object that can be changed after it is created. Common mutable built-in types in Python include:

list
dict
set

Let us look at a list example:

l = [1, 2, 3]
print(id(l))
l[0] = 99
print(l)
print(id(l))

Output:

140712192145216
[99, 2, 3]
140712192145216

The content of the list changed, but its id() stayed the same. That means Python modified the same object instead of creating a new one.
This becomes important when two variables refer to the same list:

l = [1, 2, 3]
m = l

print(m)
l[0] = 'x'
print(m)
print(l is m)
Output:
[1, 2, 3]
['x', 2, 3]
True

Both l and m point to the same list object, so changing the list through l also changes what m sees. This situation is called aliasing.

The same idea applies to dictionaries:
d1 = {"name": "Alice"}
d2 = d1

d1["name"] = "Bob"
print(d2)
Output:
{'name': 'Bob'}

Because dictionaries are mutable, both variables still refer to the same object after the change.

## Immutable objects

An immutable object is an object that cannot be changed after it is created. Common immutable built-in types include:
int
float
str
tuple
bool

Let us start with integers:

a = 5
print(id(a))
a = a + 1
print(a)
print(id(a))

Output:
140712193861936
6
140712193861968

The value changed from 5 to 6, but notice that the id() also changed. Python did not modify the old integer object. Instead, it created a new integer object and made a point to it.

The same idea applies to strings:

s = "cat"
print(id(s))
s = s + "s"
print(s)
print(id(s))

Output:

140712193900976
cats
140712193901168

Again, Python created a new object instead of changing the original string.

## Tuples are also immutable:

t = (1, 2, 3)
print(type(t))
Output:
<class 'tuple'>

You cannot do this:
t[0] = 99

Output:
TypeError: 'tuple' object does not support item assignment
This is because tuples cannot be modified after creation.

## Why does it matter and how differently does Python treat mutable and immutable objects

This matters because it affects how assignments work and how changes behave in a program. With immutable objects, changing a value usually means creating a new object. With mutable objects, changing a value often means modifying the same object in place.

## Compare these two examples.

First, immutable integers:
a = 1
b = a
a = 2

print(a)
print(b)
Output:
2
1

Why did b stay 1? Because when a = 2 happened, Python made a point to a new integer object. It did not change the object 1.
Now compare that with a mutable list:

l = [1, 2, 3]
m = l
l[0] = 100

print(l)
print(m)

Output:
[100, 2, 3]
[100, 2, 3]
This time both variables changed, because l and m point to the same mutable object.

This also explains the difference between == and is.
a = [1, 2]
b = [1, 2]
c = a

print(a == b)
print(a is b)
print(a is c)

Output:
True
False
True

a == b checks value equality.
a is b checks identity.

a is c is True because c is just another reference to the same object as a.
When working with mutable objects, it is often safer to create copies when needed.

original = [1, 2, 3]
copy = original.copy()

original[0] = 99

print(original)
print(copy)
print(original is copy)

Output:
[99, 2, 3]

[1, 2, 3]

False

This creates a new list object, so changing one does not affect the other.
How arguments are passed to functions and what that implies for mutable and 

## immutable objects

Python passes arguments to functions by object reference. This means the function receives a reference to the same object that was passed in. What happens next depends on whether the object is mutable or immutable.

## Let us start with an immutable object:

def add_one(x):
    x = x + 1
    print("Inside function:", x)

n = 5
add_one(n)
print("Outside function:", n)

Output:

Inside function: 6
Outside function: 5

Inside the function, x was reassigned to a new integer object. This did not affect n outside the function.

## Now let us try a mutable object:

def change_list(my_list):
    my_list[0] = 99
    print("Inside function:", my_list)

numbers = [1, 2, 3]
change_list(numbers)
print("Outside function:", numbers)

Output:

Inside function: [99, 2, 3]
Outside function: [99, 2, 3]

The function changed the list in place, so the original list outside the function was also modified.

However, if we reassign the parameter itself inside the function, that does not change the original reference outside:

def reassign_list(my_list):
    my_list = [7, 8, 9]
    print("Inside function:", my_list)

numbers = [1, 2, 3]
reassign_list(numbers)
print("Outside function:", numbers)

## Output:

Inside function: [7, 8, 9]
Outside function: [1, 2, 3]

Here, the function parameter my_list was made to point to a new list, but the original numbers variable outside the function still points to the old list.

## So the key idea is:

If a function modifies a mutable object, the change is visible outside.
If a function reassigns its parameter, the outside variable is not affected.
With immutable objects, “changes” usually create new objects, so the original object outside stays the same.

## What I learned from the advanced tasks

From the advanced tasks, I understood more clearly that copying and aliasing are not the same thing. For example, if I do:
a = [1, 2, 3]
b = a

then b is only another name for the same object. But if I do:
a = [1, 2, 3]
b = a.copy()

then b is a new list object with the same values. That is why:

print(a == b)
print(a is b)
gives:
True
False

I also learned that tuples are immutable, but they can contain mutable objects inside them:

t = ([1, 2], 3)

t[0].append(99)

print(t)

Output:
([1, 2, 99], 3)

The tuple itself did not change structure, but the list inside it was mutable and could still be modified. This was an important detail because it showed me that immutability can depend on what is inside an object as well.

## Conclusion

This project helped me understand that Python variables are not boxes storing values directly. They are names pointing to objects in memory. Once I understood that, many confusing behaviors became much clearer. Mutable objects can be changed in place, which means aliases can see the same modification. Immutable objects cannot be changed, so Python creates new objects instead. This also explains why function behavior depends so much on the type of object passed in. In short, understanding objects, identity, mutability, and references is essential for writing correct Python code and for explaining Python clearly in interviews or real projects.
Image idea for the top of your post
Put a simple diagram at the top showing this:
a = [1, 2, 3]
b = a
both arrows pointing to the same list object
then a[0] = 99
both a and b show the changed list
