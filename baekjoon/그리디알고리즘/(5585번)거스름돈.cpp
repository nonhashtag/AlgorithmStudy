#include <stdio.h>
#include <iostream>

#pragma warning (disable:4996)

using namespace std;

int changes(int n)
{
	int coins[6] = {500, 100, 50, 10, 5, 1};
	int answer = 0;
	for (int i : coins)
	{
		while (n>=i)
		{
			n -= i;
			answer += 1;
		}
	}
	return answer;
}


int main()
{
	int change;
	
	cin >> change;
	change = 1000 - change;

	printf("%d", changes(change));

	return 0;
}
