import numpy as np
import random
p = (3 - np.sqrt(5)) / 2

N = 1000
cnt = 0
for _ in range(N):
    x_n = 1
    x_n_1 = 2    
    for _ in range(N):
        a = random.randint(0, 1)
        if a == 0:
            tmp = x_n_1
            x_n_1 = x_n + x_n_1
            x_n = tmp
        else:
            tmp = x_n_1
            x_n_1 = abs(x_n - x_n_1)
            x_n = tmp
        if x_n == 1 and x_n_1 == 1:
            cnt += 1
            break
print(cnt / N, p)
