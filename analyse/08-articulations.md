# plan-suite — articulations possibles des 41 axes

Trois agents, même prompt, en parallèle, aveugles les uns aux autres.
Trois articulations chacun. Neuf propositions, **cinq familles distinctes**.

---

# Convergence et singularité

| Famille | Proposée par | Statut |
|---|---|---|
| **Pipeline à phases** | les 3 agents | convergence totale |
| **Graphe de dépendances** | les 3 agents, sous trois formes | convergence sur le principe, divergence sur le mécanisme |
| **Moteur à règles / blackboard** | 1 agent | singulier |
| **Anneaux de confrontation** | 1 agent | singulier |
| **Récursion par scope** | 1 agent | singulier |

La convergence vaut peu par les règles du skill qu'on conçoit : trois instances
de la même famille de modèles partagent leurs angles morts. Elle dit que le
pipeline et le graphe sont **les deux formes évidentes**, pas qu'il n'y en a pas
d'autres. Les trois propositions singulières sont, à ce titre, les plus
informatives.

---

# Famille 1 — Pipeline à phases

**Principe** — l'ordre des 8 groupes *est* l'ordre d'exécution. Chaque groupe
est une phase fermée par une porte de sortie ; une porte qui échoue renvoie vers
la phase amont responsable, jamais en avant. Le groupe 7 sort des phases et
devient transverse : ses axes sont des services que toute phase invoque.

```
PHASE 0 (G1) → applicabilité · terrain · tier
PHASE 1 (G2) → élucidation · réussite · délimitation · garde-fous · cadrage
   GATE1 : cible et périmètre stables ?        → sinon ARRÊT UTILISATEUR
PHASE 2 (G3) → état · inconnues · investigation (agents ∥) · faits · épistémique
   GATE2 : un fait contredit le cadrage        → BOUCLE vers PHASE 1
PHASE 3 (G4) → points · qualification · orientation
   orientation = fait manquant  → BOUCLE vers PHASE 2 (ciblée)
   orientation = préférence     → accumulée pour salve utilisateur
   orientation = vrai choix     → options · indépendance · épreuve · arbitrage
PHASE 4 (G5) → dérivation · structure · forme · contrats · contrôles · alternatives
   GATE4 : couverture, cohérence, invariants ? → BOUCLE vers PHASE 1, 2 ou 3
PHASE 5 (G6) → risque · incertitude assumée
PHASE 6 (G8) → destinataire · rédaction · économie · matérialisation · contrôle final
   échec du contrôle final → BOUCLE vers la phase fautive
   restitution → ARRÊT UTILISATEUR FINAL

TRANSVERSE (G7) : 7.1 matérialise les arrêts · 7.2 matérialise les spawns
                   7.3 borne 7.2 à chaque appel · 7.4 consultée en PHASE 0
```

**Optimise** — la lisibilité : « où en est-on » a toujours une réponse en un
mot. Auditabilité de la trace. Coût d'implémentation le plus faible. Colle au
format fixe du plan (P-10).

**Sacrifie** — tout parallélisme entre phases. Une invalidation locale et
tardive coûte un saut de phase entière : du travail refait pour rien, et le
risque que l'agent revalide en apparence les points non concernés plutôt que de
les re-trancher — brèche silencieuse dans P-01.

**Où elle casse** — trois critiques distinctes, une par agent :

1. *L'erreur de cadrage tardive et diffuse.* Migration d'un monolithe vers des
   microservices : le vrai problème (frontières d'équipe, pas frontières de
   code) n'apparaît qu'une fois plusieurs squelettes dessinés en PHASE 4.
   Aucun signal ne s'est déclenché au moment du cadrage. Il faut alors une
   boucle PHASE 4 → PHASE 1, qui n'est qu'une exception nommée dans
   l'algorithme — le risque réel étant que l'agent rustine localement plutôt que
   de rouvrir le cadrage.
2. *La boucle trop grosse.* Migration d'un monorepo module par module : la
   PHASE 4 révèle une contrainte qui invalide **un seul** point périphérique
   tranché en PHASE 3. Le seul retour disponible refait passer tous les points.
