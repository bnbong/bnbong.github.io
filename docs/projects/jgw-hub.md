---
title: JaramGroupware Hub - 커뮤니티 서비스 API
description: 자람 허브 스터디 대표 커뮤니티 서비스 ‘허브’의 API 서버 개발
authors:
  - bnbong
tags:
  - Python
  - FastAPI
  - SQLAlchemy
  - API Server
---

# JaramGroupware Hub API

자람 허브 스터디 대표 커뮤니티 서비스 ‘허브’.

자람 학회원에게 커뮤니티 서비스를 제공하기 위해 만들어진 서비스.

자람 허브 스터디 프로젝트의 일환으로 진행.

## 개요

기존 Python Django로 개발된 커뮤니티 서비스를 FastAPI로 마이그레이션하는 작업 진행.

### 저장소

<https://github.com/msng-devs/JGW-hub>

## API 문서

- (Version 2) https://jgw.gitbook.io/jgw-hub-v2/

단, v2 API 문서의 경우 배포된 Gitbook 문서 페이지에 일부 response 필드가 누락되거나 잘못 표기된 경우가 있음. 소스 폴더 docs에 있는 openapi.json 혹은 openapi.yaml 파일을 다운 받아 Swagger 뷰어로 확인하는 것을 권장.

자세한 내용은 [README.md](https://github.com/msng-devs/JGW-hub/blob/4711860a241efe564fd5921c0aa2f7985f54e054/readme.md)파일 참고.

## 역할

- 백엔드 개발
- 문서화
- 테스트 코드 작성
- 배포 자동화

## Stack

- Language : Python 3.10.10
- Framework : FastAPI + SQLAlchemy
- Document : Gitbook (redoc template)
