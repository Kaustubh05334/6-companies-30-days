from collections import defaultdict
def mostProfitablePath(edges, bob: int, amount) -> int:
    adjList = defaultdict(list)
    for u,v in edges :
        adjList[u].append(v)
        adjList[v].append(u)
    
    n = len(adjList)
    time = [0]*n
    time[bob] = 1
    def dfs1(node,par):
        if node == bob :
            return time[bob]
        res = 0
        for adj in adjList[node]:
            if adj == par :
                continue
            flag = dfs1(adj,node)
            if flag != 0  :
                res = 1 + flag
        time[node] = res
        return time[node]
    dfs1(0,None)
    
    
    res = float("-inf")
    def dfs2(node,par,t,income):
        for adj in adjList[node]:
            if adj == par :
                continue
            newTime = t + 1
            newIncome = income
            if time[adj] == 0 or newTime < time[adj] :
                newIncome += amount[adj]
            elif newTime == time[adj] :
                newIncome += amount[adj]//2
            if len(adjList[adj]) == 1 :
                res = max(res,newIncome)
            dfs2(adj,node,newTime,newIncome)
            
    
    dfs2(0,None,1,amount[0])
    return res