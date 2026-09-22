
# --- diagrams ------------------------------------------------------------
# Regles : vertical uniquement, un libelle = une seule ligne de 44 caracteres
# au maximum, majuscule initiale, deux sorties par noeud au plus, et aucun
# noeud qui ne soit pas une etape ou un etat reel du traitement.

D_OVER = MM + """flowchart TD
  P["00 · Entrée"]
  C["01 · Crible"]
  N1["02 · Niveau 1, lecture du besoin"]
  N2["03 · Niveau 2, enchaînement"]
  MO["04 à 07 · Itération"]
  MF["08 · Mise en forme"]
  CT["09 · Contrôle et émission"]
  EM["Plan émis, registre clos"]
  DE["Refus motivé, aucun plan produit"]
  P --> C --> N1 --> N2 --> MO --> MF --> CT --> EM
  P -. "Aucun plan" .-> DE
  MO -. "Besoin contredit" .-> N1
  CT -. "Défaut relevé" .-> MO
  class DE dette
  class EM quit""" + CLS

D_PORTE = MM + """flowchart TD
  R1["Lecture du cadre autorisé"]
  R2["Inventaire des capacités disponibles"]
  R3["Identification du destinataire du plan"]
  R4["Forme du travail et nature du territoire"]
  V{"Un plan existant est-il fourni ?"}
  E1["Le besoin est à établir depuis la demande"]
  W{"Vient-il du système lui-même ?"}
  E2["Le besoin est dérivé du plan"]
  G["Le plan concourt aux niveaux 1 et 2"]
  E3["Son registre est repris"]
  RF["Faits repris, péremption contrôlée"]
  Q{"Un problème de planification est-il posé ?"}
  DE["Refus motivé, le traitement s'arrête"]
  OK["Ouverture du registre de travail"]
  EX["Exigence de la tâche évaluée, cadre en garde"]
  R1 --> R2 --> R3 --> R4 --> V
  V -- "Non" --> E1 --> Q
  V -- "Oui" --> W
  W -- "Non" --> E2 --> G --> Q
  W -- "Oui" --> E3 --> RF --> Q
  Q -- "Non" --> DE
  Q -- "Oui" --> OK --> EX
  class DE dette
  class EX quit""" + CLS

D_CRIBLE = MM + """flowchart TD
  D["La demande seule. Aucun chemin n'a encore été imaginé"]
  Q1["Qu'est-ce qui est dans le périmètre, qu'en est exclu, et d'où part-on ?"]
  Q2["Quels objectifs, dans quel ordre, et lesquels s'opposent entre eux ?"]
  Q3["Que faut-il tenir sans jamais le relâcher, du début à la fin ?"]
  Q4["Quelles préférences sont exprimées, à ne pas confondre avec des contraintes ?"]
  Q5["Quelles obligations formelles s'imposent, et de quoi dépend-on sans le maîtriser ?"]
  Q6["Qu'a-t-on déjà établi ou déjà fait, qui éviterait de le refaire ?"]
  Q7["L'énoncé du problème tient-il, et une solution y est-elle déjà glissée ?"]
  Q8["Qu'a-t-on ajouté que personne n'a demandé, et quelles hypothèses viennent du dehors ?"]
  Q9["Qui d'autre subira certainement l'effet du plan, et le demandeur le sait-il ?"]
  Q10["Quelles exigences vont tellement de soi qu'elles ne sont jamais dites ?"]
  Q11["Qu'est-ce qui est écarté du plan, et qu'il faut noter sans le traiter ?"]
  Q12["Qu'est-ce qu'on ignore encore, à l'échelle du problème entier ?"]
  A["Chaque question reçoit une disposition écrite"]
  W{"La question a-t-elle un objet dans cette demande ?"}
  V["Sans objet. Groupées toutes ensemble en une seule ligne"]
  X{"La lecture sait-elle y répondre ?"}
  E["La réponse désigne quelque chose : entrée au registre"]
  I["Personne ne sait répondre : entrée « Fait manquant »"]
  D --> Q1 --> Q2 --> Q3 --> Q4 --> Q5 --> Q6 --> Q7 --> Q8
  Q8 --> Q9 --> Q10 --> Q11 --> Q12 --> A
  A --> W
  W -- "Non" --> V
  W -- "Oui" --> X
  X -- "Oui" --> E
  X -- "Non" --> I
  class E dette
  class I dette""" + CLS

