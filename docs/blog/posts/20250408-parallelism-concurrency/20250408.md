---
title: '[Computer Science] 병렬성과 동시성의 차이'
description: 병렬성(Parallelism)과 동시성(Concurrency)의 개념과 차이점 이해하기
authors:
  - bnbong
date:
  created: 2025-04-08
  updated: 2025-04-08
categories:
  - Computer Science
tags:
  - Algorithms
  - Concurrency
  - Parallelism
  - Computer Science
comments: true
---

## 개요

최근 기술 면접을 준비하면서 병렬성(Parallelism)과 동시성(Concurrency)의 차이에 대한 질문을 자주 접하게 되었다.

두 용어는 비슷해 보이지만 명확하게 다른 개념이며, 실제 개발에서도 이 차이를 이해하는 것이 매우 중요하다.

이번 포스팅에서는 병렬성과 동시성의 개념과 차이점, 그리고 관련된 다른 개념들에 대해 정리해보고자 한다.


## 1. 병렬성(Parallelism)이란?

**병렬성**은 여러 작업을 ==물리적으로 동시에 실행==하는 것을 의미한다.

멀티 코어 시스템에서 각 코어가 독립적으로 작업을 처리하여 실제로 같은 시간에 여러 작업이 진행되는 것을 말한다.

즉, 병렬성은 **실제로 여러 작업이 동시에 실행**되는 것이다.

### 병렬성의 특징

- **하드웨어 의존적**: 멀티 코어, 멀티 프로세서 시스템, GPU, 또는 네트워크로 연결된 분산 컴퓨팅 환경이 필요하다. 반드시 단일 머신의 멀티 코어에만 한정되지 않으며, 여러 물리적 장치를 활용할 수도 있다.
- **실제 동시 실행**: 여러 작업이 같은 시간에 물리적으로 실행된다.
- **성능 향상**: 작업을 나누어 처리하므로 전체 처리 시간이 단축된다.
- **CPU 집약적 작업**에 적합: 계산, 데이터 처리 등의 작업에 효과적이다.

### 병렬성 예시

레스토랑에서 여러 명의 요리사가 각자 다른 요리를 동시에 만드는 상황을 생각해보자.

요리사 A는 파스타를 만들고, 요리사 B는 스테이크를 굽고, 요리사 C는 샐러드를 준비한다. 이들은 각자의 조리대에서 실제로 동시에 작업을 수행하고 있다.

이것이 바로 병렬성이다.

---

## 2. 동시성(Concurrency)이란?

**동시성**은 여러 작업을 ==논리적으로 동시에 처리==하는 것을 의미한다.

싱글 코어 환경에서는 작업들을 빠르게 전환하면서 마치 동시에 실행되는 것처럼 보이게 하고, 멀티 코어 환경에서는 실제 병렬 실행과 함께 나타날 수도 있다. 핵심은 동시성이 **여러 작업을 효율적으로 다루는 구조적 접근 방법**이라는 점이다.

### 동시성의 특징

- **하드웨어 독립적**: 싱글 코어 시스템에서도 구현 가능하다. 멀티 코어에서는 병렬성과 함께 나타날 수 있다.
- **논리적 동시 처리**: 작업들이 시간을 나누어 가며 실행되거나(Time Slicing), 여러 코어에서 독립적으로 실행될 수 있다.
- **응답성 향상**: 사용자 인터페이스가 멈추지 않고 반응할 수 있다.
- **I/O 집약적 작업**에 적합: 네트워크 요청, 파일 읽기/쓰기 등의 작업에 효과적이다.

### 동시성 예시

한 명의 요리사가 여러 요리를 번갈아가며 만드는 상황을 생각해보자.

요리사는 파스타 물을 끓이는 동안 스테이크를 굽고, 스테이크가 익는 동안 샐러드를 준비한다. 실제로는 한 번에 하나의 작업만 하지만, 작업들을 효율적으로 전환하면서 여러 요리를 동시에 진행하는 것처럼 보인다.

이것이 바로 동시성이다.

<!-- more -->

---

## 3. 병렬성과 동시성의 핵심 차이

