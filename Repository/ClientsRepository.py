'''
Created on 3 nov. 2015

@author: paul
'''
from Domain.Clients import Clients
from Domain.MExceptions import MovieException


class ClientsRepository:
    def __init__(self):
        """
        Creates an instance of the Clients.
        """
        self.__data = []

    def __findID(self, id):
        '''
        Returns the index having the given id.
        Input: id - integer, the id of Client that is being searched for
        Output: index - if the client was found, -1 - otherwise 
        Exception: - 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getID() == id:
                return i
        return -1

    def __checkCNP(self, CNP):
        '''
        Checks if there is another client that has the same CNP
        Input: CNP - an integer, the client CNP 
        Output: True if there is another client with the same CNP, false otherwise
        Exception: -
        '''
        for cl in self.__data:
            if cl.getCNP() == CNP:
                return True
        return False

    def findById(self, id):
        '''
        Returns the Client having the given id.
        Input: id - integer, the id of the Client that is being searched for
        Output: the client, if found or None otherwise
        '''
        idx = self.__findID(id)
        if idx == -1:
            return None
        return self.__data[idx]

    def __findName(self, name):
        '''
        Returns the index having the given Name
        Input: name - a string, the name of the client is being searched for
        Output: index - if the client was found, -1 -otherwise
        Exceptions: -
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getName() == name:
                return i
        return -1

    def findByName(self, name):
        '''
        Returns the Client having the given name.
        Input: id - integer, the id of the Client that is being searched for
        Output: the client, if found or None otherwise
        Exceptions: raises MovieExceptions if the client with the given name does not exist
        '''
        idx = self.__findName(name)
        if idx == -1:
            raise MovieException('The name "' + name + '" does not exist in the clients list.')
        return self.__data[idx]

    def add(self, cl):
        '''
        Adds a Client to the repository.
        Input: cl - object of type Clients
        Output: the given client is added to the repository, if no other client with the same id exists
        Exceptions: raises MovieException if another client with the same id already exists
        '''
        if self.findById(cl.getID()) != None:
            raise MovieException('Client with id "' + str(cl.getID()) + '" already exists!')
        if self.__checkCNP(cl.getCNP()):
            raise MovieException('There is already a client with the CNP:' + str(cl.getCNP()))
        self.__data.append(cl)

    def remove(self, id):
        '''
        Removes a Client from the repository, using its id
        Input: id - integer, the id of the client that must be removed
        Output: if such a client exists, it is removed and returned
        Exceptions: raises MovieException if a client with the given id does not exist
        '''
        idx = self.__findID(id)
        if idx == -1:
            raise MovieException("There is no client with id " + str(id) + "!")
        return self.__data.pop(idx)

    def __len__(self):
        '''
        Returns the size of the list of clients
        (Overriding the len() built-in function)
        '''
        return len(self.__data)

    def getAll(self):
        '''
        Returns the list of clients
        '''
        return self.__data

    def update(self, id, newName, NewCNP):
        '''
        Update the client with the given id
        Input: id - integer, the id of the client that must be removed
               newName- a string, the client new name
               newCNP - integer, the client new CNP    
        Output: if such a client exists, it is removed and returned
        Exceptions: raises MovieException if a client with the given id does not exist, and the there is another client with the same CNP
        '''
        idx = self.__findID(id)
        if idx == -1:
            raise MovieException("There is no client with id " + str(id) + "!")
        if self.__checkCNP(NewCNP):
            raise MovieException('There is already a client with the CNP:' + str(NewCNP))

        self.__data[idx].setName(newName)
        self.__data[idx].setCNP(NewCNP)


def testRepository():
    '''
    Test functions of the current repository
    '''
    repo = ClientsRepository()

    c1 = Clients(1, "Doina", 2602020060033)
    c2 = Clients(2, "Simi", 1601010060022)

    assert len(repo) == 0
    repo.add(c1)
    assert len(repo) == 1
    assert repo.findById(1) == c1

    try:
        repo.add(c1)
        assert False
    except MovieException:
        assert True

    repo.add(c2)
    assert len(repo) == 2
    assert repo.findById(1) == c1
    assert repo.findById(2) == c2

    assert len(repo) == 2
    repo.remove(1)
    assert len(repo) == 1
    assert repo.findById(2) == c2
    assert repo.findById(1) == None

    try:
        repo.remove(1)
        assert False
    except MovieException:
        assert True

    assert repo.remove(2) == c2
    assert len(repo) == 0


if __name__ == '__main__':
    testRepository()
