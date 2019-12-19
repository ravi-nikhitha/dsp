#To write a python program on linear algebra by using "linalg"
import numpy as np
import scipy
from scipy import linalg
a=np.array(input('enter 2*2 matrix1'))
b=np.array(input('enter 2*2 matrix2'))
#Finding the determinant of the matrix
z=np.linalg.det(a)
print "det of a=\n",z
#Finding the inverse of matrix
x=np.linalg.inv(a)
print"inverse of a=\n", x
#Finding eigen values of matrix
v=np.linalg.eig(a)
print "eigen value of a=\n",v
#Find sloving linear equation
t=np.linalg.solve(a,b)
print "linear equation=\n",t
#Finding eigen hermitian(conjugate symmetric) of matrix
s=np.linalg.eigh(a)
print "eigenh value of a=\n",s
#Finding logarithm of matrix
q=scipy.linalg.logm(a)
print "log of a=\n",q
#Finding exponential of matrix
o=scipy.linalg.expm(a)
print "exp of a=\n",o
#Finding eigen vector of given matrix
m=np.linalg.eigvals(a)
print "eigen vector of a=\n",m
#Finding vectors norms
k=scipy.linalg.norm(a)
print "norm of a=\n",k
#Finding square root of given matrix
i=scipy.linalg.sqrtm(a)
print "square root of a=\n",i
#To create new matrix of 1 and 0
g=scipy.linalg.tri(2,3,dtype=int)
print "new matrix=\n",g
#Finding rank of the given matrix
f=np.linalg.matrix_rank(a)
print "rank of a=\n",f
#To find the power of given matrix
d=np.linalg.matrix_power(a,2)
print "power of a=\n",d
#Finding orthogonal of given matrix
b1=scipy.linalg.orth(a)
print "orthogonal of a=\n",b1
#To find the polar form 
e1=scipy.linalg.polar(a)
print "polar form of a=\n",e1
#To find sum of two matrix 
f1=np.add(a,b)
print "addition of two matrix using numpy=\n",f1

