import os
from Manage import *
if __name__ == '__main__':
    l = []
    P1 = Person("hamza", Date(1,9,1998), Grade(12.6))
    P2 = Person("youssef", Date(2,7,1998), Grade(2.15))
    l = Manage.newp2(l,P1)
    l = Manage.newp2(l,P2)
    l = Manage.newp0(l)
    Manage.showlist(l)
    os.system("pause")
    

	










