# App — Plan de trading US Breakout (OPR)

Utilisation simple : ouvrez le lien `trading-plan/index.html` dans un navigateur et utilisez-le comme une petite app.

## Ce que vous pouvez faire

- Modifier directement les textes, règles, paires et lignes du journal.
- Ajuster le risque, les horaires et le ratio TP.
- Cocher/décocher les checklists pendant votre session.
- Sauvegarder automatiquement vos changements dans le navigateur.
- Télécharger une sauvegarde JSON avec **Sauvegarder mes données**.
- Restaurer une sauvegarde JSON avec **Restaurer mes données**.
- Exporter votre version en PDF avec **Exporter les modifications en PDF**.
- Installer l'app si le navigateur propose le bouton **Installer l'app**.

## Fichiers

- App prête à utiliser : `trading-plan/index.html`
- Mode app installable : `trading-plan/manifest.webmanifest` + `trading-plan/sw.js`
- PDF statique : `trading-plan/artifacts/plan-trading-us-breakout-opr.pdf`
- Générateur du PDF statique : `scripts/generate_trading_plan_pdf.py`

## Régénérer le PDF statique

```bash
python3 scripts/generate_trading_plan_pdf.py
```
