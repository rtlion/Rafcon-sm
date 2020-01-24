WAYPOINT_ORDER_CLOCKWISE = [
    "island",
    "fridge",
    "dishwasher",
    "cabinet",
    "sink",
    "kitchen",
    "table",
    "display",
    "tv",
    "sideboard",
    "living",
    "armchair",
    "plant",
    "coffee",
    "couch",
    "trash",
    "bin",
    "desk",
    "shoe",
    "safe",
    "coat",
    "localization",
    "office", #bedroom chest missing?
    "chest",
    "bedroom",
    "side",
    "bed",
    "shelf"
]

def execute(self, inputs, outputs, gvm):
    global WAYPOINT_ORDER_CLOCKWISE
    
    start = inputs["start"]
    target = inputs["target"]
    
    self.logger.debug("tourguide: start point is %s" % start)
    self.logger.debug("tourguide: target point is %s" % start)
    
    start_index = WAYPOINT_ORDER_CLOCKWISE.index(start)
    target_index = WAYPOINT_ORDER_CLOCKWISE.index(target)
    
    direction = "clockwise" if start_index <= target_index else "counterclockwise"
    
    outputs["direction"] = direction
    self.logger.debug("tourguide: direction is %s" % direction)
    
    return 0
