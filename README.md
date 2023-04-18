# Chapter6Assignment
 6th Assignment for Python


Assignment is commented in the main file, copied here for convenience

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
