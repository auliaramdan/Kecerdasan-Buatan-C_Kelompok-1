from copy import deepcopy as dc
import numpy as np


stateAwal = [[1,2,3], [4, 0, 5], [7,8,6]]
stateGoal = [[1,2,3], [4, 5, 6], [7,0,8]]
heuristic = 0
position = [-1, -1]
moves = 0
f = 0
#def startHeu():
#    for i in stateGoal:
#        for j in stateGoal[i]:
#            if stateAwal[i][j] != stateGoal[i][j]:
#                heuristic += 1

def startHeu(array):
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if array[i][j] != stateGoal[i][j] and array[i][j] != 0:
                for l in range(3):
                    if array[i][j] in stateGoal[l]:
                        k = stateGoal[l].index(array[i][j])
                        break
                heuristic += (abs(i - l) + abs(j - k))
    return heuristic
                
def where0():
    for i in range(3):
        if 0 in stateAwal[i]:
            break
    global position
    position = [stateAwal[i].index(0), i]
    
def swap(j, i, array):
    temp = array[i][j]
    array[i][j] = 0
    array[position[1]][position[0]] = temp
    return array
    
def astarUtil(g,  heuristic, array):
    global f
    temph = []
    temp = dc(gN)
    temploc = []
    
    if heuristic == 0:
        return

    if (g + heuristic) > f:
        return
    
    if position[0] + 1 < 3:
        temph.append(astarUtil2(g, heuristic,position[0] + 1, position[1], temp))
        temploc.append([position[0] + 1, position[1]])
        
    if position[1] - 1 < 3:
        temph.append(astarUtil2(g, heuristic,position[0], position[1] - 1, temp))
        temploc.append([position[0], position[1] - 1])
        
    if position[0] - 1 < 3:
        temph.append(astarUtil2(g, heuristic,position[0] - 1, position[1], temp))
        temploc.append([position[0] - 1, position[1]])
        
    if position[1] + 1 < 3:
        temph.append(astarUtil2(g, heuristic,position[0], position[1] + 1, temp))
        temploc.append([position[0], position[1] + 1])
        
    enumtemp = list(enumerate(temph))
    tempnp = np.array(enumtemp)
    expand = np.argmin(tempnp, axis = 1)
    take = np.argmax(expand)
    f = heuristic + g
    print(temploc[take][0], temploc[take][1], f)
    move(temploc[take][0], temploc[take][1], temph[take], g+1)
    
 
def astarUtil2(g, heuristic, i, j, array):
    h = 0
    if heuristic == 0:
        return 0
    if heuristic + g > f:
        return 1
    temp = dc(array)
    temp = swap(i, j, array)
    h = startHeu(temp)
    return h

def move(i, j, heuristic, g):
    global gN, moves
    moves += g
    gN = swap(i, j, gN)
    where0()
    astarUtil(g, heuristic, gN)
               
def astar():
    global f, gN
    where0()
    gN = stateAwal
    heuristic = startHeu(gN)
    f = heuristic
    astarUtil(0, heuristic, gN)
