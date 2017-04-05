from base64 import b64decode
from re import compile, findall, match
import binascii

def match(input):
    res= matchb64(input)
    if res != None:
        #check how much of total string is base64
        return 1
    else:
        return 0

def process(input):
    try:
        return b64decode(input)
    except:
        return "invalid base64!"
    

def matchb64(input):
    prog= compile("([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)")
    res= prog.match(input)
    return res
    
    
def test():
    pass


if __name__ == "__main__":
    test()