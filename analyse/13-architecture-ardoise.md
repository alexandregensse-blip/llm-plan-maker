J'ai lu les 130 fonctions, le fichier des trois architectures en entier (dépouillement des dix-huit inclus), et je n'ai pas eu besoin de rouvrir les dix-huit elles-mêmes : le dépouillement est assez précis sur les mécanismes que je reprends.

**Un point de matériau, d'entrée.** Le tour précédent a travaillé sur 129 fonctions et a conclu sa quatrième partie par « l'autonomie du texte n'est pas vérifiée : le contrôle correct existerait — donner le plan seul à un agent qui n'a rien vu et lui demander où il devrait redemander quelque chose — aucune fonction ne le décrit ». Cette fonction existe maintenant : `EPROUVER_AUTONOMIE_DU_TEXTE`, mot pour mot. A, B et C ne l'appellent donc pas, et aucune n'a d'équivalent : leur contrôle final est `FAIRE_CONTROLER_PAR_UN_TIERS`, qui donne au relecteur le plan **et les critères**, c'est-à-dire exactement ce qu'un lecteur autonome n'aura pas. Je ne le leur compte pas comme faute, mais c'est un trou du matériau que je comble.

---

# PREMIÈRE PARTIE — DÉPOUILLEMENT

**S** = suivabilité, **F** = fidélité, **B** = boucles, **U** = usage des fonctions, **P** = proportionnalité.

| Nom | S | F | B | U | P | Appréciation | À RETENIR | À NE PAS FAIRE |
|---|---|---|---|---|---|---|---|---|
| **A — Le greffe** | 3 | 4 | 4 | 4 | 2 | La plus rigoureuse des trois, et celle qui se contredit le plus vite. Sa quittance est le meilleur mécanisme du corpus : aucun item ne sort d'un registre sans un état de résolution appartenant à un ensemble clos, et aucune des issues n'arrête le système. Mais elle paie cette rigueur par une cérémonie qu'elle finit par avouer — « A est la plus lourde des trois, et ne doit pas être le régime par défaut » : une architecture qui se déclare un domaine d'emploi a perdu avant de commencer. | La **quittance** (R1) et son corollaire : « en attente », « non résolu » et « invalide » ne sont pas des sorties, ce sont des renvois. Le **routage du contrôle final par nature du défaut** vers le registre compétent, où le finding « se dissout, puisqu'il devient un item ordinaire — pas de boucle spéciale, pas de compteur » : c'est le meilleur traitement du contrôle final des vingt-et-une. L'argument monotone sur `VERIFIER_FIDELITE_CIBLE_BESOIN` : chaque échec ajoute un critère ou une contrainte, jamais n'en retire, donc l'espace des cibles admissibles ne fait que se restreindre. L'envoi groupé unique des questions. | Légiférer un format de plan (sa « règle F ») : le principe 10 dit que ce n'est pas le travail de l'architecture. Reconstituer le mémo de couples de l'architecture 04 sous un autre nom — « un même fait ne peut rouvrir deux fois la même pièce : c'est écrit au registre » est une table (pièce, fait) à tenir, et c'est précisément ce que le dépouillement des dix-huit a condamné. Ouvrir trois registres et tenir un plancher de trois confrontations sur une demande de deux lignes. Rouvrir « cette pièce seule » sans jamais dire **comment on sait laquelle** : la réouverture ciblée est annoncée, pas outillée. |
| **B — Les contrats emboîtés** | 3 | 3 | 4 | 4 | 4 | L'objet « contrat » est juste et l'argument de terminaison par termes figés est le meilleur du corpus sur la question de la taille. Mais B achète la cohérence de son découpage en muselant ses enfants : huit fonctions leur sont interdites, dont `EXPOSER_EXTERNALITES_CERTAINES` — un contrat qui découvre une externalité certaine doit attendre la clôture racine pour que le demandeur en soit informé, alors que la fonction dit « s'assurer que le demandeur l'a compris ». B le reconnaît et appelle ça une latence : c'est une violation du principe 1, pas une latence. | L'**objet contrat** comme charge utile minimale d'un contexte séparé : périmètre, faits d'entrée avec provenance, cible observable et critères locaux, contraintes et invariants hérités, interfaces promises, termes figés. La **terminaison par gel monotone** : une renégociation ne peut que retirer un degré de liberté, jamais en rendre. La **frontière nette entre renégociation et escalade** : « si honorer le contrat exigerait de relâcher un terme déjà figé, ce n'est plus une renégociation » — observable, pas d'appréciation. Le **socle** établi une fois, qu'aucun enfant ne redémontre. « Les contrats qui produisent un fait attendu par d'autres passent devant ». | Faire du découpage un **objet de concurrence séparé** avec son propre niveau : sur un travail à un seul contrat, ce niveau entier se réduit à un champ d'un seul et on a payé une confrontation pour rien. Faire porter `BALAYER_EXIGENCES_TACITES` une seule fois, à la racine, **avant qu'aucun chemin n'existe** : c'est le moment où le balayage a le moins de prise, puisqu'une exigence tacite se révèle le plus souvent contre un pas précis. Tenir une file de réserve de questions sur toute la durée du run. Interdire à un enfant de remonter ce qu'il voit au moment où il le voit. |
| **C — Le brouillon-sonde** | 5 | 3 | 3 | 4 | 5 | La seule des trois qui soit réellement suivable : sa liste de travail n'est pas un document à maintenir, c'est un texte déjà sous les yeux, et son moteur — trois questions posées à chaque ligne — est le générateur d'objets le plus tranchant du corpus. Et la seule dont le défaut central soit connu de son auteur et laissé ouvert : « une présupposition que les quatre sondes partagent ne sera jamais interrogée, puisque l'interrogation porte sur les lignes et non sur ce qu'aucune ligne n'a écrit ». Un angle mort systématique traité par « un filet à grosses mailles » n'est pas un aveu honnête, c'est un manquement au principe 1. | Les **trois questions par ligne** — sur quoi repose-t-elle, choisit-elle quelque chose, qu'est-ce qui dira qu'elle a réussi. La **taille constatée à l'endroit exact où elle se voit** : une ligne dont l'attendu n'est nommable qu'en plusieurs observables indépendants est trop grosse, et c'est là que la décomposition se déclenche. La **réécriture depuis les décisions closes plutôt que le rapiéçage**, avec `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE` qui fait double emploi : purger les scories et désigner ce qui reste à interroger. La **diversité obtenue par la méthode de production** et non déclarée. Le critère d'`ELAGUER_LA_PROSE` : retirer ce qu'une instance de l'exécutant, contexte vierge, lira ou vérifiera de toute façon. | Faire de la sonde le **seul** générateur d'objets. Justifier cinq exclusions absolues par un domaine d'emploi déclaré — « si `IDENTIFIER_DESTINATAIRE` rend un humain, on n'est plus dans le domaine de C : c'est le domaine de A » : dans un brief qui exige une architecture unique, c'est disqualifiant. Affirmer que « les choix litigieux ne se rouvrent jamais une fois tranchés » tout en autorisant une remontée au niveau 1 qui change la lecture du problème : C ne dit pas ce que deviennent les choix déjà tranchés quand le problème bouge. Passer `BALAYER_EXIGENCES_TACITES` comme un balayage global auquel on peut répondre « rien à signaler ». |

