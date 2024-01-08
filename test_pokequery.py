# File to test pokemon calls

import pytest 
from data_request.poke_query import poke_grabber as pg

# Test for pokemon calls for dex

def test_name():
    # Test for pokename
    assert pg("mew")[1] == "mew"

def test_height():
    # Test for poketype
    result = pg("mew")
    assert type(result[2]) == float

def test_type():
    # Test for pokeheight
    assert pg("mew")[3] == "psychic" 




