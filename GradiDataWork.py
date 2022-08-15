import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

plt.axis([0, 50, 0, 50])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title("Pizza Order Regression")
plt.xlabel("Reservation", fontsize=15)
plt.ylabel("Pizzas", fontsize=15)


def predict(X, w, b):
    return X * w + b


def loss(X, Y, w, b):
    return np.average((predict(X, w, b) - Y) ** 2)


def gradient(X, Y, w, b):
    w_gradient = 2 * np.average(X * (predict(X, w, b) - Y))
    b_gradient = 2 * np.average(predict(X, w, b) - Y)
    return w_gradient, b_gradient


def train(X, Y, interation, lr):
    w = b = 0
    for i in range(interation):
        print("Iteration %4d => Loss: %.10f" % (i, loss(X, Y, w, b)))
        w_gradient, b_gradient = gradient(X, Y, w, b)
        w -= w_gradient * lr
        b -= b_gradient * lr
    return w, b


print(plt.style.available)
path = "C:/Users/amadu/PycharmProjects/ProjectPhoenix\Data/reser.txt"
X, Y = np.loadtxt(path, skiprows=1, unpack=True)
w, b = train(X, Y, interation=20000, lr=0.001)
print("\nw=%.10f, b =%.10f, " % (w, b))
print("Prediction: x=%d => y=%.2f" % (20, predict(20, w, b)))

sn.set()
y_new = predict(20, w, b)
plt.plot([0, 20], [b, Y[18]], "r-", linewidth=2)
plt.plot(X, Y, "b.")
plt.show()
