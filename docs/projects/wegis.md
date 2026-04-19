---
title: Wegis
description: 멀티모달 AI 기반 QR/URL 피싱 탐지 시스템 (MobileBERT + 1D-CNN, FastAPI 추론 서버)
authors:
  - bnbong
tags:
  - Python
  - FastAPI
  - PyTorch
  - OCI
  - Docker
  - ai
  - personal
  - backend
featured: true
period: 2025.09 - 2025.10
role: 개인 프로젝트 · AI 학습 / 서버 / 인프라 / 확장 프로그램 전반
---

# Wegis

## 개요

!!! tip "아이템 한줄 설명"
    멀티모달 AI 기반 QR/URL 피싱 탐지 시스템

QR 코드를 스캔하거나 URL을 붙여 넣으면 **이미지(QR 구조) + 텍스트(URL 문자열)** 를 동시에 분석해
피싱 여부를 판단하는 멀티모달 AI 서비스이다. 브라우저 확장 프로그램과 FastAPI 추론 서버,
그리고 PyTorch 기반 학습 파이프라인으로 구성되어 있다.

### 저장소

- Extension & Model training : <https://github.com/bnbong/Wegis>
- Inference Server : <https://github.com/bnbong/Wegis_server>

## 문제 정의

!!! warning
    - 기존 QR 피싱 탐지 연구는 URL 문자열 단일 피처만을 사용해 우회(단축 URL, homoglyph) 공격에 취약하다.
    - 이미지 기반 탐지는 QR 패턴을 임의로 조작한 경우 일반화가 어렵다.
    - 두 모달리티를 결합해 상호보완적인 판정이 필요하다고 보았다.

## 주요 역할

- 데이터셋 수집·전처리 파이프라인 설계 (URL + QR 이미지 페어링)
- MobileBERT(텍스트) + 1D-CNN(이미지 피처) 결합 멀티모달 분류 모델 학습
- FastAPI 추론 서버 구축 및 브라우저 확장과의 통신 규격 설계
- OCI 기반 인프라 설계·재구성 (Kubernetes → 단일 컨테이너 재설계)
- Chrome 확장 프로그램 개발 (QR 이미지 캡처, 서버 호출, 결과 렌더링)

## 핵심 설계 판단

### 1. 멀티모달 입력

URL 단일 입력 대비 **이미지 + 텍스트 페어링 입력**으로 얻는 일반화 이득이 크다고 판단하였다.
공격자가 URL 문자열을 위장하더라도 QR 패턴에 미묘한 차이가 남고, 반대로 QR 이미지 자체가 의도적으로
교란되더라도 텍스트 피처로 교정할 수 있다.

### 2. 모바일 친화 모델 — MobileBERT

BERT-base 대비 4배 가벼운 **MobileBERT**를 텍스트 인코더로 채택하여 추론 지연을 줄였다.
이미지 쪽은 파라미터 수가 적은 1D-CNN을 사용하여 두 인코더를 결합한 이후에도 단일 GPU/CPU에서
실시간 응답이 가능하도록 구성했다.

### 3. 체크포인트 서버 내 배치

모델 체크포인트를 외부 오브젝트 스토리지에서 매 요청마다 받아오지 않고 **컨테이너 이미지에 동봉**하여
콜드 스타트와 네트워크 홉을 제거했다. 모델 업데이트 주기가 길어 이 선택의 단점(이미지 크기 증가)보다
응답 속도 이득이 컸다.

### 4. Kubernetes → 단일 컨테이너 재설계

초기에는 OKE(Oracle Kubernetes Engine) 기반으로 설계했으나, 트래픽 수준과 개인 프로젝트 운영 비용을
고려했을 때 **단일 컨테이너(OCI Compute + Docker)** 가 훨씬 합리적이라고 판단해 재설계했다.
월 약 26,000원 수준이던 운영비를 **0원**(Always Free tier) 으로 떨어뜨렸다.

## Stack

### Model & Training

- Python 3.11
- PyTorch
- Hugging Face Transformers (MobileBERT)
- 1D-CNN (이미지 피처 추출)

### Inference Server

- Python 3.11
- FastAPI + Pydantic
- Docker

### Infra

- Oracle Cloud Infrastructure (Compute Always Free)
- Docker 단일 컨테이너 배포

### Extension

- Chrome Extension (Manifest V3)
- JavaScript

## 결과

- **F1 0.8739** (멀티모달 구성 기준, 단일 모달 대비 유의미한 향상)
- 추론 지연 **AVG −34.5% / p95 −43.6%** (Kubernetes 구성 대비 단일 컨테이너 구성)
- 운영비 **월 26,000원 → 0원**
- Chrome 확장 프로그램에서 실사용자 플로우(QR 스캔 → 서버 판정 → 경고 UI) 동작 확인

## 배운 점

- **"인프라는 트래픽이 정할 문제"** — 처음부터 Kubernetes를 올렸다가 재설계하는 과정을 통해,
  초기 트래픽과 운영 비용을 먼저 추정한 뒤 인프라 복잡도를 결정해야 한다는 것을 체감했다.
- **모달리티 결합 시 경량 모델 선택의 중요성** — 두 인코더를 합친 뒤 추론 지연이 선형으로 늘지
  않도록 각 브랜치의 파라미터 예산을 초기에 정해두는 편이 안전하다.
- **체크포인트 배치 전략** — 모델 업데이트 주기와 응답 속도 요구사항에 따라 스토리지/이미지 내장/온라인
  로딩 중 어떤 전략이 맞는지 판단하는 기준을 얻었다.
