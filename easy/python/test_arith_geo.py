from arith_geo import arithGeo


def test_1():
    assert arithGeo([2, 4, 6, 8]) == "Arithmetic"
    assert arithGeo([3, 4, 5, 6]) == "Arithmetic"

def test_2():
    assert arithGeo([2, 6, 18, 54]) == "Geometric"
    assert arithGeo([1, 6, 36, 216, 1296]) == "Geometric"

def test_3():
    assert arithGeo([1, 2, 3, 5]) == -1

def test_4():
    assert arithGeo([1]) == -1

def test_5():
    assert arithGeo([]) == -1