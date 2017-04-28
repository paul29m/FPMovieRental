'''
Created on 3 nov. 2015

@author: paul
'''
from Domain.Movies import Movies
from Domain.MExceptions import MovieException

class MovieRepository:
    def __init__(self):
        """
        Creates an instance of the MovieRepository.
        """
        self.__data = []
    
    def __find(self, id):
        '''
        Returns the index movie having the given id.
        Input: id - integer, the id of the movie that is being searched for
        Output: index - if the movie was found, -1 - otherwise 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getID() == id:
                return i
        return -1
    
    def findById(self, id):
        '''
        Returns the movie having the given id.
        Input: id - integer, the id of the movie that is being searched for
        Output: the movie, if found or None otherwise
        '''
        idx = self.__find(id) 
        if idx == -1:
            return None
        return self.__data[idx]
    
    def __findName(self,name):
        '''
        Returns the index having the given Name
        Input: name - a string, the name of the movie is being searched for
        Output: index - if the movie was found, -1 -otherwise
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getTitle() == name:
                return i
        return -1
    def findByName(self,name):
        '''
        Returns the movie having the given name.
        Input: name - string, the string of the movie that is being searched for
        Output: the movie, if found 
        Exception: Raise Movie Exception if the movie is not in the list
        '''
        idx = self.__findName(name) 
        if idx == -1:
            raise MovieException('The title "'+ name +'" does not exist in the list')
        return self.__data[idx]
    
    def add(self, mov):
        '''
        Adds a movie to the repository.
        Input: mov - object of type Movies
        Output: the given movie is added to the repository, if no other movie with the same id exists
        Exceptions: raises MovieException if another movie with the same id already exists
        '''
        if self.findById(mov.getID()) != None:
            raise MovieException('Movie with id "' + str(mov.getID()) + '" already exists!')
        self.__data.append(mov)
        
    def remove(self, id):
        '''
        Removes a movie from the repository, using its id
        Input: id - integer, the id of the movie that must be removed
        Output: if such a movie exists, it is removed and returned
        Exceptions: raises MovieException if a movie with the given id does not exist
        '''
        idx = self.__find(id)
        if idx == -1:
            raise MovieException("There is no movie with id " + str(id) + "!")
        self.__data.pop(idx)
    
    def update(self,id,newTitle,newDescription,newType):
        '''
        Update the movie with the given id
    
        Input: id - integer, the id of the client that must be removed
               newname- a string, the movie new name
               newdescription - string, the movie new description
               newType- string, the new movie type   
        Output: if such a movie exists, it is removed and returned
        Exceptions: raises MovieException if a movie with the given id does not exist
        '''
        idx = self.__find(id)
        if idx == -1:
            raise MovieException("There is no movie with id " + str(id) + "!")
        self.__data[idx].setTitle(newTitle)
        self.__data[idx].setDescription(newDescription)
        self.__data[idx].setType(newType)
    
    def __len__(self):
        '''
        Returns the size of the list of movies
        (Overriding the len() built-in function)
        '''
        return len(self.__data)
    
    def getAll(self):
        '''
        Returns the list of movies
        '''
        return self.__data
    
def testRepository():
    '''
    tests the functions in the curent repository
    '''
    repo= MovieRepository()
    
    m1=Movies(1,"RAGE","D","A")
    m2=Movies(2,"City","D","H")
    
    #test adding movies to repository
    repo.add(m1)
    assert len(repo) == 1
    assert repo.findById(1) == m1
    
    try:
        repo.add(m1)
        assert False
    except MovieException:
        assert True
        
    repo.add(m2)
    assert len(repo) == 2
    assert repo.findById(1) == m1
    assert repo.findById(2) == m2
    
    #Test removing movies from repository
    assert len(repo) == 2
    repo.remove(1)
    assert len(repo) == 1
    assert repo.findById(2) == m2
    assert repo.findById(1) == None
    
    try:
        repo.remove(1)
        assert False
    except MovieException:
        assert True
    
    assert repo.remove(2) == m2
    assert len(repo) == 0
    
if __name__ == '__main__':
    testRepository()