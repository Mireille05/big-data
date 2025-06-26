def calculate_age(year_of_birth):
    current_year = 2025
   return current_year - year_of_birth

 name = input("Enter your name: ")

 year_of_birth = int(input("Enter your year of birth (e.g., 2000): "))

 age = calculate_age(year_of_birth)

 print("Thank you")
 print(f"{name}, You are age is:{age} ")
