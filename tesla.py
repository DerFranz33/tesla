from random import randrange
from batterypack import Batterypack
class Tesla:
    def __init__(self, type, colour):
        self.__type = 3
        self.type = type
        self.__colour = 'Solid Black'
        self.colour = colour
        self.__mileage = 0
        self._panel_broken = self._panel_is_broken(self.colour)
        self._battery = Batterypack(100)
        

    def __str__(self):
        return('Tesla van het type: {} -- met colour: {} -- en mileage: {} -- en is panel broken?: {} -- en battery status: {} -- en battery kwh: {}'
              .format(self.type, self.colour, self.mileage, self._panel_broken, self._battery.status, self._battery.kwh))




    def drive(self,miles):
        if(isinstance(miles, int) and self._panel_broken == False):
             for mile in range(miles):
              kwh_charge_used = (ord(self.type)/100)*1
              current_battery_status = self._battery.status
              if(current_battery_status - kwh_charge_used >= 0):
                # self._battery.juice(kwh_charge_used)
                self._battery.juice(10)




    def _panel_is_broken(self, colour):
        c = len(colour)
        chance_percentage = round((c * 0.001 * 100), 2)
        if(randrange(0, 100) <= chance_percentage): #TODO wanky
            return True
        return False


    def _charge(self):
       self._battery.charge()


    def _can_drive(self):
        if(self._panel_broken == True):
            return False
        if(self._panel_broken == False):
            return True


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