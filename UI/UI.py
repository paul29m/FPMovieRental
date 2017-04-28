'''
Created on 3 nov. 2015

@author: paul
'''
from datetime import *
from Domain.Clients import Clients
from Domain.Movies import Movies
from Domain.MExceptions import MovieException
from Domain.Rental import *
from Validator.ClientValidator import *
from Validator.MovieValidator import *
from queue import Empty
 

class UI:
    def __init__(self, movController,clController,renContrller,undoCtrl):
        self.__mc = movController
        self.__cc = clController
        self.__rc = renContrller
        self.__uc = undoCtrl
        
    @staticmethod
    def printMenu():
        str = '\nAvailable commands:\n'
        str += '\t 1 - Manage Clients \n'
        str += '\t 2 - Manage Movies \n'
        str += '\t 3 - Rent a movie \n'
        str += '\t 4 - Return movie \n'
        str += '\t 5 - Show all rentals \n'
        str += '\t 6 - Statistics \n'
        str += '\t 7 - Undo \n'
        str += '\t 8 - Redo \n'
        str += '\t 0 - Exit \n'
        print(str)
    
    @staticmethod  
    def validInputCommand(command):
        '''
        Verifies if the given command is a valid one.
        Input: command - the given command - a string
        Output: True - if the command id valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '5', '6' , '7', '8' , '0'];
        return (command in availableCommands)

    @staticmethod
    def readPositiveInteger(msg):
        '''
        Reads a positive integer
        Input: msg - the message to be shown to the user before reading.
        Exceptions: a message of MovieException is shown if there is something wrong
        Output: A positive integer 
        '''
        res = 0
        while True:
            try:
                res = int(input(msg))
                if res < 0:
                    raise ValueError()
                break
            except ValueError:
                print("The value you introduced was NOT a positive integer.")
        return res
    
        
    def __addMovieMenu(self):
        '''
        Adds a movie to the list.
        Input: -
        Exceptions: a message of MovieException is shown if there is something wrong
        Output: a new movie is read and added (if there is no other movie with the same id).
        '''
        
        id = UI.readPositiveInteger("Please enter the movie id: ")
        title = input("Please enter the movie title : ")
        description = input("Please enter the movie description : ")
        type = input("Please enter the movie type: ")
        
        try:
            mov = Movies(id, title,description, type)
            MovieValidator.validateMovie(mov)
            self.__mc.addMovie(mov)
            print("Action done!")
        except MovieException as ex:
            print(ex)
        
    def __removeMovieMenu(self):
        '''
        Removes a movie from the list.
        Input: -
        Exceptions: a message of MovieException is shown if there is something wrong
        Output: the medicine is removed, if it exists.
        '''
        id = UI.readPositiveInteger("Please enter the movie id: ")
        
        try:
            self.__mc.removeMovie(id)
            print("Action done!")
        except MovieException as ex:
            print(ex)
    def __updateMovieMenu(self):
        """
        Updates a movie whit a given id
        Input: -
        Exceptions: a message of MovieException is shown if there is something wrong
        output: the movie is updated if it exist
        """
        id = UI.readPositiveInteger("Please enter the movie id: ")
        title = input("Please enter movie title: ")
        description= input("Please enter movie description: ")
        type= input("Please enter movie type: ")
        try:
            self.__mc.updateMovie(id,title,description,type)
            print("Action done!")
        except MovieException as ex:
            print(ex)
    
    def __showAllMoviesMenu(self):
        '''
        Prints all movies in the list
        '''
        mov= self.__mc.getAll()
        if len(mov) == 0:
            print("There are no movies in the list.")
        else:
            for e in mov:
                print(e)
    def __addClientMenu(self):
        '''
        Adds a client to the list
        Input: -
        Exceptions: a message of MovieException is shown if there is something wrong
        Output: a new client is read and added (if there is no other client with the same id).
        '''
        id = UI.readPositiveInteger("Please enter the client id: ")
        name = input("Please enter the client name: ")
        CNP = UI.readPositiveInteger("Please enter client CNP: ")
        try:
            cl= Clients(id,name,CNP)
            ClientValidator.validateC(cl)
            self.__cc.addClient(cl)
            print("Action done!")
        except MovieException as ex:
            print(ex)
    
    def __removeClientMenu(self):
        '''
        Remove a client from the list
        Input:-
        Exceptions: -
        Output: the client is removed(if there is such client)
        '''
        id = UI.readPositiveInteger("Please enter the client id: ")
        
        try:
            self.__cc.removeClient(id)
            print("Action done!")
        except MovieException as ex:
            print(ex)
    def __updateClientsMenu(self):
        """
        Updates a client with the given id
        Input:-
        Exceptions: a message of MovieException is shown if there is something wrong
        Output: the updated client if there is one on the id
        """
        id = UI.readPositiveInteger("Please enter the client id: ") 
        name= input("Please enter the new client name: ")
        CNP= UI.readPositiveInteger("Please enter the new client CNP: ")
        try:
            self.__cc.updateClient(id,name,CNP)
            print("Action done!")
        except MovieException as ex:
                print(ex)
        
    def __showAllClientsMenu(self):
        """
        Shows the list of all clients
        Input:-
        Exceptions: -
        Output: the list of clients
        """
        cl= self.__cc.getAll()
        if len(cl) == 0:
            print("There are no clients in the list.")
        else:
            for e in cl:
                print(e)
    def __findClientByname(self):
        """
        Finds the client by name 
        Input: -
        Exceptions: - a message of MovieException is shown if there is something wrong
        Output: the all information of a client
        """
        name= input("Please enter the client name: ")
        try:
            cl=self.__cc.findByName(name)
            print(cl)
        except MovieException as e:
            print(e)
            
    def __findMovieByTitle(self):
        """
        Finds the movie by Title 
        Input: -
        Exceptions: - a message of MovieException is shown if there is something wrong
        Output: the all information the movie
        """
        name= input("Please enter the movie title: ")
        try:
            mov=self.__mc.findByName(name)
            print(mov)
        except MovieException as e:
            print(e)
        
    def __findMovieByID(self):
        """
        Finds the movie by ID
        Input: -
        Output: the all information the movie
        Exceptions: a message of MovieException is shown if there is something worng
        """
        id = UI.readPositiveInteger("Please enter the movie id: ")
        try:
            mov=self.__mc.findById(id)
            print(mov)
        except MovieException as e:
            print(e)
    
    def __findClientByID(self):
        """
        Finds the client by id
        Input: -
        Output: the all information of a client
        Exceptions: - a message of MovieException is shown if there is something worng
        """
        id = UI.readPositiveInteger("Please enter the client id: ")
        try:
            cl=self.__cc.findByID(id)
            print(cl)
        except MovieException as e:
            print(e)
        
    def __addRentalMenu(self):
        """
        Makes a rental
        Input:-
        Output: the rental is added to rental list
        Exceptions: - a message of MovieException is shown if there is something wrong
        """
        try:
            title= input("Please enter the movie title you want to rent: ")
            mov=self.__mc.findByName(title)
            name= input("Please enter the client name: ")
            cl=self.__cc.findByName(name)
            ren=Rental(cl,mov,datetime.now(),0)
            self.__rc.addR(ren)
            print("The movie was rented")
        except MovieException as e:
            print(e)
    def __showAllRentalsMenu(self):
        '''
        Shows the list of all clients
        Input:-
        Exceptions: -
        Output: - shows the list of all rentals
        '''
        r= self.__rc.show()
        if len(r) == 0:
            print("There are no rentals made.")
        else:
            for e in r:
                print(e)
    
    def __returnMovieMenu(self):
        '''
        Return a rent movie
        Input:
        Exceptions: - a message of MovieException is shown if there is something wrong
        Output: the rental list is modified, if the movie is in the rental list
        '''
        try:
            title=input("Please enter movie title: ")
            mov=self.__mc.findByName(title)
            self.__rc.returnMovie(mov)
            print("The movie was successfully returned")
        except MovieException as e:
            print(e)
            
    def __mostRentedMovies(self):
        '''
        Shows a list with the most rented movies
        Input: -
        Exceptions: -
        Output: -
        '''
        mov= self.__rc.mostRentedMovies()
        if len(mov) == 0:
            print("There are no movies rented")
        else:
            for e in mov:
                print("\t" + str(e))

    
    
    def __mostActiveClients(self):
        '''
        Shows a list with the most active clients
        Input: -
        Exceptions: -
        Output: - 
        '''
        cl= self.__rc.mostActiveClients()
        if len(cl) == 0:
            print("There are no active clients ")
        else:
            for e in cl:
                print(e)
    
    def __clientsOrdonator(self):
        '''
        Orders active clients alphabetical
        Input: -
        Exceptions: -
        Output: -
        '''
        cl= self.__rc.clientsOrdonator()
        if len(cl) == 0:
            print("There are no active clients ")
        else:
            for e in cl:
                print(e)
    
    def __moviesOrdonator(self):
        '''
        Orders rented movies alphabetical
        Input: -
        Exceptions: -
        Output: -
        '''
        mov= self.__rc.movieOrdonator()
        if len(mov) == 0:
            print("There are no movies rented")
        else:
            for e in mov:
                print(e)
    
    @staticmethod  
    def validInputCommand2(command):
        '''
        Verifies if the given command is a valid one.
        Input: command - the given command - a string
        Output: True - if the command id valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '0'];
        return (command in availableCommands)
    @staticmethod  
    def validInputCommand3(command):
        '''
        Verifies if the given command is a valid one.
        Input: command - the given command - a string
        Output: True - if the command id valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '5', '6' , '0'];
        return (command in availableCommands)

    @staticmethod
    def printMenuStatistics():
        str = 'Chose the list of:\n'
        str +='\t 1 - Most rented movies \n'
        str +='\t 2 - Most active clients \n'
        str +='\t 3 - Rented movies ordered alphabetic \n'
        str +='\t 4 - Clients with rented movies ordered alphabetic\n'
        str +='\t 0 - Return to main menu'
        print(str)
        
    def __showStatisticsMenu(self):
        '''
        Shows the statistics menu
        Input: -
        Exceptions: -
        Output: -
        '''
        commandDict= {'1': self.__mostRentedMovies,
                      '2': self.__mostActiveClients,
                      '3': self.__moviesOrdonator,
                      '4': self.__clientsOrdonator
                    }
        UI.printMenuStatistics()
        command = input("Please enter your command: ")
        while not UI.validInputCommand2(command):
            print("Please enter a valid command!")
            command = input("Please enter your command: ")
        if command=='0':
            return 
        commandDict[command]()
        
    @staticmethod
    def printMenuClients():
        str ='Select an action: \n'
        str+='\t1 - Add client \n'
        str+='\t2 - Remove a client \n'
        str+='\t3 - Update a client \n'
        str+='\t4 - Find a client by id \n'
        str+='\t5 - Find a client by name\n'
        str+='\t6 - Show all clients\n'
        str+='\t0 - Return to main menu.\n'
        print(str)
        
    def __manageClientsMenu(self):
        '''
        Shows the clients menu
        Input: -
        Exceptions: -
        Output: -
        '''
        commandDict = {'1': self.__addClientMenu,
                       '2': self.__removeClientMenu,
                       '3': self.__updateClientsMenu,
                       '4': self.__findClientByID,
                       '5': self.__findClientByname,
                       '6': self.__showAllClientsMenu
                       }
        UI.printMenuClients()
        command = input("Please enter your command: ")
        while not UI.validInputCommand3(command):
            print("Please enter a valid command!")
            command = input("Please enter your command: ")
        if command == '0':
            return 0
        commandDict[command]()
    
    @staticmethod
    def printMenuMovies():
        str ='Select an action: \n'
        str+='\t 1 - Add movie \n'
        str+='\t 2 - Remove a movie \n'
        str+='\t 3 - Update a movie \n'
        str+='\t 4 - Find a movie by id\n'
        str+='\t 5 - Find a movie by title\n'
        str+='\t 6 - Show all movies\n'
        str+='\t 0 - Return to main menu.'
        print(str)
    def __manageMoviesMenu(self):
        '''
        Shows the movie menu
        Input: -
        Exceptions: -
        Output: -
        '''
        commandDict = {'1': self.__addMovieMenu,
                       '2': self.__removeMovieMenu,
                       '3': self.__updateMovieMenu,
                       '4': self.__findMovieByID,
                       '5': self.__findMovieByTitle,
                       '6': self.__showAllMoviesMenu,
                       }
        UI.printMenuMovies()
        command = input("Please enter your command: ")
        while not UI.validInputCommand3(command):
            print("Please enter a valid command!")
            command = input("Please enter your command: ")
        if command == '0':
            return 0
        commandDict[command]()
    def __undoMenu(self):
        '''
        Undoes the last operation made
        '''
        res = self.__uc.undo()
        if res == True:
            print("Undo successfully made.")
        else:
            print("No more undo operations are possible.")
    
    def __redoMenu(self):
        '''
        Redoes the last undone operation
        '''
        res = self.__uc.redo()
        if res == True:
            print("Redo successfully made.")
        else:
            print("No more redo operations are possible.")
    
    def mainMenu(self):
        '''
        Shows the main menu
        Input: -
        Exceptions: -
        Output: -
        '''
        commandDict = {'1': self.__manageClientsMenu,
                       '2': self.__manageMoviesMenu,
                       '3': self.__addRentalMenu,
                       '4': self.__returnMovieMenu,
                       '5': self.__showAllRentalsMenu,
                       '6': self.__showStatisticsMenu,
                       '7': self.__undoMenu,
                       '8': self.__redoMenu
                        }  
        while True:
            UI.printMenu()
            command = input("Please enter your command: ")
            while not UI.validInputCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return 0
            commandDict[command]()
            
    @staticmethod
    def chooseMemoryMenu():
        '''
        Shows the menu where the user can choose between files or Empty
        Input: -
        Exceptions: -
        Output: method- 1 or 0 depending on user choice 
        ''' 
        while True:
            method=input("Press '1' for reading from file or '0' for using predefine data: ")
            if method=='1'or method=='0':
                return method
            else: 
                print("Wrong input!")
            