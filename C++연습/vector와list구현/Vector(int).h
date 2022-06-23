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


		void add(int element) override; // �ߺ� element ���� �� fail
		void delete_(int element) override; // ������ ���� element ������ fail
		int getSize() const override; // ���� ������ ���� ��ȯ
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
