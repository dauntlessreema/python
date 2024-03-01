filename = "DOB.txt"  # Replace with your actual file name

with open(filename, 'r') as file:
   for line in file:
       name_parts, birthdate_parts = line.strip().split(maxsplit=1)
       first_name, surname = name_parts.split()
       day, month, year = birthdate_parts.split()

       # Print formatted information
       print("Name-")
       print(f"First Name {first_name}")
       print(f"Surname {surname}")

       print("\nBirthdate-")
       print(f"{day}/{month}/{year}")

       print("-" * 20)  # Separator between entries