const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("visible");
            observer.unobserve(e.target);
          }
        });
      },
      { threshold: 0.08 },
    );
    document
      .querySelectorAll(".fade-up")
      .forEach((el) => observer.observe(el));

    const navLinks = document.querySelectorAll(".nav-link");
    const sections = Array.from(navLinks)
      .map((link) => document.querySelector(link.getAttribute("href")))
      .filter(Boolean);
    const navBySectionId = new Map(
      Array.from(navLinks).map((link) => [
        link.getAttribute("href").slice(1),
        link,
      ]),
    );
    const menuBtn = document.getElementById("menuBtn");
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");
    const topNav = document.getElementById("topNav");
    const progressBar = document.getElementById("progressBar");
    const backToTop = document.getElementById("backToTop");
    const chatToggle = document.getElementById("chatToggle");
    const chatClose = document.getElementById("chatClose");
    const openPixVideo = document.getElementById("openPixVideo");
    const modal = document.getElementById("modal");
    const modalIframe = document.getElementById("modal-iframe");
    const closeModalBtn = document.getElementById("closeModalBtn");

    function setActiveSection(id) {
      navLinks.forEach((link) => {
        link.classList.toggle("active", link === navBySectionId.get(id));
      });
    }

    const activeSectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) setActiveSection(entry.target.id);
        });
      },
      {
        rootMargin: "-28% 0px -62% 0px",
        threshold: 0,
      },
    );
    sections.forEach((section) => activeSectionObserver.observe(section));

    // Scroll shadow on nav + progress bar + utility buttons
    
let isScrolling = false;
window.addEventListener("scroll", () => {
  if (!isScrolling) {
    isScrolling = true;
    window.requestAnimationFrame(() => {

      const heroHeight = document.querySelector(".hero").offsetHeight;
      topNav.classList.toggle("scrolled", window.scrollY > heroHeight - 80);

      // Progress bar
      const scrollTop = window.scrollY;
      const docHeight =
        document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + "%";

      backToTop.classList.toggle("visible", scrollTop > 600);
      chatToggle.classList.toggle("visible", scrollTop > 720);
      isScrolling = false;
    });
  }
});

    // Mobile menu toggle
    function toggleMenu() {
      sidebar.classList.toggle("open");
      overlay.classList.toggle("open");
    }
    menuBtn.addEventListener("click", toggleMenu);
    overlay.addEventListener("click", toggleMenu);
    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        sidebar.classList.remove("open");
        overlay.classList.remove("open");
      });
    });

    function openModal() {
      modalIframe.src = "https://www.youtube.com/embed/BjnrFbpOGho?autoplay=1";
      modal.classList.add("open");
      document.body.style.overflow = "hidden";
    }

    function closeModal(e) {
      if (e && e.target !== modal && e.currentTarget !== closeModalBtn) return;
      modalIframe.src = "";
      modal.classList.remove("open");
      document.body.style.overflow = "";
    }

    openPixVideo.addEventListener("click", openModal);
    modal.addEventListener("click", closeModal);
    closeModalBtn.addEventListener("click", closeModal);
    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    chatToggle.addEventListener("click", toggleChat);
    chatClose.addEventListener("click", toggleChat);

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeModal();
    });

    // Gift timer animation
    (function () {
      const el = document.getElementById("giftTimer");
      if (!el) return;
      let secs = 0;
      setInterval(() => {
        secs = secs >= 60 ? 0 : secs + 1;
        const m = String(Math.floor(secs / 60)).padStart(2, "0");
        const s = String(secs % 60).padStart(2, "0");
        el.textContent = m + ":" + s;
      }, 1000);
    })();
