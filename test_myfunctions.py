from myfunctions import *

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
    data = [{'key1': 'apple', 'key2': 'tomato', 'key3': 'banana'}, 
            {'key1': 'pear', 'key2': 'tomato', 'key3': 'orange'}, 
            {'key1': 'orange', 'key2': 'potato', 'key3': 'carrot'}
            ]
    
    filters = {'key1': 'orange', 'key3': 'banana'}
    assert filter_or(data, filters) == [{'key1': 'apple', 'key2': 'tomato', 'key3': 'banana'}, {'key1': 'orange', 'key2': 'potato', 'key3': 'carrot'}]

    filters = {'key1': 'apple', 'key2': 'cherry'}
    assert filter_or(data, filters) == [{'key1': 'apple', 'key2': 'tomato', 'key3': 'banana'}]

    filters = {}
    assert filter_or(data, filters) == data

def test_avg_val():
    data = [{'key1': '1', 'key2': '2'}, {'key1': '3', 'key2': '4'}, {'key1': '5', 'key2': '6'}, {'key1': 'invalid entry', 'key2': '4'}]
    assert avg_val(data, 'key1') == 3
    assert avg_val(data, 'key2') == 4

    data = [{'key1': 1, 'key2': 2}, {'key1': 3, 'key2': 4}, {'key1': 5}]
    assert avg_val(data, 'key1') == 3
    assert avg_val(data, 'key2') == 3

    data = [{'key1': 1}, {'key1': 3}, {'key1': 5}]
    assert avg_val(data, 'key1') == 3

    data = []
    assert avg_val(data, 'key1') == 0

    data = [{'key1': 1, 'key2': 2}, {'key1': 3, 'key2': 4}, {'key1': 5, 'key2': 6}]
    assert avg_val(data, 'key3') == 0

def test_total_amount():
    data = [{'key1': '1', 'key2': '2'}, {'key1': '3', 'key2': '4'}, {'key1': '5', 'key2': '6'}, {'key1': 'invalid entry', 'key2': '4'}]
    assert total_amount(data, 'key1') == 9
    assert total_amount(data, 'key2') == 16

    data = [{'key1': 1}, {'key1': 3}, {'key1': 5}]
    assert total_amount(data, 'key1') == 9

    data = []
    assert total_amount(data, 'key1') == 0

    data = [{'key1': 1, 'key2': 2}, {'key1': 3, 'key2': 4}, {'key1': 5, 'key2': 6}]
    assert total_amount(data, 'key3') == 0

if __name__ == '__main__':
    test_filter_or()
    test_filter_and()
    test_avg_val()