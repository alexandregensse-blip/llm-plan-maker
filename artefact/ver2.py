# -*- coding: utf-8 -*-
"""Controles complementaires : libelles mermaid, elisions, coherence des comptes."""
import re, html as H

import os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ardoise.html')
src = open(SRC, encoding='utf-8').read()
fail = []

# --- schemas -------------------------------------------------------------
for i, mm in enumerate(re.findall(r'<pre class="mermaid">(.*?)</pre>', src, re.S)):
    body = mm.split('%%\n', 1)[1]
    if not body.lstrip().startswith('flowchart TD'):
        fail.append(('direction', i))
    if '<br' in body:
        fail.append(('saut de ligne dans un libelle', i))
    # les etiquettes d'aretes sont tronquees par le rendu au-dela d'environ 20 signes
    for lab in re.findall(r'-\.?-\s*"([^"]+)"\s*\.?->', body):
        if len(lab) > 18:
            fail.append(('etiquette d arete trop longue', i, len(lab), lab))
    for lab in re.findall(r'[\[\{]"([^"]+)"[\]\}]', body):
        if len(lab) > 90:   # au-dela, le rendu ne peut plus envelopper proprement
            fail.append(('libelle trop long', i, len(lab), lab))
        if not lab[0].isupper() and not lab[0].isdigit():
            fail.append(('minuscule initiale', i, lab))
    # au plus deux sorties par noeud, et aucune boucle sur soi
    out = {}
    for line in body.split('\n'):
        c = re.sub(r'"[^"]*"', '', line)
        if c.strip().startswith(('class', 'classDef')):
            continue
        hops = [h.strip() for h in re.split(r'-\.?->|--', c) if h.strip()]
        hops = [re.sub(r'[\[\{].*', '', h).strip() for h in hops]
        hops = [h for h in hops if re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', h)]
        for a, b in zip(hops, hops[1:]):
            out.setdefault(a, set()).add(b)
            if a == b:
                fail.append(('boucle sur soi', i, a))
    for k, v in out.items():
        if len(v) > 2:
            fail.append(('plus de deux sorties', i, k, sorted(v)))

# --- pseudo-code ---------------------------------------------------------
code = '\n'.join(H.unescape(c) for c in
                 re.findall(r'<pre class="listing"><code>(.*?)</code></pre>', src, re.S))
for pat in [r'\b[Ll]a (entrée|itération)\b', r'\b[Ll]e (entrée|enchaînement|itération)\b',
            r'\bde (entrée|itération|enchaînement)\b', r'\bdu (entrée|enchaînement|itération)\b',
            r'\bà le (entrée|enchaînement|itération)\b', r'\bde la (entrée|itération)\b']:
    for m in re.finditer(pat, code):
        fail.append(('elision', code[max(0, m.start() - 30):m.end() + 10].replace('\n', ' | ')))
for w in ['POINT DE VAGUE', 'point de vague', 'point de synchronisation', 'pivot', 'PIVOT',
          "d'registre", "d'ardoise", 'une registre', 'la registre', 'cette registre',
          'Cas d\'exécution', 'Point à soumettre', 'Décision litigieuse']:
    if w in code or w in src:
        fail.append(('terme abandonne', w))
# « pas » au sens d'etape : le document dit « etape » partout
for pat in [r'\b(le|les|un|une|chaque|aucun|aucune|tout|toute|du|des|ce|cette|deux|premier) pas\b',
            r'\bpas (neuf|neufs|neuve|neuves)\b', r'\(pas\)', r'\bpas_']:
    for m in re.finditer(pat, code):
        fail.append(('pas au sens d etape', code[max(0, m.start() - 30):m.end() + 20].replace(chr(10), ' | ')))

# --- prose ---------------------------------------------------------------
text = re.sub(r'<[^>]+>', ' ', src)
text = H.unescape(text)
for w in [' vous ', ' votre ', ' vos ', 'vous-même']:
    if w in text:
        fail.append(('vouvoiement', w))
if '130' in text:
    fail.append(('compte de fonctions perime',))

# --- ancres du sommaire --------------------------------------------------
ids = set(re.findall(r'\bid="([^"]+)"', src))
for h in re.findall(r'href="#([^"]+)"', src):
    if h not in ids:
        fail.append(('ancre morte', h))

print('ERREURS:' if fail else '>>> AUCUNE ERREUR DETECTEE')
for f in fail:
    print(' -', f)
