import pytest
from pypass import clean_input

def test_clean():
    assert clean_input('bob') == 'bob'
    assert clean_input('Mary-Jane') == 'maryjane'
    assert clean_input('#$%tsitsi&') == 'tsitsi'
    assert clean_input(' sarah ') == 'sarah'
    assert clean_input('JOHN') == 'john'
