J'ai lu les 129 fonctions et les dix-huit architectures intégralement, et j'ai vérifié par recoupement quelles fonctions chacune appelle réellement.

**Avertissement préalable sur le gisement.** Les dix-huit ne sont pas dix-huit. Les architectures 02, 04 et 15 partagent **mot pour mot** trois blocs (`CONFRONTATION`, `CONSTITUER_DOSSIER_INITIAL`, `METTRE_EN_FORME_ET_CONTROLER`) et ne diffèrent que par leur pilote de haut niveau. Les architectures 07, 11 et 13 partagent mot pour mot `PROLOGUE_CADRAGE` et `EPILOGUE_CLOTURE` et ne présentent chacune qu'un `CYCLE_x` distinct. Il y a donc environ onze propositions réelles, et les « accords » entre architectures ne sont pas des confirmations : c'est exactement le cas que `DETECTER_ORIGINE_COMMUNE_SOURCES` décrit. J'en ai tenu compte en notant : je note ce qui est écrit dans chaque soumission, mais je ne compte jamais un mécanisme comme validé parce que trois clones le portent.

---

# PREMIÈRE PARTIE — DÉPOUILLEMENT

Notes sur 5. **S** = suivabilité, **F** = fidélité, **B** = boucles, **U** = usage des fonctions, **P** = proportionnalité.

