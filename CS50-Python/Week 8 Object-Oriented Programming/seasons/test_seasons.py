from seasons import get_birthdate, get_minutes_alive
from datetime import date
import pytest


def test_invalid_birthdate(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2002/07/07")
    with pytest.raises(SystemExit) as e:
        get_birthdate()

    assert e.type == SystemExit
    assert e.value.code == "Invalid date"


def test_birthdate(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2002-07-07")
    assert get_birthdate() == date.fromisoformat("2002-07-07")