import module_base64
import module_urldecode

MODULES= [
    module_base64.Base64(),
    module_urldecode.Urldecode()
    ]

def getModule(module_id):
    if module_id < len(MODULES):
        return MODULES[module_id]
    return None

def match(data):
    res= []
    for id, module in zip(range(len(MODULES)), MODULES):
        m= {}
        m["name"]= module.name()
        m["module_id"]= id
        m["content"]= ""
        try:
            m["score"]= module.match(data)
        except:
            m["score"]= 0
        res.append(m)
        
    return res