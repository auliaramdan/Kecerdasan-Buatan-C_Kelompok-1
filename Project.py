stateAwal = [[1,2,3], [4, 5, 0], [7,8,6]]
stateGoal = [[1,2,3], [4, 5, 6], [7,8,0]]
Current = [[1,2,3],[4,0,5],[6,7,8]]

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
                
def wherenum(array,num):
    for i in range(3):
        if num in array[i]:
            break
    position = [i,array[i].index(num)]
    return position

def swap0U(array):
    Z = wherenum(array,0)
    X = Z[0]
    Y = Z[1]
    array[X][Y] = array[X-1][Y]
    array[X-1][Y] = 0
    return array

def swap0D(array):
    Z = wherenum(array,0)
    X = Z[0]
    Y = Z[1]
    array[X][Y] = array[X+1][Y]
    array[X+1][Y] = 0
    return array

def swap0L(array):
    Z = wherenum(array,0)
    X = Z[0]
    Y = Z[1]
    array[X][Y] = array[X][Y-1]
    array[X][Y-1] = 0
    return array

def swap0R(array):
    Z = wherenum(array,0)
    X = Z[0]
    Y = Z[1]
    array[X][Y] = array[X][Y+1]
    array[X][Y+1] = 0
    return array
