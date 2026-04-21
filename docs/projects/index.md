---
title: Projects
description: bnbong이 진행한 프로젝트 — featured 우선 · 카테고리 기반 archive
hide:
  - toc
---

<!--
  Archive 유지 가이드:
  - featured 플래그는 각 프로젝트 md의 frontmatter에 `featured: true`로 표시합니다.
  - 카테고리(backend / cloud / devops / ai / system / oss / team / personal / coursework / game)도
    frontmatter `tags`에 소문자 키워드로 함께 포함되어 있습니다.
  - 새 프로젝트 상세 md를 추가한 경우, 아래 Archive 섹션의 해당 카테고리 목록에
    한 줄씩 추가해 주세요. 저는 수작업 링크 리스트를 유지하고 있습니다.

  현재 docs/projects/ 하위 상세 md 목록 (index/femu 제외 순서 무관):
    wegis, fall-in,
    bngdrasil, tookindfriendchat, univapi, ricktcal, kakaotalk-weatherforecast,
    project-pinned, awesomechat, mugip, kbuddy,
    jgw-hub, jgw-penalty-python, jgw-attendance-python, qr-phishing-detector,
    azure-sdk-python, azure-sdk-python-kor, fastapi-fastkit, blog-post-workflow,
    femu-monitoring
-->

# Projects

지금까지 진행해 온 프로젝트를 **Featured → Archive** 순으로 정리했습니다.

## Featured

<div class="grid cards" markdown>

-   :material-shield-search:{ .lg .middle } **Wegis**

    ---

    <span class="period-badge">2025.09 – 2025.10</span>

    멀티모달 AI 기반 QR/URL 피싱 탐지 시스템. MobileBERT + 1D-CNN, FastAPI 추론 서버.

    <span class="badge-inline">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
    <img src="https://img.shields.io/badge/OCI-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="OCI">
    </span>

    운영비 **월 26,000원 → 0원**, 추론 지연 **p95 −43.6%**.

    [:fontawesome-brands-github: Wegis](https://github.com/bnbong/Wegis) · [자세히 보기 →](wegis.md)

-   :material-package-variant:{ .lg .middle } **FastAPI-fastkit**

    ---

    <span class="period-badge">2024.08 – 진행중</span>

    FastAPI 프로젝트 부트스트랩 CLI + 템플릿 OSS. PyPI 배포, 다중 템플릿 관리.

    <span class="badge-inline">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/click-000000?style=for-the-badge&logo=python&logoColor=white" alt="click">
    <img src="https://img.shields.io/badge/rich-000000?style=for-the-badge&logo=python&logoColor=white" alt="rich">
    </span>

    [:fontawesome-brands-github: FastAPI-fastkit](https://github.com/bnbong/FastAPI-fastkit) · [자세히 보기 →](fastapi-fastkit.md)

-   :material-earth:{ .lg .middle } **K-Buddy**

    ---

    <span class="period-badge">2023.09 – 2024.06</span>

    방한 외국인 대상 로컬 경험 플랫폼 창업팀. Oracle Cloud 컨테이너 MSA 인프라 설계.

    <span class="badge-inline">
    <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java">
    <img src="https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white" alt="Spring Boot">
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/OCI-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="OCI">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    </span>

    [:fontawesome-brands-github: KBuddy-Server](https://github.com/KBuddy-devs/KBuddy-Server) · [자세히 보기 →](kbuddy.md)

-   :material-cards-playing-outline:{ .lg .middle } **헤쳐 모여! (Fall In!)**

    ---

    <span class="period-badge">2026.01 – 진행중</span>

    6 Nimmt! 룰을 공군 ORI 세계관으로 재해석한 1인 전략 카드 게임.

    <span class="badge-inline">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Pygame%20CE-000000?style=for-the-badge&logo=python&logoColor=white" alt="Pygame CE">
    <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest">
    <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
    </span>

    [:fontawesome-brands-github: Fall-In](https://github.com/bnbong/Fall-In) · [자세히 보기 →](fall-in.md)

-   :material-harddisk:{ .lg .middle } **FEMU Monitoring & Hot/Cold**

    ---

    <span class="period-badge">2024.09 – 2024.12</span>

    가상 SSD 에뮬레이터 FEMU 계측 모듈 + Hot/Cold Data Separation.
    Zipfian 1.2 기준 **WAF ~35% 감소**, **IOPS ~20% 개선**.

    <span class="badge-inline">
    <img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" alt="C">
    <img src="https://img.shields.io/badge/FEMU-555555?style=for-the-badge" alt="FEMU">
    <img src="https://img.shields.io/badge/QEMU-FF6600?style=for-the-badge&logo=qemu&logoColor=white" alt="QEMU">
    <img src="https://img.shields.io/badge/SSD-222222?style=for-the-badge" alt="SSD">
    </span>

    [:fontawesome-brands-github: FEMU](https://github.com/bnbong/FEMU) · [자세히 보기 →](femu-monitoring.md)

</div>

## Archive

모든 프로젝트 상세 문서는 링크에서 바로 확인할 수 있습니다. 한 프로젝트가 여러
카테고리에 동시에 등장할 수 있습니다 (예: `fastapi-fastkit`는 OSS이자 Personal).

### Backend

<div class="project-archive-list" markdown>

- [Wegis](wegis.md) · 2025.09 – 2025.10 <span class="tag-badge">Featured</span>
- [FastAPI-fastkit](fastapi-fastkit.md) · 2024.08 – 진행중 <span class="tag-badge">Featured</span>
- [K-Buddy](kbuddy.md) · 2023.09 – 2024.06 <span class="tag-badge">Featured</span>
- [Project Pinned](project-pinned.md) · 2023
- [JaramUniv Sugang API](univapi.md) · 2023
- [JaramGroupware Hub](jgw-hub.md) · 2023
- [JaramGroupware Penalty](jgw-penalty-python.md) · 2023
- [JaramGroupware Attendance](jgw-attendance-python.md) · 2023
- [Awesome Chatting App](awesomechat.md) · 2022
- [BNGdrasil](bngdrasil.md) · 2022 – 진행중
- [Mugip](mugip.md) · 2020.09 – 2021.04
- [KakaoTalk-channel-WeatherToday](kakaotalk-weatherforecast.md) · 2023
- [Azure SDK for Python](azure-sdk-python.md) · 2023

</div>

### Cloud · DevOps

<div class="project-archive-list" markdown>

- [K-Buddy](kbuddy.md) · 2023.09 – 2024.06 <span class="tag-badge">Featured</span>
- [BNGdrasil](bngdrasil.md) · 2022 – 진행중
- [Blog Post Workflow](blog-post-workflow.md) · 2024

</div>

### AI · System

<div class="project-archive-list" markdown>

- [Wegis](wegis.md) · 2025.09 – 2025.10 <span class="tag-badge">Featured</span>
- [FEMU Monitoring & Hot/Cold](femu-monitoring.md) · 2024.09 – 2024.12 <span class="tag-badge">Featured</span>
- [Phishing QR detector](qr-phishing-detector.md) · 2024

</div>

### OSS

<div class="project-archive-list" markdown>

- [FastAPI-fastkit](fastapi-fastkit.md) · 2024.08 – 진행중 <span class="tag-badge">Featured</span>
- [Azure SDK for Python](azure-sdk-python.md) · 2023
- [Azure SDK for Python — Korean Docs](azure-sdk-python-kor.md) · 2023
- [Blog Post Workflow](blog-post-workflow.md) · 2024

</div>

### Team

<div class="project-archive-list" markdown>

- [K-Buddy](kbuddy.md) · 2023.09 – 2024.06 <span class="tag-badge">Featured</span>
- [Project Pinned](project-pinned.md) · 2023
- [JaramGroupware Hub](jgw-hub.md) · 2023
- [JaramGroupware Penalty](jgw-penalty-python.md) · 2023
- [JaramGroupware Attendance](jgw-attendance-python.md) · 2023
- [Phishing QR detector](qr-phishing-detector.md) · 2024
- [Awesome Chatting App](awesomechat.md) · 2022
- [Mugip](mugip.md) · 2020.09 – 2021.04

</div>

### Personal

<div class="project-archive-list" markdown>

- [Wegis](wegis.md) · 2025.09 – 2025.10 <span class="tag-badge">Featured</span>
- [FastAPI-fastkit](fastapi-fastkit.md) · 2024.08 – 진행중 <span class="tag-badge">Featured</span>
- [FEMU Monitoring & Hot/Cold](femu-monitoring.md) · 2024.09 – 2024.12 <span class="tag-badge">Featured</span>
- [헤쳐 모여! (Fall In!)](fall-in.md) · 2026.01 – 진행중 <span class="tag-badge">Featured</span>
- [BNGdrasil](bngdrasil.md) · 2022 – 진행중
- [TooKindFriendChat](tookindfriendchat.md) · 2022
- [JaramUniv Sugang API](univapi.md) · 2023
- [rickTcal_DayLife](ricktcal.md) · 2023
- [KakaoTalk-channel-WeatherToday](kakaotalk-weatherforecast.md) · 2023

</div>

### Coursework

<div class="project-archive-list" markdown>

- [FEMU Monitoring & Hot/Cold](femu-monitoring.md) · 2024.09 – 2024.12 <span class="tag-badge">Featured</span>
- [Phishing QR detector](qr-phishing-detector.md) · 2024

</div>

### Game

<div class="project-archive-list" markdown>

- [헤쳐 모여! (Fall In!)](fall-in.md) · 2026.01 – 진행중 <span class="tag-badge">Featured</span>

</div>
