 #!/usr/bin/python
################################################
    #Name: Everlyne 
    #Date: 06/06/2022
    #MAIN
###############################################
#import module

import operations
from student import Student

from teachers import Teachers


print(operations.add_numbers(4,5))
print(operations.sub_numbers(56, 45))
print(operations.mult_numbers(70, 6))
print(operations.div_numbers(800,40))

new_student = Student("Kelsey" , "Cooking", str(1994))
new_student.greet_student()

new_teacher = Teachers("Mark",67539, "Theology", 60000)
print(new_teacher.get_TSC_number())

