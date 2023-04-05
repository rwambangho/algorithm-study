#include<iostream>
#include<queue> 
#define endl '\n'
/*
1-N까지의 번호
카드가 한장 남을 때까지 
제일 위에 있는 카드를 버리고 그다음카드를 제일 아래 카드 밑으로 옮긴다  
1 .1부터 N까지 반복문으로 큐에 숫자 넣고 
 2. while로 카드 한장남는다는 조건걸어서 pop(), push()쓰고 
 3. 남아있는 카드 출력 
 
*/
using namespace std;

int main() {
	queue<int> q;
	int num;
	
	cin >> num;
	
	for(int i=1; i<=num; i++) { //1부터 N까지의 카드  
		q.push(i); 
		}	
	
	while(q.size()>1) { 
		q.pop(); //맨앞의 원소를 지우고  
		q.push(q.front()); //그다음 원소를 맨뒤로  
		q.pop(); //옮기고 남아있는 원소를 삭제
		  
			 
	}
	
	cout << q.front() << endl;
	
	return 0;
}