####################################
# This program randomly generates  #
#       a secure password          #
####################################


import string
import random

def passwordgen():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size=8
    return ''.join(random.choice(chars) for x in
                   range(size,20))

print(passwordgen())
