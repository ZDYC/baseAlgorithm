def bubble(nlist,direction=True):
    """
    bubble sort
    when direction is True,min to max,
    is False, max to min
    """
    for i in range(0,len(nlist)-1):
        for j in range(0,len(nlist)-i-1):
            if direction:
                if(nlist[j] > nlist[j+1]):
                    nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
            else:
                if(nlist[j] < nlist[j+1]):
                    nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
    return nlist


print(bubble([2,3,45,1]))