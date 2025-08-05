arr = input().split()
string, q = arr[0], int(arr[1])

for i in range(q):
    qtype, a, b = input().split()
    string = list(string)
    
    if qtype == "1":
        string_a = string[int(a)-1]
        string_b = string[int(b)-1]
        
        string[int(a)-1] = string_b
        string[int(b)-1] = string_a
    
    elif qtype == "2":
        for i in range(len(string)):
            if string[i] == a:
                string[i] = b
            
    string = "".join(string)
    print(string)
    
