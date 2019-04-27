import random

xLarge = 21
yLarge = 21

def initField(xSize, ySize):
	board = []
	for i in range(xSize):
		row = []
		for j in range(ySize):
			row.append('#')
		board.append(row)
	return board
		
def checkNeighbors(board, xPos, yPos):
	leftTrue = False
	rightTrue = False
	upTrue = False
	downTrue = False
	returnList = []
	if xPos > 2: #Left
		if board[xPos-1][yPos] == '#':
			if board[xPos-2][yPos] == '#':
				if board[xPos-3][yPos] == '#':
					leftTrue = True
	
	if xPos == 2:
		if board[xPos-1][yPos] == '#':
			if board[xPos-2][yPos] == '#':
				leftTrue = True

	if xPos < xLarge-3: #Right
		if board[xPos+1][yPos] == '#':
			if board[xPos+2][yPos] == '#':
				if board[xPos+3][yPos] == '#':
					rightTrue = True
					
	if xPos == xLarge - 3:
		if board[xPos+1][yPos] == '#':
			if board[xPos+2][yPos] == '#':
				rightTrue = True
	
	if yPos > 2: #Up
		if board[xPos][yPos-1] == '#':
			if board[xPos][yPos-2] == '#':
				if board[xPos][yPos-3] == '#':
					upTrue = True

	if yPos == 2:
		if board[xPos][yPos-1] == '#':
			if board[xPos][yPos-2] == '#':
				upTrue = True				
					
	if yPos < yLarge-3: #Down
		if board[xPos][yPos+1] == '#':
			if board[xPos][yPos+2] == '#':
				if board[xPos][yPos+3] == '#':
					downTrue = True
					
	if yPos == yLarge-3:
		if board[xPos][yPos+1] == '#':
			if board[xPos][yPos+2] == '#':
				downTrue = True
	
	returnList.append(leftTrue)
	returnList.append(rightTrue)
	returnList.append(upTrue)
	returnList.append(downTrue)
	return returnList
	
def checkSodden(board, xPos, yPos):
	leftTrue = False
	rightTrue = False
	upTrue = False
	downTrue = False
	returnList = []
	if xPos > 0: #Left
		if board[xPos-1][yPos] == '1':
			leftTrue = True

	if xPos < xLarge-1: #Right
		if board[xPos+1][yPos] == '1':
			rightTrue = True
	
	if yPos > 0: #Up
		if board[xPos][yPos-1] == '1':
			upTrue = True			
					
	if yPos < yLarge-1: #Down
		if board[xPos][yPos+1] == '1':
			downTrue = True
			
	returnList.append(leftTrue)
	returnList.append(rightTrue)
	returnList.append(upTrue)
	returnList.append(downTrue)
	return returnList	
	
def generate(board):
	cX = 0
	cY = 0
	board[cX][cY] = '1'
	finishCondition = False
	while(not finishCondition):
		neighbors = checkNeighbors(board, cX, cY)
		comrades = checkSodden(board, cX, cY)
		if sum(neighbors) == 0:
			if sum(comrades) == 0:
				finishCondition = True
		if sum(neighbors) == 0:
			board[cX][cY] = '2'
			if comrades[0] == True:
				board[cX-1][cY] = '2'
				cX = cX - 2
			if comrades[1] == True:
				board[cX+1][cY] = '2'
				cX = cX + 2
			if comrades[2] == True:
				board[cX][cY-1] = '2'
				cY = cY - 2
			if comrades[3] == True:
				board[cX][cY+1] = '2'
				cY = cY + 2
		else:
			randDirection = 0 #Left, Right, Up, Down 		
			randDirection = random.randint(1,sum(neighbors))
			count = 0
			loc = -1
			breakCase = False
			while breakCase == False:
				loc = loc + 1
				if neighbors[loc] == True:
					randDirection = randDirection - 1
					if randDirection == 0:
						if (loc == 0):
							board[cX - 1][cY] = '1'
							board[cX - 2][cY] = '1'
							cX = cX - 2
							breakCase = True
						if (loc == 1):
							board[cX + 1][cY] = '1'
							board[cX + 2][cY] = '1'
							cX = cX + 2
							breakCase = True
						if (loc == 2): 
							board[cX][cY - 1] = '1'
							board[cX][cY - 2] = '1'
							cY = cY - 2
							breakCase = True
						if (loc == 3):
							board[cX][cY + 1] = '1'
							board[cX][cY + 2] = '1'
							cY = cY + 2
							breakCase = True			
	

	for i in range(xLarge):
		tempString = ''
		for j in range(yLarge):
			if board[i][j] == '2':
				board[i][j] = ' '
		
	
maze = initField(xLarge, yLarge)
generate(maze)

for i in range(xLarge):
	print(maze[i])

text = input("")