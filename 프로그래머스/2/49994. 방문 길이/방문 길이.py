def solution(dirs):
    answer = 0
    x,y=0,0
    visited=set()
    for d in dirs:
        if d=='U':
            dx, dy = x, y+1
        elif d=='D':
            dx, dy = x, y-1
        elif d=='L':
            dx, dy = x-1, y
        elif d=='R':
            dx, dy = x+1, y
        else:
            continue
        
        if -6 < dx < 6 and -6 < dy < 6:
            path=(dx,dy,x,y)
            path_r=(x,y,dx,dy)
        
            visited.add(path)
            visited.add(path_r)
            x,y=dx,dy
        
    answer=len(visited)/2   
            
    return answer