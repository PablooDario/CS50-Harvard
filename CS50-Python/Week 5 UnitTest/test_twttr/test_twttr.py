from twttr import shorten

def test_no_vocals():
    assert shorten("250") == "250"

def test_vocals():
    assert shorten("Hello World") =="Hll Wrld"

def test_upper_vocals():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_punctuation():
    assert shorten("...") == "..."