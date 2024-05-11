import random
import time
import numpy as np

# Function to check if a list is sorted
def is_sorted(arr):
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return False

    return True


# Function to shuffle an array, keeping its
# element’s keys
def shuffle(arr):
    for i in range(0, len(arr)):
        new_elem = random.randint(0, len(arr) - 1)
        arr[i], arr[new_elem] = arr[new_elem], arr[i]


def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max1 = max(arr)

    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10


def counting_sort(arr):
    # Create a new list and a count for all keys
    new_ls = [0 for i in range(len(arr))]
    key_count = [0 for i in range(len(arr))]

    # Count how many times every key appears in the list
    for elem in arr:
        key_count[elem] += 1

    # Create a new list containing all the keys in order
    index = 0
    for key in range(len(arr)):
        if key_count[key] != 0:
            for _ in range(key_count[key]):
                new_ls[index] = key
                index += 1

    # Append the new list to the original list
    for i in range(len(arr)):
        arr[i] = new_ls[i]


def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


def merge_sort(seq):
    if len(seq) == 1:
        return seq
    left = merge_sort(seq[:len(seq) // 2])
    right = merge_sort(seq[len(seq) // 2:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_count = 0
    right_count = 0
    try:
        while True:
            if left[left_count] > right[right_count]:
                result.append(right[right_count])
                right_count += 1
            else:
                result.append(left[left_count])
                left_count += 1
    except:
        return result + left[left_count:] + right[right_count:]


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

                # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


test_list = []


def test1(algorithm):

    global test_list
    start_time = time.time()
    algorithm(test_list)
    end_time = time.time()

    print("Done test1")
    return (end_time - start_time) * 1000


def test2(algorithm):

    global test_list
    test_list = test_list[::-1]

    start_time = time.time()
    algorithm(test_list)
    end_time = time.time()

    print("Done test2")
    return (end_time - start_time) * 1000


def test3(algorithm):

    global test_list
    test_list = np.random.permutation(test_list)

    start_time = time.time()
    algorithm(test_list)
    end_time = time.time()

    print("Done test3")
    return (end_time - start_time) * 1000


def tests(algorithm, size):

    global test_list
    test_list = [i for i in range(size)]
    result1 = test1(algorithm)
    result2 = test2(algorithm)
    result3 = test3(algorithm)

    return result1, result2, result3


alg = selection_sort
n = 10
results = tests(alg, n)

if float("{:.4f}".format(results[0])) < 1000:
    t1 = str("{:.4f}".format(results[0]))
    print("Best case: " + t1 + "ms")
else:
    t1 = str(float("{:.4f}".format(results[0] / 1000)))
    print("Best case: " + t1 + "s")

if float("{:.4f}".format(results[1])) < 1000:
    t1 = str("{:.4f}".format(results[1]))
    print("Average case: " + t1 + "ms")
else:
    t1 = str(float("{:.4f}".format(results[1] / 1000)))
    print("Average case: " + t1 + "s")

if float("{:.4f}".format(results[2])) < 1000:
    t1 = str("{:.4f}".format(results[2]))
    print("Worst case: " + t1 + "ms")
else:
    t1 = str(float("{:.4f}".format(results[2] / 1000)))
    print("Worst case: " + t1 + "s")
