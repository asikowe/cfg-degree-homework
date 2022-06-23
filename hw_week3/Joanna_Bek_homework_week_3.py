# # TASK 1
# # QUESTION 1

# is_raining = input('Is it raining? y/n ')

# if is_raining == 'y':
#     print("Take an umbrella.")
# elif is_raining == 'n':
#     print("You don't need an umbrella.")
# else:
#     print("Invalid input")

# # QUESTION 2
# my_money = int(input('How much money do you have? '))
# boat_cost = 20 + 5
# if my_money > boat_cost:
#     print('You can afford the boat hire')
# else :
#     print('You cannot afford the board hire')

# # QUESTION 3
# acceptable_values = list(range(1800,1951))
# date = int(input("What year was the book published? "))

# if date in acceptable_values:
#     if date <= 1819:
#         print("Nineteenth Century, First Decade")
#     elif date <= 1829:
#         print("Nineteenth Century, Twenties")
#     elif date <= 1839:
#         print("Nineteenth Century, Thirties")
#     elif date <= 1849:
#         print("Nineteenth Century, Forties")
#     elif date <= 1859:
#         print("Nineteenth Century, Fifties")
#     elif date <= 1869:
#         print("Nineteenth Century, Sixties")
#     elif date <= 1879:
#         print("Nineteenth Century, Seventies")
#     elif date <= 1889:
#         print("Nineteenth Century, Eighties")
#     elif date <= 1899:
#         print("Nineteenth Century, Nineties")
#     elif date <= 1919:
#         print("Twentieth Century, First Decade")
#     elif date <= 1929:
#         print("Twentieth Century, Twenties")
#     elif date <= 1939:
#         print("Twentieth Century, Thirties")
#     elif date <= 1949:
#         print("Twentieth Century, Forties")
#     elif date == 1950:
#         print("Twentieth Century, Fifties")
# else:
#     print("Our bookshop sells only books published between 1800 and 1950.")

# # TASK 2
# # QUESTION 1
# shopping_list = [
# "oranges",
# "cat food",
# "sponge cake",
# "long-grain rice",
# "cheese board"
# ]

# print(shopping_list[0])

# # QUESTION 2
# chocolates = {
# 'white': 1.50,
# 'milk': 1.20,
# 'dark': 1.80,
# 'vegan': 2.00
# }

# user_choice = input('Which chocolate you would like to buy? Available choices are: white, milk, dark or vegan. ')
# print(f'The price for this chocolate is: £{chocolates[user_choice]}')

# # QUESTION 3
# import random

# # list of seven numbers representing lottery ticket
# lottery_numbers = [2, 6, 8, 9, 16, 18, 20]

# # generate seven unique numbers in a range
# random_numbers = random.sample(range(1, 21), k=7)

# # find matches
# common_numbers = set(lottery_numbers).intersection(random_numbers)

# # print tidied statements
# print(f'The lottery numbers for today are: {", ".join(map(str, lottery_numbers))}')

# print(f'Your numbers are: {", ".join(map(str, sorted(random_numbers)))}')

# print(f'The numbers that match are: {", ".join(map(str, sorted(common_numbers)))}')

# # calculate winnings
# if len(common_numbers) < 3:
#     print("Better luck next time!")
# if len(common_numbers) == 3:
#     print("You have won £20!")
# if len(common_numbers) == 4:
#     print("You have won £40!")
# if len(common_numbers) == 5:
#     print("You have won £100!")
# if len(common_numbers) == 6:
#     print("You have won £10000!")
# if len(common_numbers) == 7:
#     print("JACKPOT! You have won £1000000!")

# # TASK 3
# # QUESTION 2
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'w') as poem_file:
#     poem_file.write(poem)
#     print('Poem written to a file')

# # QUESTION 3
# # store lyrics in a variable
# lyrics = '''You could never know what it's like
# Your blood like winter freezes just like ice
# And there's a cold lonely light that shines from you
# You'll wind up like the wreck you hide behind that mask you use
# And did you think this fool could never win?
# Well look at me, I'm coming back again
# I got a taste of love in a simple way
# And if you need to know while I'm still standing, you just fade away
# Don't you know I'm still standing better than I ever did
# Looking like a true survivor, feeling like a little kid
# I'm still standing after all this time
# Picking up the pieces of my life without you on my mind
# I'm still standing (Yeah, yeah, yeah)
# I'm still standing (Yeah, yeah, yeah)'''

# # write lyrics to a file
# with open('song.txt', 'w') as file:
#     file.write(lyrics)
#     print('Lyrics written to a file')

# # check if file has been created
# with open('song.txt', 'r') as file:
#     [print(line.strip()) for line in file.readlines()]

# # print lines with word 'still' only
# with open('song.txt', 'r') as file:
#     [print(line.strip()) for line in file.readlines() if 'still' in line]

# # If we also wanted to include possibility of 'Still':
# with open('song.txt', 'r') as file:
#     [print(line.strip()) for line in file.readlines() if 'still' in line.lower()]

# # TASK 4
# # QUESTION 1
# import requests
# import random

# # create a list of 6 unique pokemon numbers from a sample of 100
# pokemon_number = sorted(random.sample(range(1,101), k=6))

# # with file open, loop through the numbers and retrieve needed information. Format the answer and write it to a file.
# with open('pokemon.txt', 'w') as file:
#     for number in pokemon_number:
#         pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}/').json()
#         file.write("Pokemon name: " + pokemon['name'].capitalize() + ".\n")
#         file.write("Its moves are: " )
#         [file.write(move['move']['name'].capitalize() + ". ") for move in pokemon['moves']]
#         file.write("\n")
#     print("Written to a file.")

# # to check if it's there:
# with open('pokemon.txt', 'r') as file:
#     [print(line.strip()) for line in file]

# # QUESTION 2
# from pprint import pprint as pp
# import requests

# response = requests.get('https://opentdb.com/api.php?amount=3').json()

# pp(response)