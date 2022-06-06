 #!/usr/bin/python
################################################
    #Name: Everlyne 
    #Date: 06/06/2022
    #OPERATIONS
###############################################
#opening a file
f = open("lesson1.txt")
#opening and reading a file
print(f.read())
#closing a file
f.close()

#returning lines in a code
f = open("lesson1.txt")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#read only parts of the file
f = open("lesson1.txt", "r") #r
print(f.read(31)) #returns the first 31 characters
f.close()

#creating a new file


#appending a file just adds more to the existing file
f = open("lesson1.txt", "a")
f.write("Current status: Captain Marshall and Captain Welsh ahave been reported dead.")
f.close()

#open and read file after appending
f = open("lesson1.txt")
print(f.read)

#overwriting content in the file using w
f = open("myfile.txt", "w")
f.write("Jake Winters, a research consultant for the democrats, hass been chosen to find the person responsible for Bowe's death\n")
print(f.read())

f = open("lesson1.txt")
with open("lesson1.txt", "w") as f:
    f.write("Curret Status: The Navy Emergency Seal Team are on their way to aid SBX-1\n")
    f.write("Captain Marshall and Welsh have been reported dead\n")
    f.write("The missile aimed at Los Angeles has been successfully intercepted\n")
print(f.read())
f.close()

f.seek()

f.tell()
