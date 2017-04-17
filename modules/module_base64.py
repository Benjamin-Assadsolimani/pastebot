from __future__ import division
from base64 import b64decode
import re

class Module():
    def __init__(self):
        self.regex= re.compile("([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)")
        
    def name(self):
        return "Base64-Decode";
    
    def match(self, text):
        matches= self.regex.finditer(text)
        count= 0
        for match in matches:
            count+= match.end()-match.start()
        
        return (count/len(text))
        
    
    def process(self, text):
        text= text.encode("utf8")
        return self.regex.sub(self.convert, text)
    
    def convert(self, matchobj):
        text= matchobj.group(0)    
        try:
            return b64decode(text)
        except:
            return text
        
    def test(self):
        pass


if __name__ == "__main__":
    m= Module()
    m.test()