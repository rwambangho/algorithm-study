def emergency_check():
  
  critical_count = 0  # A 진료소에 가는 사람 수를 세는 변수

  for _ in range(3):  # 3명의 정보를 입력받습니다.
    symptom, temperature = input().split()
    temperature = float(temperature)  # 체온을 실수형으로 변환합니다.

    if symptom == "Y" and temperature >= 37:  # 증상이 있고 체온이 37 이상인 경우
      critical_count += 1

  if critical_count >= 2:  # A 진료소에 2명 이상이 가는 경우
    return "E"  # 위급 상황
  else:
    return "N"  # 위급 상황 아님

if __name__ == "__main__":
  result = emergency_check()
  print(result)  # 결과 출력