# Artefact — architecture de plan-suite

Page unique décrivant l'architecture de production du plan : vue d'ensemble, onze blocs avec leurs schémas et leur pseudo-code, boucles et arguments de terminaison, invariants.

Publiée à l'adresse https://claude.ai/code/artifact/16851e9a-d3bc-4e55-a4c5-f12ad226df16

## Construire

```
cat gen_head.py gen_diagrams.py gen_data.py gen_tail.py > gen.py && python3 gen.py
python3 ver2.py
```

`ardoise.html` est le fichier produit, et c'est lui qui est publié.

## Ce que contient chaque source

`gen_head.py` lit le pseudo-code dans `../analyse/13-architecture-ardoise.md`, y applique les réécritures qui le mettent en accord avec les décisions d'architecture, puis unifie son vocabulaire.
Chaque réécriture est assortie d'une assertion : si le passage visé a bougé dans la source, la génération échoue au lieu de produire un document faux.

`gen_diagrams.py` contient les quatorze schémas, en syntaxe mermaid.

`gen_data.py` contient le texte des blocs — rôle, commentaire, découpes du pseudo-code — et les tables : cinq types d'entrée, six boucles, douze invariants, limites connues.

`gen_tail.py` assemble le tout dans `tpl.html`, qui porte la coque de la page, la feuille de style et les sections de prose.

`ver2.py` contrôle le fichier produit : imbrication HTML, ancres mortes, validité des schémas, longueur et casse des libellés, nombre de sorties par nœud, élisions et accords laissés par le renommage, termes abandonnés, vouvoiement.

`split_blocs.py` découpe le document en un dossier de relecture par bloc, chacun accompagné du contexte commun.
