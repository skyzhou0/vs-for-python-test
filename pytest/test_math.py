def add(x, y):
    return x + y 


def subtract(x, y):
    return x - y 


def inc(x):
    return x + 1


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(4, 2) == 2

def test_inc():
    assert inc(2) == 3
