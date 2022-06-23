#pragma once
#include <memory>

template <typename DataType>
class Node
{
private:
	DataType data;
	std::shared_ptr<Node> pNext;

public:
	Node(DataType data);
	std::shared_ptr<Node<DataType>> getNext();
	void setNext(std::shared_ptr<Node<DataType>> pNext);
	DataType getData();
};

//#include "Node.hpp"
template <typename DataType>
Node<DataType>::Node(DataType data)
{
	this->data = data;
	this->pNext = nullptr;
}


template <typename DataType>
std::shared_ptr<Node<DataType>> Node<DataType>::getNext()
{
	return pNext;
}


template <typename DataType>
void Node<DataType>::setNext(std::shared_ptr<Node<DataType>> pNext)
{
	this->pNext = pNext;
}


template <typename DataType>
DataType Node<DataType>::getData()
{
	return data;
}