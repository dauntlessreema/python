#the following is a program that calculates the award a person completing a triathlon based on their total time to complete all three events

#defined variables
swimming_time = int(input("Minutes taken to complete swimming event: "))
cycling_time = int(input("Minutes taken to complete cycling event: "))
running_time = int(input("Minutes taken to complete running event: "))
qualifying_time = 100

#calculation and display of total time
total_time = swimming_time + cycling_time + running_time
print("Total minutes taken to complete all events: " + str(total_time) + "!")

#award provided based on total time
if total_time <= qualifying_time:
    print("The award earned is Provincial Colours!")

elif total_time <= qualifying_time + 5:
    print("The award earned is Provincial Half Colours!")

elif total_time <= qualifying_time + 10:
    print("The award earned is a Procincial Scroll!")

else:
    print("No award has been earned.")