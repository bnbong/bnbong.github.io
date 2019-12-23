#include "main_header.h"

typedef struct Node{
    int val;
    struct Node *prev;
    struct Node *next;
} Node;

typedef struct {
    Node *head;
    int size;
} DLL;

Node *newnode(int n){
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->val = n;
    temp->prev = NULL;
    temp->next = NULL;
    return temp;
}

DLL *newDLL(){
    DLL *temp = (DLL *)malloc(sizeof(DLL));
    temp->head = NULL;
    temp->size = 0;
    return temp;
}


char* Multiply(char *arr1, char *arr2){ //곱셈연산
        int buho = 1; //buho 가 1이면 양수, 0 이면 음수
        char *silsu1, *silsu2;
        char *sosu1, *sosu2;
        int *num1, *num2;
        int *calculate;
        char *resultreverse, *result;
        unsigned long long i,j,k,l;
        unsigned long long lengthofsosu = 0;

        while(arr1[0] == '0'){
            if((arr1[1] == 0) || (arr1[1] == '.'))break;
            memmove(arr1,arr1+1,strlen(arr1));
        }
        while(arr2[0] == '0'){
            if((arr2[1] == 0) || (arr2[1] == '.'))break;
            else memmove(arr2,arr2+1,strlen(arr2));
        }
        if(arr1[0] == '-'){
            while(arr1[1] == '0'){
            if((arr1[2] == 0) || (arr1[2] == '.'))break;
            memmove(arr1+1,arr1+2,strlen(arr1-1));}
        }
        if(arr2[0] == '-'){
            while(arr2[1] == '0'){
            if((arr2[2] == 0) || (arr2[2] == '.'))break;
            memmove(arr2+1,arr2+2,strlen(arr2-1));}
        }
    
        if(arr1[0] == '-'){
            memmove(arr1,arr1+1,strlen(arr1));
            if(arr2[0] > '0'){buho = 0;}
            else{memmove(arr2,arr2+1,strlen(arr2));}
        }
        else if(arr2[0] == '-'){
            memmove(arr2,arr2+1,strlen(arr2));
            buho = 0;}
    
        silsu1 = strtok(arr1,".");
        sosu1 = strtok(NULL,".");
        silsu2 = strtok(arr2,".");
        sosu2 = strtok(NULL,".");
    
        if(sosu1 == NULL){sosu1 = "0";}
        if(sosu2 == NULL){sosu2 = "0";}
        lengthofsosu = strlen(sosu1) + strlen(sosu2);
        
        num1 = (int*)malloc((strlen(silsu1)+strlen(sosu1))*sizeof(int));
        num2 = (int*)malloc((strlen(silsu2)+strlen(sosu2))*sizeof(int));
        calculate = (int*)malloc((strlen(silsu1)+strlen(silsu2)+strlen(sosu1)+strlen(sosu2))*sizeof(int));
        result = (char*)malloc((strlen(silsu1)+strlen(silsu2)+strlen(sosu1)+strlen(sosu2))*sizeof(char)+2);
        memset(calculate,0,strlen(silsu1)+strlen(silsu2)+strlen(sosu1)+strlen(sosu2));
        memset(result,0,strlen(silsu1)+strlen(silsu2)+strlen(sosu1)+strlen(sosu2)+1);
    
        for(i = 0; i < strlen(silsu1); i++){
            num1[i] = silsu1[i] - '0';
        }
        for(i = strlen(silsu1); i < strlen(silsu1)+strlen(sosu1); i++){
            num1[i] = sosu1[i-strlen(silsu1)] - '0';
        }
        for(i=0; i < strlen(silsu2); i++){
            num2[i] = silsu2[i] - '0';
        }
        for(i = strlen(silsu2); i < strlen(silsu2)+strlen(sosu2); i++){
            num2[i] = sosu2[i-strlen(silsu2)] - '0';
        }

            if((strlen(silsu1)+strlen(sosu1)) >= (strlen(silsu2)+strlen(sosu2))){
            k = 0;
            
            for(i = 1; i <= (strlen(silsu2)+strlen(sosu2)); i++){
                l = -1;
                for(j = 1; j <= (strlen(silsu1)+strlen(sosu1)); j++){
                    l++;
                    calculate[k+l] += num2[(strlen(silsu2)+strlen(sosu2))-i] * num1[(strlen(silsu1)+strlen(sosu1))-j];
                    if(calculate[k+l] >= 10){
                        calculate[k+l+1] += calculate[k+l] / 10;
                        calculate[k+l] -= (calculate[k+l] / 10) * 10;
                    }
                }
                
                k++;
            }
            
        }
        else{
                    k = 0;
            
            for(i = 1; i <= (strlen(silsu1)+strlen(sosu1)); i++){
                l = -1;
                for(j = 1; j <= (strlen(silsu2)+strlen(sosu2)); j++){
                    l++;
                    calculate[k+l] += num1[(strlen(silsu1)+strlen(sosu1))-i] * num2[(strlen(silsu2)+strlen(sosu2))-j];
                    if(calculate[k+l] >= 10){
                        calculate[k+l+1] += calculate[k+l] / 10;
                        calculate[k+l] -= (calculate[k+l] / 10) * 10;
                    }
                }
                
                k++;
            }
            
        }
        
    
        if(buho == 0){
        for(i = 0; i < strlen(sosu1) + strlen(sosu2); i++){
            result[i] = calculate[i] + '0';
        }
        result[i] = '.';
        i++;
        for(j = 0; j < strlen(silsu1)+strlen(silsu2)-1; j++){
            result[i+j] = calculate[i+j-1] + '0';
        }
        if(calculate[i+j-1] != 0){
            result[i+j] = calculate[i+j-1] + '0';
            result[i+j+1] = '-';
        }else{
            result[i+j] = '-';
        }
        }
        else{
        for(i = 0; i < strlen(sosu1) + strlen(sosu2); i++){
            result[i] = calculate[i] + '0';
        }
        result[i] = '.';
        i++;
        for(j = 0; j < strlen(silsu1)+strlen(silsu2)-1; j++){
            result[i+j] = calculate[i+j-1] + '0';
        }
        if(calculate[i+j-1] != 0){
            result[i+j] = calculate[i+j-1] + '0';
        }}
    
        resultreverse = (char*)malloc(strlen(result)*sizeof(char)+1);
            memset(resultreverse,0,strlen(result));
            
            for(i = 0; i < strlen(result); i++){
                resultreverse[i] = result[strlen(result)-i-1];
            }
            
            i = 1;
            
            while(resultreverse[strlen(result)-i] == '0'){
                if(resultreverse[strlen(resultreverse)-i+1] == '\0'){
                    resultreverse[strlen(result)-i] = '\0';
                }
                i++;
            }if(resultreverse[strlen(result)-i] == '.'){resultreverse[strlen(result)-i] = '\0';}
    
    free(result);
    
    return resultreverse;
}

