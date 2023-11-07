import types


def flat_generator(list_of_lists):
    counter = -1
    while counter < len(list_of_lists)-1:
        counter += 1
        current_list = list_of_lists[counter]
        for el in current_list:
            yield el


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]]


def test_2():

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


results_list = []

if __name__ == '__main__':
    test_2()
    for item in flat_generator(list_of_lists_1):
        results_list.append(item)
    print(results_list)
    