###############################
#       HTML Decode           #
###############################
from __future__ import division
import HTMLParser

class Module():
    def name(self):
        return "HTML-Decode";
    
    #@input string 
    #@return match index [0, 1] indicating how well the input matches the module
    def match(self, text):
        score= (text.count('&')+text.count(';'))/(len(text)+1)
        score*=5
        return score
    
    #@input string
    #@return the processed user input
    def process(self, text):
        try:
            parser = HTMLParser.HTMLParser()
            return parser.unescape(text)
        except:
            return "HTMLParser error!"
    
    
    #self-testing
    def test(self):
        pass

if __name__ == "__main__":
    m= Module()
    m.test()