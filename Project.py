from copy import deepcopy as dc

stateAwal = [[1,2,3], [4, 5, 0], [7,8,6]]
stateGoal = [[1,2,3], [4, 5, 6], [7,8,0]]
position = [-1, -1]
gN = dc(stateAwal)
f = 1
h = [0, 0, 0, 0]
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
    #position
    array[position[0]][position[1]] = temp
    return array
    
def astar(g,  heuristic):
    global h
    if (g + heuristic) > f:
        return
    if position[0] + 1 < 3:
        temp = dc(gN)
        temp = swap(position[0] + 1, position[1], temp)
        h[0] = startHeu(temp)
        print("Kanan {}{}".format(h, temp))
        temp = 0
    if position[1] - 1 < 3:
        temp = dc(gN)
        print('{} {}'.format(position[0], position[1] -1))
        temp = swap(position[0], position[1] - 1, temp)
        h[1] = startHeu(temp)
        print("Atas {}{}".format(h, temp))
        temp = 0
    if position[0] - 1 < 3:
        temp = dc(gN)
        temp = swap(position[0] - 1, position[1], temp)
        h[2] = startHeu(temp)
        print("Kiri {}{}".format(h, temp))
        temp = 0
    if position[1] + 1 < 3:
        temp = dc(gN)
        temp = swap(position[0], position[1] + 1, temp)
        h[3] = startHeu(temp)
        print("Bawah {}{}".format(h, temp))
        temp = 0