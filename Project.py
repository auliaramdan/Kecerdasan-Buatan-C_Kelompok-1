import time
from copy import deepcopy as dc
StateAwal = []
StateGoal = []
Dummy = []
hURDL = [100,100,100,100]
Counter = 1
BlockPath = 100

def GetState(array):
    for i in range(3):
        array.append([int(j) for j in input().split()])

def PrintState(array):
    for A in range(0,3):
        print(array[A][0],array[A][1],array[A][2])

def Interface():
    print("\nInput 3x3 nilai untuk state awal:")
    GetState(StateAwal)
        
    print("\nState Awal:")
    PrintState(StateAwal)
        
    global Dummy
    Dummy = dc(StateAwal)
        
    print("\nInput 3x3 nilai untuk state goal:")
    GetState(StateGoal)
        
    print("\nState Goal:")
    PrintState(StateGoal)
        
def Heurist(array):
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if array[i][j] != StateGoal[i][j] and array[i][j] != 0:
                for l in range(3):
                    if array[i][j] in StateGoal[l]:
                        k = StateGoal[l].index(array[i][j])
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

def Start():
    print("\nState Awal:")
    PrintState(StateAwal)

def Astar(Minimal):
    if Minimal == 0:
        return 0
    global Counter
    global BlockPath
    Z = wherenum(Dummy,0)
    X = Z[0]
    Y = Z[1]
    print("\nStep ke",Counter)
    Counter = Counter + 1
    if X - 1 != -1:
        swap0U(Dummy)
        hURDL[0] = Heurist(Dummy)
        swap0D(Dummy)
    else:
        hURDL[0] = BlockPath
    if Y + 1 != 3:
        swap0R(Dummy)
        hURDL[1] = Heurist(Dummy)
        swap0L(Dummy)
    else:
        hURDL[1] = BlockPath
    if X + 1 != 3:
        swap0D(Dummy)
        hURDL[2] = Heurist(Dummy)
        swap0U(Dummy)
    else:
        hURDL[2] = BlockPath
    if Y - 1 != -1:
        swap0L(Dummy)
        hURDL[3] = Heurist(Dummy)
        swap0R(Dummy)
    else:
        hURDL[3] = BlockPath
    Minimal = min(hURDL)
    Pos = hURDL.index(Minimal)
    if Pos == 0:
        swap0U(Dummy)
        hURDL[2] = BlockPath
        PrintState(Dummy)
    elif Pos == 1:
        swap0R(Dummy)
        hURDL[3] = BlockPath
        PrintState(Dummy)
    elif Pos == 2:
        swap0D(Dummy)
        hURDL[0] = BlockPath
        PrintState(Dummy)
    elif Pos == 3:
        swap0L(Dummy)
        hURDL[1] = BlockPath
        PrintState(Dummy)
    print("Heuristic =",Minimal)
    Astar(Minimal)

def Main():
    StartTime = time.time()
    Interface()
    Start()
    Astar(100)
    EndTime = time.time()
    Z = EndTime - StartTime
    print("Program runtime =",Z)
