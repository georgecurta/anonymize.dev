/**
 * Anonymize.dev - Main JavaScript
 * Neon Protocol Theme - Developer-First Functionality
 */

document.addEventListener('DOMContentLoaded', function() {
  // =============================================
  // MOBILE NAVIGATION
  // =============================================

  const navToggle = document.querySelector('.nav__toggle');
  const navMobile = document.querySelector('.nav__mobile');

  if (navToggle && navMobile) {
    navToggle.addEventListener('click', function() {
      navMobile.classList.toggle('is-open');
      const isOpen = navMobile.classList.contains('is-open');
      navToggle.setAttribute('aria-expanded', isOpen);

      // Animate hamburger to X
      const spans = navToggle.querySelectorAll('span');
      if (isOpen) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });

    // Close on link click
    navMobile.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navMobile.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // =============================================
  // NAVIGATION SCROLL EFFECT
  // =============================================

  const nav = document.querySelector('.nav');
  if (nav) {
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;

      if (currentScroll > 50) {
        nav.classList.add('nav--scrolled');
      } else {
        nav.classList.remove('nav--scrolled');
      }

      lastScroll = currentScroll;
    }, { passive: true });
  }

  // =============================================
  // ACTIVE NAV LINK
  // =============================================

  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('nav__link--active');
    }
  });

  // =============================================
  // SMOOTH SCROLL
  // =============================================

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // =============================================
  // SCROLL-TRIGGERED ANIMATIONS
  // =============================================

  const scrollRevealElements = document.querySelectorAll(
    '.scroll-reveal, .scroll-reveal-left, .scroll-reveal-right, .scroll-reveal-scale, .stagger-children'
  );

  if (scrollRevealElements.length > 0 && 'IntersectionObserver' in window) {
    const scrollObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          scrollObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    scrollRevealElements.forEach(el => scrollObserver.observe(el));
  } else {
    // Fallback
    scrollRevealElements.forEach(el => el.classList.add('visible'));
  }

  // =============================================
  // CODE COPY FUNCTIONALITY
  // =============================================

  document.querySelectorAll('.code-block__copy').forEach(btn => {
    btn.addEventListener('click', async function() {
      const codeBlock = this.closest('.code-block');
      const code = codeBlock.querySelector('code');

      if (code) {
        try {
          await navigator.clipboard.writeText(code.textContent);
          this.classList.add('copied');
          this.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Copied!';

          setTimeout(() => {
            this.classList.remove('copied');
            this.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg> Copy';
          }, 2000);
        } catch (err) {
          console.error('Failed to copy:', err);
        }
      }
    });
  });

  // =============================================
  // CONTACT FORM HANDLING
  // =============================================

  const RECAPTCHA_SITE_KEY = '6LcFEFosAAAAAH6zUMF5USUNKGGjr07y97nC5uDr';
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  if (contactForm) {
    contactForm.addEventListener('submit', async function(e) {
      e.preventDefault();

      const submitButton = this.querySelector('button[type="submit"]');
      const originalText = submitButton.innerHTML;

      // Loading state
      submitButton.innerHTML = '<span class="loading-ring" style="width:20px;height:20px;border-width:2px;margin-right:8px;"></span> Sending...';
      submitButton.disabled = true;

      try {
        // Get reCAPTCHA token
        let recaptchaToken = '';
        if (typeof grecaptcha !== 'undefined') {
          try {
            recaptchaToken = await grecaptcha.execute(RECAPTCHA_SITE_KEY, { action: 'contact_form' });
          } catch (recaptchaError) {
            console.error('reCAPTCHA error:', recaptchaError);
          }
        }

        // Collect form data
        const formData = {
          name: this.querySelector('#name').value.trim(),
          email: this.querySelector('#email').value.trim(),
          github: this.querySelector('#github')?.value.trim() || '',
          interest: this.querySelector('#interest').value,
          message: this.querySelector('#message').value.trim(),
          recaptcha_token: recaptchaToken
        };

        // Send to backend
        const response = await fetch('api/send-message.php', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (result.success) {
          this.style.display = 'none';
          if (formSuccess) {
            formSuccess.style.display = 'block';
            formSuccess.style.animation = 'fadeInScale 0.4s ease-out';
          }
          this.reset();
        } else {
          const errorMsg = result.errors ? result.errors.join(', ') : (result.error || 'Failed to send message');
          showFormError(this, errorMsg);
          submitButton.innerHTML = originalText;
          submitButton.disabled = false;
        }
      } catch (error) {
        console.error('Form submission error:', error);
        showFormError(this, 'Network error. Please try again later.');
        submitButton.innerHTML = originalText;
        submitButton.disabled = false;
      }
    });
  }

  function showFormError(form, message) {
    const existingError = form.querySelector('.form-error');
    if (existingError) existingError.remove();

    const errorDiv = document.createElement('div');
    errorDiv.className = 'form-error';
    errorDiv.style.cssText = 'padding: 1rem; background: rgba(255, 51, 102, 0.1); color: #ff3366; border: 1px solid #ff3366; border-radius: 0.5rem; text-align: center; margin-top: 1rem; animation: fadeInScale 0.3s ease-out;';
    errorDiv.innerHTML = `<strong>Error:</strong> ${message}`;
    form.appendChild(errorDiv);

    setTimeout(() => {
      errorDiv.style.animation = 'fadeInScale 0.3s ease-out reverse';
      setTimeout(() => errorDiv.remove(), 300);
    }, 5000);
  }

  // =============================================
  // MATRIX RAIN BACKGROUND
  // =============================================

  const matrixContainer = document.querySelector('.matrix-rain');
  if (matrixContainer) {
    const chars = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789ABCDEF';
    const columns = Math.floor(window.innerWidth / 20);

    for (let i = 0; i < columns; i++) {
      const column = document.createElement('div');
      column.className = 'matrix-rain__column';
      column.style.left = `${i * 20}px`;
      column.style.animationDuration = `${8 + Math.random() * 10}s`;
      column.style.animationDelay = `${Math.random() * 5}s`;

      // Generate random string
      let text = '';
      const length = 10 + Math.floor(Math.random() * 20);
      for (let j = 0; j < length; j++) {
        text += chars.charAt(Math.floor(Math.random() * chars.length));
      }
      column.textContent = text;

      matrixContainer.appendChild(column);
    }
  }

  // =============================================
  // ANIMATED COUNTERS
  // =============================================

  const animateCounter = (element, target, duration = 2000) => {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;

    const updateCounter = () => {
      current += increment;
      if (current < target) {
        element.textContent = Math.floor(current);
        requestAnimationFrame(updateCounter);
      } else {
        element.textContent = target;
        const suffix = element.dataset.suffix || '';
        element.textContent = target + suffix;
      }
    };

    updateCounter();
  };

  const statNumbers = document.querySelectorAll('[data-count]');
  if (statNumbers.length > 0 && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = parseInt(entry.target.dataset.count, 10);
          animateCounter(entry.target, target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    statNumbers.forEach(el => counterObserver.observe(el));
  }

  // =============================================
  // GLITCH TEXT EFFECT
  // =============================================

  document.querySelectorAll('.glitch').forEach(el => {
    el.setAttribute('data-text', el.textContent);
  });

  // =============================================
  // BUTTON ANIMATIONS
  // =============================================

  document.querySelectorAll('.btn').forEach(btn => {
    btn.classList.add('btn-animated');
  });

  // =============================================
  // CARD ANIMATIONS
  // =============================================

  document.querySelectorAll('.card').forEach(card => {
    card.classList.add('card-animated');
  });

  // =============================================
  // ICON ANIMATIONS
  // =============================================

  document.querySelectorAll('.card__icon, .feature-item__icon').forEach(icon => {
    icon.classList.add('icon-animated');
  });

  // =============================================
  // REDUCED MOTION
  // =============================================

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  if (prefersReducedMotion.matches) {
    document.documentElement.classList.add('reduced-motion');
  }

  prefersReducedMotion.addEventListener('change', (e) => {
    if (e.matches) {
      document.documentElement.classList.add('reduced-motion');
    } else {
      document.documentElement.classList.remove('reduced-motion');
    }
  });

  // =============================================
  // TAB SWITCHING (for code examples)
  // =============================================

  document.querySelectorAll('.tabs').forEach(tabContainer => {
    const buttons = tabContainer.querySelectorAll('.tab-btn');
    const panels = tabContainer.querySelectorAll('.tab-panel');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.dataset.tab;

        buttons.forEach(b => b.classList.remove('active'));
        panels.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        tabContainer.querySelector(`[data-panel="${target}"]`)?.classList.add('active');
      });
    });
  });
});