D_CONF = MM + """flowchart TD
  Q["La question mise en concurrence"]
  G["Une méthode imposée à chaque concurrent"]
  P["Propositions produites en isolement"]
  H["Chacune écrit les hypothèses qu'elle fait"]
  HY{"Une hypothèse est-elle une inconnue ?"}
  AT["Le fait est établi avant toute attaque"]
  IND{"L'indépendance obtenue est-elle suffisante ?"}
  ANG{"Reste-t-il un angle non employé ?"}
  REP["Un concurrent reproduit avec cet angle"]
  FAIB["Indépendance faible consignée au registre"]
  O["Chaque proposition est attaquée séparément"]
  T["Hypothèses communes marquées par intersection"]
  AR["Arbitrage par un agent distinct"]
  Z{"L'arbitre retient-il une proposition ?"}
  V["Verdict rendu, entrée close"]
  QU["Aucune ne tient : passe à l'utilisateur"]
  Q --> G --> P --> H --> HY
  HY -- "Oui" --> AT --> IND
  HY -- "Non" --> IND
  IND -- "Non" --> ANG
  ANG -- "Oui" --> REP --> H
  ANG -- "Non" --> FAIB --> O
  IND -- "Oui" --> O
  O --> T --> AR --> Z
  Z -- "Oui" --> V
  Z -- "Non" --> QU
  class QU dette
  class V quit""" + CLS

D_N1 = MM + """flowchart TD
  A["Le registre, alimenté par le crible"]
  RB{"Un besoin arrêté est-il au registre ?"}
  CF{"La demande le contredit-elle ?"}
  KB["Besoin conservé, cible et critères repris"]
  B["Plusieurs lectures du besoin proposées"]
  C{"L'arbitre retient-il une lecture ?"}
  QU["Aucune ne tient : passe à l'utilisateur"]
  D["Cible énoncée en termes observables"]
  E["Critères d'acceptation, ordonnés"]
  F{"La cible garantit-elle l'effet voulu ?"}
  G["Une exigence manquait : elle entre au crible"]
  H["Le besoin est arrêté"]
  A --> RB
  RB -- "Non" --> B
  RB -- "Oui" --> CF
  CF -- "Non" --> KB --> H
  CF -- "Oui" --> B
  B --> C
  C -- "Non" --> QU
  C -- "Oui" --> D --> E --> F
  F -- "Non" --> G --> A
  F -- "Oui" --> H
  class G dette
  class QU dette
  class KB quit
  class H quit""" + CLS

D_N2 = MM + """flowchart TD
  A["Besoin arrêté, faits déjà établis"]
  R{"Un enchaînement arrêté est-il au registre ?"}
  N{"Cible, critères ou hypothèse contredite ?"}
  K["Enchaînement conservé, contrôlé à la fin"]
  B["Enchaînements concurrents proposés"]
  C["Chacun découpe selon un principe différent"]
  E["Attaques, puis arbitrage"]
  Z{"L'arbitre retient-il un enchaînement ?"}
  QU["Aucun ne tient : passe à l'utilisateur"]
  F["Enchaînement retenu"]
  A --> R
  R -- "Non" --> B
  R -- "Oui" --> N
  N -- "Non" --> K --> F
  N -- "Oui" --> B
  B --> C --> E --> Z
  Z -- "Non" --> QU
  Z -- "Oui" --> F
  class QU dette
  class F quit""" + CLS

D_VAGUE = MM + """flowchart TD
  IT["Début d'itération"]
  A["Les étapes nouvelles de l'enchaînement"]
  B["Trois questions posées à chaque étape"]
  CD["Crible repassé sur besoin et enchaînement"]
  D["Entrées inscrites au registre"]
  AP["Résorption, un traitement par type"]
  PV["Envoi unique à l'utilisateur"]
  RE["Réécriture depuis les décisions arrêtées"]
  S{"Les quatre conditions sont-elles réunies ?"}
  MF["Passage à la mise en forme"]
  IT --> A --> B --> D
  IT --> CD --> D
  D --> AP --> PV --> RE --> S
  S -- "Non" --> IT
  S -- "Oui" --> MF
  class D dette
  class MF quit""" + CLS

