#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i=1; i<n+1; i++){
        if(i%2==0 || i%3==0){
            cout << 1 << " ";
        }
        else{
            cout << 0 << " ";
        }
    }
    return 0;
}