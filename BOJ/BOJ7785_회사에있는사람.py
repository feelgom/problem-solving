import sys
input = sys.stdin.readline
N = int(input())

map = {}
for _ in range(N):
    name, action = input().split()
    if action == "enter":
        map[name] = 1
    elif action == "leave":
        map.pop(name)

keys = list(map.keys())
keys.sort(reverse=True)
for elem in keys:
    print(elem)