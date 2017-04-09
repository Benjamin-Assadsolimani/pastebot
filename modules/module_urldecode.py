###############################
#       URL DECODE            #
###############################
from __future__ import division
from urllib import unquote

class Urldecode():
    def name(self):
        return "URL-Decode";
    
    #@input string 
    #@return match index [0, 1] indicating how well the input matches the module
    def match(self, text):
        score= text.count('%')/len(text)
        score*=3
        if score > 1:
            score= 1
            
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
    m= Urldecode()
    m.test()