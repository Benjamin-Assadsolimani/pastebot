from modules import *

MODULES= [
    module_base64.Module(),
    module_urldecode.Module(),
    module_htmldecode.Module()
    ]

def getModule(module_id):
    if module_id < len(MODULES):
        return MODULES[module_id]
    return None

def match(data):
    res= []
    for module_id, module in zip(range(len(MODULES)), MODULES):
        m= {}
        m["name"]= module.name()
        m["module_id"]= module_id
        m["content"]= ""
        try:
            m["score"]= module.match(data)
        except:
            m["score"]= 0
        res.append(m)
        
    return res