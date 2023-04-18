'''
Created on Oct 26, 2022

@author: Brandon Demeritt
'''

'''
(1) Prompt the user to enter a string of their choosing. Store the text in a string. Output the string.

(2) Implement a print_menu() function, which has a string as a parameter, outputs a menu of user options for analyzing/editing the string, 
and returns the user's entered menu option and the sample text string (which can be edited inside the print_menu() function). 
Each option is represented by a single character.

If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement the Quit menu option before implementing other options. 
Call print_menu() in the main section of your code. Continue to call print_menu() until the user enters q to Quit. 

(3) Implement the get_num_of_non_WS_characters() function. get_num_of_non_WS_characters() has a string parameter and returns the number 
of characters in the string, excluding all whitespace. Call get_num_of_non_WS_characters() in the print_menu() function. 

(4) Implement the get_num_of_words() function. get_num_of_words() has a string parameter and returns the number of words in the string. 
Hint: Words end when a space is reached except for the last word in a sentence. Call get_num_of_words() in the print_menu() function.  

(5) Implement the fix_capilization() function. fix_capilization() has a string parameter and returns an updated string, where lowercase letters 
at the beginning of sentences are replaced with uppercase letters. fix_capilization() also returns the number of letters that have been capitalized. 
Call fix_capilization() in the print_menu() function, and then output the number of letters capitalized and the edited string. 
Hint 1: Look up and use Python functions .islower() and .upper() to complete this task. Hint 2: Create an empty string and use string 
concatenation to make edits to the string.

(6) Implement the replace_punctuation() function. replace_punctuation() has a string parameter and two keyword argument parameters exclamationCount 
and semicolonCount. replace_punctuation() updates the string by replacing each exclamation point (!) character with a period (.) and each 
semicolon (;) character with a comma (,). replace_punctuation() also counts the number of times each character is replaced and outputs those counts. 
Lastly, replace_punctuation() returns the updated string. Call replace_exclamation() in the print_menu() function, and then output the edited string. 

(7) Implement the shorten_space() function. shorten_space() has a string parameter and updates the string by replacing all sequences of 2 or 
more spaces with a single space. shorten_space() returns the string. Call shorten_space() in the print_menu() function, and then output the 
edited string. Hint: Look up and use Python function .isspace().

'''

OPTIONS = ("c", "w", "f", "r", "s", "q")

#Main function, gets initial string from user, calls menu.
def main():
    userString = input("Please enter a string of your choice: ")
    print("You entered: ", userString)
    while True:
        userString = print_menu(userString)
        
#Menu function.  Displays menu, calls getOption function, gets it's return and passes it to the runOption function.
def print_menu(userString):
    menu = {
        "c" : "Number of non-whitespace characters",
        "w" : "Number of words",
        "f" : "Fix capitalization",
        "r" : "Replace punctuation",
        "s" : "Shorten spaces",
        "q" : "Quit"
        }
    for x, y in menu.items():
        print (x + " --> " + y)
    option = getOption()
    userString = runOption(option, userString)
    return userString
        
#getOption function, asks user which option from the menu they want to use and returns it to menu function.        
def getOption():
    while True:
        option = input("\nPlease choose an option: ")
        if not option in OPTIONS:
            print("ERROR: that is not an option")
        else:
            return option
        
        
#runOption function.  Get the argument from menu function and figures out which function to run based on the argument.
def runOption(option, userString):
    if option == "c":
        nonWS = get_num_of_non_WS_characters(userString)
        print("The number of non white space characters is: ", nonWS)
        return userString
        
    elif option == "w":
        words = get_num_of_words(userString)
        print("The number of words is: ", words)
        return userString
        
    elif option == "f":
        fixString = fix_capitalization(userString)
        userString = fixString[1]
        print("The number of fixed letters is: ", fixString[0])
        print("Fixed text is: ", userString)
        return userString
        
    elif option == "r":
        puncString = replace_punctuation(userString)
        userString = puncString[0]
        print("The number of fixed exclamation marks is: ", puncString[1])
        print("The number of fixed semicolons is: ", puncString[2])
        print("The edited text is: ", userString)
        return userString
        
    elif option == "s":
        remSpace = shorten_space(userString)
        print("The text with any excess space removed is: ", remSpace)
        return userString
        
    elif option == "q":
        print("\nGoodbye!")
        exit()

#get non WS function.  Gets the amount of non-whitespace characters in the string and returns it to the runOption to print.
def get_num_of_non_WS_characters(userString):
    nonWS = 0
    for i in userString:
        if not i.isspace():
            nonWS += 1
    return nonWS
    
#get number of words function.  Counts the number of words and returns it to runOption to print.    
def get_num_of_words(userString):
    return(len(userString.strip().split()))
    
#Fix capitalization function.  Looks for words after a period and space and then capitalizes them.    
def fix_capitalization(userString):
    wordString = list(userString.split(". "))
    capFixedSentence = ""
    count = 0
    for i in range(len(wordString)):
        wordString[i] = wordString[i].strip()
        wordString[i] = wordString[i].strip(".")
        if wordString[i][:1].islower():
            wordString[i] = wordString[i][:1].upper() + wordString[i][1:]
            count += 1
        capFixedSentence += wordString[i] + ". "
    return [count, capFixedSentence]

#Replace punctuation function.  Replaces ! with . and ; with ,
def replace_punctuation(userString):
    punctString = list(userString)
    exclamationCount = 0
    semicolonCount = 0
    fixPunctString = ""
    for i in range(len(punctString)):
        if punctString[i] == "!":
            exclamationCount += 1
            punctString[i] = "."
        elif punctString[i] == ";":
            semicolonCount += 1
            punctString[i] = ","
        fixPunctString += punctString[i]
    return [fixPunctString, exclamationCount, semicolonCount]
            
#shorten spaces function.  Removes excess white space between words.
def shorten_space(userString):
    remSpace = " ".join(userString.strip().split())
    return remSpace
    
main()


