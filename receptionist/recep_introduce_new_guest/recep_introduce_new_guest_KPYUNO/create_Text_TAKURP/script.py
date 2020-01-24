
def execute(self, inputs, outputs, gvm):
    
    name = inputs['name']
    personsDict = inputs['personsDict']
    
    drink = personsDict[name]['drink']
    
    try:
        gender = personsDict[name]['gender']
        
        if gender == "m":
            genderWord = "his"
        else:
            genderWord = "her"
            
    except KeyError as e:
        self.logger.warning("Person '{}' has no assigned gender!")
        genderWord = "his"
        
    
    text = "This is {name}, and {gender} favourite drink is {drink}".format(name = name,
                                                                            gender = genderWord,
                                                                            drink = drink)
    
    
    outputs['text'] = text
    
    return "success"
