import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from main import print_hi


def predictor(X, w):
    return np.matmul(X, w)


def loss(X, Y, w):
    return np.average((predictor(X, w) - Y) ** 2)


def gradient(X, Y, w):
    return 2 * np.matmul(X.T, (predictor(X, w) - Y)) / X.shape[0]


def train(X, Y, interation, lr):
    w = np.zeros([X.shape[1], 1])
    for i in range(interation):
        print("iteration %4d => Loss: %20f" % (i, loss(X, Y, w)))
        w -= gradient(X, Y, w) * lr
    return w


path = "C:/Users/amadu/PycharmProjects/ProjectPhoenix/Data/pizza_3_vars.txt"
X1, X2, X3, Y = np.loadtxt(path, skiprows=1, unpack=True)
X = np.column_stack([np.ones(X1.size), X1, X2, X3])
Y = Y.reshape(-1, 1)
w = np.zeros([X.shape[1], 1])
w = train(X, Y, interation=1_000_001 - (1_000_001 - 977693), lr=0.0001)
print(w)
value = np.array([[[1, 3, 2, 3], [1, 2, 3], [1, 2, 3]]], dtype=object)
value = value.transpose()
print(value)
