---
title: FEMU Monitoring
description: FEMU 내부에 WAF/Latency/Throughput 계측을 추가하고 Hot/Cold Data Separation까지 실험한 시스템 프로젝트
authors:
  - bnbong
tags:
  - C
  - FEMU
  - QEMU
  - SSD
  - personal
  - system
  - coursework
featured: true
period: 2024.09 - 2024.12
role: 개인 · 수업 과제 / 계측 모듈 설계 / FTL 수정 / 실험 정리
---

# FEMU Monitoring

## 개요

!!! tip "아이템 한줄 설명"
    QEMU 기반 SSD 에뮬레이터 FEMU 내부를 직접 수정해 SSD 내부 지표를 계측하고, Hot/Cold 분리 기법을 실험한 프로젝트

한양대학교 ERICA 시스템프로그래밍 과제로 수행한 프로젝트다. 단순히 에뮬레이터를 실행하는 데서 끝내지 않고, FEMU 내부 코드에 직접 손을 대어 **SSD 내부 동작을 측정할 수 있는 계측 지표**를 추가했다.
그 위에서 Hot/Cold Data Separation 기법까지 실험했다.

### 저장소

<https://github.com/bnbong/FEMU>

## 1차 작업: 계측 모듈 추가

### 문제

기본 FEMU만으로는 내가 보고 싶었던 지표를 바로 얻기 어려웠다. 특히 과제 목표가
"정책 변경 전후의 차이를 정량적으로 비교하는 것"이었기 때문에, 최소한 다음 값은 내부에서 직접 기록할 수 있어야 했다:

- Host write 대비 NAND write 비율인 WAF
- 처리량 변화
- I/O 지연시간

### 설계

계측 모듈은 SSD 내부 경로를 크게 바꾸지 않고, 기존 입출력 흐름에 측정 포인트를 삽입하는 방향으로
구성했다.

- host write 수와 internal write 수를 누적해 WAF 계산
- 요청 제출 시점과 완료 시점을 기록해 latency 계산
- 일정 구간 동안 완료된 I/O 수를 기반으로 throughput 산출
- 후속 정책 실험에서 재사용할 수 있도록 계측 로직을 기능 로직과 최대한 분리

가장 중요했던 건 **기존 FTL 동작을 망가뜨리지 않는 것**이었다. 측정 자체가
시스템 동작을 왜곡해 버리면 실험 의미가 사라져 버리기 때문이다. 이를 고려한 코드 덩어리 추가가 생각보다 까다로워서 적지 않은 시간을 쏟았다.

## 2차 작업: Hot/Cold Data Separation

앞서 만든 계측 모듈 위에서 이어서 진행한 작업이다. 두 작업은 동일 FEMU fork 위에서
하나의 프로젝트 흐름으로 연결되어 있다.

### 문제

플래시 SSD의 GC(Garbage Collection)는 유효 페이지를 이동한 뒤 블록을 지우는 구조다.
이때 자주 갱신되는 hot 데이터와 거의 바뀌지 않는 cold 데이터가 같은 블록에 섞이면,
GC 때마다 cold 페이지까지 반복해서 복사해야 하므로 불필요한 write amplification이 누적된다.

결과적으로

- WAF가 상승하고
- 유효 IOPS가 감소하며
- GC 비용이 사용자 체감 성능으로 이어진다

는 문제가 생긴다.

### 설계

이 문제를 줄이려고 hot/cold separation을 도입했고, write pointer를 단일 포인터가 아니라 두 개로 분리했다.

- `hot_wp`와 `cold_wp`를 분리해 서로 다른 블록 그룹으로 데이터 배치
- 쓰기 경로에서 접근 빈도 기반 threshold를 사용해 hot/cold를 판정
- GC 시 블록 내부의 hot/cold 혼입을 줄여 유효 페이지 복사량을 줄이는 방향 유도

## 실험 결과

동일 FEMU 환경에서 **Zipfian 1.2 워크로드** 기준으로 비교한 결과는 다음과 같다.

| 지표 | 기존 단일 write pointer | Hot/Cold 분리 |
|---|---:|---:|
| WAF | 4.2 ~ 4.3 | **2.7 ~ 2.9** |
| IOPS | 7,000 ~ 7,500 | **8,500 ~ 9,000** |

- WAF 약 **35% 감소**
- IOPS 약 **20% 개선**

## 역할

- FEMU 내부 계측 포인트 설계 및 구현
- WAF/Latency/Throughput 산출 로직 작성
- Hot/Cold write pointer 분리 정책 구현
- 실험 워크로드 설정 및 결과 비교 정리

## 배운 점

- **측정 가능해야 최적화할 수 있다**. 지표가 없을 때는 정책 효과를 설명할 수가 없었다.
- FTL 수정은 파급 범위가 크기 때문에, 변경 지점을 최소화하는 설계가 디버깅 비용을 크게 줄여 준다.
- 운영체제/파일시스템/에뮬레이터/스토리지 계층이 어떻게 연결되는지 몸으로 이해하게 된 프로젝트였다.
