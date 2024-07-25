from working import convert
import pytest

def test_wrong_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:80 PM")

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("25:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 100:00 PM")

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

def test_no_minutes():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"

def test_correct_ones():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
