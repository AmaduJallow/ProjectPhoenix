import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

plt.axis([0, 50, 0, 50])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title("Pizza Order Regression")
plt.xlabel("Reservation", fontsize=15)
plt.ylabel("Pizzas", fontsize=15)


def predict(X, w):
    return X * w


def loss(X, Y, w):
    return np.average((predict(X, w) - Y) ** 2)


def train(X, Y, interation, lr):
    w = 0
    for i in range(interation):
        current_loss = loss(X, Y, w)
        print("Iterations %4d => Loss: %.13f" % (i, current_loss))
        if loss(X, Y, w + lr) < current_loss:
            w += lr
            # print("width from actual value %.25f" % w)
        elif loss(X, Y, w - lr) < current_loss:
            w -= lr
            # print("width from actual value %.25f" % w)
        else:
            # print("width from actual value %.25f" % w)
            return w
    raise Exception("Could not converge with in %d interations" % interation)


print(plt.style.available)
path = "C:/Users/amadu/PycharmProjects/ProjectPhoenix\Data/reser.txt"
X, Y = np.loadtxt(path, skiprows=1, unpack=True)
w = train(X, Y, interation=1_000_000, lr=0.01)
print("\nw=%.3f" % w)
print("Prediction: x=%d => y=%.2f" % (20, predict(20, w)))
y_new = predict(20, w)

print(f"the value of y {y_new}")
sn.set()
plt.plot([0, 20], [20 , y_new], "r-", linewidth=2)
plt.plot(X, Y, "b.")
plt.show()