3. *Le destinataire découvert trop tard.* L'axe 8.1 n'est examiné qu'en PHASE 6,
   alors que l'identité du destinataire aurait dû cadrer les critères
   d'acceptation (2.2) et les attendus par étape (5.4) dès le début.

---

# Famille 2 — Graphe de dépendances

**Principe commun** — les groupes cessent d'être une unité d'ordre. Chaque axe
consomme et produit des objets ; ce qui ordonne le travail, ce sont les
dépendances de données réelles, pas le récit. Deux axes sans dépendance
s'exécutent en parallèle même s'ils appartiennent à des groupes éloignés.

Trois mécanismes différents pour la même idée :

### 2a — Worklist et drapeaux « sali »
Des objets d'état porteurs d'invariants (Cible, Garde-fous, Faits, Inconnues,
Décisions, Squelette, Résiduel, Trace, Livrable). Un ordonnanceur traite l'objet
dont l'invariant est violé ; le traitement en salit d'autres, qui repassent en
file, jusqu'à point fixe — plus aucun objet sale, plus aucune question en
attente. Il n'y a pas de « retour vers une phase antérieure » : c'est la même
primitive partout.

### 2b — Graphe d'artefacts avec propagation transitive
Neuf nœuds (Entrée, Cadrage, Faits, Registre de décision, Squelette, Plan
contractualisé, Résiduel, Trace, Sortie). Une arête signifie « l'aval ne peut
être validé tant que l'amont ne l'est pas ». Invalider un nœud invalide
transitivement ce qui en dépend — mais pas ce qui n'en dépend pas.
**Apport propre** : la Trace ne dépend que des Faits et du Registre de décision.
Elle peut donc se construire **en parallèle du plan**, alors que toute
articulation organisée par le temps la met forcément après.

### 2c — Ordonnancement topologique par batch
Chaque axe est un nœud avec ses entrées ; l'ordonnanceur exécute en parallèle
tout nœud dont les entrées sont prêtes, borné par le palier de configuration.
Une boucle arrière est simplement un nœud amont remis en file.
**Apport propre** : le destinataire (8.1) ne dépend que du mandat, donc il est
prêt dès le départ et tourne en parallèle de tout le groupe 2 — exactement le
défaut que la critique n°3 du pipeline identifiait.

**Optimise** — le parallélisme réel, et la précision de l'invalidation : on sait
exactement quel objet refaire, jamais plus. La correction sous changement tardif
est traitée par le mécanisme générique, pas par une exception.

**Sacrifie** — la lisibilité : « où en es-tu » n'a pas de réponse simple, la
réponse est un état de graphe. Le coût d'implémentation. Et il faut une garde
anti-oscillation explicite : rien n'empêche nativement deux objets de se salir
mutuellement sans converger.

**Où elle casse** — trois critiques :

1. *La tâche triviale.* « Renomme ce package en trois commits » : monter un
   ordonnanceur, des drapeaux et des arêtes pour trois commits indépendants est
   de la plomberie pure.
2. *Le doute fondamental pendant que les accessoires avancent.* Si le cadrage
   n'est pas tranché mais que des nœuds périphériques sont « prêts » selon le
   graphe, l'ordonnanceur avance dessus. Si le cadrage bascule, ce travail est
   perdu — **le graphe n'a aucune notion de priorité narrative** qui dirait
   d'attendre.
3. *L'absence de frontière nette entre artefacts.* Refactoring exploratoire où
   chaque fait trouvé redéfinit le périmètre : Cadrage et Faits s'invalident
   mutuellement en boucle serrée sans converger, là où un pipeline qui les
   traite comme un bloc itéré s'en sortirait.

---

# Famille 3 — Moteur à règles piloté par événements

*Singulier — un seul agent.*

**Principe** — pas de phases, pas de graphe explicite. Une mémoire de travail
dont chaque champ est `valide / invalide / absent`, et une trentaine de règles
condition → action, une par axe ou petit groupe d'axes. Toute règle dont la
condition est vraie peut tirer ; l'ordre d'exécution n'est écrit nulle part, il
découle de l'état. Une invalidation réarme mécaniquement les règles qui en
dépendaient — **aucune boucle n'est à écrire**, la portée du retour est
exactement la portée du champ invalidé.

