'''
Created on 12 nov. 2015

@author: paul
'''
from Domain.Movies import *
from Domain.MExceptions import *

class MovieValidator:
    @staticmethod
    def validateName(name):
        '''
        Checks if the name of a movie field is a valid one
        Input: name - a string, the movie filed name
        Output: true if is valid, false otherwise
        '''
        if len(name)<3:
            return False
        if name[0]<'A' and name[0]>'Z':
            return False
        for i in range(len(name)-1):
            if name[i+1]<'a'and name[i+1]>'z':
                return False
        return True
    
    @staticmethod
    def validateMovie(m):
        '''
        Checks if the movie is valid
        Input: m- an instance of movie
        Output: returns None if instance is valid, otherwise raises an Exception detailing the error(s)
        '''
        msg=""
        if isinstance(m, Movies)==False:
            raise MovieException("The movie is not a valid one")
        if MovieValidator.validateName(m.getTitle())==False:
            msg+="-title not valid;\n"
        if MovieValidator.validateName(m.getType())==False:
            msg+="-type not valid;\n"
        if MovieValidator.validateName(m.getDescription())==False:
            msg+="-description not valid;\n"
        if len(msg)!=0:
            raise MovieException("The movie has the following:\n"+msg+"\n NOTE: All fields must start with a capital letter")

def testMovieValidator():
    '''
    Test the movie validator
    '''
    pass
if __name__=='__main__':
    testMovieValidator()