# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Generating synthetic dataset
np.random.seed(0)
house_sizes = np.random.randint(800, 3000, 50)  # House sizes (square feet)
prices = 50 * house_sizes + np.random.normal(0, 20000, 50)  # House prices

# Reshape the data for scikit-learn input
X = house_sizes.reshape(-1, 1)  # Feature matrix (House sizes)
y = prices  # Target variable (Prices)

#Splitting the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Creating and fitting the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Calculating R² score (coefficient of determination)
r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)

# Plotting the regression line and data points
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Linear Regression: House Size vs. Price')
plt.xlabel('House Size (sqft)')
plt.ylabel('Price ($)')
plt.show()

# Printing the coefficients
print("\nIntercept:", model.intercept_)
print("Coefficient:", model.coef_[0])