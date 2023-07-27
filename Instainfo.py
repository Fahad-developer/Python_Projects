import instaloader

# Create an instance of Instaloader
ig = instaloader.Instaloader()

# Print a developer message
print("Program is Developed by Muhammad Fahad.")

# Prompt the user to enter an Instagram username
username = input("Enter Instagram Username: ")

# Retrieve the profile of the specified username
profile = instaloader.Profile.from_username(ig.context, username)

# Print the username
print("Username: ", profile.username)

# Print the number of posts uploaded by the profile
print("Number of posts uploaded: ", profile.mediacount)

# Print the number of followers
print(profile.username + " has " + str(profile.followers) + ' followers.')

# Print the number of people the profile is following
print(profile.username + " is following " + str(profile.followees) + ' people.')

# Print the biography of the profile
print("Bio: ", profile.biography)

# Download the profile's pictures only
ig.download_profile(username, profile_pic_only=True)
