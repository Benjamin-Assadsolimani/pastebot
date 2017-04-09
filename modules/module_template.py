###############################
#       MODULE TEMPLATE       #
###############################

class Module():
    def name(self):
        return "name";
    
    #@return category of the module as a string (just for display purposes)
    def category(self):
        return "general"
    
    #@input string 
    #@return match index [0, 1] indicating how well the input matches the module
    def match(self, text):
        return 0
    
    #@input string
    #@return the processed user input
    def process(self, text):
        return input
    
    
    #self-testing
    def test(self):
        pass

if __name__ == "__main__":
    m= Module()
    m.test()