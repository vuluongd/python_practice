# Demonstrating the use of the copy() method in Python
numbers = [1, 2, 3, 4, 5]
numbers_copy = numbers.copy()
print(numbers_copy)
# Output: [1, 2, 3, 4, 5]
# The copy() method creates a shallow copy of the list

# Demonstrating the use of the copy module for deep copying
import copy
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)
print(deep_copied_list)
# Output: [[1, 2, 3], [4, 5, 6]]
# The deepcopy() function creates a deep copy of the list, including nested lists
