#include "List.h"

using namespace onboarding_list;


List::List()
{
	head = nullptr;
	tail = nullptr;
}

void List::add(int element)
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

void List::delete_(int element)
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

int List::getSize() const
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

void List::print() const
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


bool List::isEmpty()
{
	return head == nullptr;
}

void List::createNode(int element)
{
	head = std::make_shared <Node> (element);
	tail = head;
}

void List::pushFront(int element)
{
	auto temp = head;
	if (isEmpty())
	{
		createNode(element);
		return;
	}
	head = std::make_shared<Node> (element);
	head->setNext(temp);

	return;
}

void List::pushBack(int element)
{
	if (isEmpty())
	{
		createNode(element);
		return;
	}
	tail->setNext(std::make_shared<Node>(element));
	tail = tail->getNext();

	return;
}

void List::popFront()
{
	if (isEmpty())
	{
		std::cout << "########## List is Empty!! ##########\n";
		return;
	}
	head = head->getNext();
	return;
}

void List::popBack()
{
	int tail_count = tail.use_count();
	auto temp = head;
	if (isEmpty())
	{
		std::cout << "########## List is Empty!! ##########\n";
		return;
	}
	while (temp->getNext()!=tail)
	{
		temp = temp->getNext();
	}
	temp->setNext(nullptr);
	tail = temp;

	return;
}

void List::insert(int index, int element)
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
		if (idx == index-1)
		{
			auto temp = std::make_shared<Node>(element);
			temp->setNext(cur->getNext());
			cur->setNext(temp);
			return;
		}
		cur = cur->getNext();
		idx++;
	}

	return;
}


void List::erase(int index)
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
		if (idx == index-1)
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
