month_days = {
   1 : 31, #January
   2 : 28, #February
   3 : 31, #March
   4 : 30, #April
   5 : 31, #May
   6 : 30, #June
   7 : 31, #July
   8 : 31, #August
   9 : 30, #September
   10 : 31, #October
   11 : 30, #November
   12 : 31, #December
}

try:
    #Asking what month it is
    month_number = int(input("Input a month number from 1-12:"))
    #Checking month validity
    if 1 <= month_number <= 12:
        #Checks Feb for leap year
        if month_number == 2:
            is_leap_year = input("Is it a leap year? (yes/no):").lower()

            #if the answer is "yes" then Feb has 29 days
            if is_leap_year == "yes":
               print(f"There are 29 days in month{month_number}(February) in this leap year")

            #Otherwise if answer is "no"
            elif is_leap_year == "no":
                print(f"There are{month_days[month_number]}days in the {month_number} month")

            else:
                print("Please enter a valid input for the leap year.'yes' or 'no'.")
        #Displays corresponding number with month
        else:
            print(f"There are {month_days[month_number]} days in month {month_number}")
    else:
        print("Please enter a valid month number from 1-12.")
except ValueError:
    print("Invalid response. Please enter a whole number")




