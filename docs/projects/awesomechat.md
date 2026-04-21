---
title: Awesome Chatting App
description: Firebase Realtime Database를 활용해 빠르게 익명 채팅 앱을 구현한 팀 프로젝트
authors:
  - bnbong
tags:
  - Android Studio
  - Java
  - Firebase
  - Mobile Application
  - team
  - backend
period: "2022"
role: 팀 프로젝트 · 설계 / 문서화 / 이슈 관리 / 테스트
---

# Awesome Chatting App

## 개요

![Awesome Chatting App](img/awesomechatlogo.png)

Awesome Chatting App은 별도 회원가입 없이 닉네임만 입력하면 바로 익명 채팅방에 들어갈 수 있도록 만든
모바일 채팅 앱이다. 오픈소스 SW 수업 팀 프로젝트로 진행했다.

### 저장소

<https://github.com/bnbong/Awesome_ChattingApp>

### 팀원

- 백엔드 개발 : [JJongmen](https://github.com/JJongmen/JJongmen.github.io)
- DB 및 이슈 관리 : [namHG](https://github.com/namHG/namHG.github.io)
- 프론트엔드 개발 : [GoodTY](https://github.com/GoodTY/GoodTY.github.io)
- 프로젝트 디렉팅 및 문서화 : [bnbong](https://github.com/bnbong/bnbong.github.io)

## 왜 Firebase였는가

이 프로젝트의 목표는 로그인 체계나 서버 인프라를 직접 만드는 것이 아니라,
**수업 과제 범위 안에서 실시간 채팅 경험을 빠르게 구현하는 것**이었다. 그래서 자체 서버보다
Firebase Realtime Database가 훨씬 적합했다.

- 실시간 데이터 동기화를 빠르게 붙일 수 있다.
- 별도 백엔드 구축 없이 메시지 입출력 흐름을 확인할 수 있다.
- 팀 프로젝트 일정 안에서 UI/기능 검증에 집중할 수 있다.

기술 선택의 기준은 장기 운영보다 **구현 속도와 실시간성 검증**에 있었다.

## 구현 포인트

<div class="grid" markdown>
<div markdown>
![Awesome Chat 1](img/awesomechat1.png)
</div>
<div markdown>
![Awesome Chat 2](img/awesomechat2.png)
</div>
</div>

- 닉네임만 입력해 즉시 채팅방 입장
- 본인 메시지와 타인 메시지를 구분해 읽기 쉽게 렌더링
- 단순한 화면 구성으로 핵심 대화 흐름에 집중

서비스 목표가 명확했기 때문에, 기능을 늘리기보다 진입 장벽을 줄이고 실시간 대화 경험을 살리는 데
무게를 뒀다.

## 내가 맡은 역할

- 프로젝트 설계 및 방향 정리
- 스프린트와 이슈 관리
- 테스트 코드 작성
- 문서화

## 배운 점

- 모바일 팀 프로젝트에서는 모든 기능을 직접 구현하는 것보다, **문제에 맞는 백엔드 서비스를 고르는 판단**이 중요하다.
- Firebase 같은 BaaS는 "쉬워 보이는 도구"가 아니라, 짧은 기간의 프로토타이핑에 매우 강력한 선택지라는 걸 체감했다.
- 작은 프로젝트라도 문서화와 역할 분리가 있으면 협업 품질이 눈에 띄게 좋아진다.