char* Plus(char *arr1, char *arr2){ //덧셈연산
    char *silsu1, *silsu2;
    char *sosu1, *sosu2;
    char *resultsilsu = NULL, *resultsosu = NULL, *result, *temp;
    
    unsigned long long i,j;
    
    if(arr1[0] < '0' && arr2[0] < '0'){
        memmove(arr1,arr1+1,strlen(arr1));
        memmove(arr2,arr2+1,strlen(arr2));
        temp = Plus(arr1,arr2);
        result = (char*)malloc(strlen(temp)*sizeof(char)+2);
        result[0] = '-';
        for(i = 1; i <= strlen(temp); i++){
            result[i] = temp[i-1];
        }
        return result;
        
    }else if(arr1[0] < '0' && arr2[0] >= '0'){
                memmove(arr1,arr1+1,strlen(arr1));
                return Minus(arr2,arr1);
            }else if(arr1[0] >= '0' && arr2[0] < '0'){
                return Minus(arr1,arr2);}
        
        while(arr1[0] == '0'){
            if((arr1[1] == 0) || (arr1[1] == '.'))break;
            memmove(arr1,arr1+1,strlen(arr1));
        }
        while(arr2[0] == '0'){
            if((arr2[1] == 0) || (arr2[1] == '.'))break;
            else memmove(arr2,arr2+1,strlen(arr2));
        }
        if(arr1[0] == '-'){
            while(arr1[1] == '0'){
            if((arr1[2] == 0) || (arr1[2] == '.'))break;
            memmove(arr1+1,arr1+2,strlen(arr1-1));}
        }
        if(arr1[0] == '-'){
            while(arr2[1] == '0'){
            if((arr2[2] == 0) || (arr2[2] == '.'))break;
            memmove(arr2+1,arr2+2,strlen(arr2-1));}
        }
    
    silsu1 = (char*)malloc(strlen(arr1)*sizeof(char)+1);
    silsu2 = (char*)malloc(strlen(arr2)*sizeof(char)+1);
    sosu1 = (char*)malloc(strlen(arr1)*sizeof(char)+1);
    sosu2 = (char*)malloc(strlen(arr2)*sizeof(char)+1);
    
    silsu1 = strtok(arr1,".");
    sosu1 = strtok(NULL,".");
    silsu2 = strtok(arr2,".");
    sosu2 = strtok(NULL,".");
    
    if(sosu1 == NULL){sosu1 = "0";}
    if(sosu2 == NULL){sosu2 = "0";}

    int *intsilsu1, *intsilsu2, *intsosu1, *intsosu2;
    
    intsilsu1 = (int*)malloc(strlen(silsu1)*sizeof(int)+1);
    intsilsu2 = (int*)malloc(strlen(silsu2)*sizeof(int)+1);
    intsosu1 = (int*)malloc(strlen(sosu1)*sizeof(int));
    intsosu2 = (int*)malloc(strlen(sosu2)*sizeof(int));
    
    intsilsu1[0] = 0;
    intsilsu2[0] = 0;

    for(i = 0;i<strlen(silsu1);i++){
        intsilsu1[i+1] = silsu1[i] - '0';
    }
    for(i = 0;i<strlen(silsu2);i++){
        intsilsu2[i+1] = silsu2[i] - '0';
    }
    for(i=0;i<strlen(sosu1);i++){
        intsosu1[i] = sosu1[i] - '0';
    }
    for(i=0;i<strlen(sosu2);i++){
        intsosu2[i] = sosu2[i] - '0';
    }

    if(strlen(sosu1) >= strlen(sosu2)){
        
        for(i = 1; i < strlen(sosu2); i++){
            intsosu1[strlen(sosu2)-i] += intsosu2[strlen(sosu2)-i];
            if(intsosu1[strlen(sosu2)-i] >= 10){
                intsosu1[strlen(sosu2)-i] -= 10;
                intsosu1[strlen(sosu2)-(1+i)] += 1;}
        }
        
        intsosu1[0] += intsosu2[0];
        if((intsosu1[0]) >= 10){
            intsosu1[0] -= 10;
            intsilsu1[strlen(silsu1)]++;}

        
        resultsosu = (char*)malloc((strlen(sosu1)+1)*sizeof(char));
        memset(resultsosu,0,(strlen(sosu1)+1)*sizeof(char));
        
        resultsosu[strlen(sosu1)] = '\0';
        for(i = 0; i < strlen(sosu1); i++){resultsosu[i] = intsosu1[i] + '0';}


    }
    else if(strlen(sosu1) < strlen(sosu2)){
        for(i = 1; i < strlen(sosu1); i++){
            intsosu2[strlen(sosu1)-i] += intsosu1[strlen(sosu1)-i];
            if((intsosu2[strlen(sosu1)-i]) >= 10){
                intsosu2[strlen(sosu1)-i] -= 10;
                intsosu2[strlen(sosu1)-1-i]++;}
        }
        
        intsosu2[0] += intsosu1[0];
        if((intsosu2[0]) >= 10){
            intsosu2[0] -= 10;
            intsilsu1[strlen(silsu1)]++;}
        
        resultsosu = (char*)malloc((strlen(sosu2)+1)*sizeof(char));
        for(i = 0; i < strlen(sosu2); i++){resultsosu[i] = intsosu2[i] + '0';}
        resultsosu[strlen(sosu2)] = '\0';
    }
    
    
    if(strlen(silsu1) >= strlen(silsu2)){
        
        for(i = 0; i <= strlen(silsu2); i++){
            intsilsu1[strlen(silsu1)-i] += intsilsu2[strlen(silsu2)-i];
            if(intsilsu1[strlen(silsu1)-i] >= 10){
                intsilsu1[strlen(silsu1)-i] -= 10;
                intsilsu1[strlen(silsu1)-i-1]++;}
        }
        
        for(i = 0; i <= strlen(silsu1); i++){
            if(intsilsu1[strlen(silsu1)-i] >= 10){
            intsilsu1[strlen(silsu1)-i] -= 10;
            intsilsu1[strlen(silsu1)-i-1]++;}
        }
        
        if(intsilsu1[0] == 0){
        resultsilsu = (char*)malloc(strlen(silsu1)*sizeof(char)+1);
            for(i = 0; i < strlen(silsu1); i++){
                resultsilsu[i] = intsilsu1[i+1] + '0';
            }
        }
        else{
            resultsilsu = (char*)malloc(strlen(silsu1)*sizeof(char)+2);
            for(i = 0; i < strlen(silsu1)+1; i++){
            resultsilsu[i] = intsilsu1[i] + '0';
                }
            }
                
    }
    else{
        
        for(i = 0; i < strlen(silsu1); i++){
            intsilsu2[strlen(silsu2)-i] += intsilsu1[strlen(silsu1)-i];
            if(intsilsu2[strlen(silsu2)-i] >= 10){intsilsu2[strlen(silsu2)-i] -= 10; intsilsu2[strlen(silsu2)-i-1]++;}
        }
        
        for(i = 0; i <= strlen(silsu2); i++){
            if(intsilsu2[strlen(silsu2)-i] >= 10){
            intsilsu2[strlen(silsu2)-i] -= 10;
            intsilsu2[strlen(silsu2)-i-1]++;}
        }
        
        if(intsilsu2[0] == 0){
        resultsilsu = (char*)malloc(strlen(silsu2)*sizeof(char)+1);
            for(i = 0; i < strlen(silsu2); i++){
                resultsilsu[i] = intsilsu2[i+1] + '0';
            }
        }
        else{
            resultsilsu = (char*)malloc(strlen(silsu2)*sizeof(char)+2);
            for(i = 0; i < strlen(silsu2)+1; i++){
            resultsilsu[i] = intsilsu2[i] + '0';
                }
            }
    }
    
    result = (char*)malloc((strlen(resultsilsu)+strlen(resultsosu))*sizeof(char)+1);
    memset(result,0,(strlen(resultsilsu)+strlen(resultsosu))*sizeof(char)+1);
    
    i = 1;
    j = strlen(resultsosu);
    
    while(resultsosu[j-i+1] == '\0'){
        if(resultsosu[j-i] == '0'){resultsosu[j-i] = '\0';}
        i++;
        if(i > j){break;}
    }
    for(i = 0; i < strlen(resultsilsu); i++){
        result[i] = resultsilsu[i];
    }
    if(resultsosu[0] != '\0'){
        result[i] = '.';
        i++;
        for(j = 0; j < strlen(resultsosu); j++){
            result[i+j] = resultsosu[j];
        }
    }else{result[i] = '\0';}
    return result;
    }

