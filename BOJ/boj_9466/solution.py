import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, graph, visited, dict_):
    if visited[i]:
        return 0
    visited[i] = True
    dict_[i] = len(dict_)
    if graph[i] in dict_:
        ans = dict_[graph[i]]
        dict_.clear()
        return ans
    elif visited[graph[i]]:
        ans = len(dict_)
        dict_.clear()
        return ans
    else:
        return dfs(graph[i], graph, visited, dict_)
    
def main(N, graph):
    ans = 0
    dict_ = dict()
    graph = [0] + graph
    visited = [False] * (N+1)
    
    for i in range(1, N+1):
        ans += dfs(i, graph, visited, dict_)
    ans += len(dict_)
        
    print(ans)

if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        main(N, nums)
