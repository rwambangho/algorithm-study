from functools import cmp_to_key
def compare(x,y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0
def solution(numbers):
    answer = ''
    #문자열로 변환
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer=str(int(''.join(numbers)))
    
    return answer