def calculate_age(year_of_birth, current_year=2025):
    return current_year - year_of_birth

name = input("Please enter your name: ")
year_of_birth = int(input("Please enter your year of birth (e.g., 2000): "))
age = calculate_age(year_of_birth)

print("Thank you")
print(f"{name}, your age is: {age}")
print("Current date: Wednesday, June 25, 2025, 7:23 PM SAST")
