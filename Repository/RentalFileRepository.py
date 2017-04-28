'''
Created on Nov 30, 2015

@author: Muresan
'''
from Domain.Rental import *
from Domain.Clients import *
from Domain.Movies import *

from Repository.RentalRepository import *


class RentalFileRepository(RentalRepository):
    '''
    Class that is used for retrieve/store rentals from files
    '''

    def __init__(self, fileName):
        RentalRepository.__init__(self)
        self.__filename = fileName
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
            rentalAttributes = line.split("|")
            if len(rentalAttributes) != 9:
                continue

            clientId = rentalAttributes[0].strip()
            clientName = rentalAttributes[1].strip()
            clientCNP = rentalAttributes[2].strip()
            client = Clients(int(clientId), clientName, int(clientCNP))

            movieId = rentalAttributes[3].strip()
            movieTitle = rentalAttributes[4].strip()
            movieD = rentalAttributes[5].strip()
            movieT = rentalAttributes[6].strip()
            movie = Movies(int(movieId), movieTitle, movieD, movieT)

            startDate = datetime.strptime(rentalAttributes[7], '%m/%d/%Y')
            if rentalAttributes[8] != '0':
                endDate = datetime.strptime(rentalAttributes[8], '%m/%d/%Y')
            else:
                endDate = 0

            ren = Rental(client, movie, startDate, endDate)
            RentalRepository.add(self, ren)

    def add(self, ren):
        '''
        Overrides the 'add' function from the main rental Repository
        Input:-
        Output:- the list of rentals is stored both in memory&file
        Exceptions:-
        '''
        RentalRepository.add(self, ren)
        self.__storeToFile()

    def returnMovie(self, m):
        '''
        Overrides the 'returnMovie' function from the main rental Repository
        Input:-
        Output:- the updated list of rentals is stored both in memory&file
        Exceptions:-
        '''
        rental = RentalRepository.returnMovie(self, m)
        self.__storeToFile()
        return rental

    def __storeToFile(self):
        '''
        Stores all the rentals in the file.
        Input: -
        Output: all the rentals from the repository are stored to the file self.__filename
        '''
        f = open(self.__filename, 'w')

        for r in self.getAll():
            m = r.getMovie()
            c = r.getClient()
            startStr = r.getStart().strftime('%m/%d/%Y')
            if str(r.getEnd()) == "0":
                endStr = "0"
            else:
                endStr = r.getEnd().strftime('%m/%d/%Y')
            f.write(str(c.getID()) + "|" + c.getName() + "|" + str(c.getCNP()) + "|" + str(
                m.getID()) + "|" + m.getTitle() + "|" + m.getDescription() + "|" + m.getType() + "|" + startStr + "|" + endStr + '\n')

        f.close()
