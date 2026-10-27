import numpy as np
from sklearn.linear_model import LinearRegression


X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 80, 110, 140, 170])

model = LinearRegression()

model.fit(X, y)

print("=== Մեքենայական ուսուցման մոդելը պատրաստ է ===")

rooms = 6
predicted_price = model.predict([[rooms]])

print(f"Սենյակների քանակը: {rooms}")
print(f"Կանխատեսվող գինը: {predicted_price[0]:.2f} հազար դոլար")
