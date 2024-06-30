def is_sorted(listToCheck):
    for index,value in enumerate(listToCheck):
        if index + 1 < len(listToCheck) - 1 and value > listToCheck[index + 1]:
            return False
        else:
            continue
    return True

def swap_elements(listToRearrange, indexOne, indexTwo):
    x = listToRearrange[indexOne]
    y = listToRearrange[indexTwo]
    listToRearrange[indexOne] = y
    listToRearrange[indexTwo] = x
    return listToRearrange

def bubble_sort(listToSort):
    while is_sorted(listToSort) == False:
        for index,value in enumerate(listToSort):
            if index < len(listToSort) - 1:
                if value > listToSort[index + 1]:
                    swap_elements(listToSort, index, index + 1)
