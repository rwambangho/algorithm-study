#include<iostream>
#include<algorithm> 
#define endl '\n'
/*
다섯개의 정수를 자연수로 받는다 자연수: 0보다큰 양의정수 
평균과 중앙값을 출력한다
1. 평균과 중앙값을 정의한다
2. 평균=모든수의합/5, 중앙값은 정렬상태에서 가운데 값으로 설정  
*/

using namespace std;


int main() {
	int avr,mid;
	int input[5] ={}; 
	int sum_data=0;
	for(int i=0; i<5; i++){ //자연수 입력을 5번받음 
		
			cin >> input[i];
			sum_data += input[i];
		
	}
	
	sort(input, input+5); //5개의 수를 정렬
	
	
	avr = sum_data / 5; //평균 
	mid = input[2]; //중앙값  
	cout << avr << endl;
	cout << mid;	
	
	
	return 0;
}