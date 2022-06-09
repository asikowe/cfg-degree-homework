# Question 1 version 1
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)

# Question 1 version 2
chairs = '15'
nails = 4
total_nails = int(chairs) * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)


# Question 2
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)


# Question 3
amount_of_boxes = 6
eggs_in_a_box_of_eggs = 6
eggs_needed_for_omlette = 4
making_omlette = (amount_of_boxes*eggs_in_a_box_of_eggs)//eggs_needed_for_omlette
# Use conditions to format text correcly
if making_omlette == 1 and amount_of_boxes == 1:
    print(f'You can make {making_omlette} omlette with {amount_of_boxes} box of eggs.')
elif making_omlette > 1 and amount_of_boxes == 1:
    print(f'You can make {making_omlette} omlettes with {amount_of_boxes} box of eggs.')
elif making_omlette == 1 and amount_of_boxes > 1:
    print(f'You can make {making_omlette} omlette with {amount_of_boxes} boxes of eggs.')
elif making_omlette > 1 and amount_of_boxes > 1:
    print(f'You can make {making_omlette} omlettes with {amount_of_boxes} boxes of eggs.')
elif making_omlette < 1:
    print('No omlette for you today!')

# Question 4
# Task 1 - Replace the (.) character with (!) instead. Output should be “I love coding!”
my_str = "I love coding."
# Type your code here.
my_str = my_str.replace('.' ,'!')
print(my_str)

# Task 2 - Reassign str so that all of its characters are lowercase.
my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
# Type your code here.
my_str_1 = my_str_1.lower()
print(my_str_1)

# Task 3 - Output whether this string starts with an A or not
my_str_2 = "We enjoy travelling"
# Type your code here.
ans_1 = my_str_2.startswith('A')
print(ans_1)

# Task4 - What is the length of the given string?
my_str_3 = "1.458.001"
# Type your code here:
ans_2 = len(my_str_3)
print(ans_2)

# Question 5
# Task 1 - Slice the word so that you get "thon".
wrd = "Python"
# Type your answer here.
ans_1 = wrd[2:]
print(ans_1)

# Task 2 - Slice the word until "o". (Pyth)
wrd = "Python"
# Type your answer here.
ans_1 = wrd[:4]
print(ans_1)

# Task 3 - Now try to get "th" only.
wrd = "Python"
# Type your answer here.
ans_1 = wrd[2:4]
print(ans_1)

# Task 4 - Now slice the word with steps of 2, excluding first and last characters
wrd = "Python"
# Type your answer here.
ans_1 = wrd[1:-1:2]
print(ans_1)

# Question 7
def calculate_vat(amount):
    return amount * 1.2
total = calculate_vat(100)
print(total)

# Question 8

# Create empty dictionary to store values later
items = {}

# Request information from user
for num in range(1,4):
    items.update(dict({input(f'Item_{num}_name: '):float(input(f'Item_{num}_price: '))}))
    
# Define function
def cashier_receipt(d):
    total_sum = 0
    for key in d:
        print(key, d[key])
        total_sum = total_sum + d[key]
    print('TOTAL')
    print(total_sum)

# Run the function with the input from user
cashier_receipt(items)