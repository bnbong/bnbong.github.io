#include <stdio.h>
int get_n_from_user();
void move(int n, int beg, int aux, int end);

void move(int n, char beg, char aux, char end)
{
	
	if (n == 1) {
		++cnt;
		printf("%5d: %s%d%s%c%s%c.\n", cnt, "Move disk", beg, );
		
	}
	else
		

}

int get_n_from_user()
{
	int n;
	if(scanf("%d", &n) != 1 || n < 1) {
		exit(1)
	}
	return n;
}



int main()
{
	int n;
	n = get_n_from_user();
	assert(n > 0);
	move(n, 'A', 'B', 'C');

	return 0;
}

