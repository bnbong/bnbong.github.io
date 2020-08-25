#include <stdio.h>

int main(){
   int N;
   scanf("%d" , &N);
   for(int i = 0; i < 2*N - i - 1; i++){
      for(int j = 0; j < i; j++){
         printf("b");
      }
      for(int j = 0; j < 2*N - 2*i - 1; j++){
         printf("*");
      }
   printf("\n");
   }
   for(int i = 1; i < 2*N - i - 1; i++){
      for(int j = 0; j < N - i - 1; j++){
         printf("b");
      }
      for(int j = 0; j < 2*i + 1; j++){
         printf("*");
      }
   printf("\n");
   }
}
