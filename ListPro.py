# Importing date and time module.
import datetime
# Importing random module.
import random
# Importing Operating system module.
import os

# Creating a Function to add items in list.
def add_item(shopping_list):
    item = input("Enter an item to add: ")
    # Adding item in list using append method.
    shopping_list.append(item)
    print("Item added sucessfully.")


# Creating a Function to view list items.
def view_list(shopping_list):
    print("-----shopping list by Fahad-----")
    # Looping threw an list.
    for item in shopping_list:
        print(item)
        print("--------------------")


# Creating a Function to remove items from the list.
def remove_item(shopping_list):
    # Calling view list Function.
    view_list(shopping_list)
    item = input("Enter the item to remove: ")
    # Finding if items exsist in list.
    if item in shopping_list:
        shopping_list.remove(item)
        # Looping Threw an list.
        for items in shopping_list:
            print(items)
    else:
        print("Item not found in list.")


# Creating a function to check of item exsist in list.
def check_item(shopping_list):
    item = input("Enter the item to check: ")
    # Finding if item exsist in the list.
    if item in shopping_list:
        print("Yes item is in list.")
    else:
        print("Item is not in list.")
        exit()


# Creating a Function to clear list.
def clear_list(shopping_list):
    # Taking permession before clearing list.
    confirm = input("Are you sure you want to clear list y/n: ")
    if confirm == "y":
        # Clearing list using "clear()" method.
        shopping_list.clear()
    else:
        exit()


# Creating a Function to Show and download recipt.
def recipt(shopping_list):
    # Saving list len in a variable.
    Quantity = len(shopping_list)
    name = input("What is your name: ")
    fname = input("What is father name: ")
    num = input("Enter your phone number: ")
    # Saving num variable length in a variable.
    len_num = len(num)
    # Comparing num variable length.
    # If length of a phone number is less than 11 an error occurred and program will exit.
    if len_num < 11:
        print("Invalid phone number! Please check your number and try again.")
        # exit() Command to stop and exit program.
        exit()
    # If length of a phone number is bigger than 11 an error occurred and program will exit.
    elif len_num > 11:
        print("Invalid phone number! Please check your number and try again.")
        exit()
    # If length of the phone number is equal to 11 then the program pass the test and continue its journey.
    elif len_num == 11:
        pass
    print("=============recipt================")
    print(name,"s/o",fname)
    # Creating a random 4 digit number using random library.
    customer_id = random.randint(1000, 9999)
    print("Customer id: ",customer_id)
    print("Contact number: ",num)
    print("Total items: ",Quantity)
    # Looping threw shopping list.
    for items in shopping_list:
        print(items)
        print("-------------------")
    # dt variable contain current date time which we get threw datetime module.
    dt = datetime.datetime.now()
    print(dt)
    print("==============================")
    # Getting choice of the user if he want to print the reciept.
    choice1 = input("Do you want to print reciept y/n: ")
    if choice1 == "y":
        # giving path to save the file using OS module.
        desktop_path = os.path.expanduser("~/Desktop")
        # Creating a file name for the file choosing name and document type.
        file_name = f"receipt_{customer_id}.docx"
        file_path = os.path.join(desktop_path, file_name)
        # Opening the file to write data by using F_string.
        with open(file_path, "w") as file:
            file.write("============= Receipt ================\n")
            file.write(f"{name} s/o {fname}\n")
            file.write(f"Customer ID: {customer_id}\n")
            file.write(f"Contact number: {num}\n")
            file.write(f"Total items: {Quantity}\n")
            file.write("-------------------\n")
            for item in shopping_list:
                file.write(f"{item}\n")
            file.write("-------------------\n")
            file.write(f"{dt}\n")
            file.write("==============================\n")

        print(f"Receipt created and saved as '{file_path}'")
    elif choice1 == "n":
        print("Thank you for using.")
        exit()
    else:
        print("unrecognized command.")
        exit()
def main():
    # Creating a Empty shopping list.
    shopping_list = []
    # While loop set to True.
    while True:
        # Header for the menu
        print("=====shopping list Manager by Fahad=====")
        print("1- add item")
        print("2- view list")
        print("3- remove item")
        print("4- check item")
        print("5- clear list")
        print("6- recipt")
        print("7- Quit")
        # Taking input to know the customer choice.
        choice = input("Enter your choice: ")
        # Comparing the input to our shown options and calling the function.
        if choice == "1":
            # Calling the Function.
            add_item(shopping_list)
        elif choice == "2":
            view_list(shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
        elif choice == "4":
            check_item(shopping_list)
        elif choice == "5":
            clear_list(shopping_list)
        elif choice == "6":
            recipt(shopping_list)
        elif choice == "7":
            break
        else:
            print("Unrecognized command")
            exit()


main()
