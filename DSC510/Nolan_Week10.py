# DSC 510
# Week 10
# Programming Assignment 10.1
# Author Doug Nolan
# 11/16/2025

import locale


class CashRegister:
    #Create CashRegister class to track the number of items and total price of all items added to the cart

    def __init__(self):
        #set total price and item count to zero
        self.total_price = 0.0
        self.item_count = 0

    def add_item(self, price):
        #add item to the cart and update the total price and count
        self.total_price += price
        self.item_count += 1

    def get_total(self):
        #return the total price of all items
        return  self.total_price

    def get_count(self):
        #return the total number of items in the cart
        return  self.item_count

def main():
    #main function - program entry point
    print("\nWelcome to the Cash Register Program!")
    print("\nYou can add items and prices to your cart. Type 'q' when finished\n")
    print("-" * 50)
    print(" " * 30)

    #set locale for currency formatting
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    #create an instance of CashRegister
    register = CashRegister()

    while True:
        user_input = input("Enter the item price or 'q' to quit: ").strip().lower()

        if user_input == 'q':
            break

        try:
            price = float(user_input)
            if price <0:
                print("Price cannot be negative. Try again.")
                continue

            register.add_item(price)
            print(f"Added item #{register.get_count()} at {locale.currency(price)}")

        except ValueError:
            print("Invalid input. Please enter a numeric value or 'q' to quit.")


    #disply results
    print("\nCheckout Summary")
    print("-------------------")
    print(f"Total number of items: {register.get_count()}")
    print(f"Total price: {locale.currency(register.get_total())}")
    print("\nThank you for shopping with us!")




if __name__ == "__main__":
    main()