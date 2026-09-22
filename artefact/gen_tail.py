
# --- assemble ------------------------------------------------------------
def block_html(b):
    o = ['<section class="block" id="%s">' % b['id']]
    o.append('<header class="block-h"><span class="bn">%s</span><h3>%s</h3></header>' % (b['n'], b['t']))
    o.append('<p class="role">%s</p>' % b['role'])
    if b.get('dia'):
        o.append(plate(*b['dia']))
    if b.get('code'):
        o.append(pre(b['code']))
    if b.get('note'):
        o.append('<p class="note">%s</p>' % b['note'])
    for s in b.get('subs', []):
        o.append('<div class="sub"><h4>%s</h4>' % s[0])
        if s[2]:
            o.append(plate(*s[2]))
        o.append(pre(s[1]))
        o.append('</div>')
    o.append('</section>')
    return '\n'.join(o)

blocks_html = '\n'.join(block_html(b) for b in BLOCKS)
dettes_html = '\n'.join(
  '<tr><th scope="row"><span class="chip d">%s</span></th><td>%s</td><td>%s</td></tr>' % d for d in DETTES)
boucles_html = '\n'.join(
  '<tr><th scope="row">%s</th><td>%s</td><td>%s</td><td>%s</td></tr>' % b for b in BOUCLES)
invar_html = '\n'.join(
  '<li><span class="ik">%s</span><span>%s</span></li>' % i for i in INVAR)
ouvert_html = '\n'.join(
  '<div class="open-item"><h4>%s</h4><p>%s</p></div>' % o for o in OUVERT)

NAV = [('principe','Principe de fonctionnement'),('conception','Contraintes de conception'),
       ('overview',"Vue d'ensemble"),('lexique','Lexique'),('types',"Les cinq types d'entrée"),
       ('blocs-intro','Pseudo-code'),
       ('porte','00 · Entrée'),('crible','01 · Le crible'),
       ('confronter','§ · confronter()'),
       ('niveau1','02 · Niveau 1'),('niveau2','03 · Niveau 2'),('vague',"04 · L'itération"),
       ('apurement','05 · Résorption'),('pointdevague','06 · Envoi des questions'),
       ('reecriture','07 · Réécriture'),('miseenforme','08 · Mise en forme'),
       ('controle','09 · Contrôle'),
       ('boucles','Boucles et terminaison'),('invariants','Invariants'),
       ('limites','Limites connues')]
nav_html = '\n'.join('<a href="#%s">%s</a>' % n for n in NAV)

tpl = open(os.path.join(os.path.dirname(OUT),'tpl.html'), encoding='utf-8').read()
for k, v in [('{{NAV}}',nav_html),('{{BLOCKS}}',blocks_html),('{{DETTES}}',dettes_html),
             ('{{BOUCLES}}',boucles_html),('{{INVAR}}',invar_html),('{{OUVERT}}',ouvert_html),
             ('{{D_OVER}}',D_OVER)]:
    assert k in tpl, 'placeholder manquant: ' + k
    tpl = tpl.replace(k, v)
assert '{{' not in tpl, 'placeholder residuel'
open(OUT,'w',encoding='utf-8').write(tpl)
print('written', OUT, os.path.getsize(OUT))
