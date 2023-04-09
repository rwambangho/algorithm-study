#include<iostream>
#define endl '\n'
/*
2원짜리와 5원짜리로 거스름돈 준다 동전의 최소개수
거슬러 줄 수 없으면 -1출력  
몫이 최소가 되게 한다. 
1. 5로 나눠 떨어지면 몫 출력
2. 안 나눠 떨어질때 나머지가 짝수이면 몫을 저장하고 나머지를 2로나눈  몫을 저장 
3. 나머지가 홀수이면 5를 더하고 2로 나눠서 몫을 저장   
*/
using namespace std;

int main() {
	int n;
	cin >> n; 
	int cnt = 0; //동전개수  
	int temp = 0;//나머지값  
	temp = n%5;
	 
	
	while(n>0) {
		
		if(temp==0){ //5로 나눠서 떨어지면 몫을 저장    
			cnt += n/5;
			break;
		}
		
		else {//5로 안나눠 떨어질때 
			if(n==1 || n==3){
			 	 cnt = -1;
			 	 break;
			} 
			else
				
			 		
			if(temp%2==0) { //나머지가 짝수이면 
				cnt += n/5;  //일단 몫을 저장하고  
				cnt += temp/2; //나머지를 2로 나눠서 몫을 저장 
				break;
			}
			
			else { //나머지가 홀수이면
				temp += 5; //나머지에 5를 더해주고  
				cnt += temp/2; //2로 나눠서 몫을 저장
				n -= temp; //입력값에서 나머지값 뺴주고  
				cnt += n/5;//5로 나눈 몫을 더해준다
				break; 
			}
		}  
	}
	cout << cnt << endl;
	
	return 0; 
}
			
	
	 
	
	
