print("Welcome to instagram!")
print("\t")
first = str(input("Is this your first time using Instagram? "))
if first == "Yes" or "yes":
    print("You'll need to sign in.")
    print("\t")
    phone_number = str(input("Enter your phone number: "))
    if len(phone_number) < 10 or len(phone_number) >10:
        print("The number input is invalid. Please try again.")
        phone_number = str(input("Enter your phone number: "))    
    else:
        email = str(input("Enter your email account: "))
        print("\t")
        password = str(input("Enter your new password: "))
        if len(password) < 10:
            print("Your password is not strong. Please try again.")
            password = str(input("Enter your new password: "))
        else:
            user_name = input("Enter the username you will use: ")
            print("\t")
            print("The set-up is complete! Welcome to instagram", user_name)
else:
    print("You'll need to login.")