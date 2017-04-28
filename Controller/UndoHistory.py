'''
Created on 22 nov. 2015

@author: paul
'''
from Repository.ClientsRepository import *
from Repository.MovieRepository import *
from Repository.RentalRepository import *
from _sqlite3 import OperationalError

class AddOperation:
    """
    Class that models an add operation in the controller 
    """
    def __init__(self, object):
        """
        Constructor for AddOperation class
        object - The object that was added
        """
        self.__object = object
        
    def getObject(self):
        return self.__object
    
class RemoveOperation:
    """
    Class that models a remove operation in the controller 
    """
    def __init__(self, object):
        """
        Constructor for RemoveOperation class
        object - The object that was removed
        """
        self.__object = object
        
    def getObject(self):
        return self.__object
        
class UpdateOperation:
    """
    Class that models an update operation in the controller 
    """
    def __init__(self, oldObject, updatedObject):
        """
        Constructor for UpdateOperation class
        oldObject - The instance before updating
        updatedObject - The instance after the update
        """
        self.__oldObject = oldObject
        self.__updatedObject = updatedObject
    
    def getOldObject(self):
        return self.__oldObject

    def getNewObject(self):
        return self.__updatedObject
