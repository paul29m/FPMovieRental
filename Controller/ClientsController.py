'''
Created on 3 nov. 2015

@author: paul
'''
from Repository.ClientsRepository import *
from Domain.Clients import *
from Controller.UndoController import *
from Controller.UndoHistory import *
from Validator.ClientValidator import *

class ClientsController:
    '''
    Creates a new instance of clients Controller.
    '''
    def __init__(self, clRepo,undoController):
        self.__repo = clRepo
        
        self.__uC = undoController
        self.__index = 0 
        self.__operations = []
        
        
    def addClient(self, cl):
        '''
        Adds a client to the list.
        Input: cl - a client object, the client we wnat to add
        Output: the client is added, if there in no other client with the given id
        Exceptions: raises MovieException if another client with the same id already exists
        '''
        self.__repo.add(cl)
        try:
            ClientValidator.validateC(cl)
            self.__operations.append(AddOperation(cl))
            self.__index += 1
            self.__uC.recordUpdatedController(self)
        except MovieException:
            return
        
    def removeClient(self, id):
        '''
        Removes a client from the list, using its id
        Input: id - integer, the id of the client that must be removed
        Output: if such a client exists, it is removed and returned
        Exceptions: raises MovieException if a client with the given id does not exist
        '''
        try:
            cl= self.finByID(id)
        except MovieException:
            cl = False
            
        self.__repo.remove(id)
        
        if isinstance(cl, Clients):
            self.__operations.append(RemoveOperation(cl))
            self.__index += 1
            self.__uC.recordUpdatedController(self)
        
    
    def getAll(self):
        '''
        Returns the list of client
        '''
        return self.__repo.getAll()
    
    def updateClient(self,id,newName,newCNP):
        '''
        Update the client with the given id
        Input: id - integer, the id of the client that must be removed
               newname- a string, the client new name
               newcnp - integer, the client new cnp    
        Output: if such a client exists, it is removed and returned
        Exceptions: raises MovieException if a client with the given id does not exist
        ''' 
        try:
            cl = self.finByID(id)
            oldClient=Clients(cl.getID(),cl.getName(),cl.getCNP())
            ClientValidator.validateC(cl)
        except MovieException:
            oldClient = False
        self.__repo.update(id,newName,newCNP)
        
        if isinstance(oldClient, Clients):
            try:
                cl =  self.finByID(id)
                newClient=Clients(cl.getID(),cl.getName(),cl.getCNP())
                ClientValidator.validateC(newClient)
                self.__operations.append(UpdateOperation(oldClient, newClient))
                self.__index += 1
                self.__uC.recordUpdatedController(self)
            except MovieException:
                return
            
    def findByName(self,name):
        '''
        Finds the client
        input: name- a string, the client  name
        Output: if such a client exists, it returns it
        Exceptions: raises MovieException if a client with the given name does not exist
        '''
        return self.__repo.findByName(name)
    
    def finByID(self,id):
        '''
        Finds the client id
        input: id- an integer, the client id
        Output: if such a client exists, it returns it
        Exceptions: raises MovieException if a client with the given name does not exist
        '''
        if self.__repo.findById(id)==None:
            raise MovieException('The client with the id"'+str(id)+'"does not exist' )
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
        try:
            if isinstance(operation, AddOperation):
                self.__repo.remove(operation.getObject().getID())
            elif isinstance(operation, RemoveOperation):
                self.__repo.add(operation.getObject())
            else:
                self.__repo.update(operation.getOldObject().getID(),operation.getOldObject().getName(),operation.getOldObject().getCNP())
        except MovieException:
            return False
        
    def redo(self):
        """
        Redo the last undone operation that changed the set of clients
        Input:-
        Output: Returns True if operation was redone, False otherwise.
        Exceptions: -
        """
        if self.__index>len(self.__operations):
            return False
        operation = self.__operations[self.__index]
        try:
            if isinstance(operation, AddOperation):
                self.__repo.add(operation.getObject())
            elif isinstance(operation, RemoveOperation):
                self.__repo.remove(operation.getObject().getID())
            else:
                self.__repo.update(operation.getNewObject().getID(), operation.getNewObject().getName(), operation.getNewObject().getCNP() )
        except MovieException:
            return False
        
        self.__index += 1