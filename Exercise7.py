#Counting Loops
#starts at 0, stops before 51, step of 1
print("\nCounting up from 0 to 50 in increments of 1:")
for i in range(0,50): #range(start, stop, step)
    print(i)
    #starts at 50, stops before -1, steps of -1
    print("\nCounting down from 50 to 0 in decrements of 1:")
    for i in range(50, -1, -1):
        print(i)

    #starts at 30, stops before 51, steps of 1
    print("\nCounting up from 30 to 50 in increments 1:")
    for i in range(30, 51, 1):
        print(i)

    #starts at 50, stops before 9, steps -2
    print("\nCounting down from 50 to 10 in decrements of 2:")
    for i in range(50, 9, -2):
        print(i)

    #starts at 100, stops before 201, steps of 5
    print("\nCounting up from 100 to 200 in increments of 5:")
    for i in range(100,201,4):
        print(i)    