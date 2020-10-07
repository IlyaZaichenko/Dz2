import numpy as np

p = int(input())
k = int(input())
x = np.random.random(p).reshape(p, 1)
y = np.eye(p)
a = y * x
u = np.random.random((p, k))
v = np.random.random((k, p))
c = np.eye(k)


def woodbury(a, u, v):
    a1 = np.linalg.inv(a)
    f = np.linalg.inv(c + v @ a1 @ u)
    return a1 - a1 @ u @ f @ v @ a1


woodbury(a, u, v)


def realwoodbury(a, u, v):
    return np.linalg.inv(a + u @ v)


realwoodbury(a, u, v)
