name = input("Enter Your Full Name: ")
length_of_name = len(name)
if length_of_name > 15:
    print("The length of name is greater then 15.")
else:
    print()

fname = input("Enter Your Father Name: ")
length_of_fname = len(fname)
if length_of_fname > 15:
    print("The length of name is greater then 15.")
else:
    print()

# jazz
# intialize a empty list
jazz = []
str1 = "030"
# Loop through a range of numbers.
x = range(10)
for i in x:
# Append the square of i to the list
    jazz.append(str1 + str(i))

# Telenor
telenor = []
str2 = '034'
y = range(8)
for i in y:
    telenor.append(str2 + str(i))

# Ufone
ufone = []
str3 = '033'
z = range(8)
for i in z:
    ufone.append(str3 + str(i))

# Zong
zong = []
str4 = '031'
a = range(5)
for i in a:
    zong.append(str4 + str(i))

phone_number = input("Enter Your Phone Number: ")
num_length = len(phone_number)
if num_length == 11:
    print("Valid Phone Number.")
else:
    exit("Invalid phone number kindly try again.")

first_four_digit = phone_number[:4]

if first_four_digit in jazz:
    print("Service Provider: Jazz")

elif first_four_digit in zong:
    print("Service provider: Zong")

elif first_four_digit in ufone:
    print("Service provider: Ufone")

elif first_four_digit in telenor:
    print("Service provider: Telenor")

else:
    print("Invalid Phone number, kindly check and try again.")

cnic_num = str(input("Enter your CNIC number with '-': "))
length_of_cnic = len(cnic_num)
if length_of_cnic > 15:
    exit("Inncorrect cnic number kindly check it and try again.")
elif length_of_cnic < 15:
    exit("Incorrect cnic number kindly check it and try again.")
else:
    print()

if cnic_num[5] == "-" and cnic_num[13] == "-":
    print("Valid Cnic.")
else:
    exit("Incorect Cnic Format (also include dashes).")


day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
year = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

print("Please Enter your Date of Birth one by one in the following format: day-month-year (5-6-2002).")
dob_day = int(input("Enter the day you were born (e.g., 5 or 6): "))
if dob_day in day:
    print("Valid Day.")
else:
    exit("Invalid date! Please check again.")


dob_month = int(input("Enter the month you were born in (e.g., 6): "))
if dob_month in month:
    print("Valid Month.")
else:
    exit("Invalid month! Please check again.")


dob_year = int(input("Enter the year you were born in (e.g., 2002): "))
if dob_year in year:
    exit("Your are not 18 years old, You are not Eligible.")

else:
    print("Valid Year.")


date_of_birth = str(dob_day) + "-" + str(dob_month) + "-" + str(dob_year)
print("Your Date of Birth According to you is:", date_of_birth)
choice = input("Do you want to proceed with this Date of birth. y/n: ").lower()
if choice == "y":
    print()
else:
    exit("Kindly Fill the form again.")

print("Enter your Email Below, Note only gmail accounts are allowed. Ex: Email@gmail.com")
email = input("Enter you Email: ")
if "@" and "gmail.com" in email:
    print("Valid Email.")
else:
    exit("Invalid Email.")

print("Enter your address in parts, 1st your coloney, 2nd your House No, 3rd your city.")
coloney = input("Enter your coloney: ")
house_no = input("Enter you House No: ")
city = input("Enter you city: ")
if coloney and house_no and city == "":
    print("Invalid Address please check and try again.")
else:
    print()

address = coloney + house_no + city
print("your address according to you is: ", address)
print("Your form has suceesfully filled out.")







