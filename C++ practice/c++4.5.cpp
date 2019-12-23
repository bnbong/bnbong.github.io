#include <stdio.h>

int main(void){
	int a;
	scanf("%d",&a);
	for(int x = 0 ; x < a ; x++){
		for(int y = 0 ; y < x ; y ++){
			printf(" ");
		}
		for(int g = 0; g<2*a-1-2*x ; g ++){
			printf("*");
		}
		if(x==a-2){
			break;
		}
		else{
			printf("\n");
		}
	}
	for(int i = -1 ; i < a ; i++){
		if(a==1){
			break;
		}
		for(int j = a-1 ; j > i  ; j--){
			printf(" ");
		}
		for(int k = 0 ; k < i+1 ; k++){
			printf("*");
		}
		for(int z = 0 ; z < i ; z++){
			printf("*");
		}
		printf("\n");
	}
}
