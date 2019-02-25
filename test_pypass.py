import pytest
from pypass import clean_input, validate

def test_clean():
    assert clean_input('bob') == 'bob'
    assert clean_input('Mary-Jane') == 'maryjane'
    assert clean_input('#$%tsitsi&') == 'tsitsi'
    assert clean_input(' sarah ') == 'sarah'
    assert clean_input('JOHN') == 'john'
    assert clean_input('james%') != 'james%'
    assert clean_input('Blessing') != 'Blessing'

def test_vali():
    assert validate('2001-01-02') == True
    assert validate('09-02 2012') == False
    assert validate('12-25-1990') == False
    assert validate('2011-12-04') == True
    assert validate('09-2017-08') == False
    assert validate('2001-1-4') == False
