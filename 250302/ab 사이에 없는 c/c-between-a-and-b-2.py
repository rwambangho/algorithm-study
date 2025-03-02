a, b, c = map(int, input().split())

for i in range(a, b + 1):
    if i % c == 0:  # 첫 번째 배수를 찾으면 바로 YES 출력 후 종료
        print("YES")
        break
else:  # for 루프가 break 없이 끝나면 실행됨
    print("NO")
