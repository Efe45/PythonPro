import random
karakterler ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input("Kaç karakterlik şifre istersiniz"))

for i in range(x):
    a = random.choice(karakterler)
    print(a, end="")