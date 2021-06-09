import random

N = 10000
q = 0.5
for i in range(N):
    a = random.randint(0, 1)
    if a == 0:
        q = q ** 2
    else:
        q = 2 * q - q ** 2
print(q)
