from bfmmr import sum_of_values
def test_sum_of_values():
    values = [10, 20, 30]
    keys = [1, 0, 1]
    assert sum_of_values(values, keys) == 40

    values = [5, 15, 25]
    keys = [0, 1, 0]
    assert sum_of_values(values, keys) == 15

    values = [2, 4, 6]
    keys = [1, 1, 1]
    assert sum_of_values(values, keys) == 12

    values = [3, 6, 9]
    keys = [0, 0, 0]
    assert sum_of_values(values, keys) == 0