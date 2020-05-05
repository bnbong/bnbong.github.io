#include <stdio.h>

typedef struct Node;
{
	int data;
} Node;

typedef struct CircularQueue
{
	Node* Nodes;

	int Front;
	int Rear; // pointing +1st number
	int Capacity; // has +1 room
} CircularQueue;

void CreateQueue(CircularQueue** Queue, int Capacity)
{
	(*Queue) = (CircularQueue*)malloc(sizeof(CircularQueue));

	(*Queue)->Nodes = (Node*)malloc(sizeof(Node)*(Capacity+1));

	(*Queue)->Front = 0;
	(*Queue)->Rear = 0;
	(*Queue)->Capacity = Capacity;
}

void Enqueue(CircularQueue* Queue, int Data)
{
	int Position = 0;

	Position = Queue->Rear;
	Queue->Rear = (Queue->Rear + 1) % (Queue->Capacity + 1);
	Queue->Nodes[Position].Data = Data;
}

int Dequeue(CircularQueue* Queue)
{
	int Position = Queue->Front;

	Queue->Front = (Queue->Front + 1) % (Queue->Capacity + 1);

	return Queue->Nodes[Position].Data;
}

int IsEmpty(CircularQueue* Queue)
{
	return (Queue->Front == Queue->Rear);
}

int IsFull(CircularQueue* Queue)
{
	if (Queue->Front < Queue->Rear)
		return (Queue->Rear - Queue->Front) == Queue->Capacity;
	else
		return (Queue->Rear + 1) == Queue->Front;
}


