# PYTHON BASICS 

# 1. PRINT FUNCTION
# THE PRINT FUNCTION IS USED TO DISPLAY OUTPUT TO THE USER.
# IT CAN TAKE MULTIPLE ARGUMENTS AND SEPARATE THEM WITH A SPACE BY DEFAULT
# let's see all the basic uses of the print function one by one

# 1.1 PRINTING A STRING

print("Hello, World!")  # This will print the string "Hello, World!" to the console

# 1.2 PRINTING MULTIPLE ARGUMENTS
name = "Alice"
age = 30    
print("Name:", name, "Age:", age)  # This will print "Name: Alice Age: 30"

# 1.3 PRINTING WITH A CUSTOM SEPARATOR

print("Hello", "World", sep="-")  # This will print "Hello-World"

# 1.4 PRINTING WITHOUT A NEWLINE
print("Hello, ", end="")  # This will print "Hello, " without a newline
print("World!")  # This will print "World!" on the same line as "Hello, "

# this function doesn't have much use as you can just type it all in one print statement, but it's still good to know about it as it can be useful in certain situations.

# 1.5 PRINTING WITH A CUSTOM END CHARACTER
print("Hello, ", end="---")  # This will print "Hello, " followed by "---" instead of a newline
print("World!")  # This will print "World!" on the same line as "Hello, " followed by "---"

# 1.6 PRINTING WITH FORMATTING
# We can use f-strings for formatting output in Python
name = "Bob"
age = 25
print(f"My name is {name} and I am {age} years old.")  # This will print "My name is Bob and I am 25 years old."

# 1.7 PRINTING WITH THE FORMAT METHOD
name = "Charlie"
age = 35
print("My name is {} and I am {} years old.".format(name, age))  # This will print "My name is Charlie and I am 35 years old."

# 1.8 PRINTING WITH PERCENTAGE FORMATTING
name = "David"
age = 40
print("My name is %s and I am %d years old." % (name, age))  # This will print "My name is David and I am 40 years old."

# THAT'S ALL FOR THE PRINT FUNCTION! NOW LET'S MOVE ON TO THE INPUT FUNCTION
# note: there are still more print function features,
# but we'll cover those in later lessons when we learn about file handling and other advanced topics.
# NOW LET'S MOVE ON TO THE INPUT FUNCTION

# 2. INPUT FUNCTION
# THE INPUT FUNCTION IS USED TO TAKE INPUT FROM THE USER.
# IT RETURNS THE INPUT AS A STRING, SO WE OFTEN NEED TO CONVERT IT TO THE APPROPRIATE DATA TYPE
# in simpler terms, the input function allows us to ask the user for information and store it in a variable for later use.
# let's see how to use the input function with some examples
#(note: we will be discussing 8 basic, and most useful examples of each basic function, and then move on to the next one)
# 2.1 TAKING STRING INPUT

name = input("Enter your name: ")  # This will prompt the user to enter their name and store it in the variable 'name'
print(f"Hello, {name}!")  # This will greet the user with their name

# 2.2 TAKING INTEGER INPUT
age = int(input("Enter your age: "))  # This will prompt the user to enter their age and convert it to an integer
print(f"You are {age} years old.")  # This will print the user's age

# 2.3 TAKING FLOAT INPUT
height = float(input("Enter your height in meters: "))  # This will prompt the user to enter their height and convert it to a float
print(f"You are {height} meters tall.")  # This will print the user's height

# 2.4 TAKING MULTIPLE INPUTS
# We can take multiple inputs in a single line by using the split() method

first_name, last_name = input("Enter your first and last name: ").split()  # This will prompt the user to enter their first and last name and split it into two variables
print(f"Your first name is {first_name} and your last name is {last_name}.")  # This will print the user's first and last name

# 2.5 TAKING INPUT WITH A CUSTOM PROMPT
color = input("What is your favorite color? ")  # This will prompt the user to enter their favorite color
print(f"Your favorite color is {color}.")  # This will print the user's favorite color

# 2.6 TAKING INPUT AND STRIPPING WHITESPACE
username = input("Enter your username: ").strip()  # This will prompt the user to enter their username and remove any leading or trailing whitespace
print(f"Your username is '{username}'.")  # This will print the user's username without any extra whitespace

# 2.7 TAKING INPUT AND CONVERTING TO BOOLEAN
is_student = input("Are you a student? (yes/no): ").strip().lower()  # This will prompt the user to answer if they are a student and convert the input to lowercase
is_student = is_student == "yes"  # This will convert the input to a boolean value (True if the user entered "yes", False otherwise)
print(f"Is the user a student? {is_student}.")  # This will print whether the user is a student or not