char* Minus(char *a1, char *a2){ //뺄셈연산
 
 char *arr1, *arr2;
 arr1 = (char*)malloc(strlen(a1)*sizeof(char)+1);
 arr2 = (char*)malloc(strlen(a2)*sizeof(char)+1);
 int reverse = 1;
 char *silsu1, *silsu2;
 char *sosu1, *sosu2;
 char *resultsilsu = NULL, *resultsosu = NULL, *result;
 unsigned long long i,j;
 char *temp;
 
 strcpy(arr1,a1);
 strcpy(arr2,a2);
 
 /* 음수양수 판별
 1. A-B = A-B (그대로 계산)
 2. A-(-B) = A+B 함수로 이관
 3. -A-B = -(A+B), 그러므로 A+B 함수로 넘겨서 앞에 -만 붙이고 Return
 4. -A-(-B) = -A+B = B-A*/
    
 if(arr1[0] < '0' && arr2[0] < '0'){
     memmove(arr1,arr1+1,strlen(arr1));
     memmove(arr2,arr2+1,strlen(arr2));
     return Minus(arr2,arr1);
 }else if(arr1[0] < '0' && arr2[0] >= '0'){
             memmove(arr1,arr1+1,strlen(arr1));
             return Minus(arr1,arr2);
         }else if(arr1[0] >= '0' && arr2[0] < '0'){
             memmove(arr2,arr2+1,strlen(arr2));
             return Plus(arr1,arr2);}
     
     while(arr1[0] == '0'){
         if((arr1[1] == 0) || (arr1[1] == '.'))break;
         memmove(arr1,arr1+1,strlen(arr1));
     }
     while(arr2[0] == '0'){
         if((arr2[1] == 0) || (arr2[1] == '.'))break;
         else memmove(arr2,arr2+1,strlen(arr2));
     }
     if(arr1[0] == '-'){
         while(arr1[1] == '0'){
         if((arr1[2] == 0) || (arr1[2] == '.'))break;
         memmove(arr1+1,arr1+2,strlen(arr1-1));}
     }
     if(arr1[0] == '-'){
         while(arr2[1] == '0'){
         if((arr2[2] == 0) || (arr2[2] == '.'))break;
         memmove(arr2+1,arr2+2,strlen(arr2-1));}
     }

 
 silsu1 = strtok(arr1,".");
 sosu1 = strtok(NULL,".");
 silsu2 = strtok(arr2,".");
 sosu2 = strtok(NULL,".");
 
 if(sosu1 != NULL){
 i = 1;
 j = strlen(sosu1);
 while(sosu1[j-i+1] == '\0'){
     if(sosu1[j-i] == '0'){sosu1[j-i] = '\0';}
     i++;
     if(i > j){break;}}
 }else sosu1 = "0";
 
 if(sosu2 != NULL){
 i = 1;
 j = strlen(sosu2);
 while(sosu2[j-i+1] == '\0'){
     if(sosu2[j-i] == '0'){sosu2[j-i] = '\0';}
     i++;
     if(i > j){break;}}
 }else sosu2 = "0";
 
 int *intsilsu1, *intsilsu2, *intsosu1, *intsosu2;
 
 intsilsu1 = (int*)malloc(strlen(silsu1)*sizeof(int)+1);
 intsilsu2 = (int*)malloc(strlen(silsu2)*sizeof(int)+1);
 intsosu1 = (int*)malloc(strlen(sosu1)*sizeof(int));
 intsosu2 = (int*)malloc(strlen(sosu2)*sizeof(int));
 
 //크기 판별
 //A>B 면 그대로 빼기, A<B면 B-A
 
 if(strlen(silsu1) < strlen(silsu2)){
     temp = Minus(a2,a1);
     result = (char*)malloc(strlen(temp)*sizeof(char)+2);
     result[0] = '-';
     for(i = 1; i <= strlen(result); i++){
         result[i] = temp[i-1];}
         return result;
 }
 
 if(strlen(silsu1) > strlen(silsu2)){
     reverse = 0;
 }else if(strlen(silsu1) == strlen(silsu2)){
     for(i = 0; i < strlen(sosu1); i++){
     if(silsu1[i] < silsu2[i]){
         temp = Minus(a2,a1);
         result = (char*)malloc(strlen(temp)*sizeof(char)+2);
         result[0] = '-';
         for(i = 1; i <= strlen(result); i++){
             result[i] = temp[i-1];}
             return result;}
         break;
         }
     }
 

 if(reverse){
     if(strlen(sosu1) >= strlen(sosu2)){
         reverse = 0;
         for(i = 0; i < strlen(sosu2); i++){
         if(sosu1[i] < sosu2[i]){
             temp = Minus(a2,a1);
             result = (char*)malloc(strlen(temp)*sizeof(char)+2);
             result[0] = '-';
             for(i = 1; i <= strlen(result); i++){
                 result[i] = temp[i-1];}
                 return result;}
             }
         }else{
         for(i = 0; i < strlen(sosu1); i++){
         if(sosu1[i] < sosu2[i]){
             temp = Minus(a2,a1);
             result = (char*)malloc(strlen(temp)*sizeof(char)+2);
             result[0] = '-';
             for(i = 1; i <= strlen(result); i++){
                 result[i] = temp[i-1];}
                 return result;}
             }
         }
    }

 
 intsilsu1[0] = 0;
 intsilsu2[0] = 0;
 
 for(i = 0;i<strlen(silsu1);i++){
     intsilsu1[i+1] = silsu1[i] - '0';
 }
 for(i = 0;i<strlen(silsu2);i++){
     intsilsu2[i+1] = silsu2[i] - '0';
 }
 for(i=0;i<strlen(sosu1);i++){
     intsosu1[i] = sosu1[i] - '0';
 }
 for(i=0;i<strlen(sosu2);i++){
     intsosu2[i] = sosu2[i] - '0';
 }

 //소수연산!!
 
 if(strlen(sosu1) >= strlen(sosu2)){
     for(i = 1; i < strlen(sosu2); i++){
         intsosu1[strlen(sosu2)-i] -= intsosu2[strlen(sosu2)-i];
         if((intsosu1[strlen(sosu2)-i]) < 0){
             intsosu1[strlen(sosu2)-i] += 10;
             intsosu1[strlen(sosu2)-1-i]--;}}
     intsosu1[0] -= intsosu2[0];
     if((intsosu1[0]) < 0){
         intsosu1[0] += 10;
         intsilsu1[strlen(silsu1)]--;}

     
     resultsosu = (char*)malloc(strlen(sosu1)*sizeof(char)+1);
     memset(resultsosu,0,strlen(sosu1)*sizeof(char)+1);
     
     for(i = 0; i < strlen(sosu1); i++){resultsosu[i] = intsosu1[i] + '0';}
     for(i = strlen(sosu1)-1; i > -1; i--){
         if((resultsosu[i] == '0')&&(resultsosu[i+1] == 0)){resultsosu[i] = 0;}
     }
 
     
 }
 else if(strlen(sosu1) < strlen(sosu2)){
     
     for(i = 1; i <= strlen(sosu2) - strlen(sosu1); i++){
         intsosu2[strlen(sosu2)-i] = 10 - (sosu2[strlen(sosu2)-i]);
         sosu2[strlen(sosu2)-i-1]++;
     }
     
     for(i = 1; i < strlen(sosu1); i++){
         intsosu2[strlen(sosu1)-i] = intsosu1[strlen(sosu1)-i] - intsosu2[strlen(sosu1)-i];
         if((intsosu2[strlen(sosu1)-i]) < 0){
             intsosu2[strlen(sosu1)-i] += 10;
             intsosu2[strlen(sosu1)-1-i]++;}
     }
     
     intsosu2[0] = intsosu2[0] - intsosu1[0];
     if((intsosu2[0]) < 0){
         intsosu2[0] += 10;
         intsilsu2[strlen(silsu2)]++;}
     
     
     resultsosu = (char*)malloc(strlen(sosu2)*sizeof(char)+1);
     memset(resultsosu,0,strlen(sosu2)*sizeof(char)+1);
     
     for(i = 0; i < strlen(sosu2); i++){resultsosu[i] = intsosu2[i] + '0';}
     
     for(i = strlen(sosu2)-1; i > -1; i--){
         if((resultsosu[i] == '0')&&(resultsosu[i+1] == 0)){resultsosu[i] = 0;}
     }
     
 }
 
 //정수연산!!
 
     for(i = 0; i < strlen(silsu2); i++){
         intsilsu1[strlen(silsu1)-i] -= intsilsu2[strlen(silsu2)-i];
         if(intsilsu1[strlen(silsu1)-i] < 0){
             intsilsu1[strlen(silsu1)-i] += 10;
             intsilsu1[strlen(silsu1)-(i+1)]--;}
     }
 
     for(i = 0; i < strlen(silsu1); i++){
         if(intsilsu1[strlen(silsu1)-i] < 0){
             intsilsu1[strlen(silsu1)-i] += 10;
             intsilsu1[strlen(silsu1)-i-1]--;}
         }
 
     if(intsilsu1[0] == 0){
     resultsilsu = (char*)malloc(strlen(silsu1)*sizeof(char)+1);
         for(i = 0; i < strlen(silsu1); i++){
             resultsilsu[i] = intsilsu1[i+1] + '0';
         }
     }else{
         resultsilsu = (char*)malloc(strlen(silsu1)*sizeof(char)+2);
         resultsilsu[0] = '-';
         for(i = 1; i < strlen(silsu1)+1; i++){
         resultsilsu[i] = intsilsu1[i] + '0';
             }
         }

 result = (char*)malloc((strlen(resultsilsu)+strlen(resultsosu))*sizeof(char)+2);
 memset(result,0,(strlen(resultsilsu)+strlen(resultsosu))*sizeof(char)+2);
 
 i = 1;
 j = strlen(resultsosu);
 
 while(resultsosu[j-i+1] == '\0'){
     if(resultsosu[j-i] == '0'){resultsosu[j-i] = '\0';}
     i++;
     if(i > j){break;}
 }
 
 for(i = 0; i < strlen(resultsilsu); i++){
     result[i] = resultsilsu[i];
 }
 if(resultsosu[0] != 0){
     result[i] = '.';
     i++;
     for(j = 0; j < strlen(resultsosu); j++){
         result[i+j] = resultsosu[j];
     }
 }

     while(result[0] == '0'){
         if((result[1] == 0) || (result[1] == '.'))break;
         memmove(result,result+1,strlen(result));}
    
     if(result[0] == '-'){
         while(result[1] == '0'){
         if((result[2] == 0) || (result[2] == '.'))break;
         memmove(result+1,result+2,strlen(result-1));}
        }
    
 
     return result;
 }

