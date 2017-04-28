# FPMovieRental

Write an application for movie rental. The application will store:
Movie: 
<movieId>, <title>,<description>,<genre>.
Client:
<clientId>, <name>, <cnp>.
Rental:
-at your choise
Create an application which allows the user to:
1.
Manage the list of clients and available movies. The application must allow the user to add, 
remove, update, and list both clients and movies. 
2.
Rent or return a movie. A client can rent
an available movie until a given date, as long as they 
have no rented movies that passed their due date for return. A client can return a rented movie 
at any time. Only available movies are available for renting.
3.
Search for clients or movies using any one
of their fields (e.g. movies can be searched for using 
id, title, description or genre). The search must work using case
-insensitive, partial string matching, and must return all matching items.
4.
Create statistics: 
-Most rented movies (alphabetic order).
-Most active clients (alphabetic order). 
-All rentals. All movies currently rented.

5.
Unlimited undo/redo functionality. Each step will undo/redo the previous operation 
performed by the user.
