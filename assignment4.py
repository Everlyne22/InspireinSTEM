 #!/usr/bin/python
#Write a program to withdraw Ksh. 25000 
#If the account balance is betwen Ksh.100000 and Ksh. 200000
#If 30%of the account balance is between Ksh. 500,000 and Ksh. 1,000,000
#If above Ksh. 1,000,000 deduct

acc_balance = input("Enter your account balance") 
if (int(acc_balance) > 100000 and int(acc_balance) < 200000):
     newacc_balance = int(acc_balance) - 25000
     print("We have deducted Ksh. 25000 from your account. Your new account balance is Ksh. " + str(newacc_balance))

elif(int(acc_balance) > 500000 and int(acc_balance) < 1000000):
     newwacc_balance = int(acc_balance) - (0.3 * int (acc_balance))
     print(f"We have deducted 30 percent from your account. Your new account balance is Ksh. " + str(newwacc_balance))

elif (int(acc_balance) > 1000000):
    newwwacc_balance = int(acc_balance) - 15000
    print("We have deducted Ksh. 15000. Your new account balance is Ksh. " + str(newwwacc_balance)  )

pass_mark = int(45)
your_marks = int(input("Enter your marks here: "))
if (your_marks >= pass_mark):
     print("Congratulations! You can eat ice cream today!")
     
else:
     print("You need to resit the test again!")
