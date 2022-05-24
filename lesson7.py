 #!/usr/bin/python
 #################################
    #Name: Everlyne Njuguna#
###################################    
#Creating loops
school = ['Mercy' , 'Joy' , 'Peace' , 'Kindness']
student =['Nadia' , 'Raziel' , 'Selene' , 'Dominic' , 'Caitlin']
print(f"Hello I am {student[0]} and I study at school of {school[0]} ")
print(f"Hello I am {student[1]} and I study at school of {school[1]} ")
print(f"Hello I am {student[2]} and I study at school of {school[2]} ")
print(f"Hello I am {student[3]} and I study at school of {school[3]} ")

#or
for students in student:
    print(f'Hello I am {student}')
print("\t")
for school in school:
    print(f'I attend the school of {school}')

squares = []
for number in range(0,10):
    square = number **2
    squares.append (square)
print(squares)

cubes =[]
for number in range (0,10):
    cube = number **3
    cubes.append (cube)
print(cubes)

sum = 0
for number in range (0,10):
    sum = sum + number
print(sum)

sum = 0
for number in range (0,100):
    sum = sum + number
print(sum)