| 구분 | 병렬성 (Parallelism) | 동시성 (Concurrency) |
|------|---------------------|---------------------|
| **정의** | 여러 작업을 실제로 동시에 실행 | 여러 작업을 논리적으로 동시에 처리 |
| **실행 방식** | 물리적으로 동시 실행 | 시간을 나누어 실행하거나 병렬 실행과 결합 |
| **하드웨어 요구사항** | 멀티 코어/프로세서/GPU/분산 환경 필요 | 싱글 코어에서도 가능, 멀티 코어와도 호환 |
| **목적** | 성능 향상 (처리 시간 단축) | 응답성 향상 (효율적인 자원 활용) |
| **적합한 작업** | CPU 집약적 작업 | I/O 집약적 작업 |
| **예시** | 여러 명의 요리사가 각자 요리 | 한 명의 요리사가 여러 요리를 번갈아 진행 |

### Rob Pike의 명언

Go 언어를 만든 Rob Pike는 동시성과 병렬성의 차이를 다음과 같이 정의했다:

> "Concurrency is about **dealing with** lots of things at once.
> Parallelism is about **doing** lots of things at once."

즉, 동시성은 여러 작업을 **다루는 방법**이고, 병렬성은 여러 작업을 **실제로 수행**하는 것이다.

---

## 4. 관련 개념들

다음 내용은 병렬성과 동시성과 관련된 파생 개념들이다. 필자는 개발자 지망생이므로(ㅋㅋ) 각 개념들에 대한 간단한 코드 예시까지 첨부해보았다. 개념의 단순 구현에만 집중했으므로 오류가 있을 수 있으니 로직 흐름정도만 이해하고 넘어가기를 양해 바란다.

### 4.1 프로세스(Process)와 스레드(Thread)

병렬성과 동시성을 이해하기 위해서는 프로세스와 스레드의 개념을 알아야 한다.

#### 프로세스(Process)

- 운영체제로부터 자원을 할당받는 **작업의 단위**
- 독립적인 메모리 공간을 가진다
- 프로세스 간에는 메모리를 공유하지 않는다
- 생성/종료에 많은 비용이 든다

#### 스레드(Thread)

- 프로세스 내에서 실행되는 **실행 흐름의 단위**
- 같은 프로세스 내의 스레드들은 메모리를 공유한다
- 프로세스보다 생성/전환 비용이 적다
- 경량 프로세스(Lightweight Process)라고도 한다

```python
import threading
import multiprocessing
import time

# 스레드를 사용한 동시성 예제
def task_with_thread(name):
    print(f"Thread {name}: 시작")
    time.sleep(2)
    print(f"Thread {name}: 종료")

threads = []
for i in range(3):
    thread = threading.Thread(target=task_with_thread, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("모든 스레드 작업 완료")

# 프로세스를 사용한 병렬성 예제
def task_with_process(name):
    print(f"Process {name}: 시작")
    time.sleep(2)
    print(f"Process {name}: 종료")

processes = []
for i in range(3):
    process = multiprocessing.Process(target=task_with_process, args=(i,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("모든 프로세스 작업 완료")
```

### 4.2 멀티스레딩(Multithreading)과 멀티프로세싱(Multiprocessing)

#### 멀티스레딩(Multithreading)

- 하나의 프로세스 내에서 여러 스레드를 생성하여 작업을 처리
- 메모리를 공유하므로 데이터 공유가 쉽다
- **동시성**을 구현하는 주요 방법 중 하나
- 일반적으로 멀티 코어 환경에서는 병렬 실행이 가능하지만, Python의 경우 GIL(Global Interpreter Lock) 때문에 한 번에 하나의 스레드만 Python 바이트코드를 실행할 수 있어 CPU 집약적 작업에서는 실질적인 병렬 실행이 불가능하다

#### 멀티프로세싱(Multiprocessing)

- 여러 프로세스를 생성하여 작업을 처리
- 독립적인 메모리 공간을 가지므로 안전하지만 통신 비용이 크다
- **병렬성**을 구현하는 방법
- CPU 집약적 작업에서 실제로 성능 향상을 얻을 수 있다

```python
import threading
import multiprocessing
import time

# CPU 집약적 작업 예제
def cpu_intensive_task(n):
    """CPU 집약적 작업: 소수 찾기"""
    count = 0
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

# 멀티스레딩 (동시성) - GIL로 인해 성능 향상 제한적
def test_multithreading():
    start = time.time()
    threads = []
    for _ in range(4):
        thread = threading.Thread(target=cpu_intensive_task, args=(100000,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"멀티스레딩 소요 시간: {time.time() - start:.2f}초")

# 멀티프로세싱 (병렬성) - 실제 성능 향상
def test_multiprocessing():
    start = time.time()
    processes = []
    for _ in range(4):
        process = multiprocessing.Process(target=cpu_intensive_task, args=(100000,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"멀티프로세싱 소요 시간: {time.time() - start:.2f}초")

# 순차 실행
def test_sequential():
    start = time.time()
    for _ in range(4):
        cpu_intensive_task(100000)
    print(f"순차 실행 소요 시간: {time.time() - start:.2f}초")

if __name__ == "__main__":
    print("=== CPU 집약적 작업 성능 비교 ===")
    test_sequential()
    test_multithreading()
    test_multiprocessing()
```

