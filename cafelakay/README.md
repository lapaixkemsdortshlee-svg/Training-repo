# CafeLakay — Sit vitrine

Site web premium pour la marque de café haïtien **CafeLakay**, entièrement en
créole haïtien. Statique — aucun build, aucune dépendance : HTML + CSS + JS
vanilla, polices auto-hébergées (`fonts/`).

## ⚠️ Avant de publier : numéro WhatsApp

Toute la stratégie CTA passe par WhatsApp. Ouvrez `js/main.js` et remplacez le
numéro placeholder à la ligne 7 :

```js
const WA_NUMBER = "50900000000"; // ← mettez votre numéro, format international sans "+"
```

Exemple pour Haïti : `50937123456`. Tous les boutons « Kòmande » du site
(nav, héro, vitrine, cartes produits, CTA final, footer) utilisent ce numéro
avec un message pré-rempli par produit.

## Lancer en local

```bash
cd cafelakay
python3 -m http.server 8080
# → http://localhost:8080
```

## Déployer

C'est un dossier statique : Vercel, Netlify, GitHub Pages, ou n'importe quel
hébergeur. Aucune configuration nécessaire.

## Design

- **Palette** : noir café chaud `#0D0A08`, crème `#EFE6D8`, or caramel
  `#C9974C`. Le seul vert de la page est le bouton WhatsApp — le CTA est
  impossible à manquer.
- **Typographie** : Fraunces (display) + Instrument Sans (texte), variables,
  auto-hébergées.
- **Signature** : la « vitrine 3D » — effet container-scroll (inspiré du
  composant Aceternity sur 21st.dev, réimplémenté sans dépendance) qui
  redresse la carte produit pendant le scroll, avec un sac de café dessiné
  100 % en CSS/SVG.
- **Motion** : reveals au scroll (IntersectionObserver), marquee, lévitation
  du sac, glow ambiant — tout respecte `prefers-reduced-motion`.
