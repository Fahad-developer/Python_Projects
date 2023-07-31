import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Get input from the user for the phone number with country code
mobileNo = input("Enter phone number with country code (+xx xxxxxxxx): ")

# Set a default region for parsing (e.g., "US")
default_region = "US"

# Parse the phone number using the phonenumbers library, considering the default region
mobileNo = phonenumbers.parse(mobileNo, default_region)

# Check if the parsed phone number is valid
if phonenumbers.is_valid_number(mobileNo):
    # If the phone number is valid, print the time zones for the number's region
    print("Phone number belongs to region:", timezone.time_zones_for_number(mobileNo))
    # Print the service provider for the phone number (in English)
    print("Service provider:", carrier.name_for_number(mobileNo, "en"))
    # Print the description of the country where the phone number belongs (in English)
    print("Phone number belongs to country:", geocoder.description_for_number(mobileNo, "en"))
else:
    # If the phone number is not valid, inform the user to enter a valid mobile number
    print("Please enter a valid mobile number.")
