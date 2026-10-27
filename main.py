import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[15], [20], [25], [30], [35]])
y = np.array([20, 40, 70, 100, 130])

model = LinearRegression()
model.fit(X, y)

print("Project is ready")

temp = 38
predicted_sales = model.predict([[temp]])

print(f"tempreture: {temp}°C")
print(f"predicted sales: {predicted_sales[0]:.1f} հատ պաղպաղակ")
