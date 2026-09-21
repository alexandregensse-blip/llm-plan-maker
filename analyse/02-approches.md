# plan-suite — recensement des approches

Pour chaque question que doit trancher un skill de planification, les réponses
réellement présentes dans les 16 versions : comment elles marchent, d'où elles
viennent, ce qu'elles coûtent, et où le corpus se contredit.

Document descriptif. Aucune recommandation.

---

# A. Décider combien de travail la tâche mérite

## A1 — Le calibrage de la profondeur

**A1.1 — Score arithmétique** · v3 §0
`PCS = O + 2·B + 3·I + D + S`, avec des seuils vers L0–L4. Les coefficients ne
sont justifiés nulle part. v4 le supprime en l'expliquant : *« removes false
precision, same routing power »*.

**A1.2 — Table de signaux qualitative** · v4 §1, v5 §2, v6 §1, v7 §1
Des lignes « signal présent → profondeur », et une trace écrite en une ligne :
`depth=L2 because: <signaux observables>`. Pas de calcul, une décision auditable.

**A1.3 — Questionnaire de triage** · v6 §1 (5 questions), v7 §1 (6), v8 §6 (7)
On interroge explicitement : y a-t-il un engagement ? est-ce réversible ?
l'environnement est-il connu ? l'utilisateur veut-il un plan ou une action ?
quelle conséquence si c'est faux ? combien d'invocations isolées sont possibles ?

**A1.4 — Une seule question** · v9 §2, v10 §1, v13 §1
*« L'action suivante est-elle irréversible ou matériellement conséquente ? »*
Non → agis. Oui → protocole. Binaire, aucune échelle.

**A1.5 — Deux questions** · v12 §1, v14 §1, v15 §1, v16–v18 §1
Réversibilité, **puis territoire**. Voir A2.

*Règle stable partout où une échelle existe* : en cas de doute entre L1 et L2,
prendre L1 — sauf si l'action est irréversible.

## A2 — La question du territoire

Apparue en v12 §1, conservée jusqu'à v18. Absente de v3 à v11.

> *« Known path »* — runbook, API documentée, procédure déjà exécutée.
> L'environnement est prévisible : on planifie d'avance sur plusieurs étapes.
> *« Frontier work »* — l'issue de l'étape N reconfigure ce qu'est l'étape N+1.
> On ne planifie que jusqu'à la limite.

v12 §1 en fait un reproche explicite au reste du corpus : *« Most planning
skills silently assume frontier work everywhere. That forces re-discovery of
known paths and wastes compute. »*

## A3 — Le budget et sa dégradation

**A3.1 — Classes de modèles et registre de coût** · v4 §0, §5
Trois classes définies par capacité et non par fournisseur : Router (le moins
cher), Drafter (moyen), Judge (le plus fort). Règles : ne jamais employer le
Judge là où le Drafter suffit ; ne jamais laisser une instance être le
relecteur indépendant de sa propre sortie. Budgets par profondeur en nombre
d'invocations par classe. **Unique dans le corpus.**

**A3.2 — Ordre de dégradation** · v5 §13, v6 §9.3, v7 §11, v8 §24, v18 §12
Moins de candidats → moins de lentilles → moins de prose. Avec un plancher :
ne jamais retirer la provenance des affirmations porteuses, l'attaque adverse
sur l'irréversible, le veto utilisateur, l'incertitude visible.

**A3.3 — Mono-modèle** · v4 §9, v5 §19, v8 §24, v18 §12
La structure survit, les prétentions d'indépendance rétrécissent. v5 impose
d'étiqueter `independence=simulated` ; v18 impose `staged` partout.

---

# B. Décider de quoi un plan est fait

## B1 — Objectifs → options → actions · v3 §1, v5, v6

