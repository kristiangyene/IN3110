#!/usr/bin/env python3
import pytest
from complex import Complex
from math import sqrt

error = "The result is wrong."

def test_add():
    """Test to make sure the __add__ function works.

    form:

        z1 + z2 = (a1 + a2) + (b1 + b2)i
        Where z=complex number, a=real, b=imaginary

    """
    complexNumber1 = Complex(2, 0)
    complexNumber2 = Complex(0, 1)
    assert (complexNumber1 + complexNumber2) == Complex(2, 1), error

    complexNumber1 = Complex(0, 0)
    complexNumber2 = Complex(1, 0)
    assert (complexNumber1 + complexNumber2) == Complex(1, 0), error

    complexNumber1 = Complex(-5, -1)
    complexNumber2 = Complex(4, 4)
    assert (complexNumber1 + complexNumber2) == Complex(-1, 3), error

    complexNumber1 = Complex(-1, 2)
    complexNumber2 = Complex(-1, 2)
    assert (complexNumber1 + complexNumber2) == Complex(-2, 4), error


def test_radd():
    """Test to make sure the __radd__ function works."""
    complexNumber = Complex(0, 3)
    assert (complexNumber + 3) == Complex(3, 3), error

    complexNumber = Complex(-7, -2)
    assert (complexNumber + 5) == Complex(-2, -2), error


def test_sub():
    """Test to make sure the __sub__ function works.

    form:

        z1 − z2 = (a1 − a2) + (b1 − b2)i
        Where z=complex number, a=real, b=imaginary

    """
    complexNumber1 = Complex(2, 0)
    complexNumber2 = Complex(0, 1)
    assert (complexNumber1 - complexNumber2) == Complex(2, -1), error

    complexNumber1 = Complex(0, 0)
    complexNumber2 = Complex(1, 0)
    assert (complexNumber1 - complexNumber2) == Complex(-1, 0), error

    complexNumber1 = Complex(-5, -1)
    complexNumber2 = Complex(5, 4)
    assert (complexNumber1 - complexNumber2) == Complex(-10, -5), error

    complexNumber1 = Complex(-1, 2)
    complexNumber2 = Complex(-1, 2)
    assert (complexNumber1 - complexNumber2) == Complex(0, 0), error


def test_rsub():
    """Test to make sure the __rsub__ function works."""
    complexNumber = Complex(2, 0)
    assert (complexNumber - 3) == Complex(-1, 0), error

    complexNumber = Complex(-4, -2)
    assert (complexNumber - 3) == Complex(-7, -2), error


def test_mul():
    """Test to make sure the __mul__ function works.

    form:
        z1 * z2 = (a1 * a2 − b1 * b2) + (a1 * b2 + a2 * b1)i
        Where z=complex number, a=real, b=imaginary


    """
    complexNumber1 = Complex(2, 0)
    complexNumber2 = Complex(0, 1)
    assert (complexNumber1 * complexNumber2) == Complex(0, 2), error

    complexNumber1 = Complex(0, 0)
    complexNumber2 = Complex(1, 0)
    assert (complexNumber1 * complexNumber2) == Complex(0, 0), error

    complexNumber1 = Complex(-3, -1)
    complexNumber2 = Complex(4, 4)
    assert (complexNumber1 * complexNumber2) == Complex(-8, -16), error
  
    complexNumber1 = Complex(-1, 2)
    complexNumber2 = Complex(-1, 2)
    assert (complexNumber1 * complexNumber2) == Complex(-3, -4), error


def test_rmul():
    """Test to make sure the __rmul__ function works."""
    complexNumber = Complex(2, 1)
    assert (complexNumber * 2) == Complex(4, 2), error

    complexNumber = Complex(-1, 4)
    assert (complexNumber * 4) == Complex(-4, 16), error


def test_conj():
    """Test to make sure the conjugate() function works.

    form:
        !z = a − bi
        Where z=complex number, a=real, b=imaginary

    """
    complexNumber = Complex(2, 0)
    assert complexNumber.conjugate() == Complex(2, 0), error

    complexNumber = Complex(4, 7)
    assert complexNumber.conjugate() == Complex(4, -7), error

    complexNumber = Complex(0, 8)
    assert complexNumber.conjugate() == Complex(0, -8), error

    complexNumber = Complex(-1, -3)
    assert complexNumber.conjugate() == Complex(-1, 3), error


def test_mod():
    """Test to make sure the modulus() function works.

    form:
        |z| = sqrt(a^2 + b^2)
        Where z=complex number, a=real, b=imaginary

    """
    complexNumber = Complex(2, 0)
    assert complexNumber.modulus() == 2, error

    complexNumber = Complex(4, 7)
    assert complexNumber.modulus() == sqrt(65), error

    complexNumber = Complex(3, 8)
    assert complexNumber.modulus() == sqrt(73), error

    complexNumber = Complex(-1, -3)
    assert complexNumber.modulus() == sqrt(10), error


def test_eq():
    """Test to make sure the __eq__ function works."""
    complexNumber = Complex(0, 1)
    assert complexNumber == Complex(0, 1), error

    complexNumber = Complex(4, 7)
    assert complexNumber == Complex(4, 7), error

    complexNumber = Complex(3, 0)
    assert complexNumber == Complex(3, 0), error

    complexNumber = Complex(2, 2)
    assert complexNumber == Complex(2, 2), error