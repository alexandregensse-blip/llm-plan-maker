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

## D-16 — Le format du plan est fixé par un template, et c'est hors scope pour l'instant

Le plan livré suit un template fixe.
On ne décide pas maintenant de ses sections : on y reviendra après l'architecture.
Aucune fonction ne porte le format, et c'est assumé.
La « règle F » proposée par l'agent Opus reste une proposition, pas une décision.

---

## D-17 — La validation du plan par l'utilisateur est hors du skill

La sortie du skill est le plan, et rien d'autre.
Si l'utilisateur n'est pas satisfait, il réinvoque le skill en disant ce qui ne va pas.
Mais si ça arrive, c'est qu'on a mal cerné son besoin : c'est un défaut du skill en amont, pas une porte manquante en aval.

---

## D-18 — Pas de fonction pour traquer les retraits silencieux

Il suffit que le contrôle final soit assez bon pour les rendre bruyants.
Un retrait dont personne ne s'aperçoit au contrôle est un retrait qu'il fallait faire.

---

## D-19 — L'épreuve d'autonomie est ajoutée au périmètre

Le principe 13 veut un plan auto-porteur, et rien ne l'éprouvait.
Le contrôle : donner le plan seul à un agent qui n'a rien vu de l'enquête, et lui demander non pas de l'exécuter, mais de dire à quel endroit il devrait redemander quelque chose.
Nouvelle fonction `EPROUVER_AUTONOMIE_DU_TEXTE`, axe 8.6.

---

## D-20 — Le plan n'est pas daté

Ce qui bouge avec le temps n'est pas le plan mais les faits dont il part.
Le traitement correct existe déjà : une étape de vérification des hypothèses, constats et axiomes, inscrite dans le plan.
Rejouer un plan se fait à la demande de l'utilisateur, ce qui est hors du périmètre du skill.

---

## D-21 — Une seule architecture, efficace dans tous les cas

Pas de régimes A / B / C, pas de sélecteur en amont.
Une architecture unique, qui doit tenir sur la demande triviale comme sur le travail trop gros.
Si elle n'y arrive pas, on l'améliore — on ne la duplique pas.

---

## D-22 — Les règles communes ne sont pas arbitrées par nous

Les quatre invariants proposés par l'agent Opus (quittance, arbitre briefé, champ d'un seul, cadre) ne sont ni validés ni rejetés.
C'est aux agents qui proposent des architectures de juger si c'est bien.

---

## D-23 — L'indépendance des concurrents aveugles est atteignable

Constat empirique : à modèle identique, les discours diffèrent réellement.
Quand ils ne diffèrent pas assez, biaiser explicitement un concurrent — lui demander autre chose — fonctionne.
C'est une technique légitime, pas un aveu de faiblesse.

---

## D-24 — Utilisateur non coopératif

S'il ne répond pas : on attend.
S'il répond « je ne sais pas » : on lui explique simplement de quoi il s'agit.
S'il se contredit : c'est que le besoin est mal cerné, et c'est à l'agent de le cerner mieux.

---

## D-25 — Les inconnues sont réputées résolubles avant le plan

On part toujours du principe qu'une inconnue peut être levée avant d'écrire le plan.
Le classement construction / exécution existe, mais il doit être contrôlé par le système lui-même, jamais décidé en silence.
Pas par l'utilisateur : on ne le sollicite jamais sur ce qu'on peut faire en autonomie.

---

## D-26 — On ne sollicite jamais l'utilisateur sur ce qu'on peut faire en autonomie

La question à l'utilisateur est un dernier recours, jamais un réflexe ni un moyen de se couvrir.
Contrepoids indispensable au principe « l'utilisateur décide » : sans lui, le système se décharge de son travail d'enquête en posant des questions.

---

## D-27 — Arbitrage des fonctions manquantes relevées par l'architecture

Cinq opérations sans fonction dédiée ont été soumises ; trois deviennent des fonctions, deux sont absorbées.

**Ajoutées.**
`LIRE_MODELE_DE_PLAN` — le format du plan est une entrée du système et rien n'allait le chercher.
`CONTROLER_REPORT_A_L_EXECUTION` — le contrôle du classement d'une inconnue en « exécution ».
C'est le principe le plus fort du plan, il ne doit pas dépendre d'un montage de quatre fonctions.
`REPRENDRE_PASSE_PRECEDENTE` — reprise d'un plan issu du skill lui-même, avec son registre.

**Absorbées.**
Le contrôle du brief avant envoi n'est pas une fonction : c'est une technique de rédaction du brief, et la définition de `REDIGER_BRIEF_AGENT` l'intègre.
L'explication de l'enjeu n'est pas une fonction : `FORMULER_QUESTION_ACTIONNABLE` doit exposer ce qui change selon la réponse.

**Deux cas distincts en entrée**, et c'est ce qui motive `REPRENDRE_PASSE_PRECEDENTE` :
un plan produit par une exécution antérieure du skill arrive au format connu, avec son registre — on poursuit les itérations avec les informations nouvelles ;
un plan d'origine étrangère arrive sans registre et dans un format inconnu — `AMORCER_DEPUIS_PLAN_EXISTANT` en dérive le besoin.
Confondre les deux fait repayer ce qui était déjà acquis.

