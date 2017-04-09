from __future__ import division
from base64 import b64decode
import re

class Module():
    def name(self):
        return "Base64-Decode";
    
    def match(self, text):
        res= self.matchb64(text)
        if res != None:
            return 1
        else:
            return 0
    
    def process(self, text):
        try:
            return b64decode(text.encode("utf8"))
        except:
            return "invalid base64!"
        
    
    def matchb64(self, text):
        prog= re.compile("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$")
        res= prog.match(text)
        return res
        
        
    def test(self):
        pass


if __name__ == "__main__":
    m= Module()
    m.test()