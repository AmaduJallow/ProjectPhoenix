import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

plt.axis([0, 50, 0, 50])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Reservation", fontsize=20)
plt.ylabel("Pizzas", fontsize=20)


def predict(X, w):
    return X * w


def loss(X, Y, w):
    return np.average((predict(X, w) - Y) ** 2)


def train(X, Y, interations, lr):
    w = 0
    for i in range(interations):
        current_loss = loss(X, Y, w)
        print("Iterations %4d => Loss: %.6f" % (i, current_loss))
        if loss(X, Y, w + lr) < current_loss:
            w += lr
        elif loss(X, Y, w - lr) < current_loss:
            w -= lr
        else:
            return w
    raise Exception("Could not converge with in %d interations" % interations)


print(plt.style.available)
path = "C:/Users/amadu/PycharmProjects/ProjectPhoenix\Data/reser.txt"
X, Y = np.loadtxt(path, skiprows=1, unpack=True)
w = train(X, Y, interations=10000, lr=0.01)
print("\nw=%.3f" % w)
print("Prediction: x=%d => y=%.2f" % (20, predict(20, w)))
plt.plot(X, Y)
plt.show()
