#/usr/bin/env/python
################################################
    #Name: Everlyne Njuguna
    #Date: 24/05/2022
##############################

#Initialising Dictionaries
Student = {"Name": "Memphis" , "Age" : "21" , "Gender": "Female"}

#Accesing values in a dictionary
print(Student["Name"])
print(Student["Age"])
print(Student["Gender"])

#Adding values to a dictionary
Student["ID No."] = "28900563"
Student["Hobby"] = "Swimming"
Student["Favourite Food"] = "Chicken Nuggets"
print(Student)

#Empty Dictionary
Student = {}
Student["Hometown"] = "Melbourne"
Student["Club"] = "Law Poll"
print(Student)

#deleting values from a dictionary
del Student["Club"]
print(Student)