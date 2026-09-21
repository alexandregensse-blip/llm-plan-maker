# Décisions de conception — plan-suite v19

Journal des choix arrêtés. Chaque entrée : la décision, ce qu'elle implique,
et ce qu'elle élimine du corpus existant.

---

## D-01 — Empaquetage : dossier de skill Anthropic uniquement

```
plan-suite/
  SKILL.md        en-tête YAML (name, description) + routeur + règles non négociables
  config.yml      tiers de techniques autorisées
  references/     chargés à la demande par le modèle
```

Divulgation progressive à trois étages : métadonnées toujours en contexte,
corps du SKILL.md au déclenchement, fichiers de `references/` sur décision
de lecture du modèle.

**Compatibilité chat : abandonnée.** Le skill peut supposer un système de
fichiers, des outils et des sous-agents.

Portage vers d'autres fournisseurs : plus tard, à la main. Risque assumé de
divergence entre versions (le reproche de v4 à la structure 4-fichiers de v3) —
mitigé par le fait qu'aucun objet n'est défini à deux endroits.

---

## D-02 — Périmètre : le skill produit un plan, et rien d'autre

Le livrable est **un plan détaillé**. Le skill pose des questions, explore,
dérisque — puis livre. Il ne conduit pas l'exécution.

**Élimine du périmètre** toute la boucle exécuter / observer / replanifier des
versions v9 → v18. Ce qui en survit devient *contenu du plan* : les déclencheurs
de replanification sont écrits dans le plan, à l'usage de qui l'exécutera.

---

## D-03 — Frontière d'autonomie : tout ce qui informe, rien qui engage

| Autorisé pendant la planification | Interdit |
|---|---|
| lire, chercher, inspecter | exécuter un commitment du plan |
| spawner des agents | toute action non trivialement réversible |
| interroger l'utilisateur | |
| expérience bornée et réversible, avec condition d'arrêt et décision débloquée | |

La typologie `discovery / commitment` que le corpus utilisait pour **typer les
étapes** sert ici à **délimiter le skill lui-même**.

---

## D-04 — Le brouillard n'est pas une doctrine, c'est un défaut d'enquête

Position de l'utilisateur, retenue contre l'ensemble du corpus :

> Soit on peut savoir — question, test, vérification — et alors **il faut savoir**.
> Soit on ne peut fondamentalement pas, et alors **on prévoit les deux**.

Conséquences :

- La doctrine « fog of war / ne planifie pas au-delà de la frontière »
  (v9 → v18) est **rejetée comme défaut par défaut**. Elle décrivait un agent
  qui exécute sans pouvoir enquêter ; le nôtre enquête avant, et a le droit de
  toucher l'environnement (D-03).
- **Une question ouverte dans un plan livré est un aveu d'enquête non faite.**
  Le skill doit la résoudre, pas la déclarer.
- Ne subsistent que les indéterminations réelles : celles dont la réponse
  n'existe pas encore au moment de planifier. Elles se traitent par **branche
  avec critère de décision explicite**, pas par troncature du plan.
- Le plan tronqué à la frontière avec replanification annoncée reste possible,
  mais en **dernier recours justifié**, jamais comme forme par défaut.

Récupère au passage le branchement conditionnel de v3 §4 (plafonné à 2 niveaux,
chaque branche = déclencheur / preuve requise / chemin / repli), abandonné après v3.

---

## D-05 — Deux axes : profondeur exigée (plancher) vs techniques autorisées (plafond)

- **Profondeur** : déduite de la tâche (conséquence, réversibilité, inconnues).
  Fixe un plancher de sûreté non négociable.
- **Effort** : déclaré dans `config.yml`. **Ce n'est pas un budget de tokens** —
  aucune estimation de coût n'est demandée au modèle. C'est une **liste de
  techniques et de types d'agents autorisés**.

```yaml
tier: standard
  spawn_agents: true
  max_parallel: 3
  roles: [explorer, verifier, risk_attacker]
  framing_pass: required
  transition_lens: on_irreversible
  independence_required: isolated
```

Le skill ne calcule rien : il vérifie que la technique qu'il allait employer
figure dans la liste.

