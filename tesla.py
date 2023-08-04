from random import randrange
from batterypack import Batterypack
class Tesla:
    def __init__(self, type, colour):
        self.__type = 3
        self.type = type
        self.__colour = 'Solid Black'
        self.colour = colour
        self.__mileage = 0
        self.__panel = self._panel_is_broken(self.colour)
        self._battery = Batterypack(100)
        


    def _panel_is_broken(self, colour):
        c = len(colour)
        chance_percentage = round((c * 0.001 * 100), 2)
        if(randrange(0, 100) <= chance_percentage): #TODO wanky
            return True
        return False

    def _charge(self):
       self._battery.charge()


#-----------------------------------PROPERTIES-------------------------------------
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, argument):
        CONSTRAIN_TYPE = ['S', 'X', 3 ,'Y']
        if(argument in CONSTRAIN_TYPE):
            self.__type = argument
        else:
            print('Tesla model 3 created (due to false input)')
    
    @property
    def colour(self):
        return self.__colour
    @colour.setter
    def colour(self, argument):
        CONSTRAIN_COLOUR = ['Deep Blue', 'Midnight Silver', 'Pearl White', 'Red', 'Solid Black']
        if(argument in CONSTRAIN_COLOUR):
            self.__colour = argument
        else:
            print('Tesla colour Solid Black sprayed (due to false input)')

    @property
    def mileage(self):
        return self.__mileage
    @mileage.setter
    def mileage(self, argument):
        if(isinstance(argument, int) and argument >= 0):
            self.__mileage = argument
# -----------------------------------END PROPERTIES-----------------------------------------