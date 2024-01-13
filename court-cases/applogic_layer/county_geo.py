from database_layer.AppDataHandler import AppLogicDBHandler


class AppLogic:
    def __init__(self, config):
        self.DBHandler = AppLogicDBHandler(config)

    def county_data(self, state):

        return self.DBHandler.get_county_data(state)
