
def execute(self, inputs, outputs, gvm):
    
    databaseList = inputs['databaseList']
    
    if len(databaseList) < 1:
        return "notNeoughData"
    else:
        for human in databaseList:
            if human['name']:
                return "notNeoughData"
        return "enoughData"