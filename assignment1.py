# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 9 July
# Description: This assignment includes multiple problems to be solved using the StaticArray class.
# Each function is designed to perform a specific task such as finding the minimum and maximum values
# in an array, implementing the FizzBuzz logic, reversing the elements of an array, rotating elements,
# creating a range of values, checking if an array is sorted, finding the mode, removing duplicates,
# sorting using count sort, and creating a sorted array of squares. The functions must handle edge
# cases and be optimized for performance where applicable.

import random

class StaticArrayException(Exception):
    """
    Custom exception for Static Array class.
    Any changes to this class are forbidden.
    """
    pass

class StaticArray:
    """
    Implementation of Static Array Data Structure.
    Implemented methods: get(), set(), length()
    Any changes to this class are forbidden.
    Even if you make changes to your StaticArray file and upload to Gradescope
    along with your assignment, it will have no effect. Gradescope uses its
    own StaticArray file (a replica of this one) and any extra submission of
    a StaticArray file is ignored.
    """
    def __init__(self, size: int = 10) -> None:
        """
        Create array of given size.
        Initialize all elements with values of None.
        If requested size is not a positive number,
        raise StaticArray Exception.
        """
        if size < 1:
            raise StaticArrayException('Array size must be a positive integer')
        self._size = size
        self._data = [None] * size

    def __iter__(self):
        """
        Disable iterator capability for StaticArray class.
        """
        return None

    def __str__(self) -> str:
        """Override string method to provide more readable output."""
        return f"STAT_ARR Size: {self._size} {self._data}"

    def get(self, index: int):
        """
        Return value from given index position.
        Invalid index raises StaticArrayException.
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        return self._data[index]

    def set(self, index: int, value) -> None:
        """
        Store value at given index in the array.
        Invalid index raises StaticArrayException.
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        self._data[index] = value

    def __getitem__(self, index: int):
        """Enable bracketed indexing."""
        return self.get(index)

    def __setitem__(self, index: int, value: object) -> None:
        """Enable bracketed indexing."""
        self.set(index, value)

    def length(self) -> int:
        """Return length of the array (number of elements)."""
        return self._size

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
def min_max(arr: StaticArray) -> tuple[int, int]:
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, arr.length()):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    return min_val, max_val

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
def fizz_buzz(arr: StaticArray) -> StaticArray:
    result = StaticArray(arr.length())
    for i in range(arr.length()):
        if arr[i] % 3 == 0 and arr[i] % 5 == 0:
            result[i] = "fizzbuzz"
        elif arr[i] % 3 == 0:
            result[i] = "fizz"
        elif arr[i] % 5 == 0:
            result[i] = "buzz"
        else:
            result[i] = arr[i]
    return result

# ------------------- PROBLEM 3 - REVERSE -----------------------------------
def reverse(arr: StaticArray) -> None:
    left = 0
    right = arr.length() - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------
def rotate(arr: StaticArray, steps: int) -> StaticArray:
    n = arr.length()
    result = StaticArray(n)
    steps = steps % n  # handle steps larger than array size
    for i in range(n):
        result[(i + steps) % n] = arr[i]
    return result

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
def sa_range(start: int, end: int) -> StaticArray:
    if start <= end:
        size = end - start + 1
        result = StaticArray(size)
        for i in range(size):
            result[i] = start + i
    else:
        size = start - end + 1
        result = StaticArray(size)
        for i in range(size):
            result[i] = start - i
    return result

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
def is_sorted(arr: StaticArray) -> int:
    ascending = True
    descending = True
    for i in range(1, arr.length()):
        if arr[i] < arr[i - 1]:
            ascending = False
        if arr[i] > arr[i - 1]:
            descending = False
    if ascending:
        return 1
    if descending:
        return -1
    return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------
def find_mode(arr: StaticArray) -> tuple[object, int]:
    mode = arr[0]
    max_count = 1
    current = arr[0]
    current_count = 1
    for i in range(1, arr.length()):
        if arr[i] == current:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = current
            current = arr[i]
            current_count = 1
    if current_count > max_count:
        max_count = current_count
        mode = current
    return mode, max_count

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------
def remove_duplicates(arr: StaticArray) -> StaticArray:
    if arr.length() == 0:
        return arr
    result = StaticArray(arr.length())
    index = 0
    result[index] = arr[0]
    for i in range(1, arr.length()):
        if arr[i] != arr[i - 1]:
            index += 1
            result[index] = arr[i]
    final_result = StaticArray(index + 1)
    for i in range(index + 1):
        final_result[i] = result[i]
    return final_result

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
def count_sort(arr: StaticArray) -> StaticArray:
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, arr.length()):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    range_of_values = max_val - min_val + 1
    count_array = StaticArray(range_of_values)
    for i in range(count_array.length()):
        count_array[i] = 0
    for i in range(arr.length()):
        count_array[arr[i] - min_val] += 1
    sorted_arr = StaticArray(arr.length())
    index = 0
    for i in range(count_array.length()):
        while count_array[i] > 0:
            sorted_arr[index] = i + min_val
            index += 1
            count_array[i] -= 1
    return sorted_arr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------
def sorted_squares(arr: StaticArray) -> StaticArray:
    size = arr.length()
    result = StaticArray(size)
    left = 0
    right = size - 1
    for i in range(size - 1, -1, -1):
        if abs(arr[left]) > abs(arr[right]):
            result[i] = arr[left] ** 2
            left += 1
        else:
            result[i] = arr[right] ** 2
            right -= 1
    return result

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = " " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
        print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
