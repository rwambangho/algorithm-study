#include<iostream>
#include<queue>
using namespace std;


//배열에 자연수 x를 넣는다.
//배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
//프로그램은 처음에 비어있는 배열에서 시작하게 된다.
int main() {
	ios::sync_with_stdio(false);cin.tie(NULL);

	int n,x;
	cin >> n;//연산의 개수
    priority_queue <int, vector <int>, greater <int>> q;
	
	for (int i = 0; i < n; i++) {
		cin >> x;
		if (x != 0)
			q.push(x); //0이 아니면 자연수를 넣는다
		else {
			if (q.empty()) {
				cout << 0 << '\n';
			}
			else {
				cout << q.top() << '\n'; //루트노드
				q.pop();//루트제거
			}
		}
	}
	return 0;
}