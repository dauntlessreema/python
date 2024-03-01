import math
#programme of two different financial calculators

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#user confirmation of the type of deposit regardless of case chosen 

deposit_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#if user choice of deposit is investment

if deposit_type == "investment".lower():
    deposit = float(input("How much money are you depositing? "))
    interest_rate = float(input("what is the percentage rate as a figure only? "))
    interest_rate_float = float(interest_rate / 100)
    years = float(input("How many years do you want to invest for? "))
    interest_type = input("Will it be simple or compound interest? ").lower()
    
#if user choice is simple interest choice

    if interest_type == "simple":
        money_back_simple = deposit * (1 + (interest_rate_float * years))
        print(f"Money returned to you would be {money_back_simple}")
    
#if user choice is compound interest choice

    elif interest_type == "compound":
         money_back_compound = deposit * math.pow((1 + interest_rate_float), years)
         print(f"Money returned to you would be £{money_back_compound}")
    else:
        breakpoint

#if user choice of deposit is bond

elif deposit_type == "bond".lower():
     house_value = float(input("What is the present value of the house? "))
     bond_interest_rate = float(input("What is the interest rate as a figure only? "))
     bond_interest_monthly = float((bond_interest_rate /12) / 100)
     months_to_repay = float(input("How many months do you plan to take to repay the bond? "))
     repayment = (bond_interest_monthly * house_value) / (1 - (1 + bond_interest_monthly)**(- months_to_repay))
     print(f"Monthly repayment would be £{repayment}")

#if user choice is any other response

else:
    print("Wrong choice entered")