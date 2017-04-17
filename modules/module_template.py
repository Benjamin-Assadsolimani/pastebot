#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################
#         MODULE TEMPLATE         #
# author:                         #
###################################

class Module():
    #Initialize module e.g. compiling regular expressions
    def __init__(self):
        pass
    
    #Name of the module
    def name(self):
        return "module name";
 
    #Computes and returns a match index [0, 1] indicating how well the input matches the module
    def match(self, text):
        return 0
    
    #Process input and return result
    def process(self, text):
        return text
    
    #Self-testing
    def test(self):
        pass

if __name__ == "__main__":
    m= Module()
    print("Running tests for module "+m.name()+": ")
    m.test()