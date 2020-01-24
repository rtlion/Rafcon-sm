import rospy
import os
import sys
import yaml

with open(os.path.expanduser("~/.config/rafcon/config.yaml")  , 'r') as stream:
    yamlData = yaml.safe_load(stream)
    rafconLibPath = yamlData['LIBRARY_PATHS']['rtl_rafcon_lib']
    sys.path.insert(1, rafconLibPath)
    
from externalScripts import location2ascii

def execute(self, inputs, outputs, gvm):
    self.logger.debug("Generate way description")
    
    locate = location2ascii.location()
    info = inputs['start']
    self.logger.debug(info)
    target = inputs['target']
    try:
        loc = locate.find_path(info, target)
    except:
        loc = "Sorry, I don't know that route by heart. Let's go together."
    self.logger.info(loc)
    outputs['description'] = loc
    return 0
