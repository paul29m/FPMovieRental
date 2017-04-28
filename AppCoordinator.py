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

method = UI.chooseMemoryMenu()

if method == '0':
    movieRepo = MovieRepository()
    clientRepo = ClientsRepository()
    rentRepo = RentalRepository()

    m1 = Movies(1, "The Godfather", "A mafia movie", "Drama")
    m2 = Movies(2, "Assassin's Creed", "A mafia movie", "Action")
    movieRepo.add(m1)
    movieRepo.add(m2)
    movieRepo.add(Movies(3, "The Godfather 2", "A mafia movie reloaded", "Drama"))
    movieRepo.add(Movies(4, "The Gambler", "A new movie", "Drama"))
    c1 = Clients(1, "Simi", 1851021345131)
    c2 = Clients(2, "Doina", 1860331281263)
    clientRepo.add(c1)
    clientRepo.add(c2)
    clientRepo.add(Clients(3, "Paul", 1930614296921))
    clientRepo.add(Clients(4, "Messi", 1961129060038))
    ren1 = Rental(c1, m1, datetime.now(), 0)
    ren2 = Rental(c2, m2, datetime.now(), 0)
    rentRepo.add(ren1)
    rentRepo.add(ren2)
else:
    movieRepo = MovieFileRepository('movies.txt')
    clientRepo = ClientFileRepository('clients.txt')
    rentRepo = RentalFileRepository('rentals.txt')

undoCtrl = UndoController()

movieController = MovieController(movieRepo, undoCtrl)
clientController = ClientsController(clientRepo, undoCtrl)
rentController = RentallController(rentRepo, undoCtrl)

ui = UI(movieController, clientController, rentController, undoCtrl)
ui.mainMenu()
