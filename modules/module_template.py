###############################
#       MODULE TEMPLATE       #
###############################

#@return category of the module as a string (just for display purposes)
def category():
    return "general"

#@input string 
#@return match index [0, 1] indicating how well the input matches the module
def match(input):
    return 0

#@input string
#@return the processed user input
def process(input):
    return input


#self-testing
def test():
    pass

if __name__ == "__main__":
    test()