#include <iostream>
using namespace std;

int num[100001]; //수가 들어갈 배열생성

int main() {
	ios_base::sync_with_stdio(false); //iostream의 동기화를 비활성화. 성능을 높여 실행시간을 줄일 수 있다.
	cin.tie(0); cout.tie(0); //입출력을 묶어준다.
	int n, m; 
	

	cin >> n >> m; //수의 개수 N과 합을 구해야 하는 횟수 M
	
	int temp;
	for (int a = 1; a <= n; a++) { //수를 입력
		cin >> temp;
		num[a] = num[a - 1] + temp;

	}
	
	int i, j; 
	for (int b = 0; b < m; b++) {
		cin >> i >> j; //합을 구해야 하는 구간의 수
		int result = num[j] - num[i - 1];
		cout << result <<'\n';
	}
	return 0;
}