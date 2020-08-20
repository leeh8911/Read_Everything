import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


x = np.array([[True, True],
[True, False],
[False, True],
[False, False]
])#4X2

y_true = np.array([[True],[True],[True],[False]])


W_init = 100*np.random.randn(2,1) # 2X1
b_init = np.random.randn()


def Relu(z):
    return z*(z > 0)

def Relu_back(z):
    return(z>0)

def loss_func(pred, true):
    return np.sum(0.5*(pred - true)**2)/pred.shape[0]

def loss_func_back(pred, true):
    return np.sum(pred - true)/pred.shape[0]



W = W_init
b = b_init

logW = np.empty((2,1),dtype = float)
logb = np.array([])
logLoss = np.array([])

iter = 0
lr = 0.01
while(iter < 100):

    z = x.dot(W)+np.ones([4,1])*b
    y = Relu(z)
    loss = loss_func(y, y_true)
    logW = np.append(logW, W, axis=1)
    logb = np.append(logb, b)
    logLoss = np.append(logLoss, loss)

    dl = loss_func_back(y, y_true)
    da = Relu_back(z)*dl
    dw = x.T.dot(da)
    db = da

    W -= dw*lr
    b -= db*lr

    iter += 1



fig = plt.figure()
plt.scatter(logW[0,1:].T, logW[1,1:].T, logLoss, c = logLoss, alpha = 1)
plt.show()