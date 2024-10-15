#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,num =0;
    cin >> n;
    
    for(int i=0; i<n; i++){
        cin >> num;
        if(num%3==0 && num%2!=0){
            cout << num << endl ;
        }
        
    }
   
    return 0;
    
    }