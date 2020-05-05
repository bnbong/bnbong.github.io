#include <stdio.h>

int main(void){
	int a;
	scanf("%d",&a);
	for(int i = 0 ; i < a ; i++){
		for(int j = a-1 ; j > i  ; j--){
			printf(" ");
		}
		for(int k = 0 ; k < i+1 ; k++){
			if(k==1){
				break;
			}
			else{
				printf("*");
			}
		}
		for(int z = 0 ; z < i ; z++){
			printf(" ");
		}
		for(int y = 0; y < i-1 ; y++){
			printf(" ");
		}
		for(int x = 0 ; x < i+1 ; x++){
			if(x==1){
				break;
			}
			else if(i==0){
				printf("");
			}
			else{
				printf("*");
			}
		}
		printf("\n");
	}
}