```
loop:
    si bloqué : ATTENDRE l'utilisateur ; continuer
    R = { règles dont la condition est vraie }
    si R vide : si sortie validée → rapporter, FIN
                sinon → erreur : chaîne d'axes incomplète
    exécuter(choisir(R))
```

Les axes du groupe 7 ne sont pas des règles mais des **services** que toute règle
invoque — en faire des règles créerait une dépendance temporelle qu'elles n'ont
pas.

Note importante sur le blocage : tant qu'une question est en attente, **le
moteur entier suspend**. Aucune règle ne tire, pas même celles sans rapport avec
la question. C'est la lecture stricte de P-08.

**Optimise** — la réactivité fine : P-01 est appliqué au niveau du champ, pas de
la phase. Un fait qui casse une seule décision ne recalcule que cette décision.

**Sacrifie** — la reconstruction de la trace : il faut reconstituer après coup
l'ordre d'exécution réel pour écrire quelque chose de compréhensible, ce que le
moteur ne fournit pas.

**Où elle casse** — deux règles aux conditions faiblement disjointes peuvent
s'exécuter dans un ordre cohérent mais **non reproductible d'une exécution à
l'autre**. Mauvais pour un skill dont le format de sortie doit être stable (P-10).

---

# Famille 4 — Anneaux de confrontation

*Singulier — un seul agent. C'est l'articulation qui prend D-12 au mot.*

**Principe** — ce n'est ni une histoire ni un graphe de données : ce sont **trois
anneaux de confrontation aveugle** — Problème, Structure, Décision — reliés par
des arcs de retour. Tout le reste des axes est soit la préparation d'un dossier
pour un anneau, soit la mise en forme d'un verdict d'anneau.

```
ENTRÉE (1.1 1.2 · 7.4) → EFFORT (1.3, fixe l'ampleur des trois anneaux)
                                    │
      ┌─────────────────────────────▼──────────────────────────────┐
      │ ANNEAU P — PROBLÈME                                          │
      │ dossier : élucidation, garde-fous initiaux, état minimal     │
      │ [rédacteurs aveugles] ⇉ [ARBITRE anonymisé] ⇉ verdict        │
      └──────┬────────────────────────────────┬─────────────────────┘
        « manque de faits »              « cadrage confirmé »
             ▼                                 ▼
      ┌──────────────┐                 ┌──────────────────────────┐
      │ ANNEAU R      │◄────────────────┤ ANNEAU S — STRUCTURE      │
      │ RÉEL          │                 │ dossier : squelettes      │
      │ dossier de    │────────────────►│ candidats écrits          │
      │ faits partagé │                 │ indépendamment            │
      └──────┬────────┘                 └────┬──────────────┬──────┘
             │                               │       « un concurrent résout
             │                               │        un meilleur problème »
             │                               │              │
             │                               │              ▼
             │                               │      retour ANNEAU P
             ▼                               ▼
      ┌──────────────────────────────────────────────┐
      │ ANNEAU D — DÉCISION (par point, ∥ possible)   │
      └──────┬──────────────────────────┬────────────┘
   « structure inadaptée »        « faits manquants »
             ▼                            ▼
      retour ANNEAU S              retour ANNEAU R

      MISE EN FORME (contrats, contrôles, alternatives, moyens, résiduel)
      SORTIE — le contrôle final est un anneau minimal à un vérificateur
```

**Apport propre et décisif** — l'arc *Structure → Problème*. Dans le pipeline
comme dans le graphe, un découpage faux ne se rattrape que par une boucle de
retour ajoutée après coup. Ici, le fait qu'une confrontation au niveau structure
puisse révéler qu'on résolvait le mauvais problème est **une arête du graphe, pas
une rustine**. C'est exactement l'angle mort identifié en D-13 : on ne peut
confronter que les décisions déjà listées, donc un découpage faux est validé
dans le détail par une confrontation décision par décision.

**Optimise** — met le mécanisme de référence du skill (D-12) littéralement au
centre, au lieu de le distribuer en points isolés d'une séquence.

**Sacrifie** — la légèreté. Même à ampleur réduite par le palier, la mécanique
« préparer un dossier → anonymiser → arbitrer » reste présente à chaque anneau.

