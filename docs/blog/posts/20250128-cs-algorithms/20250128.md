---
title: '[Computer Science] 코딩 테스트 준비 - 알고리즘 및 자료구조 기초'
description: 코딩 테스트 준비 - 알고리즘 및 자료구조 기초 내용 정리
authors:
  - bnbong
date:
  created: 2025-01-28
  updated: 2025-01-28
categories:
  - Computer Science
tags:
  - Algorithms
  - Data Structure
  - Computer Science
comments: true
---

## 개요

대학생 4학년으로 올라오면서 기업 코딩 테스트를 위해 반드시 알아야할 자료구조 및 알고리즘에 대해 블로그 포스팅으로 정리해보고자 한다.

지난 세월 동안 알고리즘과 담을 쌓고 살아왔기 때문에 이전에 배웠던 알고리즘 및 자료구조에 대해 한번 정리하는 시간이 필요했다.

여러 조사와 백준 등의 문제 풀이 사이트에서 직접 문제들을 풀어보면서 자주 등장하고 중요하다고 생각되는 내용들에 대해 코드를 중심으로 정리해보았다.

문제들은 Python으로 풀고 있기 때문에 예제 코드들은 모두 Python으로 작성하였다.

<br>

### 1. 자료구조 (Data Structures)

#### **배열 (Array)**

배열은 연속된 메모리 위치에 저장된 요소들의 모음이다.

python의 경우, 다른 자료구조 보다 배열을 사용해서 탐색을 하게 되면 성능이 떨어지기 때문에 해시맵 등 다른 자료구조를 사용해서 구현하는 것이 좋다.

```python
arr = [1, 2, 3, 4]
# 요소 접근
print(arr[1])  # 출력: 2
```

---

#### **집합 (Set)**

집합은 고유한 요소들의 모음이다.

python에서 집합을 선언할 때는 `{}` 또는 `set()` 혹은 `dict()` 을 사용한다.

선언 형태에 따라 사용할 수 있는 내장 메서드가 다르다. 상황에 알맞는 구조를 선택해서 구현하면 된다.

```python
s = {1, 2, 3}
s.add(4)
print(s)  # 출력: {1, 2, 3, 4}
```

---

#### **연결 리스트 (Linked List)**

연결 리스트는 노드들이 포인터로 연결된 구조이다.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

# 사용 예시
ll = LinkedList()
ll.append(1)
ll.append(2)
```

---

#### **스택 (Stack)**

스택은 LIFO(Last In, First Out) 원칙을 따른다.

<!-- more -->

```python
stack = []
stack.append(1)  # Push
stack.append(2)
print(stack.pop())  # 출력: 2
```

---

#### **큐 (Queue)**

큐는 FIFO(First In, First Out) 원칙을 따른다.

```python
from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
print(queue.popleft())  # 출력: 1
```

---

#### **우선순위 큐 (Priority Queue)**

우선순위 큐는 우선순위에 따라 요소를 반환한다.

```python
import heapq
pq = []
heapq.heappush(pq, (1, "작업1"))
heapq.heappush(pq, (3, "작업3"))
heapq.heappush(pq, (2, "작업2"))
print(heapq.heappop(pq))  # 출력: (1, "작업1")
```

---

#### **트리 (Tree)**

트리는 계층적 구조를 가지는 자료구조이다.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

---

#### **그래프 (Graph)**

그래프는 노드(정점)와 간선으로 구성된 자료구조이다.

```python
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}
```

---

### 2. 알고리즘 (Algorithms)

#### **정렬 (Sorting)**

##### **정렬 알고리즘 시간복잡도**

| **알고리즘**        | **최선 시간복잡도** | **평균 시간복잡도** | **최악 시간복잡도** | **공간복잡도** |
|---------------------|--------------------|--------------------|--------------------|----------------|
| **버블 정렬**       | $O(n)$              | $O(n²)$             | $O(n²)$             | $O(1)$           |
| **선택 정렬**       | $O(n²)$             | $O(n²)$             | $O(n²)$             | $O(1)$           |
| **삽입 정렬**       | $O(n)$              | $O(n²)$             | $O(n²)$             | $O(1)$           |
| **병합 정렬**       | $O(n \log n)$        | $O(n \log n)$        | $O(n \log n)$        | $O(n)$           |
| **퀵 정렬**         | $O(n \log n)$        | $O(n \log n)$        | $O(n²)$             | $O(\log n)$       |
| **힙 정렬**         | $O(n \log n)$        | $O(n \log n)$        | $O(n \log n)$        | $O(1)$           |
| **계수 정렬**       | $O(n + k)$          | $O(n + k)$          | $O(n + k)$          | $O(n + k)$       |
| **기수 정렬**       | $O(n \times k)$          | $O(n \times k)$          | $O(n \times k)$          | $O(n + k)$       |
| **버킷 정렬**       | $O(n + k)$          | $O(n + k)$          | $O(n²)$             | $O(n + k)$       |

!!! info "설명"
    - `n`은 데이터의 개수, `k`는 정렬된 데이터의 범위.
    - 퀵 정렬은 최악의 경우(정렬된 배열을 정렬 시도 시)에 $O(n²)$.
    - 계수 정렬, 기수 정렬, 버킷 정렬은 입력 데이터의 특성에 따라 사용.

<br>

예시) 병합 정렬 (Merge Sort) 구현:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

# 사용 예시
arr = [4, 2, 5, 1]
print(merge_sort(arr))  # 출력: [1, 2, 4, 5]
```

