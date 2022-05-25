 #!/usr/bin/python
age = input("What is your age?")

acc_balance = 0
if (int (age) > 25) and (int(age) < 30):
    newacc_balance = acc_balance+ 100000
    print("You have received Ksh. 100000 on the 24/05/2022.")
else:
    print("This offer is unavailable for this applicant.") 