```
besoin → états (actuel / cible) → garde-fous → objectifs (avec critères
d'acceptation) → options (stratégies distinctes) → actions
```
Le plan répond à *que faut-il obtenir, par quelle stratégie*.
v3 §5 en tire un gabarit de sortie à 11 sections, v5 §16 à 15 sections.

## B2 — Engagements et dérivés · v7 §2, v8 §8

Un **engagement** est un point où le plan ferme des options ou consomme des
ressources : action irréversible ou coûteuse, adoption d'une architecture ou
d'une dépendance, dépendance externe, expérience qui dépense pour lever une
inconnue. Tout le reste est **dérivé** et hérite de sa légitimité.

v7 Annexe B justifie le passage : *« Most "decisions" are compelled by evidence,
or are experiment queues, not decision points. The artifact should match the work. »*

## B3 — États et transitions · v9 à v18

```
état actuel vérifié → transitions observables → état cible falsifiable
```
Chaque étape porte un attendu observable et un filet. Le plan répond à
*comment passe-t-on d'ici à là, et comment le sait-on*.
v13 §0 : *« Planning is not a document; it is a state machine. »*

## B4 — Le graphe de décisions · v5 §1, v6 §2

Variante de B1 : on construit d'abord le graphe des décisions, on les résout
une par une, et le plan est la projection des décisions résolues. v5 §0.1 :
*« A plan is composed of decision units. »*

## B5 — La distinction des niveaux · v3, en-tête — et nulle part ailleurs

> *« Do not confuse: request ≠ need ≠ objective ≠ option ≠ implementation ≠
> action ≠ outcome. »*

Cette phrase disparaît dès v4 et ne réapparaît dans aucune version.

## B6 — Le typage des étapes

Deux taxonomies incompatibles, qui cohabitent dans v15 (§12 contre §13.1) :

| | Types | Où |
|---|---|---|
| épistémique | `discovery · commitment · derived · experiment` | v10 §2, v11 §3, v16–v18 |
| fonctionnelle | `discovery · change · validation · rollback · ask_user · branch · handoff` | v5 §11, v6 §7.1, v7 §8.1, v15 §12 |

## B7 — Le traitement des indéterminations

**B7.1 — Branches conditionnelles** · v3 §4
Plafonnées à 2 niveaux, seulement là où la condition est décisionnellement
pertinente. Chaque branche = déclencheur, preuve requise, chemin, repli.
v3 préfère explicitement `Hypothèse A → chemin A` à une question bloquante.
Disparaît après v3.

**B7.2 — Troncature à la frontière** · v9 à v18
Le plan s'arrête à l'étape dont l'issue reconfigure la suite ; ce qui suit est
une question ouverte nommée. Règle récurrente : *« si l'étape 5 dépend de la
sortie non observée de l'étape 2, supprimez 3 à 5 »*.

**B7.3 — Dette de planification** · v6 §9.2, v7 §8.5, v12 §11, v14 §9, v16–18 §11
On livre incomplet si le manquant est tenu par un gate, un moniteur ou une
expérience réversible, et on écrit ce qui manque et comment ça se résout.
v8 §32 la retire explicitement de la liste des règles générales.

---

# C. Décider ce qui compte comme un fait

## C1 — Les formes

**C1.1 — Étiquettes épistémiques** · v3 §2
Chaque énoncé porteur est marqué `Known | Inferred | Assumed | Unknown |
Conditional`. *« Ne jamais promouvoir Assumed en Known silencieusement. »*

**C1.2 — Fiches de preuve** · v5 §5.1, v6 §3.2, v7 §3.3, v8 §13.1, v15 §4.2, v16–18 §4.1
```yaml
id · claim · status · source · locator · limitations
+ checked_at / ttl        (v7, v15, v16-v18)
+ freshness               (v8)
+ independent_verifiers   (v5)
```

**C1.3 — Une règle, pas de fiche** · v9 à v13
« Verified now » = ce que j'ai effectivement regardé. Pas de schéma, pas
d'identifiants, pas de statut.

