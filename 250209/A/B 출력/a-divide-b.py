a, b = map(int, input().split())

# 나눗셈 수행
quotient = a // b  # 정수 부분
remainder = a % b  # 나머지

# 소수점 아래 21자리까지 계산
decimal_part = []
for _ in range(21):
    remainder *= 10
    decimal_digit = remainder // b
    decimal_part.append(str(decimal_digit))
    remainder %= b

truncated_decimal = "".join(decimal_part[:20])
# 결과 출력
print(f"{quotient}.{truncated_decimal}")
