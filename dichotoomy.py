def dichotomy(collections,item):
    low = 0
    high = len(collections)
    while low <= high:
        mid = (high + low) // 2
        if collections[mid] == item:
            return mid
        elif collections[mid] > item:
            pass
        else:
            pass

if __name__ == '__main__':
    dichotomy([1,2,3,4],3)