N = int(input())
lines = []
for _ in range(6):
    lines.append(list(map(int,input().split())))

long_garo = -999
long_sero = -999
for elem in lines:
    if elem[0] == 1 or elem[0] == 2:
        if elem[1] > long_garo:
            long_garo = elem[1]
            long_garo_idx = lines.index(elem)
    else:
        if elem[1] > long_sero:
            long_sero = elem[1]
            long_sero_idx = lines.index(elem)

idx_diff = long_garo_idx - long_sero_idx
if idx_diff == 1 or idx_diff == -5:
    short_garo_idx = (long_garo_idx + 2) % 6
    short_sero_idx = (long_garo_idx + 3) % 6
else:
    short_sero_idx = (long_sero_idx + 2) % 6
    short_garo_idx = (long_sero_idx + 3) % 6

area = long_garo * long_sero - lines[short_garo_idx][1] * lines[short_sero_idx][1]
print(area*N)