**Sur les quatre « règles communes » et le format.** R1 (quittance) : excellente, je la reprends telle quelle comme règle de fermeture unique. R2 (arbitre briefé) : excellente, et elle répond au meilleur constat transversal du dépouillement des dix-huit — aucune des dix-huit n'exploitait le fait, pourtant écrit dans `REDIGER_BRIEF_AGENT`, qu'un agent qui juge reçoit les critères ET le besoin. Je la reprends. R3 (champ d'un seul) : la règle est juste et l'idée qui la porte — « la proportionnalité vient du nombre d'objets soumis à un niveau, jamais d'une estimation d'effort » — est la clé de tout le problème ; A l'énonce puis la trahit avec son plancher. Je la reprends et je l'honore. R4 (cadre) : correcte, sauf que `EVALUER_EXIGENCE_TACHE` est appelée une fois, à la porte, sur des observables dont la moitié n'existe pas encore (le nombre de choix litigieux rendus par `ORIENTER_CHOIX`) ; je la rends rappelable, avec une contrainte de monotonie. **F (format fixe) : à rejeter.** Le principe 10 dit que définir ce format n'est pas le travail de l'architecture et qu'aucune fonction ne le porte ; les trois ont légiféré un format et l'ont appelé un invariant. Le template est une entrée du système, point.

**Mécanismes retenus au dépouillement des dix-huit, que A, B et C ont manqués ou mal traités, et que je reprends.**

1. **La réouverture ciblée par le fait nommé (04, 06), enfin outillée.** Les deux disent : un fait rouvre les seuls nœuds qui en dépendaient, `REUTILISER_ACQUIS` protège le reste. A l'annonce (« rouvrir CETTE pièce seule ») sans dire comment on identifie la pièce, et 04 le paie d'un graphe mutable. L'index existe déjà et ne coûte rien : `EXIGER_HYPOTHESES_EXPLICITES` **oblige chaque option à nommer ce qu'elle suppose**. Une pièce porte donc la liste écrite de ses hypothèses ; un fait nouveau rouvre exactement les pièces dont il contredit une hypothèse nommée, et cette liste se lit, elle ne se calcule pas.
2. **La double levée indépendante sur un fait pivot (03).** A, B et C appliquent le régime des faits à tous les faits et ne font jamais de seconde levée. Je la reprends, déclenchée par un observable qui la rend rare : un fait est pivot si `NOMMER_FAIT_QUI_FERAIT_BASCULER` l'a nommé, ou si plus d'un pas en dépend. Sur une demande ordinaire, zéro pivot.
3. **Le croisement des retours d'agents parallèles (11).** Les trois croisent les sources d'un même fait ; aucune ne croise les retours de branches d'enquête distinctes entre eux, alors que c'est l'endroit exact où vivent les erreurs corrélées.
4. **Le repli sur le dauphin (12, 17).** Quand `VERIFIER_FAISABILITE_PAR_EXECUTANT` échoue, on rejoue la faisabilité seule sur l'option conservée par `CONSERVER_OPTIONS_ECARTEES`, pas le choix entier. A, B et C conservent les écartées et ne s'en servent jamais.
5. **L'élimination par fragilité (13).** `AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE` sert, chez les trois, à ordonner des pas et des inconnues. 13 l'utilise pour ordonner les **attaques** : on attaque d'abord la survivante qui porte l'hypothèse la plus fragile. C'est plus court et plus tranchant.
6. **La salve mutuellement aveugle (02).** Les trois sérialisent tous les choix par ordre de dépendance. C'est juste pour les choix dépendants ; pour les choix indépendants, sérialiser c'est laisser chaque verdict contaminer le suivant. `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` dit lesquels sont indépendants : ceux-là se confrontent en aveugle mutuel.
7. **La sortie énoncée comme état vérifiable (14).** Le bon réflexe des portes de 14, sans ses huit phases obligatoires.
8. **Le moyen épuisé ne s'arrête pas, il remonte (15).** Repris par les trois ; je le garde et je l'étends : aucun épuisement, nulle part, n'autorise une livraison avec un point ouvert.

---

# DEUXIÈME PARTIE — PRÉ-CONSTRUCTION

Ce que je cherche à réussir, en un paragraphe.

L'architecture doit livrer un plan sans point ouvert et le **prouver par lecture d'un seul fichier** (l'exhaustivité de A), absorber un travail qui excède un contexte **sans changer d'algorithme** (la taille de B), et ne produire que ce que le sujet contient **tout en attrapant ce que le sujet ne dit pas** (la proportionnalité et la chasse au tacite de C). Les trois se détruisent chez A, B et C parce que chacune a choisi un seul générateur d'objets et l'a payé : A génère par recensement exhaustif — donc cérémonie constante ; C génère par interrogation du chemin — donc angle mort sur ce qu'aucune ligne n'a écrit ; B génère par découpage — donc double le cadrage ou l'interdit aux enfants. Je les fais tenir ensemble par quatre décisions. **Première : séparer le constant du proportionnel par nature d'acte, pas par volume.** La part constante de mon architecture est un acte de **lecture** — une liste fixe de questions posées une fois au problème, chacune close par une disposition écrite, y compris « vide » ; elle n'ouvre aucun agent, ne produit aucun texte livrable, ne déclenche aucune confrontation. La part proportionnelle est faite de **productions** — confrontations, agents, levées, contrats, branches — et elle est dimensionnée par le seul nombre d'objets que la lecture et l'interrogation ont rendus. L'exhaustivité s'achète donc avec de la lecture, qui est bon marché, et la cérémonie ne se déclenche que sur des objets qui existent. **Deuxième : deux générateurs indépendants, jamais un.** Le tacite se cache à deux endroits — dans ce que l'énoncé ne dit pas (attrapé par le crible, qui ne regarde pas le chemin) et dans ce que le chemin suppose sans le dire (attrapé par l'interrogation des pas, qui ne regarde pas l'énoncé). Chacun seul ancre ; leur union couvre, et leur coût reste proportionnel parce que l'un est une liste finie de dimensions et l'autre une liste finie de lignes. **Troisième : la taille n'est pas un régime, c'est un grain.** Un pas qui ne peut pas recevoir un attendu observable unique sans devenir lui-même un plan est un contrat, et le même moteur tourne dessus, avec le même fichier de travail et le socle du parent ; un travail trop gros ne change donc pas l'algorithme, il change le nombre de fois qu'il tourne. **Quatrième, et c'est elle qui rend les trois autres suivables : le fichier de travail est un fichier.** Tout ce qui reste ouvert est inscrit comme dette dans l'ardoise — qui n'est pas un document supplémentaire mais le **fichier de traçabilité que le principe 9 exige de toute façon**, simplement écrit au fil de l'eau au lieu d'être écrit à la fin. Le modèle ne tient rien de tête : il lit, il inscrit une dette, il inscrit une quittance. L'exhaustivité vérifiable devient littéralement ça — un fichier où l'absence d'une ligne se voit.

---

# TROISIÈME PARTIE — L'ARCHITECTURE

## L'ARDOISE

**Principe en une phrase.** Tout ce qui reste ouvert est inscrit comme dette dans un fichier unique — l'ardoise, qui est déjà le fichier de traçabilité exigé — alimentée par deux générateurs indépendants, le crible qui lit le problème et l'interrogation qui lit le chemin ; cinq types de dette, cinq règles de fermeture, et le plan ne s'écrit que lorsque l'ardoise est soldée.

*Les blocs que je définis sont en minuscules — `confronter`, `lever`, `honorer`, `vague` — pour qu'on ne les confonde jamais avec les 130 identifiants, qui sont en capitales.*

```
════════ PORTE ═══════════════════════════════════════════════════════════
LIRE_TECHNIQUES_AUTORISEES                   # nombre et type d'agents par fonction :
                                             # seule borne du système (principe 5)
INVENTORIER_CAPACITES ; IDENTIFIER_DESTINATAIRE ; RECENSER_RESSOURCES_EXECUTION
SI l'entrée est un plan existant :
    AMORCER_DEPUIS_PLAN_EXISTANT             # le besoin est dérivé du plan
    le plan source est conservé pour DEUX emplois et aucun autre :
        concurrent anonymisé au niveau 1, concurrent anonymisé au niveau 2.
        il n'est consulté nulle part ailleurs — ni déférence, ni rejet de principe.
    SI une ardoise de passe antérieure existe :
        REUTILISER_ACQUIS ; JUGER_PEREMPTION_FAIT sur chaque fait hérité
SINON : SEPARER_DEMANDE_ET_BESOIN
QUALIFIER_FORME_TRAVAIL ; QUALIFIER_TERRITOIRE
SI aucun problème de planification n'est posé :
    DECLINER_SI_PAS_DE_PLAN ; FIN            # unique arrêt de sa propre autorité
PLACER_ET_NOMMER_LE_FICHIER(le plan, l'ardoise)
ouvrir l'ardoise : REDIGER_TRACABILITE_SEPAREE
    # ouverte ici, écrite en continu, close à l'émission.
    # C'est à la fois la liste de travail et le livrable de traçabilité.
EVALUER_EXIGENCE_TACHE                       # parmi les techniques autorisées
RESPECTER_CADRE_AUTORISE                     # garde permanente : à chaque ouverture d'agent

════════ LE CRIBLE — générateur n°1, une passe, lecture seule ════════════
# INVARIANT : aucune fonction du crible n'ouvre d'agent, ne produit de texte
# livrable, ni ne déclenche de confrontation. Le crible lit et inscrit.
# Chaque ligne se clôt par une disposition écrite : un objet, ou « vide ».
# Les « vides » sont groupés en une ligne d'ardoise — c'est le prix entier
# du crible sur une demande de deux lignes.

DELIMITER_PERIMETRE ; ETABLIR_ETAT_ACTUEL
ORDONNER_OBJECTIFS_SANS_ECARTER ; DETECTER_CONFLIT_OBJECTIFS   # symptôme, pas arbitrage
RECENSER_CONTRAINTES_DURES ; RECENSER_INVARIANTS
RECENSER_PREFERENCES                          # tenues séparées des contraintes
RECENSER_OBLIGATIONS_FORMELLES ; RECENSER_DEPENDANCES_EXTERNES
CHERCHER_ANTECEDENTS → REUTILISER_ACQUIS      # ne pas redémontrer l'acquis valide
CONTESTER_ENONCE_PROBLEME ; DETECTER_SOLUTION_IMPOSEE
TRAQUER_AJOUTS_SILENCIEUX ; DEBUSQUER_HYPOTHESES_IMPORTEES
EXPOSER_EXTERNALITES_CERTAINES                # → dette QUESTION : le demandeur doit
                                              #   avoir compris, pas seulement être averti
BALAYER_EXIGENCES_TACITES                     # sur le problème nu
ISOLER_LE_HORS_PLAN                           # noté sans être sur le chemin
RECENSER_INCONNUES                            # premier jet, à l'échelle du problème

chaque trouvaille → une dette, typée. Rien d'autre n'est produit ici.

════════ confronter(question, objet) — le mécanisme central ══════════════
# Appelé à trois niveaux, sur trois objets qui attrapent trois erreurs
# différentes. Jamais sauté : quand le champ n'a qu'un membre, le niveau
# s'exécute comme ATTAQUER_TOUT_LE_CHAMP sur ce champ d'un seul.

ISOLER_LES_EVALUATIONS                        # rien ne circule entre propositions
propositions = PRODUIRE_OPTIONS_DISTINCTES(question)
    GARANTIR_DIVERSITE_METHODE est obtenu par GÉNÉRATEUR ASSIGNÉ, jamais déclaré :
      chaque concurrent reçoit un générateur nommé et différent —
        en remontant de la cible | en descendant de l'état actuel |
        tiré de CHERCHER_ANTECEDENTS | le plan source anonymisé |
        contraint par la ressource la plus rare | optimisé sur la dimension
        que le crible a déclarée « vide »        ← attaque adverse du crible,
                                                   à coût nul, dans une
                                                   confrontation qui existe déjà
    CHERCHER_APPROCHES_NON_ENVISAGEES
POUR chaque proposition :
    SI le cadre autorise un contexte séparé :
        DECIDER_D_OUVRIR_UN_AGENT ; RESPECTER_CADRE_AUTORISE
        REDIGER_BRIEF_AGENT(périmètre, faits établis avec provenance, question,
                            format ; rien qui oriente) ; BORNER_UN_AGENT
        INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
    EXIGER_HYPOTHESES_EXPLICITES              # la liste écrite des hypothèses de
                                              # cette proposition est l'INDEX de
                                              # réouverture (cf. boucle 3)
    DEBUSQUER_HYPOTHESES_IMPORTEES
    toute hypothèse qui est une inconnue non levée → dette INCONNUE,
        et la proposition attend la quittance de cette dette
CHOISIR_ANGLES_ATTAQUE
ordre des attaques : AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE d'abord
POUR chaque proposition : ATTAQUER_UNE_OPTION(action + faits seuls ; jamais le plaidoyer)
ATTAQUER_TOUT_LE_CHAMP                        # ce qui les ferait toutes tomber,
                                              # et les conditions d'un problème mal posé
SI tout le champ tombe :
    CONSTATER_IMPOSSIBILITE ; PRESENTER_ALTERNATIVES_AU_CHOIX
    → dette QUESTION (arbitrage). Jamais un arrêt.
QUALIFIER_INDEPENDANCE_OBTENUE ; DETECTER_ERREURS_CORRELEES
SI l'indépendance obtenue est faible ET des angles non utilisés restent :
    un concurrent est REPRODUIT avec un biais explicitement assigné
    (un angle de CHOISIR_ANGLES_ATTAQUE qu'aucun n'a porté)
    # terminaison : l'ensemble des angles est fini et décroît strictement

verdict = ARBITRER_A_L_AVEUGLE
    rendu par un contexte ouvert pour cela :
      REDIGER_BRIEF_AGENT(arbitre) ← DEFINIR_CRITERES_ACCEPTATION ordonnés
                                     + le besoin
                                     + les propositions anonymisées
                                     + les attaques subies
                                     − jamais la provenance, jamais les plaidoyers
      et une consigne de plus : NOMMER toute pièce d'une proposition battue que
      la retenue ne porte pas et qu'aucune attaque n'a tuée
    précédence = critères d'acceptation ordonnés, puis RECENSER_CONTRAINTES_DURES.
    JAMAIS le nombre de voix.
    BORNER_UN_AGENT ; INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION

CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_PORTEE_DECISION
NOMMER_FAIT_QUI_FERAIT_BASCULER               # marque le fait comme pivot
CONSERVER_OPTIONS_ECARTEES                    # avec leur viabilité : c'est le dauphin
chaque pièce nommée par l'arbitre → dette CHOIX (greffer ou non), jamais un import muet
toute pièce du verdict qu'aucune proposition ne portait :
    RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
QUALIFIER_ETAT_RESOLUTION(verdict)            # quittance
RETOURNER verdict

════════ NIVEAU 1 — quel problème planifie-t-on ? ════════════════════════
confronter(« quelle lecture du besoin ? », crible)
FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
VERIFIER_FIDELITE_CIBLE_BESOIN
    SI la cible est satisfaisable sans produire l'effet voulu :
        l'écart nomme un critère manquant ou une contrainte dure non recensée ;
        cette pièce entre au crible, la cible est reformulée.
        # l'ensemble des critères ne fait que croître : l'espace des cibles
        # admissibles ne fait que se restreindre. Ni plafond, ni cycle.
CHAINER_ETAT_ACTUEL_VERS_CIBLE                # dans les deux sens

════════ NIVEAU 2 — quel squelette ? ═════════════════════════════════════
# Un seul objet de niveau 2 : la suite ordonnée de pas qui relie l'état
# actuel à la cible. Le découpage n'est PAS un objet séparé — c'est le grain
# du squelette. Les concurrents diffèrent par principe de partition
# (par objectif | par système touché | par domaine d'inconnue | par
# irréversibilité) : sur un travail massif ils divergent réellement, sur
# une demande de deux lignes ils convergent et le niveau coûte une attaque.

squelette = confronter(« quel chemin de l'état actuel à la cible ? », crible + faits)

════════ LE MOTEUR — vagues d'apurement ══════════════════════════════════
RÉPÉTER :

  ── GÉNÉRATEUR n°2 : interrogation des pas neufs ───────────────────────
  pas_neufs = les pas que RATTACHER_TOUTE_PIECE_A_SON_ORIGINE désigne comme
              nés de la version courante (première vague : tous)
  POUR chaque pas neuf, trois questions :
    (a) sur quoi repose-t-il ?
        RECENSER_INCONNUES(pas) ; EXIGER_HYPOTHESES_EXPLICITES(pas)
        DEBUSQUER_HYPOTHESES_IMPORTEES(pas)          → dettes INCONNUE
    (b) choisit-il quelque chose ?
        ORIENTER_CHOIX(pas) :
            il manque un fait        → dette INCONNUE
            il faut une préférence   → dette QUESTION
            vrai choix à instruire   → dette CHOIX
        DISTINGUER_CHOIX_ET_CONSEQUENCE
        DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE
            si mécanique : CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
                           avant de l'écarter
    (c) qu'est-ce qui dira qu'il a réussi ?
        DEFINIR_ATTENDU_OBSERVABLE(pas)
            innommable sans en savoir plus        → ce n'est pas un pas,
                                                     c'est une dette INCONNUE
            nommable seulement en plusieurs observables indépendants
                                                  → dette CONTRAT
        CONTROLER_TAILLE_DES_ETAPES(pas)

  ── CRIBLE DIFFÉRENTIEL : une fois par vague, sur le COUPLE besoin×squelette ─
  BALAYER_EXIGENCES_TACITES :
      POUR chaque dimension (sécurité, montée en charge, maintenabilité,
      coût, accessibilité, et celles que le territoire impose) la vague se
      clôt par UNE disposition nommée, jamais par un « rien à signaler » global :
          servie par le pas N | déclarée hors-plan (ISOLER_LE_HORS_PLAN)
          | dette QUESTION
  TRAQUER_AJOUTS_SILENCIEUX(squelette)          # pas que personne n'a demandés
  VERIFIER_COUVERTURE_OBJECTIFS                 # objectif servi par aucun pas → dette CHOIX
  VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(squelette) # invariant franchi → dette CHOIX
  EVALUER_EXIGENCE_TACHE                        # rappelée ici : le nombre de dettes
      # et leur nature sont maintenant observables. Elle ne peut qu'AJOUTER une
      # technique autorisée, jamais en retirer une d'un objet qui existe.
      # Monotone : elle ne peut donc pas boucler.

  ── APUREMENT : cinq types, cinq règles de fermeture ───────────────────

  DETTE « INCONNUE »
    CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION ; QUALIFIER_PORTEE_INCONNUE
    DISTINGUER_INDETERMINE_ET_NON_CHERCHE
    ORDONNER_INCONNUES_SANS_ECARTER             # ordonne, n'abandonne rien
    AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE         # départage les ex æquo
    SI la portée déborde le périmètre courant (contrat) : escalade au parent,
       jamais tranchée localement
    « construction » → lever(inconnue)
    « exécution »    → CONTRE_ÉPREUVE ci-dessous, avant toute quittance

  lever(inconnue) :
    SI plusieurs domaines d'enquête séparables ET le cadre autorise les agents :
        PARALLELISER_ENQUETE ; un agent par domaine
        DECIDER_D_OUVRIR_UN_AGENT ; REDIGER_BRIEF_AGENT(les faits établis y voyagent,
            pour que personne ne refasse le travail) ; BORNER_UN_AGENT
        à chaque retour : INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
        AVANT d'intégrer, croiser les retours ENTRE EUX :
            DETECTER_CONTRADICTION_ENTRE_SOURCES ; DETECTER_ORIGINE_COMMUNE_SOURCES
            DETECTER_ERREURS_CORRELEES
        ARRETER_ORCHESTRATION                   # un agent de plus ne changerait rien
    TANT QUE non levée ET il reste un moyen non essayé :
        CHOISIR_MOYEN_DE_LEVEE(parmi les moyens NON ENCORE ESSAYÉS)
            inspection, calcul, mesure  → MENER_VERIFICATION
            source, précédent           → CHERCHER_ANTECEDENTS
            action bornée et réversible → LEVER_INCONNUE_PAR_ACTION_REVERSIBLE
                GARDE (principe 2) : interdite si l'action coïncide avec un
                engagement du plan. Si le seul moyen de lever est de FAIRE le
                pas, l'inconnue n'est pas levable ici : elle passe la contre-épreuve.
            question                    → dette QUESTION
    # terminaison : l'ensemble des moyens est fini et décroît strictement.
    SI épuisé : DISTINGUER_INDETERMINE_ET_NON_CHERCHE
        vraiment indéterminable → CONTRE_ÉPREUVE
        sinon                   → dette QUESTION (jamais une livraison avec un trou)
    régime des faits, une fois par fait obtenu :
        CONSIGNER_PROVENANCE_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE ; ENONCER_LIMITES_FAIT
        RENDRE_INCERTITUDE_VISIBLE
        JUGER_PEREMPTION_FAIT → périssable : INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
        plusieurs sources : DETECTER_CONTRADICTION_ENTRE_SOURCES →
            DETECTER_ORIGINE_COMMUNE_SOURCES → RESOUDRE_CONTRADICTION
            (date, version, périmètre, définition — sinon dette CHOIX « contesté »)
        sources convergentes : DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
        SI le fait est PIVOT (nommé par NOMMER_FAIT_QUI_FERAIT_BASCULER,
           ou plus d'un pas en dépend) :
            seconde levée par un moyen d'une AUTRE nature, ISOLER_LES_EVALUATIONS ;
            puis DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
        SI le fait contredit une hypothèse NOMMÉE par une pièce déjà close :
            cette pièce seule est rouverte, le fait inscrit à côté d'elle ;
            REUTILISER_ACQUIS sur tout le reste
            # l'index de réouverture est la liste d'hypothèses écrite par
            # EXIGER_HYPOTHESES_EXPLICITES : elle se lit, elle ne se calcule pas

  CONTRE_ÉPREUVE d'un classement « exécution »  (principe 14 — contrôlée par le
  système, jamais déléguée à l'utilisateur, jamais décidée en silence) :
    (1) DISTINGUER_INDETERMINE_ET_NON_CHERCHE rend « indéterminable maintenant »
    (2) CHOISIR_MOYEN_DE_LEVEE sur l'ensemble des moyens qu'INVENTORIER_CAPACITES
        rend disponibles retourne l'ensemble VIDE
    (3) DEFINIR_ATTENDU_OBSERVABLE sur le SIGNAL qui la révélera à l'exécution :
        s'il n'est pas nommable, le classement est faux → retour en « construction »
    (4) SI QUALIFIER_PORTEE_INCONNUE dit qu'elle peut changer plus d'un pas :
        le classement LUI-MÊME devient une dette CHOIX, confrontée et arbitrée
    (5) REFUSER_AUTO_CONFIRMATION : le classement ne vaut pas parce que le
        système l'affirme
    les quatre épreuves passées → quittance « branchée », dette BRANCHE
    # C'est ici que le principe 7 est gardé : sans contre-épreuve, un plan se
    # remplit de branches qui sont des reports déguisés.

  DETTE « QUESTION »
    DECIDER_D_INTERROGER_UTILISATEUR            # moins cher de vérifier soi-même ?
        si oui → la dette se retype INCONNUE. La question est un dernier recours.
    FORMULER_QUESTION_ACTIONNABLE ; QUALIFIER_PORTEE_DECISION
    PRESENTER_ALTERNATIVES_AU_CHOIX si le point se ramène à deux options
    la dette reste ouverte jusqu'au POINT DE VAGUE

  DETTE « CHOIX »
    ETABLIR_DEPENDANCES_ENTRE_DECISIONS         # ordre de tranchage
    les choix MUTUELLEMENT INDÉPENDANTS sont confrontés en aveugle mutuel
        (aucun ne voit la résolution de l'autre) ; les dépendants, en ordre
    POUR chacun : confronter(le choix, faits + squelette)      ← NIVEAU 3
        verdict nommant un fait absent du registre des faits → dette INCONNUE
            # terminaison : le fait doit être NOUVEAU, vérifiable par lecture
            # de l'ardoise, et le registre des faits ne fait que croître
        verdict « tranché avec compromis » → dette QUESTION (arbitrage) :
            l'utilisateur voit le compromis matériel AVANT que le plan ne le referme

  DETTE « CONTRAT »
    DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(pas)
    contrat = { périmètre (contenu STRICTEMENT dans le parent) ;
                faits d'entrée = socle + faits du parent, avec provenance ;
                FORMULER_CIBLE_OBSERVABLE locale + DEFINIR_CRITERES_ACCEPTATION locaux ;
                contraintes dures et invariants hérités ;
                interfaces promises aux autres contrats ;
                termes figés }
    honorer(contrat) : le MÊME moteur, mêmes vagues, MÊME ardoise
        (les dettes du contrat sont marquées de son nom — c'est pourquoi un
         contrat n'a pas de file de réserve : ses questions sont drainées au
         prochain point de vague comme les autres)
        interdit dans un contrat : SEPARER_DEMANDE_ET_BESOIN,
            AMORCER_DEPUIS_PLAN_EXISTANT, CONTESTER_ENONCE_PROBLEME,
            DETECTER_SOLUTION_IMPOSEE, DECLINER_SI_PAS_DE_PLAN,
            LIRE_TECHNIQUES_AUTORISEES, INVENTORIER_CAPACITES,
            IDENTIFIER_DESTINATAIRE, RECENSER_RESSOURCES_EXECUTION
            # un enfant qui reconteste le besoin ou recalcule le cadre ne peut
            # que diverger. Tout le reste lui est ouvert, EXPOSER_EXTERNALITES_
            # CERTAINES et BALAYER_EXIGENCES_TACITES compris : il les inscrit,
            # il ne les tranche pas.
        SI le contrat ne peut être honoré tel qu'il est écrit :
            CONSTATER_IMPOSSIBILITE(local) ; remonter le TERME à modifier et le
            fait qui l'impose → le parent FIGE ce terme et rejoue ce seul enfant
            SI honorer exigerait de RELÂCHER un terme déjà figé, une contrainte
            dure ou un objectif : ce n'est plus une renégociation, c'est une
            escalade → dette QUESTION à la racine
    recomposer :
        ORDONNER_PAR_PREREQUIS à travers les frontières
        IDENTIFIER_ETAPES_SIMULTANEES → VERIFIER_SIMULTANEITE_POSSIBLE
            (deux contrats « parallèles » qui se disputent un approbateur ne le sont pas)
        VERIFIER_COHERENCE_ENSEMBLE ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN
        incohérence → elle nomme deux contrats et l'interface qui les sépare :
            cette interface devient un TERME FIGÉ chez les deux,
            REUTILISER_ACQUIS, et ces deux contrats seuls sont rejoués

  DETTE « BRANCHE »
    reste ouverte jusqu'à la mise en forme, où CONSTRUIRE_BRANCHE_CONDITIONNELLE
    l'écrit : critère de déclenchement = l'observable nommé en contre-épreuve (3),
    plus son repli.

  ── POINT DE VAGUE — l'unique rendez-vous avec l'utilisateur ────────────
  atteint quand TOUTE dette qui pouvait avancer sans l'utilisateur a avancé.
  # état vérifiable par lecture de l'ardoise, pas une appréciation d'opportunité
  SI des dettes QUESTION sont ouvertes :
      un seul envoi, groupé : toutes les questions, tous les arbitrages,
      toutes les externalités certaines
      SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE   # aucune valeur par défaut
      à la réponse :
        pas de réponse            → on attend. Rien ne repart.
        « je ne sais pas »        → la question n'était pas actionnable :
            FORMULER_QUESTION_ACTIONNABLE à nouveau, avec
            PRESENTER_ALTERNATIVES_AU_CHOIX et QUALIFIER_PORTEE_DECISION
            (ce qui change si la réponse est fausse) — on explique, on ne tranche pas
        réponse contredisant une réponse antérieure → le besoin est mal cerné :
            la contradiction devient une pièce du crible et rouvre le NIVEAU 1
            sur ce seul point, porteuse des deux réponses ; REUTILISER_ACQUIS
        sinon : chaque dette reçoit sa quittance

  ── RÉÉCRITURE — jamais un rapiéçage ───────────────────────────────────
  SI une décision close change le squelette :
      squelette = DERIVER_ACTIONS_DEPUIS_DECISIONS(décisions closes)
      ORDONNER_PAR_PREREQUIS ; AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE (départage
          entre deux ordres également valides)
      RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
          tout pas dont l'origine n'est ni un verdict, ni un fait, ni une réponse
          de l'utilisateur, ni une contrainte héritée est RETIRÉ — jamais gardé
          par prudence ; et l'origine désigne les pas neufs de la vague suivante

  ── SORTIE DE VAGUE — état vérifiable par lecture de l'ardoise ─────────
  SORTIR quand, toutes les quatre étant vraies :
      aucun pas du squelette non interrogé dans sa version courante ;
      aucune dette sans quittance ;
      aucune dimension du crible différentiel sans disposition nommée ;
      aucun non-appel conditionnel sans sa condition écrite.

════════ MISE EN FORME — la dernière vague ═══════════════════════════════
# Ses trouvailles sont des dettes ordinaires : si elle en produit, le moteur
# reprend. Ce n'est pas une phase, c'est une vague de plus.

REPERER_POINTS_ENGAGEMENT                     # ferme une option, consomme une ressource
SUR CES POINTS SEULEMENT — appareil mineur, inatteignable autrement :
    QUALIFIER_REVERSIBILITE ; DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE
        (un retour arrière vérifié, pas affirmé — ou le constat qu'il n'existe pas)
    DEFINIR_SIGNAUX_ECHEC ; PLACER_POINTS_VERIFICATION
        (là où l'erreur se propagerait avant que l'attendu du pas ne la révèle)
    RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT
    SI un acteur touché peut s'adapter : ANTICIPER_TIERS_REACTIF
    STATUER_SUR_RISQUE_RESIDUEL
        tout résidu « accepté » ou « délégué » → dette QUESTION
SI RECENSER_OBLIGATIONS_FORMELLES non vide OU un point d'engagement est irréversible :
    PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION (jamais l'exécutant)
    VERIFIER_COUVERTURE_BLOQUANTS             # toute partie capable de bloquer
                                              # reçoit un point de passage
SI IDENTIFIER_DESTINATAIRE rend un suiveur humain distinct de l'exécutant :
    PLACER_JALONS_CONSTAT                     # distincts des autorisations
SI RECENSER_RESSOURCES_EXECUTION rend personnes, délais ou budget :
    offre groupée au point de vague : PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE ;
    PROPOSER_MARGES                           # jamais produites d'office
POUR chaque dette BRANCHE : CONSTRUIRE_BRANCHE_CONDITIONNELLE
POUR chaque fait périssable : la re-vérification est placée juste avant le pas qui en dépend
IDENTIFIER_ETAPES_SIMULTANEES → VERIFIER_SIMULTANEITE_POSSIBLE
CONTROLER_TAILLE_DES_ETAPES(plan) ; ELAGUER_ETAPES_INUTILES

════════ CONTRÔLE ET ÉMISSION ════════════════════════════════════════════
VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_COHERENCE_ENSEMBLE
VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN (branches comprises)
VERIFIER_ADOSSEMENT_AFFIRMATIONS (y compris les affirmations apparues tard)
VERIFIER_FAISABILITE_PAR_EXECUTANT
    SI échec : repli sur le dauphin — CONSERVER_OPTIONS_ECARTEES rend l'option
    suivante, on rejoue CETTE SEULE vérification, pas le choix entier
REFUSER_AUTO_CONFIRMATION

REDIGER_PLAN(selon le TEMPLATE fourni au système)
    # l'architecture ne définit pas ce format et n'en porte aucune trace :
    # seul le contenu grossit avec la complexité (principe 10)
ELAGUER_LA_PROSE
    # critère : retirer tout ce qu'une instance de l'exécutant, contexte vierge,
    # lira ou vérifiera de toute façon. Le comment n'est dirigé que là où il
    # n'est pas évident. Aucune justification, aucun archivisme.
RENDRE_ACTIONNABLE_PAR_AGENT
SIGNALER_LES_LIMITES                          # GARDE : ne porte que des exclusions
    # DÉLIBÉRÉES, chacune tracée à une décision close ou à DELIMITER_PERIMETRE.
    # Un point non résolu n'y entre jamais : il retourne en dette.
ISOLER_LE_HORS_PLAN ; PREVOIR_SUITE_EN_CAS_DE_SUCCES
CONTROLER_CONTENU_FINAL                       # attendus falsifiables, aucune préférence
                                              # promue en contrainte, aucun pas sans
                                              # origine, rien d'incertain donné pour acquis
CONTROLER_INTEGRITE_DOCUMENT

— deux épreuves externes, aux objets et aux briefs DIFFÉRENTS —
FAIRE_CONTROLER_PAR_UN_TIERS(le plan + les critères + le besoin ;
                             jamais l'ardoise, jamais le raisonnement)
EPROUVER_AUTONOMIE_DU_TEXTE(le plan SEUL, à un lecteur qui n'a rien vu :
                            « où devrais-tu redemander quelque chose ? »
                            — pas « exécute-le »)
    TRI DES RETOURS, obligatoire (sans lui, cette épreuve gonfle le plan) :
      le lecteur réclame ce que le plan aurait dû décider   → dette
      le lecteur réclame ce qu'il lira ou vérifiera lui-même → refus écrit,
          avec sa raison : c'est ELAGUER_LA_PROSE qui a raison, pas lui
INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
DETECTER_ERREURS_CORRELEES ; QUALIFIER_INDEPENDANCE_OBTENUE
    # les deux briefs diffèrent matériellement : c'est le seul chemin de preuve
    # réellement distinct que je sache construire

ROUTEUR DES DÉFAUTS — tout finding devient une dette du type que sa nature désigne :
    prémisse fausse         → pièce du crible, NIVEAU 1 rejoué sur ce seul point
    fait douteux            → INCONNUE
    décision mal fondée     → CHOIX
    pas trop gros           → CONTRAT
    défaut de rédaction     → corrigé ici
  Il s'y ferme par la règle de son type. Pas de boucle spéciale, pas de compteur.

REDIGER_TRACABILITE_SEPAREE(clôture de l'ardoise)
    # ce qui a tranché et pourquoi, ce qui a été vérifié et avec quelles limites,
    # ce qui a été attaqué et ce qui subsiste, et chaque non-appel avec sa condition
PLACER_ET_NOMMER_LE_FICHIER ; RESTITUER_EN_BREF
FIN — le système s'arrête. Faire relire, approuver ou exécuter n'est pas une étape.
```

## Les boucles

**Six, toutes déclenchées par un observable, aucune avec un budget.**

1. **Fidélité cible/besoin** — déclenchée par l'échec de `VERIFIER_FIDELITE_CIBLE_BESOIN` ; remonte au crible et à la formulation de la cible. Termine parce que chaque tour ajoute un critère d'acceptation ou une contrainte dure et n'en retire jamais : l'espace des cibles admissibles se restreint de façon monotone, et son épuisement est observable — `ATTAQUER_TOUT_LE_CHAMP` fait tomber le champ entier et la boucle sort par l'utilisateur, jamais par un arrêt.
2. **Levée d'une inconnue** — déclenchée par l'échec du moyen essayé ; remonte à `CHOISIR_MOYEN_DE_LEVEE`. Termine par épuisement d'un ensemble fini de moyens qui décroît strictement. L'épuisement ne clôt rien de lui-même : il ouvre soit la contre-épreuve, soit une question.
3. **Réouverture par un fait** — déclenchée par un fait établi qui **contredit une hypothèse nommée** par une pièce déjà close ; remonte à cette pièce seule, jamais à ses voisines, jamais en amont d'elle. L'index est la liste d'hypothèses écrite par `EXIGER_HYPOTHESES_EXPLICITES` : elle se lit. Termine parce que le fait doit être absent du registre des faits, que cette absence se vérifie par lecture de l'ardoise, et que le registre des faits ne fait que croître.
4. **La vague** — déclenchée par l'existence de pas neufs ou de dettes ouvertes ; ne remonte nulle part, c'est le moteur. Termine par un argument en deux temps : une nouvelle version du squelette exige qu'une **décision close** l'ait modifié ; les décisions closes sortent d'un ensemble fini de choix litigieux qui ne se rouvrent que par la boucle 3, elle-même monotone. Sa sortie est un état vérifiable par lecture, énoncé plus haut en quatre lignes.
5. **Renégociation d'un contrat** — déclenchée par un `CONSTATER_IMPOSSIBILITE` local qui **nomme le terme** à modifier ; remonte d'exactement un cran, au parent qui a écrit le contrat. Termine parce qu'une renégociation ne peut que **figer** un degré de liberté, jamais en rendre : le nombre de degrés libres décroît strictement. La même monotonie couvre la recomposition, où une incohérence d'interface fige cette interface chez les deux contrats qu'elle nomme. Relâcher un terme déjà figé n'est pas une boucle : c'est une escalade vers l'utilisateur.
6. **Descente en contrats** — déclenchée par un pas dont l'attendu observable n'est nommable qu'en plusieurs observables indépendants. Termine par containment strict des périmètres : la condition cesse d'être vraie sur un pas qui reçoit un attendu unique. Aucune profondeur maximale.

Le routeur des défauts n'ouvre **pas** une septième boucle : un finding devient une dette ordinaire et se ferme par la règle de son type. C'est le mécanisme de A, et c'est le bon.

## Fonctions appelées plusieurs fois, et pourquoi

| Fonction | Objets distincts |
|---|---|
| `confronter` (bloc) | trois niveaux : la lecture du besoin, le squelette, chaque choix litigieux — trois erreurs différentes, c'est le principe 3 |
| `RECENSER_INCONNUES` | le problème (crible), chaque pas neuf, chaque contrat — trois échelles, et un squelette retenu nomme des inconnues que le précédent ne nommait pas |
| `ORIENTER_CHOIX` | chaque pas, chaque contrat |
| `DEFINIR_ATTENDU_OBSERVABLE` | trois emplois : l'attendu d'un pas ; le **détecteur de taille** (plusieurs observables indépendants → contrat) ; le **signal de révélation** d'une inconnue d'exécution en contre-épreuve |
| `BALAYER_EXIGENCES_TACITES` | deux placements non redondants : sur le problème nu au crible, puis sur le couple besoin × squelette à chaque vague. Le premier attrape ce que l'énoncé tait, le second ce que le chemin implique — c'est ma réponse à l'ancrage de C et au placement trop précoce de B |
| `EXIGER_HYPOTHESES_EXPLICITES` | par proposition en confrontation, par pas à l'interrogation — et c'est deux fois le même service : produire l'index de réouverture |
| `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE` | après chaque verdict (pièces qu'aucune proposition ne portait) et à chaque réécriture (purger les scories **et** désigner les pas neufs) |
| `REUTILISER_ACQUIS` | entrée de chaque contrat, chaque réouverture, et l'ardoise d'une passe antérieure — c'est ce qui empêche la réouverture de devenir un redo |
| `CONTROLER_TAILLE_DES_ETAPES` | le pas pendant l'interrogation, le plan à la mise en forme |
| `VERIFIER_COHERENCE_ENSEMBLE` | les décisions, chaque recomposition de contrats, le document |
| `ORDONNER_PAR_PREREQUIS` | à l'intérieur d'un contrat, puis à travers les frontières : deux problèmes d'ordre différents |
| `AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE` | ordonner les inconnues, départager deux ordres de pas également valides, et **ordonner les attaques** en confrontation |
| `DETECTER_CONTRADICTION_ENTRE_SOURCES`, `DETECTER_ORIGINE_COMMUNE_SOURCES`, `DETECTER_ERREURS_CORRELEES` | par fait multi-sources, et entre les retours des agents parallèles avant intégration |
| `JUGER_PEREMPTION_FAIT` | par fait obtenu, et sur tout le socle hérité en passe n+1 |
| `REFUSER_AUTO_CONFIRMATION` | chaque retour d'agent, chaque épreuve externe, chaque classement d'inconnue |
| `EVALUER_EXIGENCE_TACHE` | à la porte, puis à chaque vague — parce que ses observables (nombre et nature des dettes) n'existent pas à la porte. Contrainte : elle ne peut qu'ajouter |
| `FORMULER_QUESTION_ACTIONNABLE` | autant de fois qu'il y a de questions ; `SUSPENDRE_ENQUETE_ET_DEMANDER` une seule fois par point de vague — l'utilisateur est interrompu par vagues, jamais par questions |

## Fonctions laissées de côté

**Aucune exclusion absolue, et l'argument n'est pas celui de A.** A refusait d'exclure pour ne pas trouer sa preuve d'exhaustivité ; C excluait cinq fonctions en invoquant son domaine d'emploi. Or le brief interdit les domaines d'emploi : **dans une architecture à régime unique, une exclusion absolue est un régime caché.** Exclure `PLACER_JALONS_CONSTAT` pour toujours, c'est décréter que le destinataire n'est jamais un humain ; exclure `PROPOSER_CHIFFRAGE`, c'est décréter qu'il n'y a jamais de budget. Ce sont des restrictions de domaine déguisées en économies.

Je paie ce refus par une obligation : **tout non-appel est conditionnel, sa condition est un observable, et elle est écrite dans l'ardoise.** Un non-appel devient ainsi un objet que le contrôle final peut vérifier, au lieu d'un silence. Les seize conditions :

1. `AMORCER_DEPUIS_PLAN_EXISTANT` / `SEPARER_DEMANDE_ET_BESOIN` : exclusives, décidées par la porte d'entrée.
2. `LEVER_INCONNUE_PAR_ACTION_REVERSIBLE` : non appelée si `INVENTORIER_CAPACITES` ne rend aucune action réversible et bornée sur le système cible — ou si la seule action possible est un engagement du plan (garde du principe 2).
3. `PARALLELISER_ENQUETE`, `ARRETER_ORCHESTRATION` : si `LIRE_TECHNIQUES_AUTORISEES` n'autorise pas les agents, ou s'il n'existe qu'un domaine d'enquête séparable.
4. `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` : si aucun pas ne réclame plus d'un attendu observable indépendant.
5. `CONSTRUIRE_BRANCHE_CONDITIONNELLE` : si aucune inconnue n'a passé la contre-épreuve d'exécution. **C'est le cas normal, pas l'exception** — le principe 7 est tenu ici.
6. Toute la famille du risque et du retour arrière (`RECENSER_RISQUES_PAR_ORIGINE`, `QUALIFIER_VRAISEMBLANCE_RISQUE`, `QUALIFIER_RAYON_IMPACT`, `QUALIFIER_REVERSIBILITE`, `DEFINIR_RETOUR_ARRIERE`, `EPROUVER_RETOUR_ARRIERE`, `DEFINIR_SIGNAUX_ECHEC`, `PLACER_POINTS_VERIFICATION`, `STATUER_SUR_RISQUE_RESIDUEL`) : inatteignable si `REPERER_POINTS_ENGAGEMENT` rend l'ensemble vide. Sur un plan sans point d'engagement, cet appareil n'existe pas.
7. `ANTICIPER_TIERS_REACTIF` : si `RECENSER_DEPENDANCES_EXTERNES` ne rend aucun acteur capable de s'adapter — un dépôt de code ne réagit pas au plan qui le vise.
8. `PLACER_JALONS_CONSTAT` : si `IDENTIFIER_DESTINATAIRE` ne rend aucun suiveur humain distinct de l'exécutant — l'attendu observable du pas est alors déjà le constat.
9. `PLACER_POINTS_AUTORISATION`, `DESIGNER_AUTORITE_AUTORISATION`, `VERIFIER_COUVERTURE_BLOQUANTS` : si `RECENSER_OBLIGATIONS_FORMELLES` est vide et qu'aucun point d'engagement n'est irréversible.
10. `PROPOSER_AFFECTATION`, `PROPOSER_CHIFFRAGE`, `PROPOSER_MARGES` : si `RECENSER_RESSOURCES_EXECUTION` ne rend ni personne, ni délai, ni budget — les produire alors serait exactement les produire d'office, ce que leur définition interdit.
11. `INSCRIRE_REVERIFICATION_FAIT_PERISSABLE` : si `JUGER_PEREMPTION_FAIT` ne rend aucun fait périssable.
12. `RESOUDRE_CONTRADICTION`, `DETECTER_ORIGINE_COMMUNE_SOURCES` : si aucun fait n'a deux sources.
13. `CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE` : si `DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE` ne classe aucun pas comme mécanique.
14. `PRESENTER_ALTERNATIVES_AU_CHOIX` : si aucune question ne se ramène à deux options de haut niveau.
15. `CONSTATER_IMPOSSIBILITE` : si aucun champ ne tombe entièrement et qu'aucun contrat n'est inhonorable.
16. `DECLINER_SI_PAS_DE_PLAN` : appelée à la porte, ne s'exerce que si aucun problème de planification n'est posé. Et neuf fonctions sont **interdites dans un contrat** (liste dans le pseudo-code) : leurs réponses sont globales, un enfant qui les recalcule ne peut que diverger.

## Invariants tenus en permanence

**I1** — Zéro dette ouverte à l'émission. Un plan livré ne contient jamais de point ouvert, et cela se vérifie en lisant un fichier.
**I2** — Le système ne s'arrête jamais de sa propre autorité. `DECLINER_SI_PAS_DE_PLAN` à la porte est la seule sortie ; `CONSTATER_IMPOSSIBILITE`, l'épuisement d'un moyen, un contrat inhonorable et un champ entièrement tombé remontent tous à l'utilisateur.
**I3** — Toute pièce du plan a une origine écrite — un verdict, un fait, une réponse de l'utilisateur, une contrainte héritée. Une pièce sans origine est retirée, jamais conservée par prudence.
**I4** — Le registre des faits et l'ensemble des termes figés ne font que croître ; rien n'en sort. C'est l'argument de terminaison de toutes les boucles, et il se vérifie par lecture.
**I5** — Aucun compteur, aucun plafond, aucun budget, nulle part. Le système ne raisonne jamais en coût ; `LIRE_TECHNIQUES_AUTORISEES` est la seule borne, et `EVALUER_EXIGENCE_TACHE` ne peut qu'ajouter.
**I6** — L'appareil de risque, de retour arrière et d'autorisation n'est atteignable que par `REPERER_POINTS_ENGAGEMENT` ou `RECENSER_OBLIGATIONS_FORMELLES`. Il ne peut structurellement pas devenir le centre.
**I7** — Aucune exclusion absolue de fonction ; tout non-appel porte une condition observable, écrite.
**I8** — Le système n'agit que par `LEVER_INCONNUE_PAR_ACTION_REVERSIBLE`, jamais sur une action qui est elle-même un engagement du plan.
**I9** — L'utilisateur n'est sollicité qu'aux points de vague, en un envoi, et jamais sur ce que le système peut établir seul — la contre-épreuve du classement d'exécution ne lui est en particulier jamais soumise.
**I10** — Prioriser n'écarte jamais : aucune dette n'est fermée par déclassement de priorité.
**I11** — Le crible ne produit rien : ni agent, ni texte livrable, ni confrontation. C'est ce qui permet qu'il soit exhaustif sans être cérémonieux.
**I12** — L'architecture ne porte aucune trace du format du plan : le template est une entrée.

---

# QUATRIÈME PARTIE — AUTO-ÉVALUATION

| | S | F | B | U | P |
|---|---|---|---|---|---|
| **L'Ardoise** | 4 | 4 | 4 | 4 | 4 |

**Suivabilité 4, pas 5.** L'ardoise est un fichier et le squelette est un texte : rien à tenir de tête, aucun graphe, aucun compteur, aucune file recalculée — c'est mieux que A et que B. Mais c'est moins bien que C : là où C tient en trois questions posées à des lignes, je demande de tenir cinq types de dette, cinq règles de fermeture, un routeur, la charge utile d'un contrat et une contre-épreuve en cinq points. Et surtout, le **point de vague** — « toute dette qui pouvait avancer sans l'utilisateur a avancé » — se présente comme un état vérifiable mais reste un jugement : un modèle pressé déclenchera l'envoi trop tôt. C'est le seul endroit de l'architecture où je dis « vérifiable » sans pouvoir le prouver.

**Fidélité 4, pas 5.** Je ne vois aucun principe violé, et j'en tiens deux que personne ne tenait : la contre-épreuve du classement d'exécution (principe 14, contrôle par le système, jamais délégué) et la garde qui interdit de lever une inconnue par l'action même que le plan engage (principe 2 croisé avec le 14). Mais la fidélité de mon architecture repose en deux endroits sur la bonne foi du modèle, et je préfère le dire que le maquiller. Premièrement, la ligne des « vides » du crible : un modèle qui écrit « vide : contraintes dures, obligations formelles, préférences » sans avoir cherché produit un artefact indiscernable d'un crible honnête. Je l'ai atténué — un concurrent de niveau 1 est explicitement biaisé vers la dimension que le crible a déclarée vide, ce qui met les vides à l'épreuve dans une confrontation qui existe déjà, à coût nul — mais atténuer n'est pas vérifier. Deuxièmement, le point (3) de la contre-épreuve, « nommer le signal qui révélera cette inconnue à l'exécution », se satisfait d'une phrase plausible. Mon architecture rend la paresse **auditable** — une ligne absente se voit dans l'ardoise — elle ne la rend pas impossible.

**Boucles 4, pas 5.** Six boucles, toutes déclenchées par un observable nommé, toutes remontant à un endroit désigné par la nature du déclencheur, aucun budget nulle part. Les arguments de terminaison sont monotones et se vérifient par lecture, pas par calcul. La faiblesse est la boucle 4, la vague : son argument est en deux temps — une réécriture exige une décision close, les décisions closes sont en nombre fini et ne se rouvrent que par la boucle 3 qui est elle-même monotone. C'est correct mais c'est le seul raisonnement de l'architecture qu'on ne vérifie pas d'un coup d'œil, et un raisonnement en deux temps est un raisonnement qu'un lecteur pressé abrège.

**Usage 4, pas 5.** Toutes les répétitions portent sur des objets distincts et je peux nommer l'objet à chaque fois ; aucune fonction ne défile une fois dans l'ordre. Mais je n'exclus rien absolument, et si j'ai un argument pour ça — une exclusion absolue est un régime caché — il reste que je n'ai jamais eu à trancher un arbitrage difficile d'exclusion. C'est une faiblesse de preuve, pas seulement de goût : A avait le même trou et je ne l'ai pas comblé, je l'ai rebaptisé.

**Proportionnalité 4, pas 5.** Sur une demande de deux lignes, le plancher est : la porte (six lectures), le crible (une passe de lecture dont l'essentiel tient en une ligne de vides), deux confrontations qui s'effondrent en champ d'un seul et coûtent une attaque chacune, une vague de trois pas, aucune branche, aucun appareil de risque, deux agents de contrôle. C'est nettement moins que A (qui l'avoue) et que B. C'est plus que C, et je sais pourquoi : le crible est le prix que je paie pour ne pas avoir l'angle mort de C, et les deux épreuves externes sont le prix du principe 13. Je les tiens pour bien dépensés, mais ce sont des dépenses fixes, et une architecture parfaitement proportionnelle n'en aurait aucune.

## Ce que je n'ai pas réussi à résoudre

**L'indépendance des concurrents aveugles.** C'est traité comme un problème de méthode, comme demandé, et j'ai fait trois choses concrètes : chaque concurrent reçoit un **générateur nommé et différent** plutôt qu'une consigne de diversité ; quand `QUALIFIER_INDEPENDANCE_OBTENUE` rend « faible », un concurrent est reproduit avec un **biais explicitement assigné** tiré de la liste finie des angles d'attaque ; et les deux épreuves finales ont des briefs matériellement différents (plan + critères + besoin d'un côté, plan nu de l'autre), ce qui est le seul chemin de preuve réellement distinct que j'aie su construire. Tout cela améliore la divergence des discours. Rien de tout cela ne change les poids. `QUALIFIER_INDEPENDANCE_OBTENUE` reste une auto-évaluation, et quand elle dit « forte » personne ne peut la contredire.

**Le crible n'est pas vérifiable de l'intérieur.** Une ligne manquante se voit ; un « vide » erroné ne se voit pas. Le seul remède complet serait de faire repasser le crible par un agent aveugle qui n'a vu que la demande — je ne l'ai pas mis, parce que sur la demande ordinaire c'est un agent de plus pour un rendu presque toujours identique, et que je ne voulais pas d'une dépense fixe supplémentaire. J'ai préféré l'atténuation par le concurrent biaisé. C'est un compromis, et il peut être mauvais.

**Le point de vague.** Dit plus haut : c'est le seul endroit de l'architecture qui demande une appréciation là où je prétends fournir un état.

**Le contrat qui révèle que le découpage était faux.** B a ce trou et je ne l'ai pas comblé : quand une incohérence de recomposition ne se laisse pas traduire en une interface à figer — parce que c'est la partition elle-même qui était mauvaise — ma seule issue est l'escalade vers l'utilisateur. On pourrait soutenir que rejouer le niveau 2 serait plus juste, mais alors la terminaison par gel monotone tombe, et je préfère une architecture qui termine et qui remonte à une architecture qui boucle proprement sur le papier.

**L'auto-contrôle de la proportionnalité.** L'ardoise enregistre combien de dettes chaque générateur a produites, donc une disproportion est **visible après coup** — ce qu'aucune des vingt-et-une ne permettait. Mais rien ne la mesure et rien n'agit dessus. J'ai rendu le symptôme lisible, pas le défaut corrigible.

## Ce qui manque encore, que ni les vingt-et-une ni la mienne ne traitent

**Rien ne vérifie un brief avant qu'il ne parte.** C'est le trou le plus important du jeu de fonctions, et il est exactement sous le mécanisme central. `ISOLER_LES_EVALUATIONS` *exige* la non-contamination et `REDIGER_BRIEF_AGENT` dit « rien qui oriente » — mais aucune fonction ne relit un brief pour y chercher ce qui oriente : un ordre de présentation, un adjectif, un fait présenté avec sa conclusion, la trace d'une proposition rivale. Quand les propositions, les attaques et l'arbitre sortent du même modèle, le **contenu du brief est la seule garantie réelle du principe 3**, et c'est le seul artefact du système qu'aucun contrôle ne touche. Une fonction `CONTROLER_BRIEF_AVANT_ENVOI` serait l'ajout le moins cher et le plus rentable du jeu entier.

**Le template du plan n'a pas de fonction de lecture.** Il existe `LIRE_TECHNIQUES_AUTORISEES` pour la configuration ; il n'existe rien pour le format, alors que le principe 10 en fait une entrée obligatoire. Pire, la définition de `REDIGER_PLAN` — « écrire les étapes, leurs attendus, leurs retours arrière, les autorisations, les branches » — impose une liste fixe qui met le retour arrière, les autorisations et les branches au même rang que les étapes, ce que le principe 7 refuse et ce que le principe 10 lui retire le droit de décider. Le jeu de fonctions se contredit là, et aucun contrôle final ne vérifie la conformité au template : `CONTROLER_INTEGRITE_DOCUMENT` vérifie qu'il ne se contredit pas, `CONTROLER_CONTENU_FINAL` vérifie quatre propriétés, aucun des deux ne vérifie la forme.

**Le socle inter-passes n'est pas outillé.** `AMORCER_DEPUIS_PLAN_EXISTANT` dérive le besoin du plan source, mais le fichier de traçabilité de la passe précédente — qui contient chaque fait établi avec sa provenance et ses limites, c'est-à-dire tout ce qui coûte cher — n'a aucune fonction qui l'ingère. Je le fais à la main avec `REUTILISER_ACQUIS` et `JUGER_PEREMPTION_FAIT`, et ça marche, mais rien ne nomme l'objet ni n'oblige à aller le chercher. C'est le prix, accepté par ailleurs, de la décision de ne pas traquer les retraits silencieux : le retravail multi-passes a une porte d'entrée et pas de mémoire outillée.

**Le « je ne sais pas » de l'utilisateur n'a pas de fonction.** Il est acquis qu'on lui explique simplement de quoi il s'agit. Aucune des 130 ne décrit cet acte : `FORMULER_QUESTION_ACTIONNABLE` rend une question tranchable, `PRESENTER_ALTERNATIVES_AU_CHOIX` juxtapose deux options, `QUALIFIER_PORTEE_DECISION` dit ce qui change si la réponse est fausse — je compose les trois, et c'est une approximation. Expliquer n'est ni questionner ni présenter.

**La contre-épreuve du classement d'exécution n'a pas de primitive.** Le principe 14 exige que ce classement soit contrôlé par le système. Je l'ai construit avec quatre fonctions existantes et je crois le montage juste, mais le fait que le contrôle explicitement exigé par un principe ne repose sur aucune fonction dédiée est un signe : c'est là que le jeu de fonctions fait confiance là où il ne devrait pas.