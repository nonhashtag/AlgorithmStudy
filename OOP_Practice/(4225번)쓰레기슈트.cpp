#include <iostream>
#include <vector>
#include <algorithm>

enum RotatingDirection
{
	ClockWise = -1,
	Stopped,
	CounterClockWise
};

struct Point
{
	int x, y;
	Point(int first, int second) : x(first), y(second) {};
};

int ccw(Point p1, Point p2, Point p3)
{
	int z = (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y);
	if (z < 0)
		return ClockWise;
	else if (z == 0)
		return Stopped;
	else
		return CounterClockWise;
}

class GarbageChute
{
private:


public:
	

};

class ConvexHall
{
private:


public:

};


int main()
{
	std::vector<Point>x_axis;
	x_axis.push_back(Point(0, 0));
	x_axis.push_back(Point(1, 0));


}
