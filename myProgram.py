#Julia Ting
#julia.ting@gatech.edu
#I worked on this with the help of some people from the orgs room, asking questions
#and being given input & advice. Jarvis Johnson helped me find itertools.
#I used class notes as well.

# **** 24 :: A CARD GAME SIMULATED ON PYTHON ****

import itertools as itools
from random import *

#Please read the readme.txt! It explains what this program is!

# CALL THE FUNCTION: play() to play!


#~~~~~~PART 1~~~~~~~~~
#CREATING COMPUTER CALCULATED SOLUTION FOR 24

def printResult(o1, o2, o3, conj, a, b, c, d): #os are operations, cs are conjunctions, letters are numbers
    return("The solution is to %s %d %s %d and %s %d, then %s %d." % (o1, a, conj, b, o2, c, o3, d))


#performs all the operations & if 24 returns solution
#essentially: AI brain
def operationAI(one,two,three,four): #takes in four spots
    cardList = [one, two, three, four]

    if reduce(lambda x,y: x*y, cardList) == 24:
        return("The solution is to multiply them all together!")

    if reduce(lambda x,y: x+y, cardList) == 24:
        return("The solution is to add them all together! WOW! DON'T YOU FEEL SILLY!")

    if one - two + three + four == 24:
        return(printResult("subtract", "add", "add", "from", two, one, three, four))

    if one * two + three + four == 24:
        return(printResult("multiply", "add", "add", "with", one,two,three,four))

    if one * two * three + four == 24:
        return(printResult("multiply", "multiply", "add", "with", one,two,three,four))

    if one * two - three - four == 24:
        return(printResult("multiply", "subtract", "subtract", "with", one,two,three,four))

    if one * two * three - four == 24:
        return(printResult("multiply", "multiply", "subtract", "with", one,two,three,four))

    if (one - two) * three * four == 24:
        return(printResult("subtract", "multiply", "multiply", "from", two,one,three,four))

    if one * two + three - four == 24:
        return(printResult("multiply", "add", "subtract", "with", one,two,three,four))

    if one * (two + three) - four == 24:
        return(printResult("add","multiply","subtract", "with", two,three,one,four))

    if one % two == 0:
        if one / two + three + four == 24:
            return(printResult("divide", "add", "add", "by", one,two,three,four))
        if one / two * three + four == 24:
            return(printResult("divide","multiply","add", "by", one,two,three,four))
        if one / two * three * four == 24:
            return(printResult("divide", "multiply", "multiply", "by", one,two,three,four))
        if one / two * three - four == 24:
            return(printResult("divide", "multiply", "subtract", "by", one,two,three,four))
        if one / two + three - four == 24:
            return(printResult("divide","add","subtract", "by", one,two,three,four))

    if ( one + two ) % three == 0:
        if (one + two) / three + four == 24:
            return(printResult("add", "divide","add", "and", one,two,three,four))
        if (one + two) / three - four == 24:
            return(printResult("add", "divide", "subtract", "and", one,two,three,four))
        if (one + two) / three * four == 24:
            return(printResult("add", "divide", "multiply", "and", one,two,three,four))

    if ( one - two ) % three == 0:
        if (one - two) / three + four == 24:
            return(printResult("subtract", "divide", "add", "from", two,one,three,four))
        if (one - two) / three * four == 24:
            return(printResult("subtract", "divide", "multiply", "from", two,one,three,four))


        #else:
    #    return

#ues operations and a given 4 number list to determine if there is a solution. if there is, prints solution
#and returns the four cards
def solve24(l): #l is a list of 4 numbers
    if l == None:
        print("agh error")
        return

    for perm in itools.permutations(l): #gives tuples
        l = list(perm)
        #print(l)
        one = l[0]
        two = l[1]
        three = l[2]
        four = l[3]
        s = operationAI(one, two, three, four)
        if type(s) == type("string"):
            return s



#~~~~~~~~~PART 2:~~~~~~~~~
#CREATING CALCULATOR FOR HUMAN INPUT SOLUTION
#TAKES IN STRING AND PRODUCES A NUMBER


#changeValue
#takes in index, replaces index with new value and deletes surrounding indices from the list
#both should be numbers (ints), and takes in list to act it on

def changeValue(index,newValue,itemList):
    itemList[index] = newValue
    del(itemList[index+1]) #must delete to the right first otherwise indices will shift
    del(itemList[index-1])


#changeValueParenthesis
#changeValue for parenthesis
#takes in index of operation sign and deletes two values to the right, then two values to the left
#used for when parenthesis are applicable

def changeValueParenthesis(index,newValue,itemList):
    itemList[index] = newValue
    del(itemList[index+2])
    del(itemList[index+1])
    del(itemList[index-1])
    del(itemList[index-2])

