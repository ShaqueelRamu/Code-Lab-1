# I turned the user's name and hometown into strings
# Askes user for personal information
name = str(input("Enter your Full Name:"))
hometown = str(input("Enter yout hometown:"))

# Below I Created a loop to make sure the user enters a valid number for their age
while True:
    age = input("Enter yout age:")
    try:
        # Converts the input string to an integer
        age = int(age)
        #Leaves loop if integer is valid
        break
    #If user enters letters and not number
    except ValueError:
        #informs user to enter a valid number
        print("Invalid answer. Please enter a NUMBER.")

#Store user information and organize it in biography prompts,

Biography = {
    "name": name,
    "hometown": hometown,
    "age": age,
}
 
 #prints the values in separate lines
print(f"Name: {Biography['name']}\nHometown: {Biography['hometown']}\nAge: {Biography['age']}")