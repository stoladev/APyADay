letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4,
          4, 8, 4, 10]
letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points.update({" ": 0})


def score_word(word):
    point_total = 0
    for letter in word:
        try:
            point_total += letter_to_points[letter]
        except ValueError:
            point_total += 0
    return point_total


print(score_word("HELLO"))

brownie_points = score_word("BROWNIE")

print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],
                   "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                   "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


tarot = {1: "The Magician", 2: "The High Priestess",
         3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
         6: "The Lovers", 7: "The Chariot",
         8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune",
         11: "Justice", 12: "The Hanged Man", 13: "Death",
         14: "Temperance", 15: "The Devil", 16: "The Tower",
         17: "The Star", 18: "The Moon", 19: "The Sun",
         20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)

print(spread)

spread["present"] = tarot.pop(22)

spread["future"] = tarot.pop(10)

for key, value in spread.items():
    print("Your " + key + " is the " + value + " card.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

available_items = {"health potion": 10, "cake of the cure": 5,
                   "green elixir": 20, "strength sandwich": 25,
                   "stamina grains": 15, "power stew": 30}

health_points = 20

health_points += available_items.get("stamina grains", 0)
available_items.pop("stamina grains", 0)

health_points += available_items.get("power stew", 0)
available_items.pop("power stew", 0)

health_points += available_items.get("mystic bread", 0)
available_items.pop("mystic bread", 0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On",
         "Respect", "Good Vibrations"]

playcounts = [78, 29, 44, 21, 89, 5]

plays = {song: playcount for song, playcount in zip(songs, playcounts)}

print(plays)

plays.update({"Purple Haze": 1})

print(plays)

plays.update({"Respect": 94})

print(plays)

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {drink: caffeine for drink, caffeine in zipped_drinks}

print(drinks_to_caffeine)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
                 "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Imports
import random
from decimal import Decimal

# Variables
random_num = random.randint(1, 1000)
decimal_num = Decimal('0.531') * Decimal('2')

# Print statements
print("Hello there! Here's a random number:" + str(random_num + decimal_num))
