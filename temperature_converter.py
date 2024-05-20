print("Welcome to the Temperature Coverter")

choice = "y"
while choice != "n" and choice != "N":
    f = int(input("Enter degrees in Fahrenheit: "))
    c = (f-32) * 5/9
    print(f"Degrees in Celsius: {c:.2f}")
    choice = input("Continue? (y/n): ")
print("\nThe End")