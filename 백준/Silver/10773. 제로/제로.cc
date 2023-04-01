#include<iostream>
#include<stack>

/*
1 입력받는다
2 0이면 스택 위에있는 원소를 삭제 아니면 삽입
3 스택에 남아있는 원소들의 크기만큼 반복문 돌려서 더함  
4 더했으면 삭제하고  sum출력  
*/

using namespace std;

int main() {
	stack<int> s;
	int k,input;
	int input_sum = 0; 
	cin >> k;
	for(int i=0; i<k; i++){
		cin >> input; //입력받고 
		
		if(input!=0) { //0이 아니면 입력값을 스택에 삽입  
			
			s.push(input);
			
		}
		else {//입력값이 0이면 스택에 가장 위에있는 원소를 삭제  
			s.pop();
		}
			
	}
	int size = s.size();
	for(int i=0; i<size; i++){
		input_sum+=s.top(); //sum 에 스택 가장 위에 있는 값을 더해줌 
		s.pop(); //더했으면 삭제  
		
	}
	cout << input_sum;
	 
	return 0;
}