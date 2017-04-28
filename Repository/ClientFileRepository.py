'''
Created on Nov 30, 2015

@author: Muresan
'''
from Domain.Clients import *
from Repository.ClientsRepository import *


class ClientFileRepository(ClientsRepository):
    '''
    Class used to store/retrieve clients from file
    '''

    def __init__(self, filename):
        ClientsRepository.__init__(self)
        self.__filename = filename
        self.__loadFromFile()

    def __loadFromFile(self):
        '''
        Reads clients from file.
        Input: -
        Output: the clients from the file are stored in memory.
        Exceptions: raises IOError if the file cannot be opened raises CustomException if there are duplicate client ids in the file
         '''
        try:
            f = open(self.__filename, "r")
        except IOError:
            return

        for line in f:
            line = line.strip()
            clientAttributes = line.split("|")
            if len(clientAttributes) != 3:
                continue

            clientId = clientAttributes[0].strip()
            clientName = clientAttributes[1].strip()
            clientCNP = clientAttributes[2].strip()
            client = Clients(int(clientId), clientName, int(clientCNP))
            ClientsRepository.add(self, client)

        f.close()

    def add(self, cl):
        '''
        Overrides the "add" function from the main clients repository
        Input:-
        Output: all the clients are stored in both memory&file 
        Exceptions:-
        '''
        ClientsRepository.add(self, cl)
        self.__storeToFile()

    def remove(self, id):
        '''
        Overrides the "remove" function from the main clients repository
        Input:-
        Output: all the clients are stored in both memory&file 
        Exceptions:-
        '''
        ClientsRepository.remove(self, id)
        self.__storeToFile()

    def update(self, id, newName, NewCNP):
        '''
        Overrides the "update" function from the main clients repository
        Input:-
        Output: all the clients are stored in both memory&file 
        Exceptions:-
        '''
        ClientsRepository.update(self, id, newName, NewCNP)
        self.__storeToFile()

    def __storeToFile(self):
        '''
            Stores all the clients in the file.
            Input: -
            Output: all the clients from the repository are stored to the file self.__filename
        '''

        f = open(self.__filename, 'w')
        for e in self.getAll():
            f.write(str(e.getID()) + "|" + e.getName() + "|" + str(e.getCNP()) + '\n')

        f.close()
