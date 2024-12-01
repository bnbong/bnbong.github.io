---
title: FastAPI FastKit
description: cli operation으로 FastAPI 프로젝트를 탬플릿으로 빠르게 생성하는 패키지
authors:
  - bnbong
tags:
  - Python
  - FastAPI
  - click
  - rich
  - package
---

# FastAPI FastKit

## 개요

![fastapi-fastkit](img/fastkit_general_logo.png)

cli operation으로 FastAPI 프로젝트를 탬플릿으로 빠르게 생성하는 패키지

FastAPI 개발자 tiangolo가 최근 개발한 fastapi-cli 프로젝트의 개발 의의를 이어받아 개발한 오픈소스 패키지 프로젝트

:fontawesome-regular-copyright: copyright : bnbong

### 저장소

<https://github.com/bnbong/FastAPI-fastkit>

## 소개 (원문)

This project was created to speed up the configuration of the development environment needed to develop Python-based web apps for new users of Python and [FastAPI](https://github.com/fastapi/fastapi).

This project was inspired by the `SpringBoot initializer` of the JAVA ecosystem & Python Django's `django-admin` cli operation.

## Abstract

FastAPI는 느린 성능으로 외면을 받던 Python의 웹 앱 개발 상황에 대한 사람들의 인식을 바꾼 프레임워크이다.

Python 3.10 버전이 출시되면서 Python 언어 자체에 대한 성능 향상과 맞물려 FastAPI는 강력한 비동기 기능 지원과 빠른 성능을 자랑한다.

점차 FastAPI에 여러 기능들이 추가되기 시작하면서 FastAPI 개발자 tiangolo는 FastAPI[standard] 혹은 FastAPI[slim] 옵션을 넣어서 불필요한 패키지를 제외하여 개발 환경에 설치하여 내 프로젝트를 경량화시킬 수 있는 기능을 제공하였다.

FastAPI[slim] 옵션으로 설치를 하게 되도 FastAPI 런타임을 디버깅하는데는 전혀 문제가 없으며 많은 유저들이 이를 알고 있다. 그러나 FastAPI의 author인 tiangolo가 갑자기 fastapi-cli branch를 파서 작업한 후 다른 컨트리뷰터들이 리뷰할 충분한 기간을 주지 않고 독단적으로 merge를 한 흔적이 있다.

많은 기여자들이 이를 강하게 비판한 것을 확인할 수 있었으며 ‘[이 기능이 정말 필요한 기능인지 잘 모르겠다](https://github.com/fastapi/fastapi/pull/11522#issuecomment-2092774734)’고 평가한 의견도 볼 수 있었다.

상단의 링크에서 tiangolo의 기능 추가 급발진(?)을 조목조목 강하게 비판하는 댓글을 볼 수 있으며, 좋아요 수가 20개가 넘는다.

핵심 개발자 tiangolo는 8월에 이에 대한 reply를 남겼다. 해당 내용을 요약하자면 FastAPI 입문자를 위해 초심자 편의를 고려하여 해당 기능을 넣기로 했으며 dependancy를 경량화하고 싶은 수요를 고려하여 fastapi[standard] / fastapi[slim] 으로 분기하여 패키지를 설치할 수 있도록 쪼개고자 하는 아이디어에서 이어진 기능이라고 한다.

오랫동안 FastAPI를 활용한 나 또한 비판 의견에 동의를 하는 바지만, 사람들에게 약간이나마 편의성을 제공한다는 측면을 고려해봤을 때 해당 기능이 꼭 필요없는 기능은 아니기에 기여할 가치가 있다고 판단하여 해당 프로젝트에 기여를 할 수 있는 부분을 탐색하였다.

따라서 처음에는 fastapi-cli 프로젝트의 터미널 출력을 직관적으로 개선하는 방향으로 기여를 수행하였으나, 위의 Discussion에서 논의된 내용을 계속해서 고민해본 결과, fastapi-cli 프로젝트로는 FastAPI 프레임워크에 입문하는 사람들의 진입장벽을 낮추기 힘들다고 생각하였다.

근본적인 문제를 해결하기 위해 차라리 내가 오픈소스 프로젝트를 파서 기여를 하는 방향으로 접근하였다. cli 기능은 Python 뿐만아니라 다른 언어로 개발된 패키지에서도 지원하며, 많은 개발자들은 cli operation으로 편리하게 기능을 사용할 수 있는 역량이 있다.

그 측면에서 fastapi-cli의 기능적인 도움을 받는 것은 좋은 방향이라고 생각하였다. 거기에 추가로 Python Django의 django-admin operation으로 빠르게 project init을 수행할 수 있는 기능에 영감을 받아 비슷한 기능을 수행하는 cli operation을 내가 만들 새로운 프로젝트에 접목시키기로 결정하였으며, 이렇게 해서 fastapi-fastkit 프로젝트를 만들게 되었다.

## Stack

- python 3.12
- click 8.1.7
- fastapi-cli 0.0.5
- rich 13.9.2


## 역할

- 프로젝트 설계
- 패키지 개발

## 비고

- Template을 통해 FastAPI 프로젝트를 빠르게 Workspace에 배포할 수 있는 기본 기능 구현 완료
- 추가 기능 및 더 강력한 cli operation 기능 구현 중
