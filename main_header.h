#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void BlankDelete(char *expr);
unsigned long long CheckFileLength(void);
char *SaveExpressionToMemory(void);
void ExpressionErrorCheck(char *expr);
char* Plus(char *arr1, char *arr2);
char* Multiply(char *arr1, char *arr2);
char* Minus(char *a1, char *a2);
void FinalCalculate(char **polish, unsigned long long postfixlen, char *infix);

unsigned long long ConvertInfixtoPostfix(char *infix, char *stack, char **postfix);
int GetOperatorType(char operator);
void push(char operator, char *stack);
char pop(char *infix, char *stack);
int OperatorCheck(char operator);