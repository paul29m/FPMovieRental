'''
Created on 3 nov. 2015

@author: paul
'''
from Domain.Movies import *
from Domain.MExceptions import MovieException
from Domain.Clients import *
from Domain.Rental import *

from Repository.ClientFileRepository import *
from Repository.ClientsRepository import *
from Repository.MovieFileRepository import *
from Repository.MovieRepository import *
from Repository.RentalFileRepository import *
from Repository.RentalRepository import *

from Controller.ClientsController import *
from Controller.MovieController import *
from Controller.RentalController import *
from Controller import RentalController

from UI.UI import *
from Controller.UndoController import *


method=UI.chooseMemoryMenu()

if method == '0':
    mrepo=MovieRepository()
    crepo=ClientsRepository()
    rrepo=RentalRepository()
    
    m1=Movies(1,"The Godfather","A mafia movie","Drama")
    m2=Movies(2,"Assassin's Creed","A mafia movie","Action")
    mrepo.add(m1)
    mrepo.add(m2)
    mrepo.add(Movies(3,"The Godfather 2","A mafia movie reloaded","Drama"))
    mrepo.add(Movies(4,"The Gambler","A new movie","Drama"))
    c1=Clients(1,"Simi",1851021345131)
    c2=Clients(2,"Doina",1860331281263)
    crepo.add(c1)
    crepo.add(c2)
    crepo.add(Clients(3,"Paul",1930614296921))
    crepo.add(Clients(4,"Messi",1961129060038))
    ren1=Rental(c1,m1,datetime.now(),0)
    ren2=Rental(c2,m2,datetime.now(),0)
    rrepo.add(ren1)
    rrepo.add(ren2)
else:
    mrepo=MovieFileRepository('movies.txt')
    crepo=ClientFileRepository('clients.txt')
    rrepo=RentalFileRepository('rentals.txt')
    

undoCtrl = UndoController()

mcontroller=MovieController(mrepo,undoCtrl)
ccontroller=ClientsController(crepo,undoCtrl)
rcontroller=RentallController(rrepo,undoCtrl)

ui = UI(mcontroller,ccontroller,rcontroller,undoCtrl)
ui.mainMenu()