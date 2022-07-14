 #!/usr/bin/python
 #################################
    #Name: Everlyne 
    #Date: 08/06/2022
    #PALINDROME GENERATOR
###################################

#ask the user for input
#the program should print based on the input inserted
#the number should be a palindrome


def check_palindrome(string):
    length = len(string)
    first = 0
    last = length - 1
    status = 1
    while (first < last):
        if (string[first] == string[last]):
            first = first + 1
            last = last - 1
        else: 
            status = 0
            break    #USED TO BREAK OUT OF A LOOP AND USUALLY COMES AFTER AN IF STATEMENT
        return int(status)
    
string =  input("Enter a word which you think is a palindrome: ")
# print("Method1")
status = check_palindrome(string)

if(status):
    print("It is a palindrome")
else:
    print("Not a palindrome")


#OR
#USE A REVERSE FUNCTION

def check_palindrome1(string1):
    reversed_string = string1[::-1]  #return a variable by slicing the parameter in a reverse way
    status = 1

    if (string1 != reversed_string):
        status = 0
    return status

string1 = input("Enter the word here: ")
status = check_palindrome1(string1)
if(status):
    print("It is a palindrome")
else:
    print("Not a palindrome")

