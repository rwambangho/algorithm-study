from collections import defaultdict
def solution(n, wires):
    # 전선 하나를 끊어서 전력망을 2개로 만들었을때 송전탑 개수의 차이가 가장 적은 방법을 찾는다
    # 송전탑 개수 차이를 리턴함
    answer = -1
    count_list=[]
    
    
    # 인접리스트를 만들어준다
    adj_list=defaultdict(list)
    for i in wires:
        node=i[0]
        adj_node=i[1]
        adj_list[node].append(adj_node)
        adj_list[adj_node].append(node)
    
    # dfs하여 전력망 하나의 스택원소의 개수를 리턴한다
    def dfs(start,visited):
        visited[start]=True
        count=1
        # 인접리스트 순회해서 방문안된 노드 방문하기
        for adj in adj_list[start]:
            if not visited[adj]:
                count+=dfs(adj,visited)
        
        # 더 이상 탐색할 노드가 없으면 종료
        return count
            
                
    # wires전체를 탐색해서 전선을 하나씩 끊어준다음 어떤 걸 끊었을때 가장 차이가 적은지 확인
    # 전선을 하나씩 끊어준다음 dfs탐색해야함
    for a,b in wires:
        visited=[False] *(n+1)
        stack=[]
        # 전선 하나 끊어주기
        adj_list[a].remove(b)
        adj_list[b].remove(a)
        cnt_a=dfs(1,visited)
        cnt_b=n-cnt_a
        # 절대값을 구하고 리스트에 담는다
        
        tmp=abs(cnt_a-cnt_b)
        count_list.append(tmp)
        # 전선 복원해주기
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    answer=min(count_list)   
    return answer