#pragma once
#include <vector>
#include <sstream>
#include <fstream>

template <typename DataType>
class Container_Operator abstract{

public:
	virtual void add(DataType element) = 0; // 중복 element 존재 시 fail
	virtual void delete_(DataType element) = 0; // 여분의 동일 element 없으면 fail
	virtual size_t getSize() const = 0; // 현재 데이터 개수 반환
	virtual void print() const = 0;
	virtual std::string getInfo() const = 0;
	virtual void clear() =0;
};