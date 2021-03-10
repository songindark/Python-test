import random


def random_num():
    code = ''
    for i in range(4):
        ran1 = random.randint(0, 9)
        ran2 = chr(random.randint(65, 90))
        add = random.choice([ran1, ran2])
        code = ''.join([code, str(add)])
    return code


rand_n = random_num()
print(rand_n)