| # — Nom | S | F | B | U | P | Appréciation | À RETENIR | À NE PAS FAIRE |
|---|---|---|---|---|---|---|---|---|
| **01 — Pipeline à sas** | 4 | 2 | 3 | 2 | 1 | Catalogue linéaire : les 124 fonctions appelées défilent une fois chacune, dans l'ordre, découpées en six phases. C'est lisible et c'est précisément le vice annoncé — dérouler les fonctions une par une ne vaut rien. La compétition n'existe qu'au niveau des décisions : les deux autres niveaux du principe 3 sont absents. | Le « contrôle de sortie » de fin de phase qui **nomme la phase de retour et la cause** (`objectif non couvert → PHASE 3`, `cible infidèle → PHASE 0`) : un routage explicite par nature du défaut, au lieu d'un rebouclage global. | `EVALUER_EXIGENCE_TACHE` appelé en **phase 4**, après toute l'enquête et toute la construction : la sélection des techniques arrive quand plus rien ne peut en dépendre. Plafonds décrétés partout (`boucle_reformulation < 2`, `max 2 passes`). Phase ASSURANCE entière consacrée au risque → principe 7 violé. |
| **02 — Deux vagues + filet global** | 4 | 4 | 2 | 4 | 2 | La seule famille qui installe vraiment les trois niveaux du principe 3 (problème, structure, choix), via un bloc `CONFRONTATION` réutilisable — bonne abstraction, bien plus suivable qu'un graphe. Mais le « filet de sécurité » unique est un **redo total** : au moindre défaut on relance problème, structure et choix, ce qui est l'inverse d'un retour ciblé. | `CONFRONTATION(question, dossier)` comme **sous-programme appelé sur trois objets différents** : la répétition a un sens, elle attrape trois erreurs distinctes. La salve de confrontations de choix mutuellement aveugles (un choix ne voit pas la résolution d'un autre). | « On pousse la levée d'inconnues **au-delà du strict nécessaire** » : sur-enquête décrétée, anti-proportionnalité assumée. `dossier_gelé` : un instantané figé interdit d'intégrer un fait découvert tard. `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` et `CONTESTER_ENONCE_PROBLEME` absents → principes 8 et 3 entamés. |
| **03 — Colonne vertébrale contradictoire** | 3 | 3 | 3 | 4 | 1 | L'idée forte est d'appliquer `ATTAQUER_TOUT_LE_CHAMP` à trois grains (le cadrage nu, le champ d'options d'une décision, les combinaisons de branches). C'est trois grains d'**attaque**, pas trois niveaux de **propositions concurrentes** : le problème et la structure ne sont jamais mis en concurrence, seulement attaqués. | La **double levée indépendante sur un fait pivot**, avec `ISOLER_LES_EVALUATIONS` puis `DETECTER_ERREURS_CORRELEES` et `QUALIFIER_INDEPENDANCE_OBTENUE` : la boucle est déclenchée par un observable (l'indépendance mesurée), pas par un compteur. Le tiers relecteur reçoit le plan et les critères, **jamais le raisonnement**. | `AMORCER_DEPUIS_PLAN_EXISTANT` absent → principe 12 violé. « Si un même type de finding réapparaît : ne pas reboucler, `SIGNALER_LES_LIMITES` » — on livre un plan avec une faiblesse connue au lieu de remonter à l'utilisateur : principes 1 et 4 violés. Cérémonie identique du trivial au lourd. |
| **04 — Agenda piloté par un graphe** | 1 | 3 | 3 | 4 | 3 | Mêmes blocs que 02, pilotés par un graphe mutable et un agenda à priorité, avec un mémo `faits_ayant_déjà_rouvert = {(nœud, fait)}`. Formellement c'est le plus rigoureux du lot ; concrètement un modèle de langage ne tiendra ni le graphe, ni l'agenda, ni le mémo de couples : ce sera joué, pas suivi. | La **propagation d'invalidation déclenchée par un observable** : `NOMMER_FAIT_QUI_FERAIT_BASCULER` produit un fait, et seuls les nœuds qui dépendaient de ce fait sont rouverts, `REUTILISER_ACQUIS` protégeant le reste. L'argument de terminaison est monotone, pas décrété. | Entretenir une structure de données vivante dans une instruction destinée à être lue. `agenda.remettre(n)` avec re-calcul de priorité à chaque tour. `CONTESTER_ENONCE_PROBLEME` et `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` absents. |
| **05 — File de travail pilotée par les dépendances** | 1 | 1 | 2 | 2 | 3 | File à priorité « impact × 1/coût de résolution », compteurs de rebond par item, re-classement de la file à chaque tour, contrôle « toutes les N itérations ». Et l'appareil contradictoire est vidé : ni `ISOLER_LES_EVALUATIONS`, ni `ARBITRER_A_L_AVEUGLE`, ni `ATTAQUER_TOUT_LE_CHAMP`, avec une « attaque légère, un seul passant ». | Le traitement de l'exigence tacite comme **item de file à part entière**, retiré en un passage après réponse de l'utilisateur, et qui engendre à son tour des inconnues. Rien d'autre. | Prioriser par `1/coût` : le système raisonne en coût → principe 5 violé frontalement. `compteurs_rebond[item] > 4` : plafond arbitraire, par item, à tenir de tête. Le principe 3 — mécanisme central — est purement et simplement supprimé. |
| **06 — Chaînage par dépendances** | 3 | 2 | 2 | 3 | 2 | Résolution nœud par nœud en ordre topologique, correctement ordonnée, mais neuf boucles numérotées avec chacune son `REPEAT au plus 2 fois`. L'appareil aveugle est absent (`ARBITRER_A_L_AVEUGLE`, `ISOLER_LES_EVALUATIONS`, `GARANTIR_DIVERSITE_METHODE` jamais appelés) : les options sont attaquées puis tranchées à découvert. | La **réouverture ciblée avec propagation aux seuls dépendants, jamais en amont**, adossée à `REUTILISER_ACQUIS` sur les faits qui tiennent. `RECENSER_INCONNUES` rappelé localement à chaque nœud plutôt qu'une fois globalement. | Neuf budgets de boucle distincts à tenir simultanément. `SIGNALER_LES_LIMITES("plan non exécutable par ce destinataire")` puis on continue : on livre un plan dont on sait qu'il ne s'exécute pas. `DECIDER_D_INTERROGER_UTILISATEUR` absent : le système décide seul quand parler. |
| **07 — L'arbre des objectifs** | 3 | 2 | 3 | 2 | 4 | Décomposition récursive par grappes d'objectifs, avec remontée des décisions qui débordent leur grappe — bonne intuition sur le principe 8. Mais `TRANCHER_DECISION` n'appelle jamais `ARBITRER_A_L_AVEUGLE` : s'il reste plus d'une option survivante, la décision est **jetée à l'utilisateur**. Et le cycle n'ouvre aucun agent : ni brief, ni bornage, ni `REFUSER_AUTO_CONFIRMATION`. | Le **critère de décomposition fondé sur des observables** — conflits d'objectifs, hétérogénéité des formes de travail — et non sur une estimation de taille : c'est, avec 12, la seule proportionnalité honnête du lot. L'escalade d'un risque dont le `QUALIFIER_RAYON_IMPACT` déborde le périmètre vers le niveau parent. | Faire trancher l'utilisateur à chaque fois que l'arbitre devrait trancher : principes 3 et 4 tordus ensemble. 35 fonctions abandonnées sans un mot, dont `SUSPENDRE_ENQUETE_ET_DEMANDER`, `CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION` et tout le bloc de provenance des faits. `PROFONDEUR_MAX` décrétée. |
| **08 — File de travail à point fixe** | 1 | 3 | 3 | 4 | 4 | File typée (inconnue / décision / risque / étape) tournant jusqu'au point fixe : élégant sur le papier, ingérable à la lecture (profondeur par item, compteur global K, éligibilité recalculée). Surtout, le RISQUE devient un **type d'item de premier rang**, engendré par chaque décision : l'appareil de risque passe au centre. | L'application d'une **même famille de fonctions à quatre types d'objets** : c'est la répétition la mieux motivée du lot. Le renvoi d'une hypothèse tacite non levée en item `INCONNUE` avec différé de la décision, dépendance explicite à l'appui. | Faire du risque le moteur : principe 7 renversé. `VERIFIER_FIDELITE_CIBLE_BESOIN` jamais appelée — la cible n'est jamais confrontée au besoin. Plafond global `K` de réouvertures, puis `CONSTATER_IMPOSSIBILITE` : une impossibilité décrétée par épuisement d'un compteur n'est pas une impossibilité. |
| **09 — Cascade de passes contradictoires** | 3 | 2 | 3 | 3 | 3 | Un brouillon non vérifié, puis des passes contradictoires successives avec rebonds. Le routage des rebonds est juste, mais deux choix cassent la fidélité : la **levée paresseuse** (« seulement ce dont l'option retenue a besoin ») contre le principe 1, et l'absence de `RECENSER_CONTRAINTES_DURES` / `DEFINIR_CRITERES_ACCEPTATION` — le plan peut franchir une contrainte qu'on n'a jamais recensée. | La sortie de passe **« si rien de nouveau : sortir »** : une terminaison par absence de nouveauté observable, pas par plafond. Le rebond du champ d'options vers la passe CONTENU quand tout le champ casse — remontée au bon endroit. | « Au plus 1 rebond par couple Document→X sur tout le run » : le compteur par couple de phases, exactement ce qui sera joué et non suivi. Planifier à partir d'un brouillon qu'on rafistole ensuite, au lieu de le jeter. |
| **10 — L'épreuve récursive** | 3 | 3 | 4 | 4 | 2 | `EPROUVER(objet, nature)` appliquée à l'énoncé, aux faits, aux décisions, au plan : bonne abstraction, bonne montée en échelle. Mais c'est de l'**attaque** à toutes les échelles, pas de la **concurrence** : les propositions rivales n'existent qu'au niveau 3. Et elle vérifie des invariants sans avoir recensé les contraintes dures ni les préférences. | La meilleure terminaison locale des dix-huit : **`TANT QUE non établi ET essais < moyens disponibles`** — on épuise un ensemble fini de moyens, on ne décompte pas des tours. Le routage du niveau 5 par nature de la faille (fait → N2, décision → N3, étape → N4). | `AMORCER_DEPUIS_PLAN_EXISTANT` absent → principe 12. `RECENSER_CONTRAINTES_DURES`, `RECENSER_OBLIGATIONS_FORMELLES`, `RECENSER_PREFERENCES` absents : `VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN` porte alors sur un registre vide. `tours == 3` puis `SIGNALER_LES_LIMITES` sur un point litigieux : on livre le litige. |
| **11 — L'arbre d'enquête** | 3 | 1 | 3 | 1 | 3 | Un arbre d'enquête par domaines, avec agents parallèles et escalade — et rien d'autre. Zéro appareil contradictoire : ni `PRODUIRE_OPTIONS_DISTINCTES`, ni `ATTAQUER_UNE_OPTION`, ni `ARBITRER_A_L_AVEUGLE`. `ASSEMBLER_PLAN` est un moignon qui se termine sur `CONTROLER_TAILLE_DES_ETAPES` : ce n'est pas une architecture de plan, c'est une architecture d'enquête. | L'**escalade d'une inconnue dont la portée déborde le périmètre** vers le niveau parent, plutôt que de la trancher localement à l'aveuglette. Le croisement systématique des faits issus de branches différentes par `DETECTER_CONTRADICTION_ENTRE_SOURCES` + `DETECTER_ORIGINE_COMMUNE_SOURCES`. | 41 fonctions absentes, dont tout le principe 3, tout le risque, toutes les branches, tous les points d'engagement. Confondre « avoir enquêté » et « avoir planifié ». |
| **12 — Spirale incrémentale** | 2 | 3 | 3 | 3 | 5 | Squelette mince d'abord, épaississement **uniquement aux points marqués** « territoire reconfigurant » ou « choix différé » : c'est la meilleure proportionnalité des dix-huit, et elle est fondée sur un observable. Gâchée par quatorze boucles numérotées ayant chacune son budget, et par un appareil de cadrage amputé. | L'**épaississement conditionné par `QUALIFIER_TERRITOIRE`** : le travail supplémentaire va là où l'issue d'une étape reconfigure la suivante, nulle part ailleurs. Le repli sur le dauphin (`CONSERVER_OPTIONS_ECARTEES`) quand `VERIFIER_FAISABILITE_PAR_EXECUTANT` échoue, sans rejouer tout le choix. | Quatorze boucles à budget séparé : un grand-livre, pas une instruction. `BALAYER_EXIGENCES_TACITES`, `RECENSER_CONTRAINTES_DURES`, `RECENSER_PREFERENCES`, `ORDONNER_OBJECTIFS_SANS_ECARTER` absents : rien ne fait remonter le tacite, principes 1 et 6 entamés. `ARBITRER_A_L_AVEUGLE` jamais appelée. |
| **13 — Le tournoi d'options** | 2 | 1 | 3 | 1 | 1 | Chaque option est **développée en plan complet par récursion** avant d'être comparée : explosion combinatoire, et 59 fonctions absentes — ni attendu observable, ni retour arrière, ni ordonnancement, ni provenance, ni gouvernance. C'est un sélecteur d'options déguisé en architecture de planification. | La **boucle d'élimination par fragilité** : tant qu'il reste plusieurs survivantes, on attaque en priorité celle qui porte l'hypothèse la plus fragile — boucle déclenchée par un observable, qui décroît structurellement. La récupération de pièces des branches perdantes avec `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE`. | Payer un plan complet par option pour n'en garder qu'un. Même tournoi récursif sur une demande triviale. Livrer une architecture dont il manque `DEFINIR_ATTENDU_OBSERVABLE` : le plan produit n'est pas vérifiable. |
| **14 — Pipeline à jalons verrouillés** | 4 | 2 | 3 | 2 | 1 | Le plus lisible du lot : huit phases, des portes nettes, une fonction appelée par ligne. C'est aussi le plus pur exemple du défaut annoncé : un catalogue ordonné. Huit portes obligatoires pour une demande de deux lignes, et une PHASE 4 RISQUES verrouillée. | La formulation de terminaison de la phase 2 — « la file décroît à chaque tour, donc elle termine » — est le bon **réflexe** : chercher l'argument dans la structure. Les portes énoncées comme états vérifiables (« aucune inconnue bloquante ouverte, tout fait adossé et daté »). | L'argument de terminaison est aussitôt détruit deux lignes plus bas par `si nouvelles inconnues : file.ajouter()`. `AMORCER_DEPUIS_PLAN_EXISTANT` et `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` absents → principes 12 et 8. Conflit d'objectifs non résolu après 2 essais → `CONSTATER_IMPOSSIBILITE ; FIN` : le système s'arrête de sa propre autorité au lieu de remonter (principe 4). |
| **15 — Cascade à paliers bornés** | 4 | 4 | 4 | 4 | 2 | La meilleure des trois clones : les trois niveaux de confrontation sont des **paliers séquentiels avec droit de retour d'un seul cran**, déclenché par un observable (« le verdict remet en cause la structure »). C'est lisible, c'est ciblé, et ça remonte au bon endroit. Reste un budget décrété et une cérémonie constante. | Le **droit de retour d'exactement un palier**, déclenché par le verdict lui-même, avec `NOMMER_FAIT_QUI_FERAIT_BASCULER` transporté comme fait nouveau et `REUTILISER_ACQUIS` pour ne rien redémontrer. Le budget épuisé n'arrête pas : il déclenche `SOUMETTRE_ARBITRAGE_UTILISATEUR` — l'utilisateur tranche, le système ne s'arrête pas seul. | `budget = {PROBLEME: 1, STRUCTURE: 2}` : les seuls nombres du fichier, et rien ne les justifie. `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` absent → principe 8. `dossier` constitué intégralement avant le premier palier, quelle que soit la demande. |
| **16 — Le pipeline à portes** | 4 | 1 | 3 | 2 | 1 | Très lisible, très complet en surface (126 fonctions), et frappé d'un vice rédhibitoire : il **écrit noir sur blanc** `SI le plan est trop gros ALORS DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER # (non utilisé — voir §exclusions)`. C'est la seule architecture qui refuse par écrit le principe 8. | `tentatives < nb_moyens_disponibles` dans la levée d'inconnue : terminaison par épuisement d'un ensemble fini, pas par plafond. Le routage final de la correction vers la phase responsable selon la nature du défaut (fait→P3, décision→P4, étape→P5, risque→P6). | Exclure la décomposition. Terminer sur `SIGNALER_LES_LIMITES sur le point litigieux` après deux tours : le plan part avec un point ouvert, principe 1 violé. Sept phases obligatoires quelle que soit la demande. |
| **17 — Tournoi adversarial d'options complètes** | 3 | 2 | 3 | 3 | 1 | N plans complets construits, attaqués, puis arbitrés à l'aveugle : le contradictoire est réel mais à un seul niveau, et payé au prix fort. Trente fonctions absentes, dont `ORIENTER_CHOIX`, `ETABLIR_DEPENDANCES_ENTRE_DECISIONS`, `JUGER_PEREMPTION_FAIT`, `BALAYER_EXIGENCES_TACITES` et `AMORCER_DEPUIS_PLAN_EXISTANT`. | Le **socle de faits partagé** établi avant les concurrents, que chaque option `REUTILISER_ACQUIS` sans le redémontrer : les options diffèrent par la méthode, pas par leur base factuelle. Le repli sur le dauphin quand la faisabilité échoue, qui **rejoue la phase 6 seule et pas le tournoi**. | `o.squelette = DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(o)` : la décomposition détournée en simple mise en forme d'une option. Même tournoi complet quelle que soit la demande. `AMORCER_DEPUIS_PLAN_EXISTANT` absent. |
| **18 — Vagues par dépendances** | 2 | 3 | 4 | 4 | 3 | Vagues topologiques sur un graphe de décisions, chaque vague enchaînant enquête / décision / construction locales. L'organisation est cohérente et la répétition est la mieux motivée du lot, mais elle exige de tenir un graphe vivant, de rouvrir des vagues fermées et de compter des budgets d'arêtes. | Le **meilleur argument de terminaison des dix-huit** : `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` ne peut que gagner des arêtes correctes, jamais en reperdre, donc au plus E corrections — c'est structurel, pas décrété. `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE` marquant la vague d'origine, ce qui rend les retours ultérieurs réellement ciblables. | Faire calculer et recalculer des couches sur un graphe mutable. `AMORCER_DEPUIS_PLAN_EXISTANT` absent → principe 12 ; `DECIDER_D_OUVRIR_UN_AGENT` absent alors que des agents sont lancés → principe 5 (cadre autorisé) contourné. Phase C d'assurance globale démesurée. |

**Constats transversaux, qui gouvernent la suite.** Aucune des dix-huit ne fixe le format du plan livré (principe 10) — c'est un angle mort total. Aucune n'exploite le fait, pourtant écrit dans `REDIGER_BRIEF_AGENT`, qu'**un agent qui juge reçoit les critères ET le besoin** : l'arbitre n'est jamais un agent briefé, c'est toujours le planificateur qui s'auto-arbitre en se déclarant aveugle. Aucune ne traite le plan existant comme un **concurrent** au niveau structure — toutes appellent `AMORCER_DEPUIS_PLAN_EXISTANT` puis l'oublient. Onze sur dix-huit terminent sur un `SIGNALER_LES_LIMITES` ou un `CONSTATER_IMPOSSIBILITE` de leur propre autorité, ce qui viole ensemble les principes 1 et 4. Et treize sur dix-huit imposent une cérémonie constante.

---

# DEUXIÈME PARTIE — PRÉ-CONSTRUCTION

**A — Le greffe.** Cherche à réussir l'**exhaustivité vérifiable** : qu'aucune question ne survive dans le plan livré, et qu'on puisse le prouver. Principe d'organisation : trois registres écrits — l'énoncé, les inconnues, les choix litigieux — qui s'ouvrent dans cet ordre et se ferment par **vidage**, chaque item n'en sortant que muni d'une quittance légale. L'état des boucles n'est pas une variable à tenir de tête : c'est un document sous les yeux du modèle. La terminaison découle du fait qu'un registre ne peut être rouvert que par un fait nommé, absent du registre des faits, et que ce registre ne fait que croître.

**B — Les contrats emboîtés.** Cherche à réussir la **taille** : planifier un travail qui ne tient pas dans une seule tête, sans jamais refuser ni bâcler. Principe d'organisation : le travail est découpé en contrats — périmètre, faits d'entrée, cible observable, termes figés, interfaces promises aux autres contrats — chacun planifié isolément par la même procédure, puis recomposé par vérification des jonctions. Sa singularité est que le deuxième niveau de concurrence ne porte pas sur un squelette mais sur **le découpage lui-même** : des jeux de contrats rivaux s'affrontent à l'aveugle. La récursion termine par containment strict des périmètres ; la renégociation d'un contrat termine parce qu'elle ne peut que **figer** un degré de liberté, jamais en rendre.

**C — Le brouillon-sonde.** Cherche à réussir la **proportionnalité et la chasse au tacite** : que le volume de travail soit dicté par ce que le sujet contient, et que rien d'important ne soit supposé en silence. Principe d'organisation : on écrit d'abord le chemin le plus court — une sonde, explicitement jetable, jamais livrée — puis on **l'interrogé ligne à ligne** ; chaque ligne rend ce qu'elle présuppose, ce qu'elle choisit sans le dire, et ce qui dirait qu'elle a réussi. La sonde est le générateur du plan de travail, pas un brouillon à rafistoler : le plan livré est réécrit depuis les décisions closes. La terminaison est structurelle parce qu'on n'interroge qu'un texte fini, une fois par version, et qu'une nouvelle version exige qu'une décision close ait modifié le squelette.

Les trois visent des choses différentes : prouver qu'on n'a rien omis ; tenir un travail trop gros ; ne payer que ce que le sujet coûte. Aucune ne transige sur les treize principes.

---

## Règles communes aux trois

Elles ne sont pas une architecture : ce sont quatre invariants que les trois respectent, énoncés une fois pour n'être pas répétés trois fois.

```
R1 — QUITTANCE
  Un item ne quitte un registre, un contrat ou une interrogation qu'avec
  QUALIFIER_ETAT_RESOLUTION ∈ { tranché, tranché avec compromis, branché }.
  « en attente »   → FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE
  « non résolu »   → CONSTATER_IMPOSSIBILITE ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
  « invalide »     → l'item retourne à l'énoncé, porteur du fait qui l'invalide
  Aucune de ces trois issues n'arrête le système de sa propre autorité :
  seul DECLINER_SI_PAS_DE_PLAN arrête, et seulement à la porte.
  Conséquence directe : un plan livré ne contient jamais de point ouvert.

R2 — ARBITRE BRIEFÉ
  Tout ARBITRER_A_L_AVEUGLE est rendu par un contexte ouvert pour cela :
    DECIDER_D_OUVRIR_UN_AGENT ; RESPECTER_CADRE_AUTORISE
    REDIGER_BRIEF_AGENT(arbitre) ← DEFINIR_CRITERES_ACCEPTATION ordonnés + le besoin
                                   + les propositions anonymisées + les attaques subies
                                   ‑ jamais la provenance, jamais les plaidoyers
    BORNER_UN_AGENT ; INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
  Précédence = critères d'acceptation ordonnés, puis RECENSER_CONTRAINTES_DURES.
  Jamais le nombre de voix. L'arbitre n'a pas produit les propositions : c'est ce
  qui le distingue de celui qui les a écrites.

R3 — CHAMP D'UN SEUL
  Un niveau de concurrence n'est jamais sauté.
  Quand PRODUIRE_OPTIONS_DISTINCTES + GARANTIR_DIVERSITE_METHODE +
  CHERCHER_APPROCHES_NON_ENVISAGEES ne rendent qu'une proposition matériellement
  distincte, le niveau s'exécute comme ATTAQUER_TOUT_LE_CHAMP sur ce champ d'un seul,
  et le verdict est consigné par CONSIGNER_CE_QUI_A_TRANCHE.
  La proportionnalité vient du NOMBRE D'OBJETS soumis à un niveau — observable —
  jamais d'une estimation d'effort.

R4 — CADRE
  LIRE_TECHNIQUES_AUTORISEES fixe le nombre et le type d'agents par fonction : c'est
  la seule borne. EVALUER_EXIGENCE_TACHE choisit, PARMI les techniques autorisées,
  celles que cette tâche mérite, sur observables seuls :
    QUALIFIER_FORME_TRAVAIL, QUALIFIER_TERRITOIRE, nombre de choix litigieux rendus
    par ORIENTER_CHOIX, existence de contraintes dures ou d'obligations formelles.
  Elle ne peut jamais retirer un niveau de concurrence sur un objet qui existe.
  RESPECTER_CADRE_AUTORISE garde chaque ouverture d'agent.

F — FORMAT FIXE DU PLAN LIVRÉ (identique dans les trois ; seul le contenu grossit)
  1. Objectif — la cible observable, et rien d'autre.
  2. Étapes ordonnées — par étape : l'action ; l'attendu observable.
     Et seulement là où un marqueur l'exige : signaux d'échec, autorisation,
     branche conditionnelle, re-vérification d'un fait périssable.
  3. Limites et hors-plan.
  4. Suite en cas de succès.
  Ce qui a tranché, ce qui a été vérifié, ce qui a été attaqué : fichier séparé.
```

---

# TROISIÈME PARTIE — LES TROIS ARCHITECTURES

## A — LE GREFFE

**Principe en une phrase.** Trois registres écrits s'ouvrent dans l'ordre — l'énoncé, les inconnues, les choix litigieux — et le plan ne s'écrit que lorsque les trois sont vides, aucun item n'ayant pu en sortir sans quittance.

```
═══ PORTE ═════════════════════════════════════════════════════════════════
LIRE_TECHNIQUES_AUTORISEES ; INVENTORIER_CAPACITES ; IDENTIFIER_DESTINATAIRE
RECENSER_RESSOURCES_EXECUTION
SI l'entrée est un plan existant :
    AMORCER_DEPUIS_PLAN_EXISTANT              # le besoin est dérivé du plan
    conserver le plan source : il concourra au registre II (anonymisé)
SINON :
    SEPARER_DEMANDE_ET_BESOIN
QUALIFIER_FORME_TRAVAIL ; QUALIFIER_TERRITOIRE
SI aucun problème de planification n'est posé :
    DECLINER_SI_PAS_DE_PLAN ; FIN             # seul arrêt de sa propre autorité
EVALUER_EXIGENCE_TACHE                        # cf. R4

═══ BLOC CONFRONTER(question, pièces) — appelé aux trois niveaux ═══════════
FONCTION CONFRONTER(question, pièces_du_greffe) :
    ISOLER_LES_EVALUATIONS
    propositions = PRODUIRE_OPTIONS_DISTINCTES(question)
    GARANTIR_DIVERSITE_METHODE ; CHERCHER_APPROCHES_NON_ENVISAGEES
    CHERCHER_ANTECEDENTS → une proposition peut naître d'un antécédent
    POUR chaque proposition :
        SI le cadre autorise un contexte séparé :
            DECIDER_D_OUVRIR_UN_AGENT ; RESPECTER_CADRE_AUTORISE
            REDIGER_BRIEF_AGENT(périmètre, faits établis, question, format ; rien qui oriente)
            BORNER_UN_AGENT ; INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
        EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
        SI une hypothèse est une inconnue non levée :
            → item du REGISTRE II, et la proposition attend sa fermeture
    CHOISIR_ANGLES_ATTAQUE
    POUR chaque proposition : ATTAQUER_UNE_OPTION(action + faits seuls, jamais le plaidoyer)
    ATTAQUER_TOUT_LE_CHAMP                               # cf. R3 : vaut aussi pour un champ d'un seul
    SI tout le champ tombe :
        CONSTATER_IMPOSSIBILITE ; PRESENTER_ALTERNATIVES_AU_CHOIX
        SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE       # jamais un arrêt décidé seul
    QUALIFIER_INDEPENDANCE_OBTENUE ; DETECTER_ERREURS_CORRELEES
    verdict = ARBITRER_A_L_AVEUGLE(...)                  # cf. R2
    CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_PORTEE_DECISION
    NOMMER_FAIT_QUI_FERAIT_BASCULER ; CONSERVER_OPTIONS_ECARTEES
    POUR toute pièce du verdict qu'aucune proposition ne portait :
        RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
    QUALIFIER_ETAT_RESOLUTION(verdict)                   # cf. R1
    RETOURNER verdict

═══ REGISTRE I — L'ÉNONCÉ ═════════════════════════════════════════════════
ouvrir le registre, une ligne par pièce :
    DELIMITER_PERIMETRE ; ETABLIR_ETAT_ACTUEL
    ORDONNER_OBJECTIFS_SANS_ECARTER            # ordonne, n'abandonne aucun objectif
    RECENSER_CONTRAINTES_DURES ; RECENSER_INVARIANTS
    RECENSER_OBLIGATIONS_FORMELLES ; RECENSER_PREFERENCES
    RECENSER_DEPENDANCES_EXTERNES
    CHERCHER_ANTECEDENTS → REUTILISER_ACQUIS   # ne pas redémontrer l'acquis encore valide

passer le registre au crible — chaque trouvaille devient un item :
    CONTESTER_ENONCE_PROBLEME ; DETECTER_SOLUTION_IMPOSEE
    TRAQUER_AJOUTS_SILENCIEUX ; DEBUSQUER_HYPOTHESES_IMPORTEES
    DETECTER_CONFLIT_OBJECTIFS                 # symptôme, pas arbitrage à rendre
    EXPOSER_EXTERNALITES_CERTAINES
    BALAYER_EXIGENCES_TACITES                  # remonter et demander, jamais imposer

items qui appellent une réponse de l'utilisateur (exigence tacite, conflit d'objectifs,
externalité, obligation formelle, préférence) :
    DECIDER_D_INTERROGER_UTILISATEUR ; FORMULER_QUESTION_ACTIONNABLE (une par item)
    → UN SEUL envoi groupé : SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE
    (aucune valeur par défaut ; à la réponse, chaque item reçoit sa quittance)

CONFRONTER(« quel problème planifie-t-on ? », registre I)       ← NIVEAU 1
    pièces mises en concurrence : les lectures rivales du besoin, y compris celle
    portée par le plan source si l'entrée est un plan existant

FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
VERIFIER_FIDELITE_CIBLE_BESOIN
    SI la cible est satisfaisable sans produire l'effet voulu :
        l'écart nomme soit un critère manquant, soit une contrainte dure non recensée ;
        cette pièce entre au registre I et la cible est reformulée.
        (l'ensemble des critères ne fait que croître : l'espace des cibles admissibles
         ne fait que se restreindre — pas de plafond, pas de cycle)
CHAINER_ETAT_ACTUEL_VERS_CIBLE                 # en descendant ET en remontant

FERMETURE I : chaque item porte une quittance. Sinon → R1.

═══ REGISTRE II — LES INCONNUES ═══════════════════════════════════════════
ouvrir : RECENSER_INCONNUES(registre I + le chaînage)
POUR chaque item :
    CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION
    QUALIFIER_PORTEE_INCONNUE ; DISTINGUER_INDETERMINE_ET_NON_CHERCHE
ORDONNER_INCONNUES_SANS_ECARTER                # par portée, puis prérequis ; on n'écarte rien
AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE            # départage les ex æquo

items classés « exécution » : quittance « branché » immédiate ; ils n'appellent pas
    de levée, ils appelleront CONSTRUIRE_BRANCHE_CONDITIONNELLE à la construction.

items classés « construction » :
    regrouper par domaine d'enquête séparable
    SI le cadre l'autorise ET plusieurs domaines :
        PARALLELISER_ENQUETE : un agent par domaine
        POUR chaque : REDIGER_BRIEF_AGENT(les faits déjà établis y voyagent) ;
                      BORNER_UN_AGENT ; RESPECTER_CADRE_AUTORISE
        POUR chaque retour : INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
        ARRETER_ORCHESTRATION                  # terminateur : un agent de plus ne change rien
    POUR chaque item non levé :
        TANT QUE non levé ET il reste un moyen non essayé :
            CHOISIR_MOYEN_DE_LEVEE(parmi les moyens non encore essayés)
              inspection / calcul / mesure → MENER_VERIFICATION
              source, précédent            → CHERCHER_ANTECEDENTS
              action bornée et réversible  → LEVER_INCONNUE_PAR_ACTION_REVERSIBLE
              question                     → DECIDER_D_INTERROGER_UTILISATEUR ;
                                             FORMULER_QUESTION_ACTIONNABLE (groupée)
        # terminaison : l'ensemble des moyens est fini et décroît. Pas de plafond.
        SI épuisé : DISTINGUER_INDETERMINE_ET_NON_CHERCHE
            vraiment indéterminable maintenant → reclasser « exécution » (quittance branché)
            sinon                              → SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE

    POUR chaque fait obtenu :
        CONSIGNER_PROVENANCE_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE ; ENONCER_LIMITES_FAIT
        JUGER_PEREMPTION_FAIT → si périssable : INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
        SI plusieurs sources : DETECTER_CONTRADICTION_ENTRE_SOURCES
            → DETECTER_ORIGINE_COMMUNE_SOURCES → RESOUDRE_CONTRADICTION
              (date, version, périmètre, définition — ou item « contesté » qui reste ouvert)
        SI des sources convergent : DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
        RENDRE_INCERTITUDE_VISIBLE
        SI le fait contredit une pièce du registre I :
            rouvrir CETTE pièce seule, le fait inscrit à côté d'elle ;
            REUTILISER_ACQUIS pour tout le reste du registre I
            (un même fait ne peut rouvrir deux fois la même pièce : c'est écrit au registre)

FERMETURE II : registre vide.

CONFRONTER(« quel découpage relie l'état actuel à la cible ? », I + II)   ← NIVEAU 2
    la diversité de méthode est obtenue par construction, non par déclaration :
      un concurrent descend de la cible, un remonte de l'état actuel,
      un est tiré de CHERCHER_ANTECEDENTS, et le plan source s'il y en a un.
SI une étape du découpage retenu ne peut recevoir un attendu observable unique
   sans devenir elle-même un plan :
    DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER sur cette étape ;
    chaque sous-plan ouvre son propre registre III et sa propre construction,
    recomposés avant le contrôle final. (jamais de refus pour cause de taille)

═══ REGISTRE III — LES CHOIX LITIGIEUX ════════════════════════════════════
ouvrir : ORIENTER_CHOIX(découpage retenu) — chaque point est trié :
    « il manque un fait »          → item du REGISTRE II ; on referme II ; on revient ici
    « il faut une préférence »     → FORMULER_QUESTION_ACTIONNABLE (envoi groupé) ; ATTENDRE
    « vrai choix à instruire »     → item du REGISTRE III
DISTINGUER_CHOIX_ET_CONSEQUENCE
    avant d'écarter une conséquence mécanique :
    DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE ; CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
ETABLIR_DEPENDANCES_ENTRE_DECISIONS            # ordre de tranchage du registre

POUR chaque item, dans cet ordre :
    CONFRONTER(l'item, I + II + découpage)                                 ← NIVEAU 3
    SI le verdict nomme un fait absent du registre des faits :
        ce fait devient un item du REGISTRE II ; II se referme ; on reprend ici
        (terminaison : le fait doit être NOUVEAU, vérifiable contre le registre,
         et le registre des faits ne fait que croître)
    SI le verdict est « tranché avec compromis » :
        SOUMETTRE_ARBITRAGE_UTILISATEUR(le compromis matériel) ; ATTENDRE
        # l'utilisateur voit le compromis AVANT que le plan ne le referme

FERMETURE III : registre vide.
VERIFIER_COHERENCE_ENSEMBLE(décisions)         # de bons morceaux peuvent ne pas tenir ensemble

═══ CONSTRUCTION ══════════════════════════════════════════════════════════
DERIVER_ACTIONS_DEPUIS_DECISIONS
ORDONNER_PAR_PREREQUIS ; AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE (départage)
IDENTIFIER_ETAPES_SIMULTANEES → VERIFIER_SIMULTANEITE_POSSIBLE
                                 (ressource, verrou, approbateur, précondition cachée)
POUR chaque étape : DEFINIR_ATTENDU_OBSERVABLE
CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
POUR chaque item quittancé « branché » : CONSTRUIRE_BRANCHE_CONDITIONNELLE
POUR chaque fait périssable : placer la re-vérification juste avant l'étape qui en dépend

— appareil mineur, posé seulement là où un observable le réclame —
REPERER_POINTS_ENGAGEMENT                      # ferme une option, consomme une ressource
SUR CES POINTS SEULEMENT :
    QUALIFIER_REVERSIBILITE ; DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE
    DEFINIR_SIGNAUX_ECHEC ; PLACER_POINTS_VERIFICATION
    RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT
    SI un acteur touché peut s'adapter : ANTICIPER_TIERS_REACTIF
    STATUER_SUR_RISQUE_RESIDUEL
      tout risque « accepté » ou « délégué » → SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
SI RECENSER_OBLIGATIONS_FORMELLES non vide OU un point irréversible existe :
    PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION (jamais l'exécutant)
    VERIFIER_COUVERTURE_BLOQUANTS
SI le destinataire comprend un suiveur humain : PLACER_JALONS_CONSTAT
SI RECENSER_RESSOURCES_EXECUTION a trouvé personnes, délais ou budget :
    une seule offre groupée : PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE ; PROPOSER_MARGES

═══ CONTRÔLE ET ÉMISSION ══════════════════════════════════════════════════
VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN (branches comprises)
VERIFIER_COHERENCE_ENSEMBLE ; VERIFIER_ADOSSEMENT_AFFIRMATIONS ; REFUSER_AUTO_CONFIRMATION
VERIFIER_FAISABILITE_PAR_EXECUTANT (accès, outils, contexte que le plan présuppose)
REDIGER_PLAN(format F) ; ELAGUER_LA_PROSE ; RENDRE_ACTIONNABLE_PAR_AGENT
SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN ; PREVOIR_SUITE_EN_CAS_DE_SUCCES
CONTROLER_CONTENU_FINAL ; CONTROLER_INTEGRITE_DOCUMENT
FAIRE_CONTROLER_PAR_UN_TIERS (brief = plan + critères ; jamais la traçabilité)
    INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
    DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
CHAQUE finding devient un item du registre que sa nature désigne :
    prémisse fausse → I ; fait douteux → II ; décision mal fondée → III ;
    défaut de rédaction → corrigé ici.
    Il s'y ferme par la règle de ce registre. Pas de boucle spéciale, pas de compteur.
REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER ; RESTITUER_EN_BREF
```

**Boucles.** Cinq, toutes déclenchées par de l'observable. *(1) Fidélité cible/besoin* : déclenchée par l'échec de `VERIFIER_FIDELITE_CIBLE_BESOIN`, remonte au registre I ; termine parce que chaque tour ajoute un critère ou une contrainte et ne retire jamais rien — l'espace des cibles admissibles se restreint de façon monotone, et son épuisement est observable (`CONSTATER_IMPOSSIBILITE` → utilisateur). *(2) Levée d'une inconnue* : déclenchée par l'échec du moyen essayé, remonte au choix du moyen ; termine par épuisement d'un ensemble fini de moyens, jamais par plafond. *(3) Réouverture du registre I par un fait* : déclenchée par la contradiction constatée entre un fait établi et une pièce du cadrage, remonte à cette pièce seule ; termine parce que le couple (pièce, fait) est écrit au registre et ne se rejoue pas. *(4) Registre III → registre II* : déclenchée par un verdict qui **nomme** un fait absent du registre des faits ; termine parce que ce registre ne fait que croître et que la nouveauté du fait est vérifiable par lecture. *(5) Contrôle final* : déclenchée par un finding, remonte au registre désigné par la nature du finding — et s'y dissout, puisqu'elle devient un item ordinaire. Aucune boucle n'a de budget.

**Fonctions rappelées, et pourquoi.** `CONFRONTER` aux trois niveaux, sur trois objets qui attrapent trois erreurs différentes : planifie-t-on la bonne chose, le découpage est-il le bon, ce choix-ci est-il le bon. `RECENSER_INCONNUES` à l'ouverture du registre II, puis après le verdict de structure — un découpage retenu nomme des inconnues que le précédent ne nommait pas. `REUTILISER_ACQUIS` à chaque réouverture, pour que la réouverture reste ponctuelle. `VERIFIER_COHERENCE_ENSEMBLE` deux fois, sur deux objets distincts : l'ensemble des décisions, puis le document. `REFUSER_AUTO_CONFIRMATION` sur chaque retour d'agent et sur le tiers relecteur. `CONSIGNER_PROVENANCE_FAIT`, `ENONCER_LIMITES_FAIT`, `SEPARER_OBSERVE_ET_SUPPOSE`, `JUGER_PEREMPTION_FAIT` : une fois par fait, c'est le régime unique des faits. `FORMULER_QUESTION_ACTIONNABLE` autant de fois qu'il y a de questions, mais `SUSPENDRE_ENQUETE_ET_DEMANDER` une fois par lot — l'utilisateur est interrompu par vagues, pas par questions.

**Fonctions laissées de côté.** A n'en exclut aucune de façon absolue, et c'est délibéré : son objet est de prouver qu'aucune question ne subsiste, et toute exclusion absolue serait une faille dans cette preuve. Six sont **non appelées sous condition nommée et observable** : `LEVER_INCONNUE_PAR_ACTION_REVERSIBLE` si `INVENTORIER_CAPACITES` ne rend aucun accès en écriture au système cible ; `PARALLELISER_ENQUETE` et `ARRETER_ORCHESTRATION` si le cadre n'autorise pas les agents ou s'il n'existe qu'un domaine d'enquête ; `ANTICIPER_TIERS_REACTIF` si `RECENSER_DEPENDANCES_EXTERNES` ne rend aucun acteur capable de s'adapter ; `PLACER_JALONS_CONSTAT` si le destinataire n'est qu'un agent exécutant — l'attendu observable de chaque étape est alors déjà le constat, et le jalon dupliquerait `DEFINIR_ATTENDU_OBSERVABLE` ; `DESIGNER_AUTORITE_AUTORISATION` et `PLACER_POINTS_AUTORISATION` si aucune obligation formelle n'a été recensée et qu'aucun point n'est irréversible. Le prix honnête de cette non-exclusion : A est la plus lourde des trois, et ne doit pas être le régime par défaut.

**Cas d'emploi.** Territoire non familier, enjeu élevé, plan à une seule cartouche, plusieurs parties prenantes capables de bloquer, ou contexte où il faudra rendre compte de ce qui a été vérifié et de ce qui ne l'a pas été. C'est l'architecture de l'audit.

---

## B — LES CONTRATS EMBOÎTÉS

**Principe en une phrase.** Le travail est découpé en contrats — et c'est le découpage lui-même, pas un squelette, qui est mis en concurrence à l'aveugle — chaque contrat étant planifié isolément par la même procédure puis recomposé par vérification des jonctions.

```
CONTRAT = { périmètre ;
            faits d'entrée (établis, avec provenance) ;
            cible observable + critères d'acceptation ;
            contraintes dures et invariants hérités ;
            interfaces : ce que ce contrat promet aux autres, ce qu'il attend d'eux ;
            termes figés : les degrés de liberté déjà retirés }

═══ RACINE — fonctions réservées à la racine ══════════════════════════════
LIRE_TECHNIQUES_AUTORISEES ; INVENTORIER_CAPACITES ; IDENTIFIER_DESTINATAIRE
RECENSER_RESSOURCES_EXECUTION ; EVALUER_EXIGENCE_TACHE
SI l'entrée est un plan existant : AMORCER_DEPUIS_PLAN_EXISTANT (besoin dérivé du plan)
SINON : SEPARER_DEMANDE_ET_BESOIN
QUALIFIER_FORME_TRAVAIL
SI pas de problème de planification : DECLINER_SI_PAS_DE_PLAN ; FIN

DELIMITER_PERIMETRE ; ETABLIR_ETAT_ACTUEL ; QUALIFIER_TERRITOIRE
ORDONNER_OBJECTIFS_SANS_ECARTER ; DETECTER_CONFLIT_OBJECTIFS
RECENSER_CONTRAINTES_DURES ; RECENSER_INVARIANTS
RECENSER_OBLIGATIONS_FORMELLES ; RECENSER_PREFERENCES ; RECENSER_DEPENDANCES_EXTERNES
CONTESTER_ENONCE_PROBLEME ; DETECTER_SOLUTION_IMPOSEE ; TRAQUER_AJOUTS_SILENCIEUX
DEBUSQUER_HYPOTHESES_IMPORTEES ; EXPOSER_EXTERNALITES_CERTAINES
BALAYER_EXIGENCES_TACITES
CHERCHER_ANTECEDENTS → REUTILISER_ACQUIS

toute question née ici : DECIDER_D_INTERROGER_UTILISATEUR ; FORMULER_QUESTION_ACTIONNABLE
→ envoi unique : SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE

CONFRONTER(« quel problème planifie-t-on ? »)                          ← NIVEAU 1
FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
VERIFIER_FIDELITE_CIBLE_BESOIN                # échec → ajoute un critère/une contrainte
CHAINER_ETAT_ACTUEL_VERS_CIBLE

# --- socle : les inconnues qui changeraient le DÉCOUPAGE, et elles seules ---
RECENSER_INCONNUES(à l'échelle du découpage)
POUR chaque : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION ; QUALIFIER_PORTEE_INCONNUE
retenir celles dont la portée est « change le découpage » (ORDONNER_INCONNUES_SANS_ECARTER) ;
les autres sont léguées aux contrats, non perdues.
les lever par LEVER_UNE_INCONNUE (bloc ci-dessous)
socle = faits établis + leur provenance   # aucun contrat ne les redémontrera

CONFRONTER(« quel jeu de contrats ? »)                                 ← NIVEAU 2
    concurrents = jeux de contrats rivaux, produits par
        DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER sous des principes de partition différents :
          par objectif | par système touché | par domaine d'inconnue |
          par irréversibilité (isoler ce qui ferme des options) |
          + le découpage du plan source, anonymisé, si l'entrée était un plan
    GARANTIR_DIVERSITE_METHODE est satisfait par construction, pas déclaré.
    CHOISIR_ANGLES_ATTAQUE d'un découpage = ses interfaces :
        quel fait doit traverser une frontière ? quel contrat ne peut conclure
        sans connaître le verdict d'un autre ? quelle contrainte dure est coupée en deux ?
    ATTAQUER_UNE_OPTION par découpage ; ATTAQUER_TOUT_LE_CHAMP sur l'ensemble
    ARBITRER_A_L_AVEUGLE (R2) ; CONSERVER_OPTIONS_ECARTEES
ETABLIR_DEPENDANCES_ENTRE_DECISIONS → ORDONNER_PAR_PREREQUIS(contrats)
    les contrats qui PRODUISENT un fait attendu par d'autres passent devant

POUR chaque contrat, dans cet ordre :  HONORER(contrat)
    SI le cadre autorise les agents ET deux contrats ne partagent aucune interface :
        PARALLELISER_ENQUETE ; REDIGER_BRIEF_AGENT(contrat + socle) ; BORNER_UN_AGENT
        RESPECTER_CADRE_AUTORISE ; INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
        ARRETER_ORCHESTRATION

═══ HONORER(contrat) — la même procédure à toute profondeur ═══════════════
FONCTION HONORER(contrat) :
    REUTILISER_ACQUIS(socle + faits des contrats amont)   # jamais redémontré
    RECENSER_INCONNUES(périmètre du contrat)
    POUR chaque : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION ; QUALIFIER_PORTEE_INCONNUE
                  DISTINGUER_INDETERMINE_ET_NON_CHERCHE
    ORDONNER_INCONNUES_SANS_ECARTER ; AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE
    SI une inconnue a une portée qui DÉBORDE le périmètre du contrat :
        ne pas la trancher ici → défaut de contrat (voir plus bas)
    POUR les autres : LEVER_UNE_INCONNUE
    inconnues « exécution » : quittance « branché », léguées à la construction

    points = ORIENTER_CHOIX(contrat)
    DISTINGUER_CHOIX_ET_CONSEQUENCE
      conséquence mécanique → DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE ;
                              CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
      fait manquant         → LEVER_UNE_INCONNUE, puis reprendre le point
      préférence            → question mise en réserve, remontée à la racine (jamais posée ici)

    # --- division : par autonomie décisionnelle, jamais par taille estimée ---
    SI les choix litigieux restants forment PLUS D'UNE famille dont les inconnues
       appartiennent à des domaines disjoints :                       # observable
        sous_contrats = DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(contrat)
            chaque sous-contrat : DELIMITER_PERIMETRE(hérite strictement du parent)
                                  faits d'entrée = socle + faits du parent
                                  cible = FORMULER_CIBLE_OBSERVABLE locale
                                          + DEFINIR_CRITERES_ACCEPTATION locaux
                                  termes figés hérités
        POUR chaque : HONORER(sous_contrat)
        RECOMPOSER(sous_contrats)
    SINON :                                                           # feuille
        POUR chaque choix litigieux, en ordre de dépendance :
            CONFRONTER(le choix, contrat + socle)                     ← NIVEAU 3
            SI verdict « tranché avec compromis » → compromis mis en réserve pour la racine
        DERIVER_ACTIONS_DEPUIS_DECISIONS ; ORDONNER_PAR_PREREQUIS
        POUR chaque étape : DEFINIR_ATTENDU_OBSERVABLE
        CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
        RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
        POUR chaque inconnue branchée : CONSTRUIRE_BRANCHE_CONDITIONNELLE
        VERIFIER_COUVERTURE_OBJECTIFS(objectifs du contrat)

    SI le contrat ne peut être honoré tel qu'il est écrit :
        CONSTATER_IMPOSSIBILITE(local)
        RETOURNER défaut_de_contrat(terme à modifier, fait qui l'impose)
    RETOURNER fragment de plan + faits produits + interfaces tenues

═══ LEVER_UNE_INCONNUE — bloc commun ══════════════════════════════════════
TANT QUE non levée ET il reste un moyen non essayé :
    CHOISIR_MOYEN_DE_LEVEE → MENER_VERIFICATION | CHERCHER_ANTECEDENTS |
                             LEVER_INCONNUE_PAR_ACTION_REVERSIBLE |
                             agent (DECIDER_D_OUVRIR_UN_AGENT ; REDIGER_BRIEF_AGENT ;
                                    BORNER_UN_AGENT ; INTEGRER_RETOUR_AGENT ;
                                    REFUSER_AUTO_CONFIRMATION) |
                             question (mise en réserve pour la racine)
SI épuisé : DISTINGUER_INDETERMINE_ET_NON_CHERCHE → reclasser « exécution » ou défaut de contrat
fait obtenu : CONSIGNER_PROVENANCE_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE ; ENONCER_LIMITES_FAIT
              JUGER_PEREMPTION_FAIT → INSCRIRE_REVERIFICATION_FAIT_PERISSABLE si périssable
              DETECTER_CONTRADICTION_ENTRE_SOURCES → DETECTER_ORIGINE_COMMUNE_SOURCES
                                                   → RESOUDRE_CONTRADICTION
              DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
              RENDRE_INCERTITUDE_VISIBLE

═══ RECOMPOSER(contrats) ══════════════════════════════════════════════════
fusionner les fragments ; ORDONNER_PAR_PREREQUIS à travers les frontières
IDENTIFIER_ETAPES_SIMULTANEES → VERIFIER_SIMULTANEITE_POSSIBLE
    (deux contrats « parallèles » qui se disputent un approbateur ne le sont pas)
VERIFIER_COHERENCE_ENSEMBLE ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN
SI incohérence : elle nomme DEUX contrats et l'interface qui les sépare.
    Cette interface devient un TERME FIGÉ chez les deux.
    REUTILISER_ACQUIS ; HONORER ces deux contrats seulement.
    (l'ensemble des termes figés ne fait que croître : la renégociation termine)
SI un défaut_de_contrat remonte :
    le parent FIGE le terme nommé (il retire un degré de liberté, il n'en rend jamais)
    et rejoue HONORER sur ce seul enfant.
    SI honorer le contrat exigerait de RELÂCHER un terme déjà figé, ou une contrainte
    dure, ou un objectif : ce n'est plus une renégociation — c'est une escalade.
    → mise en réserve pour la racine.

═══ CLÔTURE — racine seule ════════════════════════════════════════════════
questions et compromis mis en réserve par tous les contrats :
    FORMULER_QUESTION_ACTIONNABLE chacun ; PRESENTER_ALTERNATIVES_AU_CHOIX si deux options
    → UN SEUL SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
    (un contrat ne parle jamais à l'utilisateur : sans cela, N contrats le harcèlent)
appareil mineur, posé là où un observable le réclame — identique à A :
    REPERER_POINTS_ENGAGEMENT → sur ces points seuls : QUALIFIER_REVERSIBILITE ;
    DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE ; DEFINIR_SIGNAUX_ECHEC ;
    PLACER_POINTS_VERIFICATION ; RECENSER_RISQUES_PAR_ORIGINE ;
    QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT ;
    ANTICIPER_TIERS_REACTIF (si un acteur peut s'adapter) ; STATUER_SUR_RISQUE_RESIDUEL
    — tout résidu accepté ou délégué remonte au lot de questions ci-dessus
SI obligations formelles OU point irréversible :
    PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION ; VERIFIER_COUVERTURE_BLOQUANTS
PLACER_JALONS_CONSTAT si un humain suit l'exécution
SI ressources d'exécution : offre groupée PROPOSER_AFFECTATION / CHIFFRAGE / MARGES
VERIFIER_COUVERTURE_OBJECTIFS (globale) ; VERIFIER_ADOSSEMENT_AFFIRMATIONS
VERIFIER_FAISABILITE_PAR_EXECUTANT ; REFUSER_AUTO_CONFIRMATION
REDIGER_PLAN(format F) ; ELAGUER_LA_PROSE ; RENDRE_ACTIONNABLE_PAR_AGENT
SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN ; PREVOIR_SUITE_EN_CAS_DE_SUCCES
CONTROLER_CONTENU_FINAL ; CONTROLER_INTEGRITE_DOCUMENT
FAIRE_CONTROLER_PAR_UN_TIERS → INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
    DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
    chaque finding nomme un contrat → il devient un terme figé, ce contrat est rejoué seul
REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER ; RESTITUER_EN_BREF
```

**Boucles.** Quatre. *(1) Descente* : déclenchée par un observable — plus d'une famille de choix litigieux sur des domaines d'inconnues disjoints ; elle termine parce que le périmètre d'un enfant est strictement contenu dans celui du parent et que la condition de division cesse d'être vraie sur un contrat à une seule famille. Pas de `PROFONDEUR_MAX`. *(2) Renégociation* : déclenchée par un `défaut_de_contrat` qui **nomme** le terme à modifier ; elle remonte d'exactement un cran, au parent qui a écrit le contrat ; elle termine parce qu'une renégociation ne peut que **figer** un terme, jamais en libérer — le nombre de degrés de liberté décroît strictement. *(3) Recomposition* : déclenchée par `VERIFIER_COHERENCE_ENSEMBLE` ou `VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN` en échec, qui nomment deux contrats et leur interface ; l'interface devient un terme figé — même argument monotone. *(4) Levée d'une inconnue* : épuisement des moyens, comme en A. La seule sortie qui n'est pas une boucle est l'escalade : relâcher un terme déjà figé n'est pas une renégociation, c'est une question pour l'utilisateur.

**Fonctions rappelées, et pourquoi.** `HONORER` tout entier, une fois par contrat : c'est la structure même. `DELIMITER_PERIMETRE`, `FORMULER_CIBLE_OBSERVABLE`, `DEFINIR_CRITERES_ACCEPTATION`, `RECENSER_INCONNUES`, `ORIENTER_CHOIX`, `VERIFIER_COUVERTURE_OBJECTIFS` : une fois par contrat, parce qu'un contrat a sa propre cible et ses propres inconnues — c'est ce qui rend l'isolement possible. `REDIGER_BRIEF_AGENT` trois fois par nature : pour un enquêteur, pour un concurrent, pour un arbitre — et le brief de l'arbitre est le seul qui contienne les critères et le besoin. `ORDONNER_PAR_PREREQUIS` à l'intérieur d'un contrat puis à travers les frontières : deux problèmes d'ordre différents. `VERIFIER_COHERENCE_ENSEMBLE` à chaque recomposition, du bas vers le haut. `REUTILISER_ACQUIS` à chaque entrée de contrat — c'est ce qui empêche N contrats de redémontrer le socle.

**Fonctions laissées de côté.** B n'exclut rien globalement mais **interdit huit fonctions hors de la racine**, et l'interdiction est ce qui rend l'architecture viable. `SEPARER_DEMANDE_ET_BESOIN`, `CONTESTER_ENONCE_PROBLEME`, `DETECTER_SOLUTION_IMPOSEE`, `BALAYER_EXIGENCES_TACITES`, `EXPOSER_EXTERNALITES_CERTAINES`, `RECENSER_OBLIGATIONS_FORMELLES` : un contrat qui reconteste le besoin ou rebalaye les exigences tacites détruit le découpage arbitré au niveau 2 et refait N fois le même travail avec N résultats divergents. `SOUMETTRE_ARBITRAGE_UTILISATEUR`, `SUSPENDRE_ENQUETE_ET_DEMANDER`, `PRESENTER_ALTERNATIVES_AU_CHOIX` : un contrat met sa question en réserve et la racine les pose toutes ensemble — sans cette règle, l'utilisateur reçoit dix questions décorrélées pour un seul plan, ce qui viole l'esprit du principe 4 tout en en respectant la lettre. `DECLINER_SI_PAS_DE_PLAN` : un enfant ne décline pas, il renégocie son contrat — décliner est une prérogative de la porte. Hors de la racine, `RECENSER_RESSOURCES_EXECUTION`, `IDENTIFIER_DESTINATAIRE`, `INVENTORIER_CAPACITES` et `LIRE_TECHNIQUES_AUTORISEES` ne sont pas rappelées : leurs réponses sont globales et un enfant qui les recalcule ne peut que diverger.

**Cas d'emploi.** Un travail qui ne tient pas dans une seule tête : plusieurs systèmes, plusieurs domaines d'inconnues, plusieurs cibles partielles. Et le cas, fréquent, où la vraie question litigieuse n'est pas « quelle solution » mais « où passent les frontières » — B est la seule des trois qui mette cette question-là en concurrence.

---

## C — LE BROUILLON-SONDE

**Principe en une phrase.** On écrit d'abord le chemin le plus court comme une sonde explicitement jetable, puis on l'interroge ligne à ligne — chaque ligne rendant ce qu'elle présuppose, ce qu'elle choisit sans le dire et ce qui dirait qu'elle a réussi — et le plan livré est réécrit depuis les décisions closes, jamais rapiécé depuis la sonde.

```
═══ PORTE ═════════════════════════════════════════════════════════════════
LIRE_TECHNIQUES_AUTORISEES ; INVENTORIER_CAPACITES ; IDENTIFIER_DESTINATAIRE
SI l'entrée est un plan existant : AMORCER_DEPUIS_PLAN_EXISTANT
SINON : SEPARER_DEMANDE_ET_BESOIN
QUALIFIER_FORME_TRAVAIL ; QUALIFIER_TERRITOIRE
SI pas de problème de planification : DECLINER_SI_PAS_DE_PLAN ; FIN
EVALUER_EXIGENCE_TACHE                        # R4, sur observables seuls
DELIMITER_PERIMETRE ; ETABLIR_ETAT_ACTUEL
ORDONNER_OBJECTIFS_SANS_ECARTER ; DETECTER_CONFLIT_OBJECTIFS
RECENSER_CONTRAINTES_DURES ; RECENSER_INVARIANTS ; RECENSER_PREFERENCES
RECENSER_OBLIGATIONS_FORMELLES ; RECENSER_DEPENDANCES_EXTERNES ; RECENSER_RESSOURCES_EXECUTION
DETECTER_SOLUTION_IMPOSEE ; CONTESTER_ENONCE_PROBLEME
CHERCHER_ANTECEDENTS → REUTILISER_ACQUIS

CONFRONTER(« quel problème planifie-t-on ? »)                          ← NIVEAU 1
    les concurrents sont des LECTURES rivales du besoin, trois phrases chacune ;
    EXIGER_HYPOTHESES_EXPLICITES sur chacune ; ATTAQUER_UNE_OPTION ;
    ATTAQUER_TOUT_LE_CHAMP ; ARBITRER_A_L_AVEUGLE (R2)
FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION ; VERIFIER_FIDELITE_CIBLE_BESOIN

═══ LA SONDE ══════════════════════════════════════════════════════════════
CONFRONTER(« quel chemin, le plus court possible ? »)                  ← NIVEAU 2
    concurrents = sondes rivales, produites par des méthodes différentes :
      CHAINER_ETAT_ACTUEL_VERS_CIBLE en remontant depuis la cible
      CHAINER_ETAT_ACTUEL_VERS_CIBLE en descendant depuis l'état
      une sonde tirée de CHERCHER_ANTECEDENTS
      le plan source, anonymisé, si l'entrée était un plan existant
    GARANTIR_DIVERSITE_METHODE est obtenu par la méthode de production, pas déclaré.
    CHERCHER_APPROCHES_NON_ENVISAGEES ; EXIGER_HYPOTHESES_EXPLICITES par sonde
    CHOISIR_ANGLES_ATTAQUE ; ATTAQUER_UNE_OPTION ; ATTAQUER_TOUT_LE_CHAMP
    ARBITRER_A_L_AVEUGLE ; CONSERVER_OPTIONS_ECARTEES
sonde = verdict.retenu
    STATUT : instrument d'interrogation. Jamais livrée. Jamais rapiécée.
    Elle ne porte ni attendu, ni retour arrière, ni branche : ce serait la prendre
    pour un plan.

═══ INTERROGATION — le moteur ═════════════════════════════════════════════
RÉPÉTER :
  lignes_neuves = lignes de la sonde jamais encore interrogées
                  (à la première passe : toutes ; ensuite : celles que
                   RATTACHER_TOUTE_PIECE_A_SON_ORIGINE désigne comme nouvelles)
  SI lignes_neuves est vide ET aucun item ouvert : SORTIR

  POUR chaque ligne de lignes_neuves, trois questions :

    (a) « sur quoi cette ligne repose-t-elle ? »
        RECENSER_INCONNUES(ligne) ; DEBUSQUER_HYPOTHESES_IMPORTEES(ligne)
        EXIGER_HYPOTHESES_EXPLICITES(ligne)
        chaque réponse → item INCONNUE
    (b) « cette ligne choisit-elle quelque chose ? »
        ORIENTER_CHOIX(ligne)
          il manque un fait  → item INCONNUE
          il faut une préférence → item QUESTION
          vrai choix à instruire → item CHOIX
        DISTINGUER_CHOIX_ET_CONSEQUENCE
        DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE
          si mécanique : CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
                         (on ne jette une conséquence mécanique qu'après avoir
                          cherché comment on aurait pu faire autrement)
    (c) « qu'est-ce qui dira que cette ligne a réussi ? »
        DEFINIR_ATTENDU_OBSERVABLE(ligne)
          impossible à nommer sans en savoir plus → ce n'est pas une étape,
              c'est une inconnue : item INCONNUE
          nommable seulement en plusieurs observables indépendants → la ligne est
              trop grosse : DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER sur cette ligne,
              le sous-plan devient une sonde traitée par ce même bloc
              (jamais de refus pour cause de taille — la taille se constate ici,
               à l'endroit exact où elle se voit)

  sur la sonde entière, une fois par passe :
    BALAYER_EXIGENCES_TACITES   # dimensions jamais mentionnées : sécurité, charge,
                                 # maintenabilité, accessibilité → items QUESTION
    TRAQUER_AJOUTS_SILENCIEUX   # lignes que personne n'a demandées
    EXPOSER_EXTERNALITES_CERTAINES
    VERIFIER_COUVERTURE_OBJECTIFS   # objectif qu'aucune ligne ne sert → item CHOIX
    VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(sonde)   # invariant franchi → item CHOIX

  # ---- fermeture des items, dans cet ordre ----
  items QUESTION : FORMULER_QUESTION_ACTIONNABLE chacun ;
                   DECIDER_D_INTERROGER_UTILISATEUR (est-ce moins cher de vérifier soi-même ?)
                   → un seul envoi : SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE

  items INCONNUE : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION
      « exécution » → quittance « branché » ; ne bloque rien
      « construction » → QUALIFIER_PORTEE_INCONNUE ; DISTINGUER_INDETERMINE_ET_NON_CHERCHE
          ORDONNER_INCONNUES_SANS_ECARTER ; AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE
          si plusieurs domaines séparables et cadre autorisant :
              PARALLELISER_ENQUETE ; REDIGER_BRIEF_AGENT (les faits acquis y voyagent) ;
              BORNER_UN_AGENT ; RESPECTER_CADRE_AUTORISE ; DECIDER_D_OUVRIR_UN_AGENT ;
              INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION ; ARRETER_ORCHESTRATION
          TANT QUE non levée ET moyen non essayé restant :
              CHOISIR_MOYEN_DE_LEVEE → MENER_VERIFICATION | CHERCHER_ANTECEDENTS |
                                       LEVER_INCONNUE_PAR_ACTION_REVERSIBLE | question
          # épuisement d'un ensemble fini : pas de plafond
          si épuisé : reclasser « exécution », ou SUSPENDRE_ENQUETE_ET_DEMANDER
          fait obtenu : CONSIGNER_PROVENANCE_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE ;
              ENONCER_LIMITES_FAIT ; JUGER_PEREMPTION_FAIT →
              INSCRIRE_REVERIFICATION_FAIT_PERISSABLE si périssable ;
              DETECTER_CONTRADICTION_ENTRE_SOURCES → DETECTER_ORIGINE_COMMUNE_SOURCES
                                                   → RESOUDRE_CONTRADICTION ;
              DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE ;
              RENDRE_INCERTITUDE_VISIBLE
          si le fait invalide la lecture du problème : l'item remonte au NIVEAU 1,
              porteur du fait ; CONFRONTER est rejoué sur ce seul point ; REUTILISER_ACQUIS

  items CHOIX : ETABLIR_DEPENDANCES_ENTRE_DECISIONS (ordre de tranchage)
      POUR chacun : CONFRONTER(le choix, faits + sonde)                ← NIVEAU 3
          CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_PORTEE_DECISION
          NOMMER_FAIT_QUI_FERAIT_BASCULER ; CONSERVER_OPTIONS_ECARTEES
          QUALIFIER_ETAT_RESOLUTION
          si « tranché avec compromis » : SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
          si le verdict nomme un fait absent : il devient un item INCONNUE de cette passe

  # ---- réécriture : jamais un rapiéçage ----
  SI une décision close change le squelette :
      sonde = DERIVER_ACTIONS_DEPUIS_DECISIONS(décisions closes)
      ORDONNER_PAR_PREREQUIS ; RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
        (toute ligne sans origine dans un verdict ou un fait est retirée :
         c'est ainsi qu'on ne traîne pas les scories de la sonde)
      → la passe suivante n'interrogera que les lignes que l'origine dit neuves
  SINON : SORTIR

# terminaison : on n'interroge qu'un texte fini, une ligne une seule fois par version ;
# une version nouvelle exige qu'une décision close ait modifié le squelette, et les
# choix litigieux sont en nombre fini et ne se rouvrent pas une fois tranchés.

═══ MISE EN FORME ═════════════════════════════════════════════════════════
IDENTIFIER_ETAPES_SIMULTANEES → VERIFIER_SIMULTANEITE_POSSIBLE
AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE (départage à validité d'ordre égale)
CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
POUR chaque item branché : CONSTRUIRE_BRANCHE_CONDITIONNELLE
POUR chaque fait périssable : re-vérification placée juste avant l'étape qui en dépend
— appareil mineur, uniquement là où un observable le réclame —
REPERER_POINTS_ENGAGEMENT → sur ces points seuls :
    QUALIFIER_REVERSIBILITE ; DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE ;
    DEFINIR_SIGNAUX_ECHEC ; PLACER_POINTS_VERIFICATION ;
    RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT ;
    STATUER_SUR_RISQUE_RESIDUEL → tout résidu accepté ou délégué :
        SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
SI RECENSER_OBLIGATIONS_FORMELLES non vide :
    PLACER_POINTS_AUTORISATION ; VERIFIER_COUVERTURE_BLOQUANTS
SI RECENSER_DEPENDANCES_EXTERNES rend un acteur capable de s'adapter : ANTICIPER_TIERS_REACTIF

═══ ÉMISSION ══════════════════════════════════════════════════════════════
VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_COHERENCE_ENSEMBLE
VERIFIER_ADOSSEMENT_AFFIRMATIONS (y compris les affirmations apparues tard)
VERIFIER_FAISABILITE_PAR_EXECUTANT ; REFUSER_AUTO_CONFIRMATION
REDIGER_PLAN(format F)
ELAGUER_LA_PROSE   # critère : retirer tout ce qu'une instance de l'exécutant, contexte
                   # vierge, lira ou vérifiera de toute façon par elle-même ;
                   # le comment n'est dirigé que là où il n'est pas évident
RENDRE_ACTIONNABLE_PAR_AGENT ; SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN
PREVOIR_SUITE_EN_CAS_DE_SUCCES
CONTROLER_CONTENU_FINAL ; CONTROLER_INTEGRITE_DOCUMENT
FAIRE_CONTROLER_PAR_UN_TIERS (le plan et les critères ; jamais la sonde, jamais la traçabilité)
    INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
    DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
    chaque finding désigne une ligne → cette ligne redevient neuve → une passe
    d'interrogation sur elle seule (même moteur, même règle de sortie)
REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER ; RESTITUER_EN_BREF
```

**Boucles.** Trois. *(1) Interrogation* : déclenchée par l'existence de lignes jamais interrogées ; elle ne remonte nulle part, elle est le moteur ; elle termine parce qu'une ligne n'est interrogée qu'une fois par version du texte, qu'une version nouvelle exige qu'une décision close ait modifié le squelette, et que les choix litigieux sont en nombre fini et ne se rouvrent jamais une fois tranchés. La sortie est observable : une passe qui ne rend ni présupposé ni choix. *(2) Levée d'une inconnue* : épuisement des moyens. *(3) Remontée au niveau 1* : déclenchée par un fait qui invalide la lecture du problème — un observable, pas une impression ; elle remonte exactement à la confrontation du problème, porteuse du fait ; elle termine parce que le fait doit être nouveau et que les faits ne font que s'accumuler. Le contrôle tiers n'ouvre pas de quatrième boucle : il rend des lignes « neuves » et rejoue le moteur.

**Fonctions rappelées, et pourquoi.** `RECENSER_INCONNUES`, `ORIENTER_CHOIX` et `DEFINIR_ATTENDU_OBSERVABLE` une fois par ligne et par version — c'est le moteur ; leur répétition n'est pas une insistance, c'est le fait que chaque ligne est un objet distinct et qu'une réécriture crée des lignes qui n'existaient pas. `CONFRONTER` aux trois niveaux. `CHAINER_ETAT_ACTUEL_VERS_CIBLE` deux fois, dans les deux sens, pour produire deux sondes rivales — c'est le moyen concret de tenir `GARANTIR_DIVERSITE_METHODE` plutôt que de l'affirmer. `DERIVER_ACTIONS_DEPUIS_DECISIONS` une fois par réécriture. `CONTROLER_TAILLE_DES_ETAPES` deux fois, sur deux objets : la ligne pendant l'interrogation (pour décider d'une décomposition), le plan à la mise en forme. `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE` à chaque réécriture, où il sert deux fonctions à la fois : purger les scories de la sonde, et désigner ce qui reste à interroger.

**Fonctions laissées de côté, et pourquoi.** C exclut cinq fonctions de façon absolue, sur la base de son domaine déclaré — un plan exécuté par un agent, le plus souvent celui-là même qui l'a écrit, après validation de l'utilisateur et nettoyage de contexte.
`PLACER_JALONS_CONSTAT` : un jalon de constat est un point où un suiveur humain vérifie l'avancement, distinct de l'autorisation. Ici chaque étape porte déjà son `DEFINIR_ATTENDU_OBSERVABLE`, que l'exécutant constate en la terminant : le jalon dupliquerait mot pour mot un attendu, et un plan qui répète est un plan qu'on lit moins bien. `DESIGNER_AUTORITE_AUTORISATION` : il n'existe qu'une autorité, l'utilisateur, déjà établie par `IDENTIFIER_DESTINATAIRE`, et la fonction demande de s'assurer que l'autorité n'est pas l'exécutant — c'est structurellement vrai ici et rien n'est à désigner. (`PLACER_POINTS_AUTORISATION` est conservée, conditionnée à `RECENSER_OBLIGATIONS_FORMELLES` non vide : une obligation formelle survit même quand l'exécutant est un agent.) `PROPOSER_AFFECTATION` : `RECENSER_RESSOURCES_EXECUTION` ne rend ici que les capacités de l'agent lui-même — il n'y a personne à qui affecter quoi que ce soit, et une offre d'affectation adressée à un utilisateur qui n'a qu'un exécutant est une question vide. `PROPOSER_CHIFFRAGE` et `PROPOSER_MARGES` : pour la même raison, il n'y a ni délai, ni budget, ni créneau à dimensionner, et ces trois fonctions portent toutes la mention « jamais produit d'office » — les produire dans ce contexte serait exactement les produire d'office. Si `IDENTIFIER_DESTINATAIRE` ou `RECENSER_RESSOURCES_EXECUTION` rendent un humain, un délai ou un budget, on n'est plus dans le domaine de C : c'est le domaine de A, et il faut y aller plutôt que rapatrier les cinq fonctions dans C.

Deux non-appels conditionnels, nommés : `LEVER_INCONNUE_PAR_ACTION_REVERSIBLE` si `INVENTORIER_CAPACITES` ne rend aucun accès en écriture au système cible ; `ANTICIPER_TIERS_REACTIF` si aucun acteur recensé ne peut s'adapter — un dépôt de code ne réagit pas au plan qui le vise.

**Cas d'emploi.** La demande ordinaire et fréquente, en territoire familier ou découvrable, avec un agent pour exécutant. Et le retravail d'un plan existant en plusieurs passes : le plan source entre comme sonde concurrente au niveau 2, anonymisé, ce qui est la seule façon honnête de le retravailler — ni le conserver par habitude, ni le jeter par principe.

---

# QUATRIÈME PARTIE — AUTO-ÉVALUATION

| Architecture | S | F | B | U | P |
|---|---|---|---|---|---|
| **A — Le greffe** | 4 | 5 | 5 | 4 | 3 |
| **B — Les contrats emboîtés** | 4 | 4 | 4 | 4 | 4 |
| **C — Le brouillon-sonde** | 5 | 4 | 4 | 4 | 5 |

**A.** Suivabilité 4 et non 5 : trois registres écrits sont tenables, mais le registre I peut atteindre vingt lignes et sa relecture à chaque réouverture est une charge réelle ; j'ai supprimé les compteurs, pas le volume. Fidélité 5 : c'est la seule des vingt-et-une qui ne laisse aucune issue à une question ouverte et qui n'arrête jamais le travail de sa propre autorité. Boucles 5 : aucune n'a de budget, toutes ont un argument monotone lisible. Usage 4 et non 5 : n'exclure aucune fonction est un choix défendable pour son objet, mais c'est aussi le symptôme que je n'ai pas su départager partout. Proportionnalité 3 : le plancher reste trois confrontations, un balayage complet des exigences tacites et un recensement intégral — sur une demande de deux lignes, c'est encore trop.

**B.** Fidélité 4 : l'interdiction faite aux contrats de parler à l'utilisateur est nécessaire, mais elle crée une latence — un enfant découvre une externalité certaine et doit attendre la clôture racine pour qu'elle soit exposée, alors que le principe 4 voudrait qu'on la remonte au moment où on la voit. Boucles 4 : l'argument des termes figés est solide, mais il suppose qu'une incohérence d'interface se laisse toujours traduire en un terme à figer, ce qui n'est pas garanti — une incohérence peut révéler que le découpage lui-même était mauvais, et B n'a alors qu'une issue, l'escalade. Proportionnalité 4 : sur une demande triviale la condition de division est fausse à la racine et B dégénère proprement en une passe unique ; il reste la confrontation sur le découpage, qui sur un contrat unique se réduit au champ d'un seul.

**C.** Suivabilité 5 : c'est la seule des trois dont la liste de travail n'est pas un document à maintenir mais un texte que le modèle a déjà sous les yeux — on interroge des lignes, on ne tient pas un registre. Fidélité 4 : la sonde ancre. J'ai atténué l'ancrage par la mise en concurrence de sondes produites par des méthodes matériellement différentes et par la réécriture depuis les décisions plutôt que le rapiéçage, mais je ne l'ai pas supprimé : une présupposition que les quatre sondes partagent ne sera jamais interrogée, puisque l'interrogation porte sur les lignes et non sur ce qu'aucune ligne n'a écrit. `BALAYER_EXIGENCES_TACITES` sur la sonde entière est le seul filet, et c'est un filet à grosses mailles. Proportionnalité 5 : le volume de travail est strictement dicté par le nombre de lignes et le nombre d'items qu'elles rendent.

**La plus solide : C.** Non parce qu'elle serait la plus rigoureuse — A l'est davantage — mais parce que le critère qui domine tous les autres ici est la suivabilité. Ces architectures sont des instructions lues par un modèle de langage : une architecture qui n'est pas suivie telle qu'elle est écrite n'a aucune fidélité, quelle que soit la fidélité de son texte. C est la seule dont le moteur soit un artefact présent, et la seule dont la charge s'annule d'elle-même sur une demande ordinaire — c'est-à-dire sur la quasi-totalité des cas réels. A reste ce vers quoi il faut basculer quand `QUALIFIER_TERRITOIRE` dit « reconfigurant » ou qu'un point irréversible apparaît ; B quand le travail excède ce qu'un seul contexte peut porter.

**Ce que je n'ai pas résolu.**

L'indépendance des concurrents aveugles. `QUALIFIER_INDEPENDANCE_OBTENUE` demande de nommer honnêtement le degré d'indépendance atteint ; quand les propositions, les attaques et l'arbitre sortent tous du même modèle, la réponse honnête est « faible », et mes trois architectures se contentent de le consigner. Ouvrir des agents séparés déplace le problème sans le résoudre : mêmes poids, mêmes angles morts. C'est le point le plus faible des trois, et il l'est aussi dans les dix-huit — aucune ne l'affronte, plusieurs le maquillent en appelant la fonction et en passant à la suite.

L'ancrage de la sonde en C, déjà dit.

La frontière entre inconnue de construction et inconnue d'exécution. Tout le principe 1 repose sur ce tri, et `CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION` est un jugement que rien ne vérifie. Une inconnue mal classée « exécution » devient une branche, et la branche est un report déguisé : le plan a l'air complet et ne l'est pas. Aucune de mes trois ne sait détecter ce cas.

L'utilisateur qui ne répond pas, qui répond « je ne sais pas », ou qui se contredit d'une réponse à l'autre. `SUSPENDRE_ENQUETE_ET_DEMANDER` attend — et ensuite ? `DETECTER_CONTRADICTION_ENTRE_SOURCES` traite des sources, et l'utilisateur n'en est pas une dans ces architectures. Mes trois supposent un interlocuteur disponible et cohérent.

L'auto-contrôle de la proportionnalité. Aucune des trois n'observe, après coup, que la cérémonie déployée était disproportionnée au sujet. Je l'ai rendue dépendante d'observables, ce qui vaut mieux qu'une estimation, mais rien ne la mesure.

Et un point que j'ai tranché sans en être satisfait : A, B et C ont des domaines d'emploi distincts, ce qui appelle une sélection en amont. La faire faire par `EVALUER_EXIGENCE_TACHE` serait une quatrième architecture, pas un réglage des trois — je l'ai signalé plutôt que de l'escamoter.

**Ce qui manque, que ni les dix-huit ni mes trois ne traitent.**

*Le format fixe n'est pas dans le jeu de fonctions.* Le principe 10 l'exige, et aucune des 129 ne le porte. Pire : la définition de `REDIGER_PLAN` — « écrire les étapes, leurs attendus, leurs retours arrière, les autorisations, les branches » — met le retour arrière, les autorisations et les branches sur le même plan que les étapes, alors que le principe 7 les veut mineurs et optionnels, et le principe 9 veut qu'on n'écrive pas ce que l'exécutant lira de toute façon. Le jeu de fonctions se contredit sur ce point, et j'ai dû légiférer un format (règle F) qui n'est adossé à aucune fonction. Aucune des dix-huit ne l'a seulement remarqué.

*La validation par l'utilisateur avant exécution n'a pas de fonction.* Le principe 11 dit que l'exécutant est un agent, après validation par l'utilisateur et nettoyage de contexte. Aucune fonction ne couvre : soumettre le plan, recevoir des corrections, les intégrer sans rouvrir tout l'appareil. `RESTITUER_EN_BREF` rapporte, il ne soumet pas. `SOUMETTRE_ARBITRAGE_UTILISATEUR` porte un compromis, pas un document. Il manque la dernière porte, et les vingt-et-une architectures s'arrêtent une étape trop tôt.

*Le retravail multi-passes n'est pas outillé.* `AMORCER_DEPUIS_PLAN_EXISTANT` ouvre la porte, et rien ne la referme : aucune fonction ne compare le plan produit au plan source. Une deuxième passe peut donc laisser tomber silencieusement un engagement de la première — exactement l'inverse de ce que `TRAQUER_AJOUTS_SILENCIEUX` fait pour les ajouts. Il manque son symétrique : traquer les retraits silencieux. B et C entrent le plan source comme concurrent anonyme, ce qui l'empêche d'être conservé par déférence, mais ne garantit pas qu'aucune de ses promesses ne disparaît sans décision.

*L'autonomie du texte n'est pas vérifiée.* Le principe 13 veut un plan auto-porteur, exécutable de manière autonome. `VERIFIER_FAISABILITE_PAR_EXECUTANT` vérifie les accès, les outils, les compétences, le contexte présupposé — pas si le texte tient debout tout seul devant un contexte vierge. `RENDRE_ACTIONNABLE_PAR_AGENT` l'affirme sans l'éprouver. Le contrôle correct existerait : donner le plan seul à un agent qui n'a rien vu et lui demander non pas de l'exécuter, mais de dire à quel endroit il devrait redemander quelque chose. Aucune fonction ne le décrit, et aucune des dix-huit n'y songe.

*La péremption du plan lui-même.* `JUGER_PEREMPTION_FAIT` et `INSCRIRE_REVERIFICATION_FAIT_PERISSABLE` traitent les faits un par un. Un plan livré aujourd'hui et exécuté dans trois semaines peut être périmé dans son ensemble — non parce qu'un fait a bougé, mais parce que l'état actuel dont il part n'est plus l'état actuel. Rien, dans les 129, ne date le plan ni ne dit à quelle condition il faut le rejouer.