a = [0 for i in range(2021)]
a[1] = 1 / 6
a[2] = a[1] / 6 + 1 / 6
a[3] = a[2] / 6 + a[1] / 6 + 1 / 6
a[4] = a[3] / 6 + a[2] / 6 + a[1] / 6 + 1 / 6
a[5] = a[4] / 6 + a[3] / 6 + a[2] / 6 + a[1] / 6 + 1 / 6
a[6] = a[5] / 6 + a[4] / 6 + a[3] / 6 + a[2] / 6 + a[1] / 6 + 1 / 6
for i in range(7, 2021):
    a[i] = (a[i - 1] + a[i - 2] + a[i - 3] + a[i - 4] + a[i - 5] + a[i - 6]) / 6
print(a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[2020])
import matplotlib.pyplot as plt
plt.plot(a)
plt.show()