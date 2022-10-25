import numpy as np


# define a method that take a list input
# then checks if it is a cycle or not
# returns: true if list is perfect cycle; otherwise return false
# Time complexity O(n); space complexity O(n)
def isListCycle(list_):
    # before validating if list is perfect cycle, check the following conditions:
    # 1. list is empty
    # 2. list has one elemnt and not perfect cycle
    # 3. list has one elemnt and it is perfect cycle
    # 4. list doesn't contains 0 we can't return to the first element
    # 5. list contains duplicate entries
    if not list_:
        return False
    elif len(list_) == 1 and list_[0] != 0:
        return False
    elif len(list_) == 1 and list_[0] == 0:
        return True
    elif 0 not in list_:
        print("List doesn't contain 0; can't have perfect cycle")
        return False
    elif len(list_) > len(np.unique(list_)):
        print("List contains duplicate numbers; can't have perfect cycle")
        return False
    elif not validateList(list_):
        print("List is invalid")
        return False

    # use the visited list to keep track of the indexes we visited
    visited = [0] * len(list_)


    try:
        iteration = 0
        i=0

        while iteration < len(list_):
            # item at index; start from begining of the list
            item = list_[i]
            #print(f"iteration: {iteration}")
            #print(f"item: {item}")
            
            # if last index we visit doesn't take us back to the begining of list
            if (item) and (iteration == len(list_)-1) and (item != 0):
                return False
            
            # if index is out of bound
            if item >= len(list_):
                return False

            # if we visit an item twice then we will have an infinte loop
            if(visited[item] == 1):
                return False

            # we visited a new item; update the indicecs and loop again
            visited[item] = 1
            i=item
            iteration += 1

    except IndexError as e:
        print(e)
        return False

    # list is perfect cycle
    return True



# verify if list is cycle with another approach; using sorting
# Time complexity for quicksort O(n*logn); the first method isListCycle(list_) is faster
def isCycleSort(list_):
    # 1. list is empty
    # 2. list has one elemnt and not perfect cycle
    # 3. list has one elemnt and it is perfect cycle
    # 4. list is not valid
    if not list_:
        return False
    elif len(list_) == 1 and list_[0] != 0:
        return False
    elif len(list_) == 1 and list_[0] == 0:
        return True
    elif not validateList(list_):
        return False

    list_ = np.sort(list_)

    # loop through the sorted list and check if we visit all indicies
    for i in range(0, len(list_)):
        if i != list_[i]:
            return False

    return True


# validate that list has integer indicies only
def validateList(list_):
    return all([isinstance(item, int) for item in list_])
