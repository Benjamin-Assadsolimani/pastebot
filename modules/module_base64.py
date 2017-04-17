#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################
#         BASE64 DECODER          #
# author: derbenoo                #
###################################

from __future__ import division
from base64 import b64decode
import re

class Module():
    def __init__(self):
        self.regex= re.compile(r"([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)")
        
    def name(self):
        return "Base64-Decode";
    
    def match(self, text):
        matches= self.regex.finditer(text)
        count= 0
        for match in matches:
            count+= match.end()-match.start()
        all= len(text) if len(text) > 0 else 1
        return (count/all)
        
    
    def process(self, text):
        text= text.encode("utf8")
        return self.regex.sub(self.convert, text)
    
    def convert(self, matchobj):
        text= matchobj.group(0)    
        try:
            return b64decode(text)
        except:
            return text
        
    def test(self):
        testvectors= [
            [0  , "", ""],
            [0.9, r"dGVzdHRlc3R0ZXN0 dGVzdHRlc3Q= dGVzdA==", "testtesttest testtest test"],
            [0  , r"abc a=== ==== abc ab ===+ ==++ =+++ abc%abc&abc$abc(abc)abc.abc:abc*abc'abc;abc{abc}abc§abc!abc^"],
            [1  , r"dA==dGU=dA==dGVzdA==dGVzdHQ=", "ttettesttestt"],
            [0.9,  "dGVzdA==\ndGVzdA==\rdGVzdA==", "test\ntest\rtest"]
            ]
        
        for i, vector in zip(range(len(testvectors)), testvectors):
            score= self.match(vector[1])
            score= round(score, 1)
            if score != vector[0]:
                print("Test vector "+str(i)+" "+str(vector)+" failed! (score: "+str(score)+")")
                continue
            
            if len(vector) > 2:
                res= self.process(vector[1])
                if res != vector[2]:
                    print("Test vector "+str(i)+" "+str(vector)+" failed! (processed: "+repr(res)+")")
                    continue
            
            print("Test vector "+str(i)+" passed.")


if __name__ == "__main__":
    m= Module()
    print("Running tests for module "+m.name()+":")
    m.test()