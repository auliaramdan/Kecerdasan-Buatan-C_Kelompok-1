//Credits to: https://www.geeksforgeeks.org/bidirectional-search/

#include <bits/stdc++.h>
using namespace std;

class Graph
{
    int node;
 
     list<int> *adj;
     
public:
    Graph(int V);
    int isIntersecting(bool *src_visited, bool *dst_visited);
    void addEdge(int u, int v);																		//Undirected
    void printPath(int *src_parent, int *dst_parent, int src, int dst, int intersectNode);			//Print jalan
    void BFS(list<int> *queue, bool *visited, int *parent);											//Untuk BFS
    int biDirSearch(int s, int t);																	//Algoritma Bidirectional
};

Graph::Graph(int node)
{
    this->node = node;
    adj = new list<int>[node];
};
 
void Graph::addEdge(int u, int v)
{
    this->adj[u].push_back(v);
    this->adj[v].push_back(u);
};

void Graph::BFS(list<int> *queue, bool *visited, int *parent)
{
    int current = queue->front();
    queue->pop_front();
    list<int>::iterator i;
    for (i=adj[current].begin();i != adj[current].end();i++)
    {
        if (!visited[*i])
        {
            parent[*i] = current;
 
            visited[*i] = true;
 
            queue->push_back(*i);
        }
    }
};

int Graph::isIntersecting(bool *src_visited, bool *dst_visited)
{
    int intersectNode = -1;
    for(int i=0;i<node;i++)
    {
        if(src_visited[i] && dst_visited[i])
            return i;
    }
    return -1;
};

void Graph::printPath(int *src_parent, int *dst_parent, int src, int dst, int intersectNode)
{
    vector<int> path;
    path.push_back(intersectNode);
    int i = intersectNode;
    while (i != src)
    {
        path.push_back(src_parent[i]);
        i = src_parent[i];
    }
    reverse(path.begin(), path.end());
    i = intersectNode;
    while(i != dst)
    {
        path.push_back(dst_parent[i]);
        i = dst_parent[i];
    }
 
    vector<int>::iterator it;
    cout<<"*****Path*****\n";
    for(it = path.begin();it != path.end();it++)
        cout<<*it<<" ";
    cout<<"\n";
};

int Graph::biDirSearch(int src, int dst)
{
    bool src_visited[node], dst_visited[node];
 
    int src_parent[node], dst_parent[node];
 
    list<int> src_queue, dst_queue;
 
    int intersectNode = -1;
 
    for(int i=0; i<node; i++)
    {
        src_visited[i] = false;
        dst_visited[i] = false;
    }
 
    src_queue.push_back(src);
    src_visited[src] = true;
 
    src_parent[src]=-1;
 
    dst_queue.push_back(dst);
    dst_visited[dst] = true;
 
    dst_parent[dst] = -1;
 
    while (!src_queue.empty() && !dst_queue.empty())
    {
        BFS(&src_queue, src_visited, src_parent);
        BFS(&dst_queue, dst_visited, dst_parent);
 
        intersectNode = isIntersecting(src_visited, dst_visited);
 
        if(intersectNode != -1)
        {
            cout << "Intersection at: " << intersectNode << "\n";
 
            printPath(src_parent, dst_parent, src, dst, intersectNode);
            exit(0);
        }
    }
    return -1;
}

int main()
{
    int n=15;

 	cin >> s;
 	cin >> t;
 
    Graph g(n);
    g.addEdge(0, 4);
    g.addEdge(1, 4);
    g.addEdge(2, 5);
    g.addEdge(3, 5);
    g.addEdge(4, 6);
    g.addEdge(5, 6);
    g.addEdge(6, 7);
    g.addEdge(7, 8);
    g.addEdge(8, 9);
    g.addEdge(8, 10);
    g.addEdge(9, 11);
    g.addEdge(9, 12);
    g.addEdge(10, 13);
    g.addEdge(10, 14);
    if (g.biDirSearch(s, t) == -1)
        cout << "Path don't exist between "
             << s << " and " << t << "\n";
 
    return 0;
}
