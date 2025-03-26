#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    
    int cnt=0;
    for(int i=0; i<n; i++){
        int arr[4];
        int total=0;
        for(int i=0; i<4; i++){
            cin >> arr[i];
            total+=arr[i];

        } 
        if(total/4 >= 60){
            cout << "pass" << endl;
            cnt++;
        }
        else{
            cout << "fail" << endl;
        }
        
    }
      
        
    
    cout << cnt;

    // Please write your code here.
    return 0;
}

