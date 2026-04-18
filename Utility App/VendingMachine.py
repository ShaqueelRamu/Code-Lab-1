#The Dictionary for the machine items
items = {
    #Cold Drinks
    "A1": {"name": "Coca Cola", "price": 3.50, "stock": 5, "category": "Cold Beverage"},
    "A2": {"name": "Mineral Water", "price": 2.00, "stock": 5, "category": "Cold Beverage"},
    "A3": {"name": "Orange Juice", "price": 4.00, "stock": 5, "category": "Cold Beverage"},
    #Hot Drinks
    "B1": {"name": "Arabic Coffee", "price": 5.00, "stock": 5, "category": "Hot Beverage"},
    "B2": {"name": "Karak Tea", "price": 3.00, "stock": 5, "category": "Hot Beverage"},
    "B3": {"name": "Hot Chocolate", "price": 5.50,"stock": 5, "category": "Hot Beverage"},
    #Snacks
    "C1": {"name": "Lays Crisps", "price": 3.00, "stock": 5, "category": "Snack"},
    "C2": {"name": "Chocolate Bar", "price": 2.50, "stock": 5, "category": "Snack"},
    "C3": {"name": "Deemah Date Biscuit", "price": 3.50, "stock": 5, "category": "Snack"}
}

#Variables in order to track user order
balance = 0.0
cart = []


def display_menu():
   #Displays the vending machine menu grouped by category.
   #Shows item code, name, price, and stock availability.
   
    print("\n" + "=" * 50)
    print("VENDING MACHINE MENU")
    print("=" * 50)
    
    print(f"{'Code':<6} {'Item':<20} {'Price':<10} {'Stock'}")
    print("-" * 50)
    
    for code, item in items.items():
        stock_status = item["stock"] if item["stock"] > 0 else "OUT OF STOCK"
        print(f"{code:<6} {item['name']:<20} AED {item['price']:<7.2f} {stock_status}")
    
    print("=" * 50)

def display_balance():
    #Displays the user's current balance.
    print(f"\n  Current Balance: AED {balance:.2f}")