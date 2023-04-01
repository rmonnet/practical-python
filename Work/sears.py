# On day one you deposit one bill on the ground in front of Sears tower.
# Every day you go out and double the number of bills.
# How many days will it take for the height of the bill stack to exceed the height of the tower?

bill_thickness = 0.11 * 0.001  # meters
sears_height = 442  # height in meters
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
