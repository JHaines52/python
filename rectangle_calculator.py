print("Welcome to the Area and Perimeter Calculator")

choice = "y"
while choice != "n" and choice != "N":
   
    length = float(input("Enter length:"))
    width = float(input("Enter width:"))
    area = length * width
    print(f"Area: {area}")
    perimeter = (length + width) * 2
    print(f"Perimeter: {perimeter}")
    choice = input("Continue? (y/n): ")
    
print("\nGoodbye")
