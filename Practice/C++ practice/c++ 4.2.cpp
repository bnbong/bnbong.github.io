#include <stdio.h>

int main(void){
	int a ,countone = 0, counttwo = 0;
	scanf("%d",&a);
	for(int i = 0 ; i < a ; i++){
		int b;
		scanf("%d",&b);
		if(b == 1){
			countone++;
		}
		if(b == 0){
			counttwo++;
		}
	}
	if(countone < counttwo){
			printf("Junhee is not cute!");
		}
	if(countone > counttwo){
			printf("Junhee is cute!");
		}
}
