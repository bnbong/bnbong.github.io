---
title: '[Algorithm] 코딩테스트 준비를 위한 알고리즘 핵심 유형 정리(Python 예제 문제 풀이 포함)'
description: 코딩테스트에서 자주 출제되는 핵심 알고리즘 유형 정리와 프로그래머스 & LeetCode 대표 문제 풀이
authors:
  - bnbong
date:
  created: 2026-05-14
  updated: 2026-05-14
categories:
  - Algorithm
tags:
  - Algorithm
  - Coding Test
  - Data Structure
  - Python
comments: true
---

## 개요

코딩테스트 문제는 무한히 다양해 보이지만, 실제로는 10여 가지 핵심 알고리즘 유형으로 대부분 분류할 수 있다. 유형을 미리 파악하고 있으면 새로운 문제를 보았을 때 접근 전략을 빠르게 세울 수 있다.

이 글에서는 코딩테스트에서 자주 출제되는 핵심 알고리즘 유형을 정리하고, 각 유형별로 프로그래머스와 LeetCode의 대표 문제를 풀어본다. 풀이는 모두 Python으로 작성하며, 코드 아래에 별도 설명을 붙인다.

> 이전 글 '[[Computer Science] 코딩 테스트 준비 - 알고리즘 및 자료구조 기초](https://bnbong.github.io/blog/2025/01/28/computer-science-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%A4%80%EB%B9%84---%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%8F-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B8%B0%EC%B4%88/)'에서 배열, 스택, 큐, 트리 등 기초 자료구조를 다루었다.
> 이번 글은 그 후속편으로, 실전 문제 풀이에 필요한 알고리즘 유형에 집중하며 이 글만으로도 독립적으로 이해할 수 있도록 각 유형의 핵심 개념부터 설명한다.

<!-- more -->

---

## 유형 파악 전략 — 입력 크기(N)로 알고리즘 추론하기

문제를 읽은 뒤 가장 먼저 확인해야 할 것은 **입력 크기 N**과 **시간 제한**이다.

코딩테스트의 시간 제한은 보통 1~2초이며, Python 기준 초당 약 2,000만~1억 회의 단순 연산을 수행할 수 있다고 가정한다면 N의 크기에 따라 허용 가능한 시간 복잡도를 추론할 수 있다.

| N 범위 | 허용 시간 복잡도 | 추천 알고리즘 유형 |
|--------|----------------|------------------|
| N ≤ 10 | $O(N!)$ | 완전 탐색, 순열 |
| N ≤ 20 | $O(2^N)$ | 비트마스킹, 백트래킹 |
| N ≤ 500 | $O(N^3)$ | 플로이드-워셜, 3중 반복 DP |
| N ≤ 5,000 | $O(N^2)$ | DP, 이중 반복 브루트포스 |
| N ≤ 100,000 | $O(N \log N)$ | 정렬, 이분 탐색, 우선순위 큐 |
| N ≤ 10,000,000 | $O(N)$ | 투 포인터, 해시, 슬라이딩 윈도우 |

위 표는 대략적인 가이드라인이며, 상수 계수와 실제 연산 내용에 따라 달라질 수 있다.

이건 항상 맞는 접근법이 아니기 때문에 알고리즘 문제를 풀면서 도저히 어떤 알고리즘을 적용해야할 지 모를 때 지푸라기라도 잡는 느낌으로 유추하는 방법을 소개한 것이다.

---

## 핵심 알고리즘 Python 구현 요약

본격적인 유형 설명에 들어가기 전, 이 글에서 다루는 10가지 알고리즘의 핵심 구현 패턴만 먼저 모아둔다.

문제를 마주했을 때 "어떤 도구를 꺼낼까"를 빠르게 훑어보는 용도이며, 자세한 설명과 대표 문제 풀이는 아래 각 섹션에서 이어진다.

### 해시 — 존재 여부 / 빈도수

```python
from collections import Counter

freq = Counter(items)          # {item: count}
exists = key in dict_or_set    # 평균 O(1) 조회
diff = Counter(a) - Counter(b) # 양수 카운트만 남김
```