## C2 — Les règles de preuve, communes à v5–v18

- Une citation n'est pas une preuve si la source ne soutient pas l'affirmation.
- La déclaration d'un agent n'est pas une preuve.
- Trois agents citant la même source = **une** preuve.
- Un calcul doit exposer entrées et formule pour être recalculable.
- Impossible d'inspecter → `unproven`. Ne pas blanchir en fait.
- Preuves contradictoires → `contested`. Ne pas moyenner, ne pas choisir la
  plus commode.
- Une conclusion ne vaut pas plus que sa prémisse porteuse la plus faible.

## C3 — Le budget de preuves

v6 §3.1, v7 §3.2, v15/v16/v17/v18 §4.1 : un plafond d'items par engagement
porteur, croissant avec la profondeur (0–1 / ≤2 / ≤4). Plafond atteint sans
résolution → marquer un trou, puis brancher, gater ou escalader.

v8 §32 supprime les compteurs fixes : *« These may still be useful local
heuristics… but they should not be mistaken for general planning laws. »*
v8 §13.5 les remplace par trois conditions d'arrêt qualitatives : décision
stable, incertitude contenue, valeur marginale inférieure au coût.

## C4 — La péremption

**TTL** · v7 §3.3 → v18 §2 : durée par défaut « cette session », re-vérifier
au moment d'exécuter, un re-contrôle qui donne une réponse différente est un
déclencheur de replanification.

**Volatilité** · v8 §13.4 : refuse explicitement un TTL universel et classe
`stable | low_volatility | volatile | unknown` — *« A source's age matters only
relative to the claim. »*

## C5 — La chambre d'écho

v10 §6.2, formulation la plus directe du corpus. Avant de traiter un fait
porteur comme vérifié :
- vient-il du raisonnement qui s'apprête à agir dessus ?
- les « deux sources » partagent-elles une origine, un corpus, une famille de
  modèles ?
- la « preuve » est-elle du texte de modèle qui reformule l'affirmation ?

Une réponse positive → le fait redescend à non vérifié.

---

# D. Décider comment produire et confronter des options

## D1 — Les formes de génération

**D1.1 — Ensemble de rédacteurs** · v4 §2
N=3 rédacteurs en parallèle, isolés, **même brief**, avec des `style_seed`
différents (« optimise la vitesse » / « la réversibilité » / « la simplicité »),
puis consolidation par un juge. Motif donné : des briefs identiques sur une
même famille de modèles convergent — *mode collapse*.
**Seule version où la concurrence porte sur des plans entiers.**

**D1.2 — Candidats par décision** · v5 §6, v6 §4, v7 §4, v15 §5, v16–18 §5
2 candidats par décision porteuse (3 si le choix est serré), brief normalisé
identique, diversité par **lentille de méthode** et non par formulation :
chemin le plus simple / contraintes d'abord / réversibilité d'abord /
test d'abord / architecture alternative.
v5 §22 justifie l'abandon de D1.1 : *« A plan can agree while hiding one
critical unresolved decision. »*

**D1.3 — Le contrôle de compulsion, en amont** · v7 §3.1 → v18 §3.1
> *« Les faits vérifiés et les contraintes dures laissent-ils exactement un
> seul chemin viable ? »*

Oui → résolu, zéro candidat. Non par fait manquant → action de découverte.
Non par ≥2 options → candidats. Non par préférence → utilisateur.
Défaut affiché : **zéro candidat**. v12 §4 : *« This is the largest compute
saver in the skill, and the check most often skipped — because generating
options feels like rigor. It isn't. »*

**D1.4 — Aucune génération** · v9 à v13
Pas de candidats. L'exécution tranche : on prend la plus petite action
observable et on lit le résultat.

