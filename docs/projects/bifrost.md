---
title: Bifrost - MSA Gateway
description: bnbong Server에 올라가있는 MSA 서비스들의 Proxy 연결을 할 목적으로 개발된 Gateway
authors:
  - bnbong
tags:
  - Java
  - Spring Cloud Gateway
  - MSA
---

# Bifrost - MSA Gateway

## 개요

bnbong Server에 올라가있는 MSA 서비스들의 Proxy 연결을 할 목적으로 개발된 Gateway

### 저장소

https://github.com/bnbong/BnbongServerGateway

## 소개

Kotlin Spring Cloud Gateway로 작성된 Bnbong Server 에서 사용할 Gateway 서비스이다.

Bnbong Server 에서 작동되는 각 Micro service Container 들의 Endpoint에 Proxy 연결을 해주는 역할을 한다.

## Stack

- Kotlin
- JAVA 17 & JVM 1.9.20
- Spring Cloud Gateway
- Spring Boot 3.2.0
- Gradle
- Docker (dev : MacOS M1, prod : Linux ARM)


## 역할

- 프로젝트 설계 및 디자인
- 백엔드 개발

## 비고

현재는 Server 기능만 존재하다. 편의성을 위해 endpoint proxy를 연결하는 액션을 도와줄 Client 프로젝트가 추후 추가될 수 있다.

### Spring Cloud Gateway를 사용하여 특정 Micro Service Endpoint에Proxy 연결하기

#### 프록시할 특정 서비스의 Endpoint 추가하기

```
* 요청 URL
POST https://api.bnbong.xyz/actuator/gateway/routes/<추가할_서비스명>

* Request Body
{
    "id": "<추가할_서비스명>",
    "predicates": [{
        "name": "Path",
        "args": {
            "pattern": "<추가할_endpoint>"
        }
    }],
    "filters": [],
    "uri": "<서비스 docker container ip>",
    "order": 0
}

# 예시
* 요청 URL
POST https://api.bnbong.xyz/actuator/gateway/routes/test_jaram_sugang

* Request Body
{
    "id": "test_jaram_sugang",
    "predicates": [{
        "name": "Path",
        "args": {
            "pattern": "/api/ping/**"
        }
    }],
    "filters": [],
    "uri": "http://172.20.0.9:9090",  # docker container 이름을 사용해도 됨
    "order": 0
}
```

#### 프록시할 특정 서비스의 Endpoint 제거하기

```
* 요청 URL
DELETE https://api.bnbong.xyz/actuator/gateway/routes/<서비스명>

# 예시
* 요청 URL
DELETE https://api.bnbong.xyz/actuator/gateway/routes/test_jaram_sugang
```

#### Gateway Refresh (변경 사항 적용)

```
* 요청 URL
POST https://api.bnbong.xyz/actuator/gateway/refresh
```

### Spring Cloud Gateway에 적용된 Endpoint 확인하기

<https://api.bnbong.xyz/actuator/gateway/routes>

### 참고

[Actuator API :: Spring Cloud Gateway](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway/actuator-api.html#gateway-retrieving-information-about-a-particular-route)
