#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################
#          CAESAR CIPHER          #
# author: derbenoo                #
###################################

from __future__ import division
import string
import re

class Module():
    def __init__(self):
        pass
    
    def name(self):
        return "Caesar-Cipher";
    
    def match(self, text):
        score= len(re.findall('[a-zA-z]', text))/len(text)
        return score

    def process(self, text):
        return self.shiftAll(text)
    
    def shift(self, cipher, shift=[1]):
        res= ""
        for i in range(0, len(cipher)):
            if cipher[i] in string.ascii_lowercase:
                alphabet= string.ascii_lowercase
            elif cipher[i] in string.ascii_uppercase:
                alphabet= string.ascii_uppercase
            else:
                res+= cipher[i]
                continue
            
            pos= alphabet.index(cipher[i])
            pos= pos+shift[i%len(shift)]
            pos= pos%len(alphabet)
            res+= alphabet[pos]
        return res
    
    
    def shiftAll(self, cipher, key= [-1]):
        res= []
        for i in xrange(1, 26):
            cipher= self.shift(cipher, key)
            res.append("[-"+str(i)+"] "+cipher)
        
        return '\n'.join(res)
    

    def test(self):
        pass

if __name__ == "__main__":
    m= Module()
    print("Running tests for module "+m.name()+": ")
    m.test()