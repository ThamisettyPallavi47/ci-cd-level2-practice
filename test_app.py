import pytest
from app import calculate_average


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90.0


def test_calculate_average_single_mark():
    assert calculate_average([75]) == 75.0


def test_calculate_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
