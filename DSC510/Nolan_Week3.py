# DSC 510
# Week 3
# Programming Assignment 3.1
# Author Doug Nolan
# 9/22/2025
import logging
print("Welcome to the Thunderdome")
#gather inputs from user. What company and length of fiber optic cable
company = input("What company do you work for?")
cable_feet_str= input("How many feet of fiber optic cable would you like?")
#convert input from user to float so errors go away
try:
    cable_feet_flt = float(cable_feet_str)
except ValueError as e:
    raise ValueError("Value input was not numeric. Please try again.")
else:
#adding if statements for costs logic
    if cable_feet_flt > 500:
        install_costs = cable_feet_flt * .55
    elif cable_feet_flt > 250:
        install_costs = cable_feet_flt * .75
    elif cable_feet_flt > 100:
        install_costs = cable_feet_flt * .85
    else:
        install_costs = cable_feet_flt * .95

#final receipt output below

print(f"""
Thank you for shopping at the Thuderdome :)
{company} has purchased {cable_feet_flt:,.1f} feet of fiber optic cable.
Your total today is {"${:.2f}".format(install_costs)}
Have a great day!
""")