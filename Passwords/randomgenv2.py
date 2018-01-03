####################################
# Randomly generate                #
# a set number of passwords        #
# depending on the loop            #
####################################


import string
import random

def passwordgen():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size=8
    return ''.join(random.choice(chars) for x in
                   range(size,20))

n=0
while n<50:
    print(passwordgen())
    n=n+1
