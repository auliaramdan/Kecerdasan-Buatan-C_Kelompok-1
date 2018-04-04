from copy import deepcopy as dc
stateAwal = [[1,2,3],[0,4,6],[7,5,8]]
stateGoal = [[1,2,3],[4,5,6],[7,8,0]]
Dummy = dc(stateAwal)
hURDL = [100,100,100,100]
Minimal = 100

def Heurist(array):
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

def Astar(array):
    global Minimal
    if Minimal == 0:
        return 0
    Z = wherenum(Dummy,0)
    X = Z[0]
    Y = Z[1]
    if X - 1 != -1:
        swap0U(Dummy)
        hURDL[0] = Heurist(Dummy)
        swap0D(Dummy)
    if Y + 1 != 3:
        swap0R(Dummy)
        hURDL[1] = Heurist(Dummy)
        swap0L(Dummy)
    if X + 1 != 3:
        swap0D(Dummy)
        hURDL[2] = Heurist(Dummy)
        swap0U(Dummy)
    if X - 1 != -1:
        swap0L(Dummy)
        hURDL[3] = Heurist(Dummy)
        swap0R(Dummy)
    Temp = min(hURDL)
    Minimal = Temp
    for I in range(3):
        if hURDL[I] == Temp:
            Pos = I
            break
    if Pos == 1:
        swap0U(Dummy)
    elif Pos == 2:
        swap0R(Dummy)
    elif Pos == 3:
        swap0D(Dummy)
    else:
        swap0L(Dummy)
    Astar(Dummy)

def Main():
    Astar(Dummy)
