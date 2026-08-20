#!/usr/bin/env python3
"""Generate a dependency-free, professionally styled trading plan PDF."""
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "trading-plan" / "artifacts" / "plan-trading-us-breakout-opr.pdf"

W, H = 595, 842
M = 48

class PDF:
    def __init__(self):
        self.pages = []
        self.ops = []
        self.y = H - 74
    def esc(self, s): return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
    def text(self, x, y, txt, size=10, font='F1', color=(0.15,0.2,0.26)):
        r,g,b=color; self.ops.append(f"BT /{font} {size} Tf {r} {g} {b} rg {x:.1f} {y:.1f} Td ({self.esc(txt)}) Tj ET")
    def line(self, x1,y1,x2,y2,c=(0.75,0.78,0.82),w=.7):
        r,g,b=c; self.ops.append(f"{r} {g} {b} RG {w} w {x1} {y1} m {x2} {y2} l S")
    def rect(self,x,y,w,h,fill=None,stroke=(0.75,0.78,0.82),sw=.7):
        if fill:
            r,g,b=fill; self.ops.append(f"{r} {g} {b} rg {x} {y} {w} {h} re f")
        r,g,b=stroke; self.ops.append(f"{r} {g} {b} RG {sw} w {x} {y} {w} {h} re S")
    def header(self, n):
        self.rect(0,H-52,W,52,fill=(0.09,0.13,0.18),stroke=(0.09,0.13,0.18))
        self.text(M,H-32,"US Breakout (OPR) · Journal de trading",10,'F2',(0.79,0.59,0.30))
        self.text(W-205,H-32,"XAUUSD · NAS100USD · EURUSD",9,'F1',(1,1,1))
        self.text(W/2-18,22,f"Page {n}",8,'F1',(0.4,0.45,0.52))
    def new_page(self):
        if self.ops:
            self.pages.append('\n'.join(self.ops)); self.ops=[]
        self.header(len(self.pages)+1); self.y=H-82
    def wrap(self, txt, width=92): return textwrap.wrap(txt, width=width)
    def para(self, txt, size=10, leading=14, font='F1', color=(0.15,0.2,0.26), width=92, x=M):
        for line in self.wrap(txt, width):
            self.text(x,self.y,line,size,font,color); self.y-=leading
    def h1(self, txt):
        self.y-=6; self.text(M,self.y,txt,15,'F2',(0.09,0.13,0.18)); self.y-=20; self.line(M,self.y+8,W-M,self.y+8,(0.79,0.59,0.30),1)
    def checkbox(self, txt):
        self.rect(M,self.y-1,8,8,stroke=(0.79,0.59,0.30),sw=1); self.para(txt,9.5,13,'F1',width=88,x=M+16); self.y-=3
    def finish(self):
        self.pages.append('\n'.join(self.ops))
        objs=[]
        for stream in self.pages:
            objs.append(f"<< /Length {len(stream.encode('latin-1','replace'))} >>\nstream\n{stream}\nendstream")
        n_pages=len(self.pages); base=len(objs)
        page_ids=[]
        for i in range(n_pages): page_ids.append(base+2+i)
        kids=' '.join(f"{pid} 0 R" for pid in page_ids)
        objs.append(f"<< /Type /Pages /Kids [{kids}] /Count {n_pages} >>")
        for i in range(n_pages):
            objs.append(f"<< /Type /Page /Parent {base+1} 0 R /MediaBox [0 0 {W} {H}] /Resources << /Font << /F1 {base+n_pages+2} 0 R /F2 {base+n_pages+3} 0 R >> >> /Contents {i+1} 0 R >>")
        objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        objs.append(f"<< /Type /Catalog /Pages {base+1} 0 R >>")
        out=bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"); offsets=[0]
        for i,o in enumerate(objs,1):
            offsets.append(len(out)); out += f"{i} 0 obj\n{o}\nendobj\n".encode('latin-1','replace')
        xref=len(out); out += f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode()
        for off in offsets[1:]: out += f"{off:010d} 00000 n \n".encode()
        out += f"trailer << /Size {len(objs)+1} /Root {len(objs)} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
        OUTPUT.parent.mkdir(parents=True, exist_ok=True); OUTPUT.write_bytes(out); print(OUTPUT)

