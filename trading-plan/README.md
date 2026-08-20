# App — Plan de trading US Breakout (OPR)

✅ Conflit résolu : cette version conserve l'app simple et prête à utiliser.

## Lien à ouvrir

Ouvrez directement ce fichier dans votre navigateur :

```text
trading-plan/index.html
```

Vous pouvez aussi lancer un petit serveur local depuis la racine du projet :

```bash
python3 -m http.server 8080
```

Puis ouvrir :

```text
http://localhost:8080/trading-plan/
```

## Utilisation normale

1. Ouvrez l'app.
2. Cliquez sur les textes, règles, paires ou lignes du journal pour les modifier.
3. Ajustez le risque, les horaires et le ratio TP.
4. Cochez/décochez les checklists pendant votre session.
5. Remplissez le journal de trading.
6. Cliquez sur **Sauvegarder mes données** pour télécharger une copie JSON.
7. Cliquez sur **Restaurer mes données** pour recharger une sauvegarde JSON.
8. Cliquez sur **Exporter les modifications en PDF** pour enregistrer votre version personnalisée.

## Fichiers

- App prête à utiliser : `trading-plan/index.html`
- Mode app installable : `trading-plan/manifest.webmanifest` + `trading-plan/sw.js`
- PDF statique : `trading-plan/artifacts/plan-trading-us-breakout-opr.pdf`
- Générateur du PDF statique : `scripts/generate_trading_plan_pdf.py`

## Régénérer le PDF statique

```bash
python3 scripts/generate_trading_plan_pdf.py
```
