# simulation for Problem 6
import random

N = 100000
total_counter = 0
reach_3_0_times = 0
for i in range(N):
    x = 0
    y = 0
    counter = 0
    while True:
        if abs(x) + abs(y) == 3:
            total_counter += counter
            if x == 3 and y == 0:
                reach_3_0_times += 1
            break
        a = random.randint(0, 3)
        if a == 0:
            x += 1
        elif a == 1:
            y += 1
        elif a == 2:
            x -= 1
        else:
            y -= 1
        counter += 1
print('expectation of E[T]')
print('empirical value', total_counter / N)
print('theoretical value', 39 / 7)

print('first hit (3, 0)')
print('empirical value', reach_3_0_times / N)
print('theoretical value', 1 / 28)
