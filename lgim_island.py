import pandas as pd
import numpy as np
test_case = [[0, 0, 0, 1, 0, 0, 1, 1, 0],
             [0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0],
             [1, 0, 0, 0, 0, 1, 1, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 1, 1],
             [0, 0, 0, 1, 0, 0, 0, 0, 0]]

test_case_1 = [[0, 0, 0],
             [0, 1, 1],
             [0, 1, 0]]

print(not test_case)
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(g`rid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)



test_df = pd.DataFrame(test_case)
print(test_df)
# print(np.where(test_df==1))
# print([(i, j) for i in test_case[j] for j in test_case])

index_li = np.dstack(np.where(test_df==1))[0].tolist()
print(index_li)

print(type(index_li))
island_list = []


def find_same_island(i,j, same_island_list):
     if
    search_idx = [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]


    for cord_i, cord_j in search_idx:
        print(f"looking for neighbour {cord_i, cord_j}")
        if [cord_i, cord_j] in index_li and [cord_i, cord_j] not in visited and (cord_i, cord_j) not in same_island_list:
            same_island_list.append((cord_i, cord_j))
            visited.append([cord_i, cord_j])

            find_same_island(cord_i, cord_j, same_island_list)
        else:
            pass

visited = []
for i,j in index_li:
    print(i,j)

    island = [(i,j)]

    find_same_island(i, j, island)

    print(island)
    '''
    for cord in [test_case[i+1][j], test_case[i-1][j], test_case[i][j+1], test_case[i][j-1]]:
        if cord==1:
            island.append((i,j))
    '''