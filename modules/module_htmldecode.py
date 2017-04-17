#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################
#          HTML DECODER           #
# author: derbenoo                #
###################################

from __future__ import division
import HTMLParser
import re

class Module():
    def __init__(self):
        self.parser= HTMLParser.HTMLParser()
        self.regex = re.compile(r'&(([a-zA-Z]{2,10})|(#[\d]{1,5}));')
    
    def name(self):
        return "HTML-Decoder";
    
    def match(self, text):
        matches= self.regex.finditer(text)
        count= 0
        for match in matches:
            count+= match.end()-match.start()
        all= len(text) if len(text) > 0 else 1
        
        return (count/all)

    def process(self, text):
        try:
            return self.parser.unescape(text)
        except:
            return text
    
    def test(self):
        testvectors=[
            [0, ""],
            [1, "&#0;&#11;&#222;&#3333;&#44444;&gt;&test;&maxlenhere;"],
            [0, "&#000000;&0;&gmaxlenhere;&#gt;&#;&gt1;&#0#00;"],
            [1, "&#49;&#049;&#0049;&#00049;&gt;&lt;&amp;", "1111><&"]
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
    print("Running tests for module "+m.name()+": ")
    m.test()