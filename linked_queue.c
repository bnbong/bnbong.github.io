

typedef struct Node
{
	int Data;
	struct Node* NextNode;
} Node;

typedef struct LinkedQueue
{
	Node* Front;
	Node* Rear;
	int Count;
} LinkedQueue;

void CreateQueue(LinkedQueue** Queue)
{
	(*Queue) = (LinkedQueue*)malloc(sizeof(LinkedQueue));
	(*Queue)->Front = NULL;
	(*Queue)->Rear = NULL;
	(*Queue)->Count = 0;
}

Node* LQ_CreateNode(int NewData)
{
	Node* NewNode = (Node*)malloc(sizeof(Node));
	NewNode->Data = NewData;

	NewNode->NextNode = NULL;

	return NewNode;
}

void Enqueue(LinkdeQueue* Queue, Node* NewNode)
{
	if (Queue->Front = NULL)
	{
		Queue->Front = NewNode;
		Queue->Rear = NewNode;
		Queue->Count++
	}
	else
	{
		Queue->Rear-NextNode = NewNode;
		Queue->Rear = NewNode;
		Queue->Count++
	}
}

Node* Dequeue(LinkedQueue* Queue)
{
	Node* Front = Queue->Front;

	if(Queue->Front->NextNode == NULL)
	{
		Queue->Front = NULL;
		Queue->Rear = NULL;
	}
	else
	{
		Queue->Front = Queue->Front->NextNode;
	}
	Queue->Count--
		return Front;
}

int IsEmpty(LinkedQueue* Queue)
{
	return (Queue->Front == NULL);
}

