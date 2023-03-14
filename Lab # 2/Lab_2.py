# Example # 01
def example1():
    print("\nExample1")
    a = int(input("Enter Number for square root: "))

    if a > 0:
        print("Number is greater than 0, calculating square root")
        root = a ** (1 / 2)
        print(f"The square root of {a} is {root}")
    if a <= 0:
        print("cant calculate the sq root of a number less than or equals to 0")


# Example: 02
def example2():
    print("\nExample2")
    a = int(input("Enter Number: "))
    if a == 1 or a == 0:
        a = 1 if a == 0 else 0
    if a >= 2 or a < 0:
        print("you have not entered number between 1,0")
    print(a)


# Example: 03
def example3():
    print("\nExample3")
    a = int(input("Enter Number b/w 10-20 "))
    if 10 <= a <= 20:
        print("Condition has been met")
    else:
        print("Condition not met")


# Example: 04
def example4():
    print("\nExample4")
    a = int(input("enter number b/w 10-20 or 30-40"))
    if 10 <= a <= 20 or 30 <= a <= 40:
        print("Condition has been met")
    else:
        print("Condition not met")


# STRUCTURED LOOP
# Example #1
def exampleLoop1():
    # Incremental
    print("\nExample Loop 1 Incremental")
    i = 1
    while i <= 100:
        print("Karachi, Pakistan")
        i += 1
    # Decremental
    print("\nExample Loop 1 Decremental")
    i = 100
    while i >= 1:
        print("Karachi, Pakistan")
        i -= 1


# Example # 2
def exampleLoop2():
    print("\nExample Loop 2")
    pcount = 0
    ncount = 0
    count = int(input("how many numbers you want?"))
    i = 1
    while i <= count:
        num = int(input("Enter number"))
        if num >= 0:
            pcount += 1
        else:
            ncount += 1
        i += 1
    print("positive", pcount)
    print("negative", ncount)


def exampleLoop3():
    print("\nExample Loop 3")
    value = 'c'
    userValue = input("Guess a letter from a to e: ")
    while userValue != value:
        print("Incorrect")
        userValue = input("Guess a letter from a to e: ")
    print("Welcome User")


# LAB EXERCISES

def labEx1():
    print("\nLab Exercise 1.1")
    width = int(input("Enter width of the cube: "))
    height = int(input("Enter height of the cube: "))
    depth = int(input("Enter depth of the cube: "))
    volume = width * height * depth
    print(f"The Volume of cube is {volume}")

    print("\nLab Exercise 1.2")
    timeConsumed = int(input("Enter the time required for worker to complete a job: "))
    if 2 <= timeConsumed <= 3:
        print("Highly efficient")
    elif 3 <= timeConsumed <= 4:
        print("Improve speed")
    elif 4 <= timeConsumed <= 5:
        print("Give training to improve speed")
    elif timeConsumed > 5:
        print("You are fired")

    print("\nLab Exercise 1.3")
    password = "abc$123"
    enteredPassword = input("Enter password: ").lower()
    if password == enteredPassword:
        print("Welcome")
    else:
        print("I don't know you")


def labEx2():
    # 1
    print("\nLab Exercise 2.1")
    n = 3
    while n >= 0:
        n -= 1
        print(n)

    #2
    print("\nLab Exercise 2.2")
    n = 4
    while n > 0:
        n += 1
        print(n)
        if n == 100:  # to break the loop at 100
            break

    #3
    print("\nLab Exercise 2.3")
    clist = ['Canada', 'USA', 'Mexico', 'Australia']
    for country in clist:
        print(country)

    #4
    print("\nLab Exercise 2.4")
    for i in range(0,101):
        print(i)

    #5
    print("\nLab Exercise 2.5")
    n = int(input("Enter number for table: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

    #6
    print("\nLab Exercise 2.6")
    print("Backward 1 to 10")
    for i in range(10,0, -1):
        print(i)

    #7
    print("\nLab Exercise 2.7")
    print("Create a loop that counts all even numbers to 10")
    even = 0
    for i in range(1,11):
        if i % 2 == 0:
            even += 1
    print(f"Count of even Numbers: {even}")

    #8
    print("\nLab Exercise 2.8")
    print("Create a loop that sums the numbers from 100 to 200")
    sum = 0
    for i in range(100,201):
        sum += i
    print(sum)




example1()
example2()
example3()
example4()
exampleLoop1()
exampleLoop2()
labEx1()
labEx2()
