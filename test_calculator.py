import pytest
from calculator import division, multiplicacion, resta, suma


def test_suma():
    assert suma(4, 6) == 10
    assert suma(-1, 1) == 0


def test_resta():
    assert resta(10, 5) == 5


def test_multiplicacion():
    assert multiplicacion(4, 5) == 20


def test_division_correcta():
    assert division(10, 2) == 5
    assert division(9, 3) == 3


def test_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero."):
        division(10, 0)