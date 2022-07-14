 #!/usr/bin/python
#######################################################################################
                #Name: Everlyne
                #Date: 30/05/2022
                #CHALLENGE 1
####################################################
number = int(input("Enter the number here."))
if number%7==0 and number%5 == 0:
    print ("The number {} is divisible by both 7 and 5" .format(number))
else:
    print("The number {} is not divisible by both 7 and 5" .format(number))


#Write a program to write numbers in reverse
number = int(input("Enter the number here: "))
temp = number
reverse_number = 0
#using the while loop
while number > 0:
    digit = number % 10 #remainder
    reverse_number = reverse_number * 10 + digit
    number = number // 10

if (temp == reverse_number):
    print("The number is the same as the Reversed Number: " + str(reverse_number))
else:
    print("Not  the same as its reverse number" + str(reverse_number))






#write a program to customize the user input
print("Enter your name so as to customize your greetings. ")
name = input("Enter your name")
print("Hello {}".format(name))

#OR
prompt = "Enter your name so as to customize your greetings. "
prompt += ("\nWhat is your name?")
print("Hello", input(prompt)) 