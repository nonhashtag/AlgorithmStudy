#include <iostream>
#include <vector>
#include <cmath>
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


std::vector <Point> dots;


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

double dotLineDistance(Point p1, Point p2, Point p3)
{
	return abs((p1.y - p2.y) * p3.x - (p1.x - p2.x) * p3.y + p1.x * p2.y - p2.x * p1.y)
		/ sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

bool ccwCompare(Point p1, Point p2)
{
	auto zero = dots[0];
	int z = ccw(zero, p1, p2);
	if (z > 0)
		return true;
	if (z < 0)
		return false;

	return getDistance(zero, p1) < getDistance(zero, p2);
}


class ConvexHull
{
private:
	std::vector<Point> verts;
	ConvexHull() {};

public:
	ConvexHull(std::vector<Point> inputs);
	void setDots();
	void setVerts();
	std::vector<Point> getVerts();
	std::vector<Point> graham();

};

ConvexHull::ConvexHull(std::vector<Point> input)
{
	dots = input;
	setDots();
	setVerts();
}

std::vector<Point> ConvexHull::graham()
{
	std::vector <Point> verts;
	for (int i = 0; i < dots.size(); i++)
	{
		while (2 <= verts.size() && ccw(verts[verts.size() - 2], verts[verts.size() - 1], dots[i]) <= 0)
			verts.pop_back();

		verts.push_back(dots[i]);
	}
	return verts;
}

void ConvexHull::setDots()
{
	int temp = 0;
	for (int i = 1; i < dots.size(); i++)
		if (dots[i].y < dots[temp].y || (dots[i].y == dots[temp].y && dots[i].x < dots[temp].x))
			temp = i;
	std::swap(dots[temp], dots[0]);
	std::sort(dots.begin() + 1, dots.end(), ccwCompare);
	return;
}

void ConvexHull::setVerts()
{
	verts = graham();
	return;
}


std::vector<Point> ConvexHull::getVerts()
{
	return verts;
}



class GarbageChute
{
private:


public:


};





int main()
{
	std::cout << std::fixed;
	std::cout.precision(2);
	int num_of_dots = 0;
	int x=0, y=0;
	int top = 0; ///////////////
	int test_case = 0;
	std::vector <Point> dots;
	std::cin >> num_of_dots;

	while(num_of_dots)
	{
		for (int i = 0; i < num_of_dots; i++)
		{
			std::cin >> x >> y;
			dots.push_back(Point(x, y));
		}
		ConvexHull shape(dots);

		/*for (auto i : shape.getVerts())
			std::cout << i.x << " " << i.y << "\n";*/

		auto stk = shape.getVerts();
		double res = 100000000;
		top = stk.size();

		/////////
		for (int i = 0, j = 1; i < top; i++) {
			double l = dotLineDistance(stk[i], stk[(i + 1) % top], stk[j]);
			while (l < dotLineDistance(stk[i], stk[(i + 1) % top], stk[(j + 1) % top])) {
				j = (j + 1) % top;
				l = dotLineDistance(stk[i], stk[(i + 1) % top], stk[j]);
			}
			res = std::min(res, l);
		}
		
		std::cout << "Case " << ++test_case << ": " << res + 0.004999999 << "\n";

		std::cin >> num_of_dots;
	}
	return 0;
}
