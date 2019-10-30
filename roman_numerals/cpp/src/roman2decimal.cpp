#include <iostream>

using namespace std;

int main(void)
{
	int count = 0;
	char c;

	while (cin >> c)
	{
		count++;
	}

	if (count)
	{
		cout << count;
	}

	return 0;
}
