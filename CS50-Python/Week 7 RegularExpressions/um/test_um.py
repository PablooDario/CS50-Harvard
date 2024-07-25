from um import count
import pytest

def test_word_including_um():
    assert count("yummy") == 0
    assert count("yum") == 0
    assert count("ummy") == 0

def test_special_characters():
    assert count("...um...") == 1
    assert count("um?") == 1
    assert count("...um") == 1

def test_incase_sensitive():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("um") == 1

def test_phrase():
    assert count("Um, thanks for the album.") == 1