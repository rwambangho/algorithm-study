def solution(answers):
    answer = []
    a=len(answers)
    cnt1, cnt2, cnt3 = 0, 0, 0
    n1=[[1,2,3,4,5] for _ in range(a)]
    n2=[[ 2, 1, 2, 3, 2, 4, 2, 5]for _ in range(a)]
    n3=[[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]for _ in range(a)]
    s1=[item for row in n1 for item in row]
    s2=[item for row in n2 for item in row]
    s3=[item for row in n3 for item in row]
    
    
    for i in range(a):
        if s1[i] == answers[i]:
            cnt1+=1
        if s2[i]==answers[i]:
            cnt2+=1
        if s3[i]==answers[i]:
            cnt3+=1
    
    
    if cnt1 > cnt2 and cnt1 > cnt3: #1
        answer.append(1)
    elif cnt2 > cnt1 and cnt2 > cnt3: #2
        answer.append(2)
    elif cnt3 > cnt1 and cnt3 > cnt2: #4
        answer.append(3)
    elif cnt1 > cnt3 and cnt2 > cnt3 and cnt1 == cnt2: #1 2
        answer.append(1)
        answer.append(2)
    elif cnt1 > cnt2 and cnt3 > cnt2 and cnt1 == cnt3: # 1 3
        answer.append(1)
        answer.append(3)
    elif cnt2 > cnt1 and cnt3 > cnt1 and cnt2 == cnt3: # 2 3
        answer.append(2)
        answer.append(3)
    elif cnt1 == cnt2 == cnt3: # 1 2 3
        answer.append(1)
        answer.append(2)
        answer.append(3)
        
              
    return answer