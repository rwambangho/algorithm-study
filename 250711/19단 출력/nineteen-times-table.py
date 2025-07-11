for i in range(1,20):
    for j in range(1,20,2):
        for k in range(j,j+2):
            if k%2==0:
                print(f"{i} * {k} = {i*k}")
            elif k==19:
                print(f"{i} * {k} = {i*k}")
                break
            else:
                print(f"{i} * {k} = {i*k}",end=' / ')
        
