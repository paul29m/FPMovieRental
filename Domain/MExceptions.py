'''
Created on 3 nov. 2015

@author: paul
'''
class MovieException(Exception):
        def __init__(self, msg):
            self.__message = msg
    
        def __str__(self):
            return self.__message
        