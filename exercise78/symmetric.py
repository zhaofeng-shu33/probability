# for first problem
import numpy as np
theta = 2 * np.pi / 7
U = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
N = 10000
x_diag = np.random.normal(scale=np.sqrt(2), size=2*N)
x_off_diag = np.random.normal(size=N)
Y = np.zeros([N, 3])
for i in range(N):
    X = np.array([[x_diag[i], x_off_diag[i]], [x_off_diag[i], x_diag[i + N]]])
    _Y = U.T @ X @ U
    Y[i, :] = np.array([_Y[0, 0], _Y[1, 1], _Y[0, 1]])
print(np.cov(Y.T))
