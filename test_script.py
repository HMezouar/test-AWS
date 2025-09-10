import pytest
from script import get_joke

def test_get_joke_returns_tuple():
    setup, punchline = get_joke()
    # Vérifie que la fonction retourne un tuple avec deux éléments
    assert isinstance(setup, str)
    assert isinstance(punchline, str)
    assert len(setup) > 0
    assert len(punchline) > 0