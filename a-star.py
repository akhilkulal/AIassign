import copy

pacman_x, pacman_y = list(map(int, input().split()))#position of pacman
#'.' is food '-' path '#' is blockage for pacman 
food_x, food_y = list(map(int, input().split()))#position of food (positioning as per 0 indexing)
n, m = list(map(int, input().split()))#size of pacman grid
grid = []
answer_routes = None

for i in range(0, n):
    grid.append(list(map(str, input())))

def astar(grid, px, py, fx, fy, ans, n, m):
	queue = []
	queue.append([px, py, [], 0])
	directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
	while len(queue) > 0:
    		x, y, r, score = queue.pop(0)
    		routes = copy.deepcopy(r)
    		routes.append([x, y])

    		if x == fx and y == fy:
        		if ans == None:
        		    	ans = routes
        		    	return ans
        

    		possible_moves = []
    		for direction in directions:
        		next_x, next_y = x + direction[0], y + direction[1]
        		if (next_x < 0 and next_x >= n) or (next_y < 0 and next_y >= n):
        		    	continue
	
        		if grid[next_x][next_y] == "-" or grid[next_x][next_y] == ".":
        		    	grid[next_x][next_y] = '='
        		    	possible_moves.append([next_x, next_y, score + abs(fx - next_x) + abs(fy - next_y)])
            
    		possible_moves.sort(key = lambda x: x[2])
    		for move in possible_moves:
       			queue.append([move[0], move[1], routes, score])
        return ans
        
ans = astar(grid, pacman_x, pacman_y, food_x, food_y, answer_routes, n, m)
if ans == None:
	print("No path found ")
else:
	print(str(len(ans) - 1))
	for point in ans:
    		print(str(point[0]) + " " + str(point[1]))
