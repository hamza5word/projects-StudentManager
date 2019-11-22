import math
class Grade :
    """
        Grade class Attributes :
            - value
    """
    #-------------------------------------------------------------------------------------------------------------------
    #CONSTRUCTOR
    def __init__(self, value=0.0):
        self.__value = float(math.fabs(value))
    #-------------------------------------------------------------------------------------------------------------------
    #TO STRING
    def __str__(self):
        return str(self.__value)
    #-------------------------------------------------------------------------------------------------------------------
    #ARITHMETIC OPERATORS
    def __add__(self, other):
        value = self.__value + other.__value
        return Grade(float(value))
    def __sub__(self, other):
        value = math.fabs(self.__value - other.__value)
        return Grade(float(value))
    def __iadd__(self, other):
        self.__value += other.__value
        return self
    def __isub__(self, other):
        self.__value -= other.__value
        return self
    #-------------------------------------------------------------------------------------------------------------------
    #COMPARE OPERATORS
    def __eq__(self, other):
        return self.__value == other.__value
    def __ne__(self, other):
        return not self == other
    def __gt__(self, other):
        return self.__value > other.__value
    def __lt__(self, other):
        return self.__value < other.__value
    def __ge__(self, other):
        return self > other or self == other
    def __le__(self, other):
        return self < other or self == other
    #-------------------------------------------------------------------------------------------------------------------
    #GETTERS SETTERS
    def getvalue(self):
        return self.__value
    def setvalue(self, value=0):
        self.__value = float(math.fabs(value))
    #-------------------------------------------------------------------------------------------------------------------
    #MANAGEMENT
    def print(self):
        print(str(self.__value))

