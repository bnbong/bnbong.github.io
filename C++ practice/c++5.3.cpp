#include <stdio.h>

int main(void){
	int a[28] = {};
	int b;
	int c[30] = {};
	for(int i = 0 ; i < 28 ; i++){
		a[i] = {i+1};
		scanf("%d",&b);
		if(a[i] != b){
			c[i] = a[i];
		}
	}
	printf("%d\n",c[30]);
}
