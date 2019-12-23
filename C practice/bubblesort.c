#include <stdio.h>
void swap(int *, int *);
void bubble(int a[], int n);


int main()
{
	int a[] = {7,3,66,3,-5,22,77,2};
	bubble(a,8);
	for(int i = 0; i < 8; i++)
		printf("[%d]", a[i]);
	printf("\n");
	return 0;
}

void bubble(int a[], int n)
{
	int i,j;
	for(i=0; i<n-1; ++i){
		for(j=n-1; j>i; --j){
			if(a[j-1] > a[j]) {
				swap(&a[j-1], &a[j]);
				//swap(a+(j-1), a+j);
			}
		}
	}
}

void swap(int *p, int *q)
{
	int temp;
	temp = *p;
	*p = *q;
	*q = temp;
}
