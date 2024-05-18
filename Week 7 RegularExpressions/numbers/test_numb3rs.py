from numb3rs import validate

def test_greater_than_255():
    assert validate("256.10.20.30") == False
    assert validate("40.0.780.20") == False

def test_negatives():
    assert validate("150.-10.20.30") == False
    assert validate("-45.10.20.30") == False
    assert validate("25.10.20.-30") == False

def test_correct():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True