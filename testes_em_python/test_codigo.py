import pytest
from codigo import is_even, divide


def test_is_even_if_number_is_even_returns_true():
    assert is_even(2) is True


def test_divide_thrwos_exception_when_dividing_by_zero():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(2, 0)
