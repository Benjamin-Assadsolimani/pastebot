from base64 import b64decode
from re import compile

class Base64():
    def name(self):
        return "Base64-Decode";
    
    def match(self, input):
        res= self.matchb64(input)
        if res != None:
            return 1
        else:
            return 0
    
    def process(self, input):
        try:
            return b64decode(input.encode("utf8"))
        except:
            return "invalid base64!"
        
    
    def matchb64(self, input):
        prog= compile("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$")
        res= prog.match(input)
        return res
        
        
    def test(self):
        pass


if __name__ == "__main__":
    m= Base64()
    m.test()