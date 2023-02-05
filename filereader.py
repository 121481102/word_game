class FileReader:       #creates basic filereader class

    def __init__(self, filename):       #creates parent object properties
        self.__filename = filename      #sets private variable for file name, this cannot be opened outside FileReader class. other classes calling this must use the getter method
        print("instance of FileReader class created!")      #notifies that the subclass was created successfully
    
    def read_all(self):     #opens file, reads lines into a list, closes file
        try:
            file_1 = open(self.__filename)      #opens txt file specified for object
            lines = file_1.readlines()      #puts lines from opened file into a list (lines)
            file_1.close()      #closes file to save space for more code
            return lines
        except:
            print("file not opened. Terminating method")        #terminates the method when an error occurs
            return False
            
    def line_count(self):       #returns amount of lines in the list created by reading the file
        lines = self.read_all()     #gets results from read_all function
        line_amount = len(lines)        #amount of items in the list is equivalant to amount of lines in the file
        return line_amount   

    def get_filename(self):     #getter for the filename of the object
        return self.__filename      #returns the private variable to be accessed outside the class

    def set_filename(self, new_filename):       #setter for the filename of the object
        self.__filename = new_filename      #sets the private variable, this must be called seperately if accessed outside the class

class QuestionFileReader(FileReader):       #child/subclass of the parent class FileReader, for more specific question files instead of regular files
    
    def __init__(self, filename):       #for class properties
        super().__init__(filename) #copies the properties from the parent file FileReader, for the filename
        self.lines = super().read_all()     #uses the parent method read_all to get the list of lines present in the txt file
        self.length = super().line_count()      #uses the parent method line_count to get the amount of items/ lines taken from the txt file
        print("instance of Questionfilereader subclass created!")       #notifies that the subclass was created successfully

    def __str__(self) -> str:       #string representation of child class
        return "Filename: %s \nClass converts content of txt file into specific nested dictionary format" % super().get_filename()     #returns information about the subclass, the function and the name of the txt file

    def new_question_dict(self,new_filename):       #method to set instance variables to match a new dictionary passed in
        super().set_filename(new_filename)      #uses parent method set_filename to change to the new file
        self.lines = super().read_all()     #uses parent method to turn lines of the new file into a list format and set this as the lines (instance value) to be used in child class
        self.length = super().line_count()      #uses parent method to get amount of lines of the new list created set this as the line length (instance value) to be used in child class

    def all_dictionary_questions(self):     #converts the list of questions into specific nested dictionary format
        lines = self.lines      #gets the list of lines from __init__
        length = self.length       #gets the length of list from __init__
        i = 1       #starts counter
        all_lines_dict = {}     #empty dictionary to add nested dictionary onto
        split_lines = []        #empty list to sort the lines

        while i < length:
            internal_dict = {}      #empty dict to become nested dictionary, inside the while loop so it resets for every line of the file list
            current_set = lines[i]      #gets current line being formatted by the while loop
            split_lines = current_set[:-1].split(",")       #removes /n from the end of line i, and splits it by the "," into a list
            internal_dict["question"] = split_lines[0]      #first value in list is the question, assigned to "question" key of the nested dictionary
            internal_dict["stimulus"] = split_lines[1]      #second value in list is the stimulus, assigned to "stimulus" key of the nested dictionary
            internal_dict["answers"] = split_lines[2:]      #remaining values in list are the answers, assigned to "answers" key of the nested dictionary
            all_lines_dict[i] = internal_dict       #the completed nested dictionary is assigned to key "i" of the full dictionary, before the nested dict is reset
            i += 1      #i is increased to continue to the next line of the file

        return all_lines_dict       #final dictionary including nested dictionary is returned in proper format

    def lines_as_dictionary(self, line_nums_list):      #return the questions, stimuli and answers at the line numbers specified in the list passed in
        i = 0       #sets counter
        all_dicts = self.all_dictionary_questions()     #gets formatted nested dictionary of all questions
        requested_dicts = {}        #empty dictionary to add requested line number questions

        while i < len(line_nums_list):      #while the line number is less than the length of the list passed in:
            dict_number = line_nums_list[i]     #get the key number of the dictionary reuqested at i
            requested_dicts[i + 1] = all_dicts[dict_number]    #set the i key number in the new dictionary to the value of the reuqested questions   
            i += 1      #increase i and move on to next requested question
            
        return requested_dicts

    def get_dictionary_range(self, ran):        #returns question, stimulus, and answers from between the range of 2 values in the list passed in

        length = self.length        #get length of the list of all questions
        terminate = "ran is not in correct format, terminating method"      #error message for incorrect formatting

        i = ran[0]      #set counter starting at first value in range specified
        requested = []      #empty list to add the requested line numbers to

        while i <= ran[1]:      #cycles through the range of values until the final value in the put in list
            requested.append(i)     #adds the value in the range to the list
            i += 1      #increases i to move on to next value

        if len(ran) != 2:       #if theres too many values in inserted list, error
            return terminate
        elif ran[0] > ran[1]:       #if first value is higher than second, error as it cant work backwards with the counter
            return terminate
        elif ran[0] < 0 or ran[1] < 0:      #if either value is less than or equal to 0, error as the formatted dictionary starts at +1
            return terminate
        elif ran[1] > length:        #if final value is higher than the possible lines in the file, error as it cant read that high
            return terminate
        else:
            return self.lines_as_dictionary(requested)      #uses the new list as parameter for the exisitng function lines_as_dictionary to get the requested lines out of it

    def random_dictionary_questions(self):      #creates a new dictionary with lines of the file in a random range

        import random

        length = self.length

        first = random.randint(1,length - 1)        #gets random integer between 1 and 1 less than the amount of lines available, as 0 is an unusable line, and the range cant be only 1 line on its own
        last = random.randint(first + 1,length)     #gets random integer that is greater than the first random integer, up until the final line number available

        full_list = self.lines      #gets the list of all lines in the txt file
        chosen_list = full_list[first:last]     #gets the randomised line number and all the ones in between in a new list
        chosen_list.insert(0, "")      #sets first value in the list as an empty string, as the all_dictionary_questions function doesnt read the first line

        self.lines = chosen_list        #overwrites the self.lines as the new list, temporarily to be used by the all_dictionary_questions
        self.length = len(chosen_list)      #overwrites the self.length as the length of the new list, temporarily to be used by the all_dictionary_questions

        random_dictionary = self.all_dictionary_questions()     #uses existing all_dictionary_questions method with the new values set to create properly formatted nested dictionary

        self.lines = super().read_all()     #reset the self.lines variable to original parent list
        self.length = super().line_count()      #reset the self.list variable to length of original parent list

        return random_dictionary        #returns newly created formatted nested dictionary

    def exclude_dictionary_questions(self, line_nums_list):         #method to return formatted nested dictionary with specified lines from input list excluded

        i = 1       #starts counter at 1 for line numbers to get
        inclusive_list = []     #new list to put the list numbers to get into

        while i < self.length:      #
            if i not in line_nums_list:     #if the current i is not included in the list of values to exclude:
                inclusive_list.append(i)        #add it to the list of lines to get
            i += 1      #increase i to move on to next line

        return self.lines_as_dictionary(inclusive_list)     #use existing lines_as_dictionary method to get the lines that arent in the input excluded list, and return them as the formatted nested dictionary

    def exclude_dictionary_range(self,questions_range):     #returns all question lines except the ones included in range of input list

        if type(questions_range) == list and type(questions_range[0]) == int and type(questions_range[1]) == int:       #checks that input parameter is list and the values in list are integers
            if questions_range[0] > 0 and questions_range[1] < self.length:     #check the range of values is less than the highest possible list number and higher than 0

                i = questions_range[0]      #set counter starting at first value in inout range
                exclusive_list = []     #creates list to add values to exclude

                while i <= questions_range[1]:      #while line number is less than max of range input:
                    exclusive_list.append(i)        #add i to the list of numbers to exclude
                    i += 1      #move on to next value possible
                
                return self.exclude_dictionary_questions(exclusive_list)        #use existing method exclude_dictionary_questions with the parameter of the list of values to exclude to get the lines outside of the range input

            else:
                return "line numbers in question_range not available in the file"       #error message for going above or below available number lines
        else:
            return "questions_range must be a list containing only integers"        #error message for incorrect formatting of input parameter
