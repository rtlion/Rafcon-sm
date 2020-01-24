
def execute(self, inputs, outputs, gvm):
    
    degreesTurned = inputs['degreeDrove']
    
    degreesTurned += 45
    
    if degrees >= 320:
        return "turnedEnough"
        
    return "keepSpinning"