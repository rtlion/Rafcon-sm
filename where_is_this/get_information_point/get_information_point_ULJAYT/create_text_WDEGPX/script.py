
def execute(self, inputs, outputs, gvm):
    
    wpName = inputs['wpName']
    
    text = "The location point is now {}".format(wpName)
    
    outputs['text'] = text
    
    # text for going to location point
    ttsText = "Going now to the information point {}".format(wpName)
    
    outputs['ttsText'] = ttsText
    
    return 0
