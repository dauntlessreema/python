full_name = input("Please enter your full name: ")

if len(full_name) == 0:
      print ("You haven't entered anything. Please enter your full name.")
elif len(full_name) <= 3:
      print ("You have entered less than 4 characters. Please make sure you have entered your name and surname.")
elif len(full_name) > 25:
      print ("You have entered more than 25 characters. PLease make sure you have only entered your full name.")
else:
      print ("Thank you for entering your full name!")
