# Project Pinned

# 개요

지역 랜드마크와 관련된 내 추억을 공유하는 지도 기반 웹 SNS 서비스

해당 프로젝트는 2023년 공개SW 개발자대회, 제 11회 문화데이터 활용 경진대회 공모전 출품용으로 진행한 프로젝트이다.

## 저장소

https://github.com/bnbong/Project-Pinned

## 팀원 Info

1. 이준혁 (팀장, 백엔드, 프로젝트 설계 및 디자인, 스프린트 매니징, 아키텍처 설계)
2. 박종윤 (백엔드, API 테스트)
3. 최수용 (프론트엔드, UI/UX 디자인 및 구현)
4. 허재원 (프론트엔드, UI/UX 디자인 및 구현)

# 소개

[핀드 - 내 추억 속의 랜드마크 시연 영상](https://youtu.be/u4GKCeECjJE)

시연 영상

지역 랜드마크와 관련된 내 추억을 공유하는 지도 기반 웹 SNS 서비스

지역 랜드마크 빅데이터를 활용한 SNS 서비스이며, 카카오맵 API를 활용하여 지도 뷰가 구현되어 있다.

해당 지도에는 각 지역 별 랜드마크가 Pin으로 나타나며 해당 Pin에서 사람들 각자가 해당 랜드마크와 관련된 추억들에 대한 포스팅들의 리스트를 피드 형식으로 볼 수 있다.

본인 또한 특정 지역 랜드마크에 해당 랜드마크와 관련된 추억을 포스팅 형식으로 남들과 공유할 수 있다.

공모전 수상까지 가진 못했지만 1달 정도 진행했던 규모있는 프로젝트로써, 프로젝트 회고 또한 진행했다.

## 개발 회고

[[Web Application] Project-Pinned 개발 회고](https://blog.naver.com/bnbong/223217885371)

# Stack

- Framework: Backend - Django, Python (3.10.10) / Frontend - Next.js, tailwind.css
- DB: PostgreSQL
- Cache DB: Redis
- Proxy: Nginx
- Container: Docker
- Hosting: AWS (현재는 인스턴스를 삭제한 상태)
- Issue Manage: Jira

# Architecture

## System

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2dd0a9b0-1aca-4d61-9ed9-d2945bd19fe6/816c29a4-8922-4e15-8d82-1de0bd661d5d/Untitled.png)

## CI/CD

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2dd0a9b0-1aca-4d61-9ed9-d2945bd19fe6/4e2ea288-a714-4608-a136-6c3420e7099a/Untitled.png)

# 비고

버전 1.1까지 업데이트를 진행했다.

개발 환경에서 포스팅 detail을 보는 페이지에서 post_title이 undefined로 넘어와서 렌더링이 안되는 오류가 있으나, 배포 환경에서는 문제없이 작동되었다.

해당 프로젝트도 bnbong Server에 MSA로 등록이 예정되어 있다.

다만, Gateway 통신 등 일부 Client ↔ Server 통신이 1.1 버전과 차이가 있으므로 수정이 필요하다(Nginx 설정 등)
