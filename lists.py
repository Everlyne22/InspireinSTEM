 #!/usr/bin/python
##########################################################
        #Name: Everlyne 
        #Date: 19/05/2022
        #LISTS
#############################################################
#list
#initializing a list
cars = ['Jaguar', 'Ferrari', 'Ford', 'Alfa Romeo', 'Camero' , "Porsche" , "Honda"]
plate_number = ['MM499' , 'MW692' , 'DD364', 'FU444' , 'SA180']
owner = ['Marilyn' , 'Monroe' , 'Dominic' , 'Lylah']

#accessing an item from the list using indices
print(cars[0])

#negative list indices
print(plate_number[-1])   #picks the last element

#Finding the type of data structure
print(type(cars))

#changing/replacing an item in a list

cars[2] = "Tesla"
print(cars)

#adding an item to the list
cars.append ('Bugatti')
print(cars)

#adding lists together
total_items = cars + plate_number
print(total_items)

#deleting an item from a list
del cars[4]
print(cars)
cars.remove("Honda")
print(cars)

#using popped
#popped_cars = cars.popp()
# print(popped_cars)

#assigning number plates and their owners
print("My name is " + owner[2] + " and I own a " + cars[1] +  plate_number[3])
print(f"My name is {owner[0]} and I own a {cars[4]} {plate_number[2]}")
print("My name is {} and I was gifted a {} {} on my birthday. " .format(owner[3], cars[5], plate_number[0]) )

#determining the list length 
size = len(cars)
print(size)

#sorting lists in an order
list_1 = ['874', '463', '89464', '67336']
list_1.sort()
print(list_1)