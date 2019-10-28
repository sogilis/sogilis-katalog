#include <stdio.h>

int main(void)
{
	char count = -1;
	char c;
	
	while ((c = getchar()) != EOF)
	{
		count++;
	}

	if (count)
	{
		printf("%d\n", count);
	}

	return 0;
}
