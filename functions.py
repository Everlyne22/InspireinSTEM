 #!/usr/bin/python
 #######################################################################################
                #Name: Everlyne 
                #Date: 31/05/2022
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