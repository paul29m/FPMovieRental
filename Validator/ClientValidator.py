'''
Created on 12 nov. 2015

@author: paul
'''
from Domain.Clients import *
from Domain.MExceptions import *


class ClientValidator:
    @staticmethod
    def validateCNP(CNP):
        '''
        Verify if the given ID is a valid one:
        -the first number must be 1 or 2
        -the 2-3 digits must be the year of birth
        -the 4-5 digits the mouth 
        -the 6-7 digits are the day 
        -the 8-9 digits are the locality
        -the 10-12 digits are random
        -the 13 digit is the control one 
        '''
        CNP = str(CNP)
        if len(CNP) != 13:
            return False
        if CNP[0] != '1' and CNP[0] != '2':
            return False
        year = int(CNP[1]) * 10 + int(CNP[2])
        if year > 99:
            return False
        mouth = int(CNP[3]) * 10 + int(CNP[4])
        if mouth > 12:
            return False
        day = int(CNP[5]) * 10 + int(CNP[6])
        if day > 31:
            return False
        if mouth == 2 and day > 28:
            return False
        locality = int(CNP[7]) * 10 + int(CNP[8])
        if locality > 52:
            return False

        control = int(CNP[0]) * 2 + int(CNP[1]) * 7 + int(CNP[2]) * 9 + int(CNP[3]) * 1 + int(CNP[4]) * 4 + int(
            CNP[5]) * 6 + int(CNP[6]) * 3 + int(CNP[7]) * 5 + int(CNP[8]) * 8 + int(CNP[9]) * 2 + int(
            CNP[10]) * 7 + int(CNP[11]) * 9
        if int(CNP[12]) != ((control % 11) % 10):
            return False
        return True

    @staticmethod
    def validateName(name):
        '''
        Checks if the name of a client is a valid one
        Input: name - a string, the client name
        Output: true if is valid, false otherwise
        '''
        if len(name) < 3:
            return False
        if name[0] < 'A' and name[0] > 'Z':
            return False
        for i in range(len(name) - 1):
            if name[i + 1] < 'a' and name[i + 1] > 'z':
                return False
        return True

    @staticmethod
    def validateC(client):
        '''
        Validate if provided Car instance is valid
        Input: client - Instance of Clients
        Output: returns None if instance is valid, otherwise raises an Exception detailing the error(s)
        '''
        msg = ""
        if isinstance(client, Clients) == False:
            raise MovieException("You enter an object that is not a Clients instance")
        if ClientValidator.validateName(client.getName()) == False:
            msg += "Must have valid name\n"
        if ClientValidator.validateCNP(client.getCNP()) == False:
            msg += "Invalid CNP\n"
        if len(msg) != 0:
            raise MovieException("Invalid client:\n" + msg)


def testClientValidator():
    '''
        Tests the client validator class
    '''
    cnp = 1951129060039
    assert ClientValidator.validateCNP(cnp) == True
    cnp = 100000000000000
    assert ClientValidator.validateCNP(cnp) == False
    cnp = 234556
    assert ClientValidator.validateCNP(cnp) == False
    cnp = 1991212040004
    assert ClientValidator.validateCNP(cnp) == False
    assert ClientValidator.validateCNP(1951129060038) == False
    assert ClientValidator.validateName("  ") == False
    client = Clients(1, "", 0)
    try:
        ClientValidator.validateC(client)
        assert False
    except MovieException:
        assert True

    client = Clients(1, "22", 1951129060039)
    try:
        ClientValidator.validateC(client)
        assert False
    except MovieException:
        assert True

    client = Clients(1, "Doina", 1951129060038)
    try:
        ClientValidator.validateC(client)
        assert False
    except MovieException:
        assert True


if __name__ == '__main__':
    testClientValidator()
