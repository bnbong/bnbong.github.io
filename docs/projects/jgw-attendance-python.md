---
title: JaramGroupware Attendance - 학회원 출결 시스템 API
description: 학회 출결 도메인을 Django REST Framework로 재구성하고 스케줄러와 문서 체계를 정리한 프로젝트
authors:
  - bnbong
tags:
  - Python
  - Django
  - Django REST framework
  - API Server
  - team
  - backend
period: "2023"
role: 팀 · 학회 / 백엔드 / 문서화 / 테스트 / 배포 자동화
---

# JaramGroupware Attendance API

## 개요

자람 그룹웨어의 출결 관리 시스템이다. 페널티 시스템과 마찬가지로, 기존 구조를 Python Django 기반으로 정리하고 운영 가능한 내부 API 형태로 재구성하는 작업의 일부였다.

### 저장소

<https://github.com/msng-devs/JGW-Attendance-Python>

## 프로젝트 특징

출결 시스템은

- 학회원 이벤트와 시간표
- 출결 상태 갱신
- 주기적인 정리 작업

이 함께 엮이는 도메인이다. 그래서 리펙토링을 수행하며 단일 앱 구현보다 **도메인별 앱 분리와 공통 모듈 정리**에 더 집중하여 `attendance`, `event`, `timetable`, `utils`, `core`를 분리했다. 이는 출결 로직을 한 파일에 몰아넣지 않고 역할 기준으로 나누려는 의도였다.

## 왜 Django REST Framework였는가

출결 시스템은 복잡한 실시간성보다 **명확한 관리 기능, 검증, 운영 편의성**이 중요했다.
DRF는 다음 이유로 적합했다.

- 관리형 API를 빠르게 구성하기 쉽다.
- Serializer와 Permission 구조가 명확하다.
- Django 생태계로 테스트와 운영을 정리하기 좋다.
- 당시에는 백엔드 경험이 부족했던 터라 Django가 내가 선택할 수 있던 가장 최선의 stack이었다.
- 같은 그룹웨어 서비스의 핵심인 커뮤니티 서비스 'Hub'가 Django로 구현되어 있어서, 기술 스택을 통일하는 것도 고려했다.

## 스케줄러가 중요했던 이유

이 프로젝트에서 특징적이었던 부분은 주기적 갱신 작업이다. 문서 기준으로 APScheduler를 사용해 학회원 출결 정보를 주기적으로 업데이트하도록 구성했다.

이 선택은 출결 도메인이 단순 요청/응답만으로 끝나지 않고, **시간이 지남에 따라 상태를 갱신해야 하는 시스템**이었기 때문이었다.

## 역할

- Django REST Framework 기반 API 구현
- 테스트 코드 작성
- GitBook 기반 문서화
- 배포 자동화
- 스케줄링 로직 정리

## 배운 점

- 출결 같은 업무 도메인은 화면보다도 **상태 전이와 주기 작업**이 더 중요하다.
- 작은 내부 서비스라도 앱 경계를 나눠 두면 이후 유지보수가 훨씬 편해진다.
- 문서와 스케줄러를 함께 관리해 본 경험이 이후 운영성 있는 백엔드 프로젝트에 도움이 됐다.
