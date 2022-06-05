 #!/usr/bin/python
################################################
    #Name: Everlyne 
    #Date: 03/06/2022
    #CLASSES
###############################################
#create class called vehicle
#has two instances max.speed and mileage
class Vehicle:
    def __init__(self, mileage, maximum_speed):
        self.mileage = mileage
        self.maximum_speed = maximum_speed
        
Alfa_Romeo= Vehicle(str(521) + "miles" , str(350) + "km/h")
Camaro= Vehicle(str(680) + "miles",  str(400) + "km/h")
print(Alfa_Romeo.maximum_speed)
print(Camaro.mileage)




