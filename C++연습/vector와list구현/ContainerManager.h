#pragma once
#include <iostream>
#include "List.h"
#include "Vector.h"


namespace onboarding_container
{
	enum Manage_Interface
	{
		Exit,
		GetSize,
		PrintAll
	};



template <typename DataType>
class ContainerManager
{

private:
	std::shared_ptr < onboarding_list::List<DataType>> lst;
	std::shared_ptr <onboarding_vector::Vector<DataType>> vec;
	size_t num_of_container;

public:
	ContainerManager();
	void initList();
	void initVector();

	std::shared_ptr <onboarding_list::List<DataType>> listHandler();
	std::shared_ptr <onboarding_vector::Vector<DataType>> vectorHandler();
	size_t getSize();
	void printInformation();
};

template <typename DataType>
ContainerManager<DataType>::ContainerManager()
{
	this->lst = nullptr;
	this->vec = nullptr;
	this->num_of_container = 0;
}

template <typename DataType>
void ContainerManager<DataType>::initList()
{
	this->lst = std::make_shared<onboarding_list::List<DataType>>();
	this->num_of_container+=1;
}

template <typename DataType>
void ContainerManager<DataType>::initVector()
{
	this->vec = std::make_shared<onboarding_vector::Vector<DataType>>();
	this->num_of_container += 1;
}

template <typename DataType>
std::shared_ptr <onboarding_list::List<DataType>> ContainerManager<DataType>::listHandler()
{
	if (this->lst == nullptr)
		initList();

	return this->lst;
}

template <typename DataType>
std::shared_ptr <onboarding_vector::Vector<DataType>> ContainerManager<DataType>::vectorHandler()
{
	if (this->vec == nullptr)
		initVector();
	return this->vec;
}

template <typename DataType>
size_t ContainerManager<DataType>::getSize()
{
	return num_of_container;
}

template <typename DataType>
void ContainerManager<DataType>::printInformation()
{
	std::cout << "LIST\n=> ";
	if (lst)		
		lst->print();

	std::cout << "\nVECTOR\n=>";
	if (vec)
		vec->print();
}


}