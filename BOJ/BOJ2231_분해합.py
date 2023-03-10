N = int(input())
for m in range(N):
    m_str = str(m)
    m_list = [int(c) for c in m_str]
    if m+sum(m_list) == N:
        print(m)
        break
else:
    print(0)