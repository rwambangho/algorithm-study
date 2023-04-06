#include<iostream>
#include<algorithm> 
#define endl '\n'
/*
n개의 수가 주어질때 오름차순정렬하라  
*/
using namespace std;

int main() {
	vector<int> input(1000000);
	int n;
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> input[i];
		
	}
	input.resize(n);
	sort(input.begin(), input.end());
	
	
	for(int i=0; i<n; i++){
		cout << input[i] << endl;
	
	}
	
	
	return 0;
} 