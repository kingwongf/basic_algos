from itertools import combinations, permutations, product
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)



print((0,0,100)==(0,100,0))
r = np.arange(0,105,5).tolist()
print(r)


comb = list(product(r,repeat=3))
df = pd.DataFrame(comb, columns=['a','b','c'])

df.to_csv("comb_lgim.csv")

df.loc[df.sum(axis=1 ) == 100, 'valid'] = True
print(df.shape)
df = df[df["valid"]==True]
df.fillna(False, inplace=True)
print(df.shape)

print(df)
# print(list(comb))


import re, seaborn as sns, numpy as np, pandas as pd, random
from pylab import *
from matplotlib.pyplot import plot, show, draw, figure, cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
sns.set_style("whitegrid", {'axes.grid' : False})

fig = plt.figure(figsize=(6,6))

ax = Axes3D(fig)

ax.scatter(df['a'], df['b'], df['c'], marker='X', s=0.5)
ax.set_xlabel('A Label')
ax.set_ylabel('B Label')
ax.set_zlabel('C Label')
plt.show()