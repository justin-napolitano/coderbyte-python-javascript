from alphabet_soup import alphabetSoup

def test_1():
    assert alphabetSoup('hello') == "ehllo"

def test_2():
    assert alphabetSoup('abcd') == "abcd"

def test_3():
    assert alphabetSoup('helloHELLO') == "EHLLOehllo"

