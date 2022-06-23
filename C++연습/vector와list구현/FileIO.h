#pragma once
#include <iostream>
#include "list.h"
#include "Vector.h"
#include "Container_Operator.h"

namespace file_space
{

	std::vector<std::string> split(std::string str, char delimiter)
	{
		std::vector<std::string> data;
		std::stringstream ss(str);
		std::string temp;

		while (getline(ss, temp, delimiter))
		{
			data.push_back(temp);
		}
		return data;
	};


template <class ContainerType, typename DataType>
class FileIO
{
public:
	void readData(std::shared_ptr <ContainerType> container_type) const
	{
		std::ifstream read_file;
		std::string file_name = "";

		if (typeid(*container_type).name() == typeid(onboarding_vector::Vector<DataType>).name())
		{
			file_name = "VectorData.txt";

		}
		else if (typeid(*container_type).name() == typeid(onboarding_list::List<DataType>).name())
		{
			file_name = "ListData.txt";
		}
		else
		{
			std::cout << "Wrong!\n";
			return;
		}

		read_file.open(file_name, std::ios::in);

		if (!read_file.is_open())
		{
			std::cout << "Can't find the File!\n";
			return;
		}
		else
		{
			container_type->clear();

			std::string str = "";
			std::string data = "";
			std::string type = "";

			while (!read_file.eof())
			{
				getline(read_file, str);
				if (str.find("]"))
					data += str;
				if (str.find("type"))
					type += str;
			}
			read_file.close();

			data = data.substr(data.find("[") + 2, data.find("]")-1);
			type = type.substr(type.find(":") + 2, type.size());

			std::vector<std::string> data_vector = split(data, ' ');
			data_vector.pop_back();

			for (auto element : data_vector)
			{
				container_type->pushBack(std::stod(element));
			}
		}
		std::cout << "Load Success!!\n";
	}


	void writeData(std::shared_ptr<ContainerType> container_type) const
	{
		std::ofstream write_file;
		std::string file_name = "";

		if (typeid(*container_type).name() == typeid(onboarding_vector::Vector<DataType>).name())
		{
			file_name = "VectorData.txt";
		}
		else if (typeid(*container_type).name() == typeid(onboarding_list::List<DataType>).name())
		{
			file_name = "ListData.txt";
		}
		else
		{
			std::cout << "Wrong!\n";
			return;
		}

		write_file.open(file_name, std::ios::out);

		std::string get_info = container_type->getInfo();
		write_file.write(get_info.c_str(), get_info.size());

		write_file.close();
		std::cout << "Save Success!!\n";

		return;
	}
};


}
