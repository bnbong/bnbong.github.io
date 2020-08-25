#include <stdio.h> 

int main(void) {
	int a;
	scanf("%d", &a);
	if (90 <= a && a<= 100) printf("A");
	else if (80 <= a && a <= 89) printf("B");
	else if (70 <= a && a <= 79) printf("C");
	else if (60 <= a && a <= 69) printf("D");
	else{
		printf("F");
	}
	return 0;
}
