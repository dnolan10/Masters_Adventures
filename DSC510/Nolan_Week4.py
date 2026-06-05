# DSC 510
# Week 3
# Programming Assignment 3.1
# Author Doug Nolan
# 10/5/2025

def calc_costs(feet, price_per_foot):
    """
    feet (float): number of feet of fiber optic cable
    price_per_foot (float): Cost per foot based quantity
    :rtype: float: total cost of installation
    """
    return feet * price_per_foot

def main():
    """
    Main function to handle program logic, user interaction and costs calculation
    :return: receipt with inputs & costs
    """
    print("Welcome to the Thunderdome")
    company = input("What company do you work for?").strip()
    feet= input("How many feet of fiber optic cable would you like?").strip()
    try:
        cable_feet_flt = (float(feet))
    except ValueError as e:
        raise ValueError("Value input was not numeric. Please try again.")
    else:
        if cable_feet_flt > 500:
            price_per_foot = .55
        elif cable_feet_flt > 250:
            price_per_foot =  .75
        elif cable_feet_flt > 100:
            price_per_foot = .85
        else:
            price_per_foot =  .95

    # Calculate total costs using cost calculation function
    total_costs = calc_costs(cable_feet_flt, price_per_foot)
    # final receipt output below
    print(f"""
    Thank you for shopping at the Thuderdome :)
    {company} has purchased {cable_feet_flt:,.1f} feet of fiber optic cable.
    Your total today is {"${:.2f}".format(total_costs)}
    Have a great day!
    """)
if __name__ == "__main__":
    main()