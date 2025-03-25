#include <iostream>
using namespace std;

int main() {
    int arr[10];
    int cnt =0;
    int total=0;
    for(int i=0; i<10; i++){
        cin >> arr[i];
        if(arr[i]==0){
            break;
        }

        if(arr[i]%2==0){
            total+=arr[i];
            cnt++;
        }
    }
    cout << cnt << " " << total;
    
    // Please write your code here.
    return 0;
}