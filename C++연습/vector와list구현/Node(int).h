#pragma once
#include "List.h"

using namespace onboarding_list;




Node::Node(int data)
{
	this->data = data;
	this->pNext = nullptr;
}



std::shared_ptr<Node> Node::getNext()
{
	return pNext;
}



void Node::setNext(std::shared_ptr<Node<DataType>> pNext)
{
	this->pNext = pNext;
}


DataType Node<DataType>::getData()
{
	return data;
}