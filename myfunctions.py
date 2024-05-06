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

def entry_max(data, key):
    """
    Find the entry with the maximum value for the given key in a list of dictionaries.

    Args:
        data (list): A list of dictionaries.
        key (str): The key to compare the values.

    Returns:
        dict: The dictionary entry with the maximum value for the given key.
              If the list is empty or the key does not exist in any of the dictionaries, an empty dictionary is returned.

    Examples:
        >>> data = [{'key1': 1, 'key2': 2}, {'key1': 3, 'key2': 4}, {'key1': 5, 'key2': 6}, {'key1': 'invalid entry', 'key2': 4}]
        >>> entry_max(data, 'key1')
        {'key1': 5, 'key2': 6}
        >>> entry_max(data, 'nonexistent key')
        {}
        >>> entry_max([], 'key2')
        {}
    """
    if data == []:
        return {}
    max_entry = data[0]
    for entry in data:
        try:
            if entry[key] > max_entry[key]:
                max_entry = entry
        except TypeError:
            # skip invalid entries
            pass
        except KeyError:
            # return empty dictionary if key does not exist
            return {}
    return max_entry

if __name__ == '__main__':
    import doctest
    doctest.testmod()