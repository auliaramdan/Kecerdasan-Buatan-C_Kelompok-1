# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:26:51 2018

@author: Ramdan
"""

cities={'Oradea':['Zerind', 'Sibiu'],
        'Zerind':['Oradea', 'Arad'],
        'Arad':['Zerind', 'Timisoara', 'Sibiu'], 
        'Sibiu':['Arad', 'Fagaras', 'Rimnicu Vilcea', 'Oradea'], 
        'Timisoara': ['Arad', 'Lugoj'],
        'Fagaras':['Sibiu', 'Bucharest'],
        'Rimnicu Vilcea':['Sibiu', 'Pitesti','Craiova'],
        'Lugoj':['Timisoara', 'Mehadia'],
        'Mehadia':['Dobreta', 'Lugoj'],
        'Dobreta':['Craiova', 'Mehadia'],
        'Craiova':['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
        'Pitesti':['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
        'Bucharest':['Giurgiu', 'Fagaras', 'Pitesti', 'Urziceni'],
        'Giurgiu':['Bucharest'],
        'Urziceni':['Vaslui', 'Hirsova', 'Bucharest'],
        'Hirsova':['Urziceni', 'Eforie'],
        'Eforie':['Hirsova'],
        'Vaslui':['Urziceni', 'Iasi'],
        'Iasi':['Neamt', 'Vaslui'],
        'Neamt':['Iasi']}

cityDist={'Oradea':[71, 151],
        'Zerind':[71, 75],
        'Arad':[75, 118, 140], 
        'Sibiu':[140, 99, 80, 151], 
        'Timisoara': [118, 111],
        'Fagaras':[99, 211],
        'Rimnicu Vilcea':[80, 97,146],
        'Lugoj':[111, 70],
        'Mehadia':[75, 70],
        'Dobreta':[120, 75],
        'Craiova':[120, 146, 138],
        'Pitesti':[97, 138, 101],
        'Bucharest':[90, 211, 101, 85],
        'Giurgiu':[90],
        'Urziceni':[85, 142, 98],
        'Hirsova':[98, 86],
        'Eforie':[86],
        'Vaslui':[142, 92],
        'Iasi':[87, 92],
        'Neamt':[87]}

heuristic={'Arad':366,
           'Bucharest':0,
           'Craiova':160,
           'Dobreta':242,
           'Eforie':161,
           'Fagaras':178,
           'Giurgiu':77,
           'Hirsova':151,
           'Iasi':226,
           'Lugoj':244,
           'Mehadia':241,
           'Neamt':234,
           'Oradea':380,
           'Pitesti':98,
           'Rimnicu Vilcea':193,
           'Sibiu':253,
           'Timisoara':329,
           'Urziceni':80,
           'Vaslui':199,
           'Zerind':374}


path = []
f = []
def AstarUtil(city, prev):
    path.append(city)
    if(city == 'Bucharest') :
        return
    else:
        index = -1
        q = 10000
        for i in range (len(cities[city])):
            if(cities[city][i] in path):
                continue
            if(q > cityDist[city][i] + prev + heuristic[cities[city][i]]):
                index = i
                q = cityDist[city][i] + prev + heuristic[cities[city][i]]
    f.append(q)
    AstarUtil(cities[city][index], prev + cityDist[city][index])
    return
    
def printPath(city):
    print("Path:\n")
    print(city)
    print(heuristic[city])
    print("\n")
    for i in range(len(path) - 1):
        print(path[i + 1])
        print(f[i])
        print("\n")

def Astar(city):
    AstarUtil(city, 0)
    printPath(city)
    
    