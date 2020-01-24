import rospy
import rtl_comm.srv

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def execute(self, inputs, outputs, gvm):
    
    # names we can search for
    
    # TEST DICT - TODO IMPORT FILE
    categoriesDict = inputs['dictCategories']
    objectsDict = inputs['dictObjects']
    
    positionsDict = merge_two_dicts(categoriesDict, objectsDict)
    
    
    positionsDict = positionsDict.keys()
    
    transcript = inputs['transcript']
    #sample = "Hello my Name is John and my favoriture drink is Beer"
    
    self.logger.info("Extracting position: {}".format(transcript))
    end = rospy.ServiceProxy('nlp/end', rtl_comm.srv.namesAndDrinks)
    data = end(transcript, positionsDict, [])
    
    names = data.names
    #drinks = data.drinks
    
    self.logger.info("positions: {}".format(names))
    
    # remove duplicate
    newNames = []
    
    for name in names:
        if name not in newNames:
            newNames.append(name)
            break
    
    
    if names is None or len(names) == 0:
        return "nothing"
    
    else:
        self.logger.info("Returning {}".format(names[0]))
        outputs['guidePos'] = names[0]
        return "success"
        