Le jeu passe à 133 fonctions.

---

## D-28 — Le redécoupage est autorisé, adossé à un fait nouveau

Lorsque deux sous-plans ne se raccordent pas et que l'incohérence révèle que le découpage lui-même était mauvais, figer l'interface ne corrige rien.
Le redécoupage est alors autorisé, à une seule condition : qu'un fait nouveau, absent du registre des faits, le justifie.
C'est la règle qui gouverne déjà la réouverture de toute décision close.
Elle préserve la garantie d'arrêt du traitement, puisque le registre des faits ne fait que croître et que les redécoupages sont donc en nombre fini.
Sans fait nouveau, le point remonte à l'utilisateur.

Écarté : l'escalade systématique, qui faisait remonter à l'utilisateur un défaut que le système savait corriger.

---

## D-29 — La structure d'une passe antérieure est conservée par défaut

Si les éléments nouveaux nécessitent de changer la structure, on la refait.
Si le système juge qu'ils ne le nécessitent pas, on ne la refait pas : elle passe par le contrôle final, comme à chaque fois.

Les éléments nouveaux sont observables : faits établis depuis la passe précédente, réponses de l'utilisateur, cible ou critères d'acceptation modifiés.
La structure n'est donc pas remise en concurrence par principe à chaque exécution du skill — sans quoi trois passes referaient trois fois le travail de structuration.
Le filet n'est pas une confrontation supplémentaire, c'est le contrôle final, qui porte de toute façon sur la structure.

Cette décision ne vaut que lorsque le registre de la passe antérieure est disponible, c'est-à-dire pour un plan issu du skill lui-même.
Un plan d'origine étrangère ne porte aucune structure enregistrée : le niveau 2 s'exécute.

---

## D-30 — Épuisement des options écartées

Lorsque la vérification de faisabilité par l'exécutant échoue, le choix n'est pas rejoué : l'option suivante parmi celles qui avaient été conservées est reprise, et cette seule vérification est refaite.
Si toutes les options conservées échouent à leur tour, le champ est épuisé.
Ce cas est alors traité exactement comme celui d'une confrontation où aucune proposition ne tient : le point passe à l'utilisateur.
Aucune issue nouvelle n'est créée, et le traitement ne s'arrête pas de lui-même.

---

## D-31 — Indépendance faible après épuisement des angles

Lorsque l'indépendance obtenue entre concurrents reste faible alors que tous les angles d'attaque disponibles ont été employés, le traitement se poursuit.
Il n'interroge pas l'utilisateur : il n'y a rien à lui demander.
L'indépendance obtenue est consignée au registre telle qu'elle est.

Motif : une faiblesse de méthode consignée n'est pas un point ouvert du plan.
Le principe « un plan livré ne contient jamais de point ouvert » porte sur le contenu du plan, pas sur la qualité des moyens employés pour l'écrire.

---

## D-32 — Une réponse qui ne tranche pas

L'utilisateur répond « je ne sais pas », ou rend une réponse inexploitable.
Premier réflexe : vérifier si un moyen disponible permet d'établir le point sans lui.
Si oui, l'entrée change de type et devient un fait à établir — elle ne lui est pas reposée.
Sinon, la question est reformulée avec l'énoncé de ce qui change selon la réponse, et elle repart **dans le même échange** : l'utilisateur est là, on ne le fait pas attendre l'itération suivante.

La promesse « une interruption par itération » porte sur le fait de ne pas revenir le chercher plus tard, pas sur le nombre d'échanges dans une conversation déjà ouverte.

---

## D-33 — Une entrée déjà reformulée qui reçoit une seconde réponse qui ne tranche pas

On ne reformule pas une troisième fois.
Cela signifie que la question porte au-delà de ce que l'utilisateur peut savoir, et la réponse n'est pas d'insister.
On change d'objet : on l'interroge sur son **besoin** — ce qu'il cherche à obtenir — plutôt que sur la manière d'y parvenir.
Les réponses obtenues alimentent le niveau 1.

L'état « déjà reformulée » est écrit au registre : ce n'est pas un compteur d'essais, c'est une propriété observable de l'entrée.

---

## D-34 — Un besoin arrêté lors d'une passe antérieure

Il est confronté à la demande telle qu'elle arrive, éventuellement reprécisée par l'utilisateur au moment où il relance le système.
Si rien dans cette demande ne le contredit, le besoin est conservé avec sa cible et ses critères, et le niveau 1 n'est pas rejoué.
S'il y a contradiction, les lectures du besoin sont remises en concurrence.

Même logique que D-29 pour la structure, avec une différence : la confrontation à la demande nouvelle est systématique, parce que c'est précisément là que l'utilisateur dit ce qui n'allait pas.

---

## Encore ouvert

- Définition exacte des tiers et du tier par défaut
- Répartition SKILL.md / references/
- Sections exactes du plan et de son annexe
- Contenu du « dossier de faits » remis aux propositions concurrentes
- Protocole d'évaluation pour sortir du statut `unproven`
