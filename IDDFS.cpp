#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class Graph{
	int node;											//Jumlah node
	list<int> *adj;										//List adjacency
	bool DLS(int node, int dest, int limit);			//Untuk DFS dengan limit
	
	public:
    Graph(int node);									//Constructor
    void addEdge(int src, int dst);						//Menambah edge
 
    bool IDDFS(int v, int target, int max_depth);		//Algoritma IDDFS
};

Graph::Graph(int node){
	this->node = node;
	adj = new list<int>[node];
}

void Graph::addEdge(int src, int dst)
{
    adj[src].push_back(dst);
}

bool Graph::DLS(int src, int dest, int limit){
	if(src == dest) return true;
	
	if(limit <= 0) return false;
	
	for (auto i = adj[src].begin(); i != adj[src].end(); ++i)
       if (DLS(*i, dest, limit-1) == true)
          return true;
          
     return false;
}

bool Graph::IDDFS(int src, int target, int max_depth)
{
    for (int i = 0; i <= max_depth; i++)
       if (DLS(src, target, i) == true)
          return true;
 
    return false;
}

int main(){
	Graph g(7);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 5);
    g.addEdge(2, 6);
 
    int target = 6, maxDepth = 3, src = 0;
    if (g.IDDFS(src, target, maxDepth) == true)
        cout << "Target reached";
    else
        cout << "Target NOT reached";
    return 0;
}
