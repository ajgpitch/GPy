import numpy as np
import pylab as pb
import GPy
np.random.seed(1)
print "GPLVM with RBF kernel"

N = 100
Q = 1
D = 2
X = np.random.rand(N, Q)
k = GPy.kern.rbf(Q, 1.0, 2.0) + GPy.kern.white(Q, 0.00001)
K = k.K(X)
Y = np.random.multivariate_normal(np.zeros(N),K,D).T

m = GPy.models.GPLVM(Y, Q)
m.constrain_positive('(rbf|bias|white)')

pb.figure()
m.plot()
pb.title('PCA initialisation')
pb.figure()
m.optimize(messages = 1)
m.plot()
pb.title('After optimisation')
