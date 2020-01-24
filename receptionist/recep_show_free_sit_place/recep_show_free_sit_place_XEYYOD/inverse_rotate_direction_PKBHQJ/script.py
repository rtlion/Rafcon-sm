
def execute(self, inputs, outputs, gvm):
    
    inputDirection = inputs['direction'].lower()

    if inputDirection == "right":
        outputs['direction'] = "left"
        
    elif inputDirection == "left":
        outputs['direction'] = "right"
        
    else:
        self.logger.error("Input direction has to be right or left!")
        return "aborted"
    
    return "success"
