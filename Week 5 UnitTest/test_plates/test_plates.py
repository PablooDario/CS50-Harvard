from plates import is_valid

def test_len():
    assert is_valid("a") == False
    assert is_valid("abc1234") == False
    assert is_valid("abc") == True

def test_digits():
    assert is_valid("50") == False
    assert is_valid("cs") == True

def test_special_char():
    assert is_valid("cs..50") == False
    assert is_valid("cs50") == True

def test_valid_digits():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50CS") == False