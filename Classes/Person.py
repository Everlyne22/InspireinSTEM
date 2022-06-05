 #!/usr/bin/python
################################################
    #Name: Everlyne 
    #Date: 2/06/2022
    #CLASSES
###############################################
class person:
    def __init__(self, _name,_age):
        self.name =_name
        self.age = _age

    def sayHi(self):
        print("Hello, my name is " + str(self.name) + " and I am  "+ str(self.age) + " years old")

person1= person("Jeremy", 56)
person1.sayHi()
person2 = person("Ashton", 27)
person2.sayHi()


class dog:
    def __init__(my, _name, _age, _furcolor, _gender, _breed):
        my.name = _name
        my.age = _age
        my.furcolor = _furcolor
        my.gender = _gender
        my.breed = _breed
    def adoptMe(my):
        print("My name  is " + (my.name) + 
        " and  I am " + str(my.age) + " years old. I am " +  
        (my.furcolor)   +   (my.gender)   +    (my.breed) + ".")

dog1 = dog("Beatrice", 7, "black", "female", "Husky")
dog1.adoptMe()