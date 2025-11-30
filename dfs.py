graph={1:[2],2:[5,3,6], 3:[4],4:[],5:[],6:[]} # directed

def dfs(v):
    visited =set()
    visited.add(v)
    print(v)
    for e in graph[v]:
        if e not in visited:
            dfs(e)

dfs(1)
