# DSC 510
# Week 6
# Programming Assignment 5.1
# Author Doug Nolan
# 10/19/2025

def main():

    #Create empty list to store temperatures
    temperatures = []

    print("\nWelcome to the Temperature List Analyzer!")
    print("Enter temperatures one by one. Type 'QUIT' to finish.")

    while True:
        user_input = input("Enter temperature: ").strip()
        #exit loop if user enters pre-determined quit criteria
        if user_input == 'QUIT':
            break
        try:
            temp = float(user_input)
            temperatures.append(temp)
        except ValueError:
            print("Invalid input. Please enter a numeric temperature or -1 to quit.")

    highest = max(temperatures)
    lowest = min(temperatures)
    count = len(temperatures)

    print("\n--- Temperature Summary ---")
    print(f"Total temperatures entered: {count}")
    print(f"Highest temperature: {highest:.2f}")
    print(f"Lowest temperature: {lowest:.2f}")


if __name__ == "__main__":
    main()
