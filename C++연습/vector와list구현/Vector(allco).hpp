#include "Vector.h"

using namespace onboarding_vector;

template <typename DataType>
void Vector<DataType>::add(DataType element)
{
	for (int i = 0; i < v_size; i++)
		if (ptr[i] == element)
			return;

	pushBack(element);
	return;
}


template <typename DataType>
void Vector<DataType>::delete_(DataType element)
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


template <typename DataType>
int Vector<DataType>::getSize() const
{
	return v_size;
}

template <typename DataType>
void Vector<DataType>::print() const
{
	std::cout << "[ ";
	for (size_t i = 0; i < v_size; i++)
		std::cout << ptr[i] << " ";

	std::cout << "]\n";

	return;
}

template <typename DataType>
size_t Vector<DataType>::getCapacity() const
{
	return v_capacity;
}

template <typename DataType>
Vector<DataType>::Vector()
{
	ptr = this->element_type.allocate(0);

	this->v_size = 0;
	this->v_capacity = 0;
}


template <typename DataType>
Vector<DataType>::Vector(size_t size)
{
	ptr = this->element_type.allocate(size);

	this->v_size = 0;
	this->v_capacity = size;
}

template <typename DataType>
Vector<DataType>::Vector(size_t size, DataType element)
{
	ptr = this->element_type.allocate(size);

	for (int i = 0; i < size; i++)
	{
		ptr[i] = element;
	}
	this->v_size = size;
	this->v_capacity = size;
}

template <typename DataType>
bool Vector<DataType>::isExceed(size_t to_add) const
{
	return v_size + to_add > v_capacity;
}

template <typename DataType>
bool Vector<DataType>::isEmpty() const
{
	return v_size == 0;
}

template <typename DataType>
size_t Vector<DataType>::requiredCapacity(size_t input_size) const
{
	size_t required_capacity = this->v_capacity;
	size_t added_v_size = input_size + this->v_size;
	while (required_capacity < added_v_size)
	{
		required_capacity *= 2;
	}

	return required_capacity;
}

template <typename DataType>
void Vector<DataType>::pushBack(DataType element)
{
	if (isExceed(1))
	{
		size_t extended_Capacity = requiredCapacity(1);
		Alloc_ptr extended_ptr = this->element_type.allocate(extended_Capacity);
		for (int i = 0; i < this->v_capacity; i++)
		{
			extended_ptr[i] = this->ptr[i];
		}
		this->element_type.deallocate(this->ptr, v_capacity);
		this->v_capacity = extended_Capacity;
		this->ptr = extended_ptr;
		return;
	}

	this->ptr[v_size++] = element;
	return;
}


template <typename DataType>
void Vector<DataType>::popBack()
{
	v_size--;
	return;
}


template <typename DataType>
DataType Vector<DataType>::front() const
{
	return ptr[0];
}


template <typename DataType>
DataType Vector<DataType>::back() const
{
	return ptr[v_size - 1];
}