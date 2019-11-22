from Person import *
class Manage :
    """
     Class to manage a list of persons
    """
    @staticmethod
    def subscribe():
        d = Date()
        g = Grade()
        p = Person()
        print("---------------------------[Subscription Formuler]----------------------------------\n")
        sreader = input("Your Name       : ")
        p.setname(sreader)
        sreader = input("Day of Birth    : ")
        d.setday(int(sreader))
        sreader = input("Mounth of Birth : ")
        d.setmounth(int(sreader))
        sreader = input("Year of Birth   : ")
        d.setyear(int(sreader))
        p.setdate(d)
        sreader = input("Your Grade      : ")
        g.setvalue(float(sreader))
        p.setgrade(g)
        return p

    @staticmethod
    def newp1(plist, name="unamed"):
        add = True
        for i in range(0, len(plist)) :
            if plist[i].getname() == name and plist[i].getdate().getday() == Date() and plist[i].getgrade() == Grade() :
                if Manage.pocc(plist[i], plist) == 1 :
                    add = False
        if add :
            plist.append(Person(name))
        return plist

    @staticmethod
    def newp2(plist, p):
        add = True
        for i in range(0, len(plist)):
            if plist[i] == p :
                if Manage.pocc(plist[i], plist) == 1:
                    add = False
        if add:
            plist.append(p)
        return plist

    @staticmethod
    def newp0(plist):
        plist = Manage.newp2(plist, Manage.subscribe())
        return plist

    @staticmethod
    def getp0(plist):
        return plist[0]

    @staticmethod
    def getp1(plist, id=1):
        for i in range(0, len(plist)) :
            if plist[i].getid() == id :
                return plist[i]

    @staticmethod
    def getp2(plist, name="unnamed"):
        for i in range(0, len(plist)) :
            if plist[i].getname() == name :
                return plist[i]

    @staticmethod
    def getallp(plist, name="unnamed"):
        nl = []
        for i in range(0, len(plist)) :
            if plist[i].getname() == name :
                nl.append(plist[i])
        return nl

    @staticmethod
    def pocc(p, plist):
        cmp = 0
        for i in range(0, len(plist)):
            if plist[i] == p:
                cmp += 1
        return cmp

    @staticmethod
    def sorter(plist):
        for i in range(0, len(plist)) :
            for j in range(i+1, len(plist)) :
                if plist[i] == plist[j] :
                    plist[i+1], plist[j] = swap(plist[i+1], plist[j])
                    break
        return plist

    @staticmethod
    def showlist(plist):
        print("----------------------PERSONS LIST-----------------------")
        plist = Manage.sorter(plist)
        for i in range(0, len(plist)) :
            if i == 0 :
                print(plist[i])
            if i > 0 and plist[i-1] != plist[i] :
                print(plist[i])


def swap(a,b):
    c = Person()
    c = a
    a = b
    b = c
    del c
    return a,b



		

