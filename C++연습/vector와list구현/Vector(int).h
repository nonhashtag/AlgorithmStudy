#pragma once
#pragma once
#include "Container_Operator.h"
#include <memory>
#include <iostream>




namespace onboarding_vector
{


	class Vector : Container_Operator {

		using Unique_Ptr = std::unique_ptr <int[]>;

	private:
		Unique_Ptr ptr;

		size_t v_size;
		size_t v_capacity;


	public:
		Vector();
		Vector(size_t size);
		Vector(size_t size, const int & element);


		void add(int element) override; // 중복 element 존재 시 fail
		void delete_(int element) override; // 여분의 동일 element 없으면 fail
		int getSize() const override; // 현재 데이터 개수 반환
		void print() const override;

		size_t getCapacity() const;
		bool isExceed(size_t to_add) const;
		bool isEmpty() const;
		size_t requiredCapacity(size_t input_size) const;
		void pushBack(int element);
		void popBack();
		int front() const;
		int back() const;

		/*friend bool operator==(const int &lhs, const int &rhs)
		{
			return lhs == rhs;
		}*/
	};


#include "Vector.hpp"
}
