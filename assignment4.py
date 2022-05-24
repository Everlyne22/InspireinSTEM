 #!/usr/bin/python
#Write a program to withdraw Ksh. 25000 
#If the account balance is betwen Ksh.100000 and Ksh. 200000
#If 30%of the account balance is between Ksh. 500,000 and Ksh. 1,000,000
#If above Ksh. 1,000,000 deduct

acc_balance = input("Enter your account balance") 
if (int(acc_balance) > 100,000) and (int(acc_balance) < 200,000):
    elif (float(0.3 * acc_balance) > 500,000) and (float(0.3 * acc_balance) < 1,000,000):

elif (int(acc_balance) > 1,000,000):
    newacc_balance = acc_balance - 25,000
    print("We have deducted Ksh. 25,000.")