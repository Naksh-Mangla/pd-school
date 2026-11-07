import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS in <head>
css_target = """  <style>
    body {
      font-family: 'Inter', sans-serif;
      color: #1E293B;
      background-color: #F8FAFC;
      -webkit-font-smoothing: antialiased;
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .hero-gradient {
      background: linear-gradient(135deg, rgba(10, 37, 64, 0.96) 0%, rgba(30, 58, 138, 0.90) 100%),
                  url('https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd6.jpeg') center/cover no-repeat;
    }
    .gold-gradient-text {
      background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .touch-target {
      min-height: 44px;
      min-width: 44px;
    }
    .premium-card {
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }
    .premium-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 24px -8px rgba(10, 37, 64, 0.12);
    }
    .gallery-img-container {
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }
    .gallery-img-container img {
      transition: transform 0.4s ease;
    }
    .gallery-img-container:hover img {
      transform: scale(1.06);
    }
    .filter-btn.active {
      background-color: #0A2540;
      color: #ffffff;
      border-color: #0A2540;
    }
  </style>"""

new_css = """  <style>
    body {
      font-family: 'Inter', sans-serif;
      color: #1E293B;
      background-color: #F8FAFC;
      -webkit-font-smoothing: antialiased;
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .hero-gradient {
      background: linear-gradient(135deg, rgba(10, 37, 64, 0.96) 0%, rgba(30, 58, 138, 0.90) 100%),
                  url('https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd6.jpeg') center/cover no-repeat;
    }
    .gold-gradient-text {
      background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .touch-target {
      min-height: 44px;
      min-width: 44px;
    }

    /* Sleek Navbar Styling */
    header.scrolled {
      height: 64px !important;
      background-color: rgba(255, 255, 255, 0.92) !important;
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      box-shadow: 0 4px 20px -2px rgba(10, 37, 64, 0.08) !important;
      border-bottom-color: rgba(226, 232, 240, 0.8) !important;
    }
    .nav-link {
      position: relative;
      padding: 6px 12px;
      border-radius: 9999px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .nav-link:hover {
      color: #1E3A8A;
      background-color: rgba(241, 245, 249, 0.8);
    }
    .nav-link::after {
      content: '';
      position: absolute;
      bottom: 2px;
      left: 50%;
      transform: translateX(-50%) scaleX(0);
      width: 16px;
      height: 2px;
      background: #D97706;
      border-radius: 2px;
      transition: transform 0.25s ease;
    }
    .nav-link:hover::after {
      transform: translateX(-50%) scaleX(1);
    }

    /* Tactile Cards & Hover */
    .premium-card {
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .premium-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 28px -10px rgba(10, 37, 64, 0.12);
    }

    /* Mobile Friendly Animations */
    @keyframes floatSlow {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-8px); }
    }
    .animate-float {
      animation: floatSlow 4s ease-in-out infinite;
    }

    @keyframes pulseGlow {
      0%, 100% { transform: scale(1); opacity: 0.9; }
      50% { transform: scale(1.05); opacity: 1; }
    }
    .animate-pulse-glow {
      animation: pulseGlow 2.5s ease-in-out infinite;
    }

    /* Scroll Reveal */
    .reveal {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }
    .reveal.active {
      opacity: 1;
      transform: translateY(0);
    }

    /* Mobile Drawer */
    #mobile-drawer {
      transition: max-height 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease, transform 0.3s ease;
    }
    #mobile-drawer.drawer-closed {
      max-height: 0;
      opacity: 0;
      transform: translateY(-10px);
      overflow: hidden;
      pointer-events: none;
    }
    #mobile-drawer.drawer-open {
      max-height: 650px;
      opacity: 1;
      transform: translateY(0);
      overflow-y: auto;
      pointer-events: auto;
    }

    .gallery-img-container {
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }
    .gallery-img-container img {
      transition: transform 0.4s ease;
    }
    .gallery-img-container:hover img {
      transform: scale(1.06);
    }
    .filter-btn.active {
      background-color: #0A2540;
      color: #ffffff;
      border-color: #0A2540;
    }

    /* Press Feedback */
    button, a {
      -webkit-tap-highlight-color: transparent;
    }
    button:active, .btn-press:active {
      transform: scale(0.96);
    }

    @media (prefers-reduced-motion: reduce) {
      *, .animate-float, .animate-pulse-glow, .reveal {
        animation: none !important;
        transition: none !important;
        transform: none !important;
        opacity: 1 !important;
      }
    }
  </style>"""

html = html.replace(css_target, new_css)

