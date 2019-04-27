import random

x_size = 21
y_size = 21
sets = []

def initField(xSize, ySize):
    board = []
    for i in range(xSize):
        row = []
        for j in range(ySize):
            row.append('#')
        board.append(row)
    return board

def makeMaze(board) :
    evensX = []
    evensY = []
    count = 0
    mergeCount = 0
    
    for i in range(0,(x_size -1)//2 + 1) :
        evensX.append(i*2)
    for i in range(0,(y_size -1)//2 + 1) :
        evensY.append(i*2)
    
    #ADD THINGS TO SETS
    for i in evensX :
        for j in evensY :
            board[i][j] = " "
            sets.append([(i,j)])
    
    #Makes list of viables walls
    viableWalls = []
    for i in evensX :
        for j in range(0,y_size) :
            if(board[i][j] != " ") :
                viableWalls.append((i,j))
    for j in evensY :
        for i in range(0,x_size) :
            if(board[i][j] != " ") :
                viableWalls.append((i,j))
                
    #Do the thing yumi
    while(len(sets) > 2):
        wall = random.randint(0,len(viableWalls)-1)
        
        count+=1
        
        upQuestion = 1
        if ((viableWalls[wall][0]%2)==1) :
            upQuestion = 0
        
        #### UP IS ACTUALLY X
        
        if upQuestion is 0:
            if viableWalls[wall][0] < x_size-1:
                if viableWalls[wall][0] > 0: 
                    if checkSets((viableWalls[wall][0]-1, viableWalls[wall][1]), (viableWalls[wall][0]+1, viableWalls[wall][1])) : #up
                        mergeSets((viableWalls[wall][0]-1, viableWalls[wall][1]), (viableWalls[wall][0]+1, viableWalls[wall][1]), (viableWalls[wall][0], viableWalls[wall][1]))
                        board[viableWalls[wall][0]][viableWalls[wall][1]] = " "
                        mergeCount += 1
                        
        else:
            if viableWalls[wall][1] < x_size-1:
                if viableWalls[wall][1] > 0:
                    if checkSets((viableWalls[wall][0], viableWalls[wall][1]-1), (viableWalls[wall][0], viableWalls[wall][1]+1)) : #up
                        mergeSets((viableWalls[wall][0], viableWalls[wall][1]-1), (viableWalls[wall][0], viableWalls[wall][1]+1), (viableWalls[wall][0], viableWalls[wall][1]))
                        board[viableWalls[wall][0]][viableWalls[wall][1]] = " "
                        mergeCount += 1
        
        viableWalls.remove(viableWalls[wall])
    
    
    #Print 
    for i in range(x_size) :
        print(board[i])
    
def checkSets(x, y) :
    for i in sets:
        if x in i:
            if y in i:
                return False
    return True
    
def mergeSets(x, y, z):
    for i in range(0,len(sets)-1):
        if x in sets[i]:
            for j in range(0,len(sets)-1):
                if y in sets[j]:
                    sets[i] = sets[i] + sets[j]
                    sets[i].append(z)
                    sets.remove(sets[j])
                    
                    return True
                        

        
makeMaze(initField(x_size,y_size))
text = input("")