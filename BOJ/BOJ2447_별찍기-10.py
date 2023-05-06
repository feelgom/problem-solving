N = int(input())

def draw_star(N):
    if N == 1:
        return ["*"]
    lis = []
    stars = draw_star(N//3)
    for star in stars:
        lis.append(star*3)
    for star in stars:
        lis.append(star+" "*(N//3)+star)
    for star in stars:
        lis.append(star*3)
        
    return lis

print("\n".join(draw_star(N)))