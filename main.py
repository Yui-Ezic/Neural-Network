import network
from numpy import array, float64

L1 = array([[1, 0.8, 0.8],
            [0, 0, 0]], dtype=float64)
L2 = array([[0, 0],
            [0, 0]], dtype=float64)
W = array([[0, 0, 1],
           [0.5, 0.5, 0]])

print(L1)
print(L2)
print(W)

network.forwards(L1, W, L2)

print(L2)

