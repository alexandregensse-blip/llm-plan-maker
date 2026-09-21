# plan-suite — cartographie des 16 versions

Document de travail. Lu intégralement : `plan-suite.skill.md` (= v3) et `v4` → `v18`,
soit 16 fichiers / ~8 800 lignes / ~330 Ko dans `plans_versions_input/`.

But : savoir ce qui est **acquis**, ce qui est **encore en litige**, ce qui est
**orphelin** (bonne idée présente dans une seule version), et ce qu'**aucune**
version ne traite — avant de fabriquer une version diffusable.

---

## 1. Inventaire

| Fichier | Lignes | Titre / thèse | Verdict rapide |
|---|---:|---|---|
| `skill.md` (v3) | 329 | Generic Plan Making — PCS + boucle need→states→guards→objectives→options→actions, 4 sous-fichiers | Historique. Le PCS (score arithmétique) est une fausse précision. Mais c'est la seule version avec schéma d'artefact versionné + chemin critique. |
| v4 | 199 | Model Allocation & Consolidation — classes R/D/J, ensemble de 3 drafters, juge consolidateur | Bonne intuition économique (multi-modèles). Mauvaise par défaut : ensemble systématique. Remplace le PCS par une table qualitative — bon. |
| v5 | 927 | Evidence-Grounded Multi-Agent Planning — graphe de décisions, evidence cards, I0–I4 | Le plus complet de la lignée « épistémique ». Inapplicable tel quel (15 sections de sortie obligatoires). |
| v6 | 565 | Decision-First Planning — decision spine, pre-mortem, budget de preuves | Première version qui **nomme les failure modes LLM**. Quotas chiffrés arbitraires. |
| v7 | 676 | Calibrated Commitment Planning — **compulsion check**, ledger de commitments, oracle utilisateur, meta-status `unproven` | Le plus gros saut conceptuel de la série. Contient une faute grave : « Silence = approval » (§7.2). |
| v8 | 1690 | Evidence-Guided Adaptive Planning — carte de matérialité, rôles d'agents, §32 « ce que v8 retire », §33 self-test métrique | Le plus **honnête** intellectuellement, le plus **inutilisable** pratiquement. Bugs de fabrication (titre dupliqué, numérotation qui démarre à §4). |
| v9 | 85 | Radical Empiricism — Horizon + Frontier, zéro bureaucratie | Coup de hache salutaire contre v8. Jette aussi tout ce qui était bon : traçabilité, construction de plan, multi-agents. « 100% empirical certainty » = formulation intenable. |
| v10 | 339 | Empirical Planning with Calibrated Containment — **care triggers**, echo-chamber check | Très bon rapport concision/rigueur. `care triggers` = la bonne abstraction pour « discipline seulement où se tromper coûte ». |
| v11 | 266 | Frontier Planning | **Seule version avec un vrai §4 « Building the plan »** (chaînage arrière depuis la cible, tri par précondition, élagage). Pièce manquante partout ailleurs. |
| v12 | 289 | Planning that pays rent | Le mieux écrit de la lignée empirique. Introduit **known path vs frontier work** (§1), vraie découverte. §0 : « le protocole doit passer son propre triage ». |
| v13 | 88 | State-Driven Containment Loop | Ultra-compact. Bon §6 « quand abandonner ». Trop maigre pour être diffusé seul. |
| v14 | 280 | Independent Validation Routing | **La fusion explicite** des deux écoles, bien argumentée. Meilleur rapport densité/valeur de toute la série. |
| v15 | 862 | State-Driven Commitment Protocol | Fusion mal digérée : séparateurs `---` triplés, emojis ✅❌⚠️, §8/§9/§10 redondants, **deux taxonomies de types d'action contradictoires** (§12 vs §13.1). Régression de forme. |
| v16 | 578 | Compelled Navigation with Blind Confrontation | Nettoyage propre de v15. |
| v17 | 799 | + Honest Diversity | Ajoute l'**Explorer / framing pass** obligatoire en L2/L3. Bonne idée, rendue obligatoire sans voie de dégradation. |
| v18 | 826 | Framing Before Framing | Corrige v17 (framing pass en 3 formes dégradables, dont `staged-weak`), ajoute **robustness**, **budget degradation**, **shape** (plan- / learning-dominant). État de l'art de la série. |

