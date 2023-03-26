A1,B1 = map(int,input().split())
A2,B2 = map(int,input().split())
    
numerator = A1*B2 + A2*B1
denominator = B1 * B2

big = max(numerator,denominator)
small = min(numerator,denominator)
while True:
    remainder = big % small
    if remainder == 0:
        GCF = small
        break
    big = small
    small = remainder

print(numerator//GCF, denominator//GCF)
