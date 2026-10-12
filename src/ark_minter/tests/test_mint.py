import re

from ..minter import mint_ark, mint_ark_by_id


def test_mint_ark():
    naan = 12345
    shoulder = "gg"
    ark_string = mint_ark(naan=naan, shoulder=shoulder)

    print(ark_string)

    # check if assigned name is 8 digit
    # check if assigned name only contains numerical and alphabetical characters (except vowels)
    assert re.match(r"^ark:12345/gg[0-9b-df-hj-np-tv-z]{8}$", ark_string)


def test_mint_ark_by_id():
    naan = 12345
    shoulder = "gg"
    test_obj_id = 123
    ark_string = mint_ark_by_id(naan=naan, shoulder=shoulder, obj_id=test_obj_id)

    print(ark_string)

    # check if assigned name is 8 digit
    # check if assigned name only contains numerical and alphabetical characters (except vowels)
    assert re.match(r"^ark:12345/gg[0-9b-df-hj-np-tv-z]{8}$", ark_string)
