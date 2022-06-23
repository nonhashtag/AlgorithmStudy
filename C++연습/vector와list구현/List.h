#pragma once
#include <iostream>
#include "Node.h"
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
		Erase,
		Load_Data,
		Save_Data
	};


	template <typename DataType>
	class List : Container_Operator<DataType> {

		using Shared_Node = std::shared_ptr<Node<DataType>>;

	private:
		Shared_Node head;
		Shared_Node tail;

	public:
		List();

		void add(DataType element) override; // 중복 element 존재 시 fail
		void delete_(DataType element) override; // 여분의 동일 element 없으면 fail
		size_t getSize() const override; // 현재 데이터 개수 반환
		void print() const override;
		std::string getInfo() const override;
		void clear() override;

		void createNode(DataType element);
		void pushFront(DataType element);
		void pushBack(DataType element);
		void popFront();
		void popBack();
		void insert(int index, DataType element);
		void erase(int index);
		bool isEmpty();
	};

#include "List.hpp"
}