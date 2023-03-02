# # sol1
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
    
# # sol2
# import sys
# print(sys.stdin.read())

# sol3
import sys
while True:
    line = sys.stdin.readline().rstrip()
    if line:
        print(line)
    else:
        break