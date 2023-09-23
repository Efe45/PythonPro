import random

def gen_pass(pass_len):

    elements ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_len):
        password += random.choice(elements)

    return password
            