### 완전 탐색 & 백트래킹 — N ≤ 20, 모든 경우의 수

```python
from itertools import permutations, combinations, product

for perm in permutations(arr, r): ...   # 순열
for comb in combinations(arr, r): ...   # 조합
for state in product(range(2), repeat=n): ...  # 부분집합 = 비트 조합

def backtrack(path):
    if is_goal(path):
        results.append(path[:])
        return
    for choice in candidates(path):
        if not feasible(path, choice):  # 가지치기(pruning)
            continue
        path.append(choice)
        backtrack(path)
        path.pop()
```

### 그리디 — 매 단계 지역 최적 선택

```python
arr.sort(key=lambda x: ...)    # 정렬 후 순차 선택

# 단조 스택 패턴 (앞자리에 큰 수를 남기는 류의 문제)
stack = []
for x in arr:
    while stack and stack[-1] < x and budget > 0:
        stack.pop()
        budget -= 1
    stack.append(x)
```

### 정렬 — 커스텀 비교 기준 설계

```python
arr.sort(key=lambda x: (x.a, -x.b))     # 다중 키 + 내림차순 혼합

from functools import cmp_to_key
arr.sort(key=cmp_to_key(lambda a, b: int(b+a) - int(a+b)))  # 비교 함수
```

### 이분 탐색 & 파라메트릭 서치 — 정렬된 데이터 / 결정 문제 변환

```python
from bisect import bisect_left, bisect_right
idx = bisect_left(sorted_arr, target)

# 파라메트릭 서치: "X 가능한가?"라는 결정 문제로 변환
left, right = lo, hi
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1   # 더 작게 시도
    else:
        left = mid + 1
answer = left
```

### DFS / BFS — 그래프 / 격자 탐색

```python
# DFS (재귀) — 모든 경로, 경우의 수
def dfs(u):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v)

# BFS (deque) — 가중치 없는 그래프 최단 경로
from collections import deque
queue = deque([(start, 0)])
visited = {start}
while queue:
    u, d = queue.popleft()
    for v in graph[u]:
        if v not in visited:
            visited.add(v)
            queue.append((v, d + 1))

# 격자 4방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
```

### 다이나믹 프로그래밍 — 최적 부분 구조 + 중복 부분 문제

```python
# Top-down (메모이제이션)
from functools import lru_cache
@lru_cache(maxsize=None)
def f(state):
    if base(state):
        return base_value
    return min(f(next) + cost for next in transitions(state))

# Bottom-up (타뷸레이션)
dp = [0] * (n + 1)
dp[0] = base
for i in range(1, n + 1):
    dp[i] = max(dp[i-1] + a[i], dp[i-2] + b[i])  # 점화식
```

### 최단 경로 — 다익스트라 / 플로이드-워셜

```python
# 다익스트라: 단일 출발점, 음수 가중치 X, O(E log V)
import heapq
dist = [float('inf')] * (n + 1); dist[s] = 0
pq = [(0, s)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

# 플로이드-워셜: 모든 쌍, V ≤ 500, O(V^3)
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

### 투 포인터 / 슬라이딩 윈도우 — $O(N^2)$ → $O(N)$ 최적화

```python
# 투 포인터: 정렬된 배열의 양 끝
left, right = 0, len(arr) - 1
while left < right:
    s = arr[left] + arr[right]
    if s == target: return (left, right)
    elif s < target: left += 1
    else: right -= 1

# 슬라이딩 윈도우: 가변 구간
left = 0
window = 0
for right in range(len(arr)):
    window += arr[right]
    while window > limit:
        window -= arr[left]
        left += 1
    answer = max(answer, right - left + 1)
```

### 구현 / 시뮬레이션 — 좌표·방향·조건 분기

```python
# 좌표 매핑
pos = {key: (r, c) for ...}
manhattan = abs(r1-r2) + abs(c1-c2)

