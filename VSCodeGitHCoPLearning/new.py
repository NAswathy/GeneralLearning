import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error  

# Step 1: Generate sample data
X = np.random.rand(10, 1) * 10
y = 2 * X + 1 + np.random.randn(10, 1) * 0.5

print (y)
print ("hello")
print (X)
print (np.random.randn(10, 1) * 0.5)

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = model.predict(X_test)