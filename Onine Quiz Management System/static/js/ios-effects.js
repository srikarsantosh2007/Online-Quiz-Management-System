/* Online Quiz Management System - UI effects (no dependencies) */
(function () {
    'use strict';
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var root = document.documentElement;

    /* ---------- Theme toggle (light / dark) ---------- */
    function applyTheme(t) {
        root.setAttribute('data-bs-theme', t);
        var icon = document.querySelector('#themeToggle i');
        if (icon) icon.className = t === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
    }
    document.addEventListener('DOMContentLoaded', function () {
        applyTheme(root.getAttribute('data-bs-theme') || 'light');
        var btn = document.getElementById('themeToggle');
        if (btn) btn.addEventListener('click', function () {
            var next = root.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
            applyTheme(next);
            try { localStorage.setItem('qms-theme', next); } catch (e) {}
        });

        init();
    });

    function init() {
        /* footer year */
        document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

        /* ---------- Scroll reveal (staggered) ---------- */
        var targets = document.querySelectorAll('main .card, main .stat, main .alert, main .table-responsive, main .breadcrumb, main h2, main .hero');
        var seen = new Set();
        targets.forEach(function (el, i) {
            if (el.closest('.card') && el.closest('.card') !== el && el.classList.contains('card')) { /* nested card: let parent animate */ }
            el.classList.add('reveal');
            el.style.setProperty('--d', Math.min((i % 6) * 70, 350) + 'ms');
        });
        if ('IntersectionObserver' in window && !reduce) {
            var io = new IntersectionObserver(function (entries) {
                entries.forEach(function (e) {
                    if (e.isIntersecting) {
                        var t = e.target;
                        t.classList.add('in'); io.unobserve(t);
                        /* hand control back to normal hover styles once the entrance is done */
                        setTimeout(function () { t.classList.remove('reveal', 'in'); t.style.removeProperty('--d'); }, 1300);
                    }
                });
            }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
            document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
        } else {
            document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
        }

        /* ---------- Count-up numbers ---------- */
        document.querySelectorAll('.card .display-4, .stat .num, [data-count]').forEach(function (el) {
            var txt = el.textContent.trim();
            if (!/^\d+$/.test(txt) || reduce) return;
            var end = parseInt(txt, 10), start = null, dur = 1300;
            el.textContent = '0';
            function step(ts) {
                if (!start) start = ts;
                var p = Math.min((ts - start) / dur, 1), eased = 1 - Math.pow(1 - p, 4);
                el.textContent = Math.round(end * eased);
                if (p < 1) requestAnimationFrame(step);
            }
            var o = new IntersectionObserver(function (en) {
                if (en[0].isIntersecting) { requestAnimationFrame(step); o.disconnect(); }
            });
            o.observe(el);
        });

        /* ---------- Button ripple ---------- */
        document.addEventListener('click', function (e) {
            var b = e.target.closest('.btn');
            if (!b || reduce) return;
            var r = b.getBoundingClientRect(), size = Math.max(r.width, r.height);
            var s = document.createElement('span');
            s.className = 'ripple';
            s.style.cssText = 'width:' + size + 'px;height:' + size + 'px;left:' + (e.clientX - r.left - size / 2) + 'px;top:' + (e.clientY - r.top - size / 2) + 'px';
            b.appendChild(s);
            setTimeout(function () { s.remove(); }, 700);
        });

        /* ---------- Cursor spotlight on cards ---------- */
        document.addEventListener('pointermove', function (e) {
            var c = e.target.closest && e.target.closest('.card');
            if (!c) return;
            var r = c.getBoundingClientRect();
            c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
            c.style.setProperty('--my', (e.clientY - r.top) + 'px');
        }, { passive: true });

        /* ---------- Aurora parallax ---------- */
        var blobs = document.querySelectorAll('.aurora span');
        if (!reduce && blobs.length && window.matchMedia('(pointer:fine)').matches) {
            document.addEventListener('pointermove', function (e) {
                var x = (e.clientX / innerWidth - .5), y = (e.clientY / innerHeight - .5);
                blobs.forEach(function (b, i) {
                    b.style.translate = (x * (i + 1) * -22) + 'px ' + (y * (i + 1) * -22) + 'px';
                });
            }, { passive: true });
        }

        /* ---------- Page leave transition ---------- */
        document.addEventListener('click', function (e) {
            var a = e.target.closest('a[href]');
            if (!a || reduce || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
            var href = a.getAttribute('href');
            if (!href || href.charAt(0) === '#' || a.target === '_blank' || a.hasAttribute('data-bs-toggle') || a.hasAttribute('download')) return;
            if (a.origin !== location.origin || /^(mailto|tel|javascript):/.test(href)) return;
            if (a.hasAttribute('onclick')) return;
            e.preventDefault();
            document.body.classList.add('leaving');
            setTimeout(function () { location.href = a.href; }, 200);
        });
        window.addEventListener('pageshow', function () { document.body.classList.remove('leaving'); });

        /* ---------- Auto-dismiss flash alerts ---------- */
        document.querySelectorAll('.alert-dismissible').forEach(function (a) {
            setTimeout(function () {
                if (window.bootstrap && document.body.contains(a)) bootstrap.Alert.getOrCreateInstance(a).close();
            }, 7000);
        });

        /* ---------- Score ring + confetti (result page) ---------- */
        document.querySelectorAll('.score-ring').forEach(function (ring) {
            var pct = Math.max(0, Math.min(100, parseFloat(ring.dataset.percent) || 0));
            var bar = ring.querySelector('.bar');
            var color = pct >= 70 ? 'url(#gGood)' : pct >= 50 ? 'url(#gMid)' : 'url(#gBad)';
            bar.setAttribute('stroke', color);
            setTimeout(function () { bar.style.strokeDashoffset = 452.4 * (1 - pct / 100); }, 250);
            var num = ring.querySelector('[data-pct-num]');
            if (num && !reduce) {
                var t0 = null;
                (function tick(ts) {
                    if (!t0) t0 = ts;
                    var p = Math.min((ts - t0) / 1600, 1);
                    num.textContent = Math.round(pct * (1 - Math.pow(1 - p, 3))) + '%';
                    if (p < 1) requestAnimationFrame(tick);
                })(performance.now());
            }
            if (pct >= 70 && !reduce) setTimeout(confetti, 600);
        });
    }

    function confetti() {
        var colors = ['#0a84ff', '#bf5af2', '#ff375f', '#ff9f0a', '#30d158', '#64d2ff', '#ffd60a'];
        for (var i = 0; i < 90; i++) {
            var c = document.createElement('i');
            c.className = 'confetti';
            c.style.left = Math.random() * 100 + 'vw';
            c.style.background = colors[i % colors.length];
            c.style.setProperty('--dx', (Math.random() * 240 - 120) + 'px');
            c.style.setProperty('--rot', (Math.random() * 900 - 450) + 'deg');
            c.style.animationDuration = (2.4 + Math.random() * 2.2) + 's';
            c.style.animationDelay = (Math.random() * .8) + 's';
            document.body.appendChild(c);
            setTimeout((function (n) { return function () { n.remove(); }; })(c), 6000);
        }
    }
})();