# 회전/방향 전환
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]   # 북동남서 순환
direction = (direction + 1) % 4          # 시계방향 회전
```

<br>

---

## 1. 해시(Hash)

### 핵심 아이디어

해시 테이블은 **키(key)를 해시 함수로 변환하여 값(value)에 빠르게 접근**하는 자료구조다.

평균적으로 탐색, 삽입, 삭제 모두 $O(1)$의 시간 복잡도를 가진다. Python에서는 `dict`와 `set`이 해시 테이블 기반으로 구현되어 있다.

"특정 값의 존재 여부를 빠르게 확인해야 하는 문제"나 "빈도수를 세는 문제"에서 해시를 떠올려야 한다.

### 대표 문제: [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) (프로그래머스, Level 1)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42576
```

마라톤에 참여한 선수 목록 `participant`와 완주한 선수 목록 `completion`이 주어질 때, 완주하지 못한 선수의 이름을 반환하는 문제다.

```python
from collections import Counter

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]
```

`collections.Counter`는 해시 맵 기반의 빈도수 카운터다. 참가자의 빈도에서 완주자의 빈도를 빼면, 남는 이름이 완주하지 못한 선수가 된다. `Counter` 간의 뺄셈은 양수인 카운트만 남기므로, 결과에는 정확히 하나의 이름만 남는다.

**시간 복잡도:** $O(N)$

**추가 연습 문제:**

- 프로그래머스 [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) (Level 2) — 해시 셋을 이용한 접두어 판별

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42577
```
- LeetCode [Two Sum](https://leetcode.com/problems/two-sum/) (#1) — 해시 맵으로 보수(complement) 탐색

```preview
https://leetcode.com/problems/two-sum/
```

<br>

---

## 2. 완전 탐색(브루트포스) & 백트래킹

### 핵심 아이디어

완전 탐색은 **가능한 모든 경우의 수를 탐색**하여 답을 찾는 방법이다.

입력 크기가 작을 때(N ≤ 20) 사용할 수 있으며, 순열·조합·부분집합 등의 형태로 나타난다.

백트래킹은 탐색 중 유망하지 않은 경로를 조기에 차단(pruning)하여 효율을 높인 완전 탐색이다.

### 대표 문제: [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) (프로그래머스, Level 2)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42839
```

각 자리 숫자가 적힌 종이 조각 `numbers`가 주어질 때, 종이 조각으로 만들 수 있는 소수의 개수를 반환하는 문제다.

```python
from itertools import permutations

def solution(numbers):
    candidates = set()
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            candidates.add(int(''.join(perm)))

    count = 0
    for num in candidates:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count
```

`itertools.permutations`로 가능한 모든 길이의 순열을 생성하고, `set`으로 중복을 제거한다.

각 후보 숫자에 대해 $\sqrt{N}$까지 나누어 소수인지 판별한다.

`numbers`의 길이가 최대 7이므로 순열의 총 수가 충분히 작아 완전 탐색이 가능하다.

**시간 복잡도:** $O(N! \times \sqrt{M})$ — N은 숫자 개수, M은 생성된 수의 최댓값.

**추가 연습 문제:**

- 프로그래머스 [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840) (Level 1) — 패턴 반복 완전 탐색

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42840
```

- LeetCode [Subsets](https://leetcode.com/problems/subsets/) (#78) — 백트래킹으로 부분집합 생성

```preview
https://leetcode.com/problems/subsets/
```

<br>

---

## 3. 그리디(탐욕법)

### 핵심 아이디어

그리디 알고리즘은 **각 단계에서 지역적으로 최적인 선택을 반복**하여 전역 최적해에 도달하는 방법이다.

그리디가 올바르게 동작하려면 **탐욕적 선택 속성(greedy choice property)**과 **최적 부분 구조(optimal substructure)**를 만족해야 한다.

직관적으로 쉬워 보이지만, 그리디 전략이 최적해를 보장하는지 검증하는 것이 핵심이다.

### 대표 문제: [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) (프로그래머스, Level 2)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42883
```

