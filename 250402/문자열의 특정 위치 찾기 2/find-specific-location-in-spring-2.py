n=input()
cnt=0
chr_list=["apple", "banana", "grape", "bluberry", "orange"]
for i in range(5):
    if chr_list[i][2] == n or chr_list[i][3] == n:
        print(chr_list[i])
        cnt+=1
print(cnt)


    