void BlankDelete(char *expr){ //식에서 빈칸지우는 함수
    unsigned long long index = 0;
    while(*expr != '\0'){
    while(*expr == ' '){memmove(expr,expr + 1,strlen(expr - index));}
    expr++; index++;}
    return;}
 
unsigned long long CheckFileLength(void){ //파일 길이 측정하는 함수
    unsigned long long templength;
    FILE *fp;
    fp = fopen("input.txt","r");
    if(fp == NULL){
    printf("File Error!\n");
    exit(1);}
    fseek(fp,0,SEEK_END);
    templength = ftell(fp);
    fclose(fp);
    return templength;}
 
char *SaveExpressionToMemory(void){ //메모리에 식 저장하는 함수
    unsigned long long length;
    length = CheckFileLength();
    FILE *fp;
    char *tempexpression;
    fp = fopen("input.txt","r");
    tempexpression = malloc(length + 1);
    memset(tempexpression,0,length + 1);
    fseek(fp,0,SEEK_SET);
    fread(tempexpression, length, 1, fp);
    fclose(fp);
    return tempexpression;}
 

void ExpressionErrorCheck(char *expr){ //식 오류 체크하는 함수
    unsigned long long i, open, close, dot;
    open = 0; close = 0; dot = 0;
    
    if((expr[0] < '0') || (expr[0] > '9')){
        if(expr[0] != ('(')){
        printf("Expression Error!\n");
        exit(1);}
        else open++;
    }
    
    for(i = 1; i < strlen(expr) - 1; i++){
        if((expr[i] < '0')){
            switch (expr[i]) {
                case '+':
                case '*':
                case '-':
                    dot = 0;
                    if(expr[i+1] < '0'){
                        if(expr[i+1] != '('){
                        printf("Expression Error!\n");
                        exit(1);}
                    }
                    break;
                case '(':
                    dot = 0;
                if((expr[i-1] > '0')||(expr[i-1] == ')')){
                    printf("Expression Error!\n");
                    exit(1);
                }
                else if(expr[i+1] < '0'){
                    if((expr[i+1] == '(')||(expr[i+1] == '-')){}
                    else{printf("Expression Error!\n"); exit(1);}
                }
                    open++;
                    break;
                case ')':
                    dot = 0;
                if((expr[i-1] < '0')){
                    if(expr[i-1]!=')'){
                        printf("Expression Error!\n");
                        exit(1);
                    }
                }
                    if(expr[i+1] >= '0'){printf("Expression Error!\n"); exit(1);}

                    close++;
                    break;
                case '.' :
                    dot++;
                    if(dot > 1){
                        printf("Expression Error!\n");
                        exit(1);
                    }
                    if((expr[i-1] < '0')||(expr[i+1] < '0')){
                            printf("Expression Error!\n");
                            exit(1);
                    }
                    break;
                default:
                    printf("Expression Error!\n");
                    exit(1);
                    break;
            }
        }
    }
    
    if(expr[strlen(expr)-1] < '0'){
        if(expr[strlen(expr)-1] != ')'){
            printf("Expression Error!\n");
            exit(1);
        }else close++;
    }
    
    if(open != close){
        printf("Expression Error!\n");
        exit(1);
    }
    return;
}

