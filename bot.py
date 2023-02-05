import random
from filereader import *


class EscapeBot:

    def __init__(self):
        self.name = "Rob"       #name can be changed with a setter method later, theres a default for users who dont want to utilise the setter
        self.position = 1       #starting position is hardcoded, bc you cant start the game midway through!
        self.goodbye = "Thank you for playing Escape Room Game!"        #this message can be changed with a setter method, the default is for if people dont want to change
        self.lives = 3      #amount of lives can be changed with a setter method later, theres a default for users who dont want to utilise the setter
        self.questions = ""     #empty string to add questions to in set_questions method
        print("instance of EscapeBot class created!")

    def __str__(self):
        info = ("Object name is %s, set lives are %s, goodbye message is %s" % (self.name, self.lives, self.goodbye))       #string representation returns the predetermined info about the function that isnt hardcoded, so the user can see what the game will be like
        return info


    def display_name(self):
        print("Hey there, my name is %s the robot!" % self.name)        #prints a simple string with the set name the user chooses

    def instructions(self):
        print("I am on a mission.\nI must retrieve the key to open this safe in front of me!\nBut only you can help me...\nYou must help me get the answers to these questions correct before I run out of lives.\nOnly then will I be able to retrieve the key to open the safe!\n ")      #this method simply returns the introduciton to the game, which can be changed to match different types of escape bots.
    
    def display_lives(self):
        print("You have %s lives remaining..." % self.lives)        #prints string with remaining lives value, which changes throughout object instantiation

    def increment_position(self):
        self.position = self.position + 1       #increments position of the instance
        question_amount = len(self.questions)     #calculates the amount of questions in the nested dictionary of the instance
        if self.position > question_amount:
            self.position = self.position - 1       #stops the game going past the amount of questions in the dictionary
            return True     #used in the instantiation to show all questions have been answered (you cant continue)
        else:
            return False        #there are questions remaining to be answered, and the game continues

    def display_correct(self, correct_message = "That answer was correct!"):
        print(correct_message)          #prints customisable string, with default value saying the answer is correc, to add flexibility

    def reveal_answer(self):
        print("\nThe correct answer is: %s" % self.correct_answer)       #prints the correct answer with a message, on a new line to make it more readable while playing
    
    def display_incorrect(self, incorrect_message = "That answer was incorrect!"):
        print(incorrect_message)        #prints customisable string, with default value saying the answer is incorrect, to add flexibility

    def set_questions(self, new_questions):     #method to change the set of questions to a new set
        if type(new_questions) != dict:     #passed in value must be a dict
            print("Questions must be of type dictionary (nested). Questions not reset.")
            return
        for key in new_questions:
            if str(key).isdigit() == False:     #if the key is not a digit string, return error
                print("Questions are not in the correct format. Questions not reset")
                return
            else:
                keys = new_questions[key]       #set the keys value to new keys of dictionary
                if type(keys) != dict:      #if keys arent dictionarys (for nested dict format) error
                    print("Questions must be of type dictionary (nested). Questions not reset.")
                    return
                if len(keys) != 3:      #if there isnt 3 keys for question, stimulus, answer, return error
                    print("Questions are not in the correct format. Questions not reset")
                    return #-1
                if "question" not in keys and "answers" not in keys and "stimulus" not in keys:     #if the labels arent right, error
                    print("Questions are not in the correct format. Questions not reset")
                    return
        print("questions set!")    #if format correct
        self.questions = new_questions      #set instance variable questions as the new questions

    def finished_game(self):
        print("Congratulations! \nAll questions have now been played! \nYou have won the game")     #string informing the user the game has been won. i left this hardcoded as it is generic enough to fit every type of game

    def ending(self):       #i changed the name of the method from "terminate" to "ending" as it was too similar to the "terminate_message" method, to avoid confusion
        print(self.goodbye)     #prints goodbye message, ending the instance
    
    def terminate_message(self):
        print("You have 0 lives remaining, and have lost the game")     #string informing the user the game has been lost. i left this hardcoded as it is generic enough to fit every type of game

    def display_position(self):
        print("You are now at position %s " % self.position)        #simple string to print position of the player during the game. this changes during the instantiation

    def current_question(self):
        set = self.questions           #gets the question nested dictionary from the class

        if self.position == 1:      #i added this code for grammar reasons, if its the first question the code saying "your next question is..." doesnt make sense
            first_next = "first"        #sets the word to first when in position 1
        else:
            first_next = "next"         #any other position the word is set to next

        ques = set[self.position]["question"]       #gets the question string from the nested dictionary
        stim = set[self.position]["stimulus"]       #gets the stimulus string from the nested dictionary
        ans = set[self.position]["answers"]         #gets the answer list from the nested dictionary

        ans_jumble = list(ans)      #creates a new list with the same values as the answer list
        random.shuffle(ans_jumble)      #the new list is jumbles, so the original list is still intact

        answer = ""     #i made a string to add the values of the jumbled list to, to make it more readable
        for i in ans_jumble:
            answer += i + "  "      #this adds each value to the new string, in a readable format


        print("The %s question is: \n\n%s \n%s \n\nPossible answers are: \n\n%s \n" % (first_next, ques, stim, answer))     #string with the question, stimulus, and potential answers so the user can see the different options for the instance

    def check_answer(self, response):
        response = str(response)       #takes user input as their response to the question. i wasnt sure why the parameter "response" was needed, as the game is played entirely in the terminal, so i used input() function to get the answer instead
        answer = response.strip()       #gets rid of empty spaces in the response
        correct = str(self.questions[self.position]["answers"][0])           #gets the correct answer from the nested dictionary, by finding what question is is with self.position, then getting the right answer which is always the first part of the nested dictionary. this is an instance variable as it is used in lots of the methods

        if answer.lower() == correct.lower():       #checks if answer (regardless of case) matches correct answer from the instance of the object
            return True     #returns true if correct
        else:
            return False        #or false if incorrect

    def draw(self, display = 0):        #parameter is used to decide which face the user wants to be shown during the game
        if display == 0:        #there are 5 options for different faces
            print("\n",
                "  ┌───────┐ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │ O   O │ \n",
                "  │   _   │ \n",
                "  └───────┘ \n"
            )
        elif display == 1:
            print("\n",
                "  ┌───────┐ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │ ^   ^ │ \n",
                "  │   o   │ \n",
                "  └───────┘ \n"
            )
        elif display == 2:
            print("\n",
                "  ┌───────┐ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │ \   / │ \n",
                "  │ o   o │ \n",
                "  │   ~   │ \n",
                "  └───────┘ \n"
            )
        elif display == 3:
            print("\n",
                "  ┌───────┐ \n",
                "  │ ───── │ \n",
                "  │  ───  │ \n",
                "  │       │ \n",
                "  │ ~   ~ │ \n",
                "  │   o   │ \n",
                "  └───────┘ \n"
            )
        elif display == 4:
            print("\n",
                "  ┌───────┐ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  ├─▄───▄─┤ \n",
                "  │   _   │ \n",
                "  └───────┘ \n"
            )
        else:
            print("\n",
                "  ┌───────┐ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │       │ \n",
                "  │ -   - │ \n",
                "  │   M   │ \n",
                "  └───────┘ \n"
            )

    def reset(self):
        self.position = 1       #resets the game back to question 1. it didnt say in the assignment brief to reset the lives as well, so im not sure of the purpose of this method

    def decrement_lives(self):
        self.lives -= 1     #decreases lives of the instanciation whenever the player gets a question wrong
        if self.lives <= 0:     #if there no lives remaining, method returns false, telling the code to end the instance as the player has lost
            return False
        else:
            return True     #otherwise the game continues, as there are lives remaining

    def gap(self,amount = 10):      #i created this as the gap between each question was too big for my computer screen, so i made it flexible and not hardcoded
        print("\n"*amount)

    def get_name(self):
        return self.name        #gets the name of the object instance

    def set_name(self, new_name):
        self.name = new_name        #sets the name of the object instance

    def get_goodbye(self):
        return self.goodbye     #gets the goodbye message of the current instance
    
    def set_goodbye(self, new_message):
        self.goodbye = new_message      #sets the goodbye message of the current instance

    def get_lives(self):
        return self.lives

    def set_lives(self, new_lives):
        self.lives = new_lives      #sets the amount of lives for this instance. this could be done at the start to make the game easier, or to add/remove extra lives during the game