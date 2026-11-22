from calc import suma, resta, multiplica


def test_suma():
    assert suma(2, 3) == 5


def test_resta():
    assert resta(5, 3) == 2


def test_multiplica():
    assert multiplica(4, 3) == 12
    assert multiplica(-2, 3) == -6
    assert multiplica(5, 0) == 0
