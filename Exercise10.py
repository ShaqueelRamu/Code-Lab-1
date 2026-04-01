#Even Odd Check Exercise

#Function determines if number is odd or even
def check_even_odd(number):
    
    #Uses modulo operator to check divisibility by 2
    if number % 2 == 0:
        return "even" #Even number, if remainder is 0
    else:
        return "odd" #Odd number, if the remainder is not 0

def main():
    try:
        #Asks user to input nmbr
        user_number = int(input("Enter a Number:"))
        result_message = check_even_odd(user_number)
        print(f"The Number {user_number} Is {result_message}.")
    except ValueError:
        print("Invalid input. Please enter an integer")
#ensures that the program runs when executed
if __name__ =="__main__":
    main()