#include <iostream>
using namespace std;

int main() {
    char n[10];
    for(int i=0; i<10; i++){
        cin >> n[i];
    }
    for(int i=9; i>-1; i--){
        cout << n[i];
    }
    // Please write your code here.
    return 0;
}
