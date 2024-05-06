from myfunctions import *

def test_negative():
    import random
    a = random.randint(1, 100)
    assert negative(a) == -a
    assert negative(-a) == a
    assert negative(0) == 0

def test_filter_data():
    data = [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]
    filters = {'key1': 'apple', 'key2': 'tomato'}
    assert filter_data(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}]

    filters = {'key1': 'pear', 'key2': 'tomato'}
    assert filter_data(data, filters) == [{'key1': 'pear', 'key2': 'tomato'}]

    filters = {'key1': 'apple', 'key2': 'potato'}
    assert filter_data(data, filters) == [{'key1': 'apple', 'key2': 'potato'}]

    filters = {'key1': 'banana', 'key2': 'tomato'}
    assert filter_data(data, filters) == []

    filters = {'key1': 'apple'}
    assert filter_data(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'apple', 'key2': 'potato'}]

    filters = {'key2': 'tomato'}
    assert filter_data(data, filters) == [{'key1': 'apple', 'key2': 'tomato'}, {'key1': 'pear', 'key2': 'tomato'}]

    filters = {}
    assert filter_data(data, filters) == data

if __name__ == '__main__':
    test_negative()
    test_filter_data()