A = input()
prev_char=A[0]
count=1
result=''
for i in range(1,len(A)):
    if A[i] == prev_char:
        count+=1
    else:
        result+=f"{prev_char}{count}"
        prev_char=A[i]
        count=1
result+=f"{prev_char}{count}"
print(len(result))
print(result)
