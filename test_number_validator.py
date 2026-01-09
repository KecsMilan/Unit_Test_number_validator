"""
TESZTELENDŐ FELADAT - NumberValidator osztály unit tesztek

A feladat: Írj unit teszteket a NumberValidator osztály metódusaihoz!
Használd a különböző assert típusokat!
"""

import pytest
from number_validator import NumberValidator


# ============================================================================
# FELADAT: Írd meg az alábbi teszteket!
# ============================================================================

def test_is_even_equal():
    """1.1 Assert equal - páros szám ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_even(2)
    assert result == True


def test_is_even_not_equal():
    """1.2 Assert not equal - páratlan szám ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_even(1)
    assert result != True


def test_is_even_with_zero():
    """1.3 Speciális eset - nulla kezelése"""
    numv = NumberValidator()
    result = numv.is_even(0)
    assert result == True


def test_is_positive_greater_than():
    """2.1 Assert > - pozitív szám ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_positive(10)
    assert result == True


def test_is_positive_with_negative():
    """2.2 Negatív szám ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_positive(10)
    result1 = numv.is_positive(-10)
    assert result == True
    assert result1 == False


def test_is_in_range_less_than():
    """3.1 Assert <, <= - tartományon belüli ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_in_range(10, 0, 11)
    assert result == True


def test_is_in_range_out_of_range():
    """3.2 Assert <, <= - tartományon kívüli ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_in_range(30, 11, 12)
    assert result != True


def test_get_absolute_value_isinstance():
    """4. Assert isinstance - típus ellenőrzés"""
    numv = NumberValidator()
    result = numv.get_absolute_value(-5)
    assert isinstance(result, int) == True
    assert isinstance(result, str) == False


def test_is_divisible_by_true_false():
    """5. Assert True/False - oszthatóság ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_divisible_by(6, 2)
    assert result == True
    result = numv.is_divisible_by(6, 4)
    assert result == False


def test_square_none():
    """6. Assert None - None ellenőrzés"""
    numv = NumberValidator()
    result = numv.square(None)
    assert result != None
    assert result == 0


def test_is_prime_multiple_asserts():
    """7. Több assert egy tesztben - prímszám ellenőrzés"""
    numv = NumberValidator()
    result = numv.is_prime(7)
    assert result == True
    assert isinstance(result, bool) == True
    assert result != False 