static int top = -1;

unsigned long long ConvertInfixtoPostfix(char *infix, char *stack, char **postfix){ //infix를 posftix로 바꾸는 함수
    unsigned long long index = 0,pgaro = 0,psero = 0;
  postfix[psero] = (char*)malloc(strlen(infix)*sizeof(char)+1);
  int operator;
  unsigned long long length=strlen(infix);
  char next;
  int type;
  while(index<length)
  {
    type=GetOperatorType(infix[index]);
    switch(type){
      case 10:
      push(infix[index],stack);
            if(infix[index+1] == '-'){
                if(psero > 0){
                    if(postfix[psero][0] < '0'){
                        pgaro = 0;
                        postfix[++psero] = (char*)malloc(length*sizeof(char)+1);
                        postfix[psero][pgaro++] = '0';
                    }
                    else{postfix[psero][pgaro++] = '0';}
                }
                else postfix[psero][pgaro++]='0';
            }
            
      break;
    
      case 20:
            while((next=pop(infix, stack))!='('){
                postfix[++psero] = (char*)malloc(2*sizeof(char));
                postfix[psero][0] = next;}
    break;
      
      case 40:
    if(psero > 0){
        if(postfix[psero][0] < '0'){
            pgaro = 0;
            postfix[++psero] = (char*)malloc(length*sizeof(char)+1);
            postfix[psero][pgaro++] = infix[index];
        }
        else{postfix[psero][pgaro++] = infix[index];}
    }
    else postfix[psero][pgaro++]=infix[index];
    break;
    
    case 30:
    operator=OperatorCheck(infix[index]);
            if(operator == 0){push(infix[index],stack); break;} //if문에 operator == 10 이었음, OperatorCheck함수는 0, 1, 2, 3만 리턴.
    while((top > -1) && (operator <= OperatorCheck(stack[top]))){
        postfix[++psero] = (char*)malloc(length*sizeof(char)+1);
        postfix[psero][0] = pop(infix,stack);}
        push(infix[index],stack);
            
    if(postfix[psero][0] >= '0'){
        postfix[++psero] = (char*)malloc(length*sizeof(char)+1);
        postfix[psero][0] = '0';
        pgaro = 0;}

    break;
    }
    index++;
    }
    
while(top>-1){
    postfix[++psero] = (char*)malloc(length*sizeof(char)+1);
    postfix[psero][0] = pop(infix,stack);}
    
    return psero;
}

