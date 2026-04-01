#Define Correct password and max attempts
def password_entry_system():
    correct_password = "3502" 
    max_attempts = 5
    attempts_left: int = max_attempts

    while attempts_left > 0:
        #Asks the user to input pass
        entered_password = input("Enter The Passkey:")

        if entered_password == correct_password:
            print("Access Granted.:)")
            break
        else:
            #Calcates remaining attempts
            attempts_left -= 1
            if attempts_left > 0:
                #Feedback on remaining attempts
                print(f"Incorrect Password. You Have {attempts_left} attempt(s) left")
            else:
                #Displays when attempts reach max.
                print("Maximum attempts reached. Try Again In The Next 24H")
#Runs The Program
password_entry_system()