숫자로 이루어진 문자열 `number`에서 `k`개의 숫자를 제거하여 만들 수 있는 가장 큰 수를 반환하는 문제다.

```python
def solution(number, k):
    stack = []
    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)
```

스택을 활용한 그리디 풀이다. 숫자를 앞에서부터 순회하면서, 스택의 top보다 현재 숫자가 크면 top을 제거한다.

이렇게 하면 앞자리에 항상 가능한 한 큰 숫자가 배치된다.

남은 제거 횟수가 있으면 뒤에서부터 잘라낸다.

**시간 복잡도:** $O(N)$ — 각 숫자는 스택에 최대 한 번 push, 한 번 pop된다.

**추가 연습 문제:**

- 프로그래머스 [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862) (Level 1) — 정렬 후 인접 탐색 그리디

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42862
```

<br>

---

## 4. 정렬 기반 문제

### 핵심 아이디어

Python의 `sort()`와 `sorted()`는 Timsort 알고리즘을 사용하며, 시간 복잡도는 $O(N \log N)$이다.

비교 기반 정렬의 이론적 하한이 $O(N \log N)$이므로 이는 최적이다.

정렬 문제의 핵심은 **커스텀 정렬 기준을 설계**하는 것이다.

### 대표 문제: [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) (프로그래머스, Level 2)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42746
```

정수 배열 `numbers`가 주어질 때, 숫자를 이어 붙여 만들 수 있는 가장 큰 수를 반환하는 문제다.

```python
from functools import cmp_to_key

def solution(numbers):
    str_nums = list(map(str, numbers))
    str_nums.sort(key=cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
    result = ''.join(str_nums)
    return '0' if result[0] == '0' else result
```

두 숫자 a, b를 이어 붙인 "ab"와 "ba"를 비교하여 더 큰 쪽이 앞에 오도록 정렬한다.

예를 들어 6과 10이 있으면 "610" > "106"이므로 6이 앞에 온다.

`cmp_to_key`를 사용해 비교 함수를 정렬 키로 변환한다.

모든 숫자가 0인 경우 "000..."이 아닌 "0"을 반환하는 예외 처리가 필요하다.

**시간 복잡도:** $O(N \log N)$

**추가 연습 문제:**

- 프로그래머스 [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) (Level 2) — 정렬 후 조건 탐색

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42747
```

<br>

---

## 5. 이분 탐색(Binary Search) & 파라메트릭 서치

### 핵심 아이디어

이분 탐색은 **정렬된 데이터에서 탐색 범위를 절반씩 줄여나가는** 방법으로, $O(\log N)$의 시간 복잡도를 가진다.

파라메트릭 서치는 **최적화 문제를 결정 문제로 변환**하여 이분 탐색을 적용하는 기법이다.

"최솟값의 최댓값" 또는 "최댓값의 최솟값"을 구하는 문제에서 파라메트릭 서치를 떠올려야 한다.

### 대표 문제: [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) (프로그래머스, Level 3)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/43238
```

n명의 사람이 입국심사를 받을 때, 각 심사관의 심사 시간 배열 `times`가 주어진다. 모든 사람이 심사를 받는 데 걸리는 최소 시간을 반환한다.

```python
def solution(n, times):
    left, right = 1, max(times) * n
    answer = right
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times)
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
```

"주어진 시간 mid 동안 최대 몇 명을 심사할 수 있는가?"라는 결정 문제로 변환한다.

각 심사관이 mid 시간 동안 처리할 수 있는 인원은 `mid // t`이고, 이를 합산하면 전체 처리 인원이 된다.

처리 가능 인원이 n 이상이면 시간을 줄이고, 부족하면 시간을 늘린다.

**시간 복잡도:** $O(M \log(T \times N))$ — M은 심사관 수, T는 최대 심사 시간.

- Python `bisect` 모듈을 활용하면 정렬된 리스트에서 이분 탐색을 간결하게 구현할 수 있다

<br>

---

## 6. DFS / BFS (깊이·너비 우선 탐색)

