 #!/usr/bin/python
  #!/usr/bin/python
################################################
    #Name: Everlyne 
    #Date: 02/06/2022
    #CLASSES
###############################################

class employee:
    def __init__(hisorher, name, salary):
        hisorher.name = name
        hisorher.salary = salary
    
    def my_employee(hisorher):
        print("The employee by the name " + (hisorher.name) +
         " will be receiving Ksh. " + str(hisorher.salary) + " every last Saturday of the month.")

employee1 = employee("Barbara Patterson", 35000)
employee1.my_employee()
employee2= employee("Thomas Merkin", 50000)
employee2.my_employee()