#operate
#goes through list given an index and the values to the left
#and right of the index, and performs operations in order given in original list

def operate(index,left,right, iFinal):
    if type(iFinal[index]) == type(5):
        return len(iFinal)

    if iFinal[index] == "*":
        r = left * right
        changeValue(index,r,iFinal)
        length = len(iFinal)
        return length
    if iFinal[index] == "/":
        r = left // right
        changeValue(index,r,iFinal)
        length = len(iFinal)
        return length
    if iFinal[index] == "+":
        r = left + right
        changeValue(index,r,iFinal)
        length = len(iFinal)
        return length
    if iFinal[index] == "-":
        r = left - right
        changeValue(index,r,iFinal)
        length = len(iFinal)
        return length

#operatesParenthesis
#operate for parenthesis
#takes in index of the left parenthesis & right parenthesis
#gets values between and performs the operation
#parenthesis will always be 0 and 4

def operateParenthesis(newList,iFinal):
    left = newList[1]
    right = newList[3]
    operation = newList[2]
    if operation == "*":
        r = left * right
        length = len(iFinal)
        return (length,r)
    if operation == "/":
        r = left // right
        length = len(iFinal)
        return (length,r)
    if operation == "+":
        r = left + right
        length = len(iFinal)
        return (length,r)
    if operation == "-":
        r = left - right
        length = len(iFinal)
        return (length,r)


#rotate
#rotates through indices for changing length of iFinal

def rotate(length,iFinal):
    for index in range(length): #length of iFinal
        left = iFinal[index-1]
        right = iFinal[index+1]
        new = operate(index,left,right,iFinal)
        if new != length:
            length = new
            return length

#rotateParenthesis
#rotate for parenthesis
#rotates through list and finds parenthesis
#if parenthesis, goes inside and operates
#returns length of list as iFinal changes

def rotateParenthesis(length,iFinal):
    if "(" not in iFinal:
        length = len(iFinal)
        return (length,iFinal)
    else:
        leftP = 0
        rightP = 0
        for index in range(len(iFinal)):
                if iFinal[index] == "(":
                    leftP = index
                if iFinal[index] == ")":
                    rightP = index
        if rightP - leftP != 4:
            print("Man your formatting...tsktsk didn't work!")
            return None #here stops for parenthesis() function
        else:
            newList = iFinal[leftP:rightP+1] #want to include right most parenthesis, creates copy
            length,value = operateParenthesis(newList,iFinal)
            operatorIndex = leftP + 2
            changeValueParenthesis(operatorIndex,value,iFinal)
            length = len(iFinal)
            return (length,iFinal)




#this function checks for parenthesis & if inside solution
#operates on them, then returns the new iFinal
#takes in list, gives back list

def parenthesis(iFinal):
    if "(" not in iFinal:
        return iFinal
    else:
        length = len(iFinal)
        while "(" in iFinal:

            if length != None:
                length,iFinal = rotateParenthesis(length,iFinal)

            else:
                return(iFinal)
        return(iFinal)



#operationInput
#should return a single integer
#a.isdigit() returns True/False for a string
#function that takes in string and performs operation written
#using helper functions

def operationInput(i):
                                        #constructs iFinal
    split = i.split()                   #splits string
    iFinal = []                         #list of operatives and ints
    for item in split:
        if item.isdigit():
            iFinal.append(int(item))
        else:
            iFinal.append(item)

    iFinal = parenthesis(iFinal)
    length = len(iFinal)

    while length != 1:
        length = rotate(length,iFinal)
    return(iFinal[0])




#~~~~~~PART 3:~~~~~~~
#CREATING THE GAME & MAKING THE DECK

#takes the given card number value, the list, and removes it from that list, but returns the value in a list

def removeCard(card,player):
    for index in range(len(player)):
        if player[index] == card:
            d = player[index]
            del(player[index])
            return([d])

#generates two randomly generated, even halves of deck
#should just use this at the start of each game

def shuffledSplit():
    deck = [1] * 4 + [2] * 4 + [3] * 4 + [4] * 4 + [5] * 4 + [6] * 4 + [7] * 4 + [8] * 4 + [9] * 4 + [10] * 4 + [11] * 4 + [12] * 4 + [13] * 4
    half1 = sample(deck,26)
    for card in half1:
        removeCard(card,deck)
    return (half1, deck)

#function takes in two lists of "cards", from each player & randomly chooses two from each list
#NOTE: IN THIS FUNCTION SHOULD BE A WAY TO HAVE A "GAME OVER"

def chooseCards(player1,player2):
    try:
        if len(player1) >= 2 and len(player2) >= 2:
            card1 = choice(player1)
            one = removeCard(card1, player1)
            card2 = choice(player1)
            two = removeCard(card2, player1)
            card3 = choice(player2)
            three = removeCard(card3, player2)
            card4 = choice(player2)
            four = removeCard(card4, player2)
            return one + two + three + four
        else:
            if len(player1) < 2:
                return("person1")
            if len(player2) < 2:
                return("person2")
    except:
        print("Bye!")
        return 0

