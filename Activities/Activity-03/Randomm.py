import random as rd

def generate(n, min, max):

    return [rd.randint(min, max) for i in range(n)]