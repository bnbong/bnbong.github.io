---
title: KakaoTalk-channel-WeatherToday
description: 공공 날씨 데이터를 수집해 카카오톡 채널로 전달하는 예보 봇 프로젝트
authors:
  - bnbong
tags:
  - Python
  - FastAPI
  - PostgreSQL
  - Docker
  - personal
  - backend
period: "2023"
role: 개인 프로젝트 · 백엔드 / 데이터 수집 / 챗봇 연동 / 배포
---

# KakaoTalk-channel-WeatherToday

## 개요

![WeatherToday bot](img/channel_thumbnail.jpg)

지역 날씨 정보를 카카오톡 채널로 전달하는 봇 프로젝트다. 공공 API와 외부 날씨 데이터를 수집하고, 사용자에게 특정 시간대에 날씨 정보를 제공하는 흐름을 목표로 했다.

### 저장소

<https://github.com/bnbong/KakaoTalk-channel-WeatherToday>

## 문제와 접근 방식

날씨 서비스는 많지만, 사용자가 매번 앱을 열어 확인하기보다 **메신저 안에서 바로 받는 경험**에 무게를 두고 싶었다. 그래서 별도 모바일 앱 대신 카카오톡 채널 + 챗봇 구조를 택했다.

핵심 흐름은 다음과 같다:

- 외부 날씨 데이터를 수집
- 지역/시간 기준으로 정리
- 카카오톡 채널 사용자에게 전달

## 왜 FastAPI였는가

챗봇 연동용 API는 비교적 가볍고, 빠르게 문서화하며, 외부 서비스와 붙이기 쉬워야 했다.
FastAPI는 이 요구에 잘 맞았다.

- 입력/응답 스키마를 명확히 정의하기 쉽다.
- Swagger 문서로 빠르게 테스트할 수 있다.
- 데이터 수집 모듈과 API 계층을 분리하기 편하다.

## 운영 구조

- Oracle Cloud Osaka 리전
- Docker / Docker Hub
- PostgreSQL
- Uvicorn
- Jenkins 기반 배포 흐름

메신저 봇은 "항상 켜져 있어야 한다"는 점이 중요했기 때문에, 개발 환경보다 운영 안정성을 먼저 고민하게 되는 프로젝트였다.

## 내가 맡은 역할

- 백엔드 개발
- 날씨 데이터 수집/전송 모듈 구현
- 카카오톡 채널 구성
- 배포 파이프라인 정리
- 문서화

## 배운 점

- 챗봇 프로젝트는 UI보다도 **외부 플랫폼 제약과 데이터 흐름**을 이해하는 일이 더 중요하다.
- 메신저 기반 서비스는 API 서버 하나만 잘 만든다고 끝나는 게 아니라,
  플랫폼 설정, 배포, 장애 대응까지 함께 묶어서 봐야 했다.
