#include <iostream>
using namespace std;

int main() {
    int n;
    // Please write your code here.
    cin >> n;
    for(int i=0; i<n; i++){
        if((i+1)%2==0){
            for(int j=0; j<i+1; j++){
                cout << "*" << " ";
            }
            
        }
        else{
            cout << "*" << "";

        }
        cout << endl;    

    }
    
    return 0;
}


