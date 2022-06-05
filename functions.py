 #!/usr/bin/python
 #######################################################################################
                #Name: Everlyne 
                #Date: 31/05/2022 // 03/06/2022
                #FUNCTIONS
 ########################################################################################
 
 #it is a block of  code that gets executed together
 #initialising/ defining a function
def say_hello():
    print("Hello Estrella.")
    
    x= 4
    y= 7
    z = x + y
    print(z)

#calling a function
say_hello()
    
#print a function of sounds made by a number of animals
def bark():
    print("A dog barks.")
bark()

def neigh():
    print("A horse neighs.")
neigh()

def moo():
    print("A cow moos.")
moo()


#function parameters
def add_numbers (x, y):
    sum_Of = x + y
    print("The sum is ", sum_Of)

add_numbers (4, 5)
add_numbers(45, 78)
add_numbers(21, 34)

#product two numbers
def prod (x,y):
    prod = x * y
    print("The product of two numbers is ", prod)

prod(56,97)
prod(39, 77)

#setting parameters on default
def print_name(name= "Madison"):
    print(name)
print_name("Bill")

#return from a function
def get_sum(num1, num2):
    sum_Of = num1 + num2
    return sum_Of
print(get_sum(24, 11))

#write a function that gets the square of numbers
def squares(number, power):
    squares_num = number ** power
    return squares_num
print(squares(6, 4))

#write a function that types your full name
def get_full_name(first_name, sec_name):
    full_name = first_name +  " " +  sec_name
    return full_name.title()
print(get_full_name("Nancy", "Mwai"))

#returning a dictionary from a function
def create_full_name(first_name, sec_name):
    person = {'first' : first_name, 'second' : sec_name}
    return person
student = create_full_name ('Regina',  'Hall')
print(student)


#parsing a list in a function
def greet_friends(names):
    for name in names:
        msg = "Hello " + name.title() + "! You are invited to a function tomorrow. Red is the theme." 
        print(msg)
friends = ['Sharon', 'Stacey', 'Neema', 'Anthony']
greet_friends(friends)