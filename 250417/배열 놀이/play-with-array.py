n,q=map(int,input().split()) 
n_arr=list(map(int,input().split())) #n개 원소의 값
for _ in range(q): #q개의 줄에걸쳐 q개의 질의가 주어진다
    q_arr=list(map(int,input().split()))
    if q_arr[0] == 1:
        print(n_arr[q_arr[1]-1])
    elif q_arr[0] == 2:
        if q_arr[1] in n_arr:
            for elem in n_arr:
                if elem == q_arr[1]:
                    print(n_arr.index(elem)+1)
                    break   
        else:
            print('0')             
    elif q_arr[0] == 3:
        for elem in n_arr[q_arr[1]-1:q_arr[2]]:
            print(elem,end=' ')
        print()
    q_arr=[0,0,0]
        







    


