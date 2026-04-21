---
title: BNGdrasil
description: Bifrost 게이트웨이에서 출발해 개인 클라우드 플랫폼으로 확장한 멀티 저장소 인프라 프로젝트
authors:
  - bnbong
tags:
  - Python
  - FastAPI
  - React
  - TypeScript
  - Terraform
  - OCI
  - Docker
  - PostgreSQL
  - personal
  - backend
  - cloud
  - devops
period: 2022 - 진행중
role: 개인 프로젝트 · 플랫폼 아키텍처 / IaC / API Gateway / Auth / 운영 콘솔 설계
---

# BNGdrasil

## 개요

!!! tip "아이템 한줄 설명"
    2022년 Bifrost 게이트웨이 실험을 개인 클라우드 플랫폼으로 확장한 멀티 저장소 아키텍처 프로젝트

BNGdrasil은 처음엔 개인 서버에 흩어져 있던 서비스를 하나로 묶기 위한 `Bifrost` 게이트웨이
아이디어에서 시작했지만,

지금은 그 범위를 넘어 API Gateway, 인증 서버, 웹 클라이언트,
운영용 Admin UI, Terraform 기반 인프라 코드까지 분리된 **개인 클라우드 플랫폼**으로 진화했다.

내가 새로 추가할 서비스를 어떻게 설계하고 배포하고 운영할지를 하나의 생태계로 정리한 프로젝트이다.

### 조직 및 저장소

- Organization : <https://github.com/BNGdrasil>
- IaC : <https://github.com/BNGdrasil/Baedalus>
- API Gateway : <https://github.com/BNGdrasil/Bifrost>
- Auth Server : <https://github.com/BNGdrasil/Bidar>
- Web Client / Admin : <https://github.com/BNGdrasil/Bantheon>
- Networking 구상용 저장소 (OpenStack 기반 Custom VPC) : <https://github.com/BNGdrasil/Bsgard>
- Game Platform 구상용 저장소 : <https://github.com/BNGdrasil/Blysium>

`Bsgard`, `Blysium`은 2026년 4월 기준 미구현 상태이다.

## 왜 Bifrost에서 BNGdrasil로 확장했는가

초기 Bifrost는 "내가 배포한 여러 서비스를 하나의 진입점으로 모으는 문제"를 해결하는 데 집중한 프로젝트였다.

그런데 서비스를 실제로 더 오래 운영해 보니, 게이트웨이만으로는 해결되지 않는 문제가 분명히 드러났다.

- 서비스 라우팅만 정리해도 **인증/권한 관리**는 여전히 각 서비스마다 중복된다.
- 서버를 수동으로 만들고 설정하면, 구조를 다시 재현하거나 이전하는 작업이 어렵다.
- 운영자가 SSH와 설정 파일에만 의존하면 서비스 등록, 상태 확인, 로그 확인 같은 작업이 비효율적이다.
- 개인 프로젝트라도 서비스 수가 늘면 네트워크, 데이터 저장소, 배포 절차를 함께 설계해야 한다.

그래서 BNGdrasil에서는 "게이트웨이"만 바라보던 시각에서 벗어나,
**플랫폼을 운영하는 데 필요한 책임들을 명시적으로 쪼개는 방향**으로 프로젝트를 재구성했다.

## 플랫폼을 어떻게 분해했는가

BNGdrasil의 핵심은 **운영 경계를 기준으로 책임을 나눈 것**이다.

- `Baedalus`는 인프라를 코드로 관리하는 레이어다. OCI 리전, VCN, 서브넷, VM 사양, 사용자 데이터 주입을
  Terraform으로 선언해 클릭 기반 인프라 관리에서 벗어나려는 목적이 강하다.
- `Bifrost`는 외부 요청의 진입점이다. 서비스 레지스트리, 프록시, 헬스체크, Admin API를 맡는다.
- `Bidar`는 인증과 권한을 전담한다. 게이트웨이가 직접 사용자 역할을 판단하는 대신, 별도 Auth 서버가
  JWT와 RBAC 검증을 담당한다.
