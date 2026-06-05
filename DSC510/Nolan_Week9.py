# DSC 510
# Week 9
# Programming Assignment 9.1
# Author Doug Nolan
# 11/9/2025

import requests

def get_random_fact():

    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("text", "No fact available today.")
    except requests.exceptions.RequestException as error:
        return f"Error fetching fact: {error}"


def main():

    # fact = get_random_fact()
    # allow user to use the API interactor or quit out
    while True:
        print("Welcome to Doug's API Interactor")
        print("Choose an option below:")
        print("1. Get a useless fact")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            try:
                #get input from user on how many facts they would like
                count = int(input("Select the number of facts you would like by entering a number between 1 and 20 : ").strip())
                if 0 < count <= 20:
                    print("\nHere are your facts:\n")
                    for i in range(1, count + 1):
                        fact = get_random_fact()
                        print(f"Fact {i}: {fact}\n")
                    return
                else:
                    print("Please enter a number between 1 and 20.")
            except ValueError:
                print("Invalid input. Please enter a valid number")
                return
            #pretty print the random fact with the loop number


        elif choice == '2':
            print("Thank you for using the API Interactor. Goodbye")
            break

        else:
            print("Invalid choice. Please select 1 or 2")



if __name__ == "__main__":
    main()
