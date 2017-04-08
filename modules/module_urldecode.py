###############################
#       URL DECODE            #
###############################
from urllib import unquote

class Urldecode():
    def name(self):
        return "URL-Decode";
    
    #@return category of the module as a string (just for display purposes)
    def category(self):
        return "general"
    
    #@input string 
    #@return match index [0, 1] indicating how well the input matches the module
    def match(self, input):
        return 0.5
    
    #@input string
    #@return the processed user input
    def process(self, input):
        return input
    
    
    #self-testing
    def test(self):
        pass

if __name__ == "__main__":
    m= Urldecode()
    m.test()