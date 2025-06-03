n = int(input())
arr = list(map(int, input().split()))
merged_arr=[0]*n

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    i=low
    j=mid+1
    k=low
    while i <= mid and j <= high:
        if arr[i]<=arr[j]:
            merged_arr[k]=arr[i]
            k+=1
            i+=1
        else:
            merged_arr[k]=arr[j]
            k+=1
            j+=1
        
    while i<=mid:
        merged_arr[k]=arr[i]
        k+=1
        i+=1
    
    while j<=high:
        merged_arr[k]=arr[j]
        k+=1
        j+=1
    
    for i in range(low,high+1):
        arr[i]=merged_arr[i]
    
    
    
    

merge_sort(arr,0,n-1)
print(*arr)