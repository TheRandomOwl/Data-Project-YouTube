from myfunctions import *

def test_filter_and():
    data = [{'a': 'apple', 'b': 'tomato'}, {'a': 'pear', 'b': 'tomato'}, {'a': 'apple', 'b': 'potato'}]
    filters = {'a': 'apple', 'b': 'tomato'}
    assert filter_and(data, filters) == [{'a': 'apple', 'b': 'tomato'}]

    filters = {'a': 'pear', 'b': 'tomato'}
    assert filter_and(data, filters) == [{'a': 'pear', 'b': 'tomato'}]

    filters = {'a': 'apple', 'b': 'potato'}
    assert filter_and(data, filters) == [{'a': 'apple', 'b': 'potato'}]

    filters = {'a': 'banana', 'b': 'tomato'}
    assert filter_and(data, filters) == []

    filters = {'a': 'apple'}
    assert filter_and(data, filters) == [{'a': 'apple', 'b': 'tomato'}, {'a': 'apple', 'b': 'potato'}]

    filters = {'b': 'tomato'}
    assert filter_and(data, filters) == [{'a': 'apple', 'b': 'tomato'}, {'a': 'pear', 'b': 'tomato'}]

    filters = {}
    assert filter_and(data, filters) == data

    filters = {'a': ('apple', 'pear'), 'b': 'potato'}
    assert filter_and(data, filters) == [{'a': 'apple', 'b': 'potato'}]

    filters = {'a': ('invalid', 'invalid'), 'b': 'tomato'}
    assert filter_and(data, filters) == []

def test_filter_or():
    data = [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, 
            {'a': 'pear', 'b': 'tomato', 'c': 'orange'}, 
            {'a': 'orange', 'b': 'potato', 'c': 'carrot'}
            ]
    
    filters = {'a': 'orange', 'c': 'banana'}
    assert filter_or(data, filters) == [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'orange', 'b': 'potato', 'c': 'carrot'}]

    filters = {'a': 'apple', 'b': 'cherry'}
    assert filter_or(data, filters) == [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}]

    filters = {}
    assert filter_or(data, filters) == data

    filters = {'a': ('apple', 'orange')}
    assert filter_or(data, filters) == [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'orange', 'b': 'potato', 'c': 'carrot'}]

    filters = {'a': ('apple', 'orange'), 'b': 'potato'}
    assert filter_or(data, filters) == [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'orange', 'b': 'potato', 'c': 'carrot'}]

    filters = {'a': ('invalid', 'invalid'), 'b': 'tomato'}
    assert filter_or(data, filters) == [{'a': 'apple', 'b': 'tomato', 'c': 'banana'}, {'a': 'pear', 'b': 'tomato', 'c': 'orange'}]

def test_avg_val():
    data = [{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}, {'a': '5', 'b': '6'}, {'a': 'invalid entry', 'b': '4'}]
    assert avg_val(data, 'a') == 3
    assert avg_val(data, 'b') == 4

    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5}]
    assert avg_val(data, 'a') == 3
    assert avg_val(data, 'b') == 3

    data = [{'a': 1}, {'a': 3}, {'a': 5}]
    assert avg_val(data, 'a') == 3

    data = []
    assert avg_val(data, 'a') == 0

    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
    assert avg_val(data, 'c') == 0

    avg_val([{'a': '2E+2'}, {'a': '5.5'}], 'a') == 102.75

def test_total_sum():
    data = [{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}, {'a': '5', 'b': '6'}, {'a': 'invalid entry', 'b': '4'}, {'a': '1E+0'}]
    assert total_sum(data, 'a') == 10
    assert total_sum(data, 'b') == 16

    data = [{'a': 1}, {'a': 3}, {'a': 5}]
    assert total_sum(data, 'a') == 9

    data = []
    assert total_sum(data, 'a') == 0

    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
    assert total_sum(data, 'c') == 0

if __name__ == '__main__':
    test_filter_or()
    test_filter_and()
    test_avg_val()
    test_total_sum()
