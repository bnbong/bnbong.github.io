# bnbong's tech Blog

기술 관련 내용을 포스팅하는 블로그 소스코드 저장소입니다.

## Stack

> with [material for MKDocs](https://squidfunk.github.io/mkdocs-material/)

- Python 3.12.4
- Material for MKDocs

## Blog Convention

### material for MKDocs general convention

https://squidfunk.github.io/mkdocs-material/conventions/

### bnbong's blog specific convention

#### 마크다운 본문 작성 시 주의사항

- .md 파일 최상단에 정의하는 메타데이터의 title이 문서 렌더 시 H1 태그로 렌더링된다.
  따라서 본문 작성 시 문서 시작 부분에는 H1 태그를 사용하지 않는다.
- 블로그 포스팅은 docs/blog/posts 디렉토리 내에 {년월일-제목} 형식의 폴더 생성 후 그 안에 .md 파일로 본문을 작성한다.
  - 이미지 파일은 같은 디렉토리 내에 images 폴더를 생성 후 그 안에 저장한다.
  - 폴더 타이틀 작명은 항상 slug 타이틀로 적지 않아도 됨, 영어로 작성하는 것을 권장.

## MileStone

- [ ] Portfolio, Blog, Project 컨텐츠 추가
- [ ] RSS 피드 에러 해결 (no rendering)
- [ ] Notion과 연동? (가능성 낮음)
