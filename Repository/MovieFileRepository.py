'''
Created on Nov 30, 2015

@author: Muresan
'''
from Domain.Movies import *
from Repository.MovieRepository import *

class MovieFileRepository(MovieRepository):
    '''
    Class that is used for retrive/store movies from/into files
    '''
    def __init__(self, filename):
        MovieRepository.__init__(self)
        self.__filename = filename
        self.__loadFromFile()
    
    def __loadFromFile(self):
        '''
        Reads movies from file.
        Input: -
        Output: the movies from the file are stored in memory.
        Exceptions: -raises IOError if the file cannot be opened 
                    -raises MovieException if there are duplicate client ids in the file
        '''
        try:
            f = open(self.__filename, "r")
        except IOError:
            return
        
        for line in f:
            line = line.strip()
            movieAtributes = line.split('|')
            if len(movieAtributes)!=4:
                continue
            movieId = movieAtributes[0].strip()
            movieTitle= movieAtributes[1].strip()
            movieD= movieAtributes[2].strip()
            movieT=movieAtributes[3].strip()
            movie=Movies(int(movieId),movieTitle,movieD,movieT)
            MovieRepository.add(self,movie)
        
        f.close()
        
    def add(self,mov):
        '''
        Overrides the "add" function from the main movies Repository
        Input:-
        Output:- the list of movies is stored both in memory&file
        Exceptions:-
        '''
        MovieRepository.add(self,mov)
        self.__storeToFile()
    
    def remove(self, id):
        '''
        Overrides the "remove" function from the main movies Repository
        Input:-
        Output: the updated list of movies is stored both in memory&file
        Exceptions:-
        '''
        MovieRepository.remove(self, id)
        self.__storeToFile()
    
    def update(self, id, newTitle, newDescription, newType):
        '''
        Overrides the "update" function from the main movies Repository
        Input:-
        Output: the updated list of movies is stored both in memory&file
        Exceptions:-
        '''
        MovieRepository.update(self, id, newTitle, newDescription, newType)
        self.__storeToFile()
    
    def __storeToFile(self):
        '''
            Stores all the movies in the file.
            Input: -
            Output: all the movies from the repository are stored to the file self.__filename
        '''
        
        f=open(self.__filename,'w')
        for e in self.getAll():
            f.write(str(e.getID())+"|"+ e.getTitle()+"|"+ e.getDescription()+"|" + e.getType()+'\n')
            
        f.close()