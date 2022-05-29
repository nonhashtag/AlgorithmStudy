#include <iostream>
#include <vector>
#include <cmath>

class Plane
{
private:
	int dimension;
	std::vector <int> quadrant;
	int move_x;
	int move_y;

public:
	Plane();
	std::vector <int> getQuadrant();
};

Plane::Plane()
{
	long long quadrant = 0;
	int dimension = 0;

	std::cin >> dimension >> quadrant;
	this->dimension = dimension;
	for (int i = 0; i < dimension; i++)
	{
		long long index = std::pow(10, --dimension);
		this->quadrant.push_back(quadrant / index);
		quadrant = quadrant % index;
	}
	//this->dimension = dimension;
}

std::vector <int> Plane::getQuadrant()
{
	return quadrant;
}




int main()
{
	Plane plane;


	return 0;
}
