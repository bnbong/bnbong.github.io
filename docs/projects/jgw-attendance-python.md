---
title: JaramGroupware Attendance - 학회원 출결 시스템 API
description: 자람 그룹웨어의 학회원 출결 시스템 API
authors:
  - bnbong
tags:
  - Python
  - Django
  - Django REST framework
  - API Server
---

# JaramGroupware Attendance API

## 개요

자람 그룹웨어의 출결 관리 시스템이다.

자람 허브 스터디 프로젝트의 일환으로 진행.

### 저장소

<https://github.com/msng-devs/JGW-Attendance-Python>

## 소개

새로 작성된 Penalty 시스템은 Python Django로 개발, 기존 Java Spring으로 개발되었던 Attendance 시스템을 바탕으로 재구성함.

## API 문서

<https://jgw.gitbook.io/jgw-attendance-python-documents/api-documents>

## Stack

- Language : Python 3.10.10
- Framework : Django + Django REST framework
- Document : Gitbook

## 역할

- 백엔드 개발
- 문서화
- 테스트 코드 작성
- 배포 자동화

## 비고

- APScheduler를 사용하여 자람 학회원의 출결 정보를 주기적으로 업데이트하는 스케쥴러가 구동중.
