from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], -1, "test") == "test"


def test_slice_normal():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_slice_empty():
    assert arrs.my_slice([]) == []


def test_slice_negative_index():
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]


def test_slice_negative_end():
    assert arrs.my_slice([1, 2, 3], -4, -2) == [1]
