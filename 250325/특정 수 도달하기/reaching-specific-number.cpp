#include <iostream>
using namespace std;

int main() {
    int arr[9];
    int total=0;
    int cnt=0;
    for(int i=0; i<10; i++){
        cin >> arr[i];
    }
   
    for(int i=0; i<10; i++){
        if(arr[i] < 250){
            total+=arr[i];
            cnt+=1;
        }
        else{
            break;
        }
        
    }
    double avg = (double)total/cnt;
    cout<<fixed;
    cout.precision(1);
    cout << total << " " << avg;

   
    
    // Please write your code here.
    return 0;
}

