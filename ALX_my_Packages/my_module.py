def top_n (items, n):
    """"Returns top n items in an array, in desc order
    
    Args:
        items (array): list or array-like object
        n (int): number of items to return
    
    Return:
        array: top n items in descending order

    Eg:
        >>> top_n([1,2,7,5,6], 2)
        [7,6]
    """
    for i in range(n):
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    
    top_n = items[-n:]

    return top_n[::-1]