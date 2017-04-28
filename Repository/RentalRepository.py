'''
Created on 10 nov. 2015

@author: paul
'''
from datetime import *
from Domain.Clients import *
from Domain.Movies import *
from Domain.Rental import *
from Repository.ClientsRepository import *
from Repository.MovieRepository import *
from Domain.MExceptions import MovieException
from asyncio.locks import Condition
from Domain.ObjectsTimes import *

class RentalRepository:
    def __init__(self):
        """
        Creates an instance of the Repository.
        """
        self.__data = []
    
    def __checkmovieID(self,m):
        '''
        Checks if the movie is rent or not
        Input: m - object of type Movies
        Output: True if the movie can be added, False otherwise
        '''
        for e in self.__data:
            if e.getMovie()==m and str(e.getEnd())=="0":
                return False
        return True

    def add(self,ren):
        '''
        Adds a rent to the repository.
        Input: ren - object of type Rental
        Output: the given rental is added to the repository, if no other client has the movie
        Exceptions: raises MovieException if another client has the movie
        '''
        m=ren.getMovie()
        condition=self.__checkmovieID(m) 
        if condition:
            self.__data.append(ren)
        else:
            raise MovieException("Movie is already rented by another client")
    def __len__(self):
        '''
        Returns the size of the list of rentals
        (Overriding the len() built-in function)
        '''
        return len(self.__data)
    
    def getAll(self):
        '''
        Returns the list of rentals
        '''
        return self.__data
    
    def returnMovie(self,m):
        '''
        Returns the movie 
        Input: m- an instance of Movies, the movie we want to remove
        Output: the movie is returned and the end date is set.
        Exception: Raises MovieException if the movie is not in the rented list 
        ''' 
        condition=0
        for e in self.__data:
            if int(e.getMovie().getID())==int(m.getID()) and str(e.getEnd())=="0":
                e.setEnd(datetime.now())
                condition=1
                return e
            elif int(e.getMovie().getID())==int(m.getID()) and str(e.getEnd())!="0":
                condition=2
        if condition==0:
            raise MovieException('The movie"'+ m.getTitle() +'" is not yet rented')
        if condition==2:
            raise MovieException('The movie"'+ m.getTitle() +'" has already been returned')
    def remove(self,ren):
        '''
        Removes a rental 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getStart() == ren.getStart():
                self.__data.pop(i)
                return
        
    def rentedTimes(self,m):
        '''
        Returns how many times a movie has been rented
        Input: m - a Movies Instance, the movie we want to measure
        Exceptions: -
        Output- nr - an integer, the number of times the movie has been rented
        '''
        nr=0
        for e in self.__data:
            if e.getMovie().getID()==m.getID():
                nr+=1
        return nr
    def mostRentedMovies(self):
        '''
        Returns a list with the most rented movies
        Input: -
        Exceptions: -
        Output: - the list of movies
        '''
        l=[]
        for e in self.__data:
            prop=True
            for i in range(len(l)):
                if isinstance(l[i], ObjectsTimes):
                    if l[i].getObj().getID()==e.getMovie().getID():
                        prop=False
            if prop:
                times=self.rentedTimes(e.getMovie())
                movieTimes=ObjectsTimes(e.getMovie(),times)
                l.append(movieTimes)
        l.sort(key=lambda x: x.getTimes(),reverse=True)
        return l
    
    def rentedTimes2(self,cl):
        '''
        Returns how many times a client has rented a movie
        Input: cl - a Clients instance, the client we want to measure  
        Exceptions: -
        Output: nr -an integer, the number of times the client has rented a movie
        '''
        nr=0
        for e in self.__data:
            if e.getClient().getID()==cl.getID():
                nr+=1
        return nr
        
    def mostActiveClients(self):
        '''
        Generates a list with the most active clients
        Input: -
        Exceptions: -
        Output: - the list of clients
        '''
        l=[]
        for e in self.__data:
            prop=True
            for i in range(len(l)):
                if isinstance(l[i], ObjectsTimes):
                    if l[i].getObj().getID()==e.getClient().getID():
                        prop=False
            if prop:
                times=self.rentedTimes2(e.getClient())
                clientTimes=ObjectsTimes(e.getClient(),times)
                l.append(clientTimes)
        l.sort(key=lambda x: x.getTimes(), reverse=True)
        return l
    def clientsOrdonator(self):
        '''
        Generates the alphabetic ordered list clients 
        Input: -
        Exceptions: -
        Output: - the list of clients
        '''
        l=[]
        for e in self.__data:
            prop=True
            for i in range(len(l)):
                if l[i]==e.getClient().getName():
                    prop=False
            if prop:
                l.append(e.getClient().getName())
        l.sort()
        return l
    def movieOrdonator(self):
        '''
        Generates the alphabetic ordered list of movies
        Input: -
        Exceptions: -
        Output: - the list of movies
        '''
        l=[]
        for e in self.__data:
            prop=True
            for i in range(len(l)):
                if l[i]==e.getMovie().getTitle():
                    prop=False
            if prop:
                l.append(e.getMovie().getTitle())
        l.sort()
        return l
    
    
def testRepository():
    '''
        Test the current repository functions
    '''
    m=Movies(1,"The revenge","John is a retired cop","action")
    c=Clients(1,"Muri",1951129060039)
    ren=Rental(m,c,1,2)
    renRepo=RentalRepository()
    assert ren.getMovie==m
    assert ren.getClient==c
    assert ren.getEnd==2
    assert ren.getStart==1
        
    assert len(renRepo)==0
    renRepo.add(ren)
    assert len(renRepo)==1
    
    if __name__ == '__main__':
        testRepository()