---

#### **탐색 (Search)**

##### **탐색 알고리즘 시간복잡도**

| **알고리즘**          | **최선 시간복잡도** | **평균 시간복잡도** | **최악 시간복잡도** |
|-----------------------|--------------------|--------------------|--------------------|
| **순차 탐색**         | $O(1)$              | $O(n)$              | $O(n)$              |
| **이진 탐색**         | $O(1)$              | $O(\log n)$          | $O(\log n)$          |
| **DFS (깊이 우선 탐색)** | $O(1)$              | $O(V + E)$          | $O(V + E)$          |
| **BFS (너비 우선 탐색)** | $O(1)$              | $O(V + E)$          | $O(V + E)$          |
| **이진 탐색 트리 탐색** | $O(\log n)$          | $O(\log n)$          | $O(n)$              |
| **해시 탐색**         | $O(1)$              | $O(1)$              | $O(n)$              |

!!! info "설명"
    - `V`는 노드(정점)의 개수, `E`는 간선의 개수.
    - 순차 탐색은 단순한 배열 또는 리스트에서 값을 찾는 방법.
    - 이진 탐색은 정렬된 배열에서만 사용할 수 있음.
    - DFS와 BFS의 시간복잡도는 그래프의 표현 방식(인접 리스트/행렬)에 따라 달라질 수 있음.
    - 해시 탐색은 해시 충돌이 없을 때 $O(1)$ 의 시간복잡도를 가짐.

<br>

예시) 이진 탐색 (Binary Search) 구현:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 사용 예시
arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 3))  # 출력: 2
```

---

#### **BFS/DFS 탐색**

**너비 우선 탐색 (BFS):**

```python
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return visited
```

**깊이 우선 탐색 (DFS):**

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

---

#### **슬라이딩 윈도우 (Sliding Window)**

최대 부분 배열의 합을 구하는 예제:

```python
def max_sum_subarray(arr, k):
    max_sum, window_sum = 0, sum(arr[:k])
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# 사용 예시
print(max_sum_subarray([1, 2, 3, 4, 5], 3))  # 출력: 12
```

---

#### **재귀 (Recursion)**

재귀를 사용한 팩토리얼 계산:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 사용 예시
print(factorial(5))  # 출력: 120
```

---

#### **동적 프로그래밍 (Dynamic Programming)**

피보나치 수열 계산:

```python
def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

# 사용 예시
print(fibonacci(10))  # 출력: 55
```

## 마치며

그래프 탐색의 경우, 베이스가 되는 BFS, DFS 구현체 자체를 어느정도 외우고 들어가야 문제를 어느정도 접근하기 용이하다.

알고리즘 문제들은 풀고 있으면 고등학교 수학 문제 푸는 느낌이라 여전히 달갑지는 않다ㅠㅠ
