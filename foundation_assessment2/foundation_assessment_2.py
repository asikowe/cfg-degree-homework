# TASK 3

# Write a function that can define whether a word is a Palindrome or not
# (a word, phrase, or sequence that reads the same backwardsas forwards, e.g. madam)

def palindrome_check(item):
    return item == item[::-1]

print(palindrome_check("madam"))

# TASK 4

# Write tests for the newly created Palindrome function. Provide a brief explanation for your test case options.

import unittest

class TestPalindromeCheckFunction(unittest.TestCase):
    def test_palindrome_check_true(self):
        expected = True
        result = palindrome_check('madam')
        self.assertEqual(expected, result)

    def test_palindrome_check_false(self):
        expected = False
        result = palindrome_check('Joanna')
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

# Depending on the argument we pass to function, it will either return True or False statement. We want to make sure
# it works correctly for both.


# TASK 9

def find_numbers(numbers, expected_sum):
    lookup = {}
    number_list = []
    for index, num in enumerate(numbers):
        if num in lookup:
            number_list.append([numbers[lookup[num]], numbers[index]])
        lookup[expected_sum - num] = index
    return number_list


my_numbers = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10

print(find_numbers(my_numbers, target_sum))
