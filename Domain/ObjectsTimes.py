'''
Created on 18 nov. 2015

@author: paul
'''
from Domain.Clients import *
from Domain.Movies import *

class ObjectsTimes:
    def __init__(self,obj,times):
        self.__obj=obj
        self.__times=times
        
    def getObj(self):
        '''
        Getter for the objects in the class
        '''
        return self.__obj
    
    def getTimes(self):
        '''
        Getter for the times that the object has been rented
        '''
        return self.__times
    def __str__(self):
        return '\n'+ str(self.__obj)+"\n Rentals: "+str(self.__times)