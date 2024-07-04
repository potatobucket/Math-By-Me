import random as rnd #-- will be removed as soon as I can work out random number generation

def diy_shuffle(listToShuffle):
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

def is_sorted(listToCheck):
    """
Checks to see if given list is sorted.
    """
    for index,value in enumerate(listToCheck):
        if index + 1 < len(listToCheck) and value > listToCheck[index + 1]:
            return False
    return True

def swap_elements(listToRearrange, indexOne, indexTwo):
    """
Swaps two elements of the given list at indexOne and indexTwo.
    """
    x = listToRearrange[indexOne]
    y = listToRearrange[indexTwo]
    listToRearrange[indexOne] = y
    listToRearrange[indexTwo] = x
    return listToRearrange

def bubble_sort(listToSort):
    """
Pretty standard bubble sort. Pass in a list to have it work its magic.\n
Appears to be stable.
    """
    while is_sorted(listToSort) == False:
        for index,value in enumerate(listToSort):
            if index < len(listToSort) - 1:
                if value > listToSort[index + 1]:
                    swap_elements(listToSort, index, index + 1)

def bogo_sort(listToSort):
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
