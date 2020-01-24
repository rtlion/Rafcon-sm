import rosservice


def execute(self, inputs, outputs, gvm):
    self.logger.info("Checking ros services")
    
    # check services
    servicesToCheck = ['/tts/speak',
                       '/stt_google',
                       '/nlp/yesno',
                       '/nlp/general']
    
    serviceList = rosservice.get_service_list()
    
    serviceNotFound = False
    
    for service in servicesToCheck:
        if service not in serviceList:
            self.logger.info("Service not found: {}".format(service))
            serviceNotFound = True
            
        
    # check topics
    # todo
    
    if serviceNotFound is True:
        return -1
    else:
        self.logger.info("All services were found!")
        return 0