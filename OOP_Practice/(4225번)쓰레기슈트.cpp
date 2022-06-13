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

int getDistance(Point p1, Point p2)
{
	return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

bool ccwCompare(const Point& starting_point, const Point& p1, const Point& p2)
{
	int z = ccw(starting_point, p1, p2);
	if (z > 0)
		return true;
	if (z < 0)
		return false;
	
	return getDistance(starting_point, p1) < getDistance(starting_point, p2);
}

bool startingPointCompare(const Point& p1, const Point& p2)
{
	auto zero_point = Point(0, 0);
	return getDistance(zero_point, p1) < getDistance(zero_point, p2);
}

class GarbageChute
{
private:


public:
	

};

class ConvexHull
{
private:
	std::vector<Point> dots;

public:
	std::vector<Point> graham();
};


std::vector<Point> graham(std::vector<Point> dots)
{
	std::vector <Point> verts;
	for (int i = 0; i < dots.size(); i++)
	{
		while (2 <= verts.size() && ccw(verts[verts.size() - 2], verts[verts.size() - 1], dots[i]) <= 0)
		{
			verts.pop_back();
		}
		verts.push_back(dots[i]);
	}
	return verts;
}

int main()
{
	std::vector<Point>x_axis;
	x_axis.push_back(Point(0, 0));
	x_axis.push_back(Point(1, 0));


}
