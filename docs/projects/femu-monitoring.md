---
title: FEMU Monitoring
description: 가상 SSD emulator FEMU에 WAF/Throughput/Latency 계측 모듈을 추가하고 Hot/Cold Data Separation 기법을 구현한 프로젝트
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
role: 개인 · 수업 과제
---

# FEMU Monitoring

## 개요

가상 SSD emulator FEMU의 WAF, Throughput, Latency 등을 모니터링하는 모듈을 추가한 프로젝트

Hanyang Univ. ERICA Software Dept. lecture 시스템프로그래밍 과제 프로젝트이다.

### 저장소

<https://github.com/bnbong/FEMU>

## 소개

(종강 이후 추가 예정)

## 역할

- 모듈 개발

## Hot/Cold Data Separation

상단의 계측 모듈 위에서 수행된 후속 작업이다. 두 작업은 동일 FEMU fork 위에서
하나의 프로젝트 흐름으로 연결되어 있다.

### 문제

플래시 SSD의 GC(Garbage Collection)는 유효 페이지를 이동(copy)시킨 뒤 블록을 지우는 구조라,
"자주 바뀌는 페이지(hot)"와 "거의 바뀌지 않는 페이지(cold)"가 동일 블록에 섞여 있으면
GC 시마다 불필요한 cold 페이지 복사 비용이 누적되어 **WAF(Write Amplification Factor)** 가
상승하고 **유효 IOPS**가 떨어진다.

### 설계

- write pointer를 **`hot_wp` / `cold_wp` 2개로 분리**하여 hot/cold write를 서로 다른 블록
  그룹에 배치.
- FTL(Flash Translation Layer) 쓰기 경로에서 판정 기준(히트 빈도 기반 threshold)을
  가지고 write pointer를 선택.
- GC가 수행될 때 블록 내 hot/cold 혼입이 최소화되어 **유효 데이터 이동량**이 줄어듦.

### 결과

동일 FEMU 환경에서 **Zipfian 1.2 워크로드** 기준 비교:

| 지표 | 기존 단일 wp | Hot/Cold 분리 wp |
|---|---|---|
| WAF | 4.2 ~ 4.3 | **2.7 ~ 2.9** |
| IOPS | 7,000 ~ 7,500 | **8,500 ~ 9,000** |

- WAF **약 35% 감소**, IOPS **약 20% 개선**
- 계측 모듈(WAF/Throughput/Latency)이 이 실험 지표 수집의 기반이 되었음

### 배운 점

- **"측정 가능해야 최적화할 수 있다"** — 계측 모듈을 먼저 만들어 두었기 때문에, Hot/Cold 분리의
  효과를 정량적으로 비교할 수 있었다.
- FTL 내부 경로 수정은 파급 범위가 크므로, 수정 포인트를 최소 write path 한 군데로 좁힌 것이
  후속 디버깅 비용을 줄이는 데 결정적이었다.
