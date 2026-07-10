/* ═══════════════════════════════════════════════════════
   CafeLakay — entèraksyon
   ═══════════════════════════════════════════════════════ */

/* ⚠️ KONFIGIRASYON — mete nimewo WhatsApp biznis ou a la a.
   Fòma entènasyonal SAN "+" ni espas. Egzanp Ayiti: 50937123456 */
const WA_NUMBER = "50900000000";

const prefersReducedMotion =
  window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ─── Lyen WhatsApp (estrateji CTA) ─────────────────── */

document.querySelectorAll("[data-wa]").forEach((el) => {
  const msg = el.dataset.msg || "Bonjou CafeLakay!";
  el.href = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`;
  el.target = "_blank";
  el.rel = "noopener";
});

/* ─── Navigasyon: fon lè w desann ───────────────────── */

const nav = document.getElementById("nav");
const onNavScroll = () => {
  nav.classList.toggle("is-scrolled", window.scrollY > 24);
};
onNavScroll();
window.addEventListener("scroll", onNavScroll, { passive: true });

/* ─── Reveal sou scroll (IntersectionObserver) ──────── */

const io = new IntersectionObserver(
  (entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        e.target.classList.add("is-in");
        io.unobserve(e.target);
      }
    }
  },
  { threshold: 0.18, rootMargin: "0px 0px -6% 0px" }
);
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

/* ─── Vitrin 3D: efè "container scroll" ─────────────────
   Kat la kòmanse panche (rotateX 22°) epi li vin dwat
   pandan w ap desann — menm prensip ak container-scroll-
   animation (Aceternity), reyekri isit la san depandans. */

const scene = document.getElementById("scene");
const card = document.getElementById("card");

if (scene && card && !prefersReducedMotion) {
  let ticking = false;

  const clamp = (v, min, max) => Math.min(max, Math.max(min, v));
  const easeOut = (t) => 1 - Math.pow(1 - t, 2.2);

  const update = () => {
    ticking = false;
    const rect = scene.getBoundingClientRect();
    const vh = window.innerHeight;

    /* pwogrè: 0 lè tèt sèn nan antre anba ekran an,
       1 lè mitan sèn nan rive nan mitan ekran an */
    const raw = (vh * 0.92 - rect.top) / (vh * 0.72);
    const p = easeOut(clamp(raw, 0, 1));

    const rx = 22 * (1 - p);           /* 22° → 0° */
    const sc = 0.94 + 0.06 * p;        /* 0.94 → 1 */
    const ty = 24 * (1 - p);           /* 24px → 0 */

    card.style.transform =
      `translateY(${ty}px) rotateX(${rx}deg) scale(${sc})`;
  };

  const requestUpdate = () => {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(update);
    }
  };

  update();
  window.addEventListener("scroll", requestUpdate, { passive: true });
  window.addEventListener("resize", requestUpdate, { passive: true });
}
