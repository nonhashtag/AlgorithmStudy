#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	string N;
	cin >> N;
	int sum = 0;
	bool check = false;
	vector <char> answer;
	for (char i : N)
	{
		if (i == '0')
			check = true;
		sum += i - '0';
		answer.push_back(i);
	}
	if (sum % 3 != 0 || check==false)
		cout << "-1";
	else
	{
		sort(answer.begin(), answer.end(), greater<>());
		for (char i : answer)
			cout << i;
	}

	return 0;
}
