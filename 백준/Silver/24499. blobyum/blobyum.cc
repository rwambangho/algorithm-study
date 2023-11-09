#include <iostream>
#include<vector>
#include<algorithm>
//슬라이딩 윈도우기법을 이용한 풀이
//k길이의 합을 left와 right를 움직여가며 최댓값을 갱신하는 방법

using namespace std;

int main() {
	int n, k;

	cin >> n >> k;
	int sum = 0;
	vector <int> a(n); //n개의 원소를 넣을 vector생성
	int input = 0;
	for (int i = 0; i <= n-1; i++) {
		cin >> a[i];
		
	}
	for (int i = 0; i <= k - 1; i++) {
		sum += a[i];
	}
	int left = 0, right = k - 1;
	int maxi = sum;
	while (true) {
		sum -= a[left]; //
		left = (left + 1) % n;
		right = (right + 1) % n;
		sum += a[right];
		if (left == 0) break;
		maxi = max(maxi, sum);
	}
	
	cout << maxi;
}