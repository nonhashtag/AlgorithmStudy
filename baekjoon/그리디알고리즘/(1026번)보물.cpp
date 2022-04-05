#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

#pragma warning (disable:4996)

using namespace std;

bool compare(int X, int Y)
{
	return X > Y;
}

int main()
{
	int N;
	int a;
	int answer = 0;
	cin >> N;
	vector <int> arr1;
	vector <int> arr2;
	for (int i = 0; i < N; i++)
	{
		cin >> a;
		arr1.push_back(a);
	}
	for (int i = 0; i < N; i++)
	{
		cin >> a;
		arr2.push_back(a);
	}

	sort(arr1.begin(), arr1.end());
	sort(arr2.begin(), arr2.end(), compare);

	for (int i = 0; i < N; i++)
	{
		answer += arr1[i] * arr2[i];
	}
	/*
	for (int i : arr1)
		printf("%d", i);
	printf("\n");
	for (int i : arr2)
		printf("%d", i);
		*/
	printf("%d", answer);
	return 0;
}
