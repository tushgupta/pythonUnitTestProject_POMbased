import string
from random import random

import names

from pageObjects.RegistrationPage import RegistrationPage as rp


class registration_functions:
    def firstname(self):
        f_name = names.get_first_name()
        rp.setfname(f_name)

    def lastname(self):
        l_name = names.get_last_name()
        rp.setlname(l_name)

    def phonenumber(self):
        ph_no = 0
        for i in range(14):
            ph_no = i
        rp.setmobilenumber(ph_no)

    def email(self):
        return "test@yopmail.com"
            #.join(random.choice(string.ascii_letters) for x in range(y))

    def passKey(self, length=8):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
