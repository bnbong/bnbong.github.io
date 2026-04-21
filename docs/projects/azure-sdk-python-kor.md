---
title: Azure SDK Python Korean
description: Azure SDK Python 구현 가이드를 한국어로 번역하며 문서 기여와 로컬 빌드 이슈를 함께 다룬 경험
authors:
  - bnbong
tags:
  - Python
  - Azure
  - Azure SDK
  - oss
period: "2023"
role: 문서 번역 기여
---

# Azure SDK Python Korean

## 개요

Azure SDK Python 공식 가이드 문서를 한국어로 번역한 기여 경험이다. OSSCA 활동 중
Python 구현 가이드의 일부를 한국어로 옮기고, 문서 저장소 이슈도 함께 다뤘다.

### 저장소

<https://github.com/bnbong/azure-sdk-korean>

## 기여 내용

- [:fontawesome-solid-code-pull-request: Translate 'docs/python/implementation.md' into korean](https://github.com/Azure/azure-sdk-korean/pull/191)
- [:fontawesome-solid-code-pull-request: Translate complete 'docs/python/implementation.md' into korean](https://github.com/Azure/azure-sdk-korean/pull/193)
- [:fontawesome-solid-code-pull-request: webrick 의존성 추가](https://github.com/Azure/azure-sdk-korean/pull/131)
- [:fontawesome-solid-code-compare: To-do: Sidebar 개선](https://github.com/Azure/azure-sdk-korean/issues/129)
- [:fontawesome-solid-code-compare: [Suggesetion] jekyll Building Failure at Local](https://github.com/Azure/azure-sdk-korean/issues/130)

## 왜 이 기여가 중요했는가

문서 번역은 단순 직역이 아니라, 원문의 의도와 구현 맥락을 이해한 뒤 한국어 독자가 읽기 쉬운 형태로
다시 쓰는 작업이다. 특히 SDK 구현 가이드는 용어 하나만 잘못 옮겨도 의미가 크게 달라질 수 있다.

또한 문서 기여 과정에서 사이드바 개선, 로컬 Jekyll 빌드 이슈 같은 운영 문제도 함께 다뤘다.
번역만이 아니라 **문서 저장소를 실제로 유지하는 과정**을 겪은 경험이었다.

## 배운 점

- 좋은 기술 번역은 언어 실력보다도 **도메인 이해도**가 더 중요하다.
- 문서 저장소도 결국 하나의 제품이며, 빌드와 구조 이슈를 같이 봐야 한다.
- 오픈소스 문서 기여는 코드 기여와 다른 방식의 정밀함을 요구한다.
