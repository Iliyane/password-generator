#!/usr/bin/python3
# Author: Iliyana Kamenova

import random
import string

# Für ein sicheres Password verwende ich hier random.SystemRandom() Methode und passe genau an, von wievielen Charakters (upper=4, lower=4, digits=4, special=3) den Password generiert werden soll.

""" Generiert einen String von 15 Zeichen
    mit 4 Grossbuchstaben, 4 Kleinbuchstaben, 4 Zahlen und 3 Special characters"""

def make_special_password(upper_chars = 4, lower_chars = 4, digit_chars = 4, special_chars = 3):
    # Generiert einen String von 15 Zeichen
    # mit 4 Grossbuchstaben, 4 Kleinbuchstaben, 4 Zahlen und 3 Special characters

    str_upper, str_lower, str_digits, str_special = '', '', '', ''

    for i in range(upper_chars):
        str_upper += random.SystemRandom().choice(string.ascii_uppercase)

    for i in range(lower_chars):
        str_upper += random.SystemRandom().choice(string.ascii_lowercase)

    for i in range(digit_chars):
        str_upper += random.SystemRandom().choice(string.digits)

    for i in range(special_chars):
        str_upper += random.SystemRandom().choice(string.punctuation)

    random_password = str_upper + str_lower + str_digits + str_special
    random_password = ''.join(random.sample(random_password, len(random_password)))
    return random_password


print('Ihr neues Password ist:', make_special_password())

# Diese Funktion kann man auch ausrufen, indem man die Anzahl von Zeichen immer wieder ändern kann.
# Zum Beispiel, hier möchte ich, dass es 3 Grossbuchstaben, 5 Kleinbuchstaben, 5 Zahlen und 2 Special Characters.

print (make_special_password(3,5,5,2))
