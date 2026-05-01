#Dictionary with the months and assigned dates
month_days = {
    1: 31,   # January
    2: 28,   # February (leap year = 29)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31,  # December
}

month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}


def main():
    while True:
        try:
            # looks to find out what month it is
            month_input = input("Enter a month number (1-12), or 'q' to quit: ").strip().lower()

            # Gives user opportunity to quit
            if month_input in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break

            month_number = int(month_input)

            # It Checks validity of the month
            if not 1 <= month_number <= 12:
                print("Please enter a valid month number from 1-12.")
                continue

            month_name = month_names[month_number]

            # Checks Feb for leap years
            if month_number == 2:
                is_leap = input("Is it a leap year? (yes/no): ").strip().lower()

                # If the answer is "yes" then Feb has 29 days = leap year
                if is_leap == "yes":
                    print(f"There are 29 days in {month_name} (February) in this leap year.")

                # Otherwise if answer is "no"
                elif is_leap == "no":
                    print(f"There are {month_days[month_number]} days in {month_name}.")

                else:
                    print("Please enter a valid input for the leap year: 'yes' or 'no'.")
            else:
                # Here it displays corresponding number with month
                print(f"There are {month_days[month_number]} days in {month_name} (month {month_number}).")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()