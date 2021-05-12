# simulation for Problem 6
import random
from math import sqrt

N = 100000
total_counter = 0
reach_3_0_times = 0
for i in range(N):
    x = 0
    y = 0
    counter = 0
    while True:
        if abs(y) >= 2 or x <= -2:
            total_counter += counter
            if x == -2 and y == 0:
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
print('theoretical value', -8+(8+5*sqrt(2))*sqrt(7-4*sqrt(2))+(5*sqrt(2)-8)*sqrt(7+4*sqrt(2)))

print('first hit (-2, 0)')
print('empirical value', reach_3_0_times / N)
print('theoretical value', 8-((2*sqrt(2)-1)*sqrt(7-4*sqrt(2)) + (2*sqrt(2)+1)*sqrt(7+4*sqrt(2)))/2)
