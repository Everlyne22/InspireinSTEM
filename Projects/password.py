 #!/usr/bin/python
 #################################
    #Name: Everlyne 
    #Date: 03/06/2022
    #PASSWORD GENERATOR
###################################    
import random
print("Hey! Welcome to Strong Password Generator!")
characters = "huinjfhw67927%$"
num_passwords = int(input("Enter number of passwords to be generated: "))
len_password = int(input("Enter length of password here: "))


print("Here are your passwords. ")
for password in range(num_passwords):
    passwords = " "
    for character in range(len_password):
        password += random.choice(character)       
           