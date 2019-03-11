import pytest
from pypass import clean_input, reverser

def test_clean():
    assert clean_input('bob') == 'bob'
    assert clean_input('Mary-Jane') == 'maryjane'
    assert clean_input('#$%tsitsi&') == 'tsitsi'
    assert clean_input(' sarah ') == 'sarah'
    assert clean_input('JOHN') == 'john'
    assert clean_input('james%') != 'james%'
    assert clean_input('Blessing') != 'Blessing'

def test_reverser():
    assert reverser('flora') == 'arolf'
    assert reverser('sarah') == 'haras'
    assert reverser('Liya') == 'ayiL'
    assert reverser('tsitsi') == 'istist'
    assert reverser('hannah') == 'hannah'
    assert reverser('MARY') == 'YRAM'
    assert reverser('john') != 'john'