import mymodule  # For Example # 13 & 15


# EXAMPLE # 01
# A lambda function that adds 10 to the number passed in as an argument, and print the result:
def example1():
    print("Example 1: ")
    x = lambda a: a + 10
    print(x(5))


# EXAMPLE # 02
# A lambda function that multiplies argument a with argument b and print the result:
def example2():
    print("Example 2: ")
    x = lambda a, b: a * b
    print(x(5, 6))


# EXAMPLE # 03
# A lambda function that sums argument a, b, and c and print the result
def example3():
    print("Example 3: ")
    x = lambda a, b, c: a + b + c
    print(x(5, 6, 2))


# EXAMPLE # 04
# Create an array containing car names
def example4():
    print("Example 4: ")
    cars = ["Ford", "Volvo", "BMW"]
    print(cars)


# EXAMPLE # 05
# Get the value of the first array item
def example5():
    print("Example 5: ")
    cars = ["Ford", "Volvo", "BMW"]
    x = cars[0]
    print(x)


# EXAMPLE # 06
# Modify the value of the first array item
def example6():
    print("Example 6: ")
    cars = ["Ford", "Volvo", "BMW"]
    cars[0] = "Toyota"
    print(cars)


# EXAMPLE # 07
# Return the number of elements in the cars array
def example7():
    print("Example 7: ")
    cars = ["Ford", "Volvo", "BMW"]
    x = len(cars)
    print(x)


# EXAMPLE # 08
# Print each item in the cars array
def example8():
    print("Example 8: ")
    cars = ["Ford", "Volvo", "BMW"]
    for x in cars:
        print(x)


# EXAMPLE # 09
# Open the file "demofile2.txt" and append content to the file
def example9():
    print("Example 9: ")
    f = open("textfile.txt", "a")
    f.write("Now the file has more content!")
    f.close()

    f = open("textfile.txt", "r")
    print(f.read())


# EXAMPLE # 10
# Open the file "demofile3.txt" and overwrite the content
def example10():
    print("Example 10: ")
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()

    f = open("demofile3.txt", "r")
    print(f.read())


# EXAMPLE # 11
# Create a file called "myfile.txt"
def example11():
    print("Example 11: ")
    f = open("demofile3.txt", "x")


# EXAMPLE # 12
# Create a new file if it does not exist
def example12():
    print("Example 12: ")
    f = open("myfile.txt", "w")


# EXAMPLE # 13 mymodule.py file

# EXAMPLE # 14
# Import the module named mymodule, and call the greeting function
def example14():
    print("Example 14: ")
    mymodule.greeting("Jonathan")


# EXAMPLE # 15 in the file mymodule.py

# EXAMPLE # 16
# Import the module named mymodule, and access the person1 dictionary
def example16():
    print("Example 16: ")
    a = mymodule.person1["age"]
    print(a)


if __name__ == "__main__":
    example1()
    example2()
    example3()
    example4()
    example5()
    example6()
    example7()
    example8()
    example9()
    example10()
    example14()
    example16()
