#include <stdio.h>

int main (void){
	int n;
	int x;
	int c;
	scanf("%d %d", &n, &x);
	for(int i = n ; i > 0 ; i--){
		scanf("%d",&c);
		if(x > c){
			printf("%d ", c);
		}
	}
}
