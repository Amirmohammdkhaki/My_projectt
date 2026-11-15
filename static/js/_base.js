/**
 * ============================================
 * باشگاه شیران — Base JavaScript
 * ============================================
 */

document.addEventListener("DOMContentLoaded", function () {
    "use strict";

    console.log("🦁 باشگاه شیران — بارگذاری موفق!");

    // ============================================
    // 1. Preloader
    // ============================================
    const preloader = document.getElementById("preloader");
    if (preloader) {
        window.addEventListener("load", function () {
            setTimeout(function () {
                preloader.classList.add("hidden");
            }, 500);
        });
        setTimeout(function () {
            preloader.classList.add("hidden");
        }, 3000);
    }

    // ============================================
    // 2. Scroll Progress
    // ============================================
    const scrollProgress = document.getElementById("scrollProgress");
    if (scrollProgress) {
        let ticking = false;
        window.addEventListener("scroll", function () {
            if (!ticking) {
                window.requestAnimationFrame(function () {
                    const scrollTop = window.scrollY;
                    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                    const percent = (scrollTop / docHeight) * 100;
                    scrollProgress.style.width = percent + "%";
                    ticking = false;
                });
                ticking = true;
            }
        });
    }

    // ============================================
    // 3. Scroll Top
    // ============================================
    const scrollTopBtn = document.getElementById("scrollTopBtn");
    if (scrollTopBtn) {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 300) {
                scrollTopBtn.classList.add("visible");
            } else {
                scrollTopBtn.classList.remove("visible");
            }
        });
        scrollTopBtn.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    // ============================================
    // 4. Live Clock
    // ============================================
    const liveClock = document.getElementById("liveClock");
    if (liveClock) {
        function updateClock() {
            const now = new Date();
            const hours = String(now.getHours()).padStart(2, "0");
            const minutes = String(now.getMinutes()).padStart(2, "0");
            const seconds = String(now.getSeconds()).padStart(2, "0");
            liveClock.textContent = hours + ":" + minutes + ":" + seconds;
        }
        updateClock();
        setInterval(updateClock, 1000);
    }

    // ============================================
    // 5. Theme Toggle
    // ============================================
    function applyTheme(theme) {
        document.documentElement.setAttribute("data-theme", theme);
        localStorage.setItem("theme", theme);

        const themeToggle = document.getElementById("themeToggle");
        if (themeToggle) {
            const icon = themeToggle.querySelector("i");
            if (icon) {
                icon.className = theme === "dark" ? "fas fa-moon" : "fas fa-sun";
            }
        }

        const floatingToggle = document.getElementById("floatingThemeToggle");
        if (floatingToggle) {
            const icon = floatingToggle.querySelector("i");
            if (icon) {
                icon.className = theme === "dark" ? "fas fa-moon" : "fas fa-sun";
            }
            if (theme === "dark") {
                floatingToggle.style.background = "rgba(17, 24, 39, 0.8)";
                floatingToggle.style.color = "#ffffff";
                floatingToggle.style.borderColor = "rgba(212, 175, 55, 0.3)";
            } else {
                floatingToggle.style.background = "rgba(255, 255, 255, 0.9)";
                floatingToggle.style.color = "#0f172a";
                floatingToggle.style.borderColor = "rgba(10, 31, 68, 0.2)";
            }
        }
    }

    const savedTheme = localStorage.getItem("theme") || "dark";
    applyTheme(savedTheme);

    const themeToggle = document.getElementById("themeToggle");
    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            const current = document.documentElement.getAttribute("data-theme") || "dark";
            const next = current === "dark" ? "light" : "dark";
            applyTheme(next);
        });
    }

    const floatingToggle = document.getElementById("floatingThemeToggle");
    if (floatingToggle) {
        floatingToggle.addEventListener("click", function () {
            const current = document.documentElement.getAttribute("data-theme") || "dark";
            const next = current === "dark" ? "light" : "dark";
            applyTheme(next);
        });
    }

    // ============================================
    // 6. Auto-dismiss Alerts (حذف شده، به Toast تبدیل شد)
    // ============================================
    // این بخش حالا در بخش Toast انجام می‌شود.

    // ============================================
    // 7. Close dropdown outside
    // ============================================
    document.addEventListener("click", function (e) {
        document.querySelectorAll(".dropdown").forEach(function (dropdown) {
            if (!dropdown.contains(e.target)) {
                const menu = dropdown.querySelector(".dropdown-menu");
                if (menu && menu.classList.contains("show")) {
                    menu.classList.remove("show");
                }
            }
        });
    });

    // ============================================
    // 8. Smooth Scroll
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener("click", function (e) {
            const targetId = this.getAttribute("href");
            if (targetId === "#" || targetId === "") return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const offset = 90;
                const pos = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top: pos, behavior: "smooth" });
            }
        });
    });

    // ============================================
    // 9. Animate Cards on Scroll
    // ============================================
    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = "1";
                        entry.target.style.transform = "translateY(0)";
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.1, rootMargin: "0px 0px -50px 0px" }
        );

        document
            .querySelectorAll(".feature-card, .price-card, .coach-card, .stat-card, .testimonial-card")
            .forEach(function (el) {
                el.style.opacity = "0";
                el.style.transform = "translateY(20px)";
                el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
                observer.observe(el);
            });
    }

    // ============================================
    // 10. Animate Numbers
    // ============================================
    const statNumbers = document.querySelectorAll(".stat-card .num");
    if (statNumbers.length > 0 && "IntersectionObserver" in window) {
        const statObserver = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        const el = entry.target;
                        const persianDigits = "۰۱۲۳۴۵۶۷۸۹";
                        const englishText = el.textContent.replace(/[۰-۹]/g, function (d) {
                            return persianDigits.indexOf(d);
                        });
                        const target = parseInt(englishText.replace(/[^\d]/g, "")) || 0;
                        if (target > 0) {
                            animateNumber(el, target);
                        }
                        statObserver.unobserve(el);
                    }
                });
            },
            { threshold: 0.5 }
        );

        statNumbers.forEach(function (el) {
            statObserver.observe(el);
        });

        function animateNumber(el, target) {
            let current = 0;
            const increment = target / 50;
            const timer = setInterval(function () {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                el.textContent = "+" + Math.floor(current);
            }, 30);
        }
    }

    // ============================================
    // 11. ⭐ Toast Notification System
    // ============================================
    window.showToast = function (message, type = "info", duration = 4000) {
        // حذف Toast قبلی اگر وجود دارد
        const existing = document.querySelector(".shiran-toast");
        if (existing) existing.remove();

        const toast = document.createElement("div");
        toast.className = `shiran-toast shiran-toast-${type}`;

        const icons = {
            success: "fa-check-circle",
            error: "fa-times-circle",
            warning: "fa-exclamation-triangle",
            info: "fa-info-circle"
        };

        toast.innerHTML = `
            <div class="shiran-toast-icon">
                <i class="fas ${icons[type] || icons.info}"></i>
            </div>
            <div class="shiran-toast-message">${message}</div>
            <button class="shiran-toast-close" aria-label="بستن">
                <i class="fas fa-times"></i>
            </button>
            <div class="shiran-toast-progress"></div>
        `;

        document.body.appendChild(toast);
        setTimeout(() => toast.classList.add("show"), 10);

        toast.querySelector(".shiran-toast-close").addEventListener("click", () => {
            toast.classList.remove("show");
            setTimeout(() => toast.remove(), 400);
        });

        setTimeout(() => {
            toast.classList.remove("show");
            setTimeout(() => toast.remove(), 400);
        }, duration);
    };

    // ============================================
    // 12. ⭐ تبدیل پیام‌های جنگو به Toast
    // ============================================
    document.querySelectorAll(".custom-alert").forEach(function (alert, index) {
        let type = "info";
        if (alert.classList.contains("alert-success")) type = "success";
        else if (alert.classList.contains("alert-danger") || alert.classList.contains("alert-error")) type = "error";
        else if (alert.classList.contains("alert-warning")) type = "warning";

        const message = alert.textContent.trim().replace(/\s+/g, " ");

        setTimeout(() => {
            alert.style.transition = "opacity 0.3s ease, transform 0.3s ease";
            alert.style.opacity = "0";
            alert.style.transform = "translateY(-10px)";
            setTimeout(() => alert.remove(), 300);
            window.showToast(message, type);
        }, index * 200);
    });

    // ============================================
    // 13. ⭐ Micro-interactions (انیمیشن دکمه‌ها)
    // ============================================
    document.querySelectorAll(".btn, button, .nav-link").forEach(function (btn) {
        btn.addEventListener("click", function (e) {
            const ripple = document.createElement("span");
            ripple.className = "btn-ripple";
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            ripple.style.width = ripple.style.height = size + "px";
            ripple.style.left = (e.clientX - rect.left - size / 2) + "px";
            ripple.style.top = (e.clientY - rect.top - size / 2) + "px";
            this.style.position = "relative";
            this.style.overflow = "hidden";
            this.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });
    });

    document.querySelectorAll(".btn").forEach(function (btn) {
        btn.addEventListener("mousedown", function () {
            this.style.transform = "scale(0.96)";
        });
        btn.addEventListener("mouseup", function () {
            this.style.transform = "";
        });
        btn.addEventListener("mouseleave", function () {
            this.style.transform = "";
        });
    });

    // ============================================
    // 14. ⭐ Scroll Reveal
    // ============================================
    if ("IntersectionObserver" in window) {
        const revealObserver = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("revealed");
                        revealObserver.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.15, rootMargin: "0px 0px -50px 0px" }
        );

        document.querySelectorAll(".reveal-on-scroll").forEach(function (el) {
            revealObserver.observe(el);
        });
    }

    // ============================================
    // 15. ⭐ Copy to Clipboard
    // ============================================
    window.copyToClipboard = function (text) {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(text).then(
                function () {
                    window.showToast("کپی شد!", "success");
                },
                function () {
                    window.showToast("خطا در کپی", "error");
                }
            );
        } else {
            const textarea = document.createElement("textarea");
            textarea.value = text;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand("copy");
            document.body.removeChild(textarea);
            window.showToast("کپی شد!", "success");
        }
    };

    // ============================================
    // 16. ⭐ Online/Offline Detection
    // ============================================
    window.addEventListener("online", function () {
        window.showToast("اتصال برقرار شد ✅", "success");
    });

    window.addEventListener("offline", function () {
        window.showToast("اتصال قطع شد ❌", "error", 6000);
    });

    // ============================================
    // 17. ⭐ Keyboard Shortcuts
    // ============================================
    document.addEventListener("keydown", function (e) {
        if ((e.ctrlKey || e.metaKey) && e.key === "k") {
            e.preventDefault();
            const searchModal = document.getElementById("searchModal");
            if (searchModal && window.jQuery) {
                window.jQuery(searchModal).modal("show");
            }
        }

        if (e.key === "Escape") {
            document.querySelectorAll(".modal.show").forEach(function (modal) {
                if (window.jQuery) {
                    window.jQuery(modal).modal("hide");
                }
            });
        }
    });

    // ============================================
    // 18. ⭐ Share on Social
    // ============================================
    window.shareOnSocial = function (platform) {
        const url = encodeURIComponent(window.location.href);
        const title = encodeURIComponent(document.title);
        let shareUrl = "";

        switch (platform) {
            case "facebook":
                shareUrl = "https://www.facebook.com/sharer/sharer.php?u=" + url;
                break;
            case "twitter":
                shareUrl = "https://twitter.com/intent/tweet?url=" + url + "&text=" + title;
                break;
            case "telegram":
                shareUrl = "https://t.me/share/url?url=" + url + "&text=" + title;
                break;
            case "whatsapp":
                shareUrl = "https://wa.me/?text=" + title + "%20" + url;
                break;
            case "linkedin":
                shareUrl = "https://www.linkedin.com/sharing/share-offsite/?url=" + url;
                break;
        }

        if (shareUrl) {
            window.open(shareUrl, "_blank", "width=600,height=500");
        }
    };

    // ============================================
    // 19. ⭐ Console Easter Egg
    // ============================================
    console.log(
        "%c🦁 باشگاه شیران",
        "color: #06b6d4; font-size: 24px; font-weight: bold; text-shadow: 0 0 10px #06b6d4;"
    );
    console.log(
        "%cقدرت، انگیزه، تعالی",
        "color: #3b82f6; font-size: 14px; font-style: italic;"
    );
});