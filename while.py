#the following programme calculates the average of numbers entered by user

#defined variables

total = 0
counter = 0

#a number is requested for the user to enter

number = int(input("Input any number (enter '-1' to be presented the average): "))

#while -1 is not entered another number will continue to be requested

while number != -1:
    total += number
    counter += 1
    number = int(input("Input any number (enter '-1' to be presented the average): "))

#following the user inputting -1 the average is calculated and printed 

average = (total) / (counter)
print(f"The average of all the numbers you entered is {average}!")

    
