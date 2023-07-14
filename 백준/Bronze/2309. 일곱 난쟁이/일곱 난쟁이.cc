#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int h[9] = {};
	int sum = 0;
	for (int i = 0; i < 9; i++) { //입력한 수를 모두 더함
		cin >> h[i];
		sum += h[i];
	}
	
	sort(h, h+9); //오름차순 정렬시켜준다
	for (int i = 0; i < 8; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (sum - h[i] - h[j] == 100) { //합에서 두 수를 뺀 값이 100이면
				for (int k = 0; k < 9; k++) {
					if (k == i || k == j) //두 수를 제외하고 출력 
						continue;
					cout << h[k] << '\n';
				}
				return 0;
			}
		}
	}
	return 0;
}