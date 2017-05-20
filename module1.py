#!/usr/bin/env python

# What happens when you import a module
# Module - contains Python defitions and statemetns
# spam.py  - 'spam' is the name of the module, available in global variable __name__

name = "BangPypers"
new_name = "Test"

# Module can contain executable statements and function definitions
# These are executed only once when the first time import is encountered
# Each module has its own private symbol table
# This symbole table is used as the global symbol table by all functions defined in the module
# Modules can import other modules.


print("This is getting executed in module1 only once at import time")


def my_function1():
    print("This is from my_function1")


def my_function2():
    print("This is from my_function2 - %s" % (name))


def my_function3():
    print("This is from my_function3 - %s" % (new_name))


#print("module1 Namespace:%s" % dir())
print("module1 Name:%s" % __name__)