int GetOperatorType(char operator){ //postfix변환 함수에서 연산자의 타입을 숫자를 통해 리턴하는 함수
  switch(operator){
    case '(':
      return(10);
    
    case ')':
      return(20);
    
    case '+':
    case '-':
    case '*':
      return(30);
    
    default :
      return(40);
    }
}

void push(char operator, char *stack){ //stack에 연산자를 저장(push)
    stack[++top]=operator;
}

char pop(char *infix, char *stack){ //stack으로 부터 연산자를 제거(pop)
    return(stack[top--]);
}

int OperatorCheck(char operator){ //push나 pop할 때 연산자를 체크하는 부분
    switch(operator){
        case '(':
            return(0);
        case '+':
            return(1);
        case '-':
            return(1);
        case '*':
            return(2);
        default :
            return(3);
    }
}

void FinalCalculate(char **polish, unsigned long long postfixlen, char *infix){ //곱셈, 덧셈, 뺄셈을 수행하는 함수
    unsigned long long index = -1, i;
    
    char *temp, **evaluation;
    evaluation = (char**)malloc(strlen(infix)*sizeof(char*)+1);;
    
    for(i = 0; i <= postfixlen; i++){
    evaluation[i] = malloc(strlen(infix)*sizeof(char*)+1);
    }
    
    for(i = 0; i <= postfixlen; i++){
        strcpy(evaluation[++index],polish[i]);
            if(evaluation[index][0] < '0'){
                switch(evaluation[index][0]){
                    case '+' :
                        strcpy(evaluation[index-2],Plus(evaluation[index-2],evaluation[index-1]));
                        index -= 2;
                        break;
                    case '-' :
                        strcpy(evaluation[index-2],Minus(evaluation[index-2],evaluation[index-1]));
                        index -= 2;
                        break;
                    case '*' :
                        strcpy(evaluation[index-2],Multiply(evaluation[index-2],evaluation[index-1]));
                        index -= 2;
                        break;
                }
            }
        }
    
    printf("%s\n",evaluation[index]);
    return;
}

int main(void){
    char *infix, *stack, **postfix;
    unsigned long long postfixlen;
    infix = SaveExpressionToMemory(); //memory에 infix로 표현된 식을 저장하고
    BlankDelete(infix); //infix식에 빈칸을 제거한 뒤(빈칸을 없앰으로써 메모리를 최대한 절약)
    ExpressionErrorCheck(infix); //infix로 직힌 식의 표현의 오류가 있나 찾고
    stack = (char*)malloc(strlen(infix)*sizeof(char)+1); //연산자를 저장하는 stack메모리를 할당,
    postfix = (char**)malloc(strlen(infix)*sizeof(char*));; //postfix로 변환할 식을 담을 메모리를 할당 후
    postfixlen = ConvertInfixtoPostfix(infix, stack, postfix); //infix식을 postfix로 변환한 뒤 연산자를 stack에, 나머지 postfix로 변환된 숫자를 postfix에 저장.
    
   FinalCalculate(postfix,postfixlen,infix); //postfix로 변경된 식을 통해 계산작업이 들어간 후 리턴.
    
    return 0;
}
