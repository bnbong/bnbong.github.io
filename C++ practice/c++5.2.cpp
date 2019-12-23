#include <stdio.h>

int main(void){
	int a;
	int b[200] = {};
	int c;
	int d = 0;
	scanf("%d",&a);
	scanf("%d",&b);
	
	for(int i = 0 ; i < a ; i++){
		scanf("%d",&c);
		if(b[i]==c){
			d = d + 1;
		}
		else{
			d = d;
		}
	}
	printf("%d",d);
}
