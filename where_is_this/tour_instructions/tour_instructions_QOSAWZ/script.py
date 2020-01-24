import os
import yaml
import sys

with open(os.path.expanduser("~/.config/rafcon/config.yaml")  , 'r') as stream:
    yamlData = yaml.safe_load(stream)
    rafconLibPath = yamlData['LIBRARY_PATHS']['rtl_rafcon_lib']
    sys.path.insert(1, rafconLibPath)
    
from externalScripts import location2ascii

def execute(self, inputs, outputs, gvm):
    infoPoint = inputs['infoPoint']
    target = inputs['target']
    loc = location2ascii.location()
    try:
        description = loc.find_path(infoPoint, target)
    except KeyError:
        outputs['description'] = ""
        self.logger.warn("Invalid Waypoints")
        return "invalidWaypoints"
    outputs['description'] = description
    self.logger.info("Description is: {}".format(description))
    return 0
