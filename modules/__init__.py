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