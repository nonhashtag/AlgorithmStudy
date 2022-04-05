#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#pragma warning (disable : 4996)

using namespace std;

int five_three(int N)
{
	int five = N / 5;
	int cnt = five;
	int total = cnt * 5;
	if (N == 3 || N == 5)
		return 1;
	if (total == N)
		return cnt;
	while (1)
	{
		if (total < N)
		{
			total += 3;
			cnt += 1;
		}
		else if (total > N )
		{
			if (five > 0)
			{
				total -= 5;
				cnt -= 1;
				five -= 1;
			}
			else
			{
				cnt = -1;
				break;
			}
		}
		else
			break;
	}

	return cnt;
}

int main()
{
	int N;
	cin >> N;
	cout << five_three(N);
	return 0;

}
