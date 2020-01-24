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
    self.logger.debug("Hello world")
    
    locate = location2ascii.location()
    loc = locate.find_path('shelf', 'couch')
    self.logger.info(loc)
    return 0
