from modules import *

MODULES= [
    module_base64.Module(),
    module_urldecode.Module(),
    module_htmldecode.Module(),
    module_request2requests.Module(),
    module_caesar.Module()
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
            score= module.match(data)
            if score > 1:
                score= 1
            if score <0:
                score= 0
            m["score"]= score
        except:
            m["score"]= 0
        res.append(m)
        
    return res