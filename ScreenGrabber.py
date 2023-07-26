import pyscreenshot  # Importing the pyscreenshot module for taking screenshots
import time  # Importing the time module for delays

print("==============================")
print("Welcome To ScreenGrabber.")
print("Created by Muhammad Fahad.")

choice = input("Do you want to take a screenshot? (y/n): ").lower()  # Prompting the user for a choice to take a screenshot

if choice == "y":  # Checking if the choice is "y"
    print()  # Print an empty line to provide spacing
else:
    print("Closing the program.")
    exit()  # Exiting the program if the choice is not "y"

delay = 5  # Setting a delay of 5 seconds
time.sleep(delay)  # Delaying the program execution for the specified time

image = pyscreenshot.grab()  # Taking a screenshot using the grab() function from the pyscreenshot module
image.show()  # Displaying the screenshot image

# Saving the screenshot in the current directory with the filename "Screenshot.png"
image.save("Screenshot.png")
