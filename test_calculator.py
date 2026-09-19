from calculator import multiplicacion, resta


def test_resta():
    assert resta(10, 5) == 5


def test_multiplicacion():
    assert multiplicacion(4, 5) == 20
