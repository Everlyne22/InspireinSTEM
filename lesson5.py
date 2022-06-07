 #!/usr/bin/python
 ###########################################
       #Name: Everlyne
       #Date: 18/05/2022
       #STRING methods
####################################################
#string concatenation
name = "Everlyne Njuguna"
age = 17
person = "I am " + str(name) + " and my age is " + str(age)
print(person)

#format method
print("My name is {} and I am {} years old " .format(name,age) )

#newline \n 
print("January\February\nMarch\nApril\nMay\n")

#tab \t
print("Kisumu\tNairobi\tMombasa\tKiambu")

print ("My name is\t {}\t and I am {}\tyears old." .format(name,age))

msgs = '''QEN5H2OXVD confirmed
       you have received Ksh. 50,000 from
       LUKE HEMMINGS on 24/07/2022
       ''' 
print(msgs)

cafe = '''Hello, Welcome to Cafe Esperanza.
       I'm Ava and I'll be your waitress today.
       What would you like to start with?'''
print(cafe)

#removing spaces
user_name = "    Addah Lovelace   "
print(user_name.lstrip())
print(user_name.rstrip())

#changing case
txt = "Corbyn Besson"
#uppercase
print(txt.upper())
#lowercase
txt = "CORBYN BESSON"
print(txt.lower())

#slicing words
country = "Armenia"
print(country[5:])
print(country[:5]) #slices from back

#replacing letters
f_name = "Luke"
s_name = "Boss"
full_name = f_name + s_name
print(full_name.replace('B' ,'G'))


#split
msg = "Hello World" #separates words and puts them in a sort of list
print(msg.split())

#length of the words and the spaces
print(len(msg))
print(len(full_name))

#converting from one data tytpe to another
#float(decimals) to integers(numbers) and V.vars()
x = 5  #integer
print(float(x))
y = 46.87
print(int(y))

#boolean data type 
#there are only two types : TRUE AND FALSE
is_true = True
print(type(is_true))

