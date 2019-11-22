import math

class Date:
    """
        Class define a Date Class with Attributes :
            - day
            - mounth
            - year
    """
    #-------------------------------------------------------------------------------------------------------------------
    # CONSTRUCTOR
    def __init__(self, day=0, mounth=0, year=0):
        self.__day = int(math.fabs(day))
        self.__mounth = int(math.fabs(mounth))
        self.__year = int(math.fabs(year))
        self.adjust()
    #-------------------------------------------------------------------------------------------------------------------
    # TO STRING
    def __str__(self):
        return str(self.__day)+"/"+str(self.__mounth)+"/"+str(self.__year)
    #-------------------------------------------------------------------------------------------------------------------
    # REPRESENTATION
    def __repr__(self):
        return "day({0}) mounth({1}) year({2})\n".format(self.__day, self.__mounth, self.__year)
	#-------------------------------------------------------------------------------------------------------------------
	#AROTHMETC OPERATORS
    def __add__(self, other):
        day = self.__day + other.__day
        mounth = self.__mounth+other.__mounth
        year = self.__year if self.__year > other.__year else other.__year
        return Date(int(day), int(mounth), int(year))
    #-------------------------------------------------------------------------------------------------------------------
    def __sub__(self, other):
        day = math.fabs(self.__day - other.__day)
        mounth = math.fabs(self.__mounth - other.__mounth)
        year = math.fabs(self.__year if self.__year < other.__year else other.__year)
        return Date(int(day), int(mounth), int(year))

    #-------------------------------------------------------------------------------------------------------------------
    #COMPARING OPERATORES
    def __eq__(self, other):
        return self.__day == other.__day and self.__mounth == other.__mounth and self.__year == other.__year
    #-------------------------------------------------------------------------------------------------------------------
    def __ne__(self, other):
        return not self == other
    #-------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other):
        if self.__year > other.__year : return True
        elif self.__year == other.__year and self.__mounth > other.__mounth : return True
        elif self.__mounth == other.__mounth and self.__day > other.__day : return True
        else: return False
    #-------------------------------------------------------------------------------------------------------------------
    def __lt__(self, other):
        return not self > other or self == other
    #-------------------------------------------------------------------------------------------------------------------
    def __ge__(self, other):
        return self > other or self == other
    #-------------------------------------------------------------------------------------------------------------------
    def __le__(self, other):
        return self < other or self == other
    #-------------------------------------------------------------------------------------------------------------------
    # GETTERS & SETTERS
    def setday(self, day=0):
        if 1 <= day <= 31 :
            self.__day = int(day)
    #-------------------------------------------------------------------------------------------------------------------
    def getday(self):
        return self.__day
    #-------------------------------------------------------------------------------------------------------------------
    def setmounth(self, mounth=0):
        if mounth >= 1 and mounth <= 12:
            self.__mounth = int(mounth)
    #-------------------------------------------------------------------------------------------------------------------
    def getmounth(self):
        return self.__mounth
    #-------------------------------------------------------------------------------------------------------------------
    def setyear(self, year=0):
        if year >= 1 :
            self.__year = int(year)
    #-------------------------------------------------------------------------------------------------------------------
    def getyear(self):
        return self.__year
    #-------------------------------------------------------------------------------------------------------------------
    # MANAGEMENT FUNCTIONS
    def print(self):
        if self.__day == 0 or self.__mounth == 0 or self.__year == 0 :
            print("Date Not Registred Yet !")
        else :
            mounths = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
            print(str(self.__day)+" "+mounths[self.__mounth-1]+" "+str(self.__year))
    #-------------------------------------------------------------------------------------------------------------------
    def adjust(self):
        while self.__day > 31 :
            self.__mounth+=1
            self.__day-=31
        while self.__mounth > 12 :
            self.__year+=1
            self.__mounth-=12