**Conflit plancher / plafond** : si la tâche exige une technique que le tier
interdit, le skill ne dégrade pas en silence — il l'écrit dans le plan.
Aucune version du corpus ne traite ce cas (v5 §13, v8 §24 et v18 §12 le
colmatent sans le nommer).

**Élimine** toute estimation de coût par le modèle — même famille de fausse
précision que le PCS arithmétique de v3.

---

## D-06 — La traçabilité vit dans un fichier séparé du plan

**Corrigé en cours de revue des fonctions (axe 4.8) :** ce ne sont pas deux
étages d'un même fichier mais **deux fichiers**. Le plan ne fait ni archivisme
ni justification.

Deux objets distincts :

1. **Le plan** — cible, invariants, état vérifié, étapes contractualisées
   (attendu falsifiable, containment), gates, branches, risque résiduel.
2. **« Pourquoi ce plan »** — décisions prises et ce qui les a tranchées, faits
   vérifiés avec leur source et leurs limites, attaques menées et ce qui reste
   résiduel, dette de planification.

Le fichier de traçabilité est **omissible** sur les tâches légères. Reprend la séparation de
v6 §10 et v7 §12. Permet de relire une décision sans refaire le travail —
ce que v5 §16.1 appelait le cœur auditable du plan.

---

## D-07 — Destination : un fichier, plus un résumé court en conversation

Le plan complet est écrit dans un fichier markdown ; la conversation reçoit un
résumé de quelques lignes et le chemin. Le plan survit à la session, se relit,
se versionne, se passe à un autre agent.

Rapproche le skill du schéma d'artefact versionné de v3 (`plan-artifact`), seule
version à avoir traité le plan comme un objet durable.

---

## D-08 — Questions à l'utilisateur : en salves groupées, autant que nécessaire

- **Toujours groupées**, jamais en série (règle stable de tout le corpus).
- **Pas de plafond** sur le nombre de salves — contrairement au « cap : 2 questions
  par phase » de v7 §7.1, v15 §11.2, v17 §8 et v18 §8. On demande autant qu'il
  le faut, du moment que c'est groupé.
- ~~Chaque question porte une valeur par défaut recommandée.~~ **Corrigé en revue
  (axe 7.1) : le skill attend la réponse.** Reprise du corpus, pas une position
  de l'utilisateur. Voir P-08.
- **Ne jamais demander ce qui est moins cher à vérifier soi-même** par inspection,
  test ou recherche — corollaire direct de D-03 et D-04.

---

## D-09 — Déclenchement : sur demande explicite de plan

Le skill se charge quand l'utilisateur demande un plan, une stratégie, une
marche à suivre, un découpage de chantier — ou invoque le skill directement.
Il ne s'auto-déclenche pas sur une demande d'action formulée comme telle
(« migre la base vers PG 16 » veut dire migre, pas planifie).

Prévisible, zéro faux positif, jamais intrusif. Conséquence assumée : le skill
ne rattrapera pas de lui-même une action risquée non formulée comme un besoin
de plan.

C'est la pièce absente des 16 versions : aucune n'a de `description`
déclenchante, alors que c'est elle qui décide du chargement.

---

## D-10 — Enquête parallèle par agents : le défaut dès deux domaines séparables

Une inconnue par agent, en parallèle, dès que deux domaines d'enquête ne
dépendent pas l'un de l'autre. Brief étroit ; chaque agent rapporte une
observation, son localisateur, ses limites, et ce qui reste inconnu — jamais
une opinion.

Borne : `max_parallel` du tier (D-05).

Existait en v3 (`plan-research` R1, « 1 agent par domaine, en parallèle »),
perdu dans les treize versions suivantes. C'est l'usage d'agents le moins cher
et le plus rentable pour un agent outillé : ils reviennent avec de
l'observation, pas avec de l'opinion.

---

## D-11 — Challenge du cadrage : sur signaux observables

L'exercice « est-ce bien le problème ? » se déclenche si :

- la demande énonce **une solution** là où le sujet est un problème
  (« ajoute un cache Redis » plutôt que « le site est lent ») ;
- le domaine est peu familier ;
- le périmètre est flou ou mouvant ;
- se tromper coûte cher.

