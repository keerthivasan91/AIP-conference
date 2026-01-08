// ===============================
// Wait for DOM to be fully ready
// ===============================
document.addEventListener('DOMContentLoaded', function () {
    initNavigation();
    initScrollEffects();
    initSmoothScrolling();
    initAnimations();
    updateFooterYear();

    console.log("✅ AIP Conference 2026 CIT - Website Loaded Successfully!");
});
lucide.createIcons();
// ===============================
// Mobile Navigation + Dropdown
// ===============================
function initNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (!navToggle || !navMenu) return;

    /* Toggle sidebar */
    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('open');
        navMenu.classList.toggle('open');
    });

    /* Handle link clicks */
    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', (e) => {

            /* 🔑 Dropdown toggle → DO NOT close sidebar */
            if (link.classList.contains('dropdown-toggle')) {
                e.preventDefault();
                e.stopPropagation();
                link.parentElement.classList.toggle('open');
                return;
            }

            /* Normal link → close sidebar */
            navToggle.classList.remove('open');
            navMenu.classList.remove('open');
        });
    });
}

// ===============================
// Navbar Scroll Effect + Active Links
// ===============================
function initScrollEffects() {
    const navbar = document.querySelector(".navbar");
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-menu a");
    const heroContent = document.querySelector(".hero-content");

    if (!navbar) return;

    function handleScroll() {
        const scrollY = window.scrollY;

        /* Navbar shadow */
        navbar.classList.toggle("scrolled", scrollY > 50);

        /* Active section highlight */
        let currentSection = '';
        sections.forEach(section => {
            const top = section.offsetTop - 120;
            const height = section.clientHeight;
            if (scrollY >= top && scrollY < top + height) {
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });

        /* Hero parallax */
        if (heroContent && scrollY < window.innerHeight) {
            heroContent.style.transform = `translateY(${scrollY * 0.4}px)`;
            heroContent.style.opacity = Math.max(0.3, 1 - scrollY / 500);
        }
    }

    window.addEventListener("scroll", handleScroll);
    handleScroll();
}

// ===============================
// Smooth Scrolling for Anchor Links
// ===============================
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", e => {
            const href = anchor.getAttribute("href");

            if (href === "#" || href === "#!") {
                e.preventDefault();
                return;
            }

            const target = document.querySelector(href);
            if (!target) return;

            e.preventDefault();
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: "smooth"
            });
        });
    });
}

// ===============================
// Intersection Observer Animations
// ===============================
function initAnimations() {
    const elements = document.querySelectorAll(
        ".info-card, .track-card, .timeline-item, .committee-card"
    );

    if (!('IntersectionObserver' in window)) {
        elements.forEach(el => {
            el.style.opacity = "1";
            el.style.transform = "translateY(0)";
        });
        return;
    }

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(30px)";
        el.style.transition = "all 0.6s ease";
        observer.observe(el);
    });
}

// ===============================
// Dynamic Footer Year
// ===============================
function updateFooterYear() {
    const footerYear = document.querySelector(".footer-bottom span");
    if (footerYear) {
        footerYear.textContent = new Date().getFullYear();
    }
}

// ===============================
// Page Load Fade-In
// ===============================
window.addEventListener("load", () => {
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity 0.4s ease";
    setTimeout(() => {
        document.body.style.opacity = "1";
    }, 80);
});

// ===============================
// Global Error Logger
// ===============================
window.addEventListener('error', e => {
    console.error("JS Error:", e.error);
});
