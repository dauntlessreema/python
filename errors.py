# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # indentation error fixed
print("\n")

# variables declaring the user's age, extracting the number, and printing the result
age_Str = "24 years old"  # (=) used instead of comparison (==)
age = int(age_Str.split()[0])  # extract the number from the string
print("I'm", age, "years old.")  # commas used for print formatting

# variables- additional years, converting to a number, and calculating total years
years_from_now = 3  # No need to quote a numerical value
total_years = age + years_from_now

# to print the total number of years
print("The total number of years:", total_years)  # Use variable name "total_years"

# to calculate and print the total months
total_months = (total_years * 12) + 6 # Use "total_years" for calculation and 6 added for the additional 6 months per statement
print("In 3 years and 6 months, I'll be", total_months, "months old")  # more commas added for formatting
#HINT, 330 months is the correct answer