from bot import *
from filereader import *

escape_bot_file = QuestionFileReader("python-game-file.txt")        #creates instance of questionfilereader subclass
file_name = escape_bot_file.get_filename()      #uses getter to get name pf the file for future use
questions = escape_bot_file.all_dictionary_questions()      #gets questions from the opened file in the nested dictionary format using method from filereader

escape_bot = EscapeBot()        #creates instance of the escapebot class
#for this instance i didnt change the name, lives, etc. its all default

escape_bot.set_questions(questions)     #sets questions for escapebot instance using the nested dictionary obtained from the filereader instance

print(escape_bot)       #prints string representation to see all the settings of escapebot instance

y_or_n = input("\nCurrent questions file is %s. Would you like to use another questions file? Press Y for yes. Any other key will continue with the current file " % file_name)      #asks user if they would like to change the dictionary of questions used in both filereader and escapebot instance

if y_or_n == "y":       #if user chooses to change question file
    try:
        new_file = input("\nWhat file would you like to use? ")       #ask for the name of the new txt file to get questions from
        new_dict = escape_bot_file.new_question_dict(new_file)      #uses new_question_dict from filereader class to set the class variables for this instance to fit new txt file
        new_questions = escape_bot_file.all_dictionary_questions()      #turns new dictionary of questions into the nested dictionary format
        escape_bot.set_questions(new_questions)     #sets the questions used by the escapebot instance ti the new nested dictionary of questions
    except:
        print ("File %s was not found. Current file %s will be used instead" % (new_file, file_name))       #error handling for when the file name typed in doesnt exist in the folder

escape_bot.draw()       #draws the robots face, here its the default
escape_bot.display_name()       #displays robots name message
escape_bot.instructions()       #displays set instructions, here its the default

in_a_row = 0        #sets counter for the amount of questions gotten right in a row to 0
in_play = False     #game hasnt started until user asks it to
user_in = input("Press Y to continue. Any other key quits the game")
if user_in.lower() == "y":      #when user says to start, game starts
    in_play = True

while in_play:
    answer_correct = True       #variable used later to say if answer is right for that instance

    escape_bot.gap()
    escape_bot.display_position()       #information is shown with robot face, then the question for this instance is asked
    
    row = 3     #sets amount of questions correct in a row required to gain lives to 3
    inc = 1     #sets the amount of lives gained to 1
    if in_a_row == row:     #if user get the required amount of questions correct in a row :
        lives = int(escape_bot.lives)       #get the amount of remaining lives as an int
        new_lives = lives + inc     #add the amount set to increase by to the amount of lives remaining
        escape_bot.set_lives(new_lives)     #use method from escapebot class to set the amount of lives remaining to this new number for this instance
        print("Congrats! You got %s questions right in a row! You gained %s life!" % (row, inc))        #tells the user they got the required amount of answers right in a row and gained the amount of lives
        in_a_row = 0        #resets the amount of questions gotten right in a row to 0

    escape_bot.display_lives()
    escape_bot.draw()
    escape_bot.current_question()

    response = input("What do you think the answer is? Type your full answer\n")

    if escape_bot.check_answer(response) == True:       #user can input answer to this question
        escape_bot.display_correct()        #if they are right they get a good message
        in_a_row += 1       #add 1 to the counter for correct questions in a row
        no_questions_left = escape_bot.increment_position()
        if no_questions_left == True:       #when every question is answered
            escape_bot.gap()
            escape_bot.draw()
            escape_bot.finished_game()      #the game ends
            in_play = False
    else:
        escape_bot.display_incorrect()      #if they are wrong...
        if escape_bot.decrement_lives() == False:       #they lose a life until there is none left
            escape_bot.gap()
            escape_bot.draw()
            escape_bot.terminate_message()      #if there is no lives left, the terminate message is shown and the game ends
            in_play = False
            break       #breaks the loop. for some reason in_play = False didnt end the loop for me, so i used this
        in_a_row = 0        #set counter for correct questions ina row to 0
        escape_bot.display_lives        #if there are lives left they are shown
        answer_correct = False

    
escape_bot.gap()
escape_bot.ending()     #the final ending of the game/ instance is shown