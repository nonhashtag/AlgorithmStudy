#pragma once
#include <iostream>
#include <memory>
#include "Container_Operator.h"


namespace onboarding_list
{

	enum List_Enum
	{
		Push_Front = 5,
		Push_Back,
		Pop_Front,
		Pop_Back,
		Insert,
		Erase
	};

	class Node
	{
	private:
		int data;
		std::shared_ptr<Node> pNext;

	public:
		Node(int data);
		std::shared_ptr<Node> getNext();
		void setNext(std::shared_ptr<Node> pNext);
		int getData();
	};



	typedef std::shared_ptr<Node> Shared_Node;
	typedef std::weak_ptr<Node> Weak_Node;



	class List : Container_Operator{

	private:
		Shared_Node head;
		Shared_Node tail;

	public:
		List();
	
		void add(int element) override; // �ߺ� element ���� �� fail
		void delete_(int element) override; // ������ ���� element ������ fail
		int getSize() const override; // ���� ������ ���� ��ȯ
		void print() const override;

		void createNode(int element);
		void pushFront(int element);
		void pushBack(int element);
		void popFront();
		void popBack();
		void insert(int index, int element);
		void erase(int index);
		bool isEmpty();
	};
}


/*
�Ϸ��׸�

����
---
---
getSize
print

����Ʈ
createNode
pushFront
pushBack
popBack
insert
erase
isEmpty

*/