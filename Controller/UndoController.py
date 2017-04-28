'''
Created on 22 nov. 2015

@author: paul
'''
from Repository.ClientsRepository import *
from Repository.MovieRepository import *
from Repository.RentalRepository import *

class UndoController:
    """
    This class controls the undo/redo operations over all application controllers.
    It is required so that we have a record of what controller must perform each undo/redo operation. 
    """
    def __init__(self):
        self.__controllers = [] 
        self.__index = -1       
        
    def recordUpdatedController(self, modifController):
        """
        Every time an application controller record an operation with support for undo/redo it must call this method.
        Input: modifController - A list of controllers that can undo/redo the operation. 
        Output: the current list of controllers is modified and the index is set to the last list of modified controllers.
        """
        self.__controllers.append(modifController)
        self.__index = len(self.__controllers) - 1
    
    def undo(self):
        """
        Undo the last performed operation by any application controller. 
        """
        if self.__index < 0:
            return False
        
        try:
            self.__controllers[self.__index].undo()
        except IndexError:
            self.__index=-1
            return False
        self.__index -= 1
        return True
    
    def redo(self):
        """
        Redoes the last operation performed by any controller
        """
        if len(self.__controllers)<=self.__index:
            return False
        try:
            self.__controllers[self.__index].redo()
            self.__index += 1
        except IndexError:
            return False
        
        return True