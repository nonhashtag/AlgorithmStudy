#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#pragma warning (disable : 4996)

using namespace std;

unsigned long long picking(vector <int> bags, vector <pair<int, int>> jewels, int K)
{
	priority_queue <int> candidate;
	int cur = 0;
	int idx = 0;
	unsigned long long answer = 0;

	for(int b : bags)
	{
		while (idx < K)
		{
			if (b < jewels[idx].first)
				break;
			candidate.push(jewels[idx].second);
			idx += 1;
		}
	}
	for (int i = 0; i < K; i++)
	{
		answer += candidate.top();
		candidate.pop();
	}
	return answer;
	
}

int main()
{
	int N, K;
	int a, b;
	vector <pair<int, int>> jewels;
	vector <int> bags;
	unsigned long long answer = 0;
	


	scanf("%d %d", &N, &K);
	for (int i = 0; i < N; i++)
	{
		scanf("%d %d", &a, &b);
		jewels.push_back(make_pair(a, b));
	}
	for (int i = 0; i < K; i++)
	{
		scanf("%d", &a);
		bags.push_back(a);
	}

	sort(bags.begin(), bags.end());
	sort(jewels.begin(), jewels.end());
	answer = picking(bags, jewels, K);

	/*
	for (int i : bags)
		printf("%d ", i);
	*/
	/*
	for (pair <int, int> j : jewels)
		printf("%d %d\n", j.first, j.second);
	*/
	printf("%llu", answer);
	return 0;

}
