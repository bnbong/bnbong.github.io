#include <stdio.h>

int main(void){
	int a[5] = {};
	int b;
	int c = 0;
	for(int i = 0 ; i < 5 ; i++){
		scanf("%d",&b);
		if(b<40){
			a[i] = 40;
		}
		else{
			a[i] = b;
		}
		c = c + a[i];
	}
	printf("%d",c/5);
}