Sinon, on cadre et on passe à l'enquête.

Quatre questions quand il se déclenche : solution imposée ou vrai problème ? ·
quelle affirmation de l'énoncé peut être fausse ? · quelle contrainte ou
préférence est importée sans être dite ? · quelle vérification pas chère
lèverait le plus gros doute ?

Forme dégradable selon le tier : agent isolé recevant l'objectif sans notre
cadrage → passe séparée dans le même contexte → réponses écrites aux quatre
questions.

Motif : une erreur de cadrage produit un plan excellent sur le mauvais
problème, et aucune rigueur appliquée à l'intérieur du plan ne la rattrape.

---

## D-12 — Les propositions concurrentes à l'aveugle sont le cœur du skill

**Position de l'utilisateur, structurante.** Ce n'est pas une technique
déclenchée en dernier recours quand un choix résiste : c'est le mécanisme de
référence du skill.

Conséquence : l'arbitrage que je proposais — « l'enquête préalable rend la
confrontation presque toujours inutile » — est écarté. La confrontation aveugle
n'est pas un filet de sécurité, c'est la méthode.

Rapproche le skill de l'école v5 → v8 (confrontation aveugle, résolution par
preuve, jamais par vote), mais avec l'étape d'enquête (D-03, D-10) que cette
école n'avait pas.

Voir D-13 (niveaux), D-14 (ampleur), D-15 (arbitrage).

---

## D-13 — La confrontation aveugle opère aux trois niveaux

| Niveau | Ce qu'on met en concurrence | L'erreur que ça attrape |
|---|---|---|
| **Problème** | l'énoncé lui-même | on planifiait la mauvaise chose |
| **Structure** | des plans complets concurrents | le découpage est faux, une approche manquait |
| **Décision** | les options d'un point d'arbitrage | on s'est attaché à la première option venue |

Les trois sont conservés parce qu'ils attrapent des erreurs disjointes. v4
faisait le niveau *structure* ; v5 l'a supprimé au profit du niveau *décision*
(« un plan peut faire consensus tout en dissimulant une décision critique non
résolue ») et tout le corpus l'a suivi jusqu'à v18 — sans voir l'angle mort
symétrique : **on ne peut confronter que les décisions déjà listées**. Un
découpage faux est validé dans le détail par une confrontation décision par
décision.

Le niveau *problème* garde son déclenchement sur signaux (D-11). Les niveaux
*structure* et *décision* voient leur ampleur fixée par le tier (D-14).

---

## D-14 — L'ampleur de la confrontation est fixée par le tier

La mécanique ne change pas d'un tier à l'autre ; seule son étendue varie —
nombre de plans concurrents, confrontation par décision ou non, nombre
d'angles d'attaque, parallélisme d'enquête.

Cohérent avec D-05 : le tier est une liste de techniques autorisées, pas un
budget. Conséquence assumée : l'ampleur dépend de la configuration, pas de ce
que la tâche exige — le plancher de sûreté de D-05 reste la seule contrainte
venue de la tâche, et un conflit entre les deux s'écrit dans le plan.

---

## D-15 — Un arbitre aveugle à l'origine des propositions

Le skill **propose** comme les autres. Toutes les propositions sont
**anonymisées**, puis remises à un **agent arbitre distinct** avec le dossier
de faits et les attaques, sans qu'il sache laquelle vient de qui. Il rend une
résolution **point par point**, en indiquant ce qui a tranché chaque point.

Reprend la séparation rédacteurs / juge de v4 §3 — le juge ne voit jamais les
chaînes de raisonnement, seulement les propositions — abandonnée de v14 à v18
où le skill arbitrait lui-même.

Règles héritées du corpus, qui s'appliquent à l'arbitre : résolution par
preuve et jamais au nombre de voix · contrôle des hypothèses partagées entre
propositions · toute étape du plan final qu'aucune proposition ne contenait
doit être justifiée explicitement.

---

## Encore ouvert

- Définition exacte des tiers et du tier par défaut
- Répartition SKILL.md / references/
- Sections exactes du plan et de son annexe
- Contenu du « dossier de faits » remis aux propositions concurrentes
- Protocole d'évaluation pour sortir du statut `unproven`
