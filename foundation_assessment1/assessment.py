# TASK 2

with open('my_file.txt') as fh:
    text = fh.read()
    capital_letters = 0
    [count += 1 for character in text if character.isupper())

# TASK 3

def string_reverse(string):
    return string[::-1]

string_reverse("Konstantynopolitanczyk")

# TASK 4

def longest_string(list_of_strings):
    return max(list_of_strings, key=len)

example_list = ['cat', 'horse', 'elephant', 'dog']

longest_string(example_list)

# TASK 5

print ("Please select operation - \n "
"1. Add \n "
"2. Subtract \n "
"3. Multiply \n "
"4. Divide \n " )
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4: "))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if select not in range(1,5):
    print('Wrong input.')
if select == 1:
    print(add(number_1, number_2))
elif select == 2:
    print(subtract(number_1, number_2))
elif select == 3:
    print(multiply(number_1, number_2))
elif select == 4:
    print(divide(number_1, number_2))