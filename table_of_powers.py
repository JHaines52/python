print("Welcome to the Squares and Cubes table")

choice = "y"
while choice != "n" and choice != "N":
    number = int(input("Enter an integer: "))

    my_array = list(range(number))

    print("Number\tSquare\tCube")

    for value in my_array:
        square = number * number
        cube= number * number * number 

        print(f"{value}\t{square}\t{cube}")
    choice = input("Continue? (y/n): ")
print("\nThe End")

    

    
