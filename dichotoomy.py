def dichotomy(lists,item):
    """
    dichotomy finds the index of the target number or string
    """
    low = 0
    high = len(lists)
    while low <= high:
        mid = (low + high) // 2
        guess = lists[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    dichotomy([1,2,3,4],4)
    dichotomy("python",'o')