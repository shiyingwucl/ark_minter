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


def mint_ark(naan: int, shoulder: str, noid_length: int = 7) -> str:
    ark_prefix = f"{naan}{shoulder}"

    # generate assigned name by appending the base ark with the noid check digit
    noid = generate_noid(noid_length)
    base_ark_string = f"{ark_prefix}{noid}"
    check_digit = noid_check_digit(base_ark_string)

    ark_string = f"ark:{naan}/{shoulder}{noid}{check_digit}"

    return ark_string


def mint_ark_by_id(
    naan: int,
    shoulder: str,
    obj_id: int,
    noid_length: int = 7,
) -> str:
    ark_prefix = f"{naan}{shoulder}"

    if obj_id < noid_length:
        return

    # generate assigned name by appending the base ark with the noid check digit
    assigned_name = f"{(noid_length - len(obj_id)) * '0'}{obj_id}"
    base_ark_string = f"{ark_prefix}{assigned_name}"
    check_digit = noid_check_digit(base_ark_string)

    ark_string = f"ark:{naan}/{shoulder}{assigned_name}{check_digit}"

    return ark_string


"""Django model intergration idea

wrap function requiring parameters to use as a default value when a Disc is created

def default_ark():
    return mint_ark(naan=12345, shoulder="gg",...)

class DiscSide(models.Model):
    ......
    ark = models.CharField(default = mint_ark)
"""

"""Django collison check idea

- ark field is set to unique
- try mint_ark function, if generated noid is a duplicate, it will throw an UNIQUE constraint failed error (IntegrityError)
- catch error, repeat the action until it succeeds.

"""

"""Make the ark field immutable in Django

class DiscSide(models.Model):
    .......
    def save(self, *args, **kwargs):
        if self.ark:
            raise ValidationError("you may not edit an existing %s" % self._meta.model_name)
        super(ModelName, self).save(*args, **kwargs)
"""
