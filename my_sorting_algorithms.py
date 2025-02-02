"""
Various and sundry sorting and search algorithms.
"""

import random as rnd #-- will be removed as soon as I can work out random number generation

def diy_shuffle(listToShuffle: list):
    """
Shuffles the given list well enough for my tastes.
    """
    first = 0
    last = 0
    length = len(listToShuffle) - 1
    for cycle in range(length):
        first = rnd.randint(-1, length)
        last = rnd.randint(-1, length)
        swap_elements(listToShuffle, first, last)

def is_sorted(listToCheck: list):
    """
Checks to see if given list is sorted.
    """
    for index,value in enumerate(listToCheck):
        if index + 1 < len(listToCheck) and value > listToCheck[index + 1]:
            return False
    return True

def swap_elements(listToRearrange: list, indexOne: int, indexTwo: int):
    """
Swaps two elements of the given list at indexOne and indexTwo.
    """
    x = listToRearrange[indexOne]
    y = listToRearrange[indexTwo]
    listToRearrange[indexOne] = y
    listToRearrange[indexTwo] = x
    return listToRearrange

def bubble_sort(listToSort: list):
    """
Pretty standard bubble sort. Pass in a list to have it work its magic.\n
Appears to be stable.
    """
    while is_sorted(listToSort) == False:
        for index,value in enumerate(listToSort):
            if index < len(listToSort) - 1:
                if value > listToSort[index + 1]:
                    swap_elements(listToSort, index, index + 1)

def bogo_sort(listToSort: list):
    """
Unlike true BOGO sort, this only shuffles and checks the given list once.\n
It will let you know if it worked, though.
    """
    diy_shuffle(listToSort)
    if is_sorted(listToSort):
        print("Holy moly! BOGO sort worked!")
        return True
    else:
        return False

def binary_search(query: int | float | str, searchableList: list, queryIndex: int | None = None):
    """
Performs a binary search for the given query in the given iterable searchableList.
    """
    searchableList = sorted(searchableList) #-- eventually I'll create a more beefy sort algorithm and I can use that instead of sorted()
    listLength: int = len(searchableList)
    halfwayPoint: int = int(listLength / 2)
    if queryIndex == None:
        queryIndex = halfwayPoint

    if query < searchableList[0] or query > searchableList[-1]:
        return False, None

    if listLength == 1 and searchableList[halfwayPoint] != query:
        return False, None
    elif query == searchableList[halfwayPoint]:
        return True, queryIndex
    elif query < searchableList[halfwayPoint]:
        searchableRange: list = searchableList[:halfwayPoint]
        newHalfwayPoint: int = round_up(len(searchableRange) / 2)
        queryIndex -= newHalfwayPoint
        return binary_search(query, searchableRange, queryIndex)
    elif query > searchableList[halfwayPoint]:
        searchableRange: list = searchableList[halfwayPoint:]
        newHalfwayPoint: int = round_down(len(searchableRange) / 2)
        queryIndex += newHalfwayPoint
        return binary_search(query, searchableRange, queryIndex)

def round_up(number: int | float):
    """
Rounds a float up to the nearest integer.\n
A helper function to the binary_search function.
    """
    decimal = number % 1
    if type(number) == int:
        return number
    elif number % 1 == 0:
        return int(number)
    else:
        return int(number + (1 - decimal))

def round_down(number: int | float):
    """
Rounds a float down to the nearest integer.\n
A helper function to the binary_search function.
    """
    return int(number)
