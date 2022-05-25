from ab_check import ab_check

def test_1():
    assert ab_check('lane borrowed') == True

def test_2():
    assert ab_check('xxbzzzax') == True

def test_3():
    assert ab_check("lane _borrowed") == False

def test_4():
    assert ab_check('aab') == False

def test_5():
    assert ab_check('') == False