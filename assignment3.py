 #!/usr/bin/python
age = input("What is your age?")
gender = input("What is your gender? male/female")

acc_balance = 0
if (int (age) > 25) and (int(age) < 30) and (gender == "male" or "Male" or "MALE"):
    newacc_balance = acc_balance+ 100000
    print("You have received Ksh. 100000 on the 24/05/2022. Your new account balance is Ksh. " + str(newacc_balance))
else:
    print("This offer is unavailable for this applicant. Your account balance is Ksh. " + str(acc_balance)) 
