# https://school.programmers.co.kr/learn/courses/30/lessons/86971

import copy

def DFS(graph, visit, v):
    if visit[v] == True:
        return
    else:
        visit[v] = True
        for node in graph[v]:
            DFS(graph,visit,node)

def solution(n, wires):
    answer = n
    graph = { i:[] for i in range(1,n+1)}
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    for wire in wires:
        graph2 = copy.deepcopy(graph)
        graph2[wire[0]].remove(wire[1])
        graph2[wire[1]].remove(wire[0])

        visit = [False for _ in range(n+1)]
        DFS(graph2, visit, 1)

        cluster1 = sum(visit)
        cluster2 = n - cluster1
        
        temp = abs(cluster1-cluster2)
        if temp < answer:
            answer = temp
        
    return answer