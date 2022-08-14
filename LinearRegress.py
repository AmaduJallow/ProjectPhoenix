import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("homeprices.csv")

plt.xlabel("Area(ft^2)")
plt.ylabel("Prices(USD$)")
plt.scatter(df.Area, df.Price, color="blue")
plt.title("Graph for Land Price")

reg = LinearRegression()
reg.fit(df[["Area"]], df.Price)
predicted = reg.predict([[10_000]])
print(predicted)
plt.show()
