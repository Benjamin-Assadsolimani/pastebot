#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################
#         MODULE URLSCAN          #
# author: derbenoo                #
###################################

import re
import requests

class Module():
    def __init__(self):
        self.regexURL           = re.compile(r'^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$')
        self.regexHTMLComment   = re.compile(r'<!--.*-->')
        self.locations          = ["robots.txt", "admin", "cgi-bin", "login", "img", "upload", "include"]
        self.timeout            = 0.4
        
    def name(self):
        return "URL-Scan";
 
    def match(self, text):
        if self.regexURL.match(text):
            return 1
        return 0
    
    #Process input and return result
    def process(self, url):
        if url[:-1] != "/":
            url+= "/"
        
        res= []
        
        #check if locations exist
        for location in self.locations:
            r= requests.head(url+location, timeout= self.timeout, verify= False)
            res.append(location+": "+str(r.status_code))
        
        #check main page for HTML comments
        r= requests.get(url, timeout= self.timeout, verify= False)
        
        numComments= len(self.regexHTMLComment.findall(r.text))
        res.append("HTML comments: "+str(numComments))
        
        return '\n'.join(res)
    
    #Self-testing
    def test(self):
        pass

if __name__ == "__main__":
    m= Module()
    print("Running tests for module "+m.name()+": ")
    m.test()