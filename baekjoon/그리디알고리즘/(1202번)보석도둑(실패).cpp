#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#pragma warning (disable : 4996)

using namespace std;

unsigned long long picking(vector <int> bags, vector <pair<int, int>> jewels, int N, int K)
{
	priority_queue <int> candidate;
	int idx = 0;
	int valid = 0;
	int b = 0;
	unsigned long long answer = 0;

	for(int i=0; i<K; i++)
	{
		if (idx >= N)
			break;
		b = bags[0];
		bags.erase(bags.begin());
		if (b >= jewels[idx].first)
		{
			valid += 1;
			while (idx < N)
			{
				if (b < jewels[idx].first)
					break;
				candidate.push(jewels[idx].second);
				idx += 1;
			}
		}
		/*
		반례
		3 3
		2 100
		4 42
		4 500
		2
		3
		4
		정답	: 600
		오출력	: 642 
		*/
		else if (i > 0 && !candidate.empty())
		{
			answer += candidate.top();
			candidate.pop();
		}
	}


	for (int i = 0; i < valid; i++)
	{
		answer += candidate.top();
		candidate.pop();
	}
	for (int i : bags)
	{
		if (candidate.empty())
			break;
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
	answer = picking(bags, jewels, N, K);

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
