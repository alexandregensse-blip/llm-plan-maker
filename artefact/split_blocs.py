# -*- coding: utf-8 -*-
"""Produit un dossier de relecture par bloc : le contexte commun, puis le bloc entier."""
import re, os, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
exec(open('gen.py', encoding='utf-8').read())          # remplit BLOCKS, DETTES, INVAR, BOUCLES

def txt(fragment):
    s = re.sub(r'<br\s*/?>', '\n', fragment)
    s = re.sub(r'<[^>]+>', '', s)
    return H.unescape(s).strip()

page = open(OUT, encoding='utf-8').read()

def section(sid):
    i = page.index('id="%s"' % sid)
    j = page.index('</section>', i)
    return txt(page[i:j])

COMMUN = '\n\n'.join([
    section('principe'), section('conception'), section('overview'),
    section('lexique'), section('types'), section('boucles'),
    section('invariants'), section('limites'),
])

OUTDIR = os.path.join(HERE, 'relecture2')
os.makedirs(OUTDIR, exist_ok=True)

for b in BLOCKS:
    parts = ['### RÔLE\n' + txt(b['role'])]
    if b.get('dia'):
        parts.append('### SCHÉMA « %s »\n%s' % (b['dia'][1], b['dia'][2].split('%%\n', 1)[1]))
    if b.get('code'):
        parts.append('### PSEUDO-CODE\n' + unify(b['code']))
    if b.get('note'):
        parts.append('### COMMENTAIRE\n' + txt(b['note']))
    for s in b.get('subs', []):
        parts.append('### SOUS-SECTION — ' + s[0])
        if s[2]:
            parts.append('SCHÉMA « %s »\n%s' % (s[2][1], s[2][2].split('%%\n', 1)[1]))
        parts.append(unify(s[1]))
    body = ('=========== CONTEXTE COMMUN À TOUT LE DOCUMENT ===========\n\n' + COMMUN +
            '\n\n=========== LE BLOC À RELIRE : %s · %s ===========\n\n' % (b['n'], b['t']) +
            '\n\n'.join(parts) + '\n')
    p = os.path.join(OUTDIR, 'bloc-%s.txt' % b['id'])
    open(p, 'w', encoding='utf-8').write(body)
    print(p, len(body))