#takes in list of 4 numbers

def twentyFourChoice(tableCards):
    options = ["1","2", "3"]
    try:
        while True:
            choice = input("Solve for 24!\n\nThe card values are %d, %d, %d, %d. \n\n1. Player 1: I GOT IT OH EM GEE!! \n2. Player 2: ME ME ME ME PICK ME! \n3. We give up :( We want the next four cards. \n0. GOTTA RUN PEACE (Quit Game) \n\nChoose your option!" % (tableCards[0],tableCards[1],tableCards[2],tableCards[3]))
            if choice == "0":
                print("Aww, bye! I hope you enjoyed playing.")
                return("0")
            elif choice in options:
                return choice
            else:
                print("Whoops! As in whoops on you! That's not an option!")

    except:
        print("Cancel? Okay!")
        return "0"


#THE ACTUAL GAME MECHANICS FUNCTION HERE

#What cards are on the table? Takes in lists of each player's cards. Returns the players decks

def theTable(player1,player2):
    tableCards = chooseCards(player1,player2)
    if tableCards == "person1":
        playAgain = input("Uh ohhhh..looky here, Player 1 doesn't have enough cards. Looks like Player 2 wins! Play again?\n\n1. Yes\n0. No.")
        if playAgain == "0":
            return(0,0)
        else:
            play()
    elif tableCards == "person2":
        playAgain = input("Wow Player 2 DROPPED the BALL! He/she/it RAN OUT OF CARDS! Can you believe that?! Looks like Player 1 wins! Play again?\n\n1. Yes\n0. No.")
        if playAgain == "0":
            return(0,0)
        else:
             play()
    elif tableCards == 0:
        return ("0","0")
    else:

    
        choice = twentyFourChoice(tableCards)
        sAI = solve24(tableCards)
        if sAI == None:
            sAI = "There is no solution."
        if choice == "0":
            return ("0","0")
        elif choice == None:
            return ("0","0")
        else:
    
            while choice != "0" and choice != None: #hit cancel?
                if choice == None:
                    return (0,0)
    
                elif choice == "1":
                    try:
                        i = input("Solve for 24!\n\nThe card values are %d, %d, %d, %d.\n\nWhat is it?!\n\n**IMPORTANT**\nRemember to format your answer correctly!\n(Hint: Use spaces between digits and write in the order you perform the operations)\n(Hinthint: Check the rules page for clarification)" % (tableCards[0],tableCards[1],tableCards[2],tableCards[3]))
                        s = operationInput(i)
                        if s == 24:
                            player1 = player1 + tableCards
                            length1 = len(player1)
                            length2 = len(player2)
                            try:
                                correctChoice = input("Congratulations! You did indeed get it! \n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (length1,length2))#choice after they get it correct!
                                print("Here are four new cards.")
                                return (player1,player2)
                            except:
                                print("Here are four new cards.")
                                return (player1,player2)
                        else:
                            player2 = player2 + tableCards
                            length1 = len(player1)
                            length2 = len(player2)
                            try:
                                incorrectChoice = input("Nope! %s\n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (sAI,length1,length2))#choice after incorrect!
                                print("Here are four new cards.")
                                return (player1,player2)
                            except:
                                print("Here are four new cards.")
                                return (player1,player2)
                    except:
                        print("That wasn't right! Looks like player 2 gets the cards.")
                        player2 = player2 + tableCards
                        length1 = len(player1)
                        length2 = len(player2)
                        try:
                            incorrectChoice = input("Nope! %s\n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (sAI,length1,length2))#choice after incorrect!
                            print("Here are four new cards.")
                            return (player1,player2)
                        except:
                            print("Here are four new cards.")
                            return (player1,player2)
                elif choice == "2":
                    try:
                        i = input("Solve for 24!\n\nThe card values are %d, %d, %d, %d.\n\nWhat is it?!\n\n**IMPORTANT**\nRemember to format your answer correctly!\n(Hint: Use spaces between digits and write in the order you perform the operations)\n(Hinthint: Check the rules page for clarification)" % (tableCards[0],tableCards[1],tableCards[2],tableCards[3]))
                        s = operationInput(i)
                        if s == 24:
                            player2 = player2 + tableCards
                            length1 = len(player1)
                            length2 = len(player2)
                            try:
                                correctChoice = input("Congratulations! You really got it! \n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (length1,length2))#choice after they get it correct!
                                print("Here are four new cards.")
                                return (player1,player2)
                            except:
                                print("Here are four new cards.")
                                return (player1,player2)
                        else:
                            player1 = player1 + tableCards
                            length1 = len(player1)
                            length2 = len(player2)
                            try:
                                incorrectChoice = input("Nope! %s\n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (sAI,length1,length2))#choice after incorrect!
                                print("Here are four new cards.")
                                return (player1,player2)
                            except:
                                print("Here are four new cards.")
                                return (player1,player2)
                    except:
                        print("That wasn't right... Looks like player 1 gets the cards.")
                        player1 = player1 + tableCards
                        length1 = len(player1)
                        length2 = len(player2)
                        try:
                            incorrectChoice = input("Nope! %s\n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (sAI,length1,length2))#choice after incorrect!
                            print("Here are four new cards.")
                            return (player1,player2)
                        except:
                            print("Here are four new cards.")
                            return (player1,player2)
                elif choice == "3":
                    if sAI != None:
                        player1 = player1 + [tableCards[0]] + [tableCards[1]]
                        player2 = player2 + [tableCards[2]] + [tableCards[3]]
                        length1 = len(player1)
                        length2 = len(player2)
                        try:
                            incorrectChoice = input("%s\n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (sAI,length1,length2))#choice after incorrect!
                            print("Here are four new cards.")
                            return (player1,player2)
                        except:
                            print("Cancel? That does the same thing as Okay!")
                            return (player1,player2)
                    else:
                        player1 = player1 + [tableCards[0]] + [tableCards[1]]
                        player2 = player2 + [tableCards[2]] + [tableCards[3]]
                        length1 = len(player1)
                        length2 = len(player2)
                        try:
                            noSolution = input("There is no solution! \n\nPlayer 1 has %d cards. \nPlayer 2 has %d cards." % (length1,length2))#choice after incorrect!
                            print("Here are four new cards.")
                            return (player1,player2)
                        except:
                            print("Cancel? That does the same thing as Okay!")
                            return (player1,player2)

    



def twentyFour():

    player1,player2 = shuffledSplit()
    while player1 != "0":
        player1,player2 = theTable(player1,player2)



#~~~~~~PART 4: ~~~~~~~
#CREATING THE MENUS

#gets the choice for the mainMenu

def mainMenuChoice():
    options = ["0", "1", "2", None]
    try:
        while True:
            choice = input("1. Play 24! \n2. Rules \n0. Exit\n What would you like to do?")

            if choice in options:
                return choice
            else:
                print("Whoops! As in whoops on you! That's not an option!")
    except:
        pass

#menu with all the rules and instructions

def rulesMenu():
    try:
        x = input("""
        **Instructions!**

        This is a two player card game called 24, simulated on Python.

        Your goal is to get all the cards. Each player starts out with half of the deck (shuffled randomly).
        Each turn each player contributes two cards to the "table", resulting in 4 cards on the table at a time.
        From these card values your goal is to compute the value 24. Once you find a solution, press the number
        for your player and enter the solution. If you correctly compute it before the other
        person then you add the four cards to your deck. Repeat until someone runs out of cards.

        This game does not use jokers!

        **Rules!**
    
        ~You may only use each card value once.

        ~You must use every card.

        ~You can only use operations * (multiplication), / (division), + (addition), - (subtraction)

        ~Input your answer in the order you want to execute each operation. (IGNORE PEMDAS, however,
        parenthesis still apply when used.)

        ~You can use parenthesis ONLY for one operation between two numbers, but it will change
        the order of execution. (See examples)
    
        ~When inputting your answer you MUST put spaces between each character. EVERY SINGLE ONE!

        IMPORTANT: If you do not format your answer correctly, it will be considered incorrect. Don't rush the typing :)

        **CAN DO**:
        6 + 3 * 2 + 6          :: 6 + 3 is 9, times 2 is 18, + 6 is 24
        9 - ( 6 / 6 ) * 3      :: 6 / 6 is 1, 9 minus 1 is 8, * 3 is 24
        ( 10 + 2 ) * ( 3 - 1 ) :: 10 + 2 is 12, 3 - 1 is 2, 12 * 2 is 24

        **CANNOT DO**:
        6+3*2+6                 :: Need spaces between characters
        9 - (6 / 6) * 3         :: Need spaces after and before parenthesis!
        ( 5 + 9 + 6 ) + 4       :: Too many numbers inside parenthesis!
        ( ( 12 / 3 ) - 1 ) * 8  :: Nested parenthesis not allowed

        """)
    except:
        print("Cancel? Okay!")




#USE THIS TO START PLAYING!!

def play():
    try:
        result = mainMenuChoice()
        if result == None:
            print("Have a nice day!")
            return
        while result != "0":
            if result == "1":
                twentyFour()
                result = mainMenuChoice()
            elif result == "2":
                rulesMenu()
                result = mainMenuChoice()
            else:
                return
    except:
        return


