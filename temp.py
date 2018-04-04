stateAwal = [[1,2,3], [4, 5, 0], [7,8,6]]
stateGoal = [[1,2,3], [4, 5, 6], [7,8,0]]
heuristic = 0
position = [-1, -1]
gN = stateAwal

#def startHeu():
#    for i in stateGoal:
#        for j in stateGoal[i]:
#            if stateAwal[i][j] != stateGoal[i][j]:
#                heuristic += 1

def startHeu():
    global heuristic
    for i in range(3):
        for j in range(3):
            if stateAwal[i][j] != stateGoal[i][j]:
                for l in range(3):
                    if stateAwal[i][j] in stateGoal[l]:
                        k = stateGoal[l].index(stateAwal[i][j])
                        break
                heuristic += (abs(i - l) + abs(j - k))
                print('{} {}'.format(k, l))
                
def where0():
    for i in range(3):
        if 0 in stateAwal[i]:
            break
    global position
    position = [i, stateAwal[i].index(0)]
    
def swap(i, j):
    temp = gN[i][j]
    gN[i][j] = 0
    gN[position[0]][position[1]] = temp