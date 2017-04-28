'''
Created on 10 nov. 2015

@author: paul
'''
from datetime import *
from Domain.Clients import *
from Domain.Movies import *

class Rental:
    def __init__(self,client,movie,start,end):
        '''
        Creates a new instance of a rental.
        '''
        self.__client = client
        self.__movie = movie
        self.__start = start
        self.__end = end
        
    def getClient(self):
        '''
        Getter for client
        '''
        return self.__client
    
    def getMovie(self):
        '''
        Getter for movie
        '''
        return self.__movie
    
    def getStart(self):
        '''
        Getter for start of period
        '''
        return self.__start
    
    def getEnd(self):
        '''
        Getter for end of period
        '''
        return self.__end
    
    def setClient(self,newClient):
        '''
        Setter for client
        Input: newClient= an instance of class Clients, the new client
        '''
        self.__client=newClient
        
    def setMovie(self,newMovie):
        '''
        Setter for movie
        Input: newMovie= an instance of class Movies, the new movie
        '''
        self.__movie=newMovie
        
    def setStart(self,newS):
        '''
        Setter for start period
        Input: newS - a time instance, the new start time 
        '''
        self.__start=newS
        
    def setEnd(self,newE):
        '''
        Setter for end of period
        Input: newE= a time instance, the new end time
        '''
        self.__end=newE
    
    def __str__(self):
        '''
        Overloads the str function
        '''
        if str(self.__end)=="0":
            msg="The movie is still rented"
        else:
            msg="End:"+ str(self.__end)

        return "Rental:\nMovie: " + str(self.__movie) + "\nClient: " + str(self.__client) + "\nStart: " + str(self.__start) + "\n" + msg
    
    def tesRental(self): 
        """
        Test getters and setters.
        """
        m=Movies(1,"The revenge","John is a retired cop","action")
        c=Clients(1,"Muri",1951129060039)
        ren=Rental(m,c,1,2)
        
        assert m.getID()==1
        assert ren.getClient()==c
        assert ren.getMovie()==m
        assert ren.getEnd()==2
        assert ren.getStart()==1