from math import floor


print("Welcome to the Travel Time Calculator")

choice = "y"
while choice != "n" and choice != "N":
    miles = float(input("Enter miles: "))
    mph = float(input("Enter miles per hour: "))
    print("Estimated travel time")
    print("-----------------------------------------")
    time = miles / mph
    hours = floor(time)

    minutes = hours * 60
   
    print(f"Hours:{hours}")
    print(f"Minutes:{minutes}")
    choice = input("Continue? (y/n): ")
print("\nThe End")