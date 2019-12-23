#include <stdio.h>

int main(void){
	int max = 0, count;
	for(int i = 0 ; i < 9 ; i ++){
		int a;
		scanf("%d",&a);
		if(max < a){
			max = a;
			count = i + 1;
		}
	}
	printf("%d\n%d", max, count);
	return 0;
}