# 2.8 TAKING INPUT AND HANDLING EXCEPTIONS
try:
    number = int(input("Enter a number: "))  # This will prompt the user to enter a number and attempt to convert it to an integer
    print(f"You entered the number {number}.")  # This will print the number entered by the user
except ValueError:
    print("That's not a valid number!")  # This will print an error message if the user enters something that cannot be converted to an integer

# THAT'S ALL FOR THE INPUT FUNCTION! NOW LET'S MOVE ON TO THE LEN FUNCTION
# 3. LEN FUNCTION
# THE LEN FUNCTION IS USED TO GET THE LENGTH OF A SEQUENCE, SUCH AS A STRING, LIST, TUPLE, OR DICTIONARY
# IT RETURNS THE NUMBER OF ITEMS IN THE SEQUENCE
# let's see how to use the len function with some examples

# 3.1 GETTING THE LENGTH OF A STRING
text = "Hello, World!"
length = len(text)  # This will get the length of the string "Hello, World!"
print(f"The length of the text is {length}.")  # This will print the length of the string

# 3.2 GETTING THE LENGTH OF A LIST
numbers = [1, 2, 3, 4, 5]
length = len(numbers)  # This will get the length of the list [1, 2, 3, 4, 5]
print(f"The length of the numbers list is {length}.")  # This will print the length of the list

# 3.3 GETTING THE LENGTH OF A TUPLE
coordinates = (10, 20)
length = len(coordinates)  # This will get the length of the tuple (10, 20)
print(f"The length of the coordinates tuple is {length}.")  # This will print the length of the tuple

# 3.4 GETTING THE LENGTH OF A DICTIONARY
person = {"name": "Alice", "age": 30, "city": "New York"}
length = len(person)  # This will get the length of the dictionary, which is the number of key-value pairs
print(f"The length of the person dictionary is {length}.")  # This will print the length of the dictionary

# 3.5 GETTING THE LENGTH OF A SET
unique_numbers = {1, 2, 3, 4, 5}
length = len(unique_numbers)  # This will get the length of the set {1, 2, 3, 4, 5}
print(f"The length of the unique_numbers set is {length}.")  # This will print the length of the set

# 3.6 GETTING THE LENGTH OF A STRING WITH WHITESPACE
text_with_spaces = "   Hello, World!   "
length = len(text_with_spaces)  # This will get the length of the string including whitespace
print(f"The length of the text with spaces is {length}.")  # This will print the length of the string including whitespace

# 3.7 GETTING THE LENGTH OF AN EMPTY SEQUENCE
empty_list = []
length = len(empty_list)  # This will get the length of the empty list, which is 0
print(f"The length of the empty list is {length}.")  # This will print the length of the empty list
empty_string = ""
length = len(empty_string)  # This will get the length of the empty string, which is 0
print(f"The length of the empty string is {length}.")  # This will print the length of the empty string

# 3.8 GETTING THE LENGTH OF A NESTED SEQUENCE
nested_list = [[1, 2], [3, 4], [5, 6]]
length = len(nested_list)  # This will get the length of the outer list, which is 3
print(f"The length of the nested list is {length}.")  # This will print the length of the outer list

# we discussed three basic functions in this lesson!
# IN THE NEXT LESSON, WE'LL DISCUSS THREE MORE BASIC FUNCTIONS IN PYTHON, AND THEN MOVE ON TO SOME MORE ADVANCED TOPICS!
# A QUIZ WILL BE PROVIDED AT THE END OF THE LESSON, SO MAKE SURE TO PAY ATTENTION TO ALL THE EXAMPLES AND EXPLANATIONS!

# QUIZ TIME!
# 1. What does the print function do in Python?
# a) It takes input from the user
# b) It displays output to the user
# c) It calculates the length of a sequence

# 2. How can you print multiple arguments in a single print statement?
# a) By separating them with a comma
# b) By separating them with a space
# c) By separating them with a hyphen

# 3. What does the input function return?
# a) An integer
# b) A float
# c) A string

# 4. How can you convert the input from a user to an integer?
# a) By using the int() function
# b) By using the float() function
# c) By using the str() function

# 5. What does the len function do in Python?
# a) It takes input from the user
# b) It displays output to the user
# c) It returns the number of items in a sequence

# ANSWERS:
# 1. b) It displays output to the user
# 2. a) By separating them with a comma
# 3. c) A string
# 4. a) By using the int() function
# 5. c) It returns the number of items in a sequence





