---
title: Open Source
description: bnbong이 운영/유지하거나 외부 저장소에 기여한 오픈소스 작업
hide:
  - toc
---

# Open Source

오픈소스는 저에게 "코드로 쓰는 자기소개"이자 "빠른 피드백 루프"입니다. 매일 쓰는 도구의
부족한 부분을 직접 고치거나, 한국어 사용자의 언어 장벽을 낮추는 작은 번역 커밋이라도 꾸준히
쌓아 두려 합니다. 여기서는 **운영/유지하는 프로젝트**와 **외부 저장소에 기여한 작업**을
나눠 정리합니다.

[:fontawesome-brands-github: GitHub 프로필 방문하기](https://github.com/bnbong){ .md-button .md-button--primary }

## 직접 운영/유지하는 OSS

<div class="grid cards" markdown>

-   :material-package-variant:{ .lg .middle } **FastAPI-fastkit**

    ---

    FastAPI 기반 백엔드 프로젝트의 부트스트랩을 가속하는 CLI + 템플릿 모음.
    Python 생태계 의존성 관리와 프로젝트 구조 표준화에 초점을 맞췄습니다.

    - 최신 상세: [자세히 보기 →](../projects/fastapi-fastkit.md)
    - 업스트림: <https://github.com/bnbong/FastAPI-fastkit>
    - 배포: PyPI 공개 패키지 (최신 버전은 PyPI 및 GitHub Releases 참조)

    **대표 기여**

    - 템플릿 스캐폴딩 CLI 설계 및 유지보수
    - 다중 템플릿(Async/Sync) 관리 구조
    - 문서화 및 사용자 피드백 반영 사이클 운영

</div>

## 외부 저장소 기여

<div class="grid cards" markdown>

-   :material-microsoft-azure:{ .lg .middle } **Azure SDK for Python**

    ---

    Microsoft Azure의 Python SDK 저장소에 기여.

    - 업스트림: <https://github.com/Azure/azure-sdk-for-python>
    - 내부 정리: [자세히 보기 →](../projects/azure-sdk-python.md)

    **대표 기여**

    - 샘플 및 문서 개선 PR
    - 재현 가능한 이슈 리포트

-   :material-translate:{ .lg .middle } **Azure SDK for Python — Korean Docs**

    ---

    Azure Python SDK 공식 문서의 한국어 번역/현지화 기여.

    - 업스트림: <https://github.com/Azure/azure-docs-sdk-python>
    - 내부 정리: [자세히 보기 →](../projects/azure-sdk-python-kor.md)

    **대표 기여**

    - 기술 용어 일관성을 지킨 번역 커밋
    - 오탈자/링크 교정

-   :material-rss:{ .lg .middle } **Blog Post Workflow**

    ---

    GitHub 프로필 README에 블로그 RSS 목록을 자동 동기화해 주는 GitHub Action.

    - 업스트림: <https://github.com/gautamkrishnar/blog-post-workflow>
    - 내부 정리: [자세히 보기 →](../projects/blog-post-workflow.md)

    **대표 기여**

    - 특정 피드 파싱 케이스 버그 수정 / 기능 PR

-   :material-harddisk:{ .lg .middle } **FEMU Monitoring & Hot/Cold**

    ---

    가상 SSD 에뮬레이터 FEMU에 WAF/IOPS/Latency 계측 모듈을 추가하고, Hot/Cold
    데이터 분리 기법을 얹은 개인 연구 프로젝트. 수업 과제에서 출발해 업스트림 구조에
    실제 기여 가능한 형태로 다듬었습니다.

    - 업스트림: <https://github.com/MoatLab/FEMU>
    - 내부 정리: [자세히 보기 →](../projects/femu-monitoring.md)

    **대표 기여**

    - WAF / Throughput / Latency 계측 모듈
    - Hot/Cold write pointer 분리 및 FTL 수정

</div>
