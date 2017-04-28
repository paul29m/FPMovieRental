'''
Created on 3 nov. 2015

@author: paul
'''
from Domain.MExceptions import MovieException

class Clients:
    def __init__(self, clientID, name, CNP):
        self.__ID=clientID
        self.__name=name
        self.__CNP=CNP
        
    def getID(self):
        """
        Returns the client ID
        """
        return self.__ID
    def getName(self):
        """
        Returns the client name
        """
        return self.__name
    
    def getCNP(self):
        """
        Returns the client CNP
        """
        return self.__CNP
    
    def setName(self,name):
        """
        Setter for the client name
        """
        self.__name=name
    def setCNP(self,CNP):
        """
        Setter for client CNP
        """
        if CNP>999999999999:
            self.__CNP=CNP
        else:
            raise MovieException("Enter a valid CNP")
        
    def __str__(self):
        return str(self.__ID) + "\t name: " + self.__name + "\t CNP: " + str(self.__CNP)
    
def testClients():
    """
    test setters and getters
    """
    c=Clients(1,"Muri",1951129060039)
    assert c.getID()== 1
    assert c.getCNP()==1951129060039
    assert c.getName()=="Muri"
    
    c.setCNP(1951126060039)
    assert c.getCNP()==1951126060039
    
    c.setName("Doina")
    assert c.getName()=="Doina"
    
    try:
        c.setCNP(26)
        assert False
    except MovieException:
        assert True
        
if __name__ == '__main__':
    testClients()