import numpy as np

# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    prices = np.dot(X, c)
    for p in prices:
        print(p)  

# Alternative implementation

def predict_2(X, c):
    x = np.array(X)
    c1 = np.array(c)

    print(x @ c1) 

predict(X, c)
predict_2(X, c)
