// your_app/static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    
    // --- Navbar Scroll Effect ---
    const nav = document.getElementById('mainNav');
    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                if (window.scrollY > 20) {
                    nav.classList.add('scrolled');
                } else {
                    nav.classList.remove('scrolled');
                }
                ticking = false;
            });
            ticking = true;
        }
    });

    // --- Mobile Menu Toggle ---
    const toggler = document.getElementById('navToggler');
    const mobileMenu = document.getElementById('navMobile');

    if (toggler && mobileMenu) {
        toggler.addEventListener('click', () => {
            const isOpen = mobileMenu.style.display === 'block';
            
            // Toggle display
            mobileMenu.style.display = isOpen ? 'none' : 'block';
            
            // Update ARIA for accessibility
            toggler.setAttribute('aria-expanded', !isOpen);
        });
    }
});