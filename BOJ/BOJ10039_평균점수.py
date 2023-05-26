lis = []
for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    lis.append(score)
print(sum(lis)//len(lis))