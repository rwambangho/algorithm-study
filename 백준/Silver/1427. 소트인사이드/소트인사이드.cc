#include<iostream>
#include <algorithm>
#define endl '\n'
/*
수가 주어지면 내림차순 정렬
*/

using namespace std;


bool compare(int i, int j) {
	
	return i > j;
}

int main() {
	string input;
	cin >> input;
	sort(input.begin(), input.end(), compare);
	for(int i=0; i<input.size(); i++) {
		cout << input[i];
	}
	
	return 0;
}