### 핵심 아이디어

DFS(깊이 우선 탐색)는 한 경로를 끝까지 탐색한 뒤 되돌아오는 방식이고, BFS(너비 우선 탐색)는 가까운 노드부터 차례로 탐색하는 방식이다.

**BFS는 가중치가 없는 그래프에서 최단 경로를 보장**하므로, 최단 거리 문제에서는 BFS를 사용한다.

DFS는 모든 경로를 탐색하거나 경우의 수를 세야 하는 문제에 적합하다.

### 대표 문제 1: [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) (프로그래머스, Level 2) — DFS

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/43165
```

정수 배열 `numbers`의 각 원소에 +나 -를 붙여 합이 `target`이 되는 경우의 수를 구한다.

```python
def solution(numbers, target):
    count = 0

    def dfs(index, current_sum):
        nonlocal count
        if index == len(numbers):
            if current_sum == target:
                count += 1
            return
        dfs(index + 1, current_sum + numbers[index])
        dfs(index + 1, current_sum - numbers[index])

    dfs(0, 0)
    return count
```

각 숫자에 대해 +와 - 두 가지 선택지가 있으므로, 이진 트리 형태의 DFS를 수행한다.

리프 노드에 도달했을 때 합이 target과 같으면 카운트를 증가시킨다.

`numbers`의 길이가 최대 20이므로 최대 $2^{20}$ ≈ 100만 개의 경우를 탐색한다.

**시간 복잡도:** $O(2^N)$

### 대표 문제 2: [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) (프로그래머스, Level 2) — BFS

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/1844
```

n×m 크기의 게임 맵에서 (0,0)부터 (n-1, m-1)까지의 최단 거리를 구한다. 1은 이동 가능, 0은 벽이다.

```python
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0, 1)])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y, dist = queue.popleft()
        if x == n - 1 and y == m - 1:
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1
```

`collections.deque`의 `popleft()`는 $O(1)$이므로 BFS에 적합하다.

4방향으로 인접 칸을 탐색하면서, 방문하지 않은 벽이 아닌 칸을 큐에 추가한다.

BFS이므로 목적지에 처음 도달한 시점의 거리가 최단 거리다.

**시간 복잡도:** $O(N \times M)$

**추가 연습 문제:**

- 프로그래머스 [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) (Level 3) — DFS로 연결 요소 개수 세기

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/43162
```

<br>

---

## 7. 다이나믹 프로그래밍(DP)

### 핵심 아이디어

DP는 **최적 부분 구조(optimal substructure)**와 **중복 부분 문제(overlapping subproblems)**를 가진 문제에 적용하는 기법이다.

큰 문제를 작은 부분 문제로 나누어 풀고, 결과를 저장(메모이제이션)하여 반복 계산을 피한다.

**점화식을 세우는 것**이 DP 풀이의 핵심이다.

DP 접근법은 크게 두 가지로 나뉜다:

- **Top-down (메모이제이션):** 재귀로 큰 문제에서 작은 문제로 내려가며, 이미 계산한 결과를 캐싱한다.
- **Bottom-up (타뷸레이션):** 작은 문제부터 순서대로 풀어 올라간다. 반복문으로 구현하며, 스택 오버플로우 걱정이 없다.

### 대표 문제: [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) (프로그래머스, Level 3)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/43105
```

삼각형의 꼭대기에서 바닥까지 이동하면서 거쳐간 숫자의 합의 최댓값을 구한다.

현재 위치에서 대각선 왼쪽 또는 오른쪽으로만 이동할 수 있다.

```python
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][-1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    return max(triangle[-1])
```

Bottom-up 방식의 풀이다.

각 위치에서의 최대 합은 "위쪽 왼쪽"과 "위쪽 오른쪽" 중 더 큰 값에 현재 값을 더한 것이다.

양쪽 끝은 올 수 있는 경로가 하나뿐이므로 별도 처리한다. 마지막 행의 최댓값이 답이다.

**점화식:** `dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])`

