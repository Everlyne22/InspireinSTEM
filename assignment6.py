9 #!/usr/bin/python
 #geometricprogression
a = int(input("Enter the first term here."))
r = int(input("Enter the geometric ratio."))
n = int(input("Enter the number of terms."))

for i in range(1, n+1):
    n_term = a * r **(i-1)
    print(n_term)

if r> 1:
    S_n = a*((r**n)-1) / (r-1)
else:
    if r< 1:
        S_n = a*(1-r**n) / (1-r)
print(S_n)