### 4.3 컨텍스트 스위칭(Context Switching)

**컨텍스트 스위칭**은 CPU가 현재 실행 중인 프로세스나 스레드를 중단하고 다른 프로세스나 스레드를 실행하도록 전환하는 과정이다.

이는 동시성 구현의 핵심 메커니즘일 뿐만 아니라, 병렬성 환경(멀티프로세서/멀티코어)에서도 운영체제의 스케줄링에 의해 발생한다. 즉, 동시성과 병렬성 모두에서 나타나는 현상이다.

#### 컨텍스트 스위칭 과정

1. 현재 실행 중인 작업의 상태(레지스터, 프로그램 카운터 등)를 저장
2. 다음에 실행할 작업의 상태를 복원
3. 새로운 작업을 실행

#### 컨텍스트 스위칭의 비용

- CPU 사이클 소모
- 캐시 무효화
- 메모리 접근 지연

너무 빈번한 컨텍스트 스위칭은 오히려 성능을 저하시킬 수 있다.

### 4.4 동기(Synchronous)와 비동기(Asynchronous)

비동기 프로그래밍은 I/O 대기 시간을 효율적으로 활용하여 동시성을 구현하는 유용한 방법 중 하나이다.

#### 동기(Synchronous)

- 작업이 완료될 때까지 대기
- 순차적으로 실행
- 코드 흐름이 명확하고 이해하기 쉽다

#### 비동기(Asynchronous)

- 작업 완료를 기다리지 않고 다음 작업 수행
- 작업 완료 시 콜백이나 이벤트로 알림
- 효율적인 자원 활용

```python
import asyncio
import time

# 동기 방식
def sync_task(name, delay):
    print(f"{name} 시작")
    time.sleep(delay)  # 블로킹
    print(f"{name} 완료")
    return f"{name} 결과"

def run_sync():
    start = time.time()
    sync_task("작업 1", 2)
    sync_task("작업 2", 2)
    sync_task("작업 3", 2)
    print(f"동기 실행 시간: {time.time() - start:.2f}초")  # 약 6초

# 비동기 방식
async def async_task(name, delay):
    print(f"{name} 시작")
    await asyncio.sleep(delay)  # 논블로킹
    print(f"{name} 완료")
    return f"{name} 결과"

async def run_async():
    start = time.time()
    await asyncio.gather(
        async_task("작업 1", 2),
        async_task("작업 2", 2),
        async_task("작업 3", 2)
    )
    print(f"비동기 실행 시간: {time.time() - start:.2f}초")  # 약 2초

if __name__ == "__main__":
    print("=== 동기 vs 비동기 ===")
    run_sync()
    print()
    asyncio.run(run_async())
```

### 4.5 블로킹(Blocking)과 논블로킹(Non-blocking)

#### 블로킹(Blocking)

- 작업이 완료될 때까지 제어권을 반환하지 않음
- 호출한 함수가 대기 상태에 머무름

#### 논블로킹(Non-blocking)

- 작업 완료 여부와 관계없이 즉시 제어권을 반환
- 호출한 함수가 다른 작업을 계속 수행할 수 있음

```python
import socket
import time

# 블로킹 소켓
def blocking_socket_example():
    print("블로킹 소켓 예제")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('www.google.com', 80))
    sock.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')

    # 데이터를 받을 때까지 블로킹
    data = sock.recv(4096)
    print("데이터 수신 완료")
    sock.close()

# 논블로킹 소켓
def nonblocking_socket_example():
    print("논블로킹 소켓 예제")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)  # 논블로킹 모드 설정

    try:
        sock.connect(('www.google.com', 80))
    except BlockingIOError:
        # 연결이 진행 중이지만 블로킹하지 않음
        print("연결 진행 중...")

    # 다른 작업을 수행할 수 있음
    time.sleep(1)

    try:
        sock.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
        data = sock.recv(4096)
        print("데이터 수신 완료")
    except BlockingIOError:
        print("아직 준비되지 않음")
    finally:
        sock.close()
```

