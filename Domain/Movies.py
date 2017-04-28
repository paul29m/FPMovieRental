'''
Created on 3 nov. 2015

@author: paul
'''
from Domain.MExceptions import MovieException
class Movies:
    def __init__(self, id, title, description, type):
        """
        Creates a new instance of Movies.
        """
        self.__id=id
        self.__title=title
        self.__description=description
        self.__type=type
    def getID(self):
        """
        Returns the movie id. This is a read-only property as we do not have a setter
        """
        return self.__id
    
    def getTitle(self):
        """
        Returns the movie title. This is a read-only property as we do not have a setter
        """
        return self.__title
    
    def getDescription(self):
        """
        Returns the movie description. This is a read-only property
        """
        return self.__description
        
    def getType(self):
        """
        Returns the movie type. This is a read-only property
        """
        return self.__type
    
    def setID(self, id):
        """
        Setter for movie id.
        """ 
        if id<0:
            raise MovieException("Movie id must be a positive integer")
        else:
            self.__id=id
    def setTitle(self, title):
        """
        Setter for title.
        """
        self.__title=title
    def setDescription(self, description):
        """
        Setter for movie description.
        """
        self.__description=description
    def setType(self, type):
        """
        Setter for movie type.
        """
        self.__type=type
    
    def __str__(self):
        return str(self.__id) + "\t title: " + self.__title + "\t type: " + self.__type + "\t description: " + self.__description 

def testMovies(self):
    """
    Test getters and setters.
    """
    m=Movies(1,"The revenge","John is a retired cop","action")
    assert m.getID()==1
    assert m.getTitle()== "The revenge"
    assert m.getDescription()== "John is a retired cop"
    assert m.getType()=="action"
    
    m.setTitle("The Mistery")
    m.setType("Horror")
    
    assert m.getTitle()== "The Mistery"
    assert m.getType()== "Horror"
    try:
        m.setID(-1)
        assert False
    except MovieException:
        assert True
if __name__ == '__main__':
    testMovies()