#include <iostream>
using namespace std;

int main() {
    int arr[10];
    int cnt = 0;
    int total=0;
    for(int i=0; i<10; i++){
        cin >> arr[i];
        if(arr[i] == 0){
            break;
        }
        cnt++;
    }
    for(int i=0;i<cnt;i++){
        total+=arr[i];
    }
    double avg=(double)total/cnt;
    cout << fixed;
    cout.precision(1);
    cout << total << " " << avg;
    // Please write your code here.
    return 0;
}



