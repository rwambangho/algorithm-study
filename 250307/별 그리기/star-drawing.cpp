#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.
    for(int i=0; i<n; i++){
        for(int j=0; j<n-1-i; j++){
            cout << " ";
        }

        for(int j=0; j<i*2+1; j++){
            cout << "*";
        }
        cout << endl;



    }

    for(int i=0; i<n-1; i++){
        for(int j=0; j<i+1; j++){
            cout << " ";
        }

        for(int j=0; j<n*2-(3+i*2); j++){
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}
