EXCEPTIONS


Python uses special objects called exceptions to manage errors that arise dur-
ing a program’s execution. Whenever an error occurs that makes Python
unsure what to do next, it creates an exception object.

If you write code that handles the exception, the program will continue running. If you don’t
handle the exception, the program will halt and show a traceback, which
includes a report of the exception that was raised.

Exceptions are handled with try-except blocks. A try-except block asks
Python to do something, but it also tells Python what to do if an excep-
tion is raised. When you use try-except blocks, your programs will continue
running even if things start to go wrong. Instead of tracebacks, which can
be confusing for users to read, users will see friendly error messages that
you write.