D_LEVER = MM + """flowchart TD
  I["Un fait manque"]
  PAR{"Plusieurs domaines séparables ?"}
  AG["Un agent par domaine, en parallèle"]
  CR["Retours croisés les uns avec les autres"]
  MOY["Essayer un moyen non encore utilisé"]
  M["Inspection, source, action, question"]
  AB{"Le moyen a-t-il abouti ?"}
  F["Fait établi, provenance consignée"]
  E{"Indéterminable, ou simplement non cherché ?"}
  QQ["Non cherché : le point passe à l'utilisateur"]
  CE["Indéterminable : contrôle du classement"]
  I --> PAR
  PAR -- "Oui" --> AG --> CR --> MOY
  PAR -- "Non" --> MOY
  MOY --> M --> AB
  AB -- "Oui" --> F
  AB -- "Non" --> MOY
  MOY -- "Moyens épuisés" --> E
  E -- "Non cherché" --> QQ
  E -- "Indéterminable" --> CE
  class QQ dette
  class F quit""" + CLS

D_CONTRE = MM + """flowchart TD
  S["Un fait est classé « à établir plus tard »"]
  G1{"Est-il indéterminable maintenant ?"}
  G2{"Tous les moyens sont-ils épuisés ?"}
  G3{"Sait-on à quoi on le verra, le moment venu ?"}
  G4{"Sa portée dépasse-t-elle une étape ?"}
  G5{"Est-il appuyé autrement que par affirmation ?"}
  C["Le classement devient lui-même une décision"]
  R["Classement refusé : le fait doit être établi"]
  Q["Classement accepté : branche du plan"]
  S --> G1
  G1 -- "Non" --> R
  G1 -- "Oui" --> G2
  G2 -- "Non" --> R
  G2 -- "Oui" --> G3
  G3 -- "Non" --> R
  G3 -- "Oui" --> G4
  G4 -- "Oui" --> C --> G5
  G4 -- "Non" --> G5
  G5 -- "Non" --> R
  G5 -- "Oui" --> Q
  class R dette
  class Q quit""" + CLS

D_CONTRAT = MM + """flowchart TD
  P["Étape sans critère de réussite unique"]
  C["Sous-plan : périmètre, cible, critères"]
  C2["Interfaces promises, termes figés"]
  H["Même traitement, même registre"]
  KO{"Le sous-plan est-il exécutable tel quel ?"}
  KO2{"Le terme en cause est-il déjà figé ?"}
  RN["Le parent fige le terme en cause"]
  ESU["Le point passe à l'utilisateur"]
  RC["Recomposition, jonctions vérifiées"]
  IN{"Les jonctions tiennent-elles ?"}
  PART{"La partition elle-même est-elle en cause ?"}
  NF{"Un fait nouveau le justifie-t-il ?"}
  RD["Redécoupage, retour au niveau 2"]
  TF["L'interface devient un terme figé"]
  FIN["Le sous-plan remonte au parent"]
  P --> C --> C2 --> H --> KO
  KO -- "Non" --> KO2
  KO2 -- "Non" --> RN --> H
  KO2 -- "Oui" --> ESU
  KO -- "Oui" --> RC --> IN
  IN -- "Non" --> PART
  IN -- "Oui" --> FIN
  PART -- "Non" --> TF --> H
  PART -- "Oui" --> NF
  NF -- "Oui" --> RD
  NF -- "Non" --> ESU
  class ESU dette
  class FIN quit""" + CLS

D_PV = MM + """flowchart TD
  A["Plus rien n'avance sans l'utilisateur"]
  B{"Des questions sont-elles en attente ?"}
  Z["L'itération se poursuit sans envoi"]
  C["Envoi unique de toutes les questions"]
  D["Attente, aucune valeur par défaut"]
  C1{"Une réponse est-elle arrivée ?"}
  R1["Le traitement reste en attente"]
  C2{"La réponse tranche-t-elle la question ?"}
  C3{"Contredit-elle une réponse antérieure ?"}
  R3["Le niveau 1 est rouvert sur ce point"]
  R4["Les entrées concernées sont closes"]
  K{"Un moyen disponible permet-il de l'établir ?"}
  FM["L'entrée devient un fait à établir"]
  REF{"L'entrée a-t-elle déjà été reformulée ?"}
  R2["Reformulée avec l'enjeu, même échange"]
  BE["Questions ramenées au besoin lui-même"]
  A --> B
  B -- "Non" --> Z
  B -- "Oui" --> C --> D --> C1
  C1 -- "Non" --> R1
  C1 -- "Oui" --> C2
  C2 -- "Oui" --> C3
  C3 -- "Oui" --> R3
  C3 -- "Non" --> R4
  C2 -- "Non" --> K
  K -- "Oui" --> FM
  K -- "Non" --> REF
  REF -- "Non" --> R2 --> D
  REF -- "Oui" --> BE
  class FM dette
  class R4 quit""" + CLS

