import re

from ..minter import mint_ark


def test_mint_ark():
    naan = 12345
    shoulder = "gg"
    ark_string = mint_ark(naan=naan, shoulder=shoulder)

    print(ark_string)

    # check if assigned name is 8 digit
    # check if assigned name only contains numerical and alphabetical characters (except vowels)
    assert re.match(r"^12345gg[0-9b-df-hj-np-tv-z]{8}$", ark_string)
