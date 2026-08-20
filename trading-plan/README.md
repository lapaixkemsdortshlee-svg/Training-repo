# Artefact — Plan de trading US Breakout (OPR)

Cette page fournit un artefact HTML modifiable avec barre de progression à chaque clic et un PDF téléchargeable du plan de trading demandé.

- Page interactive et éditable : `trading-plan/index.html`
- PDF généré : `trading-plan/artifacts/plan-trading-us-breakout-opr.pdf`
- Script de génération : `scripts/generate_trading_plan_pdf.py`

## Personnaliser le document

1. Ouvrez `trading-plan/index.html` dans un navigateur.
2. Cliquez directement sur les titres, paragraphes, règles ou lignes du journal pour les modifier.
3. Ajustez le risque, les horaires, le ratio TP et les paires depuis les champs dédiés.
4. Utilisez **Exporter les modifications en PDF** pour imprimer la version modifiée en PDF, ou **Préparer et télécharger le PDF** pour télécharger l'artefact généré.

Les modifications sont sauvegardées dans le stockage local du navigateur jusqu'à réinitialisation.

## Régénérer le PDF statique

```bash
python3 scripts/generate_trading_plan_pdf.py
```
