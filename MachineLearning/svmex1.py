import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import svm
X = np.array([[1,2],
     [5,8],
     [1.5,1.9],
     [8,8],
     [1,0.7],
     [9,11]])
Y = np.array([0,1,0,1,0,1])
plt.scatter(X[:,0],X[:,1])


clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X,Y)
X_test = np.array([[6,7]])
Y_test = clf.predict(X_test)
print Y_test
plt.scatter(X_test[:,0],X_test[:,1], c = "y")


w = clf.coef_[0]
print w
a = -w[0]/w[1] # it's  y = Ax + b (a is the slope
b = -clf.intercept_[0] / w[1]
xx = np.linspace(0,16)
yy = a*xx + b

h0 = plt.plot(xx,yy,'k-',label = "non weighted div")
plt.legend
plt.show()
clf.coef_[0]
clf.coef_[1]
clf.intercept_[0]
clf.intercept_[1]