**시간 복잡도:** $O(N^2)$ — N은 삼각형의 높이.

**추가 연습 문제:**

- LeetCode [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (#70) — 피보나치 형태의 기본 DP

```preview
https://leetcode.com/problems/climbing-stairs/
```

- 프로그래머스 [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895) (Level 3) — 집합 기반 DP

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/42895
```

<br>

---

## 8. 최단 경로 (다익스트라, 플로이드-워셜)

### 핵심 아이디어

가중치가 있는 그래프에서 최단 경로를 구하는 대표 알고리즘은 **다익스트라(Dijkstra)**와 **플로이드-워셜(Floyd-Warshall)**이다.

- **다익스트라:** 하나의 출발점에서 다른 모든 노드까지의 최단 경로. 우선순위 큐 사용 시 $O(E \log V)$. **음수 가중치가 있으면 사용할 수 없다**.
- **플로이드-워셜:** 모든 노드 쌍 간의 최단 경로. $O(V^3)$이므로 노드 수가 적을 때(V ≤ 500) 사용한다.

### 대표 문제: [배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978) (프로그래머스, Level 2)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/12978
```


N개의 마을과 양방향 도로가 주어질 때, 1번 마을에서 K 시간 이내로 배달할 수 있는 마을의 수를 구한다.

```python
import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for next_node, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return sum(1 for d in dist if d <= K)
```

다익스트라 알고리즘의 전형적인 구현이다.

`heapq` 모듈은 최소 힙을 제공하므로, 항상 현재까지의 최단 거리가 가장 작은 노드를 먼저 처리한다.

`d > dist[node]` 조건으로 이미 더 짧은 경로가 발견된 노드는 건너뛴다.

최종적으로 dist 배열에서 K 이하인 마을의 수를 세면 된다.

**시간 복잡도:** $O(E \log V)$

<br>

---

## 9. 투 포인터 & 슬라이딩 윈도우

### 핵심 아이디어

**투 포인터**는 정렬된 배열에서 두 개의 포인터를 사용하여 $O(N)$에 탐색하는 기법이다.

**슬라이딩 윈도우**는 고정 또는 가변 크기의 구간을 이동시키며 구간 내의 정보를 효율적으로 갱신하는 기법이다.

두 기법 모두 이중 반복문 $O(N^2)$을 단일 반복문 $O(N)$으로 최적화하는 데 사용한다.

### 대표 문제: [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (LeetCode #167)

```preview
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
```

정렬된 정수 배열 `numbers`에서 합이 `target`인 두 수의 인덱스(1-based)를 반환하는 문제다.

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

배열이 정렬되어 있으므로 양쪽 끝에서 포인터를 시작한다.

합이 target보다 작으면 left를 오른쪽으로, 크면 right를 왼쪽으로 이동한다.

정렬된 배열의 성질을 활용하므로 매 단계에서 탐색 범위가 줄어들고, 한 번의 순회로 답을 찾을 수 있다.

**시간 복잡도:** $O(N)$

<br>

---

## 10. 구현 / 시뮬레이션

### 핵심 아이디어

구현 문제는 특별한 알고리즘 없이 **문제에서 요구하는 동작을 정확히 코드로 옮기는** 유형이다.

복잡한 조건 분기, 좌표 계산, 문자열 처리 등이 포함된다.

알고리즘 자체보다 **꼼꼼한 구현**과 **엣지 케이스 처리**가 핵심이다.

### 대표 문제: [키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256) (프로그래머스, Level 1)

```preview
https://school.programmers.co.kr/learn/courses/30/lessons/67256
```

전화 키패드에서 눌러야 할 번호 배열이 주어질 때, 각 번호를 왼손/오른손 중 어느 손으로 누르는지 결정한다.

1, 4, 7은 왼손, 3, 6, 9는 오른손, 가운데 열(2, 5, 8, 0)은 더 가까운 손을 사용하며, 거리가 같으면 주로 쓰는 손을 사용한다.

```python
def solution(numbers, hand):
    pos = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2),
           7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}
    left, right = pos['*'], pos['#']
    result = []

    for num in numbers:
        target = pos[num]
        if num in (1, 4, 7):
            result.append('L'); left = target
        elif num in (3, 6, 9):
            result.append('R'); right = target
        else:
            ld = abs(target[0]-left[0]) + abs(target[1]-left[1])
            rd = abs(target[0]-right[0]) + abs(target[1]-right[1])
            if ld < rd or (ld == rd and hand == 'left'):
                result.append('L'); left = target
            else:
                result.append('R'); right = target
    return ''.join(result)
```

각 키의 좌표를 딕셔너리에 미리 저장한다.

왼쪽/오른쪽 열은 무조건 해당 손으로 누르고, 가운데 열은 맨해튼 거리를 계산하여 가까운 손을 선택한다.

거리가 같으면 `hand` 파라미터에 따라 결정한다.

**시간 복잡도:** $O(N)$

<br>

---

## 유형별 시간 복잡도 요약

| 유형 | 대표 시간 복잡도 | 핵심 자료구조/도구 |
|------|----------------|------------------|
| 해시 | $O(N)$ | `dict`, `set`, `Counter` |
| 완전 탐색 | $O(N!)$ 또는 $O(2^N)$ | `itertools`, 재귀 |
| 그리디 | 문제에 따라 다름 | 스택, 정렬 |
| 정렬 | $O(N \log N)$ | `sort()`, `cmp_to_key` |
| 이분 탐색 | $O(\log N)$ | `bisect` |
| DFS / BFS | $O(V + E)$ | 재귀, `deque` |
| DP | 문제에 따라 다름 | 배열, 딕셔너리 |
| 최단 경로 | $O(E \log V)$ / $O(V^3)$ | `heapq` |
| 투 포인터 | $O(N)$ | 두 포인터 변수 |
| 구현 | 문제에 따라 다름 | — |

<br>

---

## 마무리 — 효과적인 학습 순서와 연습 전략

알고리즘 유형을 학습할 때는 다음 순서를 추천한다:

1. **해시, 정렬, 완전 탐색** — 기본기를 다지는 단계. 문제를 읽고 코드로 옮기는 연습에 집중한다.
2. **DFS/BFS, 그리디** — 그래프 탐색과 최적화 문제의 기본을 익힌다.
3. **DP, 이분 탐색** — 가장 출제 빈도가 높고 난이도가 있는 유형이다. 점화식 세우기와 파라메트릭 서치를 충분히 연습한다.
4. **최단 경로, 투 포인터** — 위 유형을 익힌 후 확장하면 자연스럽게 이해할 수 있다.

원래라면 포스팅에 백준 문제 링크를 달 예정이었는데 백준이 섭종해서...

그래서 최근에는 프로그래머스를 중심으로 유형별 풀이를 통해 알고리즘 문제 풀이 역량을 쌓고 있고, 추가로 여유가 된다면 LeetCode까지 확장해서 풀이해나갈 예정이다.

개인적으로는 한 유형에 5~10문제를 집중적으로 풀어 패턴을 체화한 뒤 다음 유형으로 넘어가는 것이 좋은 것 같았다.

<br>

---

## 회고

입력 크기(N)로 알고리즘을 추론하는 방법은 이 글을 정리하면서 새삼 체계적으로 다시 보게 된 부분이다.

처음에는 약간 야매 같은 느낌에 "이런 식으로 접근하는 게 맞나?" 싶었는데, 실제로 이 방법은 경쟁 프로그래밍 커뮤니티에서 널리 쓰이는 전략이라고 한다.

나동빈의 "이것이 취업을 위한 코딩 테스트다"를 비롯한 여러 알고리즘 학습 자료에서도 N 기반 시간 복잡도 추론을 첫 번째 전략으로 소개하고 있다.

문제를 보자마자 N의 범위를 확인하고 허용 가능한 알고리즘을 좁혀가는 습관은, 한 번 체화하면 문제 접근 속도를 확실히 끌어올려 준다.
