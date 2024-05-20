from person_class import Person


print("Welcome to creating Person instances!")

person =Person(1, "Marty", "McFly", "marty@email.com", "513-121-3434")
print("Person info:")
print(f"id: {person.id}")
print(f"name: {person.first_name} {person.last_name}")
print(f"email: {person.email}")
print(f"phone: {person.phone}")


print("Goodbye!")