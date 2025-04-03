s=input()
cnt=0
cnt1=0
for i in range(len(s)-1):
    if 'ee' in s[i:i+2]:
        cnt+=1
    if 'eb' in s[i:i+2]:
        cnt1+=1
print(f"{cnt} {cnt1}")
