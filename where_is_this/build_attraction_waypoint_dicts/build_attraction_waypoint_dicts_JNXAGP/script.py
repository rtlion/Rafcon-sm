

"""
waypoints = {'gus_bedroom': 1, # gegen Uhrzeigersinn
             'gus_bedroom chest': 2,
             'gus_door to office': 3,
             'gus_office': 4,
             ...
             }
"""
import os
import yaml
import sys

with open(os.path.expanduser("~/.config/rafcon/config.yaml")  , 'r') as stream:
    yamlData = yaml.safe_load(stream)
    rafconLibPath = yamlData['LIBRARY_PATHS']['rtl_rafcon_lib']
    sys.path.insert(1, rafconLibPath)
    
from externalScripts import whereisthis_dict
attraction_name_to_waypoint_id = whereisthis_dict.waypoints

attraction_name_to_tourguide_info = {
        "bedroom": {
            "clockwise" : "We are now in the bedroom.",
            "counterclockwise" : "We are now in the bedroom."
        },
        "bedroom chest": {
            "clockwise" : "We are passing the bedroom chest on our right.",
            "counterclockwise" : "We are passing the bedroom chest on our left."
        },
        "door to office" : {
            "clockwise" : "We are going through the door to the office.",
            "counterclockwise" : "We are going through the door to the office."
        },
        "office": {
            "clockwise" : "We are now in the office. We turn to the right.",
            "counterclockwise" : "We are now in the office. We turn to the left."
        },
        "localization point" : {
            "clockwise" : "I have reached the localization point",
            "counterclockwise" : "I have reached the localization point"
        },
        "door to office" : {
            "clockwise" : "We are going through the door to the living room.",
            "counterclockwise" : "We are going through the door to the living room."
        },
        "trash bin": {
            "clockwise" : "We are passing the trash bin on our right.",
            "counterclockwise" : "We are passing the trash bin on our right."
        },
        "living room": {
            "clockwise" : "We are now in the living room. We turn to the right.",
            "counterclockwise" : "We are now in the living room. We turn to the left."
        },
        "sideboard": {
            "clockwise" : "We are passing the side board with drinks on our left.",
            "counterclockwise" : "We are passing the side board with drinks on our right."
        },
        "hallway to kitchen": {
            "clockwise" : "We are going down the hallway to the kitchen.",
            "counterclockwise" : "We are going down the hallway to the kitchen."
        },
        "kitchen": {
            "clockwise" : "We are now in the kitchen. We turn to the right.",
            "counterclockwise" : "We are now in the kitchen. Follow me through the hallway to the living room."
        },
        "hallway to living room": {
            "clockwise" : "We are going down the hallway to the living room.",
            "counterclockwise" : "We are going down the hallway to the living room."
        }
    }

def execute(self, inputs, outputs, gvm):

    global attraction_name_to_tourguide_info

    driving_waypoints = inputs["driving_waypoints"]
    
    clockwise_driving_points = {}
    counterclockwise_driving_points = {}
    attraction_viewpoints = {}
    for attraction_name in attraction_name_to_waypoint_id:
        is_clockwise = attraction_name.startswith("gus_")
        is_counterclockwise = attraction_name.startswith("uzs_")

        waypoint_id = attraction_name_to_waypoint_id[attraction_name]
        waypoint_poseStamped = driving_waypoints[waypoint_id]

        if is_clockwise:
            attraction_name_cleaned = attraction_name[4:]
            clockwise_driving_points[attraction_name_cleaned] = {}
            clockwise_driving_points[attraction_name_cleaned]["poseStamped"] = waypoint_poseStamped
            clockwise_driving_points[attraction_name_cleaned]["tourguide_info"] = attraction_name_to_tourguide_info[attraction_name]["clockwise"]
            continue
        
        if is_counterclockwise:
            attraction_name_cleaned = attraction_name[4:]
            counterclockwise_driving_points[attraction_name_cleaned]
            counterclockwise_driving_points[attraction_name_cleaned]["poseStamped"] = waypoint_poseStamped
            counterclockwise_driving_points[attraction_name_cleaned]["tourguide_info"] = attraction_name_to_tourguide_info[attraction_name]["counterclockwise"]
            continue
        
        # neither cw nor ccw --> attraction_viewpoint
        attraction_viewpoints[attraction_name] = {}
        attraction_viewpoints[attraction_name]["poseStamped"] = waypoint_poseStamped
        attraction_viewpoints[attraction_name]["tourguide_info"] = "Here is the %s" % attraction_name

    """
    attraction_name_to_tourguide_dict structure: (dummy example data)
    {
        "dishwasher": {
            "poseStamped": PoseStamped,
            "tourguide_info": "We are passing the dishwasher to our right"
        },
        "fridge": {
            "poseStamped": PoseStamped,
            "tourguide_info": "To the right you can see the fridge."
        }
    }
    """
    outputs["attraction_dict"] = attraction_viewpoints
    outputs["clockwise_attraction_dict"] = clockwise_driving_points
    outputs["counterclockwise_attraction_dict"] = counterclockwise_driving_points
    
    return 0
