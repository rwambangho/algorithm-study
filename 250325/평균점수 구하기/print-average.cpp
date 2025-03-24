#include <iostream>
using namespace std;

int main() {
    double arr[8];
    double total=0;
    
    for(int i=0; i<8; i++){
        cin >> arr[i];
        total+=arr[i];
    }
    
    
    cout << fixed;
    cout.precision(1);
    cout << total/8 << endl; 
    // Please write your code here.
    return 0;
}