**D1.5 — L'explorateur / la passe de cadrage** · v8 §11.1, v17 §5.1, v18 §5.1
Un agent dont la seule tâche est d'attaquer le cadrage avant qu'on résolve
quoi que ce soit dedans : approches matériellement différentes, hypothèses
manquantes, dépendances cachées, reformulations du problème, expérience pas
chère qui effondrerait la plus grosse incertitude.
v18 §5.1 en fait trois formes dégradables : agent isolé → passe `staged` →
liste de questions écrite, étiquetée `staged-weak`.

**D1.6 — L'exploration parallèle par domaine** · v3 `plan-research` §1, R1
Un agent par domaine d'investigation indépendant, en parallèle. Motif :
vitesse en temps réel, pas de contamination croisée. Plafond 4–5 agents.
**Disparaît après v3.**

## D2 — Les échelles d'indépendance

| Échelle | Niveaux | Où |
|---|---|---|
| I0–I4 | auto-contrôle / même modèle voyant le candidat / candidat propre en aveugle / vérification de preuve indépendante / méthode distincte et aveugle | v5 §0.3 |
| 4 modes | `self` / `simulated` / `isolated` / `external` | v6 §4.1 |
| 3 modes | `staged` / `isolated` / `external` | v7 §4.1 → v18 §5.5 |
| 3 champs | information `none/partial/isolated` · méthode `same/meaningfully_different` · sources `shared/partially/independent` | v8 §12 |

*Règles communes* : ne jamais promouvoir une étiquette · la température n'est
pas de l'indépendance · l'auto-critique n'est pas une revue · deux modèles de
la même famille partagent leurs angles morts.

## D3 — L'hygiène d'information

v5 §18, v7 §4.2, v8 §12, v15 §5.2, v16–18 §5.4

- Générer avant de lire le plaidoyer d'une option concurrente.
- Ne jamais demander d'« améliorer le candidat A » avant génération indépendante.
- Ne jamais montrer à l'attaquant le plaidoyer du candidat — l'action et les
  faits, rien d'autre.
- Ne jamais laisser le modèle le plus fort définir l'espace des options avant
  que les candidats ne soient produits (v5).
- Ne jamais appeler `isolated` une passe `staged`.

## D4 — Quand ouvrir un agent

**D4.1 — Matrice de déclencheurs** · v3 `plan-research` §1, v8 §29, v15 §15.1
Une ligne par situation → rôle → motif. Rôles nommés dans le corpus :
Explorer, Verifier, Specialist, Risk attacker, Transition attacker, Integrator,
Candidate.

**D4.2 — Bloc de justification** · v8 §29, v15 §15.2, v18 §5.0
```yaml
purpose · question · why_current_context_is_insufficient
expected_information_gain · independence · stop_condition
```
Ne peut pas le remplir → n'ouvre pas l'agent.

