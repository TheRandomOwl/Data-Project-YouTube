from myfunctions import *

def test_negative():
    import random
    a = random.randint(1, 100)
    assert negative(a) == -a
    assert negative(-a) == a
    assert negative(0) == 0

def test_filter_and():
    data = [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]
    filters = {'key1': 'apple', 'key2': 'tomato'}
    assert filter_and(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}]

    filters = {'key1': 'pear', 'key2': 'tomato'}
    assert filter_and(data, filters) == [{'key1': 'pear', 'key2': 'tomato'}]

    filters = {'key1': 'apple', 'key2': 'potato'}
    assert filter_and(data, filters) == [{'key1': 'apple', 'key2': 'potato'}]

    filters = {'key1': 'banana', 'key2': 'tomato'}
    assert filter_and(data, filters) == []

    filters = {'key1': 'apple'}
    assert filter_and(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]

    filters = {'key2': 'tomato'}
    assert filter_and(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}]

    filters = {}
    assert filter_and(data, filters) == data

def test_filter_or():
    data = [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]
    
    filters = {'key1': 'apple'}
    assert filter_or(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]

    filters = {'key2': 'tomato'}
    assert filter_or(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}]

    filters = {'key1': 'banana'}
    assert filter_or(data, filters) == []

    filters = {}
    assert filter_or(data, filters) == data

if __name__ == '__main__':
    test_filter_or()
    test_negative()
    test_filter_and()