# 2. Update Header
header_regex = re.compile(r'<header.*?</header>', re.DOTALL)
new_header = """  <!-- ========================================== -->
  <!-- 2. MAIN NAVIGATION (SLEEK & STICKY)       -->
  <!-- ========================================== -->
  <header id="main-header" class="sticky top-0 z-40 bg-white/85 backdrop-blur-xl shadow-xs border-b border-slate-200/80 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-[70px] flex items-center justify-between transition-all duration-300" id="header-container">
      
      <!-- Logo & Branding -->
      <a href="#home" class="flex items-center gap-3 group">
        <div class="relative">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/04/pdlogo.jpeg" alt="P.D. Public School Crest" class="w-10 h-10 sm:w-11 sm:h-11 object-contain rounded-full shadow-sm ring-2 ring-brand-amber/30 p-0.5 bg-white group-hover:scale-105 transition duration-300">
          <span class="absolute bottom-0 right-0 w-2.5 h-2.5 rounded-full bg-emerald-500 ring-2 ring-white animate-pulse"></span>
        </div>
        <div>
          <span class="block text-base sm:text-lg font-extrabold text-brand-navy tracking-tight leading-none group-hover:text-brand-blue transition">
            P.D. PUBLIC SCHOOL
          </span>
          <span class="block text-[10px] sm:text-[11px] font-semibold text-brand-gold tracking-wider uppercase mt-1">
            CBSE (10+2) • Mewat, Haryana
          </span>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-1 xl:gap-2 text-xs xl:text-sm font-semibold text-slate-700">
        <a href="#home" class="nav-link">Home</a>
        <a href="#about" class="nav-link">About</a>
        <a href="#academics" class="nav-link">Academics</a>
        <a href="#admissions" class="nav-link">Admissions</a>
        <a href="#fees" class="nav-link">Fee Structure</a>
        <a href="#facilities" class="nav-link">Facilities</a>
        <a href="#gallery" class="nav-link">Gallery</a>
        <a href="#disclosures" class="nav-link">CBSE Disclosures</a>
        <a href="#contact" class="nav-link">Contact</a>
      </nav>

      <!-- Desktop Header CTA -->
      <div class="hidden sm:flex items-center gap-2.5">
        <a href="https://wa.me/918607288800?text=Hello%20PD%20Public%20School,%20I%20want%20to%20inquire%20about%20admissions." target="_blank" rel="noopener noreferrer" class="px-3.5 py-1.5 rounded-full text-xs font-bold text-emerald-800 bg-emerald-50 hover:bg-emerald-100 transition flex items-center gap-1.5 border border-emerald-200/80 shadow-2xs">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          WhatsApp Desk
        </a>
        <button onclick="openInquiryModal()" class="px-5 py-2 rounded-full text-xs font-bold text-white bg-gradient-to-r from-brand-royal to-brand-navy hover:from-brand-navy hover:to-brand-royal shadow-sm hover:shadow transition transform hover:-translate-y-0.5">
          Apply Now
        </button>
      </div>

      <!-- Mobile Menu Hamburger Button -->
      <button id="menu-toggle" aria-label="Open Mobile Menu" class="lg:hidden p-2 rounded-xl text-slate-700 hover:bg-slate-100/80 transition touch-target flex items-center justify-center">
        <div class="w-5 h-4 flex flex-col justify-between items-center relative" id="hamburger-icon">
          <span class="w-5 h-0.5 bg-slate-800 rounded-full transition-all duration-300 origin-center" id="bar1"></span>
          <span class="w-5 h-0.5 bg-slate-800 rounded-full transition-all duration-300" id="bar2"></span>
          <span class="w-5 h-0.5 bg-slate-800 rounded-full transition-all duration-300 origin-center" id="bar3"></span>
        </div>
      </button>

    </div>

    <!-- Sleek Mobile Navigation Drawer -->
    <div id="mobile-drawer" class="lg:hidden drawer-closed bg-white/95 backdrop-blur-2xl border-b border-slate-200 px-5 py-5 shadow-2xl">
      <nav class="grid grid-cols-2 gap-2 text-sm font-semibold text-slate-800">
        <a href="#home" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-brand-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
          Home
        </a>
        <a href="#about" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-brand-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          About Us
        </a>
        <a href="#academics" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
          Academics
        </a>
        <a href="#admissions" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          Admissions
        </a>
        <a href="#fees" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-brand-royal" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
          Fees
        </a>
        <a href="#facilities" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
          Facilities
        </a>
        <a href="#gallery" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-pink-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          Gallery
        </a>
        <a href="#disclosures" class="mobile-nav-link flex items-center gap-2.5 px-3 py-2.5 rounded-xl hover:bg-slate-100/80 transition">
          <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          CBSE Info
        </a>
      </nav>
      <div class="mt-4 pt-4 border-t border-slate-200/80 flex flex-col gap-2.5">
        <button onclick="openInquiryModal()" class="w-full py-3 rounded-xl text-center font-bold text-sm text-white bg-gradient-to-r from-brand-royal to-brand-navy shadow-sm transition">
          Quick Admission Inquiry
        </button>
        <div class="flex items-center gap-2">
          <a href="tel:+918607288800" class="flex-1 py-2.5 rounded-xl text-center font-semibold text-xs text-brand-navy bg-slate-100 hover:bg-slate-200 transition">
            Call Office
          </a>
          <a href="https://wa.me/918607288800" target="_blank" rel="noopener noreferrer" class="flex-1 py-2.5 rounded-xl text-center font-semibold text-xs text-emerald-800 bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 transition">
            WhatsApp
          </a>
        </div>
      </div>
    </div>
  </header>"""