D_REECR = MM + """flowchart TD
  D["Décisions arrêtées pendant l'itération"]
  CH{"Une décision close change-t-elle le chemin ?"}
  KP["Enchaînement conservé, aucune étape neuve"]
  A["Actions dérivées de ces décisions"]
  O["Ordonnancement par prérequis"]
  RO["Chaque étape rattachée à son origine"]
  X["Étape sans origine : retirée"]
  N["Les étapes neuves sont désignées"]
  S1{"Aucune étape non interrogée ?"}
  S2{"Aucune entrée non close ?"}
  S3{"Aucune dimension du crible sans disposition ?"}
  S4{"Aucun non-appel sans sa condition ?"}
  RE["Une itération de plus"]
  FIN["Sortie d'itération"]
  D --> CH
  CH -- "Non" --> KP --> S1
  CH -- "Oui" --> A --> O --> RO
  RO --> X
  RO --> N --> S1
  S1 -- "Non" --> RE
  S1 -- "Oui" --> S2
  S2 -- "Non" --> RE
  S2 -- "Oui" --> S3
  S3 -- "Non" --> RE
  S3 -- "Oui" --> S4
  S4 -- "Non" --> RE
  S4 -- "Oui" --> FIN
  class X dette
  class FIN quit""" + CLS

D_FORME = MM + """flowchart TD
  P["Repérage des points d'engagement"]
  Z{"Y a-t-il un point d'engagement ?"}
  N["Aucun appareil de risque n'est atteignable"]
  R1["Réversibilité et retour arrière éprouvés"]
  R2["Signaux d'échec, points de contrôle"]
  R3["Risques par origine, résidu statué"]
  O{"Obligation formelle ou point irréversible ?"}
  AU["Points d'autorisation, autorité désignée"]
  J{"Un suiveur humain distinct de l'exécutant ?"}
  JA["Jalons de constat placés"]
  RS{"Des ressources d'exécution recensées ?"}
  PR["Affectation, chiffrage et marges proposés"]
  B["Branches écrites, faits périssables datés"]
  SI["Étapes simultanées repérées et vérifiées"]
  T["Taille des étapes, élagage du superflu"]
  P --> Z
  Z -- "Non" --> N --> O
  Z -- "Oui" --> R1 --> R2 --> R3 --> O
  O -- "Oui" --> AU --> J
  O -- "Non" --> J
  J -- "Oui" --> JA --> RS
  J -- "Non" --> RS
  RS -- "Oui" --> PR --> B
  RS -- "Non" --> B
  B --> SI --> T
  class T quit""" + CLS

D_CTRL = MM + """flowchart TD
  VE["Couverture, cohérence, invariants, adossement"]
  FA{"L'exécutant juge-t-il le plan faisable ?"}
  OP{"Reste-t-il une option écartée conservée ?"}
  RP["Option suivante reprise, faisabilité rejouée"]
  QU["Champ épuisé : le point passe à l'utilisateur"]
  PL["Plan rédigé selon le modèle fourni"]
  T1["Relecture 1 : plan, critères et besoin"]
  T2["Relecture 2 : le plan seul, lecteur à froid"]
  U1{"La relecture 1 relève-t-elle un défaut ?"}
  TR{"Le retour vise-t-il une décision manquante ?"}
  DT["Nouvelle entrée au registre"]
  RF["Refus écrit et motivé"]
  Z{"Des entrées ont-elles été ouvertes ?"}
  RO["Chacune repart vers le bloc compétent"]
  EM["Plan émis, registre clos"]
  VE --> FA
  FA -- "Non" --> OP
  OP -- "Oui" --> RP --> FA
  OP -- "Non" --> QU
  FA -- "Oui" --> PL
  PL --> T1 --> U1
  PL --> T2 --> TR
  U1 -- "Oui" --> DT
  U1 -- "Non" --> Z
  TR -- "Oui" --> DT
  TR -- "Non" --> RF --> Z
  DT --> Z
  Z -- "Oui" --> RO
  Z -- "Non" --> EM
  class DT dette
  class QU dette
  class EM quit""" + CLS
