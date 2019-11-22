import sys
from Date import *
from Grade import *
class Person :
    personsNumber = 0
    """
        Person class Attributes :
            - personsnumber
            - id
            - name
            - date
            - grade
    """
    #-------------------------------------------------------------------------------------------------------------------
    #CONSTRUCTOR
    def __init__(self, name="unnamed", date=Date(), grade=Grade()):
        Person.personsNumber+=1
        self.__id = Person.personsNumber
        self.__name = name
        self.__date = date
        self.__grade = grade
    #-------------------------------------------------------------------------------------------------------------------
    #DESTRUCTOR
    def __del__(self):
        del self.__date
        del self.__grade
    #-------------------------------------------------------------------------------------------------------------------
    #TO STRING
    def __str__(self):
        return "["+str(self.__id)+"]["+str(self.__name)+"]["+str(self.__date)+"]["+str(self.__grade)+"]"
    #-------------------------------------------------------------------------------------------------------------------
    #COMPARING OPERATORS
    def __eq__(self, other):
        return self.__name == other.__name and self.__date == other.__date and self.__grade == other.__grade
    def __ne__(self, other):
        return not self == other
    #-------------------------------------------------------------------------------------------------------------------
    #GETTERS SETTERS
    @staticmethod
    def getpnumber():
        return Person.personsNumber
    def getid(self):
        return self.__id
    def setname(self, name="unnamed"):
        self.__name = str(name)
    def getname(self):
        return self.__name
    def setdate(self, date=Date()):
        self.__date = date
    def getdate(self):
        return self.__date
    def setgrade(self, grade=Grade()):
        self.__grade = grade
    def getgrade(self):
        return self.__grade
    #-------------------------------------------------------------------------------------------------------------------
    #MANAGEMENT
    def print(self):
        print("Person ID     : "+str(self.__id))
        print("Person Name   : "+str(self.__name))
        sys.stdout.write("Person Date   : ")
        self.__date.print()
        sys.stdout.write("Person Grade  : ")
        self.__grade.print()

