#include<iostream>
#include<algorithm>
#include<string>


using namespace std;


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0); //입출력을 묶어준다 
    string a,b,cnt1,cnt2; //입력받을값과 입력값을 저장할 변수를 생성 
	int n; 
	cin >> n;  
	
	for(int i=0; i<n; i++) {
		
		cin >> a >> b;  
		cnt1 = a; 
		cnt2 = b;
	
		sort(a.begin() , a.end()); //정렬
		sort(b.begin() , b.end());
				
				
			if(a==b) 
					cout << cnt1 << " & " << cnt2 << " are anagrams."<< "\n";
				
			else
				 	cout << cnt1 << " & " << cnt2 << " are NOT anagrams."<< "\n";
		}
		return 0; 
}
			
	