---

## 5. 언제 병렬성을, 언제 동시성을 사용할까?

### 병렬성(Parallelism)을 사용해야 하는 경우

- **CPU 집약적 작업**: 이미지 처리, 동영상 인코딩, 과학 계산, 머신러닝 학습 등
- **대용량 데이터 처리**: 데이터 분석, 배치 처리 등
- **멀티 코어를 최대한 활용**하고 싶을 때

```python
from multiprocessing import Pool
import time

def process_image(image_path):
    """이미지 처리 작업 (CPU 집약적)"""
    # 실제로는 PIL, OpenCV 등을 사용
    time.sleep(0.1)  # 처리 시간 시뮬레이션
    return f"Processed: {image_path}"

if __name__ == "__main__":
    image_paths = [f"image_{i}.jpg" for i in range(100)]

    # 병렬 처리 (멀티프로세싱)
    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(process_image, image_paths)
    print(f"병렬 처리 시간: {time.time() - start:.2f}초")
```

### 동시성(Concurrency)을 사용해야 하는 경우

- **I/O 집약적 작업**: 웹 크롤링, API 호출, 데이터베이스 쿼리, 파일 읽기/쓰기 등
- **사용자 인터페이스**: UI가 멈추지 않도록 백그라운드 작업 처리
- **대기 시간이 많은 작업**: 네트워크 통신, 외부 서비스 호출 등

```python
import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    """비동기 HTTP 요청 (I/O 집약적)"""
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls():
    urls = [
        'https://www.google.com',
        'https://www.github.com',
        'https://www.stackoverflow.com',
        'https://www.reddit.com',
        'https://www.twitter.com',
    ]

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    print(f"동시성 처리 시간: {time.time() - start:.2f}초")
    return results

if __name__ == "__main__":
    asyncio.run(fetch_multiple_urls())
```

---

## 6. Python의 GIL(Global Interpreter Lock)

Python에서 병렬성과 동시성을 다룰 때 반드시 알아야 할 개념이 **GIL(Global Interpreter Lock)**이다.

### GIL이란?

- Python 인터프리터가 한 번에 하나의 스레드만 Python 바이트코드를 실행하도록 보장하는 뮤텍스(mutex)
- 메모리 관리를 단순화하기 위해 도입되었다
- **멀티스레딩으로 CPU 집약적 작업을 병렬화할 수 없다**
- 다만, I/O 작업(네트워크 요청, 파일 읽기/쓰기 등) 중에는 GIL이 해제되므로 멀티스레딩이 여전히 응답성을 높이는 데 유용하다

### GIL의 영향

```python
import threading
import time

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# 싱글 스레드
start = time.time()
increment()
increment()
print(f"싱글 스레드: {time.time() - start:.2f}초, counter={counter}")

# 멀티 스레드
counter = 0
start = time.time()
threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"멀티 스레드: {time.time() - start:.2f}초, counter={counter}")
# GIL로 인해 멀티 스레드가 더 느릴 수 있음!
```

### GIL 우회 방법

1. **멀티프로세싱 사용**: 각 프로세스는 독립적인 GIL을 가진다
2. **C 확장 모듈 사용**: NumPy, Pandas 등은 내부적으로 GIL을 해제
3. **다른 Python 구현체 사용**: Jython, IronPython은 GIL이 없다

---

## 7. 결론

병렬성과 동시성은 현대 소프트웨어 개발에서 필수적인 개념이다.

- **병렬성(Parallelism)**: 여러 작업을 물리적으로 동시에 실행. CPU 집약적 작업에 적합.
- **동시성(Concurrency)**: 여러 작업을 논리적으로 동시에 처리. I/O 집약적 작업에 적합.

두 개념을 명확히 이해하고, 작업의 특성에 맞게 적절한 방법을 선택하는 것이 중요하다.

또한 프로세스, 스레드, 동기/비동기, 블로킹/논블로킹 등의 관련 개념들을 함께 이해하면 더욱 효과적인 프로그래밍이 가능하다.

---

## 참고 자료

- [Concurrency is not Parallelism - Rob Pike](https://go.dev/blog/waza-talk)
- [Python GIL (Global Interpreter Lock)](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
- [Real Python - Async IO in Python](https://realpython.com/async-io-python/)
- [Understanding the Python GIL](https://realpython.com/python-gil/)
