#/usr/bin/env/python
################################################
    #Name: Everlyne 
    #Date: 23/05/2022
    #DICTIONARIES
##############################
#Dictionaries is a collection of key value pairs.
#Have both the key and the value
#syntax: dictionary = {"key": "value"}

#Initialising Dictionaries
Student = {"Name": "Memphis" , "Age" : "21" , "Gender": "Female"}
colors = {'Color': 'Red'}
vehicle = {'Type': 'Alfa Romeo', 'Plate number': 'NE234W'}
#print(Student)
#print(colors)
#print(vehicle)

#Finding the data structure
#print(type(Student))
#print(type(colors))

#Accesing values in a dictionary
#print(Student["Name"])
#print(Student["Age"])
#print(Student["Gender"])
#print(vehicle["Plate number"])

#Adding values to a dictionary
Student["ID No."] = "28900563"
Student["Hobby"] = "Swimming"
Student["Favourite Food"] = "Chicken Nuggets"
#print(Student)

#Empty Dictionary
Student = {}
Student["Hometown"] = "Melbourne"
Student["Club"] = "Law Poll"
Student["Book"] = "Follow me down"
#print(Student)

#deleting values from a dictionary
del Student["Club"]
#print(Student)

#task - print dictionary person
person = {"Name": "Justus" ,
    "Phone number": "0712345678" ,
     "ID No." : "25675096" ,
     "Address": "7806 - 00200"}
#print(person)
#print(type(person))

person["Band"] = "Chase Atlantic"
del person["Phone number"]
#print(person)

#loop over dictionaries / arranging the data structure
for key, value in person.items():
    print(f"{key}:{value}")
for key, value in Student.items():   
    print(f"{key}:{value}")

colors = ["black" , "blue" , " red" , "indigo"]
i = 0
while i <= len(colors):
    if(colors[1] == 'blue'):
        print(colors[1].upper())
        i = i+1

#using the get method to access a key value in a dictionary
#method just means an in buit function and whatever is within the brackets is an argument
#it gives two responses
#print(person.get("Phone number", "the '\Phone number\' key is non-existent"))
#print(Student.get('Hometown'))

#dictionary containing the two lists
Kieranfav_food = ['Fries' , 'Rice' , 'Chicken'] 
Jekyllfav_food = ['Lasagna' , 'Beef' , 'Chapati']
Fav_foods = {"Kieran": Kieranfav_food , 
         "Jekyll" : Jekyllfav_food}
#print(Fav_foods)
#print(type(Fav_foods))

#for key,value in Fav_foods.items():
    #print(f"{key}: {value}")
    #print("{} : {}" . format(key, value))