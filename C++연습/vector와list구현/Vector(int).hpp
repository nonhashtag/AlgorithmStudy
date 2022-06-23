#include "Vector.h"

using namespace onboarding_vector;

 
void Vector ::add(int element)
{
	for (int i = 0; i < v_size; i++)
		if (ptr[i] == element)
			return;

	pushBack(element);
	return;
}


 
void Vector ::delete_(int element)
{
	bool exist = false;
	for (int i = 0; i < v_size - 1; i++)
	{
		if (ptr[i] == element)
		{
			if (exist)
			{
				for (int j = i; j < v_size - 1; j++)
					ptr[j] = ptr[j + 1];
				v_size--;
			}
			else
				exist = true;
		}
	}
	return;
}


 
int Vector ::getSize() const
{
	return v_size;
}

 
void Vector ::print() const
{
	std::cout << "[ ";
	for (size_t i = 0; i < v_size; i++)
		std::cout << ptr[i] << " ";

	std::cout << "]\n";

	return;
}

 
size_t Vector ::getCapacity() const
{
	return v_capacity;
}

 
Vector ::Vector()
{
	ptr = std::make_unique<int[]>(1);

	this->v_size = 0;
	this->v_capacity = 0;
}


 
Vector ::Vector(size_t size)
{
	ptr = std::make_unique<int[]>(size);

	this->v_size = 0;
	this->v_capacity = size;
}

 
Vector ::Vector(size_t size, const int &element)
{
	ptr = std::make_unique<int[]>(size);

	for (int i = 0; i < size; i++)
	{
		ptr[i] = element;
	}
	this->v_size = size;
	this->v_capacity = size;
}

 
bool Vector ::isExceed(size_t to_add) const
{
	return v_size + to_add > v_capacity;
}

 
bool Vector ::isEmpty() const
{
	return v_size == 0;
}

 
size_t Vector ::requiredCapacity(size_t input_size) const
{
	size_t required_capacity = this->v_capacity;
	size_t added_v_size = input_size + this->v_size;
	while (required_capacity < added_v_size)
	{
		required_capacity *= 2;
	}

	return required_capacity;
}

 
void Vector ::pushBack(int element)
{
	if (isExceed(1))
	{
		size_t extended_capacity = requiredCapacity(1);
		Unique_Ptr extended_ptr = std::make_unique<int[]>(extended_capacity);
		for (int i = 0; i < this->v_capacity; i++)
		{
			extended_ptr[i] = this->ptr[i];
		}
		this->ptr = std::move(extended_ptr);
		this->v_capacity = extended_capacity;
		return;
	}

	this->ptr[v_size++] = element;
	return;
}


 
void Vector ::popBack()
{
	v_size--;
	return;
}


 
int Vector ::front() const
{
	return ptr[0];
}


 
int Vector ::back() const
{
	return ptr[v_size - 1];
}