---

## 2. Généalogie : trois lignées, pas une progression

Ce n'est pas v3→v18 linéaire. Ce sont **trois écoles** dont la dernière essaie de recoller.

### Lignée A — bureaucratie épistémique (v3 → v4 → v5 → v6 → v7 → v8)

Thèse : *un plan est un ensemble de décisions résolues ; chaque décision porte
des preuves, des attaques indépendantes, une provenance auditable.*

Trajectoire : 329 → 199 → 927 → 565 → 676 → **1690 lignes**. Explosion.

- Apports durables : séparation fait/hypothèse/préférence/contrainte, « les agents
  ne sont pas des preuves », pas de vote majoritaire, erreurs corrélées,
  contrat d'action, compulsion check (v7), meta-status `unproven` (v7).
- Pathologie : le protocole devient plus gros que le travail qu'il encadre. v7
  le diagnostique lui-même (Annexe B) : *« Long protocols get performed, not
  followed. Compliance theater is the dominant failure mode of skills like this one. »*
  …puis v8 fait 1690 lignes.

### Lignée B — empirisme radical (v9 → v10 → v11 → v12 → v13)

Thèse : *un LLM est un mauvais moteur physique. Tout plan long est de
l'hallucination déguisée en rigueur. On n'avance qu'en observant.*

v9 est une **réaction explicite** à v8 (elle le dit : « Previous versions attempted
to pre-compute complex state-transition graphs… This fails »). Retour à 85 lignes.

- Apports durables : Horizon/Frontier, contrat d'action en 3 lignes, fog of war,
  care triggers (v10), echo-chamber check (v10), known-path vs frontier (v12),
  « comment construire le plan » (v11).
- Pathologie inverse : à force de dire « n'invente pas d'étapes », le skill
  **cesse d'enseigner la planification**. v9 et v13 ne savent plus produire un plan,
  seulement exécuter prudemment. Plus aucune traçabilité, plus aucun usage des agents.

### Lignée C — fusion (v14 → v15 → v16 → v17 → v18)

v14 pose le diagnostic juste : *« This skill fuses two schools that previous
versions wrongly treated as rivals »* — l'environnement valide les faits ; les
contextes aveugles valident ce que l'environnement ne peut pas trancher
(framing, hypothèses, modes de défaillance, vrais choix).

v14 (280 l.) → v15 (862 l., régression de forme) → v16 (578) → v17 (799) → v18 (826).
**La fusion refait exactement le chemin de la lignée A : 280 → 826 lignes en 4 itérations.**
C'est le signal le plus important de tout le corpus.

---

## 3. Noyau convergent — ce qui est acquis (à ne plus rediscuter)

Présent, sous une forme ou une autre, dans la quasi-totalité des versions récentes,
et jamais contesté sur le fond :

1. **Triage en premier**, profondeur L0–L3, et le skill doit pouvoir dire « pas mon
   problème » (v6 §12, v10 §9, v12 §12, v13 §6, v16–v18 §12/§13).
   *« A skill that never says "I am not the right tool" is dangerous. »*
2. **Cible observable et falsifiable.** « Improve security » ✗ / « test X montre que
   les chemins d'accès sont fermés sous le modèle de menace T » ✓.
3. **Invariants ≠ préférences.** Ne jamais promouvoir une préférence en contrainte dure.
4. **« Vérifié » = observé.** Données d'entraînement, mémoire de session antérieure,
   assertion d'un autre agent ≠ vérification.
5. **Contrat d'action** : `Intent / Expected / Containment`. `Expected` falsifiable
   (« check it works » interdit). Rollback pensé **avant** exécution.
6. **Validation attachée à l'action**, jamais reportée à la fin.
7. **Irréversible sans containment ⇒ gate.** Pas d'exécution unilatérale.
8. **Les agents ne sont pas des preuves** ; pas de vote majoritaire ; contrôle des
   erreurs corrélées ; labels d'indépendance honnêtes (`staged` / `isolated` / `external`),
   jamais promus. *La température n'est pas de l'indépendance.*
9. **Atteindre la cible en violant une contrainte dure = `invalid`**, pas « risqué ».
10. **Pas de synthèse silencieuse** : toute action non proposée par un candidat est
    taguée `derived-from:`.
11. **Fog of war** : pas d'étapes inventées au-delà de la frontière. Si l'étape 5
    dépend de la sortie non observée de l'étape 2, supprimer 3–5.
12. **Mismatch ⇒ stop.** Ne pas composer les erreurs. Replanifier le plus petit
    sous-arbre affecté, pas tout.
13. **Digest par phase** : `done | failed | new unknowns | state delta | next gate`.
14. **Handoff** : rien de load-bearing ne vit en mémoire seule.
15. **Attaquer ≠ relire** : ne jamais donner à l'attaquant le plaidoyer du candidat,
    seulement l'action et les faits.
16. **Compulsion check** (depuis v7) : si les faits vérifiés + contraintes dures ne
    laissent qu'un chemin, le prendre. Zéro candidat, zéro débat.
    *« Deliberating a compelled answer is hallucinated rigor. »*
    → C'est probablement l'idée la plus rentable de tout le corpus.
17. **Meta-status `unproven`** + procédure d'auto-test (rejouer 3–5 échecs passés).
    Honnêteté rare et précieuse ; à garder.

---

## 4. Divergences réelles — à arbitrer

| # | Question | Positions | Arbitrage proposé |
|---|---|---|---|
| D1 | **Le silence vaut-il approbation ?** | v7 §7.2 : « Silence = approval ». v8 I9 → v18 : **jamais**, sauf délégation explicite préalable. | v8. Une faute de sécurité franche dans v7. |
| D2 | **Quotas chiffrés** (2 candidats, ≤2 preuves/commitment, 2 questions/phase) | v6/v7/v15–v18 : oui, ce sont des stop rules. v8 §32 : supprimés explicitement comme « fausses lois générales ». | Compromis : garder comme **valeurs par défaut affichées comme telles**, avec la question de stop de v8 (« cet agent peut-il changer ce qu'on fait ? »). Un quota sans stop rule ne sert à rien ; une stop rule sans chiffre n'est jamais appliquée. |
| D3 | **TTL des preuves** | v7 : `ttl`, défaut « cette session ». v8 §13.4 : refuse le TTL universel, préfère `freshness: stable / low_volatility / volatile`. v16–v18 : retour au TTL session. | v8 a raison sur le fond (l'âge ne compte que relativement à la nature du fait), v7 sur l'ergonomie. Garder `ttl` + une note « volatile ⇒ re-vérifier au moment d'exécuter ». |
| D4 | **« Ship at 80% » / planning debt** | v6/v7/v12/v14–v18 : oui. v8 §32 : retiré comme non prouvé. | Garder. Le principe « exécutable et récupérable, pas complet » est plus utile que le chiffre. Supprimer « 80 % ». |
| D5 | **« Most commitments are compelled »** | Affirmé v7/v15–v18. v8 le retire comme assertion non étayée. | Reformuler en heuristique, pas en loi : « le défaut est zéro candidat ; c'est le spawn qui se justifie ». |
| D6 | **Confiance vs robustesse** | v7 : `high/medium/low` + ship rules. v8 §18 : `robust/sensitive/contained` (« plus utile qu'un label de confiance générique »). v18 : **les deux**. | v18 a raison sur le fond mais paie en volume. Si un seul doit rester : **robustesse** (elle nomme le fait qui ferait basculer, donc elle se câble directement aux replan triggers). |
| D7 | **Score arithmétique de complexité (PCS)** | v3 seul. Supprimé en v4 avec justification (« removes false precision »). | Ne jamais ressusciter. |
| D8 | **Classes de modèles R/D/J** | v4 seul, puis disparu. | Orphelin à récupérer (voir §5). La vraie économie multi-modèles n'est traitée nulle part ailleurs. |
| D9 | **Le skill enseigne-t-il à *construire* un plan ?** | v3 (boucle need→…→actions), v5/v6 (decision graph), **v11 §4** (chaînage arrière, tri par précondition, élagage). Absent de v13, v16, v17, v18. | **Trou majeur.** v16–v18 savent trier, valider, contenir, attaquer — mais ne disent nulle part comment on passe d'un objectif à une séquence. Réinjecter v11 §4. |
| D10 | **Taxonomie des types d'étape** | A : `discovery / commitment / derived / experiment` (v10, v11). B : `discovery / change / validation / rollback / ask_user / branch / handoff` (v5–v7, v15 §12). v15 contient **les deux, contradictoires**. | A. B mélange nature épistémique et catégorie d'action. `ask_user` reste utile comme type d'action de premier rang (v7 §7.1). |
| D11 | **Fichier unique vs sous-skills** | v3 : 4 fichiers, chargement à la demande. v4+ : fichier unique (« kills drift between duplicated schemas »). | À rouvrir pour la diffusion : le format skill (SKILL.md court + `references/` chargés à la demande) donne la progressive disclosure de v3 *sans* la dérive de v3, puisqu'il n'y a plus de duplication de schémas. |
| D12 | **Schémas YAML** | v3/v5/v7/v8 : lourds. v9–v13 : zéro. v16–v18 : légers, inline. | v16–v18. Les schémas n'ont de valeur qu'en L2/L3 et en handoff machine. |
| D13 | **Pré-mortem / décomposition auto-critiquée** | v6 §2.1–2.2. Disparu, puis partiellement récupéré comme « framing pass » en v17/v18. | Garder la forme v18 (dégradable, avec la question pré-mortem en une ligne). |

---

## 5. Idées orphelines — bonnes, présentes dans une seule version

À récupérer consciemment ou à écarter consciemment ; aujourd'hui elles sont perdues par accident.

| Idée | Source | Pourquoi ça vaut le coup |
|---|---|---|
| **Chaînage arrière depuis la cible** + tri par précondition + élagage | v11 §4 | La seule méthode de *construction* du plan de tout le corpus. |
| **Classes R/D/J + ledger de coût** | v4 §0, §5 | Seule prise en compte d'un environnement multi-modèles réel (faire brouillonner un petit modèle, juger avec un gros). |
| **Chemin critique & parallélisation** | v3 §5 (sortie §8) | Toute la série planifie en séquence pure. Aucune version postérieure ne parle de parallélisme. |
| **Artefact de plan versionné, append-only, `status` mis à jour en place par les exécuteurs** | v3 `plan-artifact.schema.md` | Seule réponse au « plan vivant pendant l'exécution » exploitable par des agents. |
| **Shape : plan-dominant / learning-dominant** (le ledger devient une file d'expériences) | v7 §1, repris v18 Q3 | Évite de fabriquer un graphe de décisions là où il n'y a que de l'exploration. |
| **`experiment` avec stop condition + decision_unlocked** | v8 §10.4, v10 §2 | Le seul vrai mécanisme pour « je ne peux savoir qu'en faisant ». |
| **Matrice de spawn + bloc de justification de spawn** | v8 §29, v15 §15.2, v18 §5.0 | Rend le coût des agents explicite avant de le payer. |
| **Self-test métrique du skill** (`failure_capture_rate`, `unnecessary_compute_rate`, `false_alarm_rate`…) | v8 §33 | La seule façon de sortir du statut `unproven`. Aucune autre version ne propose de mesure. |
| **Echo-chamber check** en 3 questions | v10 §6.2 | Formulation la plus directe et la plus applicable du problème des erreurs corrélées. |
| **« Le protocole doit passer son propre triage »** | v12 §0 | Garde-fou anti-obésité, à mettre en tête. |
| **Règle des « phantom steps »** (une conséquence mécanique n'est pas une étape) | v13 §5.3 | Formulation la plus nette de `derived`. |
| **Reality gate** : « qu'est-ce qu'un expert sceptique attaquerait en premier ? » | v6 §7.3, v7 §8.3 | Une ligne, coût nul, haute valeur. Disparue après v7. |

---

## 6. Défauts récurrents dans le corpus

1. **Obésité par accrétion.** Chaque version ajoute et n'enlève presque jamais.
   Seules v9 et v14 coupent franchement. Deux cycles complets 280→850 lignes.
2. **Aucun exemple complet.** Sur 8 800 lignes, **pas un seul plan réel de bout en bout**.
   Uniquement des templates vides. C'est vraisemblablement la première cause de
   non-application par un LLM : il n'a rien à imiter.
3. **Auto-contradiction interne non détectée.** v15 embarque deux taxonomies d'actions
   incompatibles ; v7 dit « Silence = approval » et v7 §0 se réclame d'un standard de
   preuve qu'elle viole ; v8 numérote ses sections à partir de §4 et duplique son titre.
4. **Prescriptions non falsifiables.** « Most commitments are compelled »,
   « ship at 80 % », « max 4–5 agents », « ~20 % de l'effort d'exécution » (v3) :
   des chiffres sans source, dans un skill dont la thèse centrale est qu'il faut
   des sources.
5. **Le mot « vendor-neutral » n'est jamais opérationnalisé.** Aucune version ne dit
   ce que devient le protocole sans outils, sans sous-agents, ou sur un petit modèle —
   sauf des mentions de principe (v4 §9, v5 §19, v8 §24, v18 §12).
6. **Confusion skill / doctrine.** Beaucoup de sections sont des essais
   (v5 §0, v8 §31, v8 §32) plutôt que des instructions actionnables. Intéressant
   pour l'auteur, coûteux pour le modèle qui doit l'appliquer.

---

## 7. Trous que *aucune* version ne traite

Ce sont les vrais chantiers pour une version diffusable.

1. **Format de skill.** Aucune n'a de frontmatter (`name`, `description`), aucune
   n'est packagée. Or c'est la **description** qui décide si le skill se charge —
   c'est-à-dire la pièce la plus importante d'un skill diffusé, et elle n'existe pas.
2. **Déclencheurs.** Quand ce skill doit-il s'activer, et quand ne le doit-il pas ?
   Toutes les versions traitent du triage *une fois chargées*, aucune du chargement.
3. **Portabilité réelle.** Un profil « modèle sans outils », un profil « un seul
   contexte », un profil « petit modèle » — annoncés, jamais écrits.
4. **Exemples travaillés.** Au moins un L1 et un L2/L3 complets, avec les erreurs
   typiques montrées à côté du bon usage.
5. **Carte de référence courte.** v7 diagnostique que les protocoles longs sont
   « performés, pas suivis » ; personne ne fournit le recto-verso de 20 lignes
   que le modèle relira réellement en cours de tâche.
6. **Articulation avec les modes plan natifs** (plan mode de l'agent hôte,
   TODO lists, etc.). Jamais mentionnée.
7. **Interaction humaine au-delà du veto.** Restitution, négociation de périmètre,
   désaccord de l'utilisateur avec le plan : rien.
8. **Sortie du statut `unproven`.** v8 §33 donne les métriques ; aucun protocole
   d'évaluation n'existe (jeu de tâches, critères de réussite, comparaison
   avec/sans skill).

---

## 8. Hypothèse de travail pour la suite

Ce que la lecture suggère, à discuter :

- **La base la plus saine est v14** (280 lignes, fusion argumentée, rien de superflu),
  pas v18 — v18 est la meilleure *doctrine*, v14 le meilleur *skill*.
- Y réinjecter précisément : le §4 de **v11** (construction du plan), le framing pass
  dégradable de **v18** §5.1, la robustesse de **v18** §7.3, le reality gate de **v6/v7**,
  le shape de **v7/v18**.
- Traiter la longueur comme une contrainte dure, pas comme une conséquence : fixer un
  budget (p. ex. SKILL.md ≤ 150 lignes) et pousser le reste en `references/` chargées
  à la demande — ce qui répond à D11 sans rouvrir le problème de dérive de v3.
- Ajouter ce qui manque partout : frontmatter + description déclenchante, un exemple
  complet, une carte de référence courte, un profil de dégradation explicite.
- Garder `unproven` en tête de fichier, et écrire enfin le protocole d'évaluation.

Questions ouvertes à trancher avant d'écrire : voir §4 (D2, D6, D11) et §7 (1, 3, 8).
