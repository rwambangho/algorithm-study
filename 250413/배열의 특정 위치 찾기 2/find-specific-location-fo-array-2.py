s=list(map(int,input().split()))
hol=[i for i in s[:len(s):2]]

zzak=[i for i in s[1:len(s):2]]


print(abs(sum(hol)-sum(zzak)))
