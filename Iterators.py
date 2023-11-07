class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = []

    def __iter__(self):
        self.counter = -1
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.current_list):
            self.counter += 1
            if self.counter >= len(self.list_of_list):
                raise StopIteration

            self.current_list = self.list_of_list[self.counter]
            self.index = 0

        return self.current_list[self.index]


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


def test_1():

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


results_list = []

if __name__ == '__main__':
    test_1()
    for item in FlatIterator(list_of_lists_1):
        results_list.append(item)
    print(results_list)
