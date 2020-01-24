
def execute(self, inputs, outputs, gvm):
    
    name = inputs['name']
    
    text = "{}, can you please follow me now".format(name)
    
    outputs['text'] = text
    
    return "success"