- `Bantheon`은 운영 UI와 공개 웹 클라이언트를 맡는다. Admin 대시보드는 Bifrost와 Bidar 위에서 동작한다.
- `Bsgard`, `Blysium`은 각각 네트워크 추상화와 게임 플랫폼 확장을 염두에 둔 저장소다.

이렇게 나눈 이유는, 개인 프로젝트에서 조차도 결국 문제는 **"누가 라우팅을 담당하고, 누가 권한을 판단하고, 누가 인프라를 재현하느냐"** 로 귀결되기 때문이다.

## 구현 포인트

### Baedalus: 멀티 리전 인프라를 코드로 고정

`Baedalus`는 OCI Chuncheon, Osaka 두 리전을 각각 provider로 선언하고, 총 6대 VM 구성을 변수화해 관리한다.
현재 코드 기준으로는 다음과 같이 배치되어 있다(2025년 기준):

- Chuncheon Public Subnet : `vm1` 프런트/프록시, `vm2` 코어 API
- Chuncheon Private Subnet : `vm3` 데이터베이스
- Osaka Private Subnet : `vm4` 모니터링, `vm5` 백업, `vm6` 플레이그라운드

또한 `vm_configs`로 OCPU, 메모리, 스토리지를 맵 형태로 관리하고, `user_data` 스크립트에
도메인, PostgreSQL 계정, JWT 시크릿 등을 주입한다. Makefile도 `init`, `plan`, `apply`, `deploy`,
`show-ips`, `show-ssh` 같은 운영 동선 기준으로 정리했다.

Terraform이 필요했던 이유는, 이 프로젝트가 단순히 VM 몇 대 띄우는 수준이 아니라 서브넷 성격, 노출 범위, 리전별 역할까지 반복 가능하게 유지해야 했기 때문이다.

### Bifrost: 플랫폼 안의 API Gateway

현재 Bifrost는 FastAPI 기반으로 재구성되어 있다. 앱 시작 시 `ServiceRegistry`를 초기화하고,
PostgreSQL에서 활성 서비스 목록을 읽어 메모리에 적재한 뒤, `/{service_name}/{path:path}` 형태의
catch-all 라우트로 요청을 백엔드 서비스에 프록시한다.

구현 포인트는 다음과 같다:

- 서비스 목록을 정적 파일이 아니라 **DB 기반 레지스트리**로 관리
- 서비스 생성/수정/삭제 후 백그라운드에서 레지스트리를 다시 로드
- 헬스체크 결과를 DB의 `health_status`, `last_health_check`에 반영
- `structlog` JSON 로그와 Prometheus metrics 엔드포인트 제공
- Admin API에서 서비스 CRUD, 통계, 전체 헬스체크 트리거 지원

지금의 Bifrost는 단순 reverse proxy보다 **플랫폼 제어점**에 더 가깝다. 별도 게이트웨이를 유지해야 했던 이유는, 서비스가 늘어날수록 "어느 서비스가 살아 있는지", "어떤 이름으로 라우팅할지", "관리 UI에서 무엇을 건드릴지"를 한 곳에서 다뤄야 했기 때문이다.

### Bidar: 인증과 권한을 게이트웨이에서 분리

`Bidar`는 FastAPI + SQLModel + asyncpg 조합의 인증 서버다. `auth/token`, `auth/refresh`,
`auth/me` 엔드포인트를 제공하고, 사용자 모델에는 `role`, `is_superuser`, `created_at` 같은 필드를 둔다.

특히 중요한 부분은 Bifrost와의 연동 방식이다.

- Bidar는 JWT access/refresh token을 발급
- 역할 계층을 `user`, `moderator`, `admin`, `super_admin`으로 정의
- `/rbac/verify-permission` 엔드포인트에서 최소 역할 요구사항을 검증
- Bifrost는 Admin API 접근 시 이 엔드포인트를 호출해 권한을 위임 검증

이 구조를 택한 이유는, 게이트웨이가 권한 판단까지 직접 떠안으면 이후 서비스가 늘어날수록
권한 모델이 중복되기 때문이다. 인증 서버를 분리하면 게이트웨이는 진입 제어에 집중할 수 있고,
권한 규칙은 한 곳에서 관리할 수 있다.

