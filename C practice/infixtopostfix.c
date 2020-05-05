#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define SIZE 64 //이 SIZE 변수를 동적할당해야할것임.

#define OPEN 10
#define CLOSE 20
#define OPERATOR 30
#define OPERAND 40

#define LPP 0

#define ADD 1
#define MIN 2
#define MUL 3

#define NONE 9

static char infix[SIZE+1],stack[SIZE],postfix[SIZE+1]; //리스트 infix, stack, postfix 를 65, 64, 65만큼 크기를 '고정할당'
static int top=-1; //맨위의 요소위치를 가리키는 top

void infixtopostfix(void);     
int gettype(char);             
void push(char);               
char pop(void);                
int getprec(char);            

int main()
{
  char ch;
  printf("Enter an infix expression\n");
  scanf("%s", infix);	
  infixtopostfix(); //infix식을 postfix로 변환하는 본 함수
  printf("infix = %s\npost fix =%s\n",infix,postfix);
}

void infixtopostfix(void)
{
  int index,p,prec;
  int length=strlen(infix); //infix로 표현된 식의 전체 길이
  char next;
  int type;
  index=p=0;
  while(index<length)
  {
    type=gettype(infix[index]); //infix[index]에 쓰여있는 요소의 타입을 리턴
    switch(type)
    {
      case OPEN: //괄호여는 연산자일때
      push(infix[index]); 
      break;
	
      case CLOSE://괄호를 닫는 연산자일때
      while((next=pop())!='(') //연산자 닫는괄호를 pop하기 전까지
	postfix[p++]=next; //postfix에 stack에서 pop한 연산자를 저장한다.
	break;
      
      case OPERAND: //숫자는 postfix에 push
	postfix[p++]=infix[index];
	break;
	
      case OPERATOR: //연산자 + - * 일 때
	prec=getprec(infix[index]); //연산자를 세부적으로 리턴하는 함수를 통해 prec를 설정.
	while(top>-1 && prec <= getprec(stack[top])) //stack에 적어도 하나의 요소가 있으면서, stack에 맨 위에있는 연산자보다 순위가 낮거나 같을 때(연산자 우선순위)
	postfix[p++]=pop(); //postfix에 있던 연산자를 pop
	push(infix[index]); //새로 읽어들이는 연산자를 stack에 push
	break;
	}
	index++;
    }
	
    while(top>-1)
      postfix[p++]=pop(); //마지막으로 저장된 요소의 그 다음 연산자(아마garbage값)을 pop한 후 NULL문자를 넣기 위한 작업을 함.
      postfix[p]='\0'; //postfix에 저장되는 string 마지막 요소에 '\0'문자를 추가함으로써 문자의 끝을 나타내줌.
}

int gettype(char sym)
{
  switch(sym)
  {
    case '(': //sym에 적혀있는 char을 읽어서 (, ), +, -, *, / 연산자를 나누는 작업.
      return(OPEN); //괄호를 여는 연산자 OPEN
	
    case ')':
      return(CLOSE); //괄호를 닫는 연산자 CLOSE
	
    case '+':
    case '-':
    case '*':
      return(OPERATOR); //연산을 수행하는 (, )을 제외한 연산자 +, -, *
    
    default : //숫자
      return(OPERAND);
    }
}

void push(char sym) //리스트에 요소를 push하는 작업을 수행하는 함수
{
	if(top>SIZE)//define으로 정의된 top는 건들지 말아야한다. 스택이 꽉 차있을 경우(그러나 malloc으로 동적할당된 스텍을사용할것임으로 잘 나타나지 않을것.)
	{
		printf("\nStack is full\n");
		exit(0);
	}
	else
		stack[++top]=sym; //stack에 sym을 저장
}

char pop(void) //리스트에 요소를 pop하는 작업을 수행하는 함수
{
	if(top<=-1)//스텍에 아무것도 존재하지 않을 때
	{
		printf("\nStack is empty\n");
		exit(0);
	}
	else
		return(stack[top--]); //
}

int getprec(char sym) //연산자를 세부적으로 리턴하는 함수
{
	switch(sym)
	{
		case '(':
			return(LPP);
		case '+':
			return(ADD);
		case '-':
			return(MIN);
		case '*':
			return(MUL);
		default :
			return(NONE);
	}
}
