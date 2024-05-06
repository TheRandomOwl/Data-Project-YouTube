def negative(x):
    """
    >>> negative(5)
    -5
    >>> negative(-5)
    5
    """

    return -x

def filter_data(data, filters):
    """
    >>> data = [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]
    >>> filter_data(data, {'key1': 'apple', 'key2': 'tomato'})
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()