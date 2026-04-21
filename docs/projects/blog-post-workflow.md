---
title: Blog Post Workflow
description: GitHub Action 기반 블로그 포스트 수집 프로젝트에 NAVER Blog RSS 가이드와 v1.9.5 회귀 버그 리포트를 기여한 경험
authors:
  - bnbong
tags:
  - Blog
  - rss
  - github
  - github action
  - oss
  - devops
period: 2024 - 진행중
role: 오픈소스 가이드 기여 / 버그 리포트
---

# Blog Post Workflow

## 개요

`blog-post-workflow`는 README에 블로그 최신 글 목록을 자동으로 채워 넣어 주는 GitHub Action이다.
이 프로젝트에는 두 번에 걸쳐 기여했다. 처음에는 NAVER Blog RSS feed 가이드를 공식 문서에 반영하는
작업이었고, 이후에는 `1.9.5` 릴리스에서 발생한 `item_exec` 회귀 버그를 원인까지 분석해 리포트했다.

## 기여 내용

- [:fontawesome-solid-code-pull-request: [New Source]: NAVER Blog RSS Feed](https://github.com/gautamkrishnar/blog-post-workflow/issues/241)
- [:fontawesome-solid-bug: [Bug]: Regression in 1.9.5 — `item_exec` can no longer access `customTags` / local scope variables](https://github.com/gautamkrishnar/blog-post-workflow/issues/292)

## NAVER Blog RSS 가이드

이 기여는 코드 몇 줄을 바꾸는 것보다도, **기존 자동화 워크플로우가 새로운 플랫폼을 어떻게 수용할 수 있는지**
설명하는 성격이 강했다. 한국에서는 NAVER Blog가 실제 수요가 있는 소스였기 때문에,
공식 문서에 그 경로를 추가하는 것 자체가 의미 있었다.
네이버 블로그는 Velog나 티스토리 같은 플랫폼 보다는 개발자들이 잘 찾지 않는 소스이지만 한국의 대표 블로그이기 때문에 기여할 가치가 있다고 판단했다.

## v1.9.5 `item_exec` 회귀 버그 리포트

`@v1` 태그가 `1.9.5`를 가리키기 시작한 뒤부터, 기존에 잘 돌던 내 워크플로우가 갑자기 실패했다.
RSS feed 자체는 정상적으로 수신되는데, `item_exec` 안에서 `customTags`를 참조하는 순간
다음 에러가 떨어졌다.

```txt
Error: Failure in executing `item_exec` parameter
Error: ReferenceError: customTags is not defined
```

### 원인 분석

단순 신고로 끝내지 않고 소스 차이를 직접 추적했다.

- `1.9.4`에서는 `eval(ITEM_EXEC)`로 `item_exec` 스니펫을 호출자 스코프 안에서 실행해서
  `customTags` 같은 로컬 변수에도 자연스럽게 접근할 수 있었다.
- `1.9.5`부터는 `new Function('post', ...)` 방식으로 바뀌면서 스코프가 분리됐고,
  결과적으로 `post`만 주입되어 `customTags`는 더 이상 참조할 수 없게 됐다.

즉, 기능 추가가 아니라 **실행 컨텍스트 변경이 과거 사용자의 스니펫을 조용히 깨뜨린 회귀**였다.
`customTags`가 여전히 `post`에 병합되기는 해서, `post.tag`로 우회할 수 있다는 것도 같이 확인했다.

### 리포트에서 제안한 방향

- 기존 `item_exec` 스니펫이 `customTags`를 직접 쓰는 경우에 대한 하위 호환성 유지
- 혹은 릴리스 노트/README에 `item_exec`의 실행 컨텍스트가 `post`로 제한됐음을 명시하고,
  `post.tag` 같은 대체 경로를 안내

### 왜 의미 있었는가

Patch 릴리스(`1.9.4` → `1.9.5`) 안에서 호환성이 깨진 사례였기 때문에, 나처럼 `@v1`을 신뢰하고 고정해 둔
사용자 다수가 영향을 받을 수 있었다. 그래서 단순히 "내 워크플로우가 안 돌아간다"에서 멈추지 않고,
**원인 커밋과 동작 차이**까지 정리해 유지관리자가 바로 판단할 수 있는 형태로 제출했다.

## 배운 점

- 오픈소스 기여는 기능 추가뿐 아니라, **다른 사용자가 프로젝트를 더 쉽게 쓰게 만드는 문서 기여와
  회귀 리포트**도 똑같이 중요하다.
- 버그를 "재현만" 남기는 것과 **원인 코드와 커밋까지 추적해 전달하는 것**은 기여의 무게가 완전히 다르다.
