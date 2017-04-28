'''
Created on 3 nov. 2015

@author: paul
'''
from Domain.Movies import *
from Repository.MovieRepository import *
from Controller.UndoController import *
from Controller.UndoHistory import *
from Validator.MovieValidator import *

class MovieController:
    '''
    Creates a new instance of Movie Controller.
    '''
    def __init__(self, movRepo, undoController):
        self.__repo = movRepo
        
        self.__uc = undoController
        self.__operations=[]
        self.__index= 0
        
    def addMovie(self, mov):
        '''
        Adds a movie to the list.
        Input: mov - the movie
        Output: the movie is added, if there in no other movie with the given id
        Exceptions: raises MovieException if another movie with the same id already exists
        '''
        self.__repo.add(mov)
        
        try:
            MovieValidator.validateMovie(mov)
            self.__operations.append(AddOperation(mov))
            self.__index += 1
            self.__uc.recordUpdatedController(self)
        except MovieException:
            return
        
    def removeMovie(self, id):
        '''
        Removes a movie from the list, using its id
        Input: id - integer, the id of the movie that must be removed
        Output: if such a movie exists, it is removed and returned
        Exceptions: raises MovieException if a movie with the given id does not exist
        '''
        try:
            mov = self.findById(id)
            MovieValidator.validateMovie(mov)
        except MovieException:
            mov = False
        self.__repo.remove(id)
        
        if isinstance(mov, Movies):
            self.__operations.append(RemoveOperation(mov))
            self.__index += 1
            self.__uc.recordUpdatedController(self)
        
        
    def getAll(self):
        '''
        Returns the list of movies
        '''
        return self.__repo.getAll()
    def updateMovie(self,id,newName,newDescrition,newTitle):
        '''
        Update the movie with the given id
    
        Input: id - integer, the id of the client that must be removed
               newname- a string, the movie new name
               newdescription - string, the movie new description
               newType- string, the new movie type   
        Output: if such a movie exists, it is removed and returned
        Exceptions: raises MovieException if a movie with the given id does not exist
        '''
        try:
            mov= self.findById(id)
            oldMov=Movies(mov.getID(),mov.getTitle(),mov.getDescription(),mov.getType())
            MovieValidator.validateMovie(oldMov)
        except MovieException:
            oldMov= False
            
        self.__repo.update(id,newName,newDescrition,newTitle)
        
        if isinstance(oldMov, Movies):
            try:
                mov =  self.findById(id)
                newMov = Movies(mov.getID(),mov.getTitle(),mov.getDescription(),mov.getType())
                self.__operations.append(UpdateOperation(oldMov, newMov))
                self.__index += 1
                self.__uc.recordUpdatedController(self)
            except MovieException:
                return
            
    def findByName(self,name):
        '''
        Finds the movie
        input: name- a string, the movie new name
        Output: if such a movie exists, it returns it
        Exceptions: raises MovieException if a movie with the given name does not exist
        '''
        return self.__repo.findByName(name)
    def findById(self,id):
        '''
        Finds the movie
        Input: id, an integer, the movie id
        Output: if such a movie exists, it returns it
        Exceptions: raises MovieException if a movie with the given id does not exist
        '''
        if self.__repo.findById(id)==None:
            raise MovieException("The movie with the given id is not in the list")
        else:
            return self.__repo.findById(id)
        
    def undo(self):
        """
        Undoes the last client operation that changed the set of clients.
        Input:-
        Output: Returns True if operation was undone, False otherwise.
        Exceptions: -
        """
        if self.__index == 0: 
            return False
    
        self.__index -= 1
        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.remove(operation.getObject().getID())
        elif isinstance(operation, RemoveOperation):
            self.__repo.add(operation.getObject())
        else:
            self.__repo.update(operation.getOldObject().getID(),operation.getOldObject().getTitle(),operation.getOldObject().getDescription(),operation.getOldObject().getType())
    def redo(self):
        """
        Redoes the last undone operation that change the set of clients.
        Input:-
        Output: Returns True if operation was redone, False otherwise.
        Exceptions:-
        """
        if self.__index>=len(self.__operations):
            return False
        
        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.add(operation.getObject())
        elif isinstance(operation, RemoveOperation):
            self.__repo.remove(operation.getObject().getID())
        else:
            self.__repo.update(operation.getNewbject().getID(),operation.getNewObject().getName(),operation.getNewObject().getDescription(),operation.getNewbject().getType())
            
        self.__index +=1