"""
Various and sundry sorting algorithms.
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

def merge(leftArray: list, rightArray: list):
    """
A helper function to merge sort. Merges two lists together in order.
    """
    if leftArray > rightArray:
        return rightArray + leftArray
    else:
        return leftArray + rightArray

def quick_sort(listToSort, start, end):
    if end <= start:
        return
    
    pivot = quick_sort_partition(listToSort, start, end)
    quick_sort(listToSort, start, pivot - 1)
    quick_sort(listToSort, pivot + 1, end)

def quick_sort_partition(listToSort, start, end):
    pivot = listToSort[end]
    listLength = len(listToSort)
    i = start - 1
    for j in range(start, listLength - 1):
        if listToSort[j] < pivot:
            i += 1
            swap_elements(listToSort, j, i)
    i += 1
    swap_elements(listToSort, i, end)
    return i
