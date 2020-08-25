#include <stdio.h>
#define MAX 100
int front = -1;
int rear = -1;
int queue[MAX];

int IsEmpty()
{   
    if(front == rear)
        return 1; // queue is empty
    else return 0;
}   

int IsFull()
{   
    int tmp = (rear+1) % MAX;
    if(tmp == front)
        return 1;
    else return 0; // in circle queue, if (rear+1)%100 == front mean queue is full
}

void addq(int value)
{
	if(IsFull() == 1)
		printf("Queue is full.\n");
	else
		queue[++rear]=value;
}

int deleteq()
{
	if(IsEmpty() == 1)
		printf("Queue is empty.\n");
	else{
		front = (front + 1) % MAX;
		return queue[front];
	}
}

int main()
{
	addq(4);
	addq(7);
	addq(14);
	printf("%d\n", deleteq());
	printf("%d\n", deleteq());
	printf("%d\n", deleteq());
	deleteq();
	
	return 0;
}

