class Tesla:
    def __init__(self, type=3):
        self.__type = 3
        self.type = type
        

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, argument):
        CONSTRAIN_TYPE = ['S', 'X', 3 ,'Y']
        if(argument in CONSTRAIN_TYPE):
            self.__type = argument
        else:
            (type == 3)