#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################
#           URL DECODER           #
# author: derbenoo                #
###################################

from __future__ import division
from urllib import unquote
import re

class Module():
    def __init__(self):
        self.regex= re.compile(r'%[A-F0-9]{2}')
        
    def name(self):
        return "URL-Decoder";
    
    def match(self, text):
        matches= len(self.regex.findall(text))*3
        score= matches/(len(text)+1)
        score*=3
        return score
    
    def process(self, text):
        try:
            return unquote(text)
        except:
            return text
    
    def test(self):
        pass

if __name__ == "__main__":
    m= Module()
    print("Running tests for module "+m.name()+": ")
    m.test()