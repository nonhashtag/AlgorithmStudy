#include <stdio.h>
#include <iostream>

#pragma warning(disable:4996)

using namespace std;

int main()
{
	int input_t;
	int t = 0;
	int btn[3] = {300, 60, 10};
	int answer[3] = { 0, 0, 0 };
	int idx = 0;
	int out = 0;

	scanf("%d", &input_t);
	t = input_t;

	while (idx<3)
	{
		if (t < btn[idx])
		{
			idx += 1;
		}
		else
		{
			t -= btn[idx];
			answer[idx] += 1;
		}
	}
	for (int i = 0; i < 3; i++)
	{
		out += (btn[i] * answer[i]);
	}

	if (out == input_t)
	{
		for (int i = 0; i < 3; i++)
			printf("%d ", answer[i]);
	}
	else
	{
		printf("-1");
	}

	return 0;
}
