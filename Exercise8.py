#Name Search
#List of names
names = ["Jake","Zac","Ian","Ron","Sam","Dave"]

#Ask user input name to search
search_name = input("Enter Identifying Name:")

#Checks if the name is on the list
if search_name.lower() in [name.lower() for name in names]:
    print(f"{search_name} exists in list")
else:
    print(f"{search_name} does not exist in list")    