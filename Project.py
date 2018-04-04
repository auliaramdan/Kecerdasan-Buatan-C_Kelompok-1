stateAwal = [[1,2,3], [4, 5, 0], [7,8,6]]
stateGoal = [[1,2,3], [4, 5, 6], [7,8,0]]

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
                
def wherenum(state,num):
    for i in range(3):
        if num in state[i]:
            break
    position = [i,state[i].index(num)]
    return position
