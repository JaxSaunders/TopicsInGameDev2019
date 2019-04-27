import random

xLarge = 23
yLarge = 23

def initField(xSize, ySize):
    board = []
    for i in range(xSize):
        row = []
        for j in range(ySize):
            row.append('#')
        board.append(row)
    return board

def generate(board, xSize, ySize):
    cX = 3
    cY = 3
    wallList = [(3,2,3,3), (2,3,3,3), (4,3,3,3), (3,4,3,3)]
    board[cX][cY] = ' '
    #wallList.remove((1,0))
    #print(wallList)
    while (wallList != []):
        curWall = wallList[random.randint(0, len(wallList)-1)]
        
        if curWall[0] != curWall[2]: #it's vertical
            if curWall[0] > curWall[2]:
                #down
                
                if curWall[0]+1 <= xSize-1 and board[curWall[0]+1][curWall[1]] is '#': #in bounds
                    #make the other side maze, make me maze, add our walls, remove me from wall list
                    #add walls
                    
                    if curWall[0]+2 < xSize-1 and board[curWall[0]+2][curWall[1]] == '#':
                        wallList.append((curWall[0]+2, curWall[1], curWall[0]+1, curWall[1]))
                        
                    if curWall[1]+1 < ySize-1 and board[curWall[0]+1][curWall[1]+1] == '#':
                        wallList.append((curWall[0]+1, curWall[1]+1, curWall[0]+1, curWall[1]))
                        
                    if curWall[1]-1 > -1 and board[curWall[0]+1][curWall[1]-1] == '#':
                        wallList.append((curWall[0]+1, curWall[1]-1, curWall[0]+1, curWall[1]))
                        
                    board[curWall[0]+1][curWall[1]] = ' '
                    board[curWall[0]][curWall[1]] = ' '
                
                wallList.remove(curWall)
                
            else:
                #up
                
                if curWall[0]-1 > 0 and board[curWall[0]-1][curWall[1]] is '#': #in bounds
                    #make the other side maze, make me maze, add our walls, remove me from wall list
                    #add walls
                    #UP(tm)
                    if curWall[0]-2 > 0 and board[curWall[0]-2][curWall[1]] == '#':
                        wallList.append((curWall[0]-2, curWall[1], curWall[0]-1, curWall[1]))
                    #Right    
                    if curWall[1]+1 < ySize-1 and board[curWall[0]-1][curWall[1]+1] == '#':
                        wallList.append((curWall[0]-1, curWall[1]+1, curWall[0]-1, curWall[1]))  
                    #Left    
                    if curWall[1]-1 > 0 and board[curWall[0]-1][curWall[1]-1] == '#':
                        wallList.append((curWall[0]-1, curWall[1]-1, curWall[0]-1, curWall[1]))
                        
                    board[curWall[0]-1][curWall[1]] = ' '
                    board[curWall[0]][curWall[1]] = ' '
                
                wallList.remove(curWall)
                
                
        elif curWall[1] != curWall[3]: #it's horizontal
            if curWall[1] > curWall[3]:
                #right
                
                if curWall[1]+1 <= ySize-1 and board[curWall[0]][curWall[1]+1] is '#': #in bounds
                    #make the other side maze, make me maze, add our walls, remove me from wall list
                    #add walls
                    
                    #Right
                    if curWall[1]+2 < ySize-1 and board[curWall[0]][curWall[1]+2] == '#':
                        wallList.append((curWall[0], curWall[1]+2, curWall[0], curWall[1]+1))
                    #Up  
                    if curWall[0]-1 > 0 and board[curWall[0]-1][curWall[1]+1] == '#':
                        wallList.append((curWall[0]-1, curWall[1]+1, curWall[0], curWall[1]+1))
                    #Down    
                    if curWall[0]+1 < xSize-1 and board[curWall[0]+1][curWall[1]+1] == '#':
                        wallList.append((curWall[0]+1, curWall[1]+1, curWall[0], curWall[1]+1))
                        
                    board[curWall[0]][curWall[1]+1] = ' '
                    board[curWall[0]][curWall[1]] = ' '
                
                wallList.remove(curWall)
                
            else:
                #left
                
                if curWall[1]-1 > 0 and board[curWall[0]][curWall[1]-1] is '#': #in bounds
                    #make the other side maze, make me maze, add our walls, remove me from wall list
                    #add walls
                    
                    #Left
                    if curWall[1]-2 > 0 and board[curWall[0]][curWall[1]-2] == '#':
                        wallList.append((curWall[0], curWall[1]-2, curWall[0], curWall[1]-1))
                    #Up  
                    if curWall[0]-1 > 0 and board[curWall[0]-1][curWall[1]-1] == '#':
                        wallList.append((curWall[0]-1, curWall[1]-1, curWall[0], curWall[1]-1))
                    #Down    
                    if curWall[0]+1 < xSize-1 and board[curWall[0]+1][curWall[1]-1] == '#':
                        wallList.append((curWall[0]+1, curWall[1]-1, curWall[0], curWall[1]-1))
                        
                    board[curWall[0]][curWall[1]-1] = ' '
                    board[curWall[0]][curWall[1]] = ' '
                
                wallList.remove(curWall)


maze = initField(xLarge, yLarge)
generate(maze, xLarge, yLarge)	
for i in range(xLarge):
    print(maze[i])
	
text = input("")

