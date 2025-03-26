#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    for(int i=sizeof(arr)/sizeof(arr[0])-1; i>-1; i--){
        if(arr[i]%2==0){
            cout << arr[i] << " ";
        }
        
    }
    // Please write your code here.
    return 0;
}




