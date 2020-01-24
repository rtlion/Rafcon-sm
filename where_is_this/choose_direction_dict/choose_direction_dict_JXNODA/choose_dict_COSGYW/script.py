
def execute(self, inputs, outputs, gvm):
    
    cw_dict = inputs["cw_dict"]
    ccw_dict = inputs["ccw_dict"]
    direction = inputs["direction"]
    
    chosen_dict = cw_dict if direction == "clockwise" else ccw_dict
    
    outputs["ccw_or_cw_dict"] = chosen_dict
    self.logger.debug("chosen dict {0}".format(chosen_dict))
    
    return 0
