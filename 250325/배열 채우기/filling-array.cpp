#include <iostream>
using namespace std;

int main() {
    int arr[10];
    int cnt =0;
    for(int i=0; i<10; i++){
        cin >> arr[i];
        cnt++;
        if(arr[i] == 0){
            cnt--;
            break;
        }

    }
    
    for(int i=cnt-1; i>-1; i--){
        cout << arr[i] << " ";
    }
    // Please write your code here.
    return 0;
}