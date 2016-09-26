print(__doc__)

import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn import linear_model

###############################################################################
# Generate sample data
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

###############################################################################
# Add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))

###############################################################################
# Fit regression model
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)

r_ols = linear_model.LinearRegression()
r_ols.fit(X,y)
y_ols = r_ols.predict(X)

r_lasso = linear_model.Lasso(alpha=0.2)
r_lasso.fit(X,y)
y_lasso = r_lasso.predict(X)

r_ridge = linear_model.Ridge(alpha=0.1)
r_ridge.fit(X,y)
y_ridge = r_ridge.predict(X)

###############################################################################
# look at the results
plt.scatter(X, y, c='k', label='data')
plt.hold('on')
plt.plot(X, y_rbf, c='g', label='RBF model')
plt.plot(X, y_lin, c='r', label='Linear model')

plt.plot(X, y_poly, c='b', label='Polynomial model')
plt.plot(X, y_ols, c='y', label='OLS', lw=3)
plt.plot(X, y_lasso, c='c',label='Lasso(a=0.2)')
plt.plot(X, y_ridge, c='m',label='Ridge(a=0.2)')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()