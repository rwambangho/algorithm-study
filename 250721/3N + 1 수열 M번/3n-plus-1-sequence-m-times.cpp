#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n,m;
    
    cin >> m;
    for(int i=0; i<m; i++){
        int cnt=0;
        cin >> n;
    
        while(n!=1){
            if(n%2==0){
                n=n/2;
            }
            else{
                n=n*3+1;
            }
            cnt+=1;
        }
        cout << cnt << endl;
    }
    return 0;
}


