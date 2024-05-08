def filter_and(data, filters):
    """
    Filter the given data based on multiple filter conditions.

    Args:
        data (list): A list of dictionaries representing the data to be filtered.
        filters (dict): A dictionary containing the filter conditions.

    Returns:
        list: A new list containing the filtered data.

    Examples:
        >>> data = [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'pear', 'b': 'tomato', 'c': 'banana'}, {'a': 'orange', 'b': 'potato', 'c': 'banana'}]
        >>> filter_and(data, {'a': 'apple', 'b': 'tomato'})
        [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}]
        >>> filter_and(data, {'a': ('apple', 'pear'), 'b': 'tomato'})
        [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'pear', 'b': 'tomato', 'c': 'banana'}]
    """
    new_list = []
    for row in data:
        match = True
        for key, value in filters.items():
            if isinstance(value, tuple):
                if row.get(key) not in value:
                    match = False
                    break
            else:
                if row.get(key) != value:
                    match = False
                    break
        if match:
            new_list.append(row)
    return new_list

def filter_or(data, filters):
    """
    Filter a list of dictionaries based on multiple OR conditions.

    Args:
        data (list): A list of dictionaries representing the data.
        filters (dict): A dictionary containing the filter conditions.

    Returns:
        list: A new list of dictionaries that match any of the filter conditions.

    Examples:
        >>> data = [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'pear', 'b': 'tomato', 'c': 'banana'}, {'a': 'orange', 'b': 'potato', 'c': 'banana'}]
        >>> filter_or(data, {'a': 'apple', 'b': 'potato'})
        [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'orange', 'b': 'potato', 'c': 'banana'}]
        >>> filter_or(data, {'a': ('apple', 'orange')})
        [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'orange', 'b': 'potato', 'c': 'banana'}]
    """
    new_list = []
    if not filters:
        return data
    
    for row in data:
        for key, value in filters.items():
            if isinstance(value, tuple):
                if row.get(key) in value:
                    new_list.append(row)
                    break
            else:
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
        >>> data = [{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}, {'a': '5', 'b': '6'}, {'a': 'invalid entry', 'b': '4'}]
        >>> entry_max(data, 'a')
        {'a': '5', 'b': '6'}
        >>> entry_max(data, 'nonexistent key')
        {}
        >>> entry_max([], 'b')
        {}
    """
    if data == []:
        return {}
    max_entry = data[0]
    for entry in data:
        try:
            if int(entry[key]) > int(max_entry[key]):
                max_entry = entry
        except ValueError:
            # skip invalid non int entries
            pass
        except KeyError:
            # return empty dictionary if key does not exist
            return {}
    return max_entry

def avg_val(data, key):
    """
    Calculate the average value of a key in a list of dictionaries.

    Args:
        data (list): A list of dictionaries.
        key (str): The key to calculate the average value.

    Returns:
        float: The average value of the key in the list of dictionaries.
               If the key does not exist in any of the dictionaries, 0 is returned.
               If the list is empty, 0 is returned.

    Examples:
        >>> data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
        >>> avg_val(data, 'a')
        3.0
        >>> avg_val(data, 'b')
        4.0
        >>> avg_val(data, 'nonexistent key')
        0
        >>> avg_val([], 'a')
        0
    """
    if data == []:
        return 0
    total = 0
    count = 0
    for entry in data:
        if key in entry:
            try:
                total += int(entry[key])
                count += 1
            except ValueError:
                # skip invalid non int entries
                pass
    if count == 0:
        return 0
    return total / count

def total_amount(data, key):
    """
    Calculate the total amount of a key in a list of dictionaries.

    Args:
        data (list): A list of dictionaries.
        key (str): The key to calculate the total amount.

    Returns:
        int: The total amount of the key in the list of dictionaries.
             If the key does not exist in any of the dictionaries, 0 is returned.

    Examples:
        >>> data = [{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}, {'a': '5', 'b': '6'}, {'a': 'invalid entry', 'b': '4'}]
        >>> total_amount(data, 'a')
        9
        >>> total_amount(data, 'b')
        16
        >>> total_amount(data, 'nonexistent key')
        0
    """
    total = 0
    for entry in data:
        if key in entry:
            try:
                total += int(entry[key])
            except ValueError:
                # skip invalid non int entries
                pass
    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()