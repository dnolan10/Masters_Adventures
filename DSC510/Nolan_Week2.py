#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Doug Nolan
#9/16/2025

print("Welcome to the Thunderdome")
#gather inputs from user. What company and length of fiber optic cable
company = input("What company do you work for?")
cable_feet_str= input("How many feet of fiber optic cable would you like?")
#convert input from user to float so errors go away
cable_feet_flt = float(cable_feet_str)
install_costs = cable_feet_flt * .95

#testing logic below
# print(install_costs)
# print("${:.2f}".format(install_costs))

#final receipt output below

print(f"""
Thank you for shopping at the Thuderdome :)
{company} has purchased {cable_feet_str} feet of fiber optic cable.
Your total today is {"${:.2f}".format(install_costs)}
Have a great day!
""")
