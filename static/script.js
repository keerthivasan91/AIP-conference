// ===============================
// Wait for DOM to be fully ready
// ===============================
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    
    // Initialize all functionality after DOM is ready
    initNavigation();
    initScrollEffects();
    initSmoothScrolling();
    initAnimations();
    updateFooterYear();
    
    console.log("✅ AIP Conference 2026 CIT - Website Loaded Successfully!");
});

// ===============================
// Mobile Navigation Toggle
// ===============================
function initNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    console.log('Toggle element:', navToggle);
    console.log('Menu element:', navMenu);

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            console.log('Toggle clicked!');
            navToggle.classList.toggle('open');
            navMenu.classList.toggle('open');
            console.log('Toggle classes:', navToggle.classList);
            console.log('Menu classes:', navMenu.classList);
        });

        // Close menu when clicking on a link
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('open');
                navMenu.classList.remove('open');
            });
        });
    } else {
        console.warn('Navigation elements not found - mobile menu disabled');
    }
}

// ===============================
// Navbar Scroll Effect + Active Links
// ===============================
function initScrollEffects() {
    const navbar = document.querySelector(".navbar");
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-menu a");
    const heroContent = document.querySelector(".hero-content");

    if (!navbar) {
        console.warn('Navbar element not found');
        return;
    }

    function handleScroll() {
        const scrollY = window.scrollY;

        // Navbar scrolled effect
        navbar.classList.toggle("scrolled", scrollY > 50);

        // Active link highlight
        if (sections.length > 0 && navLinks.length > 0) {
            let currentSection = '';
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop - 100;
                const sectionHeight = section.clientHeight;
                const sectionId = section.getAttribute('id');

                if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                    currentSection = sectionId;
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${currentSection}`) {
                    link.classList.add('active');
                }
            });
        }

        // Parallax hero effect
        if (heroContent && scrollY < window.innerHeight) {
            heroContent.style.transform = `translateY(${scrollY * 0.5}px)`;
            heroContent.style.opacity = Math.max(0.3, 1 - scrollY / 500);
        }
    }

    window.addEventListener("scroll", handleScroll);
    handleScroll(); // Initialize on load
}

// ===============================
// Smooth Scrolling for Anchor Links
// ===============================
function initSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    if (anchorLinks.length === 0) {
        console.warn('No anchor links found for smooth scrolling');
        return;
    }

    anchorLinks.forEach(anchor => {
        anchor.addEventListener("click", e => {
            const href = anchor.getAttribute("href");
            
            // Skip if it's just "#"
            if (href === "#" || href === "#!") {
                e.preventDefault();
                return;
            }
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80;
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: "smooth"
                });
            }
        });
    });
}

// ===============================
// Intersection Observer (Fade-in Animations)
// ===============================
function initAnimations() {
    const animatedElements = document.querySelectorAll(".info-card, .track-card, .timeline-item");
    
    if (animatedElements.length === 0) {
        console.warn('No elements found for animation');
        return;
    }

    // Check if IntersectionObserver is supported
    if (!('IntersectionObserver' in window)) {
        console.warn('IntersectionObserver not supported - showing all elements');
        animatedElements.forEach(el => {
            el.style.opacity = "1";
            el.style.transform = "translateY(0)";
        });
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                // Unobserve after animation
                observer.unobserve(entry.target);
            }
        });
    }, { 
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    animatedElements.forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(30px)";
        el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
        observer.observe(el);
    });

    // Track Card Hover Effect
    const trackCards = document.querySelectorAll(".track-card");
    trackCards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transform = "translateY(-10px) scale(1.02)";
        });
        card.addEventListener("mouseleave", () => {
            card.style.transform = "translateY(0) scale(1)";
        });
    });
}

// ===============================
// Dynamic Year in Footer
// ===============================
function updateFooterYear() {
    const footerYear = document.querySelector(".footer-bottom p");
    if (footerYear) {
        const currentYear = new Date().getFullYear();
        footerYear.innerHTML = `&copy; Copyright AIP Conference ${currentYear}. All Rights Reserved.`;
    }
}

// ===============================
// Error Handling
// ===============================
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
});

// ===============================
// Page Load Animation
// ===============================
window.addEventListener("load", () => {
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity 0.5s ease";
    
    setTimeout(() => {
        document.body.style.opacity = "1";
    }, 100);
});