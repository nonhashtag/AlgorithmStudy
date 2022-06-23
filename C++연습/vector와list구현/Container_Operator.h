#pragma once
#include <vector>
#include <sstream>
#include <fstream>

template <typename DataType>
class Container_Operator abstract{

public:
	virtual void add(DataType element) = 0; // �ߺ� element ���� �� fail
	virtual void delete_(DataType element) = 0; // ������ ���� element ������ fail
	virtual size_t getSize() const = 0; // ���� ������ ���� ��ȯ
	virtual void print() const = 0;
	virtual std::string getInfo() const = 0;
	virtual void clear() =0;
};