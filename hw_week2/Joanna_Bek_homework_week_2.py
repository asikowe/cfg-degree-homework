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

"""
Nicely done, nice simply solution and nicely debugged. Loving the two
examples for slightly different use cases.
2/2
"""

# Question 2
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

"""
Again well debugged and explained with a nice simple solution proposed.
2/2
"""

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

"""
Took me a little while to figure out the variations but I'm there! The 1 omlettes and 1 boxes
strings must've really annoyed you!
Nice use of the `//` operator too.
5/5
"""

# Question 4
# Task 1 - Replace the (.) character with (!) instead. Output should be “I love coding!”
my_str = "I love coding."
# Type your code here.
my_str = my_str.replace('.' ,'!')
print(my_str)

"""
Smashed it, nice simple replace!
2/2
"""

# Task 2 - Reassign str so that all of its characters are lowercase.
my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
# Type your code here.
my_str_1 = my_str_1.lower()
print(my_str_1)

"""
Nice reassignment.
2/2
"""

# Task 3 - Output whether this string starts with an A or not
my_str_2 = "We enjoy travelling"
# Type your code here.
ans_1 = my_str_2.startswith('A')
print(ans_1)

"""
Nicely done, good old trusty `startswith` comes in handy.
2/2
"""

# Task4 - What is the length of the given string?
my_str_3 = "1.458.001"
# Type your code here:
ans_2 = len(my_str_3)
print(ans_2)

"""
My favorite string method and nice variable assignment.
2/2
"""

# Question 5
# Task 1 - Slice the word so that you get "thon".
wrd = "Python"
# Type your answer here.
ans_1 = wrd[2:]
print(ans_1)

"""
Nicely done. Equally as valid is [-4:] but I tend to work with positive
indexes where possible as lists can be appended to. Great work.
2/2
"""

# Task 2 - Slice the word until "o". (Pyth)
wrd = "Python"
# Type your answer here.
ans_1 = wrd[:4]
print(ans_1)

"""
Nothing wrong with this at all. Good understanding of the list indices. If you
didn't know where the "o" was you could use .index("o") initially.
2/2
"""

# Task 3 - Now try to get "th" only.
wrd = "Python"
# Type your answer here.
ans_1 = wrd[2:4]
print(ans_1)

"""
Again, smashed it!
2/2
"""

# Task 4 - Now slice the word with steps of 2, excluding first and last characters
wrd = "Python"
# Type your answer here.
ans_1 = wrd[1:-1:2]
print(ans_1)

"""
Great indexing, if this doesn't trip you up nothing will.
2/2
"""

"""
Q5 - Aced them all. You've shown you understand these inside out.
"""

"""
Q6 - You've understood the iteration and length of the range output. Thankfully
your last sentenced saved you because your indentation in your document is
incorrectly copied over. The print is included in the for loop in the question
so it will print the strings for each number in turn.
5/5
"""

# Question 7
def calculate_vat(amount):
    return amount * 1.2
total = calculate_vat(100)
print(total)

"""
Concise explanation of the issue. Simple and effective suggested solution.
5/5
"""

# Question 8

# Define function
def cashier_receipt():
    # Create empty dictionary to store values later
    items = {}
    total_sum = 0
    # Request user input for three items and update dictionary
    for num in range(1,4):
        items.update(dict({input(f'Item_{num}_name: '):float(input(f'Item_{num}_price: '))}))
    # Count total and print the receipt
    for key in items:
        print(key, items[key])
        total_sum += items[key]
    print('TOTAL', total_sum)

# Call function
cashier_receipt()

"""
Great use of dictionaries here and a great user input loop! You've set the item
limit to 3 as required and print a receipt for each item. I have 2 very slight 
comments, the method of adding an item uses .update which doesn't allow for 
duplicates, what if I want to buy 2 or 3 of the same item? Additionally if your
input price includes a float you sometimes get floating point errors so it doesn't
meet the format required. Minor things but worth being mindful of.
4/5
"""

# slight variation
def cashier_receipt():
    # Create empty dictionary to store values later
    items = []
    total_sum = 0
    # Request user input for three items and update dictionary
    for num in range(1,4):
        items.append(dict({
            'name': input(f'Item_{num}_name: '),
            'price': float(input(f'Item_{num}_price: ')),
        }))
    # Count total and print the receipt
    for item in items:
        print(item['name'], f"{item['price']:#.2f}")
        total_sum += item['price']
    print(f'TOTAL: {total_sum:#.2f}')

# Call function
cashier_receipt()
