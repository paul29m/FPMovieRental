'''
Created on 10 nov. 2015

@author: paul
'''
from Repository.RentalRepository import *
from Controller.RentalController import *
from Controller.UndoHistory import *
from Controller.UndoController import *

class RentallController:
    '''
    Creates a new instance of Rental Controller.
    '''
    def __init__(self, renRepo,undoControler):
        self.__repo = renRepo
        
        self.__operations=[]
        self.__index=0
        self.__uc=undoControler
        
    def addR(self,ren):
        '''
        Adds a rental to the list.
        Input: rental - the rent
        Output: the rental is added, if there in no other client that has rent the movie
        Exceptions: raises MovieException if another movie with the same id already exists
        '''
        while self.__index<len(self.__operations):
            self.__operations.pop()
        
        self.__repo.add(ren)
        self.__operations.append(AddOperation(ren))
        self.__index +=1
        self.__uc.recordUpdatedController(self)
        
    def show(self):
        '''
        Shows all rentals
        '''
        return self.__repo.getAll()
    
    def returnMovie(self,m):
        '''
        Returns the movie 
        Input: m- an instance of Movies, the movie we want to return
        Output: the movie is returned and the end date is set.
        Exception: Raises MovieException if the movie is not in the rented list 
        ''' 
        oldRental = self.__repo.returnMovie(m)
        newRental = Rental(oldRental.getMovie(),oldRental.getClient(),oldRental.getStart(),oldRental.getEnd())
        self.__operations.append(UpdateOperation(oldRental,newRental))
        self.__index +=1
        self.__uc.recordUpdatedController(self)
    def mostRentedMovies(self):
        '''
        Returns a list with the most rented movies
        Input: -
        Exceptions: -
        Output: - the list of movies
        '''
        return self.__repo.mostRentedMovies()
    def mostActiveClients(self):
        '''
        Returns a list with the most active clients
        Input: -
        Exceptions: -
        Output: - the list of clients
        '''
        return self.__repo.mostActiveClients()
    def clientsOrdonator(self):
        '''
        Returns the alphabetic ordered list clients 
        Input: -
        Exceptions: -
        Output: - the list of clients
        '''
        return self.__repo.clientsOrdonator() 
        
    def movieOrdonator(self):
        '''
        Returns the alphabetic ordered list of movies
        Input: -
        Exceptions: -
        Output: - the list of movies
        '''
        return self.__repo.movieOrdonator()
    def __findR(self,ren):
        """
        Returns the index of the rental 
        Input: ren - a rental instance, the rental we want to find
        Output: the rental index if it exists
        """
        rentals = RentalRepository.getAll()
        
        for i in range(len(rentals)):
            if rentals[i].getStart()== ren.getStart() :
                return i
        return None
                
    def undo(self):
        """
        Undoes the last client operation that changed the set of rentals.
        Returns True if operation was undone, False otherwise.
        """
        if self.__index == 0: 
            return False
        
        self.__index -= 1
        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.remove(operation.getObject())
        if isinstance(operation, UpdateOperation):
            operation.getOldObject().setEnd(0)
            
    def redo(self):
        """
        Redo the last undone operation that changed the set of rentals.
        Input:-
        Output: Returns True if operation was redone, False otherwise.
        Exceptions: -
        """
        
        if self.__index>=len(self.__operations):
            return False
        
        operation = self.__operations[self.__index]
        if isinstance(operation, AddOperation):
            self.__repo.add(operation.getObject())
        if isinstance(operation, UpdateOperation):
            operation.getOldObject().setEnd(operation.getNewObject().getEnd())
        
        self.__index +=1
    