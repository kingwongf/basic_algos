import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from functools import reduce
from collections import Counter, OrderedDict
from itertools import permutations, combinations, starmap, product

a = [1,2]
b = a
a[0] = 0
print(b)

t = 1.0 if 5==7 else 9.0
print(t)


a = [x if x%2==0 else np.nan for x in range(0,10) ] # if else in list comprehesion
b = range(0,10)

starmap_exp = starmap(np.power, zip(a,b))
print(list(starmap_exp))
prod_exp = product(a,b)
print(len(list(prod_exp)))
print(list(product('ABCD', repeat=3)))
print(list(permutations('ABCD', 3)))
print(list(combinations('ABCD', 3)))


print(" ".join(['Hello', 'King', 'Is', "it", "me"]))

print(OrderedDict(sorted({'a':'hi','c':'king','b':'world'}.items(), key=lambda x: x[0])))
print(OrderedDict(sorted({'a':'hi','c':'king','b':'world'}.items(), key=lambda x: len(x[1]))))

name = 'King'
age = 73
print(f"{name}, age: {age}")

print(set(random.choices('abcdefg', k=100)))

A = np.random.normal(size=[3,3])
A = A*A.transpose() * np.diag(np.ones(3))
print(np.linalg.cholesky(A))



exit()
df = pd.DataFrame(np.random.uniform(low=-5,high=5,size=(10,5)), columns=['feat%s'%i for i in range(1,6)])
# print(df)

remainder, whole = np.modf(df)

#print(remainder, whole)

whole = np.abs(whole.replace(0,1))




df.columns = pd.MultiIndex.from_product([['product'], df.columns.to_list()], names=['level0','level1'])

np.rint(df)

np.random.choice([1,2,3,4,5,100], size=3, p=[0.25,0.1,0.2,0.1,0.30,0.05])
random.choices([1,2,3,4,5,100], k=3, weights=[0.25,0.1,0.2,0.1,0.30,0.05]) ## same as above


# print(np.fmax(remainder, whole)) ## fmax ignores Nan
# print(np.copysign(remainder, -1))
I = np.diag(np.ones(10))  ## create Identity matrix, np.diag(np.ones(size))

# print(np.linalg.inv(np.diag(np.ones(10))))

eig_val, eig_vec = np.linalg.eig(np.linalg.inv(np.diag(np.ones(10)))) ## eigenvalues, eigenvectors = np.linalg.eig(M)

print(np.trace(np.diag(np.ones(10)))) ## trace of a matrix, sum of diag elements

print(np.argmax(I,axis=0)) ## index of first maxiumn

# print(np.random.normal(size=100))
sig=0.20
ret = np.exp(sig*np.random.normal(size=[100,10]))

ret[0,:] = 100
# print(ret)
S = ret.cumprod(0)

df_S = pd.DataFrame(ret).cumprod(0)
print(S)
print(df_S)
plt.plot(S)
# plt.show()