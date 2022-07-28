def solution(distance, rocks, n):
    rocks = [0]+rocks+[distance]
    rocks.sort()
    
    dis = []
    for i in range(1,len(rocks)):
        temp = rocks[i] - rocks[i-1]
        dis.append(temp)
        
    # print(rocks) 
    # print(dis)
    
    dis2 = [[elem, i] for i, elem in enumerate(dis)]
    dis_sorted = sorted(dis2, key = lambda x: x[0], reverse=True)
    # print("dis_sorted: " ,dis_sorted)
    
    for _ in range(n):
        min_dis  = dis_sorted[-1][0]
        cand_inds = [dis_sorted.pop()]
        while 1:
            if dis_sorted[-1][0] == min_dis:
                cand_inds.append(dis_sorted.pop())
            else:
                break

        # print("cand_inds: ", cand_inds)
        final_cand = []
        for _, ind in cand_inds:
            if ind+1 < len(dis):
                final_cand.append([dis[ind]+dis[ind+1], ind])
            if ind-1 >= 0:
                final_cand.append([dis[ind-1]+dis[ind], ind-1])

        final_sorted = sorted(final_cand)
        
        for elem in cand_inds:
            if elem[1] == final_sorted[0][1]:
                cand_inds.remove(elem)
                break
        
        # print("final: ", final_sorted[0])
        
        while cand_inds:
            dis_sorted.append(cand_inds.pop())
        # print("\ndis_sorted: " ,dis_sorted)

        new_dis = final_sorted[0][0]
        min_index = final_sorted[0][1]

        dis[min_index] = new_dis
        dis[min_index+1] = new_dis

    return min(dis)