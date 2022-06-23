## 템플릿을 이용한 Vector와 List 구현

### 파일명에 ()괄호가 있는 파일은 컴파일 실패본 혹은 Legacy 이므로 굳이 필요는 없음

- Container_Operator.h - 공통기능을 담고 있는 인터페이스

- ContainerManager.h - Vector와 List의 관리자 클래스. (본 main.cpp 파일에서 Vector, List의 핸들러가 된다.)

<br>

- List.h/hpp - List 클래스의 선언과 정의부
- Node.h - List가 Linked List이기 때문에 해당 파일의 Node 클래스가 필요하다. (참고로, Node.hpp는 필요없다.)

<br>
  
- Vector.h/hpp - Vector 클래스의 선언과 정의부

<br>

- FileIO.h - 외부파일(VectorData.txt와 NodeData.txt)과 프로그램의 연결을 위한 class

<br>

- main.cpp - 프로그램 시작부(CLI 구현)
