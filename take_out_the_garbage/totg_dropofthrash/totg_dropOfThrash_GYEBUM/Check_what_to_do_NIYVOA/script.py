
def execute(self, inputs, outputs, gvm):
    
    thrashOnArm = inputs['thrashOnArm']
    thrashOnBack = inputs['thrashOnBack']
    
    self.logger.info("Thrash on Arm: {}".format(thrashOnArm))
    self.logger.info("Trhash on Back: {}".format(thrashOnBack))
    
    # this gets returned later
    nextStep = "" 
    
    if thrashOnArm: 
        nextStep = "dropThrash"
        thrashOnArm = False
    
    elif thrashOnBack:
        nextStep = "getThrashFromBack"
        thrashOnBack = False
        
    else:
        nextStep = "Finish"
    
    
    outputs['thrashOnArm'] = thrashOnArm
    outputs['thrashOnBack'] = thrashOnBack
    
    self.logger.info("Next step is: {}".format(nextStep))
    return nextStep