**D4.3 — Les motifs légitimes** · v17 §5, v18 §5
Trois et trois seulement : **innovation** (un cadrage que personne n'a proposé),
**confirmation aveugle** (vérification indépendante d'une affirmation),
**diversité d'options** (méthodes réellement différentes).
Tout le reste — conséquences mécaniques, passes de « revue » sans lentille
propre, second avis sur une réponse forcée — est nommé *ceremony* et refusé.

**D4.4 — La règle d'arrêt** · v8 Annexe D, v14 §3.4, v17 §5.6
> *« Could this agent change what we do, or merely make the current story sound
> more convincing? »*

**D4.5 — Quand ne pas ouvrir d'agent** · v3 `plan-research` §2
Tâche triviale ou mono-domaine · sous-problème trop couplé pour être cadré
séparément · coût d'orchestration ≥ valeur attendue · l'agent n'a accès à rien
que l'appelant n'ait déjà.

---

# E. Décider comment attaquer

## E1 — Checklist adverse · v3 `plan-review` §2
Couverture objectif→action→critère · hypothèses cachées · contradictions ·
ordonnancement et position des points de validation · chemins d'échec ·
effets de bord · invariants · faisabilité · *outcome check* (le plan
résout-il le besoin, ou exécute-t-il les activités demandées ?).

## E2 — Lentilles de risque · v5 §7, v6 §5.2, v7 §5, v15 §6.2, v16–18 §6.1
Opérationnelle · environnementale · adverse · invariant · transition ·
dépendance/chaîne d'approvisionnement · humaine/processus · cohérence des données.

Deux doctrines de sélection : **par profondeur** (v5, v6 : 2 lentilles en L3)
contre **par surface de défaillance réelle** (v7 §5 : *« Choose lenses by what
can break this commitment, not by depth level »*, repris v15–v18).

## E3 — Le prompt d'attaquant · v6 §5.1, v7 A.2, v8 B.3, v15 A.3, v16–18 A.4
Huit questions stables : qu'est-ce qui peut faire échouer · quelle hypothèse est
la plus probablement fausse · que se passe-t-il en complétion partielle · le
retour arrière peut-il échouer · quel est le premier signal observable · cela
crée-t-il un état irréversible ou en cascade · un chemin viole-t-il une
contrainte dure · que ferait un environnement hostile.

## E4 — Simulation de transitions · v3 §3, v5 §12, v7 §8.4, v8 §20, v18 §6.2
```
S0 --A1--> S1 --A2--> S2
     |           |
   panne       panne
     v           v
 récupération récupération
```
Pour chaque transition matérielle : préconditions, post-condition, injection
d'une panne plausible, état de récupération, validité de l'action suivante, et
vérifier qu'une mitigation antérieure n'a pas créé une violation d'invariant
plus loin. v3 et v5 le limitent aux transitions coûteuses, irréversibles ou
inédites.

## E5 — Pré-mortem · v6 §2.2, v7 §2.2, repris en une ligne v18 §5.1
> *« Six mois ont passé et ce plan a échoué gravement. Que s'est-il passé ? »*
Un paragraphe, avant de résoudre quoi que ce soit, gardé comme entrée de
l'analyse de risque.

## E6 — Reality gate · v6 §7.3, v7 §8.3
> *« Un expert sceptique lit ce plan — qu'attaque-t-il en premier ? »*
Traiter les une ou deux premières objections, ou escalader. Disparaît après v7.

## E7 — Balayage de dangers avant décision · v8 §14
Un analyste qui ne choisit pas et ne défend rien, et qui cherche : le fait
manquant le plus dangereux, les hypothèses les plus probablement fausses, les
dépendances cachées, les transitions irréversibles, **les modes de défaillance
communs à toutes les options évidentes**, et les conditions sous lesquelles le
problème a été mal cadré. Son résultat peut rouvrir la carte de planification.

## E8 — Déclencheurs de soin · v10 §5, v11 §5, v12 §6, v14 §6
Au lieu d'attaquer systématiquement, une table trigger → outil :
irréversibilité → une attaque indépendante · compromis dépendant d'une
préférence → utilisateur · hypothèse porteuse non vérifiée → convertir en
découverte · « confirmation » de même origine → contrôle de chambre d'écho ·
cascade → attaque avec lentille de transition.
v10 §5 : *« Do not fire triggers that do not apply. Discipline spent on
reversible, preference-neutral, single-step actions is theater. »*

## E9 — Règles communes à toutes les formes
- Une mitigation n'est pas une preuve que le risque sous-jacent est petit.
- Un chemin qui atteint la cible en violant une contrainte dure est **invalide**,
  pas « risqué ».
- L'attaquant ne rend pas un verdict sur le plan : il rend une liste de modes de
  défaillance à contenir ou à accepter.

---

# F. Décider comment trancher

## F1 — Le juge consolidateur · v4 §3
Reçoit le brief et les candidats, **et rien d'autre** — ni chaînes de
raisonnement, ni consolidations antérieures. Protocole en six temps : extraire
toute affirmation distincte → audit de preuve → attaque → **fusion décision par
décision** → reconstruction et contrôle de cohérence globale → rattachement des
preuves. Produit un mémo de consolidation : ce qui est gardé et d'où, ce qui est
écarté et par quelle preuve, ce qui reste non prouvé.

## F2 — Résolution par décision, avec précédence
v5 §9.1, v6 §6.1, v7 §6.1, v15 §7.1, v16–18 §7.1 — identique partout :

1. contraintes dures et invariants
2. observations vérifiées et preuves primaires
3. test ou calcul démontré
4. raisonnement indépendamment étayé
5. réversibilité, quand les preuves ne départagent pas
6. simplicité, si toujours à égalité

*« Never pick a winning plan wholesale. »*

## F3 — Les statuts de résolution

v5 §9.2 → v18 §7.4 : `resolved` · `resolved-with-tradeoff` · `branch` ·
`gated` · `unresolved` · `invalid`.
v8 §17 a sa propre liste : `constrained` · `supported` · `preference-dependent`
· `experiment-gated` · `branch` · `unresolved` · `invalid`.

*« Never force resolved to make the output look complete. »*

## F4 — Confiance calibrée et règles d'expédition · v7 §6.2–6.3, v15 §7.2–7.3, v16–18 §7.2

| Confiance | Réversible | Conséquence | Règle |
|---|---|---|---|
| haute | — | — | livrer |
| moyenne | oui | — | livrer avec surveillance |
| moyenne | non | matérielle | gate ou veto utilisateur |
| basse | oui | triviale | livrer, visiblement signalé |
| basse | non | — | brancher, découvrir ou escalader — jamais livrer |

## F5 — Robustesse · v8 §18, v18 §7.3
> *« Quel fait non résolu et plausible pourrait faire basculer cet engagement ? »*

`robust` · `sensitive` (nommer les faits ; ils deviennent des déclencheurs de
replanification) · `contained` (tenu par un gate, un test, un retour arrière).
v8 : *« This is more useful than a generic confidence label. »*

## F6 — Les interdits communs
- **Pas de vote majoritaire.** Le nombre d'agents n'est pas une preuve. Un
  candidat minoritaire mieux étayé bat une majorité moins étayée.
- **Contrôle d'erreurs corrélées.** Les candidats ont-ils emprunté des chemins
  de preuve réellement distincts ? Partagent-ils une hypothèse, une source, une
  famille de modèles ? Si oui, ce point partagé reste non vérifié quel que soit
  le nombre d'agents qui l'ont répété.
- **Pas de synthèse silencieuse.** Toute action du plan final qu'aucun candidat
  n'a proposée est marquée `derived-from: [D#, E#, contrainte]`. Si la
  dérivation n'est pas évidente, c'est une nouvelle décision.
- **Convergence ≠ soutien.** v5 §15 : un plan peut être convergent et faiblement
  étayé, ou fortement étayé et porteur d'un vrai compromis non résolu. Les deux
  états se rapportent séparément.

---

# G. Décider comment impliquer l'utilisateur

**G1 — L'éviter par construction** · v3 §2, §4
Les inconnues deviennent des actions de découverte, pas des questions. Si
vraiment bloquant, demander **une fois**, avec les chemins par défaut proposés
pour chaque réponse. Préférer `Hypothèse A → chemin A` à une question bloquante.

**G2 — L'utilisateur comme oracle** · v7 §7, v10 §6.3, v15 §11, v16–18 §8
*« The cheapest high-bandwidth oracle in the environment. »* `ask_user` devient
un type d'action de premier rang, avec `recommended_default` et un champ `cost`
(ce que coûte une mauvaise supposition contre la latence de la question).
Règles : grouper, jamais en série · plafond de 2 questions par phase · ne jamais
demander ce qui est moins cher à vérifier par inspection, test ou recherche ·
toujours fournir un défaut pour que le plan reste exécutable sans réponse.

**G3 — Le veto de compromis** · v7 §7.2, v10 §6.3, v15 §11.1, v16–18 §8
Avant qu'un engagement irréversible ne s'exécute, chaque compromis matériel
sort en une ligne :
> `VETO ? A : <compromis> contre B : <compromis>. Je pars sur A. Réponds
> seulement si tu veux B.`

**G4 — Le schéma de gate** · v8 §19
```yaml
decision · tradeoff · options · why_the_user_decides
default_authorized · required_before
```

**G5 — Le silence — contradiction frontale du corpus**
v7 §7.2 : *« Silence = approval. This is the highest-ROI safety mechanism in
the skill. »*
v8 I9, repris v10 à v18 : *« Silence is not authorization »* — sauf délégation
explicite et préalable pour cette classe de décision. Sans délégation et sans
utilisateur joignable, l'action est gatée. Ne jamais inventer une approbation.

---

# H. Décider comment contenir le risque

## H1 — Le contrat d'action, forme longue · v3 §3, v5 §11, v6 §7.1, v7 §8.1, v8 §21, v15 §12
```yaml
id · origine (décision/preuve/attaque) · type · objectif · préconditions
execution · expected_output · validation · failure_signals
rollback (ou « impossible » + conséquence) · provenance · effort
+ replan_trigger   (v8)
```

## H2 — Le contrat minimal · v9 §3C, v10 §3, v11 §3, v12 §3, v16–18 §9.4
```
Intent · Expected · Containment
```
Trois lignes, pas plus. Une découverte n'a besoin que d'Intent et Expected — son
containment est qu'elle ne change rien.

## H3 — Les règles communes
- La validation est définie **sur** l'action, pas reportée à la fin.
- *« Check it works »* n'est pas une validation. *« GET /health renvoie 200 en
  moins de 2 s »* en est une.
- Le retour arrière est pensé **avant** l'exécution.
- Retour arrière impossible et impact élevé → gate explicite.
- Une action incapable de répondre à « quel objectif ? comment validée ? et si
  elle échoue ? » est redessinée ou coupée.
- Les conséquences mécaniques d'une étape font partie de sa validation, pas
  d'étapes séparées (v13 §5.3 : *« No Phantom Steps »*).

## H4 — L'expérience bornée · v8 §10.4, v10 §2, v11 §3
Quand l'incertitude ne se lève qu'en faisant :
```yaml
question · action bornée · coût · signal de succès
condition d'arrêt · pourquoi c'est assez sûr · décision débloquée
```

---

# I. Décider ce qu'on livre

| Forme | Où | Contenu |
|---|---|---|
| Gabarit long | v3 §5 (11 sections), v5 §16 (15 sections) | problème, objectifs, contraintes, options, architecture, plan, points de décision, chemin critique, validation, risques, travaux futurs |
| Plan d'abord + annexe en prose | v6 §10 | plan exécutable, puis appendice d'audit : décisions, preuves, note d'indépendance, dette |
| Plan + sidecar structuré | v3 `plan-artifact`, v7 §12 | v7 : *« Prose appendices are never re-read; a YAML ledger is cheap to emit and cheap to audit »* |
| Plan d'une page | v10 §8, v11 §7, v12 §9, v16–18 §9.3 | cible, invariants, état vérifié, questions ouvertes, étapes typées, gates, risque résiduel |
| Rien par défaut | v9 §5, v13 §3 | l'état vivant et le contrat suivant *sont* le plan ; un artefact seulement sur demande ou pour un passage de relais |

*Règle commune à v5–v8* : sortie proportionnelle au travail, et **pas de faux
journal d'audit pour L0/L1**.

**Le plan comme objet durable** · v3 `plan-artifact` uniquement
Identifiants stables, numéro de version, historique en ajout seul, les
exécutants mettent à jour `status` et `result` **en place**, toute modification
structurelle incrémente la version et redéclenche les relecteurs.

---

# J. Décider quand s'arrêter

**J1 — Liste de conditions** · v3 §7
Besoin et cible explicites · objectifs requis avec critères · ensemble
d'implémentations faisable · dépendances respectées · chemins d'échec
considérés · chaque objectif requis a un chemin de validation · incertitude
résiduelle énoncée. Plus une règle non mesurable : *« si la planification
dépasse ~20 % de l'effort d'exécution estimé, livrez »*.

**J2 — Plafonds et convergence** · v4 §5
Plafonds d'invocations par profondeur, et arrêt si une passe de consolidation
change moins de 10 % du plan précédent.

**J3 — Stabilité de décision** · v5 §13, v6 §9.1, v7 §11, v8 §23
S'arrêter quand un candidat de plus ne peut plus changer une décision · quand
la confrontation ne fait que reformuler · quand l'incertitude restante ne peut
pas être réduite économiquement et est tenue par un gate ou une expérience
réversible · quand le budget est épuisé.
v8 §23 nomme le critère : *« decision stability plus safe containment, not
document completeness »*, et liste les mauvais motifs d'arrêt : un quota
atteint, assez d'agents d'accord, le document « a l'air complet », la sortie est
devenue longue.

**J4 — Quand escalader plutôt que deviner** · v5 §13, v6 §9.3, v7 §11
Preuves réellement contestées et décisives · hypothèse critique intestable ·
contrainte dure en conflit avec le résultat demandé · retour arrière indisponible
sur une action à fort impact · arbitrage dépendant de priorités non inférables.

**J5 — Quand le skill ne doit pas s'appliquer** · v6 §12, v10 §9, v12 §12, v13 §6, v16–18 §12
Question, explication, action triviale et réversible · aucun engagement porteur ·
l'utilisateur veut de la vitesse et tout est réversible · le protocole coûterait
plus que la valeur du plan · **l'environnement n'offre aucune observation contre
laquelle valider** — le dire, plutôt que planifier contre sa propre imagination.

> *« A skill that never says "I am not the right tool" is dangerous. »*

---

# K. Ce que le corpus prévoit après la livraison

Hors du périmètre retenu, recensé pour mémoire.

- **Passage de relais** · v5 §17, v7 §10, v8 §22, v16–18 §10.3 — tranche de plan,
  contraintes et invariants en entier, état validé courant, preuves nécessaires à
  cette tranche, questions ouvertes, déclencheurs de replanification, pointeurs
  vers le reste. *« Nothing load-bearing lives in memory alone. »*
- **Digest de phase** · v4 §7 → v18 §10.2 — une ligne :
  `done | failed | new unknowns | state delta | next gate`.
- **Réparation locale contre replanification globale** · v4 §7, v5 §17, v8 §22 —
  réparer le plus petit sous-arbre affecté ; ne revalider que la branche réparée.
- **Déclencheurs de replanification globale** — invariant violé · fait porteur
  faux ou périmé · environnement matériellement changé · échecs locaux répétés
  (c'est le modèle du monde qui est faux, pas l'étape) · cible ou contrainte dure
  changée.

---

# L. Ce qui n'existe nulle part dans le corpus

- Un en-tête de skill (`name`, `description`) — donc aucune règle de chargement.
- Un seul plan complet donné en exemple, sur 8 800 lignes.
- Une opérationnalisation du « vendor-neutral » : aucun profil sans outils, sans
  sous-agents, ou pour petit modèle.
- Une carte de référence courte, alors que v7 Annexe B diagnostique que
  *« long protocols get performed, not followed »*.
- Un protocole de mesure, alors que v8 §33 en liste les métriques souhaitables.
- Une articulation avec les modes plan natifs des agents hôtes.
- Tout ce qui concerne la collaboration avec l'humain au-delà du veto :
  restitution, négociation de périmètre, désaccord sur le plan.
- Le chemin critique et la parallélisation : présents en v3 §5, jamais repris.
