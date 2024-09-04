from mergeSort import mergeSort, getMergeN
from quickSort import quickSort, getQuickN
import time
import random

# Generate the dataset base on size and the flag.
# size is the size of the array and the values from 1 to size
# Flags are kept to all false by default.
def generateData(size ,randomFlag=False, ascending=False, descending=False):
    # Generates Random numbers in the array according to the size
    if randomFlag:
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

def sortRunner(arr, mergeFlag = False, arrayType = 0):
    type = ""
    arrayDataType = ""

    #flags to determine which data type it is sorting.
    if arrayType == 1:
        arrayDataType = "random"
    elif arrayType == 2 :
        arrayDataType = "ascending"
    else:
        arrayDataType = "descending"
    sorted = []

    print(arrayDataType + " before: ", arr)
    start_time = time.process_time() #start the timer
    if mergeFlag:
        type = "merge sort"
        sorted = mergeSort(arr)# sort dataset
    else:
        type = "quick sort"
        quickSort(arr)# sort in place
    end_time = time.process_time() #end the timer

    #Print out the proper result
    print(type + " time: ", end_time - start_time)
    if mergeFlag:
        print(arrayDataType + " after sorted: ", sorted)
        print("Number of operations: ", getMergeN())
    else:
        print(type + " after sorted: ", arr)
        print("Number of operations: ", getQuickN())

    print('\n')

if __name__ == '__main__':
    size = 350 #Size of the array and values from 1 to size

    # Generate all the array dataset according to the flag ie. Random, ascending, descending
    arrayRandom = generateData(size, randomFlag=True)
    arrayAscending = generateData(size, ascending=True)
    arrayDescending = generateData(size, descending=True)

    arrayRandomQuick = generateData(size, randomFlag=True)
    arrayAscendingQuick = generateData(size, ascending=True)
    arrayDescendingQuick = generateData(size, descending=True)

    # Run the Sorter for each type of the array for merge and quick sort
    sortRunner(arrayRandom, mergeFlag=True, arrayType=1)
    sortRunner(arrayAscending, mergeFlag=True, arrayType=2)
    sortRunner(arrayDescending, mergeFlag=True, arrayType=3)

    sortRunner(arrayRandomQuick, mergeFlag=False, arrayType=1)
    sortRunner(arrayAscendingQuick, mergeFlag=False, arrayType=2)
    sortRunner(arrayDescendingQuick, mergeFlag=False, arrayType=3)



