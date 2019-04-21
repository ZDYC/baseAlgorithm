def bubble(collections,direction=True):
    """
    bubble sort
    when direction is True,min to max,
    is False, max to min
    Examples:
    >>> bubble([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bubble([0, 5, 3, 2, 2], direction=False)
    [5, 3, 2, 2, 0]

    """
    for i in range(0,len(collections)-1):
        for j in range(0,len(collections)-i-1):
            if direction:
                if(collections[j] > collections[j+1]):
                    collections[j], collections[j+1] = collections[j+1], collections[j]
            else:
                if(collections[j] < collections[j+1]):
                    collections[j], collections[j+1] = collections[j+1], collections[j]
    return collections


if __name__ == '__main__':
    print(bubble([2,3,45,1], direction=False))
