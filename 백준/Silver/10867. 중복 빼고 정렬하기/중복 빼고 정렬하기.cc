#include <iostream>
#include <algorithm>
#include <vector>
#define endl '\n'

/*
  중복 뺴고 정렬하기
*/

using namespace std;

int main() {
	int i, j, n, input;
	vector<int> v;
	 
	
	 cin >> n; //입력할 수의 개수 
	for(i=0; i<n; i++) {
	 
	 cin >> input;
	 v.push_back(input);
	}
	
	sort(v.begin(), v.end());//오름차순 정렬 
	v.erase(unique(v.begin(), v.end()), v.end());
	 for(j=0; j<v.size(); j++) {
	 	cout << v[j] << ' ';
	 }
	return 0; 
}