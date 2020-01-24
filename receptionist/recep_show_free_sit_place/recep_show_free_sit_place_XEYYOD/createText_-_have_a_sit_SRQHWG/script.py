
def execute(self, inputs, outputs, gvm):
    
    name = inputs['name']
    
    text = "{name}, please have a seat over there".format(name = name)
    
    outputs['text'] = text
    
    return "success"
