 #!/usr/bin/python
vehicles = ['bmw' , 'audi' , 'renault' , 'mercedes' , 'jeep']

#a single equal sign(=) is used in assigning variable
#== is an equality/comparison operator

#using for loops to print a list
for vehicle in vehicles:
    if vehicle == "jeep":
        print(vehicle.upper())

colors = ['blue', 'red' , ' yellow']
for color in colors:
    if color == "blue":
        print(color[:2])
