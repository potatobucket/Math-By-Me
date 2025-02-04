"""
Various and sundry search algorithms.
"""

def binary_search(query: int | float | str, searchableList: list, queryIndex: int | None = None):
    """
Performs a binary search for the given query in the given iterable searchableList.
    """
    searchableList.sort() #-- eventually I'll create a more beefy sort algorithm and I can use that instead of sorted()
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
