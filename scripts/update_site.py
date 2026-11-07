import re

# Read the base template or write the complete enhanced HTML
enhanced_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>P.D. Public Senior Secondary School | Ferozepur Jhirka, Mewat</title>
  <meta name="description" content="Official website of P.D. Public Senior Secondary School, Ferozepur Jhirka (Mewat), Haryana. Affiliated to CBSE, New Delhi. Admissions Open for Nursery to Class 12.">
  <meta name="keywords" content="PD Public School, Ferozepur Jhirka, CBSE School Mewat, Best School in Ferozepur Jhirka, Admissions 2025-26">

  <!-- Open Graph / Meta -->
  <meta property="og:title" content="P.D. Public Sr. Sec. School | Ferozepur Jhirka">
  <meta property="og:description" content="Empowering Minds, Shaping Futures. CBSE Affiliated Senior Secondary School in Ferozepur Jhirka (Mewat).">
  <meta property="og:image" content="https://pdpublicschool.co.in/wp-content/uploads/2024/04/pdlogo.jpeg">
  <meta property="og:url" content="https://pdpublicschool.co.in/">
  <meta name="theme-color" content="#0A2540">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="https://pdpublicschool.co.in/wp-content/uploads/2024/04/cropped-pdlogo-1-32x32.png">

  <!-- Google Fonts: Plus Jakarta Sans & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              navy: '#0A2540',
              royal: '#1E3A8A',
              blue: '#2563EB',
              gold: '#D97706',
              amber: '#F59E0B',
              slate: '#F8FAFC',
              dark: '#0F172A',
              muted: '#64748B'
            }
          },
          fontFamily: {
            heading: ['Plus Jakarta Sans', 'sans-serif'],
            body: ['Inter', 'sans-serif']
          }
        }
      }
    }
  </script>

  <style>
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
                  url('https://pdpublicschool.co.in/wp-content/uploads/2024/04/pd4-1024x768.jpg') center/cover no-repeat;
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
  </style>
</head>
<body class="overflow-x-hidden antialiased flex flex-col min-h-screen">

  <!-- ========================================== -->
  <!-- 1. TOP ANNOUNCEMENT BAR                    -->
  <!-- ========================================== -->
  <div class="bg-brand-navy text-white text-xs sm:text-sm py-2 px-4 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
      <div class="flex items-center gap-2 text-center sm:text-left">
        <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-brand-amber text-brand-dark">ADMISSIONS 2025-26</span>
        <span class="text-slate-200">Open for Nursery to Class 12 (CBSE Affiliated, New Delhi)</span>
      </div>
      <div class="hidden md:flex items-center gap-4 text-slate-300">
        <a href="tel:+918607288800" class="hover:text-brand-amber transition flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          +91 8607288800
        </a>
        <span class="text-slate-600">|</span>
        <a href="mailto:pdpublicschl@gmail.com" class="hover:text-brand-amber transition flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
          pdpublicschl@gmail.com
        </a>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 2. MAIN NAVIGATION (STICKY)               -->
  <!-- ========================================== -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-100 transition-all duration-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Logo & Branding -->
      <a href="#home" class="flex items-center gap-3.5 group">
        <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/04/pdlogo.jpeg" alt="P.D. Public School Crest" class="w-12 h-12 object-contain rounded-full shadow-sm border border-slate-200">
        <div>
          <span class="block text-lg sm:text-xl font-extrabold text-brand-navy tracking-tight leading-tight group-hover:text-brand-blue transition">
            P.D. PUBLIC SCHOOL
          </span>
          <span class="block text-[11px] sm:text-xs font-semibold text-brand-gold tracking-wide uppercase">
            Senior Secondary • CBSE Affiliated (HR.)
          </span>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-medium text-slate-700">
        <a href="#home" class="hover:text-brand-blue transition">Home</a>
        <a href="#about" class="hover:text-brand-blue transition">About</a>
        <a href="#academics" class="hover:text-brand-blue transition">Academics</a>
        <a href="#admissions" class="hover:text-brand-blue transition">Admissions</a>
        <a href="#fees" class="hover:text-brand-blue transition">Fee Structure</a>
        <a href="#facilities" class="hover:text-brand-blue transition">Facilities</a>
        <a href="#gallery" class="hover:text-brand-blue transition">Gallery</a>
        <a href="#disclosures" class="hover:text-brand-blue transition">CBSE Disclosures</a>
        <a href="#contact" class="hover:text-brand-blue transition">Contact</a>
      </nav>

      <!-- Desktop Header CTA -->
      <div class="hidden sm:flex items-center gap-3">
        <a href="https://wa.me/918607288800?text=Hello%20PD%20Public%20School,%20I%20want%20to%20inquire%20about%20admissions." target="_blank" rel="noopener noreferrer" class="px-4 py-2.5 rounded-lg text-sm font-semibold text-emerald-700 bg-emerald-50 hover:bg-emerald-100 transition flex items-center gap-1.5 border border-emerald-200">
          <svg class="w-4 h-4 fill-emerald-600" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.634.074-1.637-.323-.972-.387-1.579-1.378-1.63-1.442-.045-.064-.396-.527-.396-1.004 0-.477.25-.712.339-.81.089-.098.192-.122.257-.122.064 0 .128.001.185.006.059.006.138-.022.215.163.08.188.272.663.296.711.024.048.04.106.008.17-.032.064-.048.106-.096.162-.048.056-.101.125-.145.168-.048.048-.098.1-.042.196.056.096.249.41.534.664.368.327.679.429.775.477.096.048.152.04.208-.024.056-.064.24-.28.304-.376.064-.096.128-.08.216-.048.088.032.56.264.656.312.096.048.16.072.184.112.024.04.024.233-.12.638z"/></svg>
          WhatsApp Desk
        </a>
        <button onclick="openInquiryModal()" class="px-5 py-2.5 rounded-lg text-sm font-semibold text-white bg-brand-royal hover:bg-brand-navy shadow-sm transition">
          Apply Now
        </button>
      </div>

      <!-- Mobile Menu Hamburger Button -->
      <button id="menu-toggle" aria-label="Open Mobile Menu" class="lg:hidden p-2.5 rounded-lg text-slate-700 hover:bg-slate-100 transition touch-target flex items-center justify-center">
        <svg id="menu-icon-open" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
        <svg id="menu-icon-close" class="w-6 h-6 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

    </div>

    <!-- Mobile Navigation Drawer -->
    <div id="mobile-drawer" class="lg:hidden hidden bg-white border-b border-slate-200 px-6 py-6 transition-all duration-300">
      <nav class="flex flex-col gap-4 text-base font-semibold text-slate-800">
        <a href="#home" class="py-2 border-b border-slate-100 mobile-nav-link">Home</a>
        <a href="#about" class="py-2 border-b border-slate-100 mobile-nav-link">About Us</a>
        <a href="#academics" class="py-2 border-b border-slate-100 mobile-nav-link">Academics & Wings</a>
        <a href="#admissions" class="py-2 border-b border-slate-100 mobile-nav-link">Admission Procedure</a>
        <a href="#fees" class="py-2 border-b border-slate-100 mobile-nav-link">Fee Structure 2025-26</a>
        <a href="#facilities" class="py-2 border-b border-slate-100 mobile-nav-link">Labs & Facilities</a>
        <a href="#gallery" class="py-2 border-b border-slate-100 mobile-nav-link">Campus Photo Gallery</a>
        <a href="#committee" class="py-2 border-b border-slate-100 mobile-nav-link">Managing Committee</a>
        <a href="#disclosures" class="py-2 border-b border-slate-100 mobile-nav-link">Mandatory CBSE Disclosures</a>
        <a href="#contact" class="py-2 mobile-nav-link">Contact & Location</a>
      </nav>
      <div class="mt-6 pt-4 border-t border-slate-200 flex flex-col gap-3">
        <button onclick="openInquiryModal()" class="w-full py-3 rounded-lg text-center font-bold text-white bg-brand-royal hover:bg-brand-navy shadow transition">
          Quick Admission Inquiry
        </button>
        <a href="tel:+918607288800" class="w-full py-3 rounded-lg text-center font-semibold text-brand-navy bg-slate-100 hover:bg-slate-200 transition">
          Call Principal Office: +91 8607288800
        </a>
      </div>
    </div>
  </header>

  <main class="flex-grow">
    
    <!-- ========================================== -->
    <!-- 3. HERO SECTION (WITH PD9.PNG AT TOP)      -->
    <!-- ========================================== -->
    <section id="home" class="relative hero-gradient text-white py-14 sm:py-20 lg:py-24 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
        
        <!-- Left: Headings, School Mission & CTAs -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-brand-amber text-xs sm:text-sm font-semibold">
            <span class="w-2 h-2 rounded-full bg-brand-amber animate-pulse"></span>
            Recognized & Affiliated to CBSE, New Delhi
          </div>
          
          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white leading-tight">
            Empowering Minds,<br>
            <span class="gold-gradient-text">Shaping Futures.</span>
          </h1>

          <p class="text-base sm:text-lg text-slate-200 max-w-2xl mx-auto lg:mx-0 font-normal leading-relaxed">
            Welcome to <strong class="text-white">P.D. Public Senior Secondary School</strong>, Ferozepur Jhirka (Mewat). We believe in empowering individuals to realize their dreams and creative genius with requisite knowledge, modern scientific laboratories, and strong moral ethics.
          </p>

          <div class="flex flex-col sm:flex-row gap-3.5 justify-center lg:justify-start pt-2">
            <button onclick="openInquiryModal()" class="px-7 py-3.5 rounded-xl font-bold text-base text-brand-dark bg-brand-amber hover:bg-amber-400 shadow-lg shadow-amber-500/20 transition transform active:scale-95">
              Apply for Admission
            </button>
            <a href="#fees" class="px-7 py-3.5 rounded-xl font-semibold text-base text-white bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 transition">
              View Fee Structure
            </a>
          </div>

          <!-- Quick Badges -->
          <div class="pt-6 grid grid-cols-2 sm:grid-cols-4 gap-4 border-t border-white/15 text-left">
            <div>
              <span class="block text-2xl font-bold text-white">30+ Yrs</span>
              <span class="text-xs text-slate-300">Legacy of Trust</span>
            </div>
            <div>
              <span class="block text-2xl font-bold text-white">100%</span>
              <span class="text-xs text-slate-300">CBSE Results</span>
            </div>
            <div>
              <span class="block text-2xl font-bold text-white">3 Labs</span>
              <span class="text-xs text-slate-300">Modern Sciences</span>
            </div>
            <div>
              <span class="block text-2xl font-bold text-white">15+</span>
              <span class="text-xs text-slate-300">Safe Bus Routes</span>
            </div>
          </div>

        </div>

        <!-- Right: PROMINENT TOP IMAGE (pd9.png) & FAST-TRACK INQUIRY -->
        <div class="lg:col-span-5 flex flex-col items-center">
          
          <!-- Official Student & Learning Illustration (pd9.png) -->
          <div class="relative w-full max-w-md mx-auto group">
            <div class="absolute -inset-1 bg-gradient-to-r from-amber-400 to-blue-500 rounded-3xl blur opacity-30 group-hover:opacity-60 transition duration-500"></div>
            <div class="relative bg-white/10 backdrop-blur-md border border-white/20 p-4 sm:p-5 rounded-3xl shadow-2xl text-center">
              
              <!-- Featured pd9.png image at top -->
              <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd9.png" alt="P.D. Public School Students & Learning" class="w-full max-h-72 sm:max-h-80 object-contain mx-auto drop-shadow-2xl">
              
              <div class="mt-4 pt-3 border-t border-white/15 flex items-center justify-between text-left px-2">
                <div>
                  <span class="block text-xs font-bold text-brand-amber uppercase tracking-wider">Admissions Active</span>
                  <span class="text-xs text-slate-200">Classes: Nursery to 12th Grade</span>
                </div>
                <button onclick="openInquiryModal()" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-brand-navy hover:bg-brand-amber transition shadow">
                  Quick Inquiry &rarr;
                </button>
              </div>

            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- 4. NOTICE BOARD & CIRCULARS BANNER        -->
    <!-- ========================================== -->
    <section class="bg-amber-50/80 border-y border-amber-200/60 py-3.5 px-4 sm:px-6">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <span class="flex h-3 w-3 relative">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-3 w-3 bg-brand-gold"></span>
          </span>
          <span class="text-xs font-extrabold uppercase tracking-wider text-amber-900 bg-amber-200 px-2 py-0.5 rounded">Latest Notice</span>
          <p class="text-sm font-semibold text-slate-800">
            Admissions for 2025-26 Session open. Diagnostic skill assessment scheduled for new admissions.
          </p>
        </div>
        <div class="flex items-center gap-3 text-xs font-bold">
          <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/CALENDER-2025-26.pdf" target="_blank" rel="noopener noreferrer" class="px-3.5 py-1.5 rounded-lg bg-white border border-amber-300 text-brand-navy hover:bg-amber-100 transition shadow-sm">
            Download Academic Calendar (PDF)
          </a>
          <a href="#disclosures" class="px-3.5 py-1.5 rounded-lg bg-brand-navy text-white hover:bg-brand-royal transition shadow-sm">
            CBSE Public Disclosures
          </a>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- 5. RECOGNITION & HON'BLE MINISTER VISIT   -->
    <!-- ========================================== -->
    <section class="py-12 bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-slate-50 rounded-2xl p-6 sm:p-8 border border-slate-200 shadow-sm flex flex-col lg:flex-row items-center gap-8">
          <div class="lg:w-1/2 rounded-xl overflow-hidden shadow-md border border-slate-200">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/Ch.-Kanwar-Pal-Gurjar-Education-Minister-Haryana-768x347.jpg" alt="Hon'ble Education Minister Haryana visiting PD Public School" class="w-full h-auto object-cover hover:scale-105 transition duration-500">
          </div>
          <div class="lg:w-1/2 space-y-3 text-left">
            <div class="inline-flex items-center gap-1.5 text-xs font-bold text-brand-gold uppercase tracking-wider bg-amber-50 px-3 py-1 rounded-full border border-amber-200">
              State Government Recognition
            </div>
            <h3 class="text-2xl font-bold text-brand-navy">Excellence in Regional Education</h3>
            <p class="text-slate-600 text-sm leading-relaxed">
              P.D. Public Senior Secondary School has been consistently recognized by education authorities for maintaining exemplary academic standards, modern science laboratories, and inclusive student development across Ferozepur Jhirka and Mewat district.
            </p>
            <div class="pt-2 flex items-center gap-4 text-xs font-semibold text-slate-500">
              <span>&#10003; Certified CBSE Affiliation</span>
              <span>&#10003; PWD Certified Building Safety</span>
              <span>&#10003; Clean Water & Hygiene Approved</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- 6. ABOUT US & LEADERSHIP DESK             -->
    <!-- ========================================== -->
    <section id="about" class="py-20 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold text-brand-gold uppercase tracking-widest">Our Heritage & Values</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Welcome to P.D. Public School</h2>
        <div class="w-16 h-1 bg-brand-amber mx-auto mt-4 rounded-full"></div>
        <p class="text-slate-600 mt-4 text-base sm:text-lg">
          Established to provide top-tier English medium education in Ferozepur Jhirka (Mewat), blending academic discipline with real-world skills.
        </p>
      </div>

      <!-- Campus & Highlights Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <!-- Campus Image Showcase -->
        <div class="relative">
          <div class="rounded-2xl overflow-hidden shadow-xl border border-slate-200">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/04/pd4-1024x768.jpg" alt="P.D. Public School Main Building" class="w-full h-80 sm:h-96 object-cover hover:scale-105 transition duration-500">
          </div>
          <div class="absolute -bottom-6 -right-4 sm:right-6 bg-brand-navy text-white p-5 rounded-xl shadow-xl max-w-xs border border-white/20">
            <div class="text-2xl font-bold text-brand-amber">CBSE Certified</div>
            <div class="text-xs text-slate-300 mt-1">Co-educational Senior Secondary Institution with comprehensive transportation across the region.</div>
          </div>
        </div>

        <!-- Vision, Mission & Goals -->
        <div class="space-y-6">
          <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm premium-card">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg bg-blue-50 text-brand-blue flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-brand-navy">Our Vision</h3>
                <p class="text-slate-600 text-sm mt-1 leading-relaxed">
                  To ignite young minds to do common things in life in an uncommon way, equipping each student with knowledge, character, and confidence to lead society.
                </p>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm premium-card">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg bg-amber-50 text-brand-gold flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-brand-navy">Our Mission</h3>
                <p class="text-slate-600 text-sm mt-1 leading-relaxed">
                  To provide accessible, high-quality, modern CBSE education with strong personal mentorship, practical laboratory training, sports, and moral ethics.
                </p>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm premium-card">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-brand-navy">Diagnostic Assessment</h3>
                <p class="text-slate-600 text-sm mt-1 leading-relaxed">
                  Every new student undertakes our friendly diagnostic test to understand their strengths and learning needs so teachers can personalize their guidance.
                </p>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- Leadership Desk (Real School Insights) -->
      <div class="mt-16 grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-white rounded-2xl p-8 border border-slate-200 shadow-sm flex flex-col justify-between">
          <div>
            <span class="text-xs font-bold text-brand-gold uppercase tracking-wider">Leadership Message</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">From the Director's Desk</h3>
            <div class="w-10 h-0.5 bg-brand-gold my-3"></div>
            <p class="text-slate-600 text-sm leading-relaxed italic">
              "At P.D. Public School, education is not merely the accumulation of facts; it is the ignition of independent thinking. We invest in top infrastructure, caring teachers, and a safe environment where every student can reach their fullest potential."
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
            <div>
              <div class="font-bold text-brand-navy">Sh. Anil Goyal</div>
              <div class="text-xs text-slate-500">President / Director, School Management</div>
            </div>
            <span class="text-xs font-semibold px-2.5 py-1 bg-slate-100 rounded text-slate-700">Ferozepur Jhirka</span>
          </div>
        </div>

        <div class="bg-white rounded-2xl p-8 border border-slate-200 shadow-sm flex flex-col justify-between">
          <div>
            <span class="text-xs font-bold text-brand-blue uppercase tracking-wider">Academic Guidance</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">From the Principal & Headmistress Desk</h3>
            <div class="w-10 h-0.5 bg-brand-blue my-3"></div>
            <p class="text-slate-600 text-sm leading-relaxed italic">
              "We work hand-in-hand with parents to cultivate discipline, curiosity, and sportsmanship. Our classrooms combine modern teaching methodologies with individualized attention so no child is left behind."
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
            <div>
              <div class="font-bold text-brand-navy">Mrs. Jyoti Sharma</div>
              <div class="text-xs text-slate-500">Headmistress / Ex-Officio Member</div>
            </div>
            <span class="text-xs font-semibold px-2.5 py-1 bg-slate-100 rounded text-slate-700">CBSE Curriculum</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- 7. ACADEMICS & STREAMS                    -->
    <!-- ========================================== -->
    <section id="academics" class="py-20 bg-slate-100/60 border-y border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16">
          <span class="text-xs font-bold text-brand-royal uppercase tracking-widest">Academic Pathways</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Comprehensive CBSE Curriculum</h2>
          <div class="w-16 h-1 bg-brand-royal mx-auto mt-4 rounded-full"></div>
          <p class="text-slate-600 mt-4 text-base">
            From kindergarten foundational play to senior secondary board examinations, our curriculum is carefully phased for excellence.
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm premium-card flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-pink-50 text-pink-600 font-bold flex items-center justify-center text-lg mb-4">
                KG
              </div>
              <h3 class="text-lg font-bold text-brand-navy">Pre-Primary Wing</h3>
              <span class="text-xs font-semibold text-pink-600">Nursery, L.K.G & U.K.G</span>
              <p class="text-slate-600 text-xs sm:text-sm mt-3 leading-relaxed">
                Play-based foundational learning, phonics, motor skills development, creative arts, and gentle social development.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-slate-100 text-xs font-semibold text-slate-500">
              Annual Diagnostic Tracking
            </div>
          </div>

          <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm premium-card flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-blue-50 text-brand-blue font-bold flex items-center justify-center text-lg mb-4">
                1-5
              </div>
              <h3 class="text-lg font-bold text-brand-navy">Primary Wing</h3>
              <span class="text-xs font-semibold text-brand-blue">Classes 1st to 5th</span>
              <p class="text-slate-600 text-xs sm:text-sm mt-3 leading-relaxed">
                Strong conceptual foundations in Mathematics, English, Hindi, and Environmental Studies with activity-led learning.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-slate-100 text-xs font-semibold text-slate-500">
              Interactive Smart Classes
            </div>
          </div>

          <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm premium-card flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-amber-50 text-brand-gold font-bold flex items-center justify-center text-lg mb-4">
                6-8
              </div>
              <h3 class="text-lg font-bold text-brand-navy">Middle Wing</h3>
              <span class="text-xs font-semibold text-brand-gold">Classes 6th to 8th</span>
              <p class="text-slate-600 text-xs sm:text-sm mt-3 leading-relaxed">
                Transition to subject-specialized science laboratories, social science projects, computer education, and sports.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-slate-100 text-xs font-semibold text-slate-500">
              Practical Lab Orientation
            </div>
          </div>

          <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm premium-card flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-purple-50 text-purple-600 font-bold flex items-center justify-center text-lg mb-4">
                9-12
              </div>
              <h3 class="text-lg font-bold text-brand-navy">Senior Secondary</h3>
              <span class="text-xs font-semibold text-purple-600">Science, Commerce & Arts</span>
              <p class="text-slate-600 text-xs sm:text-sm mt-3 leading-relaxed">
                Rigorous CBSE board exam coaching, competitive test guidance, and career counseling with top subject teachers.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-slate-100 text-xs font-semibold text-slate-500">
              100% Board Exam Success
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- 8. CAMPUS INFRASTRUCTURE & ALL REAL LABS   -->
    <!-- ========================================== -->
    <section id="facilities" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold text-brand-gold uppercase tracking-widest">State-Of-The-Art Facilities</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Campus Infrastructure</h2>
        <div class="w-16 h-1 bg-brand-amber mx-auto mt-4 rounded-full"></div>
        <p class="text-slate-600 mt-4 text-base">
          Our school provides dedicated laboratories and secure amenities to ensure students learn through hands-on practice.
        </p>
      </div>

      <!-- 6 Infrastructure Cards Featuring Real Site Photos -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Science Lab (WhatsApp-Image-2023-05-13-at-15.55.02.jpeg) -->
        <div class="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm premium-card">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.55.02.jpeg" alt="Science Composite Laboratory" class="w-full h-52 object-cover">
          <div class="p-6">
            <span class="text-xs font-bold text-brand-blue uppercase">Practical Experimentation</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">Science Composite Lab</h3>
            <p class="text-slate-600 text-sm mt-2 leading-relaxed">
              Equipped with microscopes, chemical apparatus, physics models, and safety equipment conforming to CBSE guidelines.
            </p>
          </div>
        </div>

        <!-- Computer Lab (WhatsApp-Image-2023-05-13-at-15.54.56.jpeg) -->
        <div class="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm premium-card">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.54.56.jpeg" alt="Modern Computer Lab" class="w-full h-52 object-cover">
          <div class="p-6">
            <span class="text-xs font-bold text-brand-gold uppercase">Digital Literacy</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">Modern Computer Lab</h3>
            <p class="text-slate-600 text-sm mt-2 leading-relaxed">
              High-speed internet workstations, coding basics, and multimedia tools for digital learning from primary to senior classes.
            </p>
          </div>
        </div>

        <!-- Library & Reading Hall (WhatsApp-Image-2023-05-13-at-15.55.03.jpeg) -->
        <div class="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm premium-card">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.55.03.jpeg" alt="School Library & Reading Room" class="w-full h-52 object-cover">
          <div class="p-6">
            <span class="text-xs font-bold text-purple-600 uppercase">Knowledge Center</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">School Library</h3>
            <p class="text-slate-600 text-sm mt-2 leading-relaxed">
              A rich collection of curriculum books, encyclopedias, reference texts, and daily newspapers encouraging lifelong reading.
            </p>
          </div>
        </div>

        <!-- Smart Classroom (WhatsApp-Image-2023-05-13-at-15.55.00.jpeg) -->
        <div class="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm premium-card">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.55.00.jpeg" alt="Smart Classrooms" class="w-full h-52 object-cover">
          <div class="p-6">
            <span class="text-xs font-bold text-emerald-600 uppercase">Interactive Learning</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">Smart Classrooms</h3>
            <p class="text-slate-600 text-sm mt-2 leading-relaxed">
              Spacious, well-ventilated classrooms with modern digital displays, comfortable seating, and audio-visual teaching aids.
            </p>
          </div>
        </div>

        <!-- Transport Facility (1556209951_transportmainimage-768x512.jpg) -->
        <div class="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm premium-card">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/1556209951_transportmainimage-768x512.jpg" alt="School Transport Fleet" class="w-full h-52 object-cover">
          <div class="p-6">
            <span class="text-xs font-bold text-brand-blue uppercase">Safe Commute</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">School Bus Fleet</h3>
            <p class="text-slate-600 text-sm mt-2 leading-relaxed">
              GPS-monitored yellow school buses connecting Ferozepur Jhirka town and rural villages with trained drivers and attendants.
            </p>
          </div>
        </div>

        <!-- Campus Grounds & Play Area (pd10-1024x780.jpg) -->
        <div class="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm premium-card">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd10-1024x780.jpg" alt="Campus Grounds & Athletics" class="w-full h-52 object-cover">
          <div class="p-6">
            <span class="text-xs font-bold text-amber-600 uppercase">Physical Education</span>
            <h3 class="text-xl font-bold text-brand-navy mt-1">Sports & Play Area</h3>
            <p class="text-slate-600 text-sm mt-2 leading-relaxed">
              Dedicated grounds for cricket, athletics, kho-kho, yoga, and physical fitness under experienced sports instructors.
            </p>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- 9. TRANSPARENT FEE STRUCTURE & CALCULATOR -->
    <!-- ========================================== -->
    <section id="fees" class="py-20 bg-slate-100/60 border-y border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-16">
          <span class="text-xs font-bold text-brand-royal uppercase tracking-widest">Financial Transparency</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Official Fee Structure</h2>
          <div class="w-16 h-1 bg-brand-royal mx-auto mt-4 rounded-full"></div>
          <p class="text-slate-600 mt-4 text-base">
            Simple, honest pricing with zero hidden charges. Paid across 4 equal quarterly installments.
          </p>
        </div>

        <!-- Interactive Fee Calculator -->
        <div class="bg-white rounded-2xl p-6 sm:p-8 border border-slate-200 shadow-md mb-12">
          <div class="max-w-2xl mx-auto text-center mb-6">
            <span class="text-xs font-bold text-brand-gold uppercase tracking-wider">Interactive Tool</span>
            <h3 class="text-xl font-bold text-brand-navy">Instant Fee Calculator</h3>
            <p class="text-xs sm:text-sm text-slate-500 mt-1">Select your child's grade to see the exact quarterly and annual fee.</p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-center max-w-3xl mx-auto">
            <div class="md:col-span-2">
              <label class="block text-xs font-bold text-slate-700 mb-1.5">Select Class / Grade:</label>
              <select id="fee-calculator-select" onchange="calculateFee()" class="w-full px-4 py-3 rounded-xl border border-slate-300 text-sm font-semibold focus:ring-2 focus:ring-brand-blue bg-white">
                <option value="nursery">Nursery (Rs. 6,270 per quarter)</option>
                <option value="lkg">L.K.G (Rs. 6,800 per quarter)</option>
                <option value="ukg">U.K.G (Rs. 6,800 per quarter)</option>
                <option value="class1">Class 1st (Rs. 7,975 per quarter)</option>
                <option value="class2_5">Classes 2nd to 5th (Rs. 8,250 per quarter)</option>
                <option value="class6_8">Classes 6th to 8th (Rs. 8,900 per quarter)</option>
                <option value="class9_10">Classes 9th to 10th (Rs. 9,800 per quarter)</option>
                <option value="class11_12">Classes 11th to 12th (Rs. 11,500 per quarter)</option>
              </select>
            </div>
            
            <div class="bg-brand-navy text-white p-4 rounded-xl text-center">
              <div class="text-xs text-slate-300 font-medium">Total Annual Fee</div>
              <div id="calc-annual-result" class="text-2xl font-extrabold text-brand-amber mt-0.5">Rs. 25,080</div>
              <div id="calc-quarter-result" class="text-[11px] text-slate-300 mt-0.5">4 quarters of Rs. 6,270</div>
            </div>
          </div>
        </div>

        <!-- Official Fee Table (Preserved Exact Data) -->
        <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
          <div class="px-6 py-4 bg-brand-navy text-white flex flex-col sm:flex-row justify-between items-center gap-2">
            <h3 class="text-base font-bold">Standard Class-Wise Fee Schedule</h3>
            <span class="text-xs text-brand-amber font-semibold">Installments: 4 Quarters Per Academic Session</span>
          </div>
          
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm">
              <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                <tr>
                  <th class="py-3 px-4 sm:px-6">Class</th>
                  <th class="py-3 px-4">New Admission Total (Rs.)</th>
                  <th class="py-3 px-4">Old Student Total (Rs.)</th>
                  <th class="py-3 px-4">Two Children Discount</th>
                  <th class="py-3 px-4">3+ Children Discount</th>
                  <th class="py-3 px-4">Scholarship Benefit</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 text-slate-700">
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">Nursery</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 25,080 (6,270 x 4)</td>
                  <td class="py-3.5 px-4 text-slate-500">—</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">1 Month Fee (Rs. 1,590)</td>
                </tr>
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">L.K.G</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 27,200 (6,800 x 4)</td>
                  <td class="py-3.5 px-4">Rs. 24,700 (6,175 x 4)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800 (New) / Rs. 550 (Old)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000 (New) / Rs. 1,375 (Old)</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">1 Month Fee (Rs. 1,600)</td>
                </tr>
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">U.K.G</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 27,200 (6,800 x 4)</td>
                  <td class="py-3.5 px-4">Rs. 24,700 (6,175 x 4)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800 (New) / Rs. 550 (Old)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000 (New) / Rs. 1,375 (Old)</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">1 Month Fee (Rs. 1,600)</td>
                </tr>
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">1st Class</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 31,900 (7,975 x 4)</td>
                  <td class="py-3.5 px-4">Rs. 29,200 (7,300 x 4)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800 (New) / Rs. 600 (Old)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000 (New) / Rs. 1,500 (Old)</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">1 Month Fee (Rs. 1,800)</td>
                </tr>
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">2nd to 5th</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 33,000 (8,250 x 4)</td>
                  <td class="py-3.5 px-4">Rs. 30,800 (7,700 x 4)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800 (New) / Rs. 600 (Old)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000 (New) / Rs. 1,500 (Old)</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">1 Month Fee</td>
                </tr>
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">6th to 8th</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 35,600 (8,900 x 4)</td>
                  <td class="py-3.5 px-4">Rs. 33,200 (8,300 x 4)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800 (New) / Rs. 600 (Old)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000 (New) / Rs. 1,500 (Old)</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">1 Month Fee</td>
                </tr>
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">9th to 10th</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 39,200 (9,800 x 4)</td>
                  <td class="py-3.5 px-4">Rs. 36,800 (9,200 x 4)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800 (New) / Rs. 600 (Old)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000 (New) / Rs. 1,500 (Old)</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">Merit Based</td>
                </tr>
                <tr class="hover:bg-slate-50/80 transition">
                  <td class="py-3.5 px-4 sm:px-6 font-bold text-brand-navy">11th to 12th</td>
                  <td class="py-3.5 px-4 font-semibold text-brand-royal">Rs. 46,000 (11,500 x 4)</td>
                  <td class="py-3.5 px-4">Rs. 43,200 (10,800 x 4)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 800 (New) / Rs. 600 (Old)</td>
                  <td class="py-3.5 px-4 text-emerald-600 font-semibold">Rs. 2,000 (New) / Rs. 1,500 (Old)</td>
                  <td class="py-3.5 px-4 text-brand-gold font-semibold">Merit Based</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="bg-slate-50 px-6 py-4 border-t border-slate-200 text-xs text-slate-500 flex flex-col sm:flex-row justify-between items-center gap-2">
            <span>* Sibling discounts apply automatically to families enrolling multiple children.</span>
            <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/Fee-Structure-2025-26.pdf" target="_blank" rel="noopener noreferrer" class="font-bold text-brand-blue hover:underline flex items-center gap-1">
              Download Official Fee PDF &rarr;
            </a>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- 10. ADMISSION PROCEDURE                   -->
    <!-- ========================================== -->
    <section id="admissions" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold text-brand-gold uppercase tracking-widest">Enrollment Made Simple</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Admission Procedure</h2>
        <div class="w-16 h-1 bg-brand-amber mx-auto mt-4 rounded-full"></div>
        <p class="text-slate-600 mt-4 text-base">
          Four straightforward steps to secure your child's admission at P.D. Public School.
        </p>
      </div>

      <!-- 4-Step Process -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm relative">
          <div class="w-9 h-9 rounded-full bg-brand-navy text-brand-amber font-bold flex items-center justify-center text-sm mb-4">
            1
          </div>
          <h3 class="text-lg font-bold text-brand-navy">Submit Inquiry</h3>
          <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
            Fill the online admission form or visit the school reception desk in Ferozepur Jhirka.
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm relative">
          <div class="w-9 h-9 rounded-full bg-brand-navy text-brand-amber font-bold flex items-center justify-center text-sm mb-4">
            2
          </div>
          <h3 class="text-lg font-bold text-brand-navy">Campus Tour & Test</h3>
          <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
            Visit with the student for an interactive tour and a friendly diagnostic assessment to gauge learning level.
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm relative">
          <div class="w-9 h-9 rounded-full bg-brand-navy text-brand-amber font-bold flex items-center justify-center text-sm mb-4">
            3
          </div>
          <h3 class="text-lg font-bold text-brand-navy">Document Check</h3>
          <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
            Submit required verification certificates (Birth Certificate, Transfer Certificate, Photos).
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm relative">
          <div class="w-9 h-9 rounded-full bg-brand-navy text-brand-amber font-bold flex items-center justify-center text-sm mb-4">
            4
          </div>
          <h3 class="text-lg font-bold text-brand-navy">Seat Confirmation</h3>
          <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
            Complete formal registration, collect syllabus and books, and welcome your child to the school family.
          </p>
        </div>
      </div>

      <!-- Required Documents Box -->
      <div class="bg-brand-navy text-white rounded-2xl p-8 sm:p-10 shadow-xl border border-white/10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-7 space-y-4">
            <span class="text-xs font-bold text-brand-amber uppercase tracking-wider">Checklist for Parents</span>
            <h3 class="text-2xl font-bold">Documents Required for Admission</h3>
            <p class="text-slate-300 text-sm">Please carry original and photocopies during your campus visit:</p>
            <ul class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-slate-200 pt-2">
              <li class="flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                Birth Certificate (Attested copy)
              </li>
              <li class="flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                Transfer Certificate (Original TC)
              </li>
              <li class="flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                Previous Class Report Card
              </li>
              <li class="flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                Student & Parent Passport Photos (4 each)
              </li>
              <li class="flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                Aadhaar Card Copy (Child & Parents)
              </li>
              <li class="flex items-center gap-2">
                <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                Caste / Category Certificate (if applicable)
              </li>
            </ul>
          </div>

          <div class="lg:col-span-5 bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20 text-center">
            <h4 class="text-lg font-bold text-brand-amber">Need Admission Help?</h4>
            <p class="text-xs text-slate-200 mt-1 mb-4">Our admission officers are available to assist you Monday through Saturday.</p>
            <div class="flex flex-col gap-2.5">
              <button onclick="openInquiryModal()" class="w-full py-3 rounded-lg font-bold text-sm text-brand-dark bg-brand-amber hover:bg-amber-400 transition">
                Start Online Application
              </button>
              <a href="tel:+918607288800" class="w-full py-2.5 rounded-lg font-semibold text-xs text-white bg-white/10 hover:bg-white/20 transition">
                Call Helpline: +91 8607288800
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- 11. COMPREHENSIVE CAMPUS PHOTO GALLERY    -->
    <!-- ========================================== -->
    <section id="gallery" class="py-20 bg-slate-100/60 border-y border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-10">
          <span class="text-xs font-bold text-brand-royal uppercase tracking-widest">Campus Vibrancy</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Life at P.D. Public School</h2>
          <div class="w-16 h-1 bg-brand-royal mx-auto mt-4 rounded-full"></div>
          <p class="text-slate-600 mt-4 text-base">
            Explore authentic moments captured across our annual functions, sports meets, science fairs, and daily learning.
          </p>
        </div>

        <!-- Category Filter Buttons -->
        <div class="flex flex-wrap items-center justify-center gap-2 mb-10">
          <button onclick="filterGallery('all')" class="filter-btn active px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold border border-slate-300 bg-white text-slate-700 hover:bg-slate-50 transition">
            All Photos
          </button>
          <button onclick="filterGallery('cultural')" class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold border border-slate-300 bg-white text-slate-700 hover:bg-slate-50 transition">
            Annual Day & Cultural
          </button>
          <button onclick="filterGallery('sports')" class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold border border-slate-300 bg-white text-slate-700 hover:bg-slate-50 transition">
            Sports & Athletics
          </button>
          <button onclick="filterGallery('academic')" class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold border border-slate-300 bg-white text-slate-700 hover:bg-slate-50 transition">
            Competitions & Science
          </button>
          <button onclick="filterGallery('festivals')" class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold border border-slate-300 bg-white text-slate-700 hover:bg-slate-50 transition">
            National Days & Assemblies
          </button>
        </div>

        <!-- 18 Real Photos Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6" id="gallery-grid">
          
          <!-- Item 1: Cultural Dance -->
          <div class="gallery-item cultural bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0035-1024x768.jpg', 'Annual Day Cultural Dance Showcase')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0035-1024x768.jpg" alt="Annual Day Cultural Dance" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-gold uppercase">Annual Day</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Cultural Dance Showcase</h4>
            </div>
          </div>

          <!-- Item 2: Award Ceremony -->
          <div class="gallery-item cultural bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0039.jpg', 'Merit & Prize Distribution Ceremony')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0039.jpg" alt="Annual Prize Distribution" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-blue uppercase">Honors</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Prize & Award Ceremony</h4>
            </div>
          </div>

          <!-- Item 3: Stage Drama -->
          <div class="gallery-item cultural bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0040.jpg', 'Dramatic Arts & Play Performance')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0040.jpg" alt="Drama & Stage Play" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-purple-600 uppercase">Performing Arts</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Dramatic Arts & Play</h4>
            </div>
          </div>

          <!-- Item 4: Student Traditional Dress -->
          <div class="gallery-item cultural bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0044.jpg', 'Traditional Performance Costumes')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20191225-WA0044.jpg" alt="Student Traditional Costumes" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-pink-600 uppercase">Tradition</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Traditional Performers</h4>
            </div>
          </div>

          <!-- Item 5: Sports Meet 1 -->
          <div class="gallery-item sports bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9781-1-768x512.jpg', 'Annual Athletics & Track Events')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9781-1-768x512.jpg" alt="Athletics Meet" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-emerald-600 uppercase">Sports Meet</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Athletics & Track Events</h4>
            </div>
          </div>

          <!-- Item 6: Sports Meet 2 -->
          <div class="gallery-item sports bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9784-300x200.jpg', 'Inter-House Sports Tournament')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9784-300x200.jpg" alt="Inter-House Sports Tournament" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-emerald-600 uppercase">Athletics</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Inter-House Championship</h4>
            </div>
          </div>

          <!-- Item 7: Sports Meet 3 -->
          <div class="gallery-item sports bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9787-768x512.jpg', 'Sprint & Relay Races')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9787-768x512.jpg" alt="Track Sprint and Races" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-emerald-600 uppercase">Track Field</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Sprint & Relay Races</h4>
            </div>
          </div>

          <!-- Item 8: Cooking Without Fire Competition -->
          <div class="gallery-item academic bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/cooking-without-fire.jpg', 'Intra-School Cooking Without Fire Competition')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/cooking-without-fire.jpg" alt="Cooking Without Fire Competition" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-gold uppercase">Culinary Skills</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Cooking Without Fire</h4>
            </div>
          </div>

          <!-- Item 9: Dr. B.R. Ambedkar Jayanti -->
          <div class="gallery-item festivals bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220414-WA0002-1536x1156.jpg', 'Dr. B.R. Ambedkar Jayanti Celebration')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220414-WA0002-1536x1156.jpg" alt="Dr B R Ambedkar Jayanti Celebration" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-blue uppercase">Special Assembly</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Dr. Ambedkar Jayanti</h4>
            </div>
          </div>

          <!-- Item 10: Swami Vivekananda Youth Day -->
          <div class="gallery-item festivals bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220112-WA0018-768x576.jpg', 'National Youth Day - Swami Vivekananda Assembly')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220112-WA0018-768x576.jpg" alt="National Youth Day Assembly" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-amber uppercase">National Youth Day</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Youth Inspiration Event</h4>
            </div>
          </div>

          <!-- Item 11: Janmashtami Celebration -->
          <div class="gallery-item festivals bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220820-WA0019-768x346.jpg', 'Shri Krishna Janmashtami Celebration')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220820-WA0019-768x346.jpg" alt="Janmashtami Celebration" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-purple-600 uppercase">Cultural Festival</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Janmashtami Celebrations</h4>
            </div>
          </div>

          <!-- Item 12: Haryana Day Celebration 1 -->
          <div class="gallery-item festivals bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20221101-WA0032-1-766x1024.jpg', 'Haryana Day Rangoli & Cultural Display')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20221101-WA0032-1-766x1024.jpg" alt="Haryana Day Rangoli" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-emerald-600 uppercase">Haryana Day</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">State Pride & Rangoli</h4>
            </div>
          </div>

          <!-- Item 13: Haryana Day Celebration 2 -->
          <div class="gallery-item festivals bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20221101-WA0034-766x1024.jpg', 'Traditional Art & Folk Celebrations')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20221101-WA0034-766x1024.jpg" alt="Folk Celebrations" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-gold uppercase">Heritage</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Folk Art Activities</h4>
            </div>
          </div>

          <!-- Item 14: Graduation / Convocation -->
          <div class="gallery-item academic bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2019-03-25-at-09.40.29-1-1024x768.jpeg', 'Convocation & Farewell Ceremony')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2019-03-25-at-09.40.29-1-1024x768.jpeg" alt="Convocation Ceremony" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-navy uppercase">Milestones</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Convocation & Farewell</h4>
            </div>
          </div>

          <!-- Item 15: Morning Prayer & Assembly -->
          <div class="gallery-item festivals bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220214-WA0057-768x512.jpg', 'Morning Prayer & Values Assembly')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220214-WA0057-768x512.jpg" alt="Morning Prayer and Values Assembly" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-blue-600 uppercase">Values</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Morning Assembly</h4>
            </div>
          </div>

          <!-- Item 16: Science Fair STEM Models -->
          <div class="gallery-item academic bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm gallery-img-container" onclick="openLightbox('https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.54.58-1-1024x682.jpeg', 'Science Fair & Robotics Exhibition')">
            <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.54.58-1-1024x682.jpeg" alt="Science Exhibition" class="w-full h-48 object-cover">
            <div class="p-3 bg-white">
              <span class="text-[11px] font-bold text-brand-amber uppercase">STEM Project</span>
              <h4 class="text-xs font-bold text-brand-navy truncate">Science Exhibition</h4>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- 12. MANAGING COMMITTEE (100% REAL DATA)   -->
    <!-- ========================================== -->
    <section id="committee" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold text-brand-royal uppercase tracking-widest">School Governance</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Managing Committee</h2>
        <div class="w-16 h-1 bg-brand-royal mx-auto mt-4 rounded-full"></div>
        <p class="text-slate-600 mt-4 text-base">
          Guided by experienced educationists, parents, and community leaders of Ferozepur Jhirka.
        </p>
      </div>

      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden max-w-4xl mx-auto">
        <div class="px-6 py-4 bg-brand-navy text-white flex justify-between items-center">
          <h3 class="text-base font-bold">Official School Management Board</h3>
          <span class="text-xs text-slate-300">Registered Educational Society</span>
        </div>
        
        <div class="overflow-x-auto">
          <table class="w-full text-left text-sm">
            <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
              <tr>
                <th class="py-3 px-6 w-16">Sr.</th>
                <th class="py-3 px-6">Member Name</th>
                <th class="py-3 px-6">Designation</th>
                <th class="py-3 px-6">Role on Committee</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-slate-700">
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">1</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Anil Goyal</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-blue-50 text-brand-royal font-semibold text-xs">President</span></td>
                <td class="py-3.5 px-6 text-slate-500">Executive Head</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">2</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Sanjay Goyal</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-blue-50 text-brand-royal font-semibold text-xs">Vice President</span></td>
                <td class="py-3.5 px-6 text-slate-500">Governance & Operations</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">3</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Manoj Tayal</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-slate-100 text-slate-800 font-semibold text-xs">Cashier</span></td>
                <td class="py-3.5 px-6 text-slate-500">Finance & Auditing</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">4</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Yashpal Garg</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-purple-50 text-purple-700 font-semibold text-xs">Educationist</span></td>
                <td class="py-3.5 px-6 text-slate-500">Academic Standards</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">5</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Mrs. Jyoti Sharma</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-amber-50 text-brand-gold font-semibold text-xs">Headmistress / Ex-Officio</span></td>
                <td class="py-3.5 px-6 text-slate-500">Academic Leadership</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">6</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Mrs. Renu Rani</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-slate-100 text-slate-800 font-semibold text-xs">Female Member</span></td>
                <td class="py-3.5 px-6 text-slate-500">Student Welfare</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">7</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Sanjay Goyal</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-emerald-50 text-emerald-700 font-semibold text-xs">Parents Representative</span></td>
                <td class="py-3.5 px-6 text-slate-500">Parent Advisory</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">8</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Mrs. Jyoti</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-emerald-50 text-emerald-700 font-semibold text-xs">Teacher Representative</span></td>
                <td class="py-3.5 px-6 text-slate-500">Faculty Liaison</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">9</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Chagan Sharma</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-slate-100 text-slate-800 font-semibold text-xs">Member</span></td>
                <td class="py-3.5 px-6 text-slate-500">Community Outreach</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">10</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Neeraj Mehta</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-slate-100 text-slate-800 font-semibold text-xs">Member</span></td>
                <td class="py-3.5 px-6 text-slate-500">Infrastructure Support</td>
              </tr>
              <tr class="hover:bg-slate-50/80">
                <td class="py-3.5 px-6 font-bold text-slate-400">11</td>
                <td class="py-3.5 px-6 font-bold text-brand-navy">Sh. Tarkeshwar</td>
                <td class="py-3.5 px-6"><span class="px-2.5 py-1 rounded bg-slate-100 text-slate-800 font-semibold text-xs">Member</span></td>
                <td class="py-3.5 px-6 text-slate-500">Social Affairs</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- 13. CBSE MANDATORY PUBLIC DISCLOSURES     -->
    <!-- ========================================== -->
    <section id="disclosures" class="py-20 bg-slate-100/60 border-y border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-16">
          <span class="text-xs font-bold text-brand-gold uppercase tracking-widest">Compliance & Accreditation</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Mandatory Public Disclosures</h2>
          <div class="w-16 h-1 bg-brand-amber mx-auto mt-4 rounded-full"></div>
          <p class="text-slate-600 mt-4 text-base">
            Official statutory documentation in compliance with the Central Board of Secondary Education (CBSE), New Delhi.
          </p>
        </div>

        <div class="bg-white rounded-2xl border border-slate-200 shadow-md overflow-hidden">
          <div class="p-6 bg-brand-navy text-white flex flex-col sm:flex-row justify-between items-center gap-3">
            <div>
              <h3 class="text-lg font-bold">General Information & Statutory Certificates</h3>
              <p class="text-xs text-slate-300 mt-0.5">Click any document to inspect or download the verified government certificate.</p>
            </div>
            <span class="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-400/30">
              Verified Valid
            </span>
          </div>

          <div class="divide-y divide-slate-100">
            
            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">1. CBSE Affiliation & Extension Letter</div>
                <div class="text-xs text-slate-500">Official CBSE Secondary & Senior Secondary Affiliation Grant</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/pd-public-school-EXTENSITION-LETTER.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View Document (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">2. Society Registration Certificate</div>
                <div class="text-xs text-slate-500">Registered under Societies Registration Act</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2024/05/Society-Registration.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View Document (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">3. No Objection Certificate (NOC)</div>
                <div class="text-xs text-slate-500">Issued by Education Department, Government of Haryana</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/NOC.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View Document (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">4. Recognition Certificate under RTE Act</div>
                <div class="text-xs text-slate-500">State Government Directorate of School Education</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/reconigation-certificate.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View Document (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">5. Building Safety Certificate</div>
                <div class="text-xs text-slate-500">Certified by Public Works Department (PWD/B&R)</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/Building-Safety-Certificate.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View Document (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">6. Fire Safety Certificate</div>
                <div class="text-xs text-slate-500">Approved by District Fire Service Authority</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/Fire-Certificate.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View Document (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">7. Water, Health & Sanitary Hygiene Certificate</div>
                <div class="text-xs text-slate-500">Certified by Public Health & Sanitation Authority</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/hygine-certificate.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View Document (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">8. Official Academic Calendar (Session 2025-26)</div>
                <div class="text-xs text-slate-500">Term dates, exam schedules & list of gazetted holidays</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/CALENDER-2025-26.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-emerald-700 bg-emerald-50 hover:bg-emerald-100 transition border border-emerald-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                Download Calendar (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">9. Last Three Years CBSE Board Results</div>
                <div class="text-xs text-slate-500">Session-wise pass percentages for Class 10th & 12th</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/Last-Tree-Years-Board-result-Session-Wise_page-0001.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                View Board Results (PDF)
              </a>
            </div>

            <div class="p-4 sm:p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 hover:bg-slate-50 transition">
              <div>
                <div class="text-sm font-bold text-brand-navy">10. Parent-Teacher Association (PTA) Member List</div>
                <div class="text-xs text-slate-500">Official list of elected parent & teacher representatives</div>
              </div>
              <a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/PTA-MEMBER-LIST.pdf" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg text-xs font-bold text-brand-royal bg-blue-50 hover:bg-blue-100 transition border border-blue-200 flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                View PTA List (PDF)
              </a>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- 14. CONTACT & LOCATION                    -->
    <!-- ========================================== -->
    <section id="contact" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold text-brand-gold uppercase tracking-widest">Connect With Us</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy mt-2">Get In Touch</h2>
        <div class="w-16 h-1 bg-brand-amber mx-auto mt-4 rounded-full"></div>
        <p class="text-slate-600 mt-4 text-base">
          Our school office is located conveniently in Ferozepur Jhirka. We welcome your visit!
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Contact Information Cards -->
        <div class="lg:col-span-5 space-y-4">
          
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-xl bg-blue-50 text-brand-blue flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              </div>
              <div>
                <h4 class="text-base font-bold text-brand-navy">Campus Address</h4>
                <p class="text-slate-600 text-sm mt-1 leading-relaxed">
                  Opp. Gaushala, Jhir Mandir Road,<br>
                  Ferozepur Jhirka (Mewat), Haryana - 122104
                </p>
                <a href="https://maps.app.goo.gl/HwFUrS4Dtf6Gku9b6" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-xs font-bold text-brand-blue mt-2 hover:underline">
                  Get Google Maps Directions &rarr;
                </a>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              </div>
              <div>
                <h4 class="text-base font-bold text-brand-navy">Phone Numbers</h4>
                <p class="text-slate-600 text-sm mt-1">
                  Main Line: <a href="tel:+918607288800" class="font-bold text-brand-royal hover:underline">+91 8607288800</a><br>
                  Alternate: <a href="tel:+918607366600" class="font-bold text-brand-royal hover:underline">+91 8607366600</a>
                </p>
                <div class="text-xs text-slate-500 mt-1">Available Mon - Sat: 8:00 AM to 2:30 PM</div>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-xl bg-amber-50 text-brand-gold flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
              </div>
              <div>
                <h4 class="text-base font-bold text-brand-navy">Email Inquiries</h4>
                <p class="text-slate-600 text-sm mt-1">
                  <a href="mailto:pdpublicschl@gmail.com" class="font-semibold text-brand-royal hover:underline">pdpublicschl@gmail.com</a>
                </p>
                <div class="text-xs text-slate-500 mt-1">Official communications & administrative queries.</div>
              </div>
            </div>
          </div>

        </div>

        <!-- Direct Message Form -->
        <div class="lg:col-span-7 bg-white p-8 rounded-2xl border border-slate-200 shadow-sm">
          <h3 class="text-xl font-bold text-brand-navy">Send an Instant Message</h3>
          <p class="text-xs sm:text-sm text-slate-500 mt-1 mb-6">Have questions regarding transport routes, booklists, or transfer certificates?</p>

          <form id="contact-form" onsubmit="handleInquirySubmit(event, 'Contact Section')" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-slate-700 mb-1">Your Full Name *</label>
                <input type="text" required placeholder="Full Name" class="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none">
              </div>
              <div>
                <label class="block text-xs font-semibold text-slate-700 mb-1">Mobile Number *</label>
                <input type="tel" pattern="[0-9]{10}" required placeholder="10-digit Phone" class="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none">
              </div>
            </div>

            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Email Address</label>
              <input type="email" placeholder="name@example.com (optional)" class="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none">
            </div>

            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Your Message or Inquiry *</label>
              <textarea rows="4" required placeholder="Type your inquiry here..." class="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none"></textarea>
            </div>

            <button type="submit" class="w-full sm:w-auto px-8 py-3 rounded-xl font-bold text-sm text-white bg-brand-royal hover:bg-brand-navy transition shadow">
              Submit Message
            </button>
          </form>
          <div id="contact-form-status" class="hidden mt-4 p-3.5 rounded-lg text-xs font-medium text-emerald-800 bg-emerald-50 border border-emerald-200"></div>
        </div>

      </div>
    </section>

  </main>

  <!-- ========================================== -->
  <!-- 15. FOOTER                                -->
  <!-- ========================================== -->
  <footer class="bg-brand-navy text-slate-300 pt-16 pb-28 sm:pb-16 border-t border-white/10 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
      
      <!-- Brand & Mission -->
      <div class="space-y-4">
        <div class="flex items-center gap-3">
          <img src="https://pdpublicschool.co.in/wp-content/uploads/2024/04/pdlogo.jpeg" alt="PD Public School" class="w-10 h-10 object-contain rounded-full bg-white p-0.5">
          <span class="font-extrabold text-white text-base">P.D. PUBLIC SCHOOL</span>
        </div>
        <p class="text-xs text-slate-400 leading-relaxed">
          P.D. Public Senior Secondary School is dedicated to fostering academic rigor, moral integrity, and social responsibility under the CBSE New Delhi framework.
        </p>
        <div class="flex items-center gap-3 pt-2">
          <a href="https://www.facebook.com/P-D-Public-School-Ferozpur-Jhirka-100064008883593/" target="_blank" rel="noopener noreferrer" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition" aria-label="Facebook">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          </a>
          <a href="https://www.instagram.com/pd.public.school" target="_blank" rel="noopener noreferrer" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition" aria-label="Instagram">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </a>
          <a href="https://wa.me/918607288800" target="_blank" rel="noopener noreferrer" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition" aria-label="WhatsApp">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.634.074-1.637-.323-.972-.387-1.579-1.378-1.63-1.442-.045-.064-.396-.527-.396-1.004 0-.477.25-.712.339-.81.089-.098.192-.122.257-.122.064 0 .128.001.185.006.059.006.138-.022.215.163.08.188.272.663.296.711.024.048.04.106.008.17-.032.064-.048.106-.096.162-.048.056-.101.125-.145.168-.048.048-.098.1-.042.196.056.096.249.41.534.664.368.327.679.429.775.477.096.048.152.04.208-.024.056-.064.24-.28.304-.376.064-.096.128-.08.216-.048.088.032.56.264.656.312.096.048.16.072.184.112.024.04.024.233-.12.638z"/></svg>
          </a>
        </div>
      </div>

      <!-- Quick Links -->
      <div>
        <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-4">Quick Navigation</h4>
        <ul class="space-y-2 text-xs">
          <li><a href="#about" class="hover:text-white transition">About School</a></li>
          <li><a href="#academics" class="hover:text-white transition">Academics & Wings</a></li>
          <li><a href="#admissions" class="hover:text-white transition">Admission Procedure</a></li>
          <li><a href="#fees" class="hover:text-white transition">Fee Structure</a></li>
          <li><a href="#gallery" class="hover:text-white transition">Photo Gallery</a></li>
          <li><a href="#committee" class="hover:text-white transition">Managing Committee</a></li>
          <li><a href="#disclosures" class="hover:text-white transition">Mandatory CBSE Disclosures</a></li>
        </ul>
      </div>

      <!-- CBSE Compliance -->
      <div>
        <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-4">CBSE Downloads</h4>
        <ul class="space-y-2 text-xs">
          <li><a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/pd-public-school-EXTENSITION-LETTER.pdf" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">CBSE Affiliation Grant</a></li>
          <li><a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/CALENDER-2025-26.pdf" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">Academic Calendar 2025-26</a></li>
          <li><a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/Fee-Structure-2025-26.pdf" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">Official Fee Order</a></li>
          <li><a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/Building-Safety-Certificate.pdf" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">Building Safety Certificate</a></li>
          <li><a href="https://pdpublicschool.co.in/wp-content/uploads/2025/09/Fire-Certificate.pdf" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">Fire Safety Certificate</a></li>
        </ul>
      </div>

      <!-- Campus Location -->
      <div>
        <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-4">Campus Location</h4>
        <p class="text-xs text-slate-400 leading-relaxed">
          Opp. Gaushala, Jhir Mandir Road,<br>
          Ferozepur Jhirka (Mewat), Haryana - 122104
        </p>
        <p class="text-xs text-slate-400 mt-3">
          Phone: <a href="tel:+918607288800" class="text-brand-amber font-semibold">+91 8607288800</a><br>
          Email: <a href="mailto:pdpublicschl@gmail.com" class="text-slate-300">pdpublicschl@gmail.com</a>
        </p>
      </div>

    </div>

    <!-- Copyright Bar -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12 pt-6 border-t border-white/10 flex flex-col sm:flex-row justify-between items-center gap-3 text-xs text-slate-400 text-center sm:text-left">
      <div>
        &copy; 2025-2026 P.D. Public Senior Secondary School. All Rights Reserved.
      </div>
      <div>
        Affiliated to Central Board of Secondary Education (CBSE), New Delhi.
      </div>
    </div>
  </footer>

  <!-- ========================================== -->
  <!-- 16. MOBILE STICKY BOTTOM ACTION BAR       -->
  <!-- ========================================== -->
  <div class="fixed bottom-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-t border-slate-200 px-3 py-2 sm:hidden flex items-center justify-around shadow-lg">
    <a href="tel:+918607288800" class="flex flex-col items-center justify-center flex-1 py-1 text-slate-700 hover:text-brand-royal transition touch-target">
      <svg class="w-5 h-5 text-brand-royal" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
      <span class="text-[10px] font-bold mt-0.5">Call School</span>
    </a>
    <a href="https://wa.me/918607288800?text=Hello%20PD%20Public%20School,%20I%20want%20to%20inquire%20about%20admissions." target="_blank" rel="noopener noreferrer" class="flex flex-col items-center justify-center flex-1 py-1 text-emerald-700 hover:text-emerald-800 transition touch-target">
      <svg class="w-5 h-5 fill-emerald-600" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.634.074-1.637-.323-.972-.387-1.579-1.378-1.63-1.442-.045-.064-.396-.527-.396-1.004 0-.477.25-.712.339-.81.089-.098.192-.122.257-.122.064 0 .128.001.185.006.059.006.138-.022.215.163.08.188.272.663.296.711.024.048.04.106.008.17-.032.064-.048.106-.096.162-.048.056-.101.125-.145.168-.048.048-.098.1-.042.196.056.096.249.41.534.664.368.327.679.429.775.477.096.048.152.04.208-.024.056-.064.24-.28.304-.376.064-.096.128-.08.216-.048.088.032.56.264.656.312.096.048.16.072.184.112.024.04.024.233-.12.638z"/></svg>
      <span class="text-[10px] font-bold mt-0.5">WhatsApp</span>
    </a>
    <button onclick="openInquiryModal()" class="flex flex-col items-center justify-center flex-1 py-1 text-white bg-brand-royal rounded-lg my-0.5 mx-1 shadow touch-target">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
      <span class="text-[10px] font-bold mt-0.5">Apply Now</span>
    </button>
  </div>

  <!-- ========================================== -->
  <!-- 17. FULL-SCREEN IMAGE LIGHTBOX MODAL       -->
  <!-- ========================================== -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 hidden bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
    <div class="relative max-w-4xl w-full text-center">
      <button onclick="closeLightbox()" class="absolute -top-12 right-0 text-white hover:text-amber-400 p-2 touch-target" aria-label="Close Lightbox">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>
      <img id="lightbox-img" src="" alt="Full view" class="max-h-[80vh] max-w-full mx-auto rounded-xl shadow-2xl object-contain">
      <p id="lightbox-caption" class="text-white text-sm sm:text-base font-semibold mt-4 text-center"></p>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 18. POPUP ADMISSION INQUIRY MODAL         -->
  <!-- ========================================== -->
  <div id="inquiry-modal" class="fixed inset-0 z-50 hidden bg-brand-navy/60 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative border border-slate-200 overflow-y-auto max-h-[90vh]">
      
      <!-- Close Button -->
      <button onclick="closeInquiryModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-700 p-2 touch-target" aria-label="Close Modal">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <div class="mb-5">
        <span class="text-xs font-bold text-brand-gold uppercase tracking-wider">Fast-Track Registration</span>
        <h3 class="text-2xl font-bold text-brand-navy mt-1">Admission Inquiry (2025-26)</h3>
        <p class="text-xs text-slate-500 mt-1">Please enter your details below. The school office will contact you within 24 hours.</p>
      </div>

      <form id="modal-inquiry-form" onsubmit="handleInquirySubmit(event, 'Modal Popup')" class="space-y-4">
        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">Parent / Guardian Name *</label>
          <input type="text" id="m-parent" required placeholder="e.g. Ramesh Kumar" class="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none">
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">Mobile Number *</label>
            <input type="tel" id="m-phone" pattern="[0-9]{10}" required placeholder="10-digit Phone" class="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">Class Seeking *</label>
            <select id="m-class" required class="w-full px-3 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none bg-white">
              <option value="">Select Grade</option>
              <option value="Nursery">Nursery / Pre-KG</option>
              <option value="LKG/UKG">LKG / UKG</option>
              <option value="Primary (1-5)">Classes 1 to 5</option>
              <option value="Middle (6-8)">Classes 6 to 8</option>
              <option value="Secondary (9-10)">Classes 9 to 10</option>
              <option value="Class 11-12 Science">Class 11-12 (Science)</option>
              <option value="Class 11-12 Commerce">Class 11-12 (Commerce)</option>
              <option value="Class 11-12 Arts">Class 11-12 (Arts)</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">Village / Town / Location</label>
          <input type="text" id="m-location" placeholder="e.g. Ferozepur Jhirka or nearby village" class="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-brand-blue focus:outline-none">
        </div>

        <div class="flex items-center gap-2 pt-1">
          <input type="checkbox" id="m-whatsapp" checked class="rounded border-slate-300 text-brand-blue focus:ring-brand-blue">
          <label for="m-whatsapp" class="text-xs text-slate-600">Send me fee details and brochure on WhatsApp</label>
        </div>

        <button type="submit" class="w-full py-3.5 rounded-xl font-bold text-sm text-white bg-brand-royal hover:bg-brand-navy shadow-md transition mt-2">
          Submit & Connect on WhatsApp
        </button>
      </form>

      <div id="modal-form-status" class="hidden mt-4 p-3 rounded-lg text-xs font-medium text-emerald-800 bg-emerald-50 border border-emerald-200 text-center"></div>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- 19. LIGHTWEIGHT CLIENT JAVASCRIPT         -->
  <!-- ========================================== -->
  <script>
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
    });

    // Modal Controls
    function openInquiryModal() {
      document.getElementById('inquiry-modal').classList.remove('hidden');
    }

    function closeInquiryModal() {
      document.getElementById('inquiry-modal').classList.add('hidden');
    }

    // Lightbox Controls
    function openLightbox(src, caption) {
      const modal = document.getElementById('lightbox-modal');
      const img = document.getElementById('lightbox-img');
      const cap = document.getElementById('lightbox-caption');
      img.src = src;
      cap.innerText = caption;
      modal.classList.remove('hidden');
    }

    function closeLightbox() {
      document.getElementById('lightbox-modal').classList.add('hidden');
    }

    document.getElementById('lightbox-modal').addEventListener('click', (e) => {
      if (e.target.id === 'lightbox-modal') closeLightbox();
    });

    // Close on escape key
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeInquiryModal();
        closeLightbox();
      }
    });

    // Gallery Category Filtering
    function filterGallery(category) {
      document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');

      const items = document.querySelectorAll('.gallery-item');
      items.forEach(item => {
        if (category === 'all' || item.classList.contains(category)) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    }

    // Fee Calculator Logic
    const feeData = {
      'nursery': { annual: 25080, quarter: 6270 },
      'lkg': { annual: 27200, quarter: 6800 },
      'ukg': { annual: 27200, quarter: 6800 },
      'class1': { annual: 31900, quarter: 7975 },
      'class2_5': { annual: 33000, quarter: 8250 },
      'class6_8': { annual: 35600, quarter: 8900 },
      'class9_10': { annual: 39200, quarter: 9800 },
      'class11_12': { annual: 46000, quarter: 11500 }
    };

    function calculateFee() {
      const selected = document.getElementById('fee-calculator-select').value;
      const data = feeData[selected] || feeData['nursery'];
      document.getElementById('calc-annual-result').innerText = 'Rs. ' + data.annual.toLocaleString('en-IN');
      document.getElementById('calc-quarter-result').innerText = '4 quarters of Rs. ' + data.quarter.toLocaleString('en-IN');
    }

    // Form Submissions
    function handleInquirySubmit(event, source) {
      event.preventDefault();
      
      let statusDiv;
      if (source === 'Modal Popup') {
        statusDiv = document.getElementById('modal-form-status');
      } else {
        statusDiv = document.getElementById('contact-form-status');
      }

      statusDiv.classList.remove('hidden');
      statusDiv.innerHTML = `<strong>Thank you!</strong> Your inquiry has been received. Our counselor will call you shortly. You may also message us directly at <strong>+91 8607288800</strong>.`;

      const parentName = document.getElementById('m-parent')?.value || 'Parent';
      const grade = document.getElementById('m-class')?.value || 'General';
      const msg = encodeURIComponent(`Hello PD Public School, I am ${parentName}. I would like to inquire about admission in ${grade}.`);
      
      setTimeout(() => {
        if (source === 'Modal Popup') {
          window.open(`https://wa.me/918607288800?text=${msg}`, '_blank');
        }
      }, 800);
    }
  </script>

</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(enhanced_html)

print("Updated index.html written successfully!")

