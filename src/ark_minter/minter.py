import secrets

BETANUMERIC = "0123456789bcdfghjkmnpqrstvwxz"


def noid_check_digit(noid: str) -> str:
    """Calculate the check digit for an ARK.

    See: https://metacpan.org/dist/Noid/view/noid#NOID-CHECK-DIGIT-ALGORITHM
    """
    total = 0
    for pos, char in enumerate(noid, start=1):
        score = BETANUMERIC.find(char)
        if score > 0:
            total += pos * score
    remainder = total % 29  # 29 == len(BETANUMERIC)
    return BETANUMERIC[remainder]  # IndexError may be long ARK


def generate_noid(length: int) -> str:
    return "".join(secrets.choice(BETANUMERIC) for _ in range(length))


def mint_ark(naan: int, shoulder: str) -> str:
    ark_prefix = f"{naan}{shoulder}"

    # generate assigned name by appending the base ark with the noid check digit
    noid = generate_noid(7)
    base_ark_string = f"{ark_prefix}{noid}"
    check_digit = noid_check_digit(base_ark_string)

    ark_string = f"ark:{naan}/{shoulder}{noid}{check_digit}"

    return ark_string
