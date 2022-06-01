#!/usr/bin/python
#######################################################################################
                #Name: Everlyne Njuguna
                #Date: 31/05/2022
                #QUADRATIC FORMULA
##################################################################################
import math
a = int(input("Enter the coefficcient of the first term here "))
b = int(input("Enter the coefficcient of the second term here "))
c = int(input("Enter the constant here "))


def find_roots(a,b,c):
    y1 = (-b + (math.sqrt (((b**2) - (4*a*c)))) )//(2*a)
    y2 = (-b - (math.sqrt (((b**2) - (4*a*c))))  )// (2*a)
    print("The roots of the quadratic equation are ", y1,y2)

find_roots(a,b,c)
    
def find_roots(a,b,c):
    w = (math.sqrt((b**2) - (4*a*c))) 
    z= (w) // (2*a)
    y_1 =( (-b) + (z) )
    y_2 = ((-b )- (z))
    print("The roots of the quadratic equation are ", w, z, y_1, y_2)

find_roots(a,b,c)
