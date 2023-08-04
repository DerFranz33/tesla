from random import randrange
class Batterypack:
    def __init__(self, kwh, status=25) :
        self.kwh = kwh
        self.__status = status
        self.__n_charged = 0 # TODO
    

    def charge(self):
       charge_load = randrange(20, self.kwh)
       self.__status += charge_load


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
        print('Not allowed to alter battery. Battery status remains {}'.format(self.kwh))