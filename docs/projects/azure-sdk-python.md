---
title: Azure SDK Python
description: Azure SDK for Python 저장소에 코드 기여를 진행하며 OSS 기여 프로세스를 익힌 경험
authors:
  - bnbong
tags:
  - Python
  - Azure
  - Azure SDK
  - oss
  - backend
period: "2023"
role: 오픈소스 기여
---

# Azure SDK Python

## 개요

2023 OSSCA 활동 중 `Azure 클라우드 Python 오픈소스 SDK 도구 및 문서 팀`에 참여하며
Azure SDK for Python 저장소에 코드 기여를 진행했다.

### 저장소

<https://github.com/bnbong/azure-sdk-for-python>

## 기여 내용

- [:fontawesome-solid-code-pull-request: [Storage] Fixed cspell typos in storage-blob](https://github.com/Azure/azure-sdk-for-python/pull/31635)
- [:fontawesome-solid-code-pull-request: [eventhub] Fixed local variable's name typo in eventhub](https://github.com/Azure/azure-sdk-for-python/pull/32556)
- [:fontawesome-solid-code-pull-request: [Storage] Fixed cspell typos in storage-queue](https://github.com/Azure/azure-sdk-for-python/pull/31844)

## 왜 의미 있었는가

겉으로 보면 작은 수정처럼 보이지만, 이 기여 경험의 진짜 가치는 코드 한 줄보다도
**대형 오픈소스 저장소의 구조와 리뷰 프로세스를 직접 경험했다는 것**에 있었다.

- 모노레포 구조 파악
- 서비스별 패키지 경계 이해
- CI가 요구하는 규칙과 스타일 확인
- 리뷰 피드백을 반영하는 흐름 경험

작은 수정이라도 이런 저장소에서는 맥락을 읽지 못하면 기여하기 어렵다.

## 배운 점

- 오픈소스 기여는 구현 능력만이 아니라 **기존 컨벤션을 읽는 능력**이 중요하다.
- 작은 수정부터 시작하는 것이 대형 저장소의 구조를 익히는 데 가장 현실적인 방법이었다.
- 코드 변경량보다도, 리뷰어가 이해하기 쉬운 변경 단위를 만드는 것이 중요하다는 점을 배웠다.

## 아쉬웠던 점

- Azure SDK Python 같은 초대형 프로젝트에서는 MS 내부적으로 코드 품질 및 개선 방향에 대해 회의에서 논의되고 이를 Auto Gen 이라는 코드 자동 생성 도구가 반영하는데, 이런 맥락까지 알기 어려웠을 뿐더러 Auto Gen 태그가 붙은 코드는 오픈소스임에도 외부 기여자가 코드 기여를 할 수 없도록 막아둬서 실질적으로 기여할 수 있는 코드가 많지 않았다.
