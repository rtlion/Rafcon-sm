import dataset

def execute(self, inputs, outputs, gvm):
    
    name = inputs['name']
    drink = inputs['drink']
    
    dbHandler = gvm.get_variable(inputs["dbHandle"], per_reference=True)
    
    dbc = dataset.connect(dbHandler)
    
    self.logger.info("Type dbHandler: {}".format(dbHandler))
    self.logger.info("Type dbc: {}".format(dbc))
    
    re_id = inputs['re_id']
    
    #sql = """UPDATE humans
    #         SET humans.name = '{name}',
    #             humans.fav_drink = '{drink}'
    #         WHERE humans.re_id = {re_id};
    #      """.format(name = name,
    #                 drink = drink,
    #                 re_id = re_id)
    #self.logger.info("Trying SQL: {}".format(sql))
     
    
    try:
        dbHandler.update({'re_id': re_id, 'name': name, 'fav_drink': drink}, ['re_id'])
        
        #dbHandler.query(sql)
        #dbHandler.commit()
    except Exception as e:
        self.logger.warning(e)
        self.logger.warning(e.args)
    
    return "success"
