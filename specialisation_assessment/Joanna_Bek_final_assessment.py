"""
Algorithms 1 Solution
-------------------------------------------------------------------------------------------------------------------------
"""
def isValidSubsequence(array, sequence):
    # set the indices for both array and the sequence
    array_index = 0
    sequence_index = 0
    # set stopping points for while loop to avoid infinite loop
    while array_index < len(array) and sequence_index < len(sequence):
        # starting from element of array at index 0, compare its value to the value of element at index 0 of sequence
        if array[array_index] == sequence[sequence_index]:
            # if there's a match, move up to the next element of sequence
            sequence_index += 1
        # move to the next element of array and repeat the loop
        array_index += 1
    # return boolean for the result (True if sequence_index count reached the value of the length of the sequence, False if not)
    return sequence_index == len(sequence)

"""
    The time complexity of this solution is O(n) (the performance depends on the size of the input), whilst the space is O(1), 
    as we don't really store any results (array_index and sequence_index will be both just integers, no matter the size of an input).
    I've chosen this approach as for given test arrays it will perform very well. It is also easy to understand. If the order of
    the array and the sequence wasn't a concern, both could be sorted, which would make searching for matching values quicker.
    But when keeping the order, I would say this is, to my course-based knowledge, rather optimal solution.

"""

# Sample Tests for Algorithms 1
# ---------------------------------------------------------
array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]
print(isValidSubsequence(array1, sequence1))  # FALSE

array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]
print(isValidSubsequence(array2, sequence2))  # TRUE

array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]
print(isValidSubsequence(array3, sequence3))  # TRUE

"""
Algorithms 2 Solution
-------------------------------------------------------------------------------------------------------------------------
"""

def findThreeLargestNumbers(array):
    # make sure the length of an array is higher than or equal to 3
    if len(array) >= 3:
        # sort an array in a default ascending order and then display the last three values using slicing
        return sorted(array)[-3:]
    else:
        return 'The array must contain at least three elements.'

"""
    Python uses TimSort algorithm to perform .sort() and sorted() functions. Depending on the size of the array, it will either
    perform insertion sort (if it has less than 64 elements), or merge sort (for 64 or more elements). In worse case scenario 
    it will be of O(n log(n)) time complexity (for smaller lists it can be O(n)), with O(1) space complexity (not storing any results).
    If time was an essence, potentially Radix Sort with its O(nk) time complexity could be used. But for such a simple task
    it would add uneccessary complexity to the code itself, therefore I went with this simple solution.

"""

# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!

# Sample Tests for Algorithms 2
# ---------------------------------------------------------
array1 = [141, 1, 17, -17, -27, 18, 541, 8, 7, 7]
expectedOutput1 = [18, 141, 541]
print(str(findThreeLargestNumbers(array1)) + " <-- --> " + str(expectedOutput1))  # [18, 141, 541]

array2 = [141, 1, 214, -17, -27, 0, 541, 21, 7, 34]
expectedOutput2 = [141, 214, 541]
print(str(findThreeLargestNumbers(array2)) + " <-- --> " + str(expectedOutput2))  # [141, 214, 541]