#include <stdio.h>

int main(void){
	int a,b,c;
	scanf("%d %d %d", &a,&b,&c);
	if(a==b && b==c){
		printf("%d",10000 + a*1000);
	}
	else if(a==b){
		printf("%d",1000+a*100);
	}
	else if(b==c){
	    printf("%d",1000+b*100);
	}
	else if(a==c){
		printf("%d",1000+a*100);
	}
	else{
		if(a<c){
			if(b<a){
				printf("%d",c*100);
			}
			else if(c<b){
				printf("%d",b*100);
			}
			else{
				printf("%d",c*100);
			}
		}
		if(c<a){
			if(b<c){
				printf("%d",a*100);
			}
			else if(a<b){
				printf("%d",b*100);
			}
			else{
				printf("%d",a*100);
			}
		}
	}
}
