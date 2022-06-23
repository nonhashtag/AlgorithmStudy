#pragma once
#include "List.h"

using namespace onboarding_list;


template <typename DataType>
List<DataType>::List()
{
	head = nullptr;
	tail = nullptr;
}


template <typename DataType>
void List<DataType>::add(DataType element)
{
	if (isEmpty())
	{
		pushBack(element);
		return;
	}
	auto cur = head;
	while (cur->getNext() != nullptr)
	{
		if (cur->getData() == element)
			return;
		cur = cur->getNext();
	}
	pushBack(element);
	return;
}


template <typename DataType>
void List<DataType>::delete_(DataType element)
{
	if (isEmpty())
		return;
	auto cur = head;
	bool checked = false;
	if (head->getData() == element)
		checked = true;

	while (cur->getNext() != nullptr)
	{
		if (cur->getNext()->getData() == element)
		{
			if (checked)
			{
				cur->setNext(cur->getNext()->getNext());
				continue;
			}
			else
				checked = true;
		}
		cur = cur->getNext();
	}
}


template <typename DataType>
size_t List<DataType>::getSize() const
{
	auto cur = head;
	int count = 0;
	while (cur != nullptr)
	{
		count++;
		cur = cur->getNext();
	}
	return count;
}


template <typename DataType>
void List<DataType>::print() const
{
	auto cur = head;
	std::cout << "[ ";
	while (cur != nullptr)
	{
		std::cout << cur->getData() << " ";
		cur = cur->getNext();
	}
	std::cout << "]\n";
}

template <typename DataType>
std::string List<DataType>::getInfo() const
{
	std::string info = "[ ";
	std::string type = typeid(DataType).name();
	auto cur = head;
	while (cur != nullptr)
	{
		info.append(std::to_string(cur->getData()) + " ");
		cur = cur->getNext();
	}
	info.append("]\n");
	info.append("type : " + type);

	return info;
}

template <typename DataType>
void List<DataType>::clear()
{
	head = nullptr;
	tail = head;
}


template <typename DataType>
bool List<DataType>::isEmpty()
{
	return head == nullptr;
}


template <typename DataType>
void List<DataType>::createNode(DataType element)
{
	head = std::make_shared <Node<DataType>>(element);
	tail = head;
}


template <typename DataType>
void List<DataType>::pushFront(DataType element)
{
	auto temp = head;
	if (isEmpty())
	{
		createNode(element);
		return;
	}
	head = std::make_shared<Node<DataType>>(element);
	head->setNext(temp);

	return;
}


template <typename DataType>
void List<DataType>::pushBack(DataType element)
{
	if (isEmpty())
	{
		createNode(element);
		return;
	}
	tail->setNext(std::make_shared<Node<DataType>>(element));
	tail = tail->getNext();

	return;
}


template <typename DataType>
void List<DataType>::popFront()
{
	if (isEmpty())
	{
		std::cout << "########## List is Empty!! ##########\n";
		return;
	}
	head = head->getNext();
	return;
}


template <typename DataType>
void List<DataType>::popBack()
{
	int tail_count = tail.use_count();
	auto temp = head;
	if (isEmpty())
	{
		std::cout << "########## List is Empty!! ##########\n";
		return;
	}
	while (temp->getNext() != tail)
	{
		temp = temp->getNext();
	}
	temp->setNext(nullptr);
	tail = temp;

	return;
}


template <typename DataType>
void List<DataType>::insert(int index, DataType element)
{
	auto cur = head;
	int idx = 0;
	if (index == 0)
	{
		pushFront(element);
		return;
	}
	if (index > getSize())
	{
		std::cout << "######list index out of range#######\n";
		return;
	}
	while (1)
	{
		if (idx == index - 1)
		{
			auto temp = std::make_shared<Node<DataType>>(element);
			temp->setNext(cur->getNext());
			cur->setNext(temp);
			return;
		}
		cur = cur->getNext();
		idx++;
	}

	return;
}


template <typename DataType>
void List<DataType>::erase(int index)
{
	auto cur = head;
	int idx = 0;
	if (index == 0)
	{
		popFront();
		return;
	}
	if (index > getSize())
	{
		std::cout << "######list index out of range#######\n";
		return;
	}
	while (1)
	{
		if (idx == index - 1)
		{
			auto to_erased = cur->getNext();
			cur->setNext(to_erased->getNext());
			return;
		}
		cur = cur->getNext();
		idx++;
	}

	return;
}






//
//template <typename DataType>
//Node<DataType>::Node(DataType data)
//{
//	this->data = data;
//	this->pNext = nullptr;
//}
//
//
//template <typename DataType>
//std::shared_ptr<Node<DataType>> Node<DataType>::getNext()
//{
//	return pNext;
//}
//
//
//template <typename DataType>
//void Node<DataType>::setNext(std::shared_ptr<Node<DataType>> pNext)
//{
//	this->pNext = pNext;
//}
//
//
//template <typename DataType>
//DataType Node<DataType>::getData()
//{
//	return data;
//}