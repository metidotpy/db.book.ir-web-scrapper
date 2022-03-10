import string
import secrets
import random

class CreateRandomString():
    def make_random_string(self):
        text = ''.join(secrets.choice(string.ascii_letters+string.digits) for x in range(10))
        return text

make = CreateRandomString()