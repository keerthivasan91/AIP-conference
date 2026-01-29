// =======================================
// DOM Ready (Critical JS only)
// =======================================
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initScrollEffects();
    initAnimations();
    updateFooterYear();

    console.log("✅ AIP Conference 2026 CIT - Website Ready");
});

// =======================================
// Defer heavy work until full load
// =======================================
window.addEventListener('load', () => {
    if (window.lucide) {
        lucide.createIcons();
    }
});

// =======================================
// Mobile Navigation + Dropdown
// =======================================
function initNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (!navToggle || !navMenu) return;

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('open');
        navMenu.classList.toggle('open');
    });
}

// =======================================
// Scroll Effects (rAF throttled)
// =======================================
function initScrollEffects() {
    const navbar = document.querySelector('.navbar');
    const sections = [...document.querySelectorAll('section')];
    const navLinks = document.querySelectorAll('.nav-menu a');
    const heroContent = document.querySelector('.hero-content');

    if (!navbar) return;

    let ticking = false;

    function onScroll() {
        const scrollY = window.scrollY;

        // Navbar shadow
        navbar.classList.toggle('scrolled', scrollY > 50);

        // Active section highlight
        let current = '';
        for (const section of sections) {
            const top = section.offsetTop - 120;
            const bottom = top + section.offsetHeight;
            if (scrollY >= top && scrollY < bottom) {
                current = section.id;
                break;
            }
        }

        navLinks.forEach(link => {
            link.classList.toggle(
                'active',
                link.getAttribute('href') === `#${current}`
            );
        });

        // Hero parallax (desktop only)
        if (
            heroContent &&
            window.innerWidth > 768 &&
            scrollY < window.innerHeight
        ) {
            heroContent.style.transform = `translateY(${scrollY * 0.4}px)`;
            heroContent.style.opacity = Math.max(0.3, 1 - scrollY / 500);
        }

        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(onScroll);
            ticking = true;
        }
    });

    onScroll();
}

// =======================================
// Global Click Handler (Event Delegation)
// =======================================
document.addEventListener('click', e => {
    const link = e.target.closest('a');
    if (!link) return;

    const href = link.getAttribute('href');

    // Dropdown toggle
    if (link.classList.contains('dropdown-toggle')) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
        return;
    }

    // Close mobile menu on normal links
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    if (navToggle && navMenu) {
        navToggle.classList.remove('open');
        navMenu.classList.remove('open');
    }

    // Smooth scroll
    if (href && href.startsWith('#') && href.length > 1) {
        const target = document.querySelector(href);
        if (!target) return;

        e.preventDefault();
        window.scrollTo({
            top: target.offsetTop - 80,
            behavior: 'smooth'
        });
    }
});

// =======================================
// Intersection Observer Animations
// =======================================
function initAnimations() {
    const elements = document.querySelectorAll(
        '.info-card, .track-card, .timeline-item, .committee-card'
    );

    if (!('IntersectionObserver' in window)) {
        elements.forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
        return;
    }

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'none';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'transform 0.6s ease, opacity 0.6s ease';
        observer.observe(el);
    });
}

// =======================================
// Dynamic Footer Year
// =======================================
function updateFooterYear() {
    const yearEl = document.querySelector('.footer-bottom span');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }
}

// =======================================
// Global Error Logger (non-blocking)
// =======================================
window.addEventListener('error', e => {
    console.error('JS Error:', e.error);
});