**Où elle casse** — « ajoute un script de purge des logs de plus de 30 jours ».
Aucun risque de cadrage, aucune vraie décision, une inconnue triviale. Les trois
anneaux imposent leur cérémonie là où un pipeline traverserait les huit groupes
en une passe, chaque axe répondant « rien à signaler » en une ligne.

---

# Famille 5 — Récursion par scope

*Singulier — un seul agent. La seule qui intègre N-02 structurellement.*

**Principe** — l'unité de décomposition n'est ni la phase ni l'objet, mais le
**sous-plan**. Un cycle complet — cadrer, savoir, décider, construire —
s'applique récursivement à chaque nœud d'un arbre de périmètres. Les groupes 1,
6, 7 et 8 encadrent la récursion sans y entrer.

```
fonction PLAN(périmètre) :
    cadrer(périmètre)        # G2 restreint ; questions accumulées, pas envoyées
    savoir(périmètre)        # G3 restreint ; agents ∥ par inconnue
    pour chaque point de décision :
        qualifier
        si le rayon d'impact déborde le périmètre → REMONTER au parent
        orienter → fait manquant : rappeler savoir() ciblé
                   préférence    : accumuler
                   vrai choix    : options, épreuve, arbitrage
    construire(périmètre)    # G5 restreint
        si un sous-périmètre est trop dense :
            pour chaque sous-périmètre indépendant :
                actions += PLAN(sous-périmètre)   # ∥ si périmètres frères indépendants
            fusionner(actions)
    retourner { actions, décisions tracées, résiduel local }

racine = PLAN(mandat entier)
confrontation NIVEAU STRUCTURE : plusieurs arbres concurrents, arbitre distinct
```

**Apport propre** — c'est la seule articulation où **le découpage en sous-plans
et la fusion (N-02) sont le mécanisme même**, et non une fonction rangée dans un
axe. Et elle apporte une règle que personne d'autre n'a formulée : *un point de
décision dont le rayon d'impact déborde son périmètre remonte au parent — il
n'est jamais tranché localement.*

**Optimise** — la cohérence locale des sous-plans complexes. Excellente sur les
tâches multi-chantiers hétérogènes (« migre la base ET refais l'intégration
continue ET documente »).

**Sacrifie** — la vue d'ensemble précoce : la cible racine doit être fixée avant
de savoir comment découper. Et elle ajoute une mécanique de remontée
inter-périmètre — quand remonter, comment fusionner deux traces de périmètres
frères — coûteuse à spécifier.

**Où elle casse** — tâche plate et mono-périmètre : la récursion ne se déclenche
jamais, toute la machinerie de remontée est un appareil inutile, et chaque axe a
dû se demander « suis-je local ou dois-je remonter ? » pour rien. Elle dégénère
en pipeline à un seul niveau, avec un coût de raisonnement supérieur.

---

# Ce que la comparaison fait apparaître

**Toutes les cinq cassent sur des tâches différentes.** Pipeline : l'erreur de
cadrage tardive. Graphe : le doute fondamental pendant que les accessoires
avancent. Moteur à règles : la reproductibilité. Anneaux : la tâche triviale.
Récursion : la tâche plate.

**Trois défauts apparaissent chez plusieurs familles à la fois** et méritent
d'être traités quelle que soit la forme retenue :

1. **Le destinataire est examiné trop tard.** Il ne dépend que du mandat, il
   devrait cadrer les critères d'acceptation et les attendus par étape. Deux
   agents l'ont relevé, l'un comme défaut du pipeline, l'autre comme gain du
   graphe.
2. **La trace n'a pas à attendre le plan.** Elle ne dépend que des faits et des
   décisions tranchées.
3. **Il n'existe aucune notion de priorité narrative.** Dans toute articulation
   qui parallélise, rien n'interdit d'avancer sur des accessoires pendant qu'un
   doute fondamental reste ouvert.

**Une tension structurelle traverse les cinq** : ce qui rend une articulation
lisible la rend rigide, ce qui la rend précise la rend illisible. Le pipeline
répond en un mot à « où en es-tu » et paie en boucles grossières ; le graphe
invalide au nœud près et ne sait plus dire où il en est.
