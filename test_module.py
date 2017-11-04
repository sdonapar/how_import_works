#!/usr/bin/env python

module_name = "test_module"

print("This is getting executed in test_module")

def test_function():
    print("This is from test_function - %s" % (module_name))
