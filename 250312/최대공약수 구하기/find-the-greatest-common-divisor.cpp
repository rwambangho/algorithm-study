#include <iostream>

using namespace std;



void num(int n, int m){
    for(int i=m; i>0; i--){
        if(n%i==0 && m%i==0){
            cout << i;
            break;
        }
        else{
            continue;
        }
    }

}
    

int main() {
    int n, m;
    cin >> n >> m;

    // Please write your code here.
    num(n,m);
    
        

    return 0;
}


            

