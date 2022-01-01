# 1. 시작점을 큐에 삽입한다.
# 2. 시작점을 색칠한다.
# 3. 큐에서 하나를 뺀다.(빠지는 애가 현재 위치이다.)
# 4. 인접한 모든 정점에게 방문했는지 물어보고 방문하지 않았다면, 색칠하고 큐에 삽입한다.
# 5. 모두 완료했다면 다시 #3.으로 돌아간다.

"""
Queue의 핵심 기능 이해
C++ 의 <queue> 기준
queue <int> Queue; //선언

Queue.push(x); // x를 큐에 삽입
Queue.pop(); // 큐의 맨 앞에 있는 원소를 제거
Queue.front(); // 맨 앞의 원소를 반환
Queue.empty(); // 비었으면 true 반환

"""

def BFS(myGraph, check, queue):
    while True:
        if len(queue)==0:
            break
        current = queue[0]
        del queue[0]
        print(current, end=' ')

        for i in range(len(myGraph[current])):
            next = myGraph[current][i]  # current -- next 연결

            if check[next] == False:
                check[next] = True
                queue.append(next)

N = int(input()) # 노드 갯수
check = [False]*(N+1)
queue = [1]
check[1] = True
myGraph = [
            0,
           [2,3],
           [3,4,6],
           [1,2,7],
           [2,5,7,8],
           [4,6],
           [2,5],
           [3,4,8],
           [4,7,9],
           [8]
          ]
"""
#myGraph를 다음와 같이도 만들 수 있다.
myGraph=[0]*(N+1)
for i in range(int(input()): #간선 갯수 입력
    a, b = map(int, input().split())
    myGraph[a].append(b)
    myGraph[b].append(a)
"""
print()
BFS(myGraph, check, queue)


