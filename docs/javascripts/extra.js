/*==================== ACCORDION SKILLS ====================*/
const skillsContent = document.getElementsByClassName('skills__content'),
    skillsHeader = document.querySelectorAll('.skills__header')

function toggleSkills() {
    let itemClass = this.parentNode.className

    for (i = 0; i < skillsContent.length; i++) {
        skillsContent[i].className = 'skills__content skills__close'
    }
    if (itemClass === 'skills__content skills__close') {
        this.parentNode.className = 'skills__content skills__open'
    }
}

skillsHeader.forEach((el) => {
    el.addEventListener('click', toggleSkills)
})

/*==================== QUALIFICATION TABS ====================*/
const tabs = document.querySelectorAll('[data-target]'),
    tabContents = document.querySelectorAll('[data-content]')

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target)

        tabContents.forEach(tabContent => {
            tabContent.classList.remove('qualification__active')
        })
        target.classList.add('qualification__active')

        tabs.forEach(tab => {
            tab.classList.remove('qualification__active')
        })
        tab.classList.add('qualification__active')
    })
})

/*==================== BLOG TOP PAGINATION ====================*/
// 블로그 피드 상단에 페이지 네비게이터 복제
document.addEventListener('DOMContentLoaded', function () {
    // 블로그 메인 페이지인지 확인 (/blog/ 또는 /blog/page/N/)
    const isBlogPage = window.location.pathname.match(/\/blog\/(page\/\d+\/)?$/);
    if (!isBlogPage) return;

    // 하단 페이지네이션 찾기
    const pagination = document.querySelector('nav.md-pagination');
    if (!pagination) return;

    // 헤더와 첫 번째 포스트 찾기
    const header = document.querySelector('.md-content__inner > header');
    const firstPost = document.querySelector('article.md-post--excerpt');

    if (header && firstPost) {
        // 페이지네이션 복제
        const topPagination = pagination.cloneNode(true);
        topPagination.classList.add('pagination--top');

        // 헤더 다음에 (첫 번째 포스트 앞에) 삽입
        header.after(topPagination);
    }
});
