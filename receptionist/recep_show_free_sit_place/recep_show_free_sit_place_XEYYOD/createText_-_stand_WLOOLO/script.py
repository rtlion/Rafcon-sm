
def execute(self, inputs, outputs, gvm):
    
    name = inputs['name']
    
    text = "{name}, I'm sry but there is no more space left! You have to stand.".format(name = name)
    
    outputs['text'] = text
    
    return "success"
