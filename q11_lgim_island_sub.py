test_case_0 = [[0, 0, 0, 1, 0, 0, 1, 1, 0],
               [0, 0, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 1, 0, 0],
               [1, 0, 0, 0, 0, 1, 1, 0, 0],
               [1, 1, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 0, 1, 1],
               [0, 0, 0, 1, 0, 0, 0, 0, 0]]


test_case_1 = [[0, 0, 0],
               [0, 1, 1],
               [0, 1, 0],
               [1, 0, 0]]


class number_island(object):
    def find_neighbours(self, cord_i,cord_j):
        # search_idx = [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]
        # for cord_i, cord_j in search_idx:
        if 0 > cord_i or cord_i > len(test_case) -1 or 0 > cord_j or cord_j > len(test_case[0])-1:
            return
        elif test_case[cord_i][cord_j] != 1:
            return
        test_case[cord_i][cord_j]='visited'

        self.find_neighbours(cord_i +1, cord_j)
        self.find_neighbours(cord_i -1, cord_j)
        self.find_neighbours(cord_i , cord_j +1)
        self.find_neighbours(cord_i , cord_j -1)

    def find_island(self, test_case):
        num_islands=0
        for i in range(len(test_case)):
            for j in range(len(test_case[0])):
                # print(i,j)
                if test_case[i][j] == 1:
                    # print("finding neighbours")
                    self.find_neighbours(i, j)
                    num_islands+=1
        return num_islands

for test_case in [test_case_0, test_case_1]:
    m = number_island()
    print(m.find_island(test_case=test_case))


'''
Though process:
1. need to visit neighbor cells to check if there's 1 or 0 connected => recursion of up, down, left, right, escape by return 
2. need to record visited cells, to not visit again => a list or change on passed test case from 0/1 to sth
3. need to record number of islands

import pandas as pd
import numpy as np

test_df = pd.DataFrame(test_case)


index_li = np.dstack(np.where(test_df==1))[0].tolist()
print(index_li)

print(type(index_li))
island_list = []


def find_same_island(i,j, same_island_list):
    if [i,j] in visited:
        return
    search_idx = [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]
    for cord_i, cord_j in search_idx:
        visited.append([cord_i, cord_j])
        print(f"looking for neighbour {cord_i, cord_j}")

        if [cord_i, cord_j] in index_li and [cord_i, cord_j] not in visited and (cord_i, cord_j) not in same_island_list:
            same_island_list.append((cord_i, cord_j))


            find_same_island(cord_i, cord_j, same_island_list)
        else:
            pass

visited = []
for i,j in index_li:
    print(i,j)
    island = [(i,j)]
    find_same_island(i, j, island)
    print("visited")
    print(visited)
    print(island)
    
    for cord in [test_case[i+1][j], test_case[i-1][j], test_case[i][j+1], test_case[i][j-1]]:
        if cord==1:
            island.append((i,j))
    
'''