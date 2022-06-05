 #!/usr/bin/python
#surface area of a cylinder

import math
height  = input ("enter the height")
radius = input("enter the radius of a circle")
diameter = input("enter the diameter of the circle")

area =int (radius) * math.pi* int (radius) + math.pi * int (diameter) * int(height)
print("area of a circle is" + str (area))

#volume of a cube
side = input("enter the length of the side ")
volume = int (side) * int (side) * int (side)
print("The volume of a cube is " + str (volume))