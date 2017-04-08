from modules.module_base64 import Base64
from modules.module_urldecode import Urldecode

MODULES= [
    Base64(),
    Urldecode()
    ]

def match(val):
    for m in MODULES:
        yield m.match(input)
        
def numModules():
    return len(MODULES)
        
def getModuleName(id):
    if id < len(MODULES):
        return MODULES[id].name()
    else:
        return ""        
        
def matchModule(id, val):
    if id < len(MODULES):
        return MODULES[id].match(val)
    return None

def processModule(id, val):
    if id < len(MODULES):
        return MODULES[id].process(val)
    return "Module ID not found!"