###############################
#       URL DECODE            #
###############################
from __future__ import division
from urllib import unquote
import re

class Module():
    def name(self):
        return "URL-Decode";
    
    #@input string 
    #@return match index [0, 1] indicating how well the input matches the module
    def match(self, text):
        errors= len(re.findall('[^#:\-%./a-zA-z0-9]', text))
        matches= len(re.findall('%[A-F0-9][A-F0-9]', text))*3-errors
        score= matches/(len(text)+1)
        score*=3
        return score
    
    #@input string
    #@return the processed user input
    def process(self, text):
        try:
            return unquote(text)
        except:
            return "urllib.unquote error"
    
    #self-testing
    def test(self):
        pass

if __name__ == "__main__":
    m= Module()
    m.test()