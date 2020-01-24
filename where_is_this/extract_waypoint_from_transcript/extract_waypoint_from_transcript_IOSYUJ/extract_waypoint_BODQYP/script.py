
def execute(self, inputs, outputs, gvm):
    
    saidPosition = inputs['saidPosition']
    
    objects = inputs['objects']
    categories = inputs['categories']
    
    keyword2Name = inputs['keyword2name']
    
    waypointsDict = inputs['waypoints']
    
    
    wp = None # is a int
    
    # check if it's a object
    if saidPosition in objects.keys():
        self.logger.info("{} in objects".format(saidPosition))
    
        for semanticWp, category in categories.items():
            if str(category.lower()) == str(objects[saidPosition].lower()):
                self.logger.info("{} in {}".format(objects[saidPosition], category))
                self.logger.info("Searching for {} in waypoints  dict".format(semanticWp))
                wp = waypointsDict[semanticWp]
                
        if wp is None:
            self.logger.warning("Detected unknown position {}".format([objects[saidPosition]]))
            return "nothingFound"
        
    elif saidPosition in categories.keys():
        wp = waypointsDict.get(saidPosition,None)
    
    else:
        # nothing found
        self.logger.warning("Detected unknown position {} in dict: {}".format(saidPosition, waypointsDict))
        return "nothingFound"
    
    
    
    
    if wp is None:
        wp = waypointsDict['localization']
        
    
    textStr = "The {pos} is at waypoint {wp}".format(pos = saidPosition, wp = wp)
    self.logger.info(textStr)
    
    #if saidPosition in keyword2Name:
    #    saidPosition = keyword2Name[saidPosition]
        
    outputs['waypointName'] = str(saidPosition)
    
    outputs['waypoint'] = int(wp)
    
    
    
    return "success"
    
