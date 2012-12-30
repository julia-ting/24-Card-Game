Python Card Game: 24
====



This program is based off the card game 24. I got the idea because 24 is a game 
I have played a lot since childhood and enjoyed quite a bit. I thought this would 
be a fun project.

In the card game, there are two teams. Each team starts out with half of the deck. 
Each person puts the top two cards on the table, face up.

These are the "table cards." There should be four, total, and from these four 
cards the goal is to compute 24. You must use each card, but you can only use 
each card once. You can perform multiplication, division, subtraction, and addition. 
Integers only. 

The program is an input required, two player game from one computer. 

To run the game, call the function play(). 

Here is how the program works:

There are four parts - finding all solutions for 24, finding the solution of an 
input, creating the game, and rotating through the menus.

The first part:

The first part cycles through all the different permutations of a given list of 
4 values. For each permutation, it goes through and performs every possible operation 
combination. If a result equals 24, it returns the solution in a string.

The second part:

The second part takes a user input and splits the string by spaces. 
It appends digits as ints and operations as strings. Then it goes through 
a set of conditionals where for each operation it performs the operation on 
the ints. Then it replaces those three (the two numbers and the operation) 
with the resulting value. It rotates through the list and performs this until 
the list is 1 number.

The third part:

The third part is putting the first and second parts together. Given a user input, 
it prompts for a solution. If the solution is correct, then it adds the cards to 
the respective player's "deck" of cards (which is a list, in Python). If it is 
incorrect, it adds it to the other player's deck, and returns the solution. 

The fourth part:

The fourth part contains the different menus. There is the menu for playing, 
and learning the rules. If you choose to play the game, it brings up the next 
menu for the actual game. Make sure you read the rules carefully! The formatting is very specific. 

There are notes throughout the code to help explain.

Enjoy!
