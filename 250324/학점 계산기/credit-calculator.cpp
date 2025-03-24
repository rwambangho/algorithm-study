#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    double arr[5];
    double total=0;
    // Please write your code here.
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    for(int i=0; i<n; i++){
        total+=arr[i];
    }
    double val = total/n;
    cout << fixed;
    cout.precision(1);
    cout << val << endl;
    if(val>=4.0){
        cout << "Perfect";
    }
    else if(val >= 3.0){
        cout << "Good";
    
    }
    else{
        cout << "Poor";
    }
    return 0;
}