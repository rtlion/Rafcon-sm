
def execute(self, inputs, outputs, gvm):
    
    
    dbHandler = gvm.get_variable(inputs["dbHandle"], per_reference=True)
    
    visibleHumans = list(dbHandler.query("SELECT * FROM humans WHERE humans.visible = 'TRUE'"))
    
    if len(visibleHumans) == 0:
        return "no_human_in_sight"
    
    if len(visibleHumans) > 1:
        self.logger.warning("More than one human is in sight!!!")
        # TODO what do we do here ?!?
    

    self.logger.info("Visible Human: {}".format(dict(visibleHumans[0])))
    
    # convert to dict because it's a orderedDict which rafcon can not handle
    
    try:
        re_id = visibleHumans[0]['re_id']
    except Exception as e:
        self.logger.warning(e)
        self.logger.warning(e.args)
        re_id = None
        return "human_has_no_re_id"
    
    outputs['visibleHuman_re_id'] = re_id 
    
    return "success"
