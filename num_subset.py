from itertools import combinations, combinations_with_replacement
import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from matplotlib import cm

def f(nums, cond=(5,8)):
    '''
    this returns the largest subset of integers of nums that none
    of the pairs has a difference of cond[0] or cond[1]

    :param nums: list of integers
    :param cond: set of integers/ conditions
    :return: subset
    '''

    for max_num in range(len(nums),1,-1):
        ## proposed combination
        for comb in combinations(nums, max_num):
            ## if differences between a pair not in set of condition
            if set([abs(pair[1]-pair[0]) for pair in combinations(comb, 2)]).isdisjoint(set(cond)):
                return comb



print("\n")
print(f"max size of subset with condition 5,8 within range 1 to 13: {len(f(list(range(1,14)), (5,8)))}")
print("\n")
## I want to see if the integers in the full set change the max size of the subset
## We'll build a matrix where the i and j are the condition difference,
## i.e. subset doesn't have difference of i or j
for max_num in range(10,18):

    nums = list(range(1,max_num+1))

    ## prepare matrix
    b=[[0]*max_num for i in range(max_num)]

    ## find each max length based on i and j, reverse i and j to save computation
    for pair in combinations_with_replacement(range(1, max_num+1),2):
        i,j = pair
        b[i - 1][j - 1] = len(f(nums, pair))
        if i!=j:
            b[j - 1][i - 1] =  b[i - 1][j - 1]


    # b = np.tril(np.array(b))
    b = np.array(b)

    print(f"full set integers: 1 to {max_num}")
    print(b)


    ## If you want to visualize it
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    #
    # X = np.arange(1, max_num+1, 1)
    # Y = np.arange(1, max_num+1, 1)
    # X, Y = np.meshgrid(X, Y)
    # Z = b
    # # print(Z)
    # surf = ax.plot_surface(X,Y,Z, cmap=cm.coolwarm,
    #                        linewidth=0, antialiased=False)
# plt.show()

## Doesn't seem to be any straightforward solution
## using the range of 10 to 18 integers as examples e.g. full set = {1-10}, {1-11}, {1,n}, ... {1-20}
## we only see a linear part from n//2 condition and incremeting by +1 for every 2 more intergers in the full set
