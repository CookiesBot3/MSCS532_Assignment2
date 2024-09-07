from mergeSort import mergeSort, getMergeN
from quickSort import quickSort, getQuickN
import time
import random
import tracemalloc

# Generate the dataset base on size and the flag.
# size is the size of the array and the values from 1 to size
# Flags are kept to all false by default.
def generate_data(size, random_flag=False, ascending=False, descending=False):
    # Generates Random numbers in the array according to the size
    if random_flag:
        return random.sample(range(1, size + 1), size)
    # Generates ascending numbers in the array according to the size
    if ascending:
        temp = []
        for i in range(size):
            temp.append(i+1)
        return list(temp) # list() is used to decouple the array for a deepcopy
    # Generates descending numbers in the array according to the size
    if descending:
        temp = []
        for i in range(size, 0, -1):
            temp.append(i)
        return list(temp) # list() is used to decouple the array for a deepcopy

def sort_runner(arr, mergeFlag = False, arrayType = 0):
    type = ""
    array_data_type = ""

    #flags to determine which data type it is sorting.
    if arrayType == 1:
        array_data_type = "random"
    elif arrayType == 2 :
        array_data_type = "ascending"
    else:
        array_data_type = "descending"
    sorted = []

    print(array_data_type + " before: ", arr)
    start_time = time.process_time() #start the timer
    tracemalloc.start()
    if mergeFlag:
        type = "merge sort"
        sorted = mergeSort(arr)# sort dataset
    else:
        type = "quick sort"
        quickSort(arr)# sort in place
    end_time = time.process_time() #end the timer
    first_size, first_peak = tracemalloc.get_traced_memory()
    #Print out the proper result
    print(type + " time: ", end_time - start_time)
    print(type + ": " f"{first_size=}, {first_peak=}")
    tracemalloc.reset_peak()
    if mergeFlag:
        print(array_data_type + " after sorted: ", sorted)
        print("Number of operations: ", getMergeN())
    else:
        print(type + " after sorted: ", arr)
        print("Number of operations: ", getQuickN())

    print('\n')

if __name__ == '__main__':
    size = 250#Size of the array and values from 1 to size

    # Generate all the array dataset according to the flag ie. Random, ascending, descending
    arrayRandom = generate_data(size, random_flag=True)
    arrayAscending = generate_data(size, ascending=True)
    arrayDescending = generate_data(size, descending=True)

    arrayRandomQuick = generate_data(size, random_flag=True)
    arrayAscendingQuick = generate_data(size, ascending=True)
    arrayDescendingQuick = generate_data(size, descending=True)

    # Run the Sorter for each type of the array for merge and quick sort
    sort_runner(arrayRandom, mergeFlag=True, arrayType=1)
    sort_runner(arrayAscending, mergeFlag=True, arrayType=2)
    sort_runner(arrayDescending, mergeFlag=True, arrayType=3)

    sort_runner(arrayRandomQuick, mergeFlag=False, arrayType=1)
    sort_runner(arrayAscendingQuick, mergeFlag=False, arrayType=2)
    sort_runner(arrayDescendingQuick, mergeFlag=False, arrayType=3)



