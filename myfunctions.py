def negative(x):
    """
    >>> negative(5)
    -5
    >>> negative(-5)
    5
    """

    return -x

def filter_and(data, filters):
    """
    >>> data = [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]
    >>> filter_and(data, {'key1': 'apple', 'key2': 'tomato'})
    [{'key1': 'apple', 'key2': 'tomato'}]
    """
    new_list = []
    for row in data:
        match = True
        for key, value in filters.items():
            if row.get(key) != value:
                match = False
                break
        if match:
            new_list.append(row)
    return new_list

def filter_or(data, filters):
    """
    >>> data = [{'key1': 'apple', 'key2': 'tomato', 'key3': 'banana'}, {'key1': 'pear', 'key2': 'tomato', 'key3': 'banana'}, {'key1': 'orange', 'key2': 'potato', 'key3': 'banana'}]
    >>> filter_or(data, {'key1': 'apple', 'key2': 'potato'})
    [{'key1': 'apple', 'key2': 'tomato', 'key3': 'banana'}, {'key1': 'orange', 'key2': 'potato', 'key3': 'banana'}]
    """
    new_list = []
    if not filters:
        return data
    
    for row in data:
        for key, value in filters.items():
            if row.get(key) == value:
                new_list.append(row)
                break
    return new_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()