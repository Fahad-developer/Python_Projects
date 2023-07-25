# Importing random module.
import random
# Creating a dictionary with two values Keys and Value pairs.
word_hint_dict = {
    "apple": "A round fruit with red or green skin.",
    "banana": "A long, curved fruit with yellow skin.",
    "carrot": "A long, orange vegetable that grows underground.",
    "dog": "A common pet with four legs and a wagging tail.",
    "football": "A popular sport played with a round ball.",
    "house": "A place where people live.",
    "island": "A piece of land surrounded by water.",
    "koala": "A small, furry animal native to Australia.",
    "watermelon": "A juicy fruit with a green rind and sweet red flesh.",
    "yoga": "A physical, mental, and spiritual practice originating from ancient India.",
    "zebra": "A large mammal with black and white stripes.",
    "airplane": "A powered flying vehicle with fixed wings and a weight greater than that of the air it displaces.",
    "basketball": "A team sport played with a round ball and hoops.",
    "cat": "A small domesticated carnivorous mammal.",
    "dolphin": "A highly intelligent marine mammal known for its agility and playful behavior.",
    "elephant": "A large land mammal with a long trunk and tusks.",
    "flower": "The reproductive structure found in plants.",
    "giraffe": "A tall African mammal with a long neck and patterned coat.",
    "hamburger": "A popular food consisting of a cooked ground meat patty in a bun.",
    "ice cream": "A frozen dessert made from dairy products and sweet flavors.",
    "jungle": "A dense forest in a tropical region.",
    "kangaroo": "A marsupial mammal from Australia with strong hind legs for hopping.",
    "lemon": "A yellow citrus fruit with a sour taste.",
    "monkey": "A small to medium-sized primate that is highly agile and has a long tail.",
    "nurse": "A person trained to care for sick or injured people, especially in a healthcare setting.",
    "ocean": "A vast body of saltwater that covers most of the Earth's surface.",
    "piano": "A large musical instrument with a keyboard.",
    "queen": "The female ruler of a kingdom.",
    "river": "A large natural flow of water that runs through the land.",
    "sunflower": "A tall, bright yellow flower with a large center.",
    "tiger": "A large, carnivorous feline with distinctive stripes.",
    "umbrella": "A device used for protection against rain or sunlight.",
}

# Taking input of user name and saving it in name variable.
name = input("Enter Your Name: ")
# Printing the user name and greetings.
print("Welcome",name, " in WordWiz.")
# Taking option from the user.
play = input("Shoud we get started y/n: ")
# If option is y then we continue with the game.
if play == "y":
	print("Okay! Let's play the game.")
# If option is No then we exit the game.
else:
	print("Okay maybe later.")
    # A method to exit.
	exit()

# Creating a variable and selecting a key value randomly from the dic using random module.
random_word = random.choice(list(word_hint_dict.keys()))
# Creating a varianle and assigning it the value of key from dic.
hint = word_hint_dict[random_word]
# Creating a variable assigning the value of 5 which is going to be the maxium turns offered to user.
turns = 5
# Creating a variable to count the failure of user.
failure = 0
# Creating a varibale and saving the len of the word.
word_length = len(random_word)

print("We have selected a word for you.")
print("The Hint is:", hint)
print("The total alphabets in the word is:", word_length)
# Using while loop.
while turns > 0:
    # Taking input from the user about the guess word.
    guess = input("What could it be?: ").lower()
    # Comparing if the guess number is same as the random word that is selected.
    if guess == random_word:
        print("Congratulations! You win.")
        break
    else:
        print("Sorry! Wrong answer!")
        # Adding 1 in the failure.
        failure += 1
        # subtracting 1 from the turns.
        turns -= 1
        if turns == 0:
            print("You ran out of turns. The word was", random_word)
            break
        else:
            print("You have", turns, "turns left.")

result = input("Do you want to see the results: ")
if result == "y":
    print("===========********============")
    print("This game is Created By Muhammad Fahad.")
    print(f"The word is:{random_word}.")
    print(f"The word consist of : {word_length} Alphabets.")
    print(f"Remaining Turns = {turns}.")
    print(f"failed to guss {failure} Times.")
else:
    exit()












