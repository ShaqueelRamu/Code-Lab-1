#Semester 1 Assessment 2: Vending Machine

#Below I set up a Dictionary for the avaialble items in the Vending Machine.
items = {
    "A1": {"name": "Coca Cola", "price": 3.50, "stock": 5, "category": "Cold Drinks"},
    "A2": {"name": "Mineral Water", "price": 2.00, "stock": 5, "category": "Cold Drinks"},
    "A3": {"name": "Orange Juice", "price": 4.00, "stock": 5, "category": "Cold Drinks"},
    "B1": {"name": "Arabic Coffee", "price": 5.00, "stock": 5, "category": "Hot Drinks"},
    "B2": {"name": "Karak Tea", "price": 3.00, "stock": 5, "category": "Hot Drinks"},
    "B3": {"name": "Hot Chocolate", "price": 5.50, "stock": 5, "category": "Hot Drinks"},
    "C1": {"name": "Lays Crisps", "price": 3.00, "stock": 5, "category": "Snacks"},
    "C2": {"name": "Chocolate Bar", "price": 2.50, "stock": 5, "category": "Snacks"},
    "C3": {"name": "Digestive Biscuits", "price": 3.50, "stock": 5, "category": "Snacks"}
}

 #The "suggestion map" below provides the client with suggestions on what to get next
suggestion_map = {
    "Cold Drinks": ["C1", "C2"],
    "Hot Drinks": ["C2", "C3"],
    "Snacks": ["A2", "B2"]
}
 
balance = 0.0
cart = [] #This command allows the Vending Machine to keep track of everything the user bought
 
 
def display_menu():
    print("\n----------------------------")
    print("      VENDING MACHINE")
    print("------------------------------")
 
 #Here I set for the vending machine to group items by their category first
    categories = {}
    for code in items:
        cat = items[code]["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(code)
 
    #This prints each category and the items in the Machine
    for cat in categories:
        print("\n-- " + cat + " --")
        print(f"  {'Code':<6} {'Name':<22} {'Price':<10} Stock")
        for code in categories[cat]:
            item = items[code]
            if item["stock"] > 0:
                stock = item["stock"]
            else:
                stock = "OUT OF STOCK"
            print(f"  {code:<6} {item['name']:<22} AED {item['price']:<6.2f} {stock}")
 
   
 
 
def insert_money():
    global balance
 
    print("\nAccepted coins/notes: 0.25, 0.50, 1, 5, 10, 20, 50, 100, 200 AED")
 
    while True:
        try:
            amount = float(input("Insert money (enter 0 when done): AED "))
            if amount == 0:
                break
            elif amount < 0:
                print("Please enter a positive amount.")
            else:
                balance = balance + amount
                print(f"Added AED {amount:.2f}  |  Balance: AED {balance:.2f}")
                answer = input("Add more money? (y/n): ").lower()
                if answer != "y":
                    break
        #The user is told to input a valid value         
        except ValueError:
            print("Please enter a valid number.")
 
 
def check_stock(code):
    if items[code]["stock"] > 0:
        return True
    else:
        print(f"Sorry, {items[code]['name']} is out of stock!")
        return False
 
 
def has_enough_money(code):
    global balance
    if balance >= items[code]["price"]:
        return True
    else:
        #Tells the client how much money they need to purchase their item
        short = items[code]["price"] - balance
        print(f"Not enough money. You need AED {short:.2f} more.")
        return False
 
 
def dispense_item(code):
    global balance
 
    item = items[code]
    items[code]["stock"] = items[code]["stock"] - 1 #Here the stock decreases according the amount of items purchased
    balance = balance - item["price"]
    cart.append(item["name"]) #Adds the clients item to a cart
 
    print("\n DISPENSING ITEM ")
    print(f"Item: {item['name']}")
    print(f"Price: AED {item['price']:.2f}")
    print(f"Remaining balance: AED {balance:.2f}")
    print("Please collect your item from the slot.")
 
 #Below the Vending Machine suggests the client with a snack that compliments what they bought
def suggest_item(category):
    if category in suggestion_map:
        print("\n  You might also like:")
        for code in suggestion_map[category]:
            #This makes the Machine only suggest items that are in stock
            if items[code]["stock"] > 0:
                print(f"    {code}: {items[code]['name']} - AED {items[code]['price']:.2f}")
 
 
def give_change():
    global balance
 
    if balance > 0:
        print(f"\nChange to return: AED {balance:.2f}")
        print("Change breakdown:")
        
        #The currency goes from biggest note to smallest coins
        denominations = [200, 100, 50, 20, 10, 5, 1, 0.50, 0.25]
        remaining = balance
 
        for d in denominations:
            count = int(remaining // d)
            if count > 0:
                if d >= 1:
                    print(f"  {count} x AED {int(d)}")
                else:
                    fils_val = int(d * 100)
                    print(f"  {count} x {fils_val} fils")
                remaining = round(remaining - (count * d), 2)
 
        print("Please collect your change.")
        balance = 0.0
    else:
        print("\nNo change to give.")
 
 
def main():
    global balance
 
   
    print("  WELCOME TO THE VENDING MACHINE")
    print("  Prices are in UAE Dirhams (AED)")
    
    #The Machine will ask the client to insert money before anything else
    insert_money()
 
    if balance <= 0:
        print("No money inserted. Goodbye!")
        return
 
    while True:
        display_menu()
        print(f"\nYour balance: AED {balance:.2f}")
 
        code = input("\nEnter item code (or type EXIT to finish): ").strip().upper()
 
        if code == "EXIT":
            break
        #The Machine will verify if the inputed code exists
        if code not in items:
            print("Invalid code. Please try again.")
            continue
 
        if not check_stock(code):
            continue
     
        #The Vending Machine allows the client to add more money whether they want more items or they dont have enough money
        if not has_enough_money(code):
            add = input("Would you like to add more money? (y/n): ").lower()
            if add == "y":
                insert_money()
                if not has_enough_money(code):
                    continue
            else:
                continue
 
        category = items[code]["category"]
        dispense_item(code)
 
        suggest_item(category)
 
        if balance <= 0:
            print("No balance left.")
            break
 
        again = input("\nWould you like to buy another item? (y/n): ").lower()
        if again != "y":
            break
 
    print("\nThank you for using the vending machine!")
    
    #The Machine will display a list of what the client bought
    if len(cart) > 0:
        print("\nItems purchased:")
        for item in cart:
            print("  - " + item)
 
    give_change()
    print("\nBye! Bye!\n")
 
 
main()
