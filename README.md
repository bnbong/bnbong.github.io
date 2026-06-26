# bnbong's tech Blog — Redirect Bridge

> ⚠️ 이 블로그는 **[bnbong.com](https://bnbong.com/)** 으로 이전했습니다.

이 저장소는 더 이상 블로그 본문을 빌드하지 않습니다.

`https://bnbong.github.io` 로 들어오는 모든 요청(옛 글 딥링크 포함)을 `https://bnbong.com` 으로 보내는 **리다이렉트 브리지**로만 동작합니다.

## 동작 방식

- [`redirect/index.html`](redirect/index.html) — 루트 진입 리다이렉트
- [`redirect/404.html`](redirect/404.html) — 존재하지 않는 모든 경로(옛 블로그 URL 등)를 GitHub Pages의 404 처리로 가로채 홈으로 리다이렉트 (catch-all)
- 각 페이지는 `<meta refresh>` + `location.replace()` + `<link rel="canonical">` + `noindex` 조합으로 리다이렉트와 검색엔진 색인 정리를 함께 처리한다.
- [`.github/workflows/ci.yml`](.github/workflows/ci.yml) 가 push 시 `redirect/` 만 orphan `gh-pages` 브랜치로 강제 배포한다.

## 원본 소스 (보관용)

이전 MkDocs(Material) 기반 블로그 소스(`docs/`, `overrides/`, `mkdocs.yml`, `requirements.txt` 등)는 히스토리 보관 목적으로 남겨두었으며 더 이상 빌드/배포되지 않는다.
