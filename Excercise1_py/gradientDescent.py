import numpy as np

def gradientDescent(X, y, theta, alpha, iterations):
    m = len(y) # number of training examples
    J_history = np.zeros((iterations, 1))
    for i in range(iterations):
        temp = np.dot(X.T, np.dot(X, theta) - y)
        theta = theta - alpha / m * temp
        from computeCost import computeCost
        J_history[i] = computeCost(X, y, theta)
    return theta, J_history
