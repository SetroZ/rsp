from collections import deque
graph={1:[2],2:[5,3,6], 3:[4],4:[],5:[],6:[]} # directed

def bfs(s):
    q = deque([s])
    visited =set()
    while q:
        v= q.popleft()
        print(v)
        visited.add(v)
        for e in graph[v]:
            if e not in visited:
                q.append(e)

bfs(1)