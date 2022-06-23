#pragma once
#include "Container_Operator.h"
#include <memory>




namespace onboarding_vector
{	
	
	template <typename DataType>
	class Vector : Container_Operator {

		template <typename DataType>
		using Alloc = std::allocator<DataType>;

		template <typename DataType>
		using Alloc_ptr = std::allocator<DataType> (DataType*);

	private:
		Alloc<DataType> element_type;
		Alloc_ptr<DataType> ptr;

		size_t v_size;
		size_t v_capacity;


	public:
		Vector();
		Vector(size_t size);
		Vector(size_t size, DataType element);


		void add(DataType element) override; // 중복 element 존재 시 fail
		void delete_(DataType element) override; // 여분의 동일 element 없으면 fail
		int getSize() const override; // 현재 데이터 개수 반환
		void print() const override;

		size_t getCapacity() const;
		bool isExceed(size_t to_add) const;
		bool isEmpty() const;
		size_t requiredCapacity(size_t input_size) const;
		void pushBack(DataType element);
		void popBack();
		DataType front() const;
		DataType back() const;
	};


#include "Vector.hpp"
}






//https://docs.microsoft.com/ko-kr/cpp/standard-library/allocator-class?view=msvc-150 참조