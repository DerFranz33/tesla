from random import randrange
class Batterypack:
    
    def __init__(self, kwh, status=25) :
        self.kwh = kwh
        self.__status = status
        self.__n_charged = 0 # TODO
        self._battery_spend = False
    

    def charge(self):
       charge_load = randrange(20, self.kwh)
       self.status += charge_load
       self.n_charged += 1


    @property
    def kwh(self):
        return self.__kwh
    @kwh.setter
    def kwh(self, argument):
        CONSTRAIN_KWH = [70, 85, 100]
        if(isinstance(argument, int) and argument in CONSTRAIN_KWH):
            self.__kwh = argument
        else:
            self.__kwh = 70
            print('kwh set to {} due to lack of correct input'.format(self.__kwh))

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, argument):
        if(self._battery_spend == False):
            self.__status = argument
        else:
            print('impossible to change status... battery is spend!')

    
    @property
    def n_charged(self):
        return self.__n_charged
    @n_charged.setter
    def n_charged(self, argument):
        if(self.n_charged + 1 <= 10000):
            self.__n_charged = argument
        else:
            self._battery_spend = True
            print('battery is used {} times... battery is spend!'.format(self.n_charged))