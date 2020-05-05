#include <stdio.h>

int main(void){
	int num1, num2, num3, result;
	printf("¹®Á¦1");
	scanf("%d %d %d", &num1, &num2, &num3);
	result = num1 * num2 + num3;
	printf("%d * %d + %d = %d \n", num1, num2, num3, result);
	return 0;
}
