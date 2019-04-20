def dichotomy(lists,item):
    low = 0
    high = len(lists)
    while low <= high:
        guess = high // 2
        if lists[guess] == item:
            return guess

if __name__ == '__main__':
    dichotomy([1,2,3,4],3)