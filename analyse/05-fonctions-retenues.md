# plan-suite — fonctions retenues

Journal de validation, axe par axe. Ce qui est gardé, ce qui est écarté, et les
reformulations imposées en cours de revue.

---

# GROUPE 1 — SE DÉTERMINER

## Axe 1.1 · Applicabilité
- ~~1.1.1 Activation~~ — **écarté.** Le skill est invoqué explicitement par
  l'utilisateur (D-09), il n'a pas à se convoquer. Reste à écrire une
  `description` dans l'en-tête du paquet : attribut du fichier, pas fonction.
- ~~1.1.2 Jugement d'opportunité~~ — **écarté.** Le skill ne juge pas si la
  demande mérite un plan : l'utilisateur a demandé un plan.
- **1.1.3 Déclinaison** — gardé. Savoir énoncer « il n'y a pas de problème de
  planification ici » et s'arrêter.

## Axe 1.2 · Reconnaissance du terrain
- **1.2.1 Capacités disponibles** — gardé.
- **1.2.2 Forme du travail** — gardé.
- **1.2.3 Territoire** — gardé.

> **Contrainte transverse** — ce qui est établi ici ne doit pas être refait par
> chaque agent ouvert ensuite. Le résultat voyage dans le brief (axe 7.2).

## Axe 1.3 · Allocation de l'effort
- **1.3.1 Exigence de la tâche** — gardé. Quelles techniques, parmi celles
  autorisées, méritent d'être déployées ici.
- **1.3.2 Autorisation disponible** — gardé. Ce que la configuration permet.
  *Piste d'empaquetage retenue : variable d'environnement, ou skills séparés par
  tier, de sorte qu'un tier faible ne charge pas les techniques d'un tier élevé.*
- ~~1.3.3 Conflit exigence / autorisation~~ — **écarté.** Notion importée à tort
  du corpus, où le skill exécutait et devait protéger un plancher de sûreté.
  Ici rien n'est irréversible au moment où le skill travaille : le niveau
  d'effort change *comment* on planifie, jamais *si* on peut planifier.
  **Le « plancher » de D-05 tombe avec elle.**
- ~~1.3.4 Budget de planification~~ — **écarté.** Le modèle n'estime aucun coût.
  La configuration fixe un niveau d'effort, pas un niveau de dépense.

## ~~Axe 1.4 · Retour sur soi~~ — **axe supprimé.**
L'auto-évaluation par métriques est abandonnée. Le besoin d'itération est
couvert autrement, par l'entrée du skill sur un plan existant (voir N-01).

---

# GROUPE 2 — ÉTABLIR LE PROBLÈME

## Axe 2.1 · Élucidation
- **2.1.1 Séparation demande / besoin** — gardé.
- **2.1.2 Détection de solution imposée** — gardé.
- ~~2.1.3 Motif et coût de l'inaction~~ — **écarté.** Le skill ne juge pas le
  besoin de l'utilisateur. Si la demande ne sert à rien, cela se verra dans la
  distinction demande / besoin.

## Axe 2.2 · Définition de la réussite
- **2.2.1 Formulation de la cible** — gardé.
- **2.2.2 Critères d'acceptation** — gardé.
- **2.2.3 Fidélité cible ↔ besoin** — gardé.
- **2.2.4 Objectifs multiples** — gardé, **reformulé** : la priorité *ordonne*,
  elle n'écarte pas. Plusieurs besoins veulent dire qu'on les remplit tous ; ce
  n'est pas au skill de décider lesquels traiter.
- **2.2.5 Conflits d'objectifs** — gardé, **reformulé** : un conflit n'est pas un
  arbitrage à rendre, c'est un symptôme. Soit le besoin est mal compris, soit il
  heurte un besoin exprimé avant l'invocation du skill. Dans les deux cas, on
  remonte à l'utilisateur.
- ~~2.2.6 Formulation de l'intention~~ — **écarté** *(lecture à confirmer)*.
  Un plan bien fait n'a pas à prévoir la dérive ; l'improvisation est interdite
  à l'exécution ; un échec renvoie à la phase de plan.

> **Contrainte transverse** — un agent qui juge reçoit les critères
> d'acceptation **et** le besoin. Un juge qui n'a que les critères optimise les
> critères : c'est précisément le défaut que 2.2.3 existe pour attraper.

## Axe 2.3 · Délimitation
- **2.3.1 Périmètre** — gardé.
- **2.3.2 Refus des ajouts silencieux** — gardé, **déplacé** : les objectifs
  inutiles ou non alignés se voient à la confrontation du plan avec la demande.
  C'est un contrôle de sortie (groupe 8), pas une vigilance de cadrage.
- ~~2.3.3 Négociation du périmètre~~ — **écarté.** On ne négocie pas un périmètre
  demandé par l'utilisateur, et on ne refuse jamais pour cause de taille. On
  peut demander de préciser un besoin. Voir N-02.

## Axe 2.4 · Garde-fous
- **2.4.1 Contraintes dures** — gardé.
- **2.4.2 Invariants** — gardé.
- **2.4.3 Préférences** — gardé.
- **2.4.4 Exigences transverses** — gardé, **reformulé** : détecter une dimension
  tacite (données de santé ⇒ sécurisation) **ne donne pas le droit de l'imposer**.
  Faire remonter et demander, jamais décider seul — sans quoi le skill fabrique
  des contraintes que personne n'a exprimées.
- **2.4.5 Ressources et fenêtres** — gardé, **précisé** : il s'agit des ressources
  de l'**exécution** du plan. Pour planifier, on ne se bride jamais.
- **2.4.6 Dépendances externes** — gardé.
- **2.4.7 Obligations de conformité** — gardé, même réserve que 2.4.4 : on
  signale et on demande, on n'impose pas.

## ~~Axe 2.5 · Environnement humain~~ — **axe supprimé.**
Ni axe ni fonctions. Les acteurs humains, quand ils comptent, apparaissent
comme dépendances externes (2.4.6) ou obligations (2.4.7). Le reste est du
remplissage sur la grande majorité des tâches.

## Axe 2.6 · Mise en cause du cadrage
- **2.6.1 Contestation de l'énoncé** — gardé.
- **2.6.2 Hypothèses importées** — gardé.
- **2.6.3 Approches non envisagées** — gardé.
- **2.6.4 Recherche d'antécédents** — **ajouté.** Chercher ce qui a déjà été fait
  pour des besoins similaires : en local, dans le dépôt, en ligne. Sert la
  recherche d'approches, même si l'acte relève de l'investigation.

---

# GROUPE 3 — ÉTABLIR LE RÉEL

## Axe 3.1 · État des lieux
- **3.1.1 État actuel** — gardé.
- **3.1.2 Observé / supposé** — gardé.

## Axe 3.2 · Cartographie de l'incertitude
- **3.2.1 Recensement des inconnues** — gardé.
- **3.2.2 Matérialité** — gardé.
- **3.2.3 Priorisation de l'enquête** — gardé, **reformulé** : on ordonne, on
  n'écarte pas. Tout est traité dans tous les cas.
- ~~3.2.4 Mise à l'écart~~ — **dissous dans 3.2.2** *(lecture à confirmer)*.
  Une inconnue sans effet n'avait pas à figurer sur la liste.
- **3.2.5 Classement construction / exécution** — **ajouté**, même si la
  distinction est implicite. Deux sortes d'inconnues : celles qui bloquent
  l'écriture du plan, à résoudre avant de rédiger, et celles qui ne se
  révèlent qu'à l'exécution, que le plan doit absorber par une branche.
  Aucune des 16 versions ne fait cette distinction.

## Axe 3.3 · Investigation
- **3.3.1 Choix du moyen** — gardé.
- **3.3.2 Conduite des vérifications** — gardé.
- **3.3.3 Résolution par l'action** — gardé.
- **3.3.4 Parallélisation de l'enquête** — gardé, **précisé** : ce n'est qu'une
  instance. Ouvrir plusieurs agents pour obtenir plusieurs avis est un
  mécanisme transverse qui revient partout dans le skill ; il vit à l'axe 7.2,
  3.3.4 n'en est que l'application à l'enquête.
- **3.3.5 Mise en pause de l'enquête** — gardé, **renommé** : on ne s'arrête pas,
  on met en pause pour demander. Une inconnue bloquante qui ne se lève pas
  toute seule remonte à l'utilisateur.

## Axe 3.4 · Tenue des faits
- **3.4.1 Provenance** — gardé.
- **3.4.2 Limites** — gardé.
- **3.4.3 Détection des contradictions** — gardé.
- **3.4.4 Résolution des contradictions** — gardé.
- **3.4.5 Péremption** — gardé.

---

# Principes dégagés en cours de revue

### P-01 — Rien n'est reporté à l'exécution
Tout ce qui peut être vérifié, investigué, demandé ou décidé l'est **avant**,
et le plan en découle — dans la limite du possible. Une inconnue nécessaire à
l'établissement du plan qui ne se résout pas automatiquement fait l'objet d'une
question à l'utilisateur.

C'est l'inverse exact du corpus : ses skills listaient les inconnues puis les
renvoyaient à l'exécution, faute d'avoir le droit d'enquêter.

### P-02 — Prioriser n'est pas écarter
Partout où le skill hiérarchise — objectifs, inconnues — la priorité ne sert
qu'à ordonner le travail. Rien n'est abandonné au motif qu'il est moins
prioritaire.

### P-03 — Ne jamais fabriquer de contrainte
Le skill peut détecter une exigence tacite et la faire remonter. Il ne l'impose
jamais de lui-même. Corollaire du refus des ajouts silencieux.

### P-04 — Ne jamais refuser pour cause de taille
Un plan trop gros se découpe et se fusionne (N-02). Il ne se refuse pas et ne
se réduit pas unilatéralement.

---

# Fonctions nouvelles issues de la revue

### N-01 — Entrée par un plan existant
Le skill doit pouvoir partir d'un plan plutôt que d'une demande, en dérivant le
besoin du plan lui-même. Permet de travailler un plan en plusieurs itérations,
et au skill de se relire. **Seconde porte d'entrée — à traiter au groupe 1.**

### N-02 — Découpage et fusion
Un plan trop gros se découpe en parties traitées séparément, puis fusionnées.
Mécanisme de passage à l'échelle. **À traiter au groupe 5.**

### N-03 — Recherche d'antécédents
Voir 2.6.4.

### N-04 — Classement construction / exécution
Voir 3.2.5.

---

## Axe 4.8 — note
Le plan **ne porte pas** les justifications. Elles vivent dans un fichier
distinct (correction de D-06). Le plan reste une suite d'actions ; le pourquoi
est ailleurs.

## P-05 — Le filet n'autorise pas la complaisance
Le rayon d'impact (4.2.3) et le séquencement par réduction du risque (5.2.3)
servent à calibrer le soin, jamais à s'autoriser la casse. On fait tout bon du
premier coup ; ces fonctions ne sont pas une assurance contre le laisser-aller.

## Test de compulsion — écarté
La plus grosse trouvaille du corpus (v7, conservée jusqu'à v18) est rejetée :
il y a toujours une infinité de manières de faire, donc jamais un seul chemin
viable. Cohérent avec le reste — ce test existait pour économiser du calcul, et
le skill ne se bride pas sur le coût. L'axe 4.3 cesse d'être une économie et
devient **Orientation du choix**, avec une seule fonction.

---

## P-06 — Le plan est impeccable par vérification, pas par filet

Principe rappelé quatre fois par l'utilisateur au fil de la revue, après quatre
propositions de ma part allant dans l'autre sens.

- On ne planifie pas en supposant qu'on va se rater. Tout est vérifié, investigué,
  demandé et décidé **avant** (P-01), et le plan en découle.
- Les impondérables existent, mais ils sont **exceptionnels** : ils deviennent des
  branches, et « un plan n'est pas truffé de branches ».
- L'appareil de risque, de filets, de retours arrière et de points de contrôle
  est une **part mineure** du skill, jamais son centre.
- Le rayon d'impact, le séquencement par réduction du risque et la validation du
  filet servent à calibrer le soin — **jamais à s'autoriser la casse**.

**Origine du biais** : les 16 versions du corpus ont été écrites pour des agents
qui *exécutent*. Elles sont donc saturées de containment, de rollback et de
modes de défaillance — au point que les versions récentes tournent presque
entièrement autour de ça. Notre skill produit un plan ; cette machinerie doit
être proportionnée, pas réflexe.

## P-07 — Certaines fonctions sont « sur proposition », pas automatiques

Statut distinct d'« optionnel » : le skill **offre** de les faire, il ne les
produit jamais d'office. Concerne tout le chiffrage — effort, coût, délai,
marges.

---

## Décisions de fin de groupe 5 et 6

- ~~5.6.4 Repli global~~ et ~~5.6.5 Déclencheurs de replanification~~ —
  **dissous (confirmé).** Si tout est vérifié avant et si les vraies
  indéterminations sont branchées, « le plan ne marche pas comme prévu » se
  détecte par un attendu (5.4.1) non satisfait. Le seul résidu — un fait vrai à
  l'écriture et faux à l'exécution — est tenu par les contrôles de fraîcheur
  (5.5.5).
- **5.7.4 Conflits de ressources** — **dissous dans 5.2.6.** Si les ressources ne
  suivent pas, ce n'est tout simplement pas parallélisable.
- **5.3 Forme et échelle** — reconstitué avec deux fonctions : élagage, et
  découpage en sous-plans puis fusion (N-02). Le dimensionnement des étapes
  (ex-5.3.1) devient un contrôle d'auto-évaluation au groupe 8 ;
  l'homogénéisation et le découpage en phases se dissolvent.
- **6.2.1 Externalités** — **déplacé au groupe 2.** Que l'utilisateur ait compris
  ce qu'il demande relève de la définition du besoin.
- ~~6.2.2 Prise en charge après la cible~~ — **écarté.** Sans rapport avec le
  fait de faire un plan ; quand la cible est un système qui doit vivre après,
  c'est un critère d'acceptation (2.2.2).
- **Axe 6.2 supprimé.**

## Groupe 6 après revue

- **Axe 6.1 Risque** — gardé en entier : recensement par origine, vraisemblance,
  statut du résiduel. Sous réserve de P-06 : c'est une part mineure du skill.
- **Axe 6.2 Conséquences certaines** — supprimé (6.2.1 déplacé au groupe 2,
  6.2.2 écarté).
- **Axe 6.3** — ne garde que 6.3.2 Visibilité de l'incertitude.
  ~~6.3.1 Dette de planification~~ **écartée** : contredit frontalement P-01,
  rien n'est reporté à l'exécution.
- **Axe 6.4 Conditions de sortie** — **supprimé.** Ni critères d'abandon, ni
  mesure après coup.

> **Rappel à moi-même** : l'auto-évaluation du skill et la mesure d'effet après
> coup ont été écartées dès l'axe 1.4. Ne pas les re-proposer sous un autre nom.

Le groupe 6 ne compte donc plus que **4 fonctions**.

---

# GROUPE 7 — MOYENS TRANSVERSES

## Axe 7.1 · Recours à l'humain
- **7.1.1 Décision d'interroger** — gardé.
- **7.1.2 Communication de la question** — gardé.
- **7.1.3 Présentation des arbitrages** — gardé.
- ~~7.1.4 Absence de réponse~~ · ~~7.1.5 Gestion du désaccord~~ ·
  ~~7.1.6 Voies d'escalade~~ — **effondrées dans P-08.**

### P-08 — L'utilisateur décide, le skill rapporte
- Pas de réponse → **le skill attend.** Il ne continue pas sur une valeur par
  défaut. *(Corrige D-08.)*
- Désaccord → le skill s'adapte.
- Besoin d'escalader → ça passe par l'utilisateur, jamais par une autre voie.

## Axe 7.2 · Recours aux agents
Les six fonctions sont gardées : décision d'ouvrir · rédaction du brief ·
garantie d'isolement · bornage · intégration des retours · arrêt de
l'orchestration.

> **Deux contraintes portées par le brief (7.2.2)**
> — ce qui est déjà établi y voyage, pour qu'aucun agent ne refasse le travail ;
> — un agent qui juge reçoit les critères d'acceptation **et** le besoin.

## Axe 7.3 · Respect du cadre *(renommé, une seule fonction)*
- **7.3.1 Respect du cadre** — gardé, **élargi** : respecter le tier configuré
  **et** le processus établi. Ne pas improviser de lancement d'agent non
  autorisé.
- ~~7.3.2 Dégradation ordonnée~~ · ~~7.3.3 Plancher non dégradable~~ —
  **écartées.** On ne dégrade jamais, sauf demande explicite de l'utilisateur.

---

# GROUPE 8 — SORTIR

### P-09 — Un plan dit quoi faire
Définition du contenu du livrable, donnée par l'utilisateur :

- **Pas** ce que l'agent exécutant va de toute façon devoir lire ou vérifier
  lui-même : numéros de ligne à changer, tailles de paragraphes, détails qu'il
  découvrira en ouvrant le fichier.
- Le **comment** n'est dirigé **que quand il n'est pas évident**.
- **Aucun archivisme, aucune justification**, aucun « on ne fait pas X parce que
  c'est moins bien ».
- En introduction : **l'objectif, et c'est tout.**

> « un plan c'est un plan. »

### P-10 — Le format est fixe
Le format du plan est **toujours le même**. Seul le contenu grossit avec la
complexité. Il n'y a donc pas de fonction de choix de forme.

### P-11 — L'exécutant est un agent
Dans la quasi-totalité des cas, l'exécutant est un agent automatique — souvent
celui-là même qui a produit le plan, après validation par l'utilisateur.

## Axe 8.1 · Adaptation au destinataire
- **8.1.1 Identification du destinataire** — gardé.
- ~~8.1.2 Choix de la forme~~ — **écarté** (P-10).
- **8.1.3 Actionnabilité automatique** — gardé (P-11).

## Axe 8.2 · Rédaction
- **8.2.1 Rédaction du plan** — gardé.
- **8.2.2 Rédaction de la traçabilité** — gardé, fichier séparé.
- ~~8.2.3 Carte de référence~~ — **écartée** : « c'est pas du plan, c'est de
  l'exécution de plan ».
- **8.2.4 Mise en regard d'alternatives** — gardé.
- **8.2.5 Tenue à part du hors-plan** — gardé.

## Axe 8.3 · Économie du livrable
- ~~8.3.1 Budget de longueur~~ — **écarté.** Inutile sous P-09 : si le plan ne
  contient que ce qu'il doit contenir, sa taille est déjà la bonne.
- **8.3.2 Élagage de la prose** — gardé, et **élargi par P-09**.

## Axe 8.4 · Matérialisation
- **8.4.1 Emplacement et nommage** — gardé.
- ~~8.4.2 Versionnement~~ — **écarté.** git le fait.

## Axe 8.5 · Restitution
- **8.5.1 Résumé** — gardé.
- **8.5.2 Signalement des limites** — gardé.
