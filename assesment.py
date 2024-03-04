# Question 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100. 
# For multiples of 3, print "Fizz"; for multiples of 5,
# print "Buzz"; and for numbers that are multiples of both 3 and 5,
# print "FizzBuzz".
numbers=range(1,101)#declare a variable that holds the range
for number in numbers: #use for loop y iterate through each of the numbers in the range individually
    if number%3==0 and number%5==0:#print FizzBuzz for every number divisible by both 3 and 5
        print("FizzBuzz")
    elif number%3==0:#print Fizz for every number divisible by 3
       print("Fizz")
    elif number % 5==0:#print Buzz for every number divisible by  5
        print("Buzz")
    
    else:
         print(number)

#Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.
         


#  Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8=> returns true
# 6=> returns false  
         
import math #use this to import math functions for easier manipulation of data using the mathematical functions
#create a function to check if the input from the user is a power of two
def power_two(n):#we pass n as an argument so that we can use it in the function
    if n <= 0:#checking if it is a negative number since a negative number cannot be a power of 2
        return False
    log_n = math.log(n, 2)
    return log_n == int(log_n)

# Taking input from the user
try:
    num = int(input("Enter an integer: "))
    if power_two(num):#passing the user input as a parameter in the function
        print("True")  # The number is a power of two
    else:
        print("False")  # The number is not a power of two
except ValueError:
    print("Please enter a valid integer.")         
               
         
# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

#create afunction to capitalize strings
def start_capital(capitalize_input):
    # Capitalize the first letter of each word using the title() 
    capitalized_string = capitalize_input.title()
    return capitalized_string#return the result

# prompt user for input which should be a string
#here we are using the boolean True to catch an error,,where the error is,,

while True:
    user_input = input("Enter a sentence: ")
    try:
       float(user_input)#if the input from the user is an integer we propmt for a valid sentence,,
       #only a integer can be coverted to afloat ,that is why we are using float() converter
       #so if it is true it is not a string 
       print("please write a valid sentence.")
        
    except ValueError:#except is executed if the try was false,,meaning the input fron user was a string
        
         capitalized_input = start_capital(user_input)
         print(capitalized_input)
         break


# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.
    
user_input = input("Enter a number and get the reversed version: ")
#we want to catch the error of a valid number and also specify ho to deal with negative numbers
try:
    # Convert the input to an integer to validate it's a numeric entry
    user_number = int(user_input)
    
    # Check if the number is negative, and if it is , work with its absolute value using the abs()function which changes negative numbers to positive
    if user_number < 0:#less that zero is anegative number
        absolute_num = abs(user_number)#convert negative number to positive
        string_num = str(absolute_num)#convert to string to work with it
        # Reverse the string representation and prepend the negative sign
        #using the slice where the -1 says that the slice should move from the last index reversing it
        reversed_string = '-' + string_num[::-1]
    else:#if the input is a positive,it will directly to this block of code
        string_num = str(user_number)
        # Reverse the string representation
        reversed_string = string_num[::-1]
    
    # Convert the reversed string back to an integer
    reversed_number = int(reversed_string)
    print(f"The reversed number is: {reversed_number}")
except ValueError:
    print("Please enter a valid integer.")    



# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2    

user_input = input("Write a sentence: ") 
format_input=user_input.lower()# Convert to lowercase to count both upper and lower case vowels
vowels = ["a","e","i","o","u"]
# Use a set comprehension to find unique vowels in the input and count them
return_vowel = sum(1 for vowel in vowels if vowel in user_input)

print(return_vowel)

