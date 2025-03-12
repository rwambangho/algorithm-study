#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;
    int cnt = 1;
    // Please write your code here.
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(cnt != 10){
                cout << cnt << " ";
                cnt+=1;
            }
            else{
                cnt = 1;
                cout << cnt << " ";
                cnt += 1;
            }
        }
        cout << endl;
    }

    return 0;
}

