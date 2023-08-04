#include<iostream>
#include<queue>
#include<string>
#define endl '\n'

using namespace std;

int main() {
	queue<int> q;
	int n;
	int x;
	int result = 0;
	string order;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> order;
		
		if (order == "push") { //push X : 정수 X를 큐에 넣는 연산이다.
			cin >> x;
			q.push(x); //데이터 추가

		}
		else if (order == "pop") { //pop : 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
			if (q.empty()==true) {
				result = -1;
				cout << result << endl;
			}
			else {
				result = q.front();
				cout << result << endl;//최상위 데이터반환
				q.pop(); //front데이터 삭제
			}
		}
		else if (order == "size") { //size: 큐에 들어있는 정수의 개수를 출력한다.
			cout << q.size() << endl; //큐의 사이즈 반환

		}
		else if (order == "empty") { //empty : 큐가 비어있으면 1, 아니면 0을 출력한다.
			if (q.empty()==true) {
				cout << true << endl;
			}
			else
				cout << false << endl;

		}
		else if (order == "front") { //front : 큐의 가장 앞에 있는 정수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
			
			if (q.empty()==true) {
				result = -1;
				cout << result << endl;
			}
			else {
				result = q.front();
				cout << result << endl;
			}
		}
		else if (order == "back") { //back : 큐의 가장 뒤에 있는 정수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
			
			if (q.empty()==true) {
				result = -1;
				cout << result << endl;
			}
			else {
				result = q.back();
				cout << result << endl; //제일 마지막 데이터반환
			}
		}
	}
	return 0;
}