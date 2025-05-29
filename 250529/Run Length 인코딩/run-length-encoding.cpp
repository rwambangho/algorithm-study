#include <iostream>
#include <string>

using namespace std;



int main() {
    string A;
    cin >> A;
    string result="";
    char prev = A[0];
    int count=1;
    
    
    for(int i=1; i<A.length(); i++){
        if(A[i]==prev){
            count++;

        }
        else{
            result+=prev;
            result+=to_string(count);
            prev=A[i];
            count=1;
        }
    }
    result+=prev;
    result+=to_string(count);
    cout << result.length() << endl << result;

    // Please write your code here.

    return 0;
}
