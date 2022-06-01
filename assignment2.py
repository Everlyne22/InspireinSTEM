 #!/usr/bin/python
#Print a diamond of stars
#range function no start value default is 0
h = int(input("Enter the height of the diamond."))

k = 0

for i in range(1, h+1):
    for space in range(1, (h-i)+1):
        print(end ="  ")

    while k!= (2*i-1):
        print("* ", end="")
        k += 1
    k=0
    print(  )

for i in range(h-2,-1,-1):
    for space in range():
        print()
#print a pyramid of stars
