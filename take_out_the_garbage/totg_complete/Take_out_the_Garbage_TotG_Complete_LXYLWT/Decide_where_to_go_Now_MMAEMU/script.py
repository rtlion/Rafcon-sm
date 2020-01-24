"""
A bit complex but (IMO) a good handling of where we go to, to have a strucuterd state machine
"""

def execute(self, inputs, outputs, gvm):

    binList = inputs['binList'] # list
    currentBin = inputs['currentBin'] # int

    thrashOnArm = inputs['thrashOnArm'] # bool
    thrashOnBack = inputs['thrashOnBack'] # bool
    storeOnBack = inputs['storeOnBack'] # bool
    
    nextStep = "" # The value which gets returned


    if thrashOnArm:
        if storeOnBack and not thrashOnBack:
            # thrash in arm, but we are allowd (or should) store it on the back
            
            if len(binList) == 0:
                # no need to store, if this is the last thrash we gonna pick up
                nextStep = "DropOffThrash"
                
            else:
                # store the bin on the back 
                nextStep = "StoreBin"
                
        elif thrashOnBack:
            # thrash on the back and on the hand -> drop both off
            nextStep = "DropOffThrash"
            
        else:
            # thrash on the arm  and not allowed to store on the back -> drop off
            nextStep = "DropOffThrash"

    else: # no thrash on the arm
    
        if len(binList) == 0: # check if there a bins we still have to go
            # no bins to go
            if thrashOnBack:
                nextStep = "DropOffThrash"
            
            nextStep = "Finish"
        
        else:
            currentBin = binList[0] # get next bin location from the list
            binList.pop(0) # pop the bin from the list (because we are going there now)
            nextStep = "goToBin"

    outputs['currentBin'] = currentBin
    outputs['binList'] = binList

    self.logger.info("Next step is: {} - currentBin: {}".format(nextStep, currentBin))
    return nextStep