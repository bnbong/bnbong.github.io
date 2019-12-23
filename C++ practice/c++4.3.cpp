#include <stdio.h>

int main(void){
	int a, b;
	scanf("%d",&a);
	for(int i = 0 ; i < a ; i++){
		for(int j = 0 ; j < i + 1 ; j++){
			printf("*");
		}
		printf("\n");
	}
}
