#include <iostream>
#include "ContainerManager.h"
#include "List.h"
#include "Vector.h"
#include "FileIO.h"
#include <windows.h>


enum General_Interface
{
	Exit,
	Add,
	Delete,
	Getsize,
	Print
};



void listSelect(onboarding_container::ContainerManager<int> & container, int operator_choice)
{
	int input_element = 0;
	int input_index = 0;
	
	auto lst = container.listHandler();
	file_space::FileIO<onboarding_list::List<int>, int> file_io;
	switch (operator_choice)
	{
	case Exit: // 0
		break;

	case Add: // 1
		std::cin >> input_element;
		lst->add(input_element);
		break;

	case Delete: // 2
		std::cin >> input_element;
		lst->delete_(input_element);
		break;

	case Getsize: // 3
		std::cout << "List Size : " << lst->getSize() << "\n";
		break;

	case Print: // 4
		std::cout << "List\n=> " << lst->getInfo() << "\n";
		break;

	case onboarding_list::Push_Front: // 5
		std::cin >> input_element;
		lst->pushFront(input_element);
		break;

	case onboarding_list::Push_Back: // 6
		std::cin >> input_element;
		lst->pushBack(input_element);
		break;

	case onboarding_list::Pop_Front: // 7
		lst->popFront();
		break;

	case onboarding_list::Pop_Back: // 8
		lst->popBack();
		break;

	case onboarding_list::Insert: // 9
		std::cin >> input_index;
		std::cin >> input_element;
		lst->insert(input_index,input_element);
		break;

	case onboarding_list::Erase: // 10
		std::cin >> input_index;
		lst->erase(input_index);
		break;

	case onboarding_list::Load_Data: // 11
		file_io.readData(lst);
		break;

	case onboarding_list::Save_Data: // 12
		file_io.writeData(lst);
		break;
	}
}

void vectorSelect(onboarding_container::ContainerManager<int> & container, int operator_choice)
{
	int input_element = 0;
	int input_index = 0;
	

	auto vec = container.vectorHandler();
	file_space::FileIO<onboarding_vector::Vector<int>, int> file_io;
	switch (operator_choice)
	{
	case Exit: // 0
		break;

	case Add: // 1
		std::cin >> input_element;
		vec->add(input_element);
		break;

	case Delete: // 2
		std::cin >> input_element;
		vec->delete_(input_element);
		break;

	case Getsize: // 3
		std::cout << "Vector Size : " << vec->getSize() << "\n";
		break;

	case Print: // 4
		std::cout << "Vector\n=> " << vec->getInfo() << "\n";
		break;

	case onboarding_vector::Push_Back: // 5
		std::cin >> input_element;
		vec->pushBack(input_element);
		break;

	case onboarding_vector::Pop_Back: // 6
		vec->popBack();
		break;

	case onboarding_vector::Front: // 7
		std::cout << vec->front() << "\n";
		break;

	case onboarding_vector::Back: // 8
		std::cout << vec->back() << "\n";
		break;


	case onboarding_vector::Load_Data: // 9
		file_io.readData(vec);
		break;

	case onboarding_vector::Save_Data: //10
		file_io.writeData(vec);
		break;
	}
}



void managerSelect(onboarding_container::ContainerManager<int> & container, int operator_choice)
{
	switch (operator_choice)
	{
	case onboarding_container::Exit:
		break;
	case onboarding_container::GetSize:
		std::cout << container.getSize() << "\n";
	case onboarding_container::PrintAll:
		container.printInformation();
		std::cout << "\n";
		break;
	}
}


int main()
{
	int choice1 = -1;
	int choice2 = -1;
	int data = 0;


	
	onboarding_list::List<int> lst{};
	onboarding_vector::Vector<int> operator_test_vec(10, 3);
	std::cout << operator_test_vec[1] << "\n";
	std::cout << "########### Operator Test ############\n";
	
	
	onboarding_container::ContainerManager<int> container{};


	while (choice1) {

		std::cout << "Choose \n1 : Vector \n2 : List\n3: Manager\n0: Exit=> ";
		std::cin >> choice1;
		system("cls");

		if (choice1 == 1)
		{
			while (choice2 != Exit)
			{
				std::cout << "Select the Command\n";
				std::cout << "0 : exit\n";
				std::cout << "1 : Add\n";
				std::cout << "2 : Delete\n";
				std::cout << "3 : GetSize\n";
				std::cout << "4 : Print\n";
				std::cout << "5 : Push_Back\n";
				std::cout << "6 : Pop_Back\n";
				std::cout << "7 : Front\n";
				std::cout << "8 : Back\n";
				std::cout << "9 : LoadData\n";
				std::cout << "10 : SaveData\n=>";
				std::cin >> choice2;
				system("cls");
				vectorSelect(container, choice2);

			}
		}
		else if (choice1 == 2)
		{
			while (choice2 != Exit)
			{

				std::cout << "Select the Command\n";
				std::cout << "0 : exit\n";
				std::cout << "1 : Add\n";
				std::cout << "2 : Delete\n";
				std::cout << "3 : GetSize\n";
				std::cout << "4 : Print\n";
				std::cout << "5 : Push_Front\n";
				std::cout << "6 : Push_Back\n";
				std::cout << "7 : Pop_Front\n";
				std::cout << "8 : Pop_Back\n";
				std::cout << "9 : Insert\n";
				std::cout << "10 : Erase\n";
				std::cout << "11 : LoadData\n";
				std::cout << "12 : SaveData\n=>";
				std::cin >> choice2;
				system("cls");
				listSelect(container, choice2);
			}
		}
		else if (choice1 == 3)
		{
			while (choice2 != Exit)
			{
				std::cout << "Select the Command\n";
				std::cout << "0 : exit\n";
				std::cout << "1 : Get the Number of Containers\n";
				std::cout << "2 : Print All Containers\n";
				std::cin >> choice2;
				system("cls");
				managerSelect(container, choice2);
			}
		}
		choice2 = -1;
	}
	return 0;
}