
import math

SOMETHING_NEW = 1
NOTHING_NEW = 1

def is_in_visiting_range(attraction_poseStamped, robot_poseStamped, max_visiting_distance):
    x1 = attraction_poseStamped.pose.position.x
    y1 = attraction_poseStamped.pose.position.y

    x2 = robot_poseStamped.pose.position.x
    y2 = robot_poseStamped.pose.position.y

    euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    should_be_visited = (euclidean_distance <= max_visiting_distance)

    return should_be_visited


def execute(self, inputs, outputs, gvm):
    global SOMETHING_NEW, NOTHING_NEW

    # params
    max_visiting_distance = inputs["max_visiting_distance"]

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
    attraction_name_to_tourguide_dict = inputs["attraction_name_to_tourguide_dict"]
    robot_poseStamped = inputs["robot_poseStamped"]
    unvisited_attractions = inputs["unvisited_attractions"]
    # initialization for first time
    if unvisited_attractions is None:
        for attraction_name in attraction_name_to_tourguide_dict:
            unvisited_attractions.append(attraction_name)

    # cycle through all attractions and check only unvisited ones for visiting range
    for attraction_name in attraction_name_to_tourguide_dict:

        # already visited
        if attraction_name not in unvisited_attractions:
            continue
        
        # not visited yet
        attraction_entry = attraction_name_to_tourguide_dict[attraction_name]
        attraction_poseStamped = attraction_entry["poseStamped"]
        if is_in_visiting_range(attraction_poseStamped, robot_poseStamped, max_visiting_distance):
            # get tourguide info and set it as output
            attraction_description = attraction_entry["tourguide_info"]
            outputs["attraction_info"] = attraction_description

            # update unvisited locations
            unvisited_attractions.remove(attraction_name)
            outputs["unvisited_attractions"] = unvisited_attractions
            return SOMETHING_NEW

    # output unchanged unvisited attractions
    outputs["unvisited_attractions"] = unvisited_attractions
    return NOTHING_NEW
