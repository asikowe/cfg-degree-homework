## :heavy_plus_sign: Two Sum
Given an array of integers nums and an integer target, return two numbers inside that array such that they add up to target.

You may assume that each input would have at least one solution, and you may not use the same element twice.

You can return the answer in any order.

#### EXAMPLE 1:
Input: nums = [2,7,11,15], target = 9

Output: [2, 7]

Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].

#### EXAMPLE 2:
Input: nums = [3,2,4], target = 6

Output: [2, 4]

#### EXAMPLE 3:
Input: nums = [3,3], target = 6

Output: [3, 3]

## :pencil: NOTES:
* An input MAY HAVE no two numbers at all (an empty one still counts as a solution) - in this case, return a empty array
* It's an array of integer numbers - these numbers are not necessarily distinct / unique
* Make sure to discuss your solution - what is the Big O Time & Space complexity? Was there any way you could've done better or not? Why or why not? Justify.

## :checkered_flag: SOLUTION:
```
def find_numbers(numbers, expected_sum):
    lookup = {}
    number_list = []
    for index, num in enumerate(numbers):
        if num in lookup:
            number_list.append([numbers[lookup[num]], numbers[index]])
        lookup[expected_sum - num] = index
    return number_list

nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6
print(find_numbers(nums1, target1))
print(find_numbers(nums2, target2))
print(find_numbers(nums3, target3))
```

## :tophat: EXPLANATION:

This solution uses hashing. It generates an empty hashmap (lookup), and a list to store the pairs that will be found. It then iterates through the elements of the array and checks if the number exists in the lookup. If it doesn't, it adds it to the lookup as {'expected_sum - num': current_index} pair. This means that if another number is in the lookup, that's a match.
Time complexity of this one is O(n). We go through our list of numbers only once, and lookup in our hashmap costs O(1) for each time.
Space complexity is O(n), as the extra space required depends on the number of items in a list, and in worst case scenario it will be n-elements.

I think this is a decent time/space complexity for given problem. It uses any given number just once, but deals with scenario where there are duplicate numbers in a list passed as an argument (thanks to adding index as a value, it keeps track of which number was accessed), it also doesn't break when the given list is empty. 