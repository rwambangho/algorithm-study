#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n=0;
    cin >> n;
    for(int i=1; i<=n; i++){
        if(i%3==0){
            cout << 0 << " ";
        }
        else if(i/10==3 || i/10==6 || i/10==9){
            cout << 0 << " ";
        }
        else if(i%10==3 || i%10==6 || i%10==9){
            cout << 0 << " ";
        }
        else{
            cout << i << " ";
        }
    }
    
    return 0;
}