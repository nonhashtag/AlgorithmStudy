#include <iostream>
#include <vector>
#include <algorithm>


int main()
{
	int N = 0;
	int D = 0;
	int s = 0, e = 0, w = 0;
	std::vector <std::pair<int, int>> *arr;
	int* dist; 

	std::cin >> N >> D;
	dist = new int[D+1];
	arr = new std::vector <std::pair<int,int>>[D+1]; // 동적할당이나 정적할당이나 메모리 호출량은 비슷하다..

	for (int i = 0; i < N; i++)
	{
		std::cin >> s >> e >> w;
		arr[s].push_back(std::make_pair(e, w));
	}
	for (int i = 0; i <= D; i++)
		dist[i] = i;

	for (int i = 0; i <= D; i++)
	{
		if (i != 0)
		{
			dist[i] = (dist[i] < dist[i - 1] + 1) ? dist[i] : dist[i - 1] + 1;
		}
		for (std::pair<int, int> road : arr[i])
		{
			if (road.first <= D && dist[road.first] > road.second + dist[i])
				dist[road.first] = road.second + dist[i];
		}
	}
	std::cout << dist[D] << std::endl;
	delete[] dist;
	delete[] arr;

	return 0;
}