### Bantheon: 운영을 위한 웹 클라이언트

`Bantheon`은 공개용 클라이언트와 Admin 대시보드를 별도 앱으로 둔다.

공개 클라이언트는 비교적 단순한 랜딩 페이지이고, 핵심 구현은 Admin 대시보드에 집중적으로 수행했다:

- React Router로 `dashboard`, `users`, `services`, `logs`, `settings` 페이지 분리
- React Query로 서버 상태 조회와 주기적 refetch 처리
- Axios interceptor로 access token 자동 주입 및 401/403 처리
- 서비스 등록 모달, 전체 헬스체크, 레지스트리 리로드 같은 운영 액션 UI 제공

## 기술 선택 과정

### FastAPI 중심 재구성

초기 Bifrost는 게이트웨이 자체를 중심으로 보는 관점이 강했고 이후 BNGdrasil에서는
게이트웨이와 인증 서버를 모두 Python/FastAPI 스택으로 맞췄다. 이유는 다음과 같다:

- 개인 프로젝트에서 빠른 반복과 API 계약 확인이 중요했다.
- OpenAPI 문서 자동화가 운영 UI와 연결되기 쉬웠다.
- 프록시, 헬스체크, 권한 검증 같은 네트워크 지향 로직을 직접 제어하기 편했다.
- 가장 익숙한 프레임워크였기 때문에, 구현 속도를 높이는 데 도움이 됐다.

### Terraform + OCI

BNGdrasil은 인프라를 "설명"하는 게 아니라 "재현"하는 쪽을 목표로 했다. Terraform은 이 요구에 잘 맞았다.

또한 현재 설계는 OCI Free Tier 안에서 멀티 VM 구성을 실험해 보는 데 현실적인 선택지였다.

Public CSP 중에서 프리티어 개인 계정이 사용할 수 있는 리소스가 가장 많기도 했기 때문에 OCI를 선택했다.

### 게이트웨이와 인증 서버 분리

라우팅과 권한은 모두 진입점에서 만나지만, 같은 책임은 아니다. 인증 서버를 분리하면 이후 서비스가
늘어나도 게이트웨이가 사용자 저장소나 역할 정책까지 함께 안고 갈 필요가 없어진다.

### React + Vite 기반 운영 UI

운영 화면은 빠르게 만들고 자주 고쳐야 한다. Vite 기반 React 구성은 초기 부하가 낮고,
Admin UI처럼 라우팅/폼/비동기 요청이 많은 화면을 만들기 좋았다.

## 역할

- Bifrost 단일 게이트웨이에서 BNGdrasil 플랫폼 구조로 프로젝트 재정의
- 멀티 리전 OCI 인프라 구조 설계 및 Terraform 코드화
- API Gateway, Auth Server, Admin UI 간 책임 분리
- 서비스 등록/헬스체크/권한 검증 흐름 설계
- 공개 문서와 저장소 구조 정비를 통한 플랫폼 단위 운영 기반 마련

## 결과와 의미

- 단일 게이트웨이 프로젝트가 **조직 단위 플랫폼 아키텍처**로 확장됐다.
- Terraform 출력 기준으로 6개 VM, 총 8 OCPU / 48GB RAM / 380GB 스토리지 규모의
  개인 클라우드 청사진을 코드로 남겼다.
- Bifrost와 Bidar 사이에 **RBAC 위임 검증 경로**를 만들고, Bantheon에서 이를 운영 UI로 연결했다.
- 인프라, 인증, 게이트웨이, 운영 UI를 각각 분리해 이후 OpenStack 홈랩이나 추가 서비스로 확장할 수 있는
  기반을 만들었다.

## 배운 점

- 게이트웨이는 서비스 구조의 끝이 아니라 시작점이다. 서비스가 늘어나면 결국 인증, 운영 UI, IaC가 함께 따라온다.
- 개인 프로젝트에서 마이크로서비스를 쓴다면, "서비스 수"보다 **운영 경계가 명확한지**가 더 중요하다.
