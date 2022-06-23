#pragma once
#pragma once
#include "Container_Operator.h"
#include <memory>
#include <iostream>




namespace onboarding_vector
{
	enum Vector_Interface
	{
		Push_Back = 5,
		Pop_Back,
		Front,
		Back,
		Load_Data,
		Save_Data
	};

	template <typename DataType>
	class Vector : Container_Operator<DataType> {

		using Unique_Ptr = std::unique_ptr <DataType[]>;

	private:
		Unique_Ptr ptr;

		size_t v_size;
		size_t v_capacity;


	public:
		Vector();
		Vector(size_t size);
		Vector(size_t size, const DataType & element);


		void add(DataType element) override; // �ߺ� element ���� �� fail
		void delete_(DataType element) override; // ������ ���� element ������ fail
		size_t getSize() const override; // ���� ������ ���� ��ȯ
		void print() const override; // override;
		std::string getInfo() const override;
		void clear() override;



		size_t getCapacity() const;
		bool isExceed(size_t to_add) const;
		bool isEmpty() const;
		size_t requiredCapacity(size_t input_size) const;
		void pushBack(DataType element);
		void popBack();
		DataType front() const;
		DataType back() const;

		

		DataType operator[](size_t index) const
		{
			return ptr[index];
		}
	};


#include "Vector.hpp"
}
