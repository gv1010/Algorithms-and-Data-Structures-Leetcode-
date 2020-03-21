
def search(grid,i,j):
	if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
		return
	grid[i][j] = "0"
	search(grid,i+1, j)
	search(grid,i-1, j)
	search(grid,i, j+1)
	search(grid,i, j-1)
	
def dfs(grid, i, j):
	rows = len(grid)
	cols = len(grid[0])

	if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != "1":
		return 
		
	grid[i][j] = "0"
	dfs(grid,i+1,j)
	dfs(grid,i-1,j)
	dfs(grid,i,j+1)
	dfs(grid,i,j-1)
	
	
grid = [['1','1','1','1','0'],
		['1','1','0','0','0'],
		['1','0','0','1','0'],
		['1','0','1','1','0'],]

count = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == "1":
			search(grid, i,j)
			count += 1
print(count)