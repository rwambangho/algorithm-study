#include<iostream>
#include<algorithm>
#define endl '\n'
/*
점수가 가장 높은 k명, 상을 받는 커트라인 구하기 
응시한 학생수 N 입력, 상 받는 학생 수 k입력
  
*/

using namespace std;

bool compare(int i, int j) {
	
	return i > j;
}
int main() {
	int n,k;
	int input[1000]={};
	cin >> n >> k;
	for(int i=0; i<n; i++){
	cin >> input[i];
	}	
	sort(input, input+n,compare);
	cout << input[k-1] << endl;
	
	return 0; 
}