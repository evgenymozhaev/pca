import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
y = 2 * x + np.random.randn(10)*2
X = np.vstack((x,y))

print(x)
print(y)
print(X)


Xcentered = (X[0] - x.mean(), X[1] - y.mean())
m = (x.mean(), y.mean())
print(f"Mean vector: {m}")

plt.scatter(Xcentered[0], Xcentered[1])
plt.scatter(X[0], X[1])
plt.show()


covmat = np.cov(Xcentered)
print(f"covmat\n")
print(f"Variance of X:  {np.cov(Xcentered)[0,0]}")
print(f"Variance of Y:  {np.cov(Xcentered)[1,1]}")
print(f"Covariance X and Y:  {np.cov(Xcentered)[0,1]}")