pdf=PDF(); pdf.new_page()
pdf.text(83,758,"PLAN DE TRADING : Stratégie US Breakout (OPR)",22,'F2',(0.09,0.13,0.18)); pdf.y=728
pdf.para("Concept de base : Exploiter la volatilité et les volumes massifs lors de l'ouverture de la session américaine en utilisant une cassure de la première bougie, en alignement avec la tendance de fond.",10.5,15,width=88)
pdf.rect(M,pdf.y-28,W-2*M,25,fill=(0.96,0.94,0.90),stroke=(0.79,0.59,0.30),sw=1)
for i,p in enumerate(['XAUUSD','NAS100USD','EURUSD']): pdf.text(M+58+i*165,pdf.y-13,p,11,'F2',(0.09,0.13,0.18))
pdf.y-=48
sections=[
('1. Checklist Quotidienne (Préparation)',["Calendrier Économique : Vérifier qu'il n'y a pas d'annonces majeures (NFP, CPI, PPI, FOMC, Taux d'intérêt) au moment de l'ouverture.","Gestion du Risque : Vérifier que la taille de position correspond à 0,25 % du capital maximum.","Horaires stricts : Se présenter devant les graphiques à 15h00-15h30. Aucune analyse avant 15h30 (Heure de Paris)."]),
('2. Configuration des Indicateurs',["Supertrend : Plage temporelle fixe sur 1 Heure (H1).","EMA 20 (Rouge) : Plage temporelle fixe de 5 minutes (M5).","EMA 50 (Noire) : Plage temporelle fixe de 5 minutes (M5)."]),
('3. Checklist d\'Exécution (À partir de 15h45)',["Étape 1 : Attendre la clôture de la bougie M15 (de 15h30 à 15h45).","Étape 2 : Tracer une ligne sur le point le plus HAUT et le point le plus BAS de cette bougie.","Étape 3 : Utiliser l'outil Fibonacci sur cette bougie pour afficher le niveau des 50 % (Stop Loss).","Étape 4 : Passer le graphique en 1 minute (M1) pour placer l'ordre."])]
for t,items in sections:
    pdf.h1(t)
    for it in items: pdf.checkbox(it)
pdf.h1('4. Conditions de Prise de Position (Ordre Automatique)')
pdf.text(M,pdf.y,'Pour un ACHAT',12,'F2',(0.12,0.55,0.38)); pdf.text(320,pdf.y,'Pour une VENTE',12,'F2',(0.70,0.20,0.20)); pdf.y-=18
left=["Le Supertrend (H1) est vert (sous le prix).","L'EMA 20 (rouge) est au-dessus de l'EMA 50 (noire).",'Action : Placer un ordre "Buy Stop" 1 point/pip au-dessus du haut de la bougie M15.']
right=["Le Supertrend (H1) est rouge (au-dessus du prix).","L'EMA 20 (rouge) est en dessous de l'EMA 50 (noire).",'Action : Placer un ordre "Sell Stop" 1 point/pip en dessous du bas de la bougie M15.']
y0=pdf.y
for it in left: pdf.checkbox(it)
pdf.y=y0
for it in right:
    pdf.rect(320,pdf.y-1,8,8,stroke=(0.79,0.59,0.30),sw=1); pdf.para(it,9.5,13,width=40,x=336); pdf.y-=3
pdf.y=min(pdf.y,y0-62)
pdf.h1('5. Gestion du Trade')
for it in ["Stop Loss (SL) : Placé sur les 50% du range de la bougie M15.","Take Profit (TP) : Ratio fixe selon l'actif (ex: 3.5 pour NAS100, 2 pour US30).","Heure limite : Clôture impérative à 21h00 maximum."]: pdf.checkbox(it)
pdf.h1('6. Métriques Clés (Rappel)')
for b in ["Taux de réussite (Win Rate) : Environ 30 %. Ne pas paniquer après 5 pertes consécutives.","Gestion du risque primordiale (0,25% par trade).","Toujours s'entraîner en démo avant de passer en réel."]: pdf.para('• '+b,10,14,width=88)
pdf.new_page(); pdf.text(100,758,'Journal de trading — Stratégie US Breakout (OPR)',20,'F2',(0.09,0.13,0.18)); pdf.y=724
pdf.para("À remplir pour chaque paire et chaque session. Une page par journée permet de suivre la discipline, les résultats et les axes d'amélioration.",10.5,15,width=88)
cols=[48,54,55,60,47,43,43,43,35,55,70]; headers=['Date','Paire','Biais H1','Range M15','Ordre','Entrée','SL','TP','R:R','Résultat','Notes']; x=M; y=pdf.y-5
pdf.rect(M,y-18,sum(cols),18,fill=(0.09,0.13,0.18),stroke=(0.09,0.13,0.18))
for c,h in zip(cols,headers): pdf.text(x+4,y-12,h,7,'F2',(1,1,1)); x+=c
pairs=['XAUUSD','NAS100USD','EURUSD']
for r in range(12):
    y-=28; x=M; pdf.rect(M,y,sum(cols),28,fill=(1,1,1) if r%2==0 else (.97,.98,.99),stroke=(.75,.78,.82),sw=.5)
    for c in cols: pdf.line(x,y,x,y+28,(.75,.78,.82),.5); x+=c
    pdf.line(x,y,x,y+28,(.75,.78,.82),.5); pdf.text(M+52,y+10,pairs[r%3],8,'F1')
pdf.y=y-28; pdf.para("Revue post-session : erreurs évitées, règle respectée, émotion dominante, amélioration pour demain.",10,14,width=88)
pdf.finish()