html = header_regex.sub(new_header, html)

# 3. Add animate-float to pd9 image in hero
html = html.replace(
    'src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd9.png" alt="P.D. Public School Students & Learning" class="w-full max-h-72 sm:max-h-80 object-contain mx-auto drop-shadow-2xl"',
    'src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd9.png" alt="P.D. Public School Students & Learning" class="w-full max-h-72 sm:max-h-80 object-contain mx-auto drop-shadow-2xl animate-float"'
)

# 4. Add reveal class to main section cards
html = html.replace('class="premium-card"', 'class="premium-card reveal"')
html = html.replace('class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm relative"', 'class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm relative reveal"')
html = html.replace('class="bg-white rounded-2xl p-8 border border-slate-200 shadow-sm flex flex-col justify-between"', 'class="bg-white rounded-2xl p-8 border border-slate-200 shadow-sm flex flex-col justify-between reveal"')
html = html.replace('class="gallery-item', 'class="gallery-item reveal')

# 5. Update JavaScript block
js_target = """  <script>
    // Mobile Drawer Toggle
    const menuToggle = document.getElementById('menu-toggle');
    const mobileDrawer = document.getElementById('mobile-drawer');
    const iconOpen = document.getElementById('menu-icon-open');
    const iconClose = document.getElementById('menu-icon-close');

    menuToggle.addEventListener('click', () => {
      const isExpanded = !mobileDrawer.classList.contains('hidden');
      if (isExpanded) {
        mobileDrawer.classList.add('hidden');
        iconOpen.classList.remove('hidden');
        iconClose.classList.add('hidden');
      } else {
        mobileDrawer.classList.remove('hidden');
        iconOpen.classList.add('hidden');
        iconClose.classList.remove('hidden');
      }
    });

    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => {
        mobileDrawer.classList.add('hidden');
        iconOpen.classList.remove('hidden');
        iconClose.classList.add('hidden');
      });
    });"""

new_js = """  <script>
    // Sleek Mobile Drawer Toggle with Animated Hamburger Icon
    const menuToggle = document.getElementById('menu-toggle');
    const mobileDrawer = document.getElementById('mobile-drawer');
    const bar1 = document.getElementById('bar1');
    const bar2 = document.getElementById('bar2');
    const bar3 = document.getElementById('bar3');

    let isMenuOpen = false;

    function toggleMenu(open) {
      isMenuOpen = (open !== undefined) ? open : !isMenuOpen;
      if (isMenuOpen) {
        mobileDrawer.classList.remove('drawer-closed');
        mobileDrawer.classList.add('drawer-open');
        bar1.style.transform = 'translateY(7px) rotate(45deg)';
        bar2.style.opacity = '0';
        bar3.style.transform = 'translateY(-7px) rotate(-45deg)';
      } else {
        mobileDrawer.classList.remove('drawer-open');
        mobileDrawer.classList.add('drawer-closed');
        bar1.style.transform = 'none';
        bar2.style.opacity = '1';
        bar3.style.transform = 'none';
      }
    }

    menuToggle.addEventListener('click', () => toggleMenu());

    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => toggleMenu(false));
    });

    // Sleek Navbar shrink on scroll
    const mainHeader = document.getElementById('main-header');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 25) {
        mainHeader.classList.add('scrolled');
      } else {
        mainHeader.classList.remove('scrolled');
      }
    }, { passive: true });

    // Smooth Scroll Reveal Animation (Mobile Optimized)
    const revealElements = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
          }
        });
      }, {
        rootMargin: '0px 0px -30px 0px',
        threshold: 0.08
      });

      revealElements.forEach(el => observer.observe(el));
    } else {
      revealElements.forEach(el => el.classList.add('active'));
    }"""

html = html.replace(js_target, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Navbar & Mobile Animations successfully updated!")

