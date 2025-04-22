def solution(sizes):
    answer = 0
    s=len(sizes)
    max_w,max_h=0,0
    
    for i in range(s):
        if sizes[i][0]<sizes[i][1]: # w < h일때 위치 교환
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if sizes[i][0] > max_w:
            max_w=sizes[i][0] # w의 최댓값구하고
        if sizes[i][1] > max_h:
            max_h=sizes[i][1] # h의 최댓값구하고
    
    answer=max_w*max_h   
    return answer