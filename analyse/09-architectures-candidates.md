# Dix-huit architectures candidates

Chacune décrit, en pseudo-code, une façon d'enchaîner les fonctions unitaires du
système pour produire un plan. Elles ont été produites indépendamment, sans que
leurs auteurs se voient. Leur ordre ici est aléatoire et ne porte aucune
information : rien dans ce document n'indique d'où vient une architecture, ni
quelles architectures partagent une origine.

Certaines architectures factorisent des blocs réutilisables ; ces blocs sont
alors reproduits avec l'architecture qui les emploie, sous le titre
« Briques utilisées ».

---


# Architecture 01 — Pipeline à sas


**Principe en une phrase** : sept phases larges et strictement séquentielles (une par grande famille de préoccupation), chacune fermée par un contrôle de sortie, avec retours nommés vers la phase amont exactement responsable du défaut trouvé.

### Pseudo-code

```
PHASE 0 — CADRAGE
  LIRE_TECHNIQUES_AUTORISEES
  INVENTORIER_CAPACITES
  IDENTIFIER_DESTINATAIRE
  SEPARER_DEMANDE_ET_BESOIN
  CONTESTER_ENONCE_PROBLEME
  DETECTER_SOLUTION_IMPOSEE
  SI travail part d'un plan existant : AMORCER_DEPUIS_PLAN_EXISTANT
  DELIMITER_PERIMETRE
  RECENSER_CONTRAINTES_DURES
  RECENSER_OBLIGATIONS_FORMELLES
  RECENSER_PREFERENCES
  ORDONNER_OBJECTIFS_SANS_ECARTER
  SI DETECTER_CONFLIT_OBJECTIFS : SOUMETTRE_ARBITRAGE_UTILISATEUR
  TRAQUER_AJOUTS_SILENCIEUX
  BALAYER_EXIGENCES_TACITES → pour chaque exigence remontée :
      DECIDER_D_INTERROGER_UTILISATEUR ; FORMULER_QUESTION_ACTIONNABLE
  EXPOSER_EXTERNALITES_CERTAINES
  FORMULER_CIBLE_OBSERVABLE
  DEFINIR_CRITERES_ACCEPTATION
  QUALIFIER_FORME_TRAVAIL
  SI ce n'est pas un problème de planification : DECLINER_SI_PAS_DE_PLAN ; ARRÊT
  ETABLIR_ETAT_ACTUEL
  CHAINER_ETAT_ACTUEL_VERS_CIBLE
  VERIFIER_FIDELITE_CIBLE_BESOIN
  --- CONTRÔLE DE SORTIE 0 ---
  boucle_reformulation = 0
  TANT QUE VERIFIER_FIDELITE_CIBLE_BESOIN échoue ET boucle_reformulation < 2 :
      reformuler cible/périmètre ; boucle_reformulation += 1
  SI toujours en échec : SUSPENDRE_ENQUETE_ET_DEMANDER

PHASE 1 — ENQUÊTE
  RECENSER_INCONNUES
  POUR chaque inconnue : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION
  bloquantes = inconnues classées "construction"
  QUALIFIER_PORTEE_INCONNUE(bloquantes)
  ORDONNER_INCONNUES_SANS_ECARTER(bloquantes)
  DISTINGUER_INDETERMINE_ET_NON_CHERCHE(bloquantes)
  POUR chaque inconnue bloquante :
      CHOISIR_MOYEN_DE_LEVEE
      SELON le moyen :
        inspection/calcul → MENER_VERIFICATION
        action bornée     → LEVER_INCONNUE_PAR_ACTION_REVERSIBLE
        source externe    → CHERCHER_ANTECEDENTS
        agent séparé      → DECIDER_D_OUVRIR_UN_AGENT ; REDIGER_BRIEF_AGENT ;
                             BORNER_UN_AGENT
        question          → DECIDER_D_INTERROGER_UTILISATEUR ;
                             FORMULER_QUESTION_ACTIONNABLE ;
                             SUSPENDRE_ENQUETE_ET_DEMANDER
      SI réponse d'agent : INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
      CONSIGNER_PROVENANCE_FAIT ; ENONCER_LIMITES_FAIT
      SEPARER_OBSERVE_ET_SUPPOSE
      JUGER_PEREMPTION_FAIT → SI périssable : INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
  DETECTER_CONTRADICTION_ENTRE_SOURCES → SI conflit :
      DETECTER_ORIGINE_COMMUNE_SOURCES ; RESOUDRE_CONTRADICTION
  RENDRE_INCERTITUDE_VISIBLE
  VERIFIER_ADOSSEMENT_AFFIRMATIONS
  --- CONTRÔLE DE SORTIE 1 ---
  SI une inconnue révèle que le cadrage était faux :
      RETOUR → PHASE 0 (borné : 1 seul aller-retour ; au 2e, SUSPENDRE_ENQUETE_ET_DEMANDER)
  SI VERIFIER_ADOSSEMENT_AFFIRMATIONS échoue sur un fait :
      reprendre CHOISIR_MOYEN_DE_LEVEE avec un moyen plus coûteux pour ce fait seul

PHASE 2 — DÉCISION
  RECENSER_INVARIANTS
  ETABLIR_DEPENDANCES_ENTRE_DECISIONS
  POUR chaque décision, dans l'ordre de dépendance :
      PRODUIRE_OPTIONS_DISTINCTES ; GARANTIR_DIVERSITE_METHODE
      CHERCHER_APPROCHES_NON_ENVISAGEES
      EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
      ISOLER_LES_EVALUATIONS
      CHOISIR_ANGLES_ATTAQUE → POUR chaque option : ATTAQUER_UNE_OPTION
      ATTAQUER_TOUT_LE_CHAMP → SI tout échoue : CONSTATER_IMPOSSIBILITE
      ARBITRER_A_L_AVEUGLE
      ORIENTER_CHOIX
      SELON le résultat :
        fait manquant     → RETOUR → PHASE 1, ciblé sur ce fait
        préférence requise → PRESENTER_ALTERNATIVES_AU_CHOIX ;
                              SOUMETTRE_ARBITRAGE_UTILISATEUR
        vrai choix         → AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE
      DISTINGUER_CHOIX_ET_CONSEQUENCE
      QUALIFIER_PORTEE_DECISION ; NOMMER_FAIT_QUI_FERAIT_BASCULER
      CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_ETAT_RESOLUTION
      CONSERVER_OPTIONS_ECARTEES
  VERIFIER_COHERENCE_ENSEMBLE (niveau décisions)
  --- CONTRÔLE DE SORTIE 2 ---
  SI une décision reste "non résolu" sans acceptation explicite : boucler sur cette décision
  (borné : le nombre de décisions est fini, chaque aller-retour PHASE1↔PHASE2
   retire une inconnue précise et ne la rouvre jamais — REUTILISER_ACQUIS)

PHASE 3 — CONSTRUCTION
  DERIVER_ACTIONS_DEPUIS_DECISIONS
  ORDONNER_PAR_PREREQUIS
  IDENTIFIER_ETAPES_SIMULTANEES ; VERIFIER_SIMULTANEITE_POSSIBLE
  POUR chaque étape :
      DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE
      SI "mécanique" : CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
      DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC
      DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE
      QUALIFIER_TERRITOIRE
      RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
  CONSTRUIRE_BRANCHE_CONDITIONNELLE (pour chaque incertitude d'exécution absorbée)
  CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
  REUTILISER_ACQUIS
  SI plan trop gros : DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER
  REPERER_POINTS_ENGAGEMENT
  PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION
  PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE ; PROPOSER_MARGES
  VERIFIER_COUVERTURE_BLOQUANTS
  --- CONTRÔLE DE SORTIE 3 ---
  SI une dépendance entre décisions apparaît manquée à la construction :
      RETOUR → PHASE 2, sur les deux décisions concernées seulement

PHASE 4 — ASSURANCE
  RECENSER_RISQUES_PAR_ORIGINE
  POUR chaque risque : QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT ;
      QUALIFIER_REVERSIBILITE
  ANTICIPER_TIERS_REACTIF
  VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN (branches incluses)
  STATUER_SUR_RISQUE_RESIDUEL (pour chaque risque restant)
  RECENSER_DEPENDANCES_EXTERNES ; VERIFIER_FAISABILITE_PAR_EXECUTANT
  EVALUER_EXIGENCE_TACHE ; RESPECTER_CADRE_AUTORISE
  --- CONTRÔLE DE SORTIE 4 ---
  SI un chemin viole un invariant :
      RETOUR → PHASE 3 (chemin précis) ou → PHASE 2 (si la cause est une contrainte
      dure ignorée par une décision)

PHASE 5 — RÉDACTION & CONTRÔLE
  REDIGER_PLAN ; REDIGER_TRACABILITE_SEPAREE
  SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN ; PREVOIR_SUITE_EN_CAS_DE_SUCCES
  ELAGUER_LA_PROSE ; RENDRE_ACTIONNABLE_PAR_AGENT
  VERIFIER_COUVERTURE_OBJECTIFS
  VERIFIER_COHERENCE_ENSEMBLE (niveau document, à nouveau)
  CONTROLER_CONTENU_FINAL ; CONTROLER_INTEGRITE_DOCUMENT
  FAIRE_CONTROLER_PAR_UN_TIERS
  PLACER_ET_NOMMER_LE_FICHIER
  --- CONTRÔLE DE SORTIE 5 ---
  SELON ce que trouve le tiers :
      prose/incohérence locale → boucler dans la phase (max 2 passes)
      objectif non couvert / étape sans attendu → RETOUR → PHASE 3
      risque non traité        → RETOUR → PHASE 4
      cible infidèle au besoin → RETOUR → PHASE 0 (max 1 fois, sinon escalade)

PHASE 6 — LIVRAISON
  RESTITUER_EN_BREF
```

### Les boucles
- **Retour interne** (Phase 0, Phase 5) : bouclage court dans la phase même, borné à 2 passages avant escalade vers `SUSPENDRE_ENQUETE_ET_DEMANDER`.
- **Retour 1→0** (cadrage invalidé par un fait) : borné à 1 aller-retour.
- **Retour 2→1** (décision bloquée par un fait manquant) : ciblé sur l'inconnue précise, borné par le nombre fini d'inconnues bloquantes (chaque passage en retire une définitivement grâce à `REUTILISER_ACQUIS`).
- **Retour 3→2** (dépendance manquée) : borné par le nombre fini d'arêtes du graphe de décisions.
- **Retour 4→3 / 4→2** (invariant violé) : borné par le nombre fini de chemins du plan.
- **Retour 5→3 / 5→4 / 5→0** : chacun plafonné explicitement, avec un dernier recours vers l'utilisateur.
- **Terminaison** : chaque retour retire un défaut précis et fini (fait, arête, chemin), jamais rouvert une fois réglé ; un plafond global par cible de retour empêche toute boucle infinie.

### Fonctions appelées plusieurs fois
`CHOISIR_MOYEN_DE_LEVEE`, `MENER_VERIFICATION`, `CONSIGNER_PROVENANCE_FAIT` (une fois par inconnue) ; `PRODUIRE_OPTIONS_DISTINCTES`, `ATTAQUER_UNE_OPTION`, `ARBITRER_A_L_AVEUGLE`, `CONSIGNER_CE_QUI_A_TRANCHE` (une fois par décision) ; `DEFINIR_ATTENDU_OBSERVABLE`, `DEFINIR_RETOUR_ARRIERE` (une fois par étape) ; `VERIFIER_COHERENCE_ENSEMBLE` (à granularité croissante : décisions, puis document entier) ; `DECIDER_D_OUVRIR_UN_AGENT` / `REDIGER_BRIEF_AGENT` (une fois par inconnue nécessitant un agent).

### Ce qu'elle fait bien / mal
Elle est lisible, auditable, correspond au sens commun d'un pipeline à étapes. Elle est cependant grossière : un retour "Décision → Enquête" déclenché par une seule inconnue oblige à repasser conceptuellement par toute la porte de la phase, sans découpage plus fin ; elle traite tout le lot d'inconnues avant toute décision, ce qui est inefficace si le travail est très hétérogène ; et elle ne pousse pas l'audit de sa propre rigueur (elle utilise l'isolement et l'arbitrage à l'aveugle sans jamais vérifier `QUALIFIER_INDEPENDANCE_OBTENUE` ni `DETECTER_ERREURS_CORRELEES` — faiblesse assumée, corrigée par une autre approche).

### Fonctions laissées de côté
`PARALLELISER_ENQUETE` et `ARRETER_ORCHESTRATION` : l'architecture garde l'enquête mono-fil par choix, elle n'ouvre pas de flotte d'agents à arrêter. `QUALIFIER_INDEPENDANCE_OBTENUE`, `DETECTER_ERREURS_CORRELEES` : l'isolement et l'arbitrage à l'aveugle sont appliqués mais jamais audités eux-mêmes — un choix délibéré de simplicité, documenté comme faiblesse.

---

---


# Architecture 02 — Deux vagues et un filet de sécurité global

<details><summary>Briques utilisées</summary>

```
FONCTION CONFRONTATION(question, dossier):
    ISOLER_LES_EVALUATIONS()                      # verrouille le mode aveugle pour tout ce qui suit

    angles = CHOISIR_ANGLES_ATTAQUE(question)
    methodes = GARANTIR_DIVERSITE_METHODE(question) # oblige les propositions à différer par la méthode

    propositions = []
    POUR chaque méthode DANS methodes:
        brief = REDIGER_BRIEF_AGENT(dossier, question, méthode)   # rien qui oriente
        SI DECIDER_D_OUVRIR_UN_AGENT(brief) == vrai:
            BORNER_UN_AGENT(condition_arrêt)
            retour = <sous-agent traite brief>
            proposition = INTEGRER_RETOUR_AGENT(retour)
            REFUSER_AUTO_CONFIRMATION(proposition)     # l'agent l'affirme, ça ne le rend pas vrai
        SINON:
            proposition = PRODUIRE_OPTIONS_DISTINCTES(brief)
        EXIGER_HYPOTHESES_EXPLICITES(proposition)       # rejetée si elle comble une inconnue tacitement
        propositions.ajouter(proposition)

    # attaque : chaque option reçoit seulement action + faits, jamais la défense d'une autre
    POUR chaque p DANS propositions:
        ATTAQUER_UNE_OPTION(p, dossier)
        DEBUSQUER_HYPOTHESES_IMPORTEES(p)
    ATTAQUER_TOUT_LE_CHAMP(propositions, dossier)       # ce qui ferait échouer TOUTES les options

    # arbitrage aveugle
    indep = QUALIFIER_INDEPENDANCE_OBTENUE(propositions)
    SI DETECTER_ERREURS_CORRELEES(propositions):
        <dégrader la confiance d'un accord apparent entre propositions>
    verdict = ARBITRER_A_L_AVEUGLE(anonymiser(propositions), précédence_explicite)

    # mise en forme du verdict
    CONSIGNER_CE_QUI_A_TRANCHE(verdict)
    QUALIFIER_ETAT_RESOLUTION(verdict)                  # tranché / avec compromis / branché / en attente / invalide
    NOMMER_FAIT_QUI_FERAIT_BASCULER(verdict)
    CONSERVER_OPTIONS_ECARTEES(propositions - {verdict.retenu})
    SI verdict.retenu n'était proposé par aucune proposition initiale:
        RATTACHER_TOUTE_PIECE_A_SON_ORIGINE(verdict.retenu)

    RETOURNER verdict
```

### `CONSTITUER_DOSSIER_INITIAL(demande)` — construit les faits, jamais un verdict

```
FONCTION CONSTITUER_DOSSIER_INITIAL(demande_ou_plan_existant):
    LIRE_TECHNIQUES_AUTORISEES() ; INVENTORIER_CAPACITES() ; EVALUER_EXIGENCE_TACHE()
    IDENTIFIER_DESTINATAIRE()
    SI demande == plan_existant: AMORCER_DEPUIS_PLAN_EXISTANT()
    SINON: SEPARER_DEMANDE_ET_BESOIN(demande)
    DELIMITER_PERIMETRE() ; ETABLIR_ETAT_ACTUEL()
    FORMULER_CIBLE_OBSERVABLE() ; VERIFIER_FIDELITE_CIBLE_BESOIN()
    RECENSER_CONTRAINTES_DURES() ; RECENSER_INVARIANTS()
    RECENSER_OBLIGATIONS_FORMELLES() ; DESIGNER_AUTORITE_AUTORISATION()
    RECENSER_PREFERENCES() ; RECENSER_RESSOURCES_EXECUTION() ; RECENSER_DEPENDANCES_EXTERNES()
    BALAYER_EXIGENCES_TACITES() -> pour chaque exigence remontée : DECIDER_D_INTERROGER_UTILISATEUR + FORMULER_QUESTION_ACTIONNABLE
    TRAQUER_AJOUTS_SILENCIEUX() ; EXPOSER_EXTERNALITES_CERTAINES()
    CHERCHER_ANTECEDENTS() ; REUTILISER_ACQUIS()
    DETECTER_SOLUTION_IMPOSEE() ; DETECTER_CONFLIT_OBJECTIFS() -> SI conflit: ORDONNER_OBJECTIFS_SANS_ECARTER()
    QUALIFIER_FORME_TRAVAIL() ; QUALIFIER_TERRITOIRE()

    inconnues = RECENSER_INCONNUES()
    POUR chaque i DANS ORDONNER_INCONNUES_SANS_ECARTER(inconnues):
        nature = CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION(i)
        SI nature == "exécution":
            QUALIFIER_PORTEE_INCONNUE(i) ; laisser pour la mise en forme (branche conditionnelle)
            CONTINUER
        # inconnue de construction : à lever maintenant
        QUALIFIER_PORTEE_INCONNUE(i)
        SI DISTINGUER_INDETERMINE_ET_NON_CHERCHE(i) == "simplement pas cherché":
            moyen = CHOISIR_MOYEN_DE_LEVEE(i)
            SELON moyen:
              inspection/source/calcul/test -> MENER_VERIFICATION(i)
              action réversible bornée      -> LEVER_INCONNUE_PAR_ACTION_REVERSIBLE(i)
              question                      -> DECIDER_D_INTERROGER_UTILISATEUR(i) ; FORMULER_QUESTION_ACTIONNABLE(i)
                                                SUSPENDRE_ENQUETE_ET_DEMANDER(i) ; attendre la réponse
        SINON: SUSPENDRE_ENQUETE_ET_DEMANDER(i)   # vraiment indéterminable : remonter, pas insister

    POUR chaque fait établi:
        CONSIGNER_PROVENANCE_FAIT(fait) ; SEPARER_OBSERVE_ET_SUPPOSE(fait) ; ENONCER_LIMITES_FAIT(fait)
        SI JUGER_PEREMPTION_FAIT(fait) == "périssable":
            INSCRIRE_REVERIFICATION_FAIT_PERISSABLE(fait)   # placée juste avant l'étape qui en dépendra
        REFUSER_AUTO_CONFIRMATION(fait)

    SI DETECTER_CONTRADICTION_ENTRE_SOURCES(faits):
        SI DETECTER_ORIGINE_COMMUNE_SOURCES(...): <une seule source en réalité, pondérer en conséquence>
        RESOUDRE_CONTRADICTION(...)   # date / version / périmètre / définition, ou marquer contesté

    RENDRE_INCERTITUDE_VISIBLE()
    RETOURNER dossier
```

### `METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts, dossier)` — met en forme, puis vérifie avant d'émettre

```
FONCTION METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts_choix, dossier):
    actions = DERIVER_ACTIONS_DEPUIS_DECISIONS(verdicts_choix)
    ordre = ORDONNER_PAR_PREREQUIS(squelette, actions)
    ordre = AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE(ordre)   # départage à validité égale
    simultanées = IDENTIFIER_ETAPES_SIMULTANEES(ordre)
    POUR chaque paire simultanée: VERIFIER_SIMULTANEITE_POSSIBLE(paire)
    POUR chaque inconnue d'exécution laissée en dossier: CONSTRUIRE_BRANCHE_CONDITIONNELLE(inconnue)
    POUR chaque étape:
        DEFINIR_ATTENDU_OBSERVABLE(étape) ; DEFINIR_CRITERES_ACCEPTATION(étape) ; DEFINIR_SIGNAUX_ECHEC(étape)
        DEFINIR_RETOUR_ARRIERE(étape) ; EPROUVER_RETOUR_ARRIERE(étape)
        DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE(étape)
        SI "mécanique": CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE(étape)
    PLACER_POINTS_VERIFICATION(ordre) ; PLACER_POINTS_AUTORISATION(ordre) ; PLACER_JALONS_CONSTAT(ordre)
    RECENSER_RISQUES_PAR_ORIGINE() -> QUALIFIER_VRAISEMBLANCE_RISQUE() -> QUALIFIER_RAYON_IMPACT() -> STATUER_SUR_RISQUE_RESIDUEL()
    ANTICIPER_TIERS_REACTIF() ; QUALIFIER_REVERSIBILITE() ; REPERER_POINTS_ENGAGEMENT()
    PROPOSER_MARGES() ; PROPOSER_AFFECTATION() ; PROPOSER_CHIFFRAGE()   # jamais imposés
    PRESENTER_ALTERNATIVES_AU_CHOIX(points laissés à l'utilisateur)
    CONTROLER_TAILLE_DES_ETAPES() ; ELAGUER_ETAPES_INUTILES()
    SIGNALER_LES_LIMITES() ; ISOLER_LE_HORS_PLAN()
    VERIFIER_COUVERTURE_OBJECTIFS() ; VERIFIER_COUVERTURE_BLOQUANTS() ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN()
    VERIFIER_COHERENCE_ENSEMBLE() ; VERIFIER_FAISABILITE_PAR_EXECUTANT()
    RENDRE_ACTIONNABLE_PAR_AGENT() ; PREVOIR_SUITE_EN_CAS_DE_SUCCES()
    ELAGUER_LA_PROSE() ; VERIFIER_ADOSSEMENT_AFFIRMATIONS() ; RENDRE_INCERTITUDE_VISIBLE()

    plan = REDIGER_PLAN(ordre, actions, ...)

    TANT QUE vrai:                                         # boucle de vérification finale
        rapport = CONTROLER_CONTENU_FINAL(plan)
        rapport += CONTROLER_INTEGRITE_DOCUMENT(plan)
        rapport += FAIRE_CONTROLER_PAR_UN_TIERS(plan)
        SI rapport.vide: SORTIR
        <corriger localement le plan selon rapport>          # jamais une nouvelle confrontation
        SI <2 corrections déjà tentées>: STATUER_SUR_RISQUE_RESIDUEL(rapport.restant) ; SORTIR

    REDIGER_TRACABILITE_SEPAREE() ; PLACER_ET_NOMMER_LE_FICHIER(plan)
    RESTITUER_EN_BREF()
    RETOURNER plan
```

Ces trois briques couvrent, à elles seules, la quasi-totalité des 129 identifiants. Ce qui suit montre, pour chaque architecture, **comment on arrive à `CONFRONTATION`, dans quel ordre, ce qui la déclenche, et comment un verdict peut rouvrir ce qui précède** — c'est là qu'elles diffèrent réellement.

---

</details>


**Principe** : on investit tout l'effort d'enquête en amont (une vague unique), on tranche PROBLÈME puis STRUCTURE une seule fois chacun, on confronte *tous* les choix litigieux ensemble en une seule salve aveugle, puis un unique audit global décide s'il faut *tout* refaire une fois — jamais de réouverture chirurgicale, seulement un retraitement complet borné à une seule répétition.

### Pseudo-code

```
FONCTION PLANIFIER(demande):
    LIRE_TECHNIQUES_AUTORISEES() ; EVALUER_EXIGENCE_TACHE()
    SI DECLINER_SI_PAS_DE_PLAN(demande): RETOURNER

    # --- Vague 0 : enquête totale, front-loaded ---
    dossier = CONSTITUER_DOSSIER_INITIAL(demande)
    # spécificité : on pousse la levée d'inconnues au-delà du strict nécessaire au palier suivant,
    # pour qu'aucune confrontation future n'ait à revenir enquêter.
    POUR chaque inconnue restante non encore levée:
        SI QUALIFIER_PORTEE_INCONNUE(inconnue) == "large" OU probablement utile à STRUCTURE/CHOIX:
            CHOISIR_MOYEN_DE_LEVEE(inconnue) ; lever maintenant
        SINON:
            ORDONNER_INCONNUES_SANS_ECARTER(inconnue)   # listée, non levée, non écartée
    dossier_gelé = dossier   # instantané figé pour toute la suite

    tentative = 1
    RÉPÉTER:
        # --- Vague 1 : une confrontation PROBLEME, une confrontation STRUCTURE ---
        v_p = CONFRONTATION("problème", dossier_gelé)
        SI v_p.état == "invalide": CONSTATER_IMPOSSIBILITE() ; RETOURNER
        v_s = CONFRONTATION("structure", dossier_gelé + {v_p.retenu})
        squelette = v_s.retenu

        # --- Vague 2 : TOUS les choix litigieux, en une seule salve, aveugles entre eux ---
        points = ORIENTER_CHOIX(squelette)
        litigieux = [ p DANS points SI DISTINGUER_CHOIX_ET_CONSEQUENCE(p) == "vrai choix" ET p.nature == "vrai choix" ]
        POUR chaque p DANS points \ litigieux: <résoudre hors confrontation : fait manquant ou préférence>
        verdicts_choix = {}
        POUR chaque p DANS litigieux:            # salve : ISOLER_LES_EVALUATIONS garantit qu'un choix
            verdicts_choix[p] = CONFRONTATION(p, dossier_gelé + squelette)   # ne voit pas la résolution d'un autre

        plan_brut = METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts_choix, dossier_gelé)
        # ^ inclut déjà CONTROLER_CONTENU_FINAL / CONTROLER_INTEGRITE_DOCUMENT / FAIRE_CONTROLER_PAR_UN_TIERS
        #   mais ici on les traite comme LE seul filet de sécurité de l'architecture, pas comme une correction locale

        audit = <résultat des contrôles ci-dessus, agrégé>
        SI audit.rien_à_redire: RETOURNER plan_brut

        SI tentative == 2:
            SOUMETTRE_ARBITRAGE_UTILISATEUR(audit.désaccords_restants) ; RETOURNER plan_brut
        # un seul redo global autorisé : les constats de l'audit deviennent des faits nouveaux du dossier
        dossier_gelé += audit.faits_nouveaux
        REUTILISER_ACQUIS(dossier_gelé)   # ne redémontre pas ce que l'audit n'a pas remis en cause
        tentative = 2
        # on relance TOUT : problème, structure, choix — pas de reprise partielle
```

### 3. Les boucles

- **Boucle « deux vagues »** (la seule boucle de retour de cette architecture) : déclenchée uniquement par l'audit global final, jamais par un verdict individuel en cours de route. Remonte toujours jusqu'à la Vague 1 dans son ensemble (jamais une réouverture ciblée d'un seul nœud). Bornée *par construction* à `tentative == 2` : au deuxième échec, on n'essaie plus, on transfère la décision à l'utilisateur via `SOUMETTRE_ARBITRAGE_UTILISATEUR`.
- **Boucle de levée d'inconnues en Vague 0** : bornée par la liste finie d'inconnues et par `DISTINGUER_INDETERMINE_ET_NON_CHERCHE` (qui empêche de chercher indéfiniment une inconnue déclarée indéterminable).
- **Boucle de vérification finale** (à l'intérieur de `METTRE_EN_FORME_ET_CONTROLER`) : sert ici de *détecteur* qui alimente la boucle de retour, pas de correcteur local — dans cette architecture, on ne corrige jamais à la marge, on refait la vague.

### 4. Fonctions appelées plusieurs fois

`CONFRONTATION` (au moins 2 + N la première fois, jusqu'à deux fois ce total si redo) ; `CONTROLER_CONTENU_FINAL` / `CONTROLER_INTEGRITE_DOCUMENT` / `FAIRE_CONTROLER_PAR_UN_TIERS` / `VERIFIER_COHERENCE_ENSEMBLE` (une fois par tentative, donc au plus 2) ; `ORIENTER_CHOIX` et `DISTINGUER_CHOIX_ET_CONSEQUENCE` (une fois par tentative) ; `REUTILISER_ACQUIS` (au moment du redo, pour ne pas rejouer ce que l'audit n'a pas contesté) ; `CHOISIR_MOYEN_DE_LEVEE` / `MENER_VERIFICATION` (une fois par inconnue en Vague 0, et à nouveau si l'audit produit des faits nouveaux nécessitant vérification).

### 5. Forces / faiblesses

**Bien** : le nombre de passages est borné *a priori* à une constante (2), indépendamment de la taille du plan — la terminaison ne dépend d'aucun budget par nœud à calibrer ; l'enquête étant totalement front-loaded, les confrontations elles-mêmes sont rapides et n'ont jamais à interrompre leur raisonnement pour aller chercher un fait ; très facile à auditer (deux vagues au plus, chacune traçable intégralement).

**Mal** : coûteuse en cas d'échec — un seul choix litigieux mal évalué force à rejouer *tout* (problème, structure, et tous les autres choix), même ceux que l'audit n'a pas remis en cause, ce que `REUTILISER_ACQUIS` atténue sans l'éliminer ; la Vague 0 investit dans la levée d'inconnues qui ne serviront peut-être jamais (si PROBLÈME ou STRUCTURE prennent une direction qui les rend sans objet) ; moins réactive qu'une architecture qui pourrait corriger chirurgicalement un seul nœud.

---

---


# Architecture 03 — Colonne vertébrale contradictoire


**Principe en une phrase** : à chaque niveau (faits, options, plan entier), le contrôle de sortie n'est pas un auto-diagnostic mais une véritable tentative de casser ce qui vient d'être produit, menée par un regard isolé de celui qui l'a produit — les mêmes primitives d'attaque (`ATTAQUER_*`, `ISOLER_LES_EVALUATIONS`, `QUALIFIER_INDEPENDANCE_OBTENUE`) sont réemployées à trois grains croissants.

### Pseudo-code

```
PHASE 0 — CADRAGE CONTESTÉ
  LIRE_TECHNIQUES_AUTORISEES ; INVENTORIER_CAPACITES ; RECENSER_RESSOURCES_EXECUTION
  SEPARER_DEMANDE_ET_BESOIN ; CONTESTER_ENONCE_PROBLEME ; DETECTER_SOLUTION_IMPOSEE
  DELIMITER_PERIMETRE ; RECENSER_CONTRAINTES_DURES ; RECENSER_OBLIGATIONS_FORMELLES
  RECENSER_PREFERENCES
  ORDONNER_OBJECTIFS_SANS_ECARTER ; DETECTER_CONFLIT_OBJECTIFS ; TRAQUER_AJOUTS_SILENCIEUX
  BALAYER_EXIGENCES_TACITES ; EXPOSER_EXTERNALITES_CERTAINES
  FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
  ATTAQUER_TOUT_LE_CHAMP  — [grain 1/3] appliqué ici au cadrage lui-même : chercher ce
      qui ferait échouer TOUTE approche compte tenu du périmètre retenu, avant qu'aucune
      option n'existe
  SI ATTAQUER_TOUT_LE_CHAMP révèle un problème mal posé : CONSTATER_IMPOSSIBILITE ;
      → aller directement en PHASE 6 avec un constat d'impossibilité motivé
  VERIFIER_FIDELITE_CIBLE_BESOIN
  DECLINER_SI_PAS_DE_PLAN ; QUALIFIER_FORME_TRAVAIL
  ETABLIR_ETAT_ACTUEL ; CHAINER_ETAT_ACTUEL_VERS_CIBLE
  --- CONTRÔLE DE SORTIE 0 ---
  SI le cadrage ne survit pas à l'attaque : reformuler, boucler (max 2 fois),
      puis SUSPENDRE_ENQUETE_ET_DEMANDER

PHASE 1 — ENQUÊTE ADOSSÉE
  RECENSER_INCONNUES ; POUR chaque : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION
  QUALIFIER_PORTEE_INCONNUE ; ORDONNER_INCONNUES_SANS_ECARTER
  DISTINGUER_INDETERMINE_ET_NON_CHERCHE
  POUR chaque inconnue bloquante :
      CHOISIR_MOYEN_DE_LEVEE → MENER_VERIFICATION / LEVER_INCONNUE_PAR_ACTION_REVERSIBLE /
          CHERCHER_ANTECEDENTS
      SI fait pivot (porte une décision à fort impact) :
          DECIDER_D_OUVRIR_UN_AGENT ; REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT
          → puis une seconde levée indépendante :
          ISOLER_LES_EVALUATIONS (la 2e tentative ne voit pas le résultat de la 1re)
          DETECTER_ERREURS_CORRELEES (chemins de preuve vraiment distincts ?)
          QUALIFIER_INDEPENDANCE_OBTENUE
      INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION (systématique)
      CONSIGNER_PROVENANCE_FAIT ; ENONCER_LIMITES_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE
      JUGER_PEREMPTION_FAIT → INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
  DETECTER_CONTRADICTION_ENTRE_SOURCES → DETECTER_ORIGINE_COMMUNE_SOURCES →
      RESOUDRE_CONTRADICTION
  RENDRE_INCERTITUDE_VISIBLE ; VERIFIER_ADOSSEMENT_AFFIRMATIONS
  ARRETER_ORCHESTRATION
  DECIDER_D_INTERROGER_UTILISATEUR ; FORMULER_QUESTION_ACTIONNABLE ;
      SUSPENDRE_ENQUETE_ET_DEMANDER (pour l'irréductible)
  --- CONTRÔLE DE SORTIE 1 ---
  round = 0
  TANT QUE un fait pivot a une indépendance jugée faible ET round < 2 :
      relancer une levée par un moyen réellement distinct ; round += 1
  SI indépendance encore faible après 2 rounds :
      QUALIFIER_INDEPENDANCE_OBTENUE("faible, acceptée") — consigné, pas rejoué indéfiniment
  SI un fait contredit une prémisse du cadrage : RETOUR → PHASE 0 (borné à 1 fois)

PHASE 2 — OPTIONS ATTAQUÉES À L'AVEUGLE
  ETABLIR_DEPENDANCES_ENTRE_DECISIONS
  POUR chaque décision, dans l'ordre de dépendance :
      PRODUIRE_OPTIONS_DISTINCTES ; GARANTIR_DIVERSITE_METHODE
      CHERCHER_APPROCHES_NON_ENVISAGEES
      EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
      ISOLER_LES_EVALUATIONS (chaque option évaluée sans voir le plaidoyer des autres)
      CHOISIR_ANGLES_ATTAQUE
      POUR chaque option : ATTAQUER_UNE_OPTION  (reçoit seulement action + faits, jamais
          le plaidoyer)
      ATTAQUER_TOUT_LE_CHAMP  — [grain 2/3] sur le champ d'options de CETTE décision
      SI tout échoue : CONSTATER_IMPOSSIBILITE
      ARBITRER_A_L_AVEUGLE (options anonymisées, précédence explicite, jamais au nombre
          de voix)
      QUALIFIER_INDEPENDANCE_OBTENUE ; DETECTER_ERREURS_CORRELEES (l'attaque et la
          défense partageaient-elles une même source ?)
      SI contamination détectée :
          RETOUR interne : refaire ISOLER_LES_EVALUATIONS + ATTAQUER_UNE_OPTION avec un
          moyen réellement séparé (borné à 2 reprises pour cette décision, puis
          QUALIFIER_INDEPENDANCE_OBTENUE("faible, acceptée") + SOUMETTRE_ARBITRAGE_UTILISATEUR)
      ORIENTER_CHOIX → PRESENTER_ALTERNATIVES_AU_CHOIX / SOUMETTRE_ARBITRAGE_UTILISATEUR /
          DECIDER_D_INTERROGER_UTILISATEUR selon le cas
      AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE ; DISTINGUER_CHOIX_ET_CONSEQUENCE
      QUALIFIER_PORTEE_DECISION ; NOMMER_FAIT_QUI_FERAIT_BASCULER
      CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_ETAT_RESOLUTION ; CONSERVER_OPTIONS_ECARTEES
  --- CONTRÔLE DE SORTIE 2 ---
  SI une option n'est invalidée que par un fait non vérifié :
      RETOUR → PHASE 1, ciblé sur ce fait seul

PHASE 3 — CONSTRUCTION
  DERIVER_ACTIONS_DEPUIS_DECISIONS ; ORDONNER_PAR_PREREQUIS
  IDENTIFIER_ETAPES_SIMULTANEES ; VERIFIER_SIMULTANEITE_POSSIBLE
  DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE ; CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
  CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
  DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC
  DEFINIR_RETOUR_ARRIERE → EPROUVER_RETOUR_ARRIERE (traité comme une attaque : un retour
      arrière seulement affirmé, jamais exercé, fait échouer le contrôle)
  CONSTRUIRE_BRANCHE_CONDITIONNELLE ; QUALIFIER_TERRITOIRE
  SI trop gros : DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER
  REUTILISER_ACQUIS ; RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
  REPERER_POINTS_ENGAGEMENT
  PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION
  PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE ; PROPOSER_MARGES
  VERIFIER_COUVERTURE_BLOQUANTS
  --- CONTRÔLE DE SORTIE 3 ---
  SI une décision "tranchée" ne se traduit pas en actions bornées : RETOUR → PHASE 2

PHASE 4 — ASSURANCE
  RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT ;
      QUALIFIER_REVERSIBILITE ; ANTICIPER_TIERS_REACTIF
  RECENSER_INVARIANTS ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN
  ATTAQUER_TOUT_LE_CHAMP  — [grain 3/3] appliqué cette fois aux combinaisons de branches
      du plan construit : une combinaison ouvre-t-elle un chemin qui viole une contrainte
      dure recensée en phase 0 ?
  STATUER_SUR_RISQUE_RESIDUEL ; PROPOSER_MARGES
  RECENSER_DEPENDANCES_EXTERNES ; VERIFIER_FAISABILITE_PAR_EXECUTANT
  EVALUER_EXIGENCE_TACHE ; RESPECTER_CADRE_AUTORISE
  --- CONTRÔLE DE SORTIE 4 ---
  SI violation : RETOUR → PHASE 3 (branche visée) ou → PHASE 2 (si la cause est
      une décision incompatible avec une contrainte dure)

PHASE 5 — CONTRE-LECTURE TIERCE
  REDIGER_PLAN ; REDIGER_TRACABILITE_SEPAREE ; SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN
  PREVOIR_SUITE_EN_CAS_DE_SUCCES ; ELAGUER_LA_PROSE ; RENDRE_ACTIONNABLE_PAR_AGENT
  VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_COHERENCE_ENSEMBLE
  CONTROLER_CONTENU_FINAL ; CONTROLER_INTEGRITE_DOCUMENT
  BORNER_UN_AGENT ; REDIGER_BRIEF_AGENT (le tiers reçoit le plan et les critères,
      jamais le raisonnement qui y a mené)
  FAIRE_CONTROLER_PAR_UN_TIERS — traité comme une dernière attaque : le plan entier est
      "l'option" à casser
  INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
  DETECTER_ERREURS_CORRELEES (le tiers a-t-il vraiment un regard neuf, ou les mêmes
      angles morts que l'auteur ?) ; QUALIFIER_INDEPENDANCE_OBTENUE
  PLACER_ET_NOMMER_LE_FICHIER
  --- CONTRÔLE DE SORTIE 5 ---
  SI finding : corriger, relancer FAIRE_CONTROLER_PAR_UN_TIERS UNE fois de plus max
  SI un même type de finding réapparaît une 2e fois : ne pas reboucler — SIGNALER_LES_LIMITES
      (consigner la faiblesse survivante comme limite assumée) puis avancer
  SELON la nature du finding non résolu par correction : RETOUR ciblé vers
      PHASE 3 / PHASE 4 / PHASE 2 / PHASE 0 comme précédemment

PHASE 6 — LIVRAISON
  RESTITUER_EN_BREF
```

### Les boucles
- **Boucles de rattrapage classiques** (1→0, 2→1, 3→2, 4→3/2, 5→*) : même logique de ciblage et de terminaison monotone que dans A/B.
- **Boucles d'audit d'indépendance** (Phase 1 sur les faits pivots, Phase 2 sur l'arbitrage, Phase 5 sur le tiers) : explicitement **plafonnées en nombre de rounds** (2, 2, 1) — spécificité de cette architecture. Une primitive d'attaque, contrairement à une case de checklist, peut toujours trouver quelque chose si on la laisse chercher indéfiniment ; le plafond est donc une pièce architecturale obligatoire, absente d'A et B. Au-delà du plafond, le défaut n'est pas rejoué : il est converti en résidu documenté (`QUALIFIER_INDEPENDANCE_OBTENUE("faible, acceptée")`, `SIGNALER_LES_LIMITES`, `STATUER_SUR_RISQUE_RESIDUEL`).
- **Terminaison** : combinaison de l'argument monotone (défauts finis, retirés un par un) et du plafond explicite de rounds adversariaux.

### Fonctions appelées plusieurs fois
`ATTAQUER_TOUT_LE_CHAMP` : trois fois, à trois grains différents (le cadrage, le champ d'options d'une décision, les combinaisons de branches du plan) — signature de cette architecture. `ATTAQUER_UNE_OPTION` : une fois par option par décision. `ISOLER_LES_EVALUATIONS` / `QUALIFIER_INDEPENDANCE_OBTENUE` / `DETECTER_ERREURS_CORRELEES` : à trois étages distincts (fait, option, document) avec les mêmes primitives. `REFUSER_AUTO_CONFIRMATION` / `INTEGRER_RETOUR_AGENT` : à chaque retour d'agent, quel qu'il soit. `DECIDER_D_OUVRIR_UN_AGENT` / `REDIGER_BRIEF_AGENT` / `BORNER_UN_AGENT` : pour chaque investigation indépendante et pour la contre-lecture tierce.

### Ce qu'elle fait bien / mal
Elle est la plus résistante à l'auto-persuasion : rien n'avance sur la seule foi de celui qui l'a produit, à tous les étages — c'est sa propriété la plus solide, et elle détecte des défauts que A et B (plus déclaratives, un contrôle qui coche ses propres cases) peuvent laisser passer, notamment la contamination entre évaluations censées indépendantes. En contrepartie, c'est la plus coûteuse en agents ouverts et en appels (chaque investigation pivot est doublée) ; et son risque propre est que l'attaque ne soit jamais satisfaite — d'où la nécessité du plafond de rounds, une pièce que A et B n'ont pas à porter. Sur un travail simple et à faible enjeu (que `QUALIFIER_FORME_TRAVAIL` / `EVALUER_EXIGENCE_TACHE` signaleraient dès la phase 0), cette architecture est en sur-qualité.

### Fonctions laissées de côté
`AMORCER_DEPUIS_PLAN_EXISTANT` : même raison qu'en B, entrée par demande fraîche uniquement. `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` : utilisé mais volontairement secondaire — cette architecture ne s'organise pas par découpage/fusion de sous-plans comme B, mais par étages d'épreuve contradictoire ; le concept de "vague rouverte" de B n'existe pas ici, remplacé par les plafonds de rounds.

---


# Architecture 04 — Agenda piloté par un graphe de dépendances

<details><summary>Briques utilisées</summary>

```
FONCTION CONFRONTATION(question, dossier):
    ISOLER_LES_EVALUATIONS()                      # verrouille le mode aveugle pour tout ce qui suit

    angles = CHOISIR_ANGLES_ATTAQUE(question)
    methodes = GARANTIR_DIVERSITE_METHODE(question) # oblige les propositions à différer par la méthode

    propositions = []
    POUR chaque méthode DANS methodes:
        brief = REDIGER_BRIEF_AGENT(dossier, question, méthode)   # rien qui oriente
        SI DECIDER_D_OUVRIR_UN_AGENT(brief) == vrai:
            BORNER_UN_AGENT(condition_arrêt)
            retour = <sous-agent traite brief>
            proposition = INTEGRER_RETOUR_AGENT(retour)
            REFUSER_AUTO_CONFIRMATION(proposition)     # l'agent l'affirme, ça ne le rend pas vrai
        SINON:
            proposition = PRODUIRE_OPTIONS_DISTINCTES(brief)
        EXIGER_HYPOTHESES_EXPLICITES(proposition)       # rejetée si elle comble une inconnue tacitement
        propositions.ajouter(proposition)

    # attaque : chaque option reçoit seulement action + faits, jamais la défense d'une autre
    POUR chaque p DANS propositions:
        ATTAQUER_UNE_OPTION(p, dossier)
        DEBUSQUER_HYPOTHESES_IMPORTEES(p)
    ATTAQUER_TOUT_LE_CHAMP(propositions, dossier)       # ce qui ferait échouer TOUTES les options

    # arbitrage aveugle
    indep = QUALIFIER_INDEPENDANCE_OBTENUE(propositions)
    SI DETECTER_ERREURS_CORRELEES(propositions):
        <dégrader la confiance d'un accord apparent entre propositions>
    verdict = ARBITRER_A_L_AVEUGLE(anonymiser(propositions), précédence_explicite)

    # mise en forme du verdict
    CONSIGNER_CE_QUI_A_TRANCHE(verdict)
    QUALIFIER_ETAT_RESOLUTION(verdict)                  # tranché / avec compromis / branché / en attente / invalide
    NOMMER_FAIT_QUI_FERAIT_BASCULER(verdict)
    CONSERVER_OPTIONS_ECARTEES(propositions - {verdict.retenu})
    SI verdict.retenu n'était proposé par aucune proposition initiale:
        RATTACHER_TOUTE_PIECE_A_SON_ORIGINE(verdict.retenu)

    RETOURNER verdict
```

### `CONSTITUER_DOSSIER_INITIAL(demande)` — construit les faits, jamais un verdict

```
FONCTION CONSTITUER_DOSSIER_INITIAL(demande_ou_plan_existant):
    LIRE_TECHNIQUES_AUTORISEES() ; INVENTORIER_CAPACITES() ; EVALUER_EXIGENCE_TACHE()
    IDENTIFIER_DESTINATAIRE()
    SI demande == plan_existant: AMORCER_DEPUIS_PLAN_EXISTANT()
    SINON: SEPARER_DEMANDE_ET_BESOIN(demande)
    DELIMITER_PERIMETRE() ; ETABLIR_ETAT_ACTUEL()
    FORMULER_CIBLE_OBSERVABLE() ; VERIFIER_FIDELITE_CIBLE_BESOIN()
    RECENSER_CONTRAINTES_DURES() ; RECENSER_INVARIANTS()
    RECENSER_OBLIGATIONS_FORMELLES() ; DESIGNER_AUTORITE_AUTORISATION()
    RECENSER_PREFERENCES() ; RECENSER_RESSOURCES_EXECUTION() ; RECENSER_DEPENDANCES_EXTERNES()
    BALAYER_EXIGENCES_TACITES() -> pour chaque exigence remontée : DECIDER_D_INTERROGER_UTILISATEUR + FORMULER_QUESTION_ACTIONNABLE
    TRAQUER_AJOUTS_SILENCIEUX() ; EXPOSER_EXTERNALITES_CERTAINES()
    CHERCHER_ANTECEDENTS() ; REUTILISER_ACQUIS()
    DETECTER_SOLUTION_IMPOSEE() ; DETECTER_CONFLIT_OBJECTIFS() -> SI conflit: ORDONNER_OBJECTIFS_SANS_ECARTER()
    QUALIFIER_FORME_TRAVAIL() ; QUALIFIER_TERRITOIRE()

    inconnues = RECENSER_INCONNUES()
    POUR chaque i DANS ORDONNER_INCONNUES_SANS_ECARTER(inconnues):
        nature = CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION(i)
        SI nature == "exécution":
            QUALIFIER_PORTEE_INCONNUE(i) ; laisser pour la mise en forme (branche conditionnelle)
            CONTINUER
        # inconnue de construction : à lever maintenant
        QUALIFIER_PORTEE_INCONNUE(i)
        SI DISTINGUER_INDETERMINE_ET_NON_CHERCHE(i) == "simplement pas cherché":
            moyen = CHOISIR_MOYEN_DE_LEVEE(i)
            SELON moyen:
              inspection/source/calcul/test -> MENER_VERIFICATION(i)
              action réversible bornée      -> LEVER_INCONNUE_PAR_ACTION_REVERSIBLE(i)
              question                      -> DECIDER_D_INTERROGER_UTILISATEUR(i) ; FORMULER_QUESTION_ACTIONNABLE(i)
                                                SUSPENDRE_ENQUETE_ET_DEMANDER(i) ; attendre la réponse
        SINON: SUSPENDRE_ENQUETE_ET_DEMANDER(i)   # vraiment indéterminable : remonter, pas insister

    POUR chaque fait établi:
        CONSIGNER_PROVENANCE_FAIT(fait) ; SEPARER_OBSERVE_ET_SUPPOSE(fait) ; ENONCER_LIMITES_FAIT(fait)
        SI JUGER_PEREMPTION_FAIT(fait) == "périssable":
            INSCRIRE_REVERIFICATION_FAIT_PERISSABLE(fait)   # placée juste avant l'étape qui en dépendra
        REFUSER_AUTO_CONFIRMATION(fait)

    SI DETECTER_CONTRADICTION_ENTRE_SOURCES(faits):
        SI DETECTER_ORIGINE_COMMUNE_SOURCES(...): <une seule source en réalité, pondérer en conséquence>
        RESOUDRE_CONTRADICTION(...)   # date / version / périmètre / définition, ou marquer contesté

    RENDRE_INCERTITUDE_VISIBLE()
    RETOURNER dossier
```

### `METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts, dossier)` — met en forme, puis vérifie avant d'émettre

```
FONCTION METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts_choix, dossier):
    actions = DERIVER_ACTIONS_DEPUIS_DECISIONS(verdicts_choix)
    ordre = ORDONNER_PAR_PREREQUIS(squelette, actions)
    ordre = AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE(ordre)   # départage à validité égale
    simultanées = IDENTIFIER_ETAPES_SIMULTANEES(ordre)
    POUR chaque paire simultanée: VERIFIER_SIMULTANEITE_POSSIBLE(paire)
    POUR chaque inconnue d'exécution laissée en dossier: CONSTRUIRE_BRANCHE_CONDITIONNELLE(inconnue)
    POUR chaque étape:
        DEFINIR_ATTENDU_OBSERVABLE(étape) ; DEFINIR_CRITERES_ACCEPTATION(étape) ; DEFINIR_SIGNAUX_ECHEC(étape)
        DEFINIR_RETOUR_ARRIERE(étape) ; EPROUVER_RETOUR_ARRIERE(étape)
        DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE(étape)
        SI "mécanique": CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE(étape)
    PLACER_POINTS_VERIFICATION(ordre) ; PLACER_POINTS_AUTORISATION(ordre) ; PLACER_JALONS_CONSTAT(ordre)
    RECENSER_RISQUES_PAR_ORIGINE() -> QUALIFIER_VRAISEMBLANCE_RISQUE() -> QUALIFIER_RAYON_IMPACT() -> STATUER_SUR_RISQUE_RESIDUEL()
    ANTICIPER_TIERS_REACTIF() ; QUALIFIER_REVERSIBILITE() ; REPERER_POINTS_ENGAGEMENT()
    PROPOSER_MARGES() ; PROPOSER_AFFECTATION() ; PROPOSER_CHIFFRAGE()   # jamais imposés
    PRESENTER_ALTERNATIVES_AU_CHOIX(points laissés à l'utilisateur)
    CONTROLER_TAILLE_DES_ETAPES() ; ELAGUER_ETAPES_INUTILES()
    SIGNALER_LES_LIMITES() ; ISOLER_LE_HORS_PLAN()
    VERIFIER_COUVERTURE_OBJECTIFS() ; VERIFIER_COUVERTURE_BLOQUANTS() ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN()
    VERIFIER_COHERENCE_ENSEMBLE() ; VERIFIER_FAISABILITE_PAR_EXECUTANT()
    RENDRE_ACTIONNABLE_PAR_AGENT() ; PREVOIR_SUITE_EN_CAS_DE_SUCCES()
    ELAGUER_LA_PROSE() ; VERIFIER_ADOSSEMENT_AFFIRMATIONS() ; RENDRE_INCERTITUDE_VISIBLE()

    plan = REDIGER_PLAN(ordre, actions, ...)

    TANT QUE vrai:                                         # boucle de vérification finale
        rapport = CONTROLER_CONTENU_FINAL(plan)
        rapport += CONTROLER_INTEGRITE_DOCUMENT(plan)
        rapport += FAIRE_CONTROLER_PAR_UN_TIERS(plan)
        SI rapport.vide: SORTIR
        <corriger localement le plan selon rapport>          # jamais une nouvelle confrontation
        SI <2 corrections déjà tentées>: STATUER_SUR_RISQUE_RESIDUEL(rapport.restant) ; SORTIR

    REDIGER_TRACABILITE_SEPAREE() ; PLACER_ET_NOMMER_LE_FICHIER(plan)
    RESTITUER_EN_BREF()
    RETOURNER plan
```

Ces trois briques couvrent, à elles seules, la quasi-totalité des 129 identifiants. Ce qui suit montre, pour chaque architecture, **comment on arrive à `CONFRONTATION`, dans quel ordre, ce qui la déclenche, et comment un verdict peut rouvrir ce qui précède** — c'est là qu'elles diffèrent réellement.

---

</details>


**Principe** : pas de paliers fixes — un graphe de points à trancher (1 nœud PROBLÈME, 1 nœud STRUCTURE, N nœuds CHOIX découverts au fil de l'eau) est traité par un agenda à priorité ; les confrontations indépendantes tournent en parallèle via des sous-agents ; un verdict invalide *exactement* les nœuds qui dépendaient du fait qu'il remet en cause, propagation dans les deux sens (amont et aval), jusqu'à un point fixe.

### Pseudo-code

```
FONCTION PLANIFIER(demande):
    LIRE_TECHNIQUES_AUTORISEES() ; EVALUER_EXIGENCE_TACHE()
    SI DECLINER_SI_PAS_DE_PLAN(demande): RETOURNER

    dossier = CONSTITUER_DOSSIER_INITIAL(demande)   # volontairement minimal : juste assez pour ouvrir PROBLEME
    graphe = {}  ; agenda = FILE_A_PRIORITE()
    graphe.ajouter(PROBLEME) ; agenda.empiler(PROBLEME)
    faits_ayant_déjà_rouvert = {}                     # mémo (nœud, fait) -> empêche le rebouclage infini

    TANT QUE agenda non vide:
        n = agenda.dépiler_le_plus_prêt(critère = ETABLIR_DEPENDANCES_ENTRE_DECISIONS)

        SI n.dossier_local_insuffisant:
            manques = RECENSER_INCONNUES(n)
            domaines = <regrouper manques par domaine séparable>
            SI len(domaines) > 1 ET RESPECTER_CADRE_AUTORISE("parallélisation"):
                PARALLELISER_ENQUETE(domaines)
                POUR chaque domaine: DECIDER_D_OUVRIR_UN_AGENT(...) ; BORNER_UN_AGENT(...) ; REDIGER_BRIEF_AGENT(...)
                POUR chaque retour: INTEGRER_RETOUR_AGENT(retour) ; REFUSER_AUTO_CONFIRMATION(retour)
                ARRETER_ORCHESTRATION()               # constat : un agent de plus ne changerait rien
            SINON:
                POUR chaque manque: CHOISIR_MOYEN_DE_LEVEE(manque) ; MENER_VERIFICATION/LEVER_INCONNUE_PAR_ACTION_REVERSIBLE/question
            agenda.remettre(n) ; CONTINUER

        v = CONFRONTATION(n.question, n.dossier_local)
        n.verdict = v

        SI n == PROBLEME:
            SI v.état == "invalide": CONSTATER_IMPOSSIBILITE() ; RETOURNER
            graphe.ajouter(STRUCTURE, dépend_de = PROBLEME) ; agenda.empiler(STRUCTURE)

        SI n == STRUCTURE:
            POUR chaque p DANS ORIENTER_CHOIX(v.retenu):
                SI DISTINGUER_CHOIX_ET_CONSEQUENCE(p) == "conséquence mécanique": CONTINUER
                SI p.nature != "vrai choix": <résoudre hors confrontation> ; CONTINUER
                graphe.ajouter(CHOIX[p], dépend_de = ETABLIR_DEPENDANCES_ENTRE_DECISIONS(p, points_déjà_graphés))
                agenda.empiler(CHOIX[p])              # les CHOIX indépendants sortent ensemble -> confrontations en parallèle

        # --- propagation d'invalidation, fixpoint ---
        fait = NOMMER_FAIT_QUI_FERAIT_BASCULER(v)
        SI fait est réellement nouveau (absent du dossier au moment où d'autres nœuds ont été tranchés):
            POUR chaque nœud m (amont ou aval) dont le dossier dépendait de fait:
                SI (m, fait) DANS faits_ayant_déjà_rouvert:
                    SOUMETTRE_ARBITRAGE_UTILISATEUR(m, fait) ; CONTINUER   # pas de deuxième réouverture, même motif
                faits_ayant_déjà_rouvert.ajouter((m, fait))
                REUTILISER_ACQUIS(m.dossier)          # tout ce qui ne dépend pas de `fait` reste acquis
                m.dossier += fait ; agenda.empiler(m)

    # agenda vide = point fixe atteint : plus aucune invalidation en attente
    squelette = graphe[STRUCTURE].verdict.retenu
    verdicts_choix = { p: graphe[CHOIX[p]].verdict pour p DANS points litigieux }
    plan = METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts_choix, dossier)
```

### 3. Les boucles

- **Boucle d'enrichissement local** (dossier insuffisant → lever → réempiler) : bornée car les inconnues sont en nombre fini et `DISTINGUER_INDETERMINE_ET_NON_CHERCHE` force à déclarer une inconnue vraiment indéterminable plutôt que de la relever indéfiniment.
- **Boucle de propagation** (un verdict rouvre des nœuds amont/aval) : c'est la boucle de retour de cette architecture — elle peut remonter *jusqu'au PROBLÈME* depuis n'importe quel CHOIX, contrairement à une approche purement séquentielle qui ne remonte que d'un cran. Terminaison : le mémo `(nœud, fait)` interdit qu'un même motif rouvre deux fois le même nœud ; comme l'ensemble des faits est fini, le nombre total de réouvertures est fini.
- **Boucle principale de l'agenda** : se termine quand elle est vide — c'est-à-dire quand plus aucun nœud n'est ni à enrichir, ni à trancher, ni à rouvrir : un vrai point fixe, pas un budget arbitraire.

### 4. Fonctions appelées plusieurs fois

`CONFRONTATION` (une fois par nœud, potentiellement rejouée après réouverture) ; `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` (à chaque priorisation d'agenda *et* à chaque insertion d'un nouveau nœud CHOIX) ; `DECIDER_D_OUVRIR_UN_AGENT` / `BORNER_UN_AGENT` / `REDIGER_BRIEF_AGENT` / `INTEGRER_RETOUR_AGENT` (une fois par domaine parallèle, potentiellement nombreuses fois) ; `REUTILISER_ACQUIS` (à chaque réouverture partielle, pour isoler ce qui ne dépend pas du fait invalidant) ; `NOMMER_FAIT_QUI_FERAIT_BASCULER` (à chaque verdict, sert de déclencheur de propagation).

### 5. Forces / faiblesses

**Bien** : la plus fidèle à la réalité du problème — rien n'oblige la structure à être figée avant que certains choix indépendants d'elle soient instruits ; la parallélisation est native et directement rattachée aux fonctions d'orchestration d'agents ; la règle « même motif ne rouvre pas deux fois » est un critère de terminaison honnête (fondé sur les faits, pas sur un chiffre arbitraire).

**Mal** : la plus complexe à implémenter et à auditer (il faut maintenir un graphe, un mémo de réouverture, un ordonnanceur) ; le risque de "chatter" est réel si `NOMMER_FAIT_QUI_FERAIT_BASCULER` est mal calibré (des faits presque-nouveaux qui rouvrent en cascade) ; moins lisible a posteriori qu'une cascade linéaire pour quelqu'un qui relit le déroulé.

---

---


# Architecture 05 — La file de travail pilotée par les dépendances


**Principe en une phrase :** il n'y a pas de phases fixes ; une seule file de priorité contient tous les items ouverts (inconnues, exigences tacites à vérifier, décisions), et l'on traite à chaque tour l'item de plus fort impact, la résolution d'un item débloquant et repoussant dans la file les items qui en dépendaient — le plan émerge de l'épuisement de la file, pas d'un enchaînement de blocs.

### Pseudo-code

```
INITIALISATION
  LIRE_TECHNIQUES_AUTORISEES ; EVALUER_EXIGENCE_TACHE
  INVENTORIER_CAPACITES ; IDENTIFIER_DESTINATAIRE
  QUALIFIER_FORME_TRAVAIL ; SI non pertinent ALORS DECLINER_SI_PAS_DE_PLAN ; ARRÊT
  SI plan existant ALORS AMORCER_DEPUIS_PLAN_EXISTANT
  SEPARER_DEMANDE_ET_BESOIN ; DELIMITER_PERIMETRE
  FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
  ETABLIR_ETAT_ACTUEL ; QUALIFIER_TERRITOIRE ; CHAINER_ETAT_ACTUEL_VERS_CIBLE
  RECENSER_CONTRAINTES_DURES ; RECENSER_OBLIGATIONS_FORMELLES ; EXPOSER_EXTERNALITES_CERTAINES
  ORDONNER_OBJECTIFS_SANS_ECARTER
  SI DETECTER_CONFLIT_OBJECTIFS ALORS SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE

  FILE := file de priorité, vide
  RECENSER_INCONNUES → pour chacune : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION,
                        QUALIFIER_PORTEE_INCONNUE → empiler dans FILE si bloquante-construction
  BALAYER_EXIGENCES_TACITES → empiler chaque dimension comme item "exigence à vérifier"
  ETABLIR_DEPENDANCES_ENTRE_DECISIONS → empiler dans FILE les décisions sans prérequis ouvert
  compteurs_rebond[item] := 0 pour chaque item

BOUCLE PRINCIPALE
  TANT QUE FILE non vide :
    ORDONNER_INCONNUES_SANS_ECARTER / QUALIFIER_PORTEE_DECISION → re-classer FILE
    item := extraire le plus prioritaire (impact × 1/coût de résolution)

    SI compteurs_rebond[item] > 4 ALORS
      CONSTATER_IMPOSSIBILITE ou SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE   # garde-fou anti-boucle
      passer à l'item suivant

    SELON type(item) :

      CAS "inconnue" :
        SI REUTILISER_ACQUIS(item) ALORS marquer résolu ; continuer
        DISTINGUER_INDETERMINE_ET_NON_CHERCHE
        moyen := CHOISIR_MOYEN_DE_LEVEE
        SI moyen == "question" :
          DECIDER_D_INTERROGER_UTILISATEUR
          FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE
        SINON SI moyen == "agent" :
          RESPECTER_CADRE_AUTORISE ; DECIDER_D_OUVRIR_UN_AGENT
          SI d'autres inconnues de FILE partagent un domaine d'enquête séparable :
            les regrouper ; PARALLELISER_ENQUETE
            POUR chaque agent : REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT
          SINON : REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT ; lancer un seul agent
          INTEGRER_RETOUR_AGENT
          ARRETER_ORCHESTRATION   # un agent de plus changerait-il quelque chose ?
        SINON SI moyen == "action réversible" : LEVER_INCONNUE_PAR_ACTION_REVERSIBLE
        SINON : MENER_VERIFICATION

        CONSIGNER_PROVENANCE_FAIT ; ENONCER_LIMITES_FAIT ; JUGER_PEREMPTION_FAIT
        SI périssable ALORS INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
        REFUSER_AUTO_CONFIRMATION
        SI contradiction avec un fait déjà établi :
          DETECTER_CONTRADICTION_ENTRE_SOURCES ; DETECTER_ORIGINE_COMMUNE_SOURCES
          RESOUDRE_CONTRADICTION
        SEPARER_OBSERVE_ET_SUPPOSE ; RENDRE_INCERTITUDE_VISIBLE

        SI toujours non levée : compteurs_rebond[item] += 1 ; réinsérer dans FILE
        SINON :
          marquer résolu
          POUR chaque item de FILE dépendant de cette inconnue : le rendre éligible

      CAS "exigence tacite" :
        SI la dimension est pertinente pour ce périmètre :
          FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE   # jamais imposée
          SI confirmée : ajouter à RECENSER_CONTRAINTES_DURES ou RECENSER_PREFERENCES
                          empiler les inconnues/décisions que cela fait naître
        retirer de FILE (traité en un passage)

      CAS "décision" :
        ORIENTER_CHOIX
        SI "fait manquant" :
          empiler l'inconnue correspondante avec haute priorité ; réinsérer cette décision
                    en attente (dépendance explicite) ; continuer
        SINON SI "préférence" : demander directement à l'utilisateur ; ATTENDRE
        SINON :
          PRODUIRE_OPTIONS_DISTINCTES ; GARANTIR_DIVERSITE_METHODE
          CHERCHER_APPROCHES_NON_ENVISAGEES ; CHERCHER_ANTECEDENTS
          EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
          SI hypothèse = inconnue non levée : empiler, réinsérer la décision en attente ; continuer
          POUR chaque option : ATTAQUER_UNE_OPTION (attaque légère, un seul passant)
          SI compromis matériel : PRESENTER_ALTERNATIVES_AU_CHOIX ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
          SINON : trancher directement sur le résultat de l'attaque
        DISTINGUER_CHOIX_ET_CONSEQUENCE
        CONSIGNER_CE_QUI_A_TRANCHE ; NOMMER_FAIT_QUI_FERAIT_BASCULER
        QUALIFIER_PORTEE_DECISION ; QUALIFIER_ETAT_RESOLUTION ; CONSERVER_OPTIONS_ECARTEES
        DERIVER_ACTIONS_DEPUIS_DECISIONS → ajouter au JEU_D_ETAPES (accumulateur, hors file)
        marquer résolu ; débloquer les décisions dépendantes → les empiler

    toutes les N itérations : VERIFIER_COUVERTURE_OBJECTIFS
      SI objectif non couvert ALORS empiler une nouvelle décision "couvrir cet objectif"

ASSEMBLAGE (file épuisée)
  DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER si le JEU_D_ETAPES est trop gros
  DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE → CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
  ORDONNER_PAR_PREREQUIS ; IDENTIFIER_ETAPES_SIMULTANEES → VERIFIER_SIMULTANEITE_POSSIBLE
  POUR chaque étape : DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC
                       DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE ; QUALIFIER_REVERSIBILITE
  POUR chaque inconnue d'exécution parquée : CONSTRUIRE_BRANCHE_CONDITIONNELLE
  RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
  TANT QUE NON CONTROLER_TAILLE_DES_ETAPES : ajuster
  ELAGUER_ETAPES_INUTILES

  RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT
  RECENSER_INVARIANTS
  SI NON VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN :
    empiler un item "décision : reconcevoir ce chemin" dans FILE ; RETOUR à BOUCLE PRINCIPALE
  ANTICIPER_TIERS_REACTIF ; STATUER_SUR_RISQUE_RESIDUEL
  RECENSER_RESSOURCES_EXECUTION ; RECENSER_DEPENDANCES_EXTERNES
  SI NON VERIFIER_FAISABILITE_PAR_EXECUTANT :
    empiler un item "décision : ajuster au profil de l'exécutant" ; RETOUR à BOUCLE PRINCIPALE
  REPERER_POINTS_ENGAGEMENT
  PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION
  TANT QUE NON VERIFIER_COUVERTURE_BLOQUANTS : ajouter les points manquants
  PROPOSER_AFFECTATION ; PROPOSER_MARGES ; PROPOSER_CHIFFRAGE
  PREVOIR_SUITE_EN_CAS_DE_SUCCES ; SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN

REDACTION ET CONTROLE FINAL
  REDIGER_PLAN ; RENDRE_ACTIONNABLE_PAR_AGENT ; ELAGUER_LA_PROSE
  REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER

  tours := 0
  RÉPÉTER
    VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_COHERENCE_ENSEMBLE
    VERIFIER_ADOSSEMENT_AFFIRMATIONS ; REFUSER_AUTO_CONFIRMATION
    RENDRE_INCERTITUDE_VISIBLE ; SEPARER_OBSERVE_ET_SUPPOSE
    CONTROLER_INTEGRITE_DOCUMENT ; CONTROLER_CONTENU_FINAL
    FAIRE_CONTROLER_PAR_UN_TIERS ; INTEGRER_RETOUR_AGENT
    SI échec : empiler l'item ciblé correspondant dans FILE ; retraiter (BOUCLE PRINCIPALE, portée réduite au seul item) ; tours += 1
  JUSQU'À (tout passe) OU (tours == 3)
  RESTITUER_EN_BREF
```

### Les boucles

- **La boucle principale elle-même** est LA boucle de l'architecture — pas une exception locale. Déclenchée par : FILE non vide. Termine parce que chaque item traité est soit résolu (retiré définitivement), soit réinjecté avec un compteur de rebond qui augmente ; au-delà de 5 rebonds, un garde-fou force une sortie (`CONSTATER_IMPOSSIBILITE` ou `SUSPENDRE_ENQUETE_ET_DEMANDER`, qui attend une réponse humaine et ne boucle donc jamais côté système). La taille de FILE n'est pas monotone (un item peut en engendrer d'autres) mais elle est bornée par le nombre fini d'inconnues/décisions/exigences possibles issues du périmètre déjà délimité.
- **Boucle de déblocage par dépendance** : quand une décision bute sur un fait manquant, elle se réinsère "en attente" derrière l'inconnue qu'elle a elle-même fait naître — c'est le mécanisme structurant de cette architecture (contrairement à une approche purement séquentielle où c'est un aller-retour entre phases nommées). Termine car le fait, une fois résolu, retire la condition de blocage de façon définitive.
- **Boucle de retour depuis l'assemblage** : un échec sur les invariants ou la faisabilité ne redémarre pas une "phase" — il réinjecte un item dans FILE et relance la boucle principale, avec toute la machinerie de priorité qui s'applique aussi à cet item. Termine par le même mécanisme de compteur de rebond.
- **Boucle du contrôle final** : bornée à 3 tours, mais chaque échec ne renvoie qu'un item précis dans FILE plutôt qu'une phase entière — granularité plus fine qu'en une autre approche.

### Fonctions appelées plusieurs fois

`CHOISIR_MOYEN_DE_LEVEE`, `MENER_VERIFICATION`, `CONSIGNER_PROVENANCE_FAIT`, `REFUSER_AUTO_CONFIRMATION` (un item "inconnue" à la fois) ; `ORDONNER_INCONNUES_SANS_ECARTER`/`QUALIFIER_PORTEE_DECISION` (à chaque tour, pour re-classer la file — c'est le cœur du mécanisme de priorité, donc littéralement appelée à chaque itération) ; `ATTAQUER_UNE_OPTION` (une fois par option de chaque décision) ; `FORMULER_QUESTION_ACTIONNABLE`/`SUSPENDRE_ENQUETE_ET_DEMANDER` (chaque fois qu'un item choisit la voie "question") ; `ARRETER_ORCHESTRATION` (après chaque vague d'agents, pour juger s'il faut continuer à paralléliser) ; `REUTILISER_ACQUIS` (systématiquement en tête de traitement de toute inconnue, pour éviter le travail redondant — fonction de garde appelée à quasiment chaque itération).

### Ce qu'elle laisse de côté

- `ISOLER_LES_EVALUATIONS`, `ARBITRER_A_L_AVEUGLE`, `QUALIFIER_INDEPENDANCE_OBTENUE`, `DETECTER_ERREURS_CORRELEES`, `CHOISIR_ANGLES_ATTAQUE`, `ATTAQUER_TOUT_LE_CHAMP` : le rituel contradictoire complet (séparation stricte des évaluations, arbitrage à l'aveugle) est disproportionné pour un item traité isolément dans une file — cette architecture optimise le débit et la couverture des dépendances, pas la rigueur contradictoire de chaque décision prise une à une. C'est un vrai renoncement, pas un oubli (voir "faiblesses" plus bas) ; c'est précisément le terrain de une autre approche.

### Forces et faiblesses

**Fait bien :** épouse naturellement des tâches où les inconnues et les décisions sont enchevêtrées et où l'ordre "correct" n'est pas connu à l'avance — pas de rebond coûteux entre "phases", juste une réinsertion locale dans la file. Excellent pour maximiser le parallélisme (agents groupés par domaine via `PARALLELISER_ENQUETE`) et pour ne jamais traiter un point avant que ses préalables soient réellement réglés (dépendances explicites, pas d'ordre arbitraire).
**Fait mal :** moins lisible de l'extérieur — il n'y a pas de "où en est-on" simple, juste un état de file à un instant T, ce qui complique l'audit humain en cours de route. Le contradictoire allégé sur les décisions (une seule attaque, pas d'isolement) l'expose à des biais contrairement à une approche purement séquentielle éliminerait ; à réserver aux décisions à faible enjeu ou à compléter ponctuellement par un passage adversarial pour les décisions dont `QUALIFIER_PORTEE_DECISION` révèle un fort impact.

---

---


# Architecture 06 — Chaînage par dépendances


**Principe** : construire un graphe de décisions entre l'état actuel et la cible, les ordonner par ce qu'elles conditionnent, et résoudre chaque nœud dans cet ordre, en ne rouvrant que les nœuds affectés quand une résolution ultérieure les remet en cause.

### Pseudo-code

```
# --- Phase 0 : recevabilité --------------------------------------------
techniques = LIRE_TECHNIQUES_AUTORISEES()
destinataire = IDENTIFIER_DESTINATAIRE()
capacites = INVENTORIER_CAPACITES()
perimetre = DELIMITER_PERIMETRE()
besoin = SEPARER_DEMANDE_ET_BESOIN()

REPEAT au plus 1 fois:
    solution_imposee = DETECTER_SOLUTION_IMPOSEE()
    contestation = CONTESTER_ENONCE_PROBLEME()
    SI solution_imposee OU contestation.reformulee:
        besoin = SEPARER_DEMANDE_ET_BESOIN()   # reformulé une fois, pas plus

forme = QUALIFIER_FORME_TRAVAIL()
SI forme != "planification":
    DECLINER_SI_PAS_DE_PLAN(); STOP

techniques_actives = EVALUER_EXIGENCE_TACHE(techniques)
plan_existant = AMORCER_DEPUIS_PLAN_EXISTANT()   # si applicable

# --- Phase 1 : état, cible, objectifs -----------------------------------
etat = ETABLIR_ETAT_ACTUEL()
REPEAT:
    cible = FORMULER_CIBLE_OBSERVABLE(besoin)
    fidele = VERIFIER_FIDELITE_CIBLE_BESOIN(cible, besoin)
UNTIL fidele                                      # boucle 1

criteres = DEFINIR_CRITERES_ACCEPTATION(cible)
objectifs = ORDONNER_OBJECTIFS_SANS_ECARTER()
conflit = DETECTER_CONFLIT_OBJECTIFS(objectifs)
SI conflit:
    SOUMETTRE_ARBITRAGE_UTILISATEUR(conflit)      # bloquant, attend la réponse
    objectifs = ORDONNER_OBJECTIFS_SANS_ECARTER()  # ré-ordonné avec la réponse

BALAYER_EXIGENCES_TACITES()
TRAQUER_AJOUTS_SILENCIEUX()
prefs = RECENSER_PREFERENCES()
contraintes = RECENSER_CONTRAINTES_DURES()
obligations = RECENSER_OBLIGATIONS_FORMELLES()
EXPOSER_EXTERNALITES_CERTAINES()

# --- Phase 2 : construction du graphe -----------------------------------
squelette = CHAINER_ETAT_ACTUEL_VERS_CIBLE(etat, cible)   # aller-retour
noeuds = ETABLIR_DEPENDANCES_ENTRE_DECISIONS(squelette)
FOR chaque noeud in noeuds:
    noeud.type = DISTINGUER_CHOIX_ET_CONSEQUENCE(noeud)
    SI noeud.type == "consequence mecanique":
        noeud.essentiel = DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE(noeud)
        SI noeud.essentiel == "à sonder":
            CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE(noeud)

ordre = ORDONNER_PAR_PREREQUIS(noeuds)   # ordre topologique de résolution

# --- Phase 3 : résolution nœud par nœud (coeur de l'architecture) -------
FOR chaque noeud in ordre:                          # boucle 2 (externe)
    tentatives = 0
    REPEAT
        tentatives += 1
        inconnues = RECENSER_INCONNUES(noeud)
        FOR i in inconnues:
            i.classe = CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION(i)
        bloquantes = [i for i in inconnues if i.classe == "construction"]
        bloquantes = ORDONNER_INCONNUES_SANS_ECARTER(bloquantes)

        FOR i in bloquantes:                         # boucle 3 (levée)
            i.portee = QUALIFIER_PORTEE_INCONNUE(i)
            i.nature = DISTINGUER_INDETERMINE_ET_NON_CHERCHE(i)
            moyen = CHOISIR_MOYEN_DE_LEVEE(i)
            SWITCH moyen:
                CASE "inspection", "calcul", "test":
                    fait = MENER_VERIFICATION(i)
                CASE "source":
                    fait = CHERCHER_ANTECEDENTS(i)
                CASE "action reversible":
                    fait = LEVER_INCONNUE_PAR_ACTION_REVERSIBLE(i)
                CASE "agent":
                    SI ARRETER_ORCHESTRATION(contexte_agents):
                        fait = ECHEC
                    SINON:
                        ouvrir = DECIDER_D_OUVRIR_UN_AGENT(i)
                        SI ouvrir:
                            brief = REDIGER_BRIEF_AGENT(i, faits_etablis)
                            BORNER_UN_AGENT(brief)
                            RESPECTER_CADRE_AUTORISE(brief)
                            retour = lancer_agent(brief)
                            fait = INTEGRER_RETOUR_AGENT(retour)
                CASE "question":
                    q = FORMULER_QUESTION_ACTIONNABLE(i)
                    SUSPENDRE_ENQUETE_ET_DEMANDER(q)   # bloquant, attend
                    fait = reponse_utilisateur

            SI fait établi:
                CONSIGNER_PROVENANCE_FAIT(fait)
                SEPARER_OBSERVE_ET_SUPPOSE(fait)
                ENONCER_LIMITES_FAIT(fait)
                peremption = JUGER_PEREMPTION_FAIT(fait)
                SI peremption == "périssable":
                    INSCRIRE_REVERIFICATION_FAIT_PERISSABLE(fait, noeud)
                SI existe fait_concurrent:
                    SI DETECTER_CONTRADICTION_ENTRE_SOURCES(fait, fait_concurrent):
                        DETECTER_ORIGINE_COMMUNE_SOURCES(fait, fait_concurrent)
                        resolu = RESOUDRE_CONTRADICTION(fait, fait_concurrent)
                        SI NON resolu: i.reste_ouverte = VRAI  # -> re-choisir un moyen

        # options et arbitrage local au nœud
        SI noeud a plusieurs options plausibles:
            options = PRODUIRE_OPTIONS_DISTINCTES(noeud)
            FOR o in options:
                EXIGER_HYPOTHESES_EXPLICITES(o)
                DEBUSQUER_HYPOTHESES_IMPORTEES(o)
                angles = CHOISIR_ANGLES_ATTAQUE(o)
                ATTAQUER_UNE_OPTION(o, angles)
            options = AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE(options)  # ordre de test
            decision = ORIENTER_CHOIX(options)
            SWITCH decision.nature:
                CASE "fait manquant":
                    CONTINUE le REPEAT du noeud      # relève une inconnue -> re-boucle
                CASE "preference requise":
                    PRESENTER_ALTERNATIVES_AU_CHOIX(options)   # bloquant
                CASE "vrai choix":
                    gagnant = decision.choix
            CONSERVER_OPTIONS_ECARTEES(options, gagnant)
            QUALIFIER_PORTEE_DECISION(gagnant)
            NOMMER_FAIT_QUI_FERAIT_BASCULER(gagnant)
            CONSIGNER_CE_QUI_A_TRANCHE(gagnant)

        noeud.etat = QUALIFIER_ETAT_RESOLUTION(noeud)
    UNTIL noeud.etat in {"tranché", "tranché avec compromis", "branché"}
       OR tentatives >= 2                            # borne de la boucle 3

    SI noeud.etat == "non résolu" ET noeud a des dépendants:
        SI tentatives >= 2:
            CONSTATER_IMPOSSIBILITE(noeud); STOP        # sortie garantie
    noeud.resolu = VRAI

# --- Phase 4 : cohérence globale et réparation ciblée --------------------
passes_reparation = 0
REPEAT
    coherent = VERIFIER_COHERENCE_ENSEMBLE(noeuds)     # boucle 4
    SI NON coherent:
        noeud_fautif = identifier_source_incoherence()
        REUTILISER_ACQUIS(noeud_fautif.faits_valides)   # ne redémontre pas ce qui tient
        rouvrir(noeud_fautif)  -> relance Phase 3 pour ce noeud seul
        propager_aux_dependants(noeud_fautif)           # ré-ouvre en cascade, jamais en amont
        passes_reparation += 1
UNTIL coherent OR passes_reparation >= 2
SI NON coherent:
    SUSPENDRE_ENQUETE_ET_DEMANDER("incohérence non résoluble seul")

# --- Phase 5 : dérivation en étapes --------------------------------------
DERIVER_ACTIONS_DEPUIS_DECISIONS(noeuds)
DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(etapes_trop_grosses)
etapes = ORDONNER_PAR_PREREQUIS(etapes)
simultanees = IDENTIFIER_ETAPES_SIMULTANEES(etapes)
FOR paire in simultanees:
    SI NON VERIFIER_SIMULTANEITE_POSSIBLE(paire):
        retirer_de(simultanees, paire)

FOR noeud in noeuds où noeud.etat == "branché":
    CONSTRUIRE_BRANCHE_CONDITIONNELLE(noeud)

FOR etape in etapes:
    DEFINIR_ATTENDU_OBSERVABLE(etape)
    DEFINIR_SIGNAUX_ECHEC(etape)
    ra = DEFINIR_RETOUR_ARRIERE(etape)
    SI ra != "n'existe pas":
        REPEAT au plus 2 fois:
            verifie = EPROUVER_RETOUR_ARRIERE(ra)
        UNTIL verifie OR épuisé
    RATTACHER_TOUTE_PIECE_A_SON_ORIGINE(etape)

REPEAT
    ok = CONTROLER_TAILLE_DES_ETAPES(etapes)           # boucle 5
    SI NON ok: ajuster_decoupage(etapes)
UNTIL ok

# --- Phase 6 : risque, invariants, gouvernance ---------------------------
risques = RECENSER_RISQUES_PAR_ORIGINE(etapes)
FOR r in risques:
    QUALIFIER_VRAISEMBLANCE_RISQUE(r)
    QUALIFIER_RAYON_IMPACT(r)
QUALIFIER_REVERSIBILITE(etapes)
REPERER_POINTS_ENGAGEMENT(etapes)
ANTICIPER_TIERS_REACTIF(etapes)
invariants = RECENSER_INVARIANTS()

REPEAT
    ok = VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(etapes, invariants)  # boucle 6
    SI NON ok:
        ajouter_etape_ou_branche_correctrice()          # remonte à la Phase 5, localement
UNTIL ok
FOR r in risques: STATUER_SUR_RISQUE_RESIDUEL(r)

DESIGNER_AUTORITE_AUTORISATION()
PLACER_POINTS_AUTORISATION(etapes)
PLACER_JALONS_CONSTAT(etapes)
PLACER_POINTS_VERIFICATION(etapes)
REPEAT
    ok = VERIFIER_COUVERTURE_BLOQUANTS(etapes)          # boucle 7
    SI NON ok: ajouter_point_manquant()
UNTIL ok
RECENSER_DEPENDANCES_EXTERNES()
ressources = RECENSER_RESSOURCES_EXECUTION()
REPEAT au plus 2 fois:
    faisable = VERIFIER_FAISABILITE_PAR_EXECUTANT(etapes, ressources)  # boucle 8
    SI NON faisable: revoir_hypotheses_d_execution()
UNTIL faisable OR épuisé
SI NON faisable:
    SIGNALER_LES_LIMITES("plan non exécutable par ce destinataire")

PROPOSER_MARGES(); PROPOSER_AFFECTATION(); PROPOSER_CHIFFRAGE()  # offerts, jamais imposés

# --- Phase 7 : nettoyage puis contrôle final ------------------------------
ELAGUER_ETAPES_INUTILES(etapes)
ISOLER_LE_HORS_PLAN()
SIGNALER_LES_LIMITES()
PREVOIR_SUITE_EN_CAS_DE_SUCCES()

passes_qa = 0
REPEAT
    VERIFIER_COUVERTURE_OBJECTIFS(objectifs, etapes)
    VERIFIER_ADOSSEMENT_AFFIRMATIONS(etapes)
    REFUSER_AUTO_CONFIRMATION()
    DETECTER_ERREURS_CORRELEES()
    RENDRE_INCERTITUDE_VISIBLE()
    ok1 = VERIFIER_COHERENCE_ENSEMBLE(noeuds)
    ok2 = CONTROLER_CONTENU_FINAL()
    ok3 = CONTROLER_INTEGRITE_DOCUMENT()
    avis = FAIRE_CONTROLER_PAR_UN_TIERS()
    INTEGRER_RETOUR_AGENT(avis)
    passes_qa += 1
UNTIL (ok1 ET ok2 ET ok3 ET avis.propre) OR passes_qa >= 2      # boucle 9
SI toujours en échec:
    SUSPENDRE_ENQUETE_ET_DEMANDER("le plan ne passe pas le contrôle final")

ELAGUER_LA_PROSE()
RENDRE_ACTIONNABLE_PAR_AGENT()
REDIGER_PLAN()
REDIGER_TRACABILITE_SEPAREE()
PLACER_ET_NOMMER_LE_FICHIER()
RESTITUER_EN_BREF()
```

### Les boucles

- **Boucle 1** (fidélité cible/besoin) : déclenchée par `VERIFIER_FIDELITE_CIBLE_BESOIN` négatif ; remonte à `FORMULER_CIBLE_OBSERVABLE` seul ; se termine dès qu'elle passe (pas de borne explicite car c'est une reformulation locale peu coûteuse, mais en pratique bornée par le fait qu'il n'existe qu'un nombre fini de reformulations raisonnables).
- **Boucle 2** (externe, un tour par nœud) : structure la phase 3 entière ; se termine naturellement quand tous les nœuds sont traités dans l'ordre topologique — garantie par la taille finie du graphe.
- **Boucle 3** (levée d'inconnue à l'intérieur d'un nœud) : déclenchée par une inconnue bloquante ou un choix qui révèle un fait manquant ; remonte au plus à l'intérieur du même nœud ; bornée à 2 tentatives puis `CONSTATER_IMPOSSIBILITE`.
- **Boucle 4** (cohérence globale) : déclenchée par `VERIFIER_COHERENCE_ENSEMBLE` négatif après assemblage ; remonte uniquement au(x) nœud(s) fautif(s) et à leurs dépendants — jamais à l'amont ; bornée à 2 passes puis suspension vers l'utilisateur.
- **Boucles 5, 6, 7, 8** : boucles de vérification locales (taille des étapes, invariants, couverture des points de blocage, faisabilité côté exécutant) — chacune corrige uniquement l'objet contrôlé et se termine dès que le contrôle passe, avec une borne (2 tentatives) sur celles qui pourraient buter sur un vrai désaccord (invariants, faisabilité).
- **Boucle 9** (QA finale) : déclenchée par tout échec de `CONTROLER_CONTENU_FINAL` / `CONTROLER_INTEGRITE_DOCUMENT` / relecture tierce ; remonte à la phase concernée (pas de redémarrage complet) ; bornée à 2 passes puis `SUSPENDRE_ENQUETE_ET_DEMANDER`.

Terminaison garantie : chaque boucle interne est bornée numériquement (2 tentatives), et la boucle externe (2) porte sur un ensemble fini et acyclique de nœuds — il ne peut donc pas y avoir de cycle infini, seulement une escalade vers `CONSTATER_IMPOSSIBILITE` ou `SUSPENDRE_ENQUETE_ET_DEMANDER`.

### Fonctions appelées plusieurs fois

- `CHOISIR_MOYEN_DE_LEVEE`, `MENER_VERIFICATION`, `CONSIGNER_PROVENANCE_FAIT` : une fois par inconnue, et il y en a beaucoup, réparties sur tout le graphe.
- `VERIFIER_COHERENCE_ENSEMBLE` : une fois par passe de réparation (phase 4) puis une fois en QA finale (phase 7) — c'est le même contrôle appliqué à un objet qui a changé entre-temps.
- `QUALIFIER_ETAT_RESOLUTION`, `CONSIGNER_CE_QUI_A_TRANCHE` : une fois par nœud de décision.
- `DECIDER_D_OUVRIR_UN_AGENT` / `ARRETER_ORCHESTRATION` : à chaque inconnue candidate à la délégation, pour éviter d'ouvrir des agents en boucle.
- `EPROUVER_RETOUR_ARRIERE`, `CONTROLER_TAILLE_DES_ETAPES` : itérées jusqu'à validation.

### Ce que ça fait bien / mal

**Bien** : la dépendance entre décisions est explicite et respectée — on ne tranche jamais un point avant ce dont il dépend ; les réparations sont chirurgicales (on ne rouvre que ce qui est affecté) ; bonne traçabilité nœud par nœud.
**Mal** : le graphe de dépendances doit être construit correctement dès la phase 2 — s'il est mal formé, toute la suite hérite de l'erreur et la détection n'arrive qu'en phase 4 (coûteux à diagnostiquer) ; l'architecture ne compare jamais des *plans entiers* concurrents, seulement des options locales à un nœud, donc elle peut rater une solution radicalement différente qui n'aurait émergé qu'en repensant tout le squelette.

### Fonctions volontairement laissées de côté
`ARBITRER_A_L_AVEUGLE`, `ISOLER_LES_EVALUATIONS`, `QUALIFIER_INDEPENDANCE_OBTENUE` : ces fonctions supposent un tournoi anonymisé entre plans concurrents complets — cette architecture n'en produit pas, elle résout nœud par nœud via les faits et les dépendances. `GARANTIR_DIVERSITE_METHODE` et `CHERCHER_APPROCHES_NON_ENVISAGEES` : pertinentes pour balayer large sur un problème entier, moins pour un choix local déjà cadré par ses voisins dans le graphe.

---

---


# Architecture 07 — L'arbre des objectifs

<details><summary>Briques utilisées</summary>

```
FONCTION PROLOGUE_CADRAGE(demande):
    LIRE_TECHNIQUES_AUTORISEES()
    INVENTORIER_CAPACITES()
    IDENTIFIER_DESTINATAIRE()
    SEPARER_DEMANDE_ET_BESOIN(demande)
    CONTESTER_ENONCE_PROBLEME()
    SI DETECTER_SOLUTION_IMPOSEE(): reformuler comme problème, pas comme solution imposée
    SI DECLINER_SI_PAS_DE_PLAN(): retourner "pas de planification ici", FIN
    SI un plan existant est fourni: AMORCER_DEPUIS_PLAN_EXISTANT()
    ETABLIR_ETAT_ACTUEL()
    CHERCHER_ANTECEDENTS()
    FORMULER_CIBLE_OBSERVABLE()
    VERIFIER_FIDELITE_CIBLE_BESOIN()
    TRAQUER_AJOUTS_SILENCIEUX()
    DEFINIR_CRITERES_ACCEPTATION()
    RECENSER_CONTRAINTES_DURES()
    RECENSER_OBLIGATIONS_FORMELLES()
    RECENSER_PREFERENCES()
    BALAYER_EXIGENCES_TACITES()
    DEBUSQUER_HYPOTHESES_IMPORTEES()
    EXPOSER_EXTERNALITES_CERTAINES()
    RECENSER_DEPENDANCES_EXTERNES()
    RECENSER_RESSOURCES_EXECUTION()
    DELIMITER_PERIMETRE()
    retourner périmètre_racine, état_partagé{faits:[], décisions:[], risques:[]}

FONCTION EPILOGUE_CLOTURE(état_partagé, plan):
    RENDRE_ACTIONNABLE_PAR_AGENT(plan)
    VERIFIER_COHERENCE_ENSEMBLE(plan)
    VERIFIER_COUVERTURE_OBJECTIFS(plan)
    VERIFIER_COUVERTURE_BLOQUANTS(plan)
    VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(plan)
    VERIFIER_FAISABILITE_PAR_EXECUTANT(plan)
    VERIFIER_ADOSSEMENT_AFFIRMATIONS(état_partagé)
    ELAGUER_ETAPES_INUTILES(plan)
    ELAGUER_LA_PROSE(plan)
    ISOLER_LE_HORS_PLAN(plan)
    SIGNALER_LES_LIMITES(plan)
    PREVOIR_SUITE_EN_CAS_DE_SUCCES(plan)
    PROPOSER_MARGES() ; PROPOSER_AFFECTATION() ; PROPOSER_CHIFFRAGE()
    CONTROLER_CONTENU_FINAL(plan)
    CONTROLER_INTEGRITE_DOCUMENT(plan)
    avis = FAIRE_CONTROLER_PAR_UN_TIERS(plan)
    TANT QUE avis signale une faille ET passes < 2:
        corriger localement la partie visée ; avis = FAIRE_CONTROLER_PAR_UN_TIERS(plan) ; passes += 1
    SI faille persistante: QUALIFIER_ETAT_RESOLUTION(point) = "non résolu" ; SIGNALER_LES_LIMITES(point)
    PLACER_ET_NOMMER_LE_FICHIER()
    REDIGER_PLAN(plan)
    REDIGER_TRACABILITE_SEPAREE(état_partagé)
    RESTITUER_EN_BREF()
```

---

</details>


**Principe** : le périmètre se scinde selon les objectifs qui le composent ; chaque sous-objectif (ou cluster d'objectifs) reçoit le cycle complet, et la *structure du plan final* épouse directement cet arbre — c'est une décomposition « ET » (tous les morceaux sont nécessaires).

**Les 6 choix de conception**
- **Déclencheur de coupe** : objectifs en conflit (`DETECTER_CONFLIT_OBJECTIFS`) ou de nature hétérogène (`QUALIFIER_FORME_TRAVAIL` diverge), ou trop nombreux pour un seul cycle.
- **Découpe** : `ORDONNER_OBJECTIFS_SANS_ECARTER` regroupe en clusters cohérents ; chaque cluster devient un sous-périmètre.
- **Effort par profondeur** : le cadrage racine (prologue) n'est jamais rejoué (`REUTILISER_ACQUIS`) ; `EVALUER_EXIGENCE_TACHE` est réévalué à chaque nœud et réduit mécaniquement l'éventail de techniques (attaque adverse, marges, etc.) à mesure qu'on descend.
- **Recomposition** : `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` + `ORDONNER_PAR_PREREQUIS` sur l'union des actions, puis `VERIFIER_COHERENCE_ENSEMBLE`.
- **Dépendances entre frères** : `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` après remontée ; simultanéité testée par `IDENTIFIER_ETAPES_SIMULTANEES` + `VERIFIER_SIMULTANEITE_POSSIBLE`.
- **Borne de profondeur** : arrêt quand `QUALIFIER_FORME_TRAVAIL` devient homogène dans le cluster, ou `PROFONDEUR_MAX` fixée par la config (`RESPECTER_CADRE_AUTORISE`).

```
FONCTION CYCLE_A(périmètre, profondeur, état_partagé):
    effort = EVALUER_EXIGENCE_TACHE(périmètre, profondeur)

    objectifs = ORDONNER_OBJECTIFS_SANS_ECARTER(périmètre)
    conflits  = DETECTER_CONFLIT_OBJECTIFS(objectifs)
    formes    = [QUALIFIER_FORME_TRAVAIL(o) pour o dans objectifs]

    SI profondeur < PROFONDEUR_MAX
       ET (conflits non vides OU formes hétérogènes OU len(objectifs) > SEUIL(profondeur)):

        clusters = DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER.decouper(objectifs, conflits)
        sous_plans = []
        POUR chaque cluster DANS clusters:
            sp = DELIMITER_PERIMETRE(cluster, hérite=périmètre)
            se = REUTILISER_ACQUIS(état_partagé)
            sous_plans.ajouter( CYCLE_A(sp, profondeur+1, se) )

        # remontée : une décision qui déborde son cluster ne se tranche pas dans le cluster
        POUR chaque sp DANS sous_plans, POUR chaque décision DANS sp.décisions_en_attente:
            SI QUALIFIER_PORTEE_DECISION(décision) déborde le cluster:
                état_partagé.décisions_à_trancher_ici.ajouter(décision)
        POUR chaque décision DANS état_partagé.décisions_à_trancher_ici:
            TRANCHER_DECISION(décision, état_partagé)     # bloc ci-dessous

        actions = fusion(sous_plans.actions)
        ETABLIR_DEPENDANCES_ENTRE_DECISIONS(toutes_les_décisions(sous_plans))
        actions = ORDONNER_PAR_PREREQUIS(actions)
        POUR chaque paire DANS IDENTIFIER_ETAPES_SIMULTANEES(actions):
            SI NON VERIFIER_SIMULTANEITE_POSSIBLE(paire): dé-paralléliser la paire

        SI NON VERIFIER_COHERENCE_ENSEMBLE(actions):     # BOUCLE DE RETOUR 1
            fautifs = localiser_sous_plans_en_cause(actions)
            POUR chaque f DANS fautifs (max 2 reprises par sous-périmètre):
                f.nouveau_plan = CYCLE_A(f.périmètre, profondeur+1, f.état, contrainte+=incohérence)
            SI encore incohérent après 2 reprises: SOUMETTRE_ARBITRAGE_UTILISATEUR(fautifs)

        plan = actions

    SINON:
        plan = TRAITER_FEUILLE(périmètre, objectifs, profondeur, état_partagé)

    retourner plan


FONCTION TRAITER_FEUILLE(périmètre, objectifs, profondeur, état_partagé):
    RECENSER_INCONNUES(périmètre)
    POUR chaque inc DANS ORDONNER_INCONNUES_SANS_ECARTER(...):
        moyen = CHOISIR_MOYEN_DE_LEVEE(inc)
        fait  = MENER_VERIFICATION(moyen) OU LEVER_INCONNUE_PAR_ACTION_REVERSIBLE(moyen)
        CONSIGNER_PROVENANCE_FAIT(fait) ; état_partagé.faits.ajouter(fait)

    CHAINER_ETAT_ACTUEL_VERS_CIBLE(périmètre)
    actions = DERIVER_ACTIONS_DEPUIS_DECISIONS(décisions_locales)

    POUR chaque pas DANS actions:
        SI DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE(pas) == "mécanique":
            CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE(pas)
        DISTINGUER_CHOIX_ET_CONSEQUENCE(pas)
        DEFINIR_ATTENDU_OBSERVABLE(pas) ; DEFINIR_SIGNAUX_ECHEC(pas)
        rb = DEFINIR_RETOUR_ARRIERE(pas)
        SI rb.affirmé_non_vérifié: EPROUVER_RETOUR_ARRIERE(pas)
        REPERER_POINTS_ENGAGEMENT(pas)
    RECENSER_INVARIANTS(périmètre)

    POUR chaque risque DANS RECENSER_RISQUES_PAR_ORIGINE(périmètre):
        QUALIFIER_VRAISEMBLANCE_RISQUE(risque)
        SI QUALIFIER_RAYON_IMPACT(risque) déborde le périmètre:
            état_partagé.risques_à_traiter_au_dessus.ajouter(risque)   # ESCALADE
        SINON:
            QUALIFIER_REVERSIBILITE(risque) ; ANTICIPER_TIERS_REACTIF(risque)
            STATUER_SUR_RISQUE_RESIDUEL(risque)

    TANT QUE une étape mal taillée par CONTROLER_TAILLE_DES_ETAPES(actions) ET reprises<2:  # BOUCLE DE VERIFICATION
        refactorer l'étape ; reprises += 1

    PLACER_POINTS_VERIFICATION(actions) ; PLACER_POINTS_AUTORISATION(actions)
    DESIGNER_AUTORITE_AUTORISATION(actions) ; PLACER_JALONS_CONSTAT(actions)
    CONSTRUIRE_BRANCHE_CONDITIONNELLE(points_encore_incertains)

    SI NON VERIFIER_COUVERTURE_OBJECTIFS(objectifs, actions):
        POUR l'objectif non couvert: CONSTATER_IMPOSSIBILITE(objectif) → remonter comme décision au parent
    retourner actions


FONCTION TRANCHER_DECISION(décision, état_partagé):
    options = PRODUIRE_OPTIONS_DISTINCTES(décision)
    POUR chaque option: EXIGER_HYPOTHESES_EXPLICITES(option)
    survivantes = [o pour o dans options SI ATTAQUER_UNE_OPTION(o) résiste]
    SI survivantes vide: CONSTATER_IMPOSSIBILITE(décision) ; SOUMETTRE_ARBITRAGE_UTILISATEUR([])
    SINON SI len(survivantes) > 1: PRESENTER_ALTERNATIVES_AU_CHOIX(survivantes) ; SOUMETTRE_ARBITRAGE_UTILISATEUR(survivantes)
    SINON: CONSIGNER_CE_QUI_A_TRANCHE(survivantes[0]) ; QUALIFIER_ETAT_RESOLUTION(décision)
           NOMMER_FAIT_QUI_FERAIT_BASCULER(décision)
```

**3. Boucles**
- *Boucle de retour (incohérence)* : `VERIFIER_COHERENCE_ENSEMBLE` échoue au merge → on redescend uniquement dans les sous-périmètres en cause, jamais toute la racine ; bornée à 2 reprises, sinon escalade utilisateur.
- *Boucle de vérification (calibrage des étapes)* : `CONTROLER_TAILLE_DES_ETAPES` échoue → refactoring local, bornée à 2 passes.
- *Boucle de décision* : options produites → attaquées → si toutes tombent, remonte en `CONSTATER_IMPOSSIBILITE` ou arbitrage utilisateur (jamais de re-génération infinie d'options).

**4. Fonctions appelées plusieurs fois** : `DELIMITER_PERIMETRE`, `RECENSER_INCONNUES`/`CHOISIR_MOYEN_DE_LEVEE` (à chaque feuille), `MENER_VERIFICATION`, `VERIFIER_COHERENCE_ENSEMBLE`/`ORDONNER_PAR_PREREQUIS` (à chaque niveau de fusion), `QUALIFIER_PORTEE_DECISION` (à chaque décision remontée), `CONTROLER_TAILLE_DES_ETAPES`, `PRODUIRE_OPTIONS_DISTINCTES`/`ATTAQUER_UNE_OPTION` (à chaque décision tranchée) — parce que la structure même est récursive et que chaque nœud refait son propre mini-cycle de décision et de vérification.

**5. Forces / faiblesses** : Très bon pour la traçabilité (le plan final ressemble à ce que l'utilisateur a demandé, `VERIFIER_COUVERTURE_OBJECTIFS` devient trivial) et pour des objectifs relativement indépendants. Mauvais quand les objectifs sont fortement enchevêtrés : la découpe crée des frontières artificielles, produit beaucoup de remontées de décisions et de reprises de fusion, et dilue les risques transverses (d'où la nécessité du garde-fou sur `QUALIFIER_RAYON_IMPACT`).

---

---


# Architecture 08 — File de travail à point fixe


**Principe** : pas de phases fixes — un registre unique de « points ouverts » (inconnues, décisions, risques, étapes à qualifier) est traité en boucle par ordre de dépendance/priorité ; résoudre un point peut en faire naître d'autres de n'importe quel type ; la boucle tourne jusqu'à ce que le registre soit stable, puis un unique passage d'assemblage et de contrôle final clôt le travail.

### Pseudo-code

```
INITIALISATION
  LIRE_TECHNIQUES_AUTORISEES ; INVENTORIER_CAPACITES ; IDENTIFIER_DESTINATAIRE
  EVALUER_EXIGENCE_TACHE → si non pertinent : DECLINER_SI_PAS_DE_PLAN ; FIN
  SEPARER_DEMANDE_ET_BESOIN ; DELIMITER_PERIMETRE
  CONTESTER_ENONCE_PROBLEME ; DETECTER_SOLUTION_IMPOSEE ; QUALIFIER_FORME_TRAVAIL
  si point de départ = un plan existant : AMORCER_DEPUIS_PLAN_EXISTANT
  ETABLIR_ETAT_ACTUEL ; FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
  CHAINER_ETAT_ACTUEL_VERS_CIBLE

  Q = file à priorité (dépend de ETABLIR_DEPENDANCES_ENTRE_DECISIONS / ORDONNER_INCONNUES_SANS_ECARTER)
  amorcer Q avec :
      RECENSER_INCONNUES → items[INCONNUE]
      RECENSER_CONTRAINTES_DURES, RECENSER_OBLIGATIONS_FORMELLES, RECENSER_PREFERENCES
      BALAYER_EXIGENCES_TACITES → items[INCONNUE] éventuels
      ORDONNER_OBJECTIFS_SANS_ECARTER → items[OBJECTIF]
      chaque objectif engendre au moins un item[DECISION] "comment le servir"
  chaque item reçoit une profondeur=0 et un type

BOUCLE PRINCIPALE (point fixe)
  tant que Q contient un item prêt (dont les prérequis, via ETABLIR_DEPENDANCES_ENTRE_DECISIONS, sont résolus) :

      item = Q.pop_plus_prioritaire()   # priorité = ORDONNER_INCONNUES_SANS_ECARTER / portée

      selon type(item) :

        INCONNUE:
          CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION
          si EXECUTION : QUALIFIER_PORTEE_INCONNUE ; marquer "à absorber en branche" ; ne bloque rien
          sinon:
             DISTINGUER_INDETERMINE_ET_NON_CHERCHE ; DECIDER_D_INTERROGER_UTILISATEUR
             si oui : FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER (attente)
             sinon : CHOISIR_MOYEN_DE_LEVEE → MENER_VERIFICATION / CHERCHER_ANTECEDENTS /
                     LEVER_INCONNUE_PAR_ACTION_REVERSIBLE / agent
                     si agent : DECIDER_D_OUVRIR_UN_AGENT ; REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT
                                (PARALLELISER_ENQUETE si d'autres items INCONNUE indépendants sont prêts
                                 → on les dépile et traite ensemble)
                                INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
             CONSIGNER_PROVENANCE_FAIT ; JUGER_PEREMPTION_FAIT
             si périssable : INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
             ENONCER_LIMITES_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE ; RENDRE_INCERTITUDE_VISIBLE
             DETECTER_CONTRADICTION_ENTRE_SOURCES
             si contradiction : DETECTER_ORIGINE_COMMUNE_SOURCES ; RESOUDRE_CONTRADICTION
                si non tranchable : pousser item[DECISION]("point contesté")
          si profondeur(item) < max_profondeur ET nouvelles inconnues induites :
             RECENSER_INCONNUES(local) → Q.push(profondeur+1)
          sinon si profondeur = max_profondeur :
             forcer classification "indéterminable" ; QUALIFIER_ETAT_RESOLUTION = "non résolu, signalé"
          QUALIFIER_ETAT_RESOLUTION(item)

        DECISION:
          PRODUIRE_OPTIONS_DISTINCTES ; GARANTIR_DIVERSITE_METHODE ; CHERCHER_APPROCHES_NON_ENVISAGEES
          CHERCHER_ANTECEDENTS
          pour chaque option : EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
             si hypothèse tacite non levée : Q.push(INCONNUE(hypothèse)) ; différer cette DECISION
                (dépendance ajoutée — la décision se ré-ouvrira quand l'inconnue sera close)
          ISOLER_LES_EVALUATIONS ; CHOISIR_ANGLES_ATTAQUE
          pour chaque option : ATTAQUER_UNE_OPTION
          ATTAQUER_TOUT_LE_CHAMP
          si champ entier casse et flag "reformulation_utilisée" = faux :
             flag := vrai ; pousser DECISION("reformuler le problème") tout en tête de Q → CONTESTER_ENONCE_PROBLEME
          ARBITRER_A_L_AVEUGLE ; QUALIFIER_INDEPENDANCE_OBTENUE ; DETECTER_ERREURS_CORRELEES
          CONSERVER_OPTIONS_ECARTEES
          ORIENTER_CHOIX
          selon résultat :
             fait manquant : Q.push(INCONNUE) ; différer
             préférence   : PRESENTER_ALTERNATIVES_AU_CHOIX ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre
             vrai choix   : trancher
          DISTINGUER_CHOIX_ET_CONSEQUENCE ; QUALIFIER_PORTEE_DECISION ; NOMMER_FAIT_QUI_FERAIT_BASCULER
          CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_ETAT_RESOLUTION(item)
          DERIVER_ACTIONS_DEPUIS_DECISIONS → Q.push(items[ETAPE]...)
          RECENSER_RISQUES_PAR_ORIGINE(cette décision) → Q.push(items[RISQUE]...)

        RISQUE:
          QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT
          QUALIFIER_REVERSIBILITE ; QUALIFIER_TERRITOIRE ; ANTICIPER_TIERS_REACTIF
          STATUER_SUR_RISQUE_RESIDUEL
          si "accepté"/"délégué" : SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre
          si le risque révèle une zone non couverte : Q.push(INCONNUE)

        ETAPE:
          DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC ; DEFINIR_RETOUR_ARRIERE
          EPROUVER_RETOUR_ARRIERE
          si échec : 1 relance MENER_VERIFICATION, sinon marquer "non garanti" → Q.push(RISQUE)
          CONSTRUIRE_BRANCHE_CONDITIONNELLE si une inconnue d'exécution y est rattachée
          DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE
          si mécanique : CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE

  # sortie : Q est vide (ou ne contient plus que des items en attente de réponse utilisateur)

ASSEMBLAGE (une seule passe)
  ORDONNER_PAR_PREREQUIS ; IDENTIFIER_ETAPES_SIMULTANEES
  boucle (max 2) : VERIFIER_SIMULTANEITE_POSSIBLE → re-sérialiser si conflit
  CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
  si trop volumineux : DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER
      → relancer la BOUCLE PRINCIPALE sur chaque sous-plan (récursion bornée en profondeur)
  RECENSER_INVARIANTS ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN
  si violation : Q.push(DECISION ou ETAPE concernée) ; rouvrir la BOUCLE PRINCIPALE
     (compteur global de réouvertures, plafonné à K — au-delà : CONSTATER_IMPOSSIBILITE)
  AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE

GOUVERNANCE
  PLACER_POINTS_VERIFICATION ; PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION
  REPERER_POINTS_ENGAGEMENT ; VERIFIER_COUVERTURE_BLOQUANTS (boucle locale bornée)
  RECENSER_RESSOURCES_EXECUTION ; RECENSER_DEPENDANCES_EXTERNES ; VERIFIER_FAISABILITE_PAR_EXECUTANT
  PROPOSER_MARGES ; PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE
  PREVOIR_SUITE_EN_CAS_DE_SUCCES

CONTRÔLE FINAL
  REUTILISER_ACQUIS ; VERIFIER_COUVERTURE_OBJECTIFS
  si non couvert : Q.push(DECISION/ETAPE) ; rouvrir (même compteur K que ci-dessus)
  VERIFIER_COHERENCE_ENSEMBLE ; RATTACHER_TOUTE_PIECE_A_SON_ORIGINE ; ISOLER_LE_HORS_PLAN
  SIGNALER_LES_LIMITES ; CONTROLER_CONTENU_FINAL
  FAIRE_CONTROLER_PAR_UN_TIERS → INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION (1 seul tour)
  ELAGUER_LA_PROSE ; CONTROLER_INTEGRITE_DOCUMENT
  RENDRE_ACTIONNABLE_PAR_AGENT
  REDIGER_PLAN ; REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER
  RESTITUER_EN_BREF
```

### Boucles

- **Boucle centrale (point fixe sur Q)** : déclenchée par tout item prêt dans la file ; chaque résolution peut pousser de nouveaux items, mais chaque poussée porte une profondeur incrémentée ; termine parce que la profondeur est plafonnée et que les items « prêts » (dépendances satisfaites) finissent par s'épuiser.
- **Boucle de ré-ouverture post-assemblage** : `VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN` ou `VERIFIER_COUVERTURE_OBJECTIFS` peuvent repousser un item dans Q et rouvrir la boucle centrale ; bornée par un compteur global K (pas par phase, puisqu'il n'y a pas de phases) — au-delà, `CONSTATER_IMPOSSIBILITE`.
- **Boucle de reformulation** : `ATTAQUER_TOUT_LE_CHAMP` peut, une seule fois dans tout le run (flag dédié), pousser une décision de reformulation en tête de file — c'est la seule remontée « globale ».
- **Attente utilisateur** : toute question suspend son item précis (pas toute la file) ; les autres items indépendants continuent d'être traités pendant l'attente — propriété propre à cette architecture, absente de A.

### Fonctions appelées plusieurs fois
- Toute la section `INCONNUE`, `DECISION`, `RISQUE`, `ETAPE` du corps de boucle : appelée une fois par item de ce type, donc potentiellement des dizaines de fois (`MENER_VERIFICATION`, `QUALIFIER_VRAISEMBLANCE_RISQUE`, `DEFINIR_ATTENDU_OBSERVABLE`, etc.).
- `ATTAQUER_UNE_OPTION` : une fois par option, à chaque item DECISION traité.
- `QUALIFIER_ETAT_RESOLUTION` : appelée à la clôture de chaque item, quel que soit son type — c'est la fonction la plus rejouée de l'architecture, car elle sert de marqueur de fin de traitement uniforme.
- `SOUMETTRE_ARBITRAGE_UTILISATEUR` : à chaque point de préférence ou de résidu accepté rencontré, potentiellement plusieurs fois en parallèle.

### Ce qui est laissé de côté
- `PLACER_JALONS_CONSTAT` : une file de travail rend l'avancement visible par son propre état (items résolus / restants) ; poser des jalons narratifs séparés ferait doublon avec ce que le registre donne déjà.
- `REPERER_POINTS_ENGAGEMENT` : inclus tout de même en gouvernance, mais joue un rôle mineur — les points d'engagement sont déjà en grande partie visibles comme arêtes de dépendance dans le graphe de décisions.

### Bilan
**Bien** : colle naturellement à des tâches où les inconnues et décisions s'enchevêtrent (une inconnue en aval peut immédiatement rouvrir une décision en amont, sans détour par une phase) ; évite le travail à vide des phases non pertinentes ; parallélisation des enquêtes indépendantes native. **Mal** : plus difficile à auditer qu'un pipeline (l'ordre réel dépend de l'exécution, pas d'une structure fixe) ; le risque de « ping-pong » entre items est réel et repose entièrement sur la discipline de profondeur/compteur K pour ne pas déraper — un bug dans ce garde-fou est plus dangereux ici qu'en A.

---

---


# Architecture 09 — Cascade de passes contradictoires


**Principe** : on écrit d'abord un brouillon minimal et volontairement fragile, puis on le soumet à une série de passes d'attaque indépendantes (contenu → options → faits → risques → étapes → document), chacune convergeant localement par sa propre boucle bornée ; une passe qui invalide une passe antérieure y renvoie précisément, une seule fois par couple de passes.

### Pseudo-code

```
ÉTAPE 0 — ADMISSIBILITÉ
  LIRE_TECHNIQUES_AUTORISEES ; INVENTORIER_CAPACITES ; EVALUER_EXIGENCE_TACHE
  si non pertinent : DECLINER_SI_PAS_DE_PLAN ; FIN

ÉTAPE 1 — BROUILLON MINIMAL (un seul passage, non vérifié)
  SEPARER_DEMANDE_ET_BESOIN ; DELIMITER_PERIMETRE
  si point de départ = plan existant : AMORCER_DEPUIS_PLAN_EXISTANT
  FORMULER_CIBLE_OBSERVABLE ; ETABLIR_ETAT_ACTUEL ; CHAINER_ETAT_ACTUEL_VERS_CIBLE
  PRODUIRE_OPTIONS_DISTINCTES (une option "évidente" retenue provisoirement)
  RECENSER_INCONNUES (juste listées, pas levées)
  DERIVER_ACTIONS_DEPUIS_DECISIONS ; ORDONNER_PAR_PREREQUIS  (squelette grossier)

ÉTAPE 2 — CASCADE DE PASSES

  PASSE « CONTENU » (le problème est-il bien posé ?)
    répéter (max 2 tours) :
        CONTESTER_ENONCE_PROBLEME ; DETECTER_SOLUTION_IMPOSEE ; TRAQUER_AJOUTS_SILENCIEUX
        BALAYER_EXIGENCES_TACITES
           si exigence tacite significative : signaler à l'utilisateur (jamais imposer),
              FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER
        DETECTER_CONFLIT_OBJECTIFS
           si conflit : ORDONNER_OBJECTIFS_SANS_ECARTER ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre
        si rien de nouveau : sortir
        sinon : DELIMITER_PERIMETRE + FORMULER_CIBLE_OBSERVABLE révisés ; refaire un tour
    si tout casse : ATTAQUER_TOUT_LE_CHAMP → CONSTATER_IMPOSSIBILITE possible ; FIN

  PASSE « OPTIONS » (cœur adversarial)
    GARANTIR_DIVERSITE_METHODE ; CHERCHER_APPROCHES_NON_ENVISAGEES ; CHERCHER_ANTECEDENTS
    pour chaque option : EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
    ISOLER_LES_EVALUATIONS
    répéter (max 3 tours) :
        CHOISIR_ANGLES_ATTAQUE
        pour chaque option restante : ATTAQUER_UNE_OPTION
        ATTAQUER_TOUT_LE_CHAMP
        retirer les options qui meurent : CONSERVER_OPTIONS_ECARTEES
        si toutes meurent : 1 reprise via CHERCHER_APPROCHES_NON_ENVISAGEES, sinon CONSTATER_IMPOSSIBILITE
        si le champ entier casse et pas déjà rebondi vers PASSE CONTENU :
             rebondir vers PASSE CONTENU (1 seule fois) ; reprendre PASSE OPTIONS ensuite
        si plus rien ne casse : sortir
    ARBITRER_A_L_AVEUGLE ; QUALIFIER_INDEPENDANCE_OBTENUE ; DETECTER_ERREURS_CORRELEES
       si indépendance jugée insuffisante : ré-ISOLER_LES_EVALUATIONS + 1 tour d'attaque supplémentaire
    ORIENTER_CHOIX
       fait manquant : traité dans la PASSE FAITS suivante (dépendance en aval, pas de rebond ici)
       préférence    : PRESENTER_ALTERNATIVES_AU_CHOIX ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre
       vrai choix    : trancher ; DISTINGUER_CHOIX_ET_CONSEQUENCE ; QUALIFIER_PORTEE_DECISION
                       NOMMER_FAIT_QUI_FERAIT_BASCULER ; CONSIGNER_CE_QUI_A_TRANCHE

  PASSE « FAITS » (levée paresseuse — seulement ce dont l'option retenue a besoin)
    RECENSER_INCONNUES (recentré sur l'option retenue)
    CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION ; QUALIFIER_PORTEE_INCONNUE
    ORDONNER_INCONNUES_SANS_ECARTER
    tant que inconnue bloquante restante (nombre fini, décroît) :
        DISTINGUER_INDETERMINE_ET_NON_CHERCHE ; DECIDER_D_INTERROGER_UTILISATEUR
           oui : FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER
           non : CHOISIR_MOYEN_DE_LEVEE → MENER_VERIFICATION / agent
                 (DECIDER_D_OUVRIR_UN_AGENT ; REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT
                  INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION)
        CONSIGNER_PROVENANCE_FAIT ; JUGER_PEREMPTION_FAIT
           si périssable : INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
        DETECTER_CONTRADICTION_ENTRE_SOURCES ; DETECTER_ORIGINE_COMMUNE_SOURCES ; RESOUDRE_CONTRADICTION
        ENONCER_LIMITES_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE ; RENDRE_INCERTITUDE_VISIBLE
    si un fait levé invalide l'option retenue (et pas déjà rebondi) :
        rebondir vers PASSE OPTIONS (1 seule fois), option fautive marquée morte
    VERIFIER_ADOSSEMENT_AFFIRMATIONS (boucle locale bornée à 2 : réparer ou retirer)

  PASSE « RISQUES » (attaque de la solution retenue)
    RECENSER_RISQUES_PAR_ORIGINE
    QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT ; QUALIFIER_REVERSIBILITE
    QUALIFIER_TERRITOIRE ; ANTICIPER_TIERS_REACTIF
    STATUER_SUR_RISQUE_RESIDUEL
       si résidu non trivial : SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre

ÉTAPE 3 — CONSTRUCTION DÉTAILLÉE DES ÉTAPES (le brouillon a survécu, on l'écrit pour de vrai)
  DERIVER_ACTIONS_DEPUIS_DECISIONS (détaillé, remplace le squelette de l'Étape 1)
  ORDONNER_PAR_PREREQUIS ; IDENTIFIER_ETAPES_SIMULTANEES
  boucle (max 2) : VERIFIER_SIMULTANEITE_POSSIBLE → re-sérialiser si conflit
  pour chaque étape :
      DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE
      si mécanique : CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
      DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC ; DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE
  CONSTRUIRE_BRANCHE_CONDITIONNELLE
  CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
  RECENSER_INVARIANTS ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN
     si violation (et pas déjà rebondi) : rebondir vers PASSE OPTIONS ou FAITS selon l'origine (1 fois)
  AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE ; PREVOIR_SUITE_EN_CAS_DE_SUCCES

ÉTAPE 4 — PASSE « DOCUMENT » (attaque finale, tierce)
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION ; PLACER_POINTS_AUTORISATION
  DESIGNER_AUTORITE_AUTORISATION ; REPERER_POINTS_ENGAGEMENT ; VERIFIER_COUVERTURE_BLOQUANTS
  RECENSER_RESSOURCES_EXECUTION ; RECENSER_DEPENDANCES_EXTERNES ; VERIFIER_FAISABILITE_PAR_EXECUTANT
  PROPOSER_MARGES ; PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE
  REUTILISER_ACQUIS ; VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_COHERENCE_ENSEMBLE
  RATTACHER_TOUTE_PIECE_A_SON_ORIGINE ; ISOLER_LE_HORS_PLAN ; SIGNALER_LES_LIMITES
  QUALIFIER_ETAT_RESOLUTION (chaque point) ; CONSIGNER_CE_QUI_A_TRANCHE

  répéter (max 2 tours) :
      CONTROLER_CONTENU_FINAL
      FAIRE_CONTROLER_PAR_UN_TIERS → INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
      si le tiers casse une décision/un fait/un risque : rebondir précisément vers la passe visée
         (au plus 1 rebond par couple Document→X sur tout le run)
      sinon corriger localement ; si rien de neuf : sortir

  ELAGUER_LA_PROSE ; CONTROLER_INTEGRITE_DOCUMENT (boucle locale bornée à 2)
  RENDRE_ACTIONNABLE_PAR_AGENT
  REDIGER_PLAN ; REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER
  RESTITUER_EN_BREF
```

### Boucles

- **Boucle locale par passe** : chaque passe (Contenu, Options, Faits, Risques, Document) a sa propre convergence à point fixe, bornée à 2–3 tours ; elle boucle sur elle-même tant qu'elle trouve du nouveau, s'arrête dès qu'un tour ne révèle plus rien.
- **Boucle de rebond entre passes** : une passe avale peut invalider une passe amont (ex. la Passe FAITS tue l'option retenue) ; le rebond cible précisément cette passe, jamais « tout en arrière » ; chaque **couple** de passes ne peut rebondir qu'une fois — c'est le registre de flags qui garantit la terminaison (au pire, autant de rebonds que de couples de passes, un nombre fini et petit).
- **Boucle d'attente utilisateur** : suspend et reprend, jamais de valeur par défaut.
- **Garantie de terminaison globale** : produit du plafond de tours par passe (borné) et du nombre fini de couples de passes pouvant rebondir une fois chacun ; il n'existe aucun chemin où deux passes se renvoient indéfiniment la faute.

### Fonctions appelées plusieurs fois
- `ATTAQUER_UNE_OPTION`, `CHOISIR_ANGLES_ATTAQUE` : à chaque tour de la Passe Options, pour chaque option restante — c'est la fonction la plus sollicitée de cette architecture.
- `DERIVER_ACTIONS_DEPUIS_DECISIONS` : une première fois en brouillon (Étape 1), une seconde fois pour de vrai (Étape 3) — la différence entre brouillon et version finale est structurelle à cette architecture.
- `CONTROLER_CONTENU_FINAL` / `FAIRE_CONTROLER_PAR_UN_TIERS` : à chaque tour de la Passe Document.
- `MENER_VERIFICATION`, `CONSIGNER_PROVENANCE_FAIT` : une fois par inconnue levée dans la Passe Faits.
- `CONSTATER_IMPOSSIBILITE` : potentiellement testée à la fin de chaque passe (contenu, options), pas seulement à la fin du processus.

### Ce qui est laissé de côté
- `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` : cette architecture ne construit pas de graphe global de dépendances en amont — l'ordre émerge passe après passe (contenu avant options avant faits avant risques avant étapes), ce que la cascade elle-même impose déjà.
- `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` : fragmenter en sous-plans casserait la discipline de cascade (chaque sous-plan devrait repasser par toutes les passes séparément, ce qui n'a pas de sens tant que l'option n'est pas figée) ; le surdimensionnement se traite uniquement par `ELAGUER_ETAPES_INUTILES` / `CONTROLER_TAILLE_DES_ETAPES` en Étape 3.

### Bilan
**Bien** : détecte tôt et à moindre coût les problèmes mal posés ou les options fragiles, avant d'avoir investi dans la levée exhaustive des inconnues (la Passe Faits est paresseuse, contrairement à A) ; le mécanisme de rebond borné par couple de passes est un garde-fou de terminaison particulièrement solide et explicite. **Mal** : le brouillon initial volontairement sous-vérifié peut donner une fausse impression d'avancement rapide alors que l'essentiel du travail est dans les passes ; le suivi de « qui a rebondi vers qui » ajoute un état global à maintenir, plus difficile à expliquer simplement qu'un compteur de tours par phase.

---

---


# Architecture 10 — L'épreuve récursive (produire / attaquer / arbitrer, à toutes les échelles)


**Principe en une phrase :** un seul mécanisme épistémique — isoler puis attaquer puis arbitrer — est appliqué successivement et récursivement à l'énoncé du problème, à chaque fait convoqué, à chaque décision, puis au plan entier, au lieu de réserver le contradictoire à une seule étape "choix d'options".

### Pseudo-code

```
SOUS-PROCÉDURE EPROUVER(objet, nature) :
  ISOLER_LES_EVALUATIONS
  CHOISIR_ANGLES_ATTAQUE
  SI nature == "champ complet" : ATTAQUER_TOUT_LE_CHAMP
  SINON : ATTAQUER_UNE_OPTION
  QUALIFIER_INDEPENDANCE_OBTENUE
  SI plusieurs attaques convergent : DETECTER_ERREURS_CORRELEES
  RETOURNE (résiste | faille détectée)

NIVEAU 0 — Recevabilité (passage unique, pas de contradictoire nécessaire)
  LIRE_TECHNIQUES_AUTORISEES ; EVALUER_EXIGENCE_TACHE
  INVENTORIER_CAPACITES ; IDENTIFIER_DESTINATAIRE ; QUALIFIER_FORME_TRAVAIL
  SI non pertinent ALORS DECLINER_SI_PAS_DE_PLAN ; ARRÊT
  SEPARER_DEMANDE_ET_BESOIN ; DELIMITER_PERIMETRE

NIVEAU 1 — Éprouver l'énoncé lui-même
  CONTESTER_ENONCE_PROBLEME ; DETECTER_SOLUTION_IMPOSEE
  TRAQUER_AJOUTS_SILENCIEUX ; BALAYER_EXIGENCES_TACITES (chaque tacite → question, jamais imposée)
  reformulations := 0
  RÉPÉTER
    résultat := EPROUVER(énoncé courant, "champ complet")
    SI résultat == faille ET la faille est un vrai vice de formulation :
      SOUMETTRE_ARBITRAGE_UTILISATEUR (reformuler l'énoncé) ; ATTENDRE
      reformulations += 1
  JUSQU'À résultat == résiste OU reformulations == 2
  SI reformulations == 2 ET toujours en échec : CONSTATER_IMPOSSIBILITE ; ARRÊT
  FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
  ETABLIR_ETAT_ACTUEL ; CHAINER_ETAT_ACTUEL_VERS_CIBLE ; QUALIFIER_TERRITOIRE

NIVEAU 2 — Éprouver chaque fait convoqué
  RECENSER_INCONNUES ; POUR chacune : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION, QUALIFIER_PORTEE_INCONNUE
  POUR chaque inconnue bloquante :
    SI REUTILISER_ACQUIS ALORS continuer
    essais := 0 ; ETABLI := faux
    TANT QUE NON ETABLI ET essais < moyens disponibles :
      moyen := CHOISIR_MOYEN_DE_LEVEE
      exécuter moyen (MENER_VERIFICATION | LEVER_INCONNUE_PAR_ACTION_REVERSIBLE |
                       RESPECTER_CADRE_AUTORISE+DECIDER_D_OUVRIR_UN_AGENT+PARALLELISER_ENQUETE+
                       REDIGER_BRIEF_AGENT+BORNER_UN_AGENT+INTEGRER_RETOUR_AGENT+ARRETER_ORCHESTRATION |
                       DECIDER_D_INTERROGER_UTILISATEUR+FORMULER_QUESTION_ACTIONNABLE+SUSPENDRE_ENQUETE_ET_DEMANDER)
      CONSIGNER_PROVENANCE_FAIT ; ENONCER_LIMITES_FAIT ; JUGER_PEREMPTION_FAIT
      # le fait obtenu subit lui-même une épreuve avant d'être tenu pour acquis :
      REFUSER_AUTO_CONFIRMATION
      SI plusieurs sources :
        DETECTER_CONTRADICTION_ENTRE_SOURCES ; DETECTER_ORIGINE_COMMUNE_SOURCES
        SI contradiction ALORS RESOUDRE_CONTRADICTION
      SEPARER_OBSERVE_ET_SUPPOSE ; RENDRE_INCERTITUDE_VISIBLE
      ETABLI := (fait cohérent, source distincte, non périmé)
      essais += 1
    SI ETABLI : SI périssable ALORS INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
    SINON : DISTINGUER_INDETERMINE_ET_NON_CHERCHE
            SI bloque la cible ALORS CONSTATER_IMPOSSIBILITE ; remonter NIVEAU 1
            SINON reclasser en inconnue d'exécution (→ NIVEAU 4)

NIVEAU 3 — Éprouver les décisions (le cœur adversarial)
  ETABLIR_DEPENDANCES_ENTRE_DECISIONS
  POUR chaque décision, dans l'ordre :
    ORIENTER_CHOIX
    SI "fait manquant" : traiter cette seule inconnue au NIVEAU 2 ; revenir ici
    SI "préférence" : demander directement ; ATTENDRE
    SINON :
      PRODUIRE_OPTIONS_DISTINCTES ; GARANTIR_DIVERSITE_METHODE
      CHERCHER_APPROCHES_NON_ENVISAGEES ; CHERCHER_ANTECEDENTS
      POUR chaque option : EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
        SI hypothèse non levée ALORS la traiter comme inconnue au NIVEAU 2 ; revenir

      options_à_tester := options triées par AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE
      survivantes := []
      TANT QUE options_à_tester non vide :
        option := extraire la plus fragile en premier
        résultat := EPROUVER(option, "option unique")
        SI résultat == résiste : survivantes += option
        SINON SI la faille révèle un vice commun à toutes les options :
          résultat2 := EPROUVER(champ des options, "champ complet")   # ATTAQUER_TOUT_LE_CHAMP
          SI résultat2 == faille fondamentale : CONSTATER_IMPOSSIBILITE ; remonter NIVEAU 1

      ARBITRER_A_L_AVEUGLE sur survivantes
      SI compromis matériel : PRESENTER_ALTERNATIVES_AU_CHOIX ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
    DISTINGUER_CHOIX_ET_CONSEQUENCE
    CONSIGNER_CE_QUI_A_TRANCHE ; NOMMER_FAIT_QUI_FERAIT_BASCULER
    QUALIFIER_PORTEE_DECISION ; QUALIFIER_ETAT_RESOLUTION ; CONSERVER_OPTIONS_ECARTEES

NIVEAU 4 — Construction (passage unique — le contradictoire reviendra au niveau 5, sur l'objet fini)
  DERIVER_ACTIONS_DEPUIS_DECISIONS
  DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE → CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
  ORDONNER_PAR_PREREQUIS ; IDENTIFIER_ETAPES_SIMULTANEES → VERIFIER_SIMULTANEITE_POSSIBLE
  SI trop gros : DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER (chaque sous-plan traverse récursivement NIVEAUX 1-5)
  POUR chaque étape :
    DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC
    DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE (le retour arrière affirmé est lui-même mis à l'épreuve)
    QUALIFIER_REVERSIBILITE
  POUR chaque inconnue d'exécution résiduelle : CONSTRUIRE_BRANCHE_CONDITIONNELLE
  RATTACHER_TOUTE_PIECE_A_SON_ORIGINE
  TANT QUE NON CONTROLER_TAILLE_DES_ETAPES : ajuster
  ELAGUER_ETAPES_INUTILES

  RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT
  RECENSER_INVARIANTS
  TANT QUE NON VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN : corriger ici, ou si le vice est décisionnel, remonter NIVEAU 3
  ANTICIPER_TIERS_REACTIF ; STATUER_SUR_RISQUE_RESIDUEL
  RECENSER_RESSOURCES_EXECUTION ; RECENSER_DEPENDANCES_EXTERNES ; VERIFIER_FAISABILITE_PAR_EXECUTANT
  REPERER_POINTS_ENGAGEMENT ; PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION
  TANT QUE NON VERIFIER_COUVERTURE_BLOQUANTS : ajouter
  PROPOSER_AFFECTATION ; PROPOSER_MARGES ; PROPOSER_CHIFFRAGE
  PREVOIR_SUITE_EN_CAS_DE_SUCCES ; SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN

NIVEAU 5 — Éprouver le plan entier
  REDIGER_PLAN ; RENDRE_ACTIONNABLE_PAR_AGENT ; ELAGUER_LA_PROSE
  REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER
  VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_COHERENCE_ENSEMBLE
  VERIFIER_ADOSSEMENT_AFFIRMATIONS ; REFUSER_AUTO_CONFIRMATION
  RENDRE_INCERTITUDE_VISIBLE ; SEPARER_OBSERVE_ET_SUPPOSE
  CONTROLER_INTEGRITE_DOCUMENT ; CONTROLER_CONTENU_FINAL

  tours := 0
  RÉPÉTER
    FAIRE_CONTROLER_PAR_UN_TIERS               # un contexte qui n'a pas écrit le plan l'attaque
    INTEGRER_RETOUR_AGENT
    REFUSER_AUTO_CONFIRMATION                  # le retour du tiers n'est pas pris pour argent comptant
    VERIFIER_ADOSSEMENT_AFFIRMATIONS(retour du tiers)
    SI le tiers relève une faille :
      SELON nature(faille) :
        "fait douteux"        → traiter au NIVEAU 2, revenir ici
        "décision mal fondée" → traiter au NIVEAU 3, revenir ici
        "étape mal formée"    → traiter au NIVEAU 4, revenir ici
        "incohérence rédaction" → corriger ici même
      tours += 1
  JUSQU'À (aucune faille) OU (tours == 3)
  SI tours == 3 et faille persiste : SIGNALER_LES_LIMITES sur le point litigieux plutôt que reboucler
  RESTITUER_EN_BREF
```

### Les boucles

- **La sous-procédure `EPROUVER`** est le nœud de bouclage universel : elle n'appartient à aucun niveau en propre, elle est invoquée par tous. C'est la différence structurante avec les autres approches — ici il n'y a pas "une boucle de vérification des options" et "une boucle de contrôle final" séparées, c'est la même mécanique.
- **Boucle NIVEAU 1 (reformulation de l'énoncé)** : déclenchée si `ATTAQUER_TOUT_LE_CHAMP` révèle un vice de formulation. Bornée à 2 reformulations, puis `CONSTATER_IMPOSSIBILITE`. C'est la remontée la plus haute possible — un échec ici invalide tout le reste, donc rien en aval n'a encore été construit à ce stade (peu coûteux).
- **Boucle NIVEAU 2 (épreuve de chaque fait)** : locale à l'inconnue, épuise les moyens de levée puis conclut. Peut faire remonter jusqu'au NIVEAU 1 seulement si le fait manquant bloque la cible elle-même — sinon elle reste confinée.
- **Boucle NIVEAU 3 (épreuve de chaque option)** : teste les options de la plus fragile à la plus solide (`AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE`) — termine dès qu'une option survit ou que le champ entier est vidé. Une faille "de champ" peut remonter au NIVEAU 1 (problème mal posé), une faille "de fait" redescend au NIVEAU 2. Bornée par le nombre fini d'options.
- **Boucle NIVEAU 4 (invariants)** : identique en principe à une autre approche, mais peut remonter jusqu'au NIVEAU 3 si le défaut d'invariant révèle qu'une décision entière doit être reconsidérée, pas seulement une étape.
- **Boucle NIVEAU 5 (épreuve du plan entier par un tiers)** : la plus intéressante — c'est littéralement `EPROUVER` appliqué à l'objet final, avec `FAIRE_CONTROLER_PAR_UN_TIERS` en rôle d'attaquant. Route précisément vers le niveau d'origine de la faille. Bornée à 3 tours, avec `SIGNALER_LES_LIMITES` comme sortie garantie en dernier recours — ce qui assure la terminaison même si le tiers continue de trouver des défauts mineurs indéfiniment discutables.
- **Terminaison globale garantie** par trois mécanismes cumulés : compteurs bornés à chaque niveau, `CONSTATER_IMPOSSIBILITE` comme état absorbant en cas de vice réel, et le fait que toute remontée "consomme" l'information qui l'a causée (un fait une fois établi ne redevient pas manquant, une option une fois écartée reste dans `CONSERVER_OPTIONS_ECARTEES` et n'est pas retestée).

### Fonctions appelées plusieurs fois

`ATTAQUER_UNE_OPTION`, `CHOISIR_ANGLES_ATTAQUE`, `ISOLER_LES_EVALUATIONS`, `QUALIFIER_INDEPENDANCE_OBTENUE` — à chaque appel de `EPROUVER`, donc potentiellement des dizaines de fois (une fois par option, plus une fois pour le plan entier). `REFUSER_AUTO_CONFIRMATION` — appliquée deux fois avec un sens différent à chaque fois : une fois par fait établi (NIVEAU 2) *et* une fois sur le retour du tiers lui-même (NIVEAU 5), ce qui est un usage particulièrement révélateur du principe "rien n'est acquis du seul fait qu'un agent l'affirme". `CONSTATER_IMPOSSIBILITE` — invocable à trois niveaux distincts (1, 2, 3) avec des conséquences différentes. `CHOISIR_MOYEN_DE_LEVEE`, `MENER_VERIFICATION`, `CONSIGNER_PROVENANCE_FAIT` — une fois par fait. `EPROUVER_RETOUR_ARRIERE` — une fois par étape, elle-même une mini-épreuve du même type. `FAIRE_CONTROLER_PAR_UN_TIERS` — jusqu'à 3 fois au NIVEAU 5.

### Ce qu'elle laisse de côté

- `ORDONNER_INCONNUES_SANS_ECARTER` : cette architecture ne construit pas de file de priorité globale — les inconnues sont traitées au fil du NIVEAU 2 dans l'ordre où elles bloquent la construction, pas selon un classement coût/impact explicite ; ce mécanisme de priorisation est le cœur de une autre approche, pas de celle-ci.

### Forces et faiblesses

**Fait bien :** c'est particulièrement rigoureuse — rien n'entre dans le plan final (fait, option, ou plan lui-même) sans avoir subi une tentative sincère de le faire échouer, avec isolement et indépendance vérifiée. Très adaptée aux décisions à fort enjeu, irréversibles, ou pour lesquelles une erreur serait coûteuse à découvrir à l'exécution.
**Fait mal :** coûteuse et potentiellement disproportionnée pour une tâche simple — d'où la nécessité réelle d'`EVALUER_EXIGENCE_TACHE` en amont pour ne pas déployer tout l'appareil contradictoire sur un problème trivial. La récursivité (surtout via `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER`, chaque sous-plan retraversant les 5 niveaux) peut devenir difficile à borner en pratique si le découpage produit lui-même des sous-plans nombreux ; elle demande une discipline stricte sur les compteurs de tours pour ne pas devenir, malgré les garde-fous théoriques, extrêmement longue à dérouler.

---


# Architecture 11 — L'arbre d'enquête

<details><summary>Briques utilisées</summary>

```
FONCTION PROLOGUE_CADRAGE(demande):
    LIRE_TECHNIQUES_AUTORISEES()
    INVENTORIER_CAPACITES()
    IDENTIFIER_DESTINATAIRE()
    SEPARER_DEMANDE_ET_BESOIN(demande)
    CONTESTER_ENONCE_PROBLEME()
    SI DETECTER_SOLUTION_IMPOSEE(): reformuler comme problème, pas comme solution imposée
    SI DECLINER_SI_PAS_DE_PLAN(): retourner "pas de planification ici", FIN
    SI un plan existant est fourni: AMORCER_DEPUIS_PLAN_EXISTANT()
    ETABLIR_ETAT_ACTUEL()
    CHERCHER_ANTECEDENTS()
    FORMULER_CIBLE_OBSERVABLE()
    VERIFIER_FIDELITE_CIBLE_BESOIN()
    TRAQUER_AJOUTS_SILENCIEUX()
    DEFINIR_CRITERES_ACCEPTATION()
    RECENSER_CONTRAINTES_DURES()
    RECENSER_OBLIGATIONS_FORMELLES()
    RECENSER_PREFERENCES()
    BALAYER_EXIGENCES_TACITES()
    DEBUSQUER_HYPOTHESES_IMPORTEES()
    EXPOSER_EXTERNALITES_CERTAINES()
    RECENSER_DEPENDANCES_EXTERNES()
    RECENSER_RESSOURCES_EXECUTION()
    DELIMITER_PERIMETRE()
    retourner périmètre_racine, état_partagé{faits:[], décisions:[], risques:[]}

FONCTION EPILOGUE_CLOTURE(état_partagé, plan):
    RENDRE_ACTIONNABLE_PAR_AGENT(plan)
    VERIFIER_COHERENCE_ENSEMBLE(plan)
    VERIFIER_COUVERTURE_OBJECTIFS(plan)
    VERIFIER_COUVERTURE_BLOQUANTS(plan)
    VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(plan)
    VERIFIER_FAISABILITE_PAR_EXECUTANT(plan)
    VERIFIER_ADOSSEMENT_AFFIRMATIONS(état_partagé)
    ELAGUER_ETAPES_INUTILES(plan)
    ELAGUER_LA_PROSE(plan)
    ISOLER_LE_HORS_PLAN(plan)
    SIGNALER_LES_LIMITES(plan)
    PREVOIR_SUITE_EN_CAS_DE_SUCCES(plan)
    PROPOSER_MARGES() ; PROPOSER_AFFECTATION() ; PROPOSER_CHIFFRAGE()
    CONTROLER_CONTENU_FINAL(plan)
    CONTROLER_INTEGRITE_DOCUMENT(plan)
    avis = FAIRE_CONTROLER_PAR_UN_TIERS(plan)
    TANT QUE avis signale une faille ET passes < 2:
        corriger localement la partie visée ; avis = FAIRE_CONTROLER_PAR_UN_TIERS(plan) ; passes += 1
    SI faille persistante: QUALIFIER_ETAT_RESOLUTION(point) = "non résolu" ; SIGNALER_LES_LIMITES(point)
    PLACER_ET_NOMMER_LE_FICHIER()
    REDIGER_PLAN(plan)
    REDIGER_TRACABILITE_SEPAREE(état_partagé)
    RESTITUER_EN_BREF()
```

---

</details>


**Principe** : on ne découpe pas le problème mais l'incertitude — chaque poche d'inconnues assez grosse et assez indépendante ouvre sa propre branche d'enquête (éventuellement un sous-agent) ; la récursion ne produit **pas** directement des morceaux de plan mais une base de faits et de décisions validée, assemblée en plan **une seule fois, à plat**, à la fin.

**Les 6 choix de conception**
- **Déclencheur de coupe** : après `RECENSER_INCONNUES`/`QUALIFIER_PORTEE_INCONNUE`, si les inconnues bloquantes se répartissent sur plusieurs domaines hétérogènes et que le territoire est « reconfigurant » (`QUALIFIER_TERRITOIRE`).
- **Découpe** : un sous-périmètre par domaine d'enquête ; `DECIDER_D_OUVRIR_UN_AGENT` choisit entre sous-agent parallèle ou traitement local.
- **Effort par profondeur** : à la racine, `CHOISIR_MOYEN_DE_LEVEE` privilégie des moyens larges ; en profondeur, `REDIGER_BRIEF_AGENT` + `BORNER_UN_AGENT` réduisent le périmètre à une question précise et un budget serré — l'effort décroît structurellement avec la profondeur.
- **Recomposition** : pas un merge de plans mais une fusion de connaissances — `INTEGRER_RETOUR_AGENT`, résolution des contradictions, puis un unique passage d'assemblage du plan.
- **Dépendances entre frères** : `ISOLER_LES_EVALUATIONS` empêche la contamination pendant que les enquêtes tournent ; à la remontée, `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` vérifie qu'aucune branche ne s'est reposée tacitement sur l'hypothèse d'une autre.
- **Borne de profondeur** : `ARRETER_ORCHESTRATION` (un agent de plus ne changerait rien) + `RESPECTER_CADRE_AUTORISE` (plafond de sous-agents fixé par la config) + `DISTINGUER_INDETERMINE_ET_NON_CHERCHE` pour ne pas ouvrir de branche sur de l'indéterminable.

```
FONCTION CYCLE_B(périmètre, profondeur, état_partagé):
    RECENSER_INCONNUES(périmètre)
    inconnues = ORDONNER_INCONNUES_SANS_ECARTER(...)
    POUR chaque inc DANS inconnues:
        CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION(inc) ; QUALIFIER_PORTEE_INCONNUE(inc)
    bloquantes = [i pour i dans inconnues SI i.classe == "construction"]

    territoire = QUALIFIER_TERRITOIRE(périmètre)
    domaines = regrouper(bloquantes, par=domaine_enquête)

    SI profondeur < PROFONDEUR_MAX ET len(domaines) > 1 ET territoire == "reconfigurant":
        résultats = []
        POUR chaque domaine DANS domaines:
            SI DECIDER_D_OUVRIR_UN_AGENT(domaine):
                brief = REDIGER_BRIEF_AGENT(domaine, faits_déjà_établis=état_partagé.faits)
                BORNER_UN_AGENT(brief)
                retour = PARALLELISER_ENQUETE(brief)          # agents en parallèle, un par domaine
                ISOLER_LES_EVALUATIONS(retour)
                résultats.ajouter( INTEGRER_RETOUR_AGENT(retour) )
            SINON:
                sp = DELIMITER_PERIMETRE(domaine, hérite=périmètre)
                résultats.ajouter( CYCLE_B(sp, profondeur+1, REUTILISER_ACQUIS(état_partagé)) )

        POUR chaque paire de faits issus de résultats différents:            # BOUCLE DE CONTRADICTION
            SI DETECTER_CONTRADICTION_ENTRE_SOURCES(paire):
                SI DETECTER_ORIGINE_COMMUNE_SOURCES(paire): dévaluer à une seule source
                SI NON RESOUDRE_CONTRADICTION(paire):
                    marquer "contesté" ; état_partagé.inconnues_à_traiter_au_dessus.ajouter(paire)  # ESCALADE

        POUR chaque fait retenu:
            REFUSER_AUTO_CONFIRMATION(fait) ; SEPARER_OBSERVE_ET_SUPPOSE(fait)
            SI JUGER_PEREMPTION_FAIT(fait) == "périssable":
                INSCRIRE_REVERIFICATION_FAIT_PERISSABLE(fait, étape_dépendante)
            ENONCER_LIMITES_FAIT(fait) ; état_partagé.faits.ajouter(fait)

        ETABLIR_DEPENDANCES_ENTRE_DECISIONS(décisions(résultats))   # une branche a-t-elle présupposé l'autre ?
        SI ARRETER_ORCHESTRATION(résultats): ne pas creuser davantage

    SINON:
        POUR chaque inc DANS bloquantes:
            tentative = 0
            REPETER:                                                          # BOUCLE D'ENQUETE
                moyen = CHOISIR_MOYEN_DE_LEVEE(inc)   # respecte RESPECTER_CADRE_AUTORISE
                SI moyen == "question" ET DECIDER_D_INTERROGER_UTILISATEUR(inc):
                    q = FORMULER_QUESTION_ACTIONNABLE(inc)
                    résultat = SUSPENDRE_ENQUETE_ET_DEMANDER(q)   # attend la réponse, jamais de défaut
                SINON:
                    résultat = MENER_VERIFICATION(moyen) OU LEVER_INCONNUE_PAR_ACTION_REVERSIBLE(moyen)
                RENDRE_INCERTITUDE_VISIBLE(résultat) ; tentative += 1
            TANT QUE résultat.échec ET tentative < 2 ET DISTINGUER_INDETERMINE_ET_NON_CHERCHE(inc)=="à chercher encore"

            SI résultat.échec:
                SI QUALIFIER_PORTEE_INCONNUE(inc) déborde le périmètre:
                    état_partagé.inconnues_à_traiter_au_dessus.ajouter(inc)   # ESCALADE
                SINON:
                    SUSPENDRE_ENQUETE_ET_DEMANDER(FORMULER_QUESTION_ACTIONNABLE(inc))
            SINON:
                CONSIGNER_PROVENANCE_FAIT(résultat) ; état_partagé.faits.ajouter(résultat)

    VERIFIER_ADOSSEMENT_AFFIRMATIONS(état_partagé)
    retourner état_partagé enrichi

# Une fois la racine de CYCLE_B terminée : un seul passage d'assemblage, à plat
FONCTION ASSEMBLER_PLAN(état_partagé):
    POUR chaque décision restante: TRANCHER_DECISION(décision, état_partagé)   # même bloc que dans A
    CHAINER_ETAT_ACTUEL_VERS_CIBLE(périmètre_racine)
    actions = DERIVER_ACTIONS_DEPUIS_DECISIONS(état_partagé.décisions)
    actions = ORDONNER_PAR_PREREQUIS(actions)
    POUR chaque pas: DEFINIR_ATTENDU_OBSERVABLE(pas) ; DEFINIR_SIGNAUX_ECHEC(pas) ; DEFINIR_RETOUR_ARRIERE(pas)
    RECENSER_INVARIANTS(périmètre_racine)
    PLACER_POINTS_VERIFICATION(actions) ; PLACER_POINTS_AUTORISATION(actions)
    retourner CONTROLER_TAILLE_DES_ETAPES(actions)
```

**3. Boucles**
- *Boucle d'enquête* : moyen de levée échoue → nouveau moyen, bornée à 2 tentatives, puis soit escalade (portée débordante) soit question utilisateur bloquante (`SUSPENDRE_ENQUETE_ET_DEMANDER`, qui *attend* — pas de valeur par défaut).
- *Boucle de contradiction* : `DETECTER_CONTRADICTION_ENTRE_SOURCES` → `RESOUDRE_CONTRADICTION` ; en cas d'échec, pas de nouvelle tentative sur la même méthode — l'inconnue est requalifiée et remontée.
- *Boucle de péremption* : différée plutôt qu'immédiate — un fait périssable devient une action de revérification inscrite dans le plan, pas une re-boucle sur place.

**4. Fonctions appelées plusieurs fois** : `RECENSER_INCONNUES`/`QUALIFIER_PORTEE_INCONNUE` (à chaque nœud), `CHOISIR_MOYEN_DE_LEVEE` (par inconnue, potentiellement plusieurs fois), `MENER_VERIFICATION`, `CONSIGNER_PROVENANCE_FAIT`, `REFUSER_AUTO_CONFIRMATION`, `REDIGER_BRIEF_AGENT`/`BORNER_UN_AGENT`/`INTEGRER_RETOUR_AGENT` (à chaque sous-agent), `DECIDER_D_OUVRIR_UN_AGENT`/`ARRETER_ORCHESTRATION` (à chaque nœud, pour juger de continuer) — parce que la valeur de cette architecture est justement de traiter l'incertitude par petites doses répétées, jamais en un seul passage.

**5. Forces / faiblesses** : Excellente pour des besoins où le risque principal est factuel (faisabilité, dépendances externes, technique) et où le parallélisme des agents apporte une vraie valeur ; discipline anti-hallucination forte (contradictions, provenance, péremption). Faible pour structurer l'exécution elle-même : le plan est dérivé après coup, en un seul passage plat, donc moins naturellement traçable objectif-par-objectif que A ; risque de sur-enquêter si `ARRETER_ORCHESTRATION` est mal calibré.

---

---


# Architecture 12 — Spirale incrémentale (squelette puis épaississement)


**Principe** : écrire d'abord un plan complet mais délibérément mince (un seul chemin, sans branches ni détail de risque), le faire tenir debout, puis l'épaissir passe après passe (inconnues, options, robustesse, gouvernance, prose) — chaque passe touche tout le plan mais à une profondeur croissante, avec une porte de vérification avant de passer à la suivante.

### Pseudo-code

```
# --- Passe 0 : recevabilité ------------------------------------------------
LIRE_TECHNIQUES_AUTORISEES(); EVALUER_EXIGENCE_TACHE()
IDENTIFIER_DESTINATAIRE(); DELIMITER_PERIMETRE()
besoin = SEPARER_DEMANDE_ET_BESOIN()
REPEAT au plus 1 fois:
    SI DETECTER_SOLUTION_IMPOSEE() OU CONTESTER_ENONCE_PROBLEME().reformule:
        besoin = SEPARER_DEMANDE_ET_BESOIN()
SI QUALIFIER_FORME_TRAVAIL() != "planification":
    DECLINER_SI_PAS_DE_PLAN(); STOP
AMORCER_DEPUIS_PLAN_EXISTANT()   # si applicable

# --- Passe 1 : le squelette (chemin unique, mince) --------------------------
etat = ETABLIR_ETAT_ACTUEL()
REPEAT:
    cible = FORMULER_CIBLE_OBSERVABLE(besoin)
UNTIL VERIFIER_FIDELITE_CIBLE_BESOIN(cible, besoin)          # boucle 1
DEFINIR_CRITERES_ACCEPTATION(cible)

territoire = QUALIFIER_TERRITOIRE(etat, cible)   # familier -> chemin simple ; sinon -> marquer les points à approfondir
squelette = CHAINER_ETAT_ACTUEL_VERS_CIBLE(etat, cible)
options_evidentes = PRODUIRE_OPTIONS_DISTINCTES(squelette)   # un seul passage, léger
SI une option domine clairement: squelette = option_dominante
SINON: marquer_point_a_approfondir(squelette, "choix différé")

squelette = ORDONNER_PAR_PREREQUIS(squelette)
DERIVER_ACTIONS_DEPUIS_DECISIONS(squelette)
FOR etape in squelette: DEFINIR_ATTENDU_OBSERVABLE(etape)

REPEAT au plus 2 fois:                                        # PORTE 1 (boucle 2)
    tient = VERIFIER_COHERENCE_ENSEMBLE(squelette)
    SI NON tient: squelette = CHAINER_ETAT_ACTUEL_VERS_CIBLE(etat, cible)  # reforme le chemin
UNTIL tient
SI NON tient: CONSTATER_IMPOSSIBILITE(); STOP

# --- Passe 2 : lever ce qui bloquerait l'écriture ----------------------------
FOR etape in squelette:                                       # boucle 3 (par étape)
    inconnues = RECENSER_INCONNUES(etape)
    FOR i in inconnues:
        i.classe = CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION(i)
        SI i.classe != "construction": CONTINUE
        i.portee = QUALIFIER_PORTEE_INCONNUE(i)
        i.nature = DISTINGUER_INDETERMINE_ET_NON_CHERCHE(i)
        i = dans ORDONNER_INCONNUES_SANS_ECARTER(inconnues)
        REPEAT au plus 2 fois:                                # boucle 4 (levée d'une inconnue)
            moyen = CHOISIR_MOYEN_DE_LEVEE(i)
            SWITCH moyen:
                CASE "agent":
                    SI ARRETER_ORCHESTRATION(ctx): SKIP
                    SI PARALLELISER_ENQUETE applicable:
                        agents = ouvrir_un_agent_par_domaine()
                    SINON:
                        DECIDER_D_OUVRIR_UN_AGENT(i)
                    REDIGER_BRIEF_AGENT(); BORNER_UN_AGENT(); RESPECTER_CADRE_AUTORISE()
                    fait = INTEGRER_RETOUR_AGENT(reponse_agent)
                CASE "question":
                    q = FORMULER_QUESTION_ACTIONNABLE(i)
                    SUSPENDRE_ENQUETE_ET_DEMANDER(q)           # bloquant
                    fait = reponse_utilisateur
                DEFAULT:
                    fait = MENER_VERIFICATION(i)  # ou CHERCHER_ANTECEDENTS(i)
            SI fait: BREAK
        UNTIL fait établi
        CONSIGNER_PROVENANCE_FAIT(fait); SEPARER_OBSERVE_ET_SUPPOSE(fait); ENONCER_LIMITES_FAIT(fait)
        SI JUGER_PEREMPTION_FAIT(fait) == "périssable":
            INSCRIRE_REVERIFICATION_FAIT_PERISSABLE(fait, etape)
        SI conflit avec fait existant:
            DETECTER_CONTRADICTION_ENTRE_SOURCES(); DETECTER_ORIGINE_COMMUNE_SOURCES()
            RESOUDRE_CONTRADICTION()

REPEAT au plus 2 fois:                                        # PORTE 2 (boucle 5)
    ok = VERIFIER_ADOSSEMENT_AFFIRMATIONS(squelette) ET NON REFUSER_AUTO_CONFIRMATION().declenche
    DETECTER_ERREURS_CORRELEES(faits_nouveaux)
UNTIL ok
SI NON ok: SUSPENDRE_ENQUETE_ET_DEMANDER()

# --- Passe 3 : épaississement (options, branches, attaques ciblées) ---------
FOR point in squelette où territoire == "reconfigure" OU marque == "choix différé":  # boucle 6
    options = PRODUIRE_OPTIONS_DISTINCTES(point)
    options = GARANTIR_DIVERSITE_METHODE(options)
    CHERCHER_APPROCHES_NON_ENVISAGEES(options)
    FOR o in options:
        EXIGER_HYPOTHESES_EXPLICITES(o); DEBUSQUER_HYPOTHESES_IMPORTEES(o)
    options = AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE(options)
    ISOLER_LES_EVALUATIONS(options)
    FOR o in options:
        ATTAQUER_UNE_OPTION(o, CHOISIR_ANGLES_ATTAQUE(o))
    decision = ORIENTER_CHOIX(options)
    SWITCH decision.nature:
        CASE "preference": PRESENTER_ALTERNATIVES_AU_CHOIX(options); SOUMETTRE_ARBITRAGE_UTILISATEUR(options)  # bloquant
        CASE "vrai choix": gagnant = decision.choix
    CONSERVER_OPTIONS_ECARTEES(options, gagnant)
    QUALIFIER_PORTEE_DECISION(gagnant); NOMMER_FAIT_QUI_FERAIT_BASCULER(gagnant)
    CONSIGNER_CE_QUI_A_TRANCHE(gagnant); QUALIFIER_ETAT_RESOLUTION(gagnant)
    SI un dauphin reste valable: CONSTRUIRE_BRANCHE_CONDITIONNELLE(point, dauphin)
    DISTINGUER_CHOIX_ET_CONSEQUENCE(point)
    DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE(point)
    CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE(point)
    remplacer(squelette, point, gagnant)

DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(branches_trop_grosses)
simultanees = IDENTIFIER_ETAPES_SIMULTANEES(squelette)
FOR paire in simultanees:
    SI NON VERIFIER_SIMULTANEITE_POSSIBLE(paire): retirer(paire)

REPEAT au plus 1 fois (globale) :                              # PORTE 3 (boucle 7)
    tient = VERIFIER_COHERENCE_ENSEMBLE(squelette)
    echec_champ = ATTAQUER_TOUT_LE_CHAMP(squelette)             # cherche ce qui tuerait tout
    SI echec_champ:
        CONSTATER_IMPOSSIBILITE() OU retour complet à Passe 0 (reformuler l'énoncé)
UNTIL tient ET NON echec_champ

# --- Passe 4 : robustesse ----------------------------------------------------
FOR etape in squelette:
    DEFINIR_SIGNAUX_ECHEC(etape)
    ra = DEFINIR_RETOUR_ARRIERE(etape)
    REPEAT au plus 2 fois: verifie = EPROUVER_RETOUR_ARRIERE(ra)  # boucle 8
    UNTIL verifie OR épuisé
    SI NON verifie: ra = "n'existe pas (non vérifié)"

risques = RECENSER_RISQUES_PAR_ORIGINE(squelette)
FOR r in risques: QUALIFIER_VRAISEMBLANCE_RISQUE(r); QUALIFIER_RAYON_IMPACT(r)
QUALIFIER_REVERSIBILITE(squelette); REPERER_POINTS_ENGAGEMENT(squelette)
ANTICIPER_TIERS_REACTIF(squelette)
invariants = RECENSER_INVARIANTS()

REPEAT au plus 2 fois:                                         # PORTE 4 (boucle 9)
    ok = VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(squelette, invariants)
    SI NON ok: retour ciblé à Passe 3 pour le chemin fautif (nouvelle branche/étape)
UNTIL ok
FOR r in risques: STATUER_SUR_RISQUE_RESIDUEL(r)

# --- Passe 5 : gouvernance et exécutabilité ----------------------------------
DESIGNER_AUTORITE_AUTORISATION(); PLACER_POINTS_AUTORISATION(squelette)
PLACER_JALONS_CONSTAT(squelette); PLACER_POINTS_VERIFICATION(squelette)
REPEAT: ok = VERIFIER_COUVERTURE_BLOQUANTS(squelette); SI NON ok: ajouter_point()
UNTIL ok                                                        # boucle 10
RECENSER_DEPENDANCES_EXTERNES(); ressources = RECENSER_RESSOURCES_EXECUTION()

REPEAT au plus 2 fois:                                         # boucle 11
    faisable = VERIFIER_FAISABILITE_PAR_EXECUTANT(squelette, ressources)
    SI NON faisable:
        SI options_ecartees dispo pour le point fautif:
            reprendre_dauphin(point_fautif)   # retour ciblé Passe 3
        SINON:
            SIGNALER_LES_LIMITES()
UNTIL faisable OR épuisé
PROPOSER_MARGES(); PROPOSER_AFFECTATION(); PROPOSER_CHIFFRAGE()
REPEAT: ok = CONTROLER_TAILLE_DES_ETAPES(squelette); SI NON ok: ajuster()
UNTIL ok                                                        # boucle 12

# --- Passe 6 : toilettage et vérité globale ----------------------------------
ELAGUER_ETAPES_INUTILES(squelette); ISOLER_LE_HORS_PLAN(); SIGNALER_LES_LIMITES()
RATTACHER_TOUTE_PIECE_A_SON_ORIGINE(squelette)
REPEAT au plus 1 fois:                                          # boucle 13
    ok = VERIFIER_COUVERTURE_OBJECTIFS(objectifs, squelette)
    SI NON ok: retour ciblé à Passe 3 pour couvrir l'objectif manquant
UNTIL ok
RENDRE_INCERTITUDE_VISIBLE(); PREVOIR_SUITE_EN_CAS_DE_SUCCES()

# --- Passe 7 : contrôle final par un tiers -----------------------------------
avis = FAIRE_CONTROLER_PAR_UN_TIERS(squelette)
INTEGRER_RETOUR_AGENT(avis)
DETECTER_ERREURS_CORRELEES(avis, controles_precedents)
REPEAT au plus 2 fois:                                          # boucle 14 (PORTE finale)
    ok = CONTROLER_CONTENU_FINAL() ET CONTROLER_INTEGRITE_DOCUMENT() ET VERIFIER_COHERENCE_ENSEMBLE(squelette)
    SI NON ok: router_vers_la_passe_responsable(probleme)   # chaque passe rouvrable une fois depuis ce gate
UNTIL ok
SI NON ok: SUSPENDRE_ENQUETE_ET_DEMANDER()

ELAGUER_LA_PROSE(); RENDRE_ACTIONNABLE_PAR_AGENT()
REDIGER_PLAN(); REDIGER_TRACABILITE_SEPAREE()
PLACER_ET_NOMMER_LE_FICHIER(); RESTITUER_EN_BREF()
```

### Les boucles

- **Boucle 1** : fidélité cible/besoin — comme dans les autres approches.
- **Porte 1 (boucle 2)** : le squelette doit tenir structurellement avant même d'avoir des faits — sinon on reforme le chemin ; bornée à 2 essais puis `CONSTATER_IMPOSSIBILITE`.
- **Boucle 3/4** : par étape puis par inconnue — remontent seulement à l'intérieur de l'étape concernée ; bornées à 2 tentatives par inconnue.
- **Porte 2 (boucle 5)** : contrôle de l'adossement des faits fraîchement collectés ; remonte au choix du moyen de levée (boucle 4) si un fait échoue ; bornée à 2 passes.
- **Boucle 6** : épaississement point par point — seulement sur les points marqués « à approfondir » ou « territoire reconfigurant », pas sur tout le squelette.
- **Porte 3 (boucle 7)** : la seule boucle autorisée à remonter jusqu'à la Passe 0 (reformulation de l'énoncé), déclenchée par `ATTAQUER_TOUT_LE_CHAMP` — bornée à une seule fois, ce qui l'empêche de devenir un cycle.
- **Boucle 8** (retours arrière) et **porte 4 / boucle 9** (invariants) : la boucle 9, en cas de violation, ne revient pas à la Passe 4 elle-même mais à la Passe 3, ciblée sur le chemin fautif — bornée à 2 passes.
- **Boucles 10 à 13** : vérifications de gouvernance et de couverture, chacune corrige localement et se termine dès validation ; la boucle 11 (faisabilité) repêche un dauphin déjà connu avant d'abandonner, ce qui la borne au nombre d'options produites en Passe 3.
- **Boucle 14 (porte finale)** : dispatch vers la passe responsable de chaque défaut détecté par le tiers ; chaque passe n'est rouvrable qu'une fois depuis cette porte, garantissant la terminaison.

Terminaison garantie par : la structure en passes strictement ordonnées (on ne revient jamais « en avant », seulement en arrière d'un nombre borné de passes), combinée aux bornes numériques sur chaque boucle locale.

### Fonctions appelées plusieurs fois

- `VERIFIER_COHERENCE_ENSEMBLE` : aux portes 1, 3 et 14 — le même contrôle réappliqué à un objet de plus en plus épais.
- `CHOISIR_MOYEN_DE_LEVEE` / `MENER_VERIFICATION` : par inconnue, potentiellement plusieurs fois par inconnue si le premier moyen échoue.
- `PRODUIRE_OPTIONS_DISTINCTES` : une fois légèrement en Passe 1 (pour le squelette), puis à nouveau, en profondeur, pour chaque point épaissi en Passe 3.
- `VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN`, `VERIFIER_FAISABILITE_PAR_EXECUTANT`, `VERIFIER_COUVERTURE_BLOQUANTS`, `CONTROLER_TAILLE_DES_ETAPES` : répétées jusqu'à validation, à chaque porte concernée.
- `REUTILISER_ACQUIS` : à chaque passe suivante, pour ne pas redémontrer ce que les passes précédentes ont déjà établi.

### Ce que ça fait bien / mal

**Bien** : il existe toujours un plan complet et cohérent à chaque instant, même minimal — utile si l'enquête doit être interrompue ; le travail d'approfondissement (options, attaques, risques) n'est dépensé que là où le squelette l'exige réellement, pas partout uniformément ; les boucles de correction sont courtes car elles ciblent une passe précise, jamais un redémarrage complet, sauf la porte 3 qui reste bornée à une fois.
**Mal** : le choix fait en Passe 1 (« une option domine clairement ») peut ancrer prématurément une direction que l'épaississement en Passe 3 ne remettra en cause que localement — contrairement au tournoi de une autre approche, il n'y a pas de vraie compétition de plans entiers ; l'ordre strict des passes peut forcer à traiter la gouvernance (Passe 5) avant d'avoir totalement stabilisé la robustesse si une boucle de correction tardive rouvre la Passe 3.

---


# Architecture 13 — Le tournoi d'options

<details><summary>Briques utilisées</summary>

```
FONCTION PROLOGUE_CADRAGE(demande):
    LIRE_TECHNIQUES_AUTORISEES()
    INVENTORIER_CAPACITES()
    IDENTIFIER_DESTINATAIRE()
    SEPARER_DEMANDE_ET_BESOIN(demande)
    CONTESTER_ENONCE_PROBLEME()
    SI DETECTER_SOLUTION_IMPOSEE(): reformuler comme problème, pas comme solution imposée
    SI DECLINER_SI_PAS_DE_PLAN(): retourner "pas de planification ici", FIN
    SI un plan existant est fourni: AMORCER_DEPUIS_PLAN_EXISTANT()
    ETABLIR_ETAT_ACTUEL()
    CHERCHER_ANTECEDENTS()
    FORMULER_CIBLE_OBSERVABLE()
    VERIFIER_FIDELITE_CIBLE_BESOIN()
    TRAQUER_AJOUTS_SILENCIEUX()
    DEFINIR_CRITERES_ACCEPTATION()
    RECENSER_CONTRAINTES_DURES()
    RECENSER_OBLIGATIONS_FORMELLES()
    RECENSER_PREFERENCES()
    BALAYER_EXIGENCES_TACITES()
    DEBUSQUER_HYPOTHESES_IMPORTEES()
    EXPOSER_EXTERNALITES_CERTAINES()
    RECENSER_DEPENDANCES_EXTERNES()
    RECENSER_RESSOURCES_EXECUTION()
    DELIMITER_PERIMETRE()
    retourner périmètre_racine, état_partagé{faits:[], décisions:[], risques:[]}

FONCTION EPILOGUE_CLOTURE(état_partagé, plan):
    RENDRE_ACTIONNABLE_PAR_AGENT(plan)
    VERIFIER_COHERENCE_ENSEMBLE(plan)
    VERIFIER_COUVERTURE_OBJECTIFS(plan)
    VERIFIER_COUVERTURE_BLOQUANTS(plan)
    VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(plan)
    VERIFIER_FAISABILITE_PAR_EXECUTANT(plan)
    VERIFIER_ADOSSEMENT_AFFIRMATIONS(état_partagé)
    ELAGUER_ETAPES_INUTILES(plan)
    ELAGUER_LA_PROSE(plan)
    ISOLER_LE_HORS_PLAN(plan)
    SIGNALER_LES_LIMITES(plan)
    PREVOIR_SUITE_EN_CAS_DE_SUCCES(plan)
    PROPOSER_MARGES() ; PROPOSER_AFFECTATION() ; PROPOSER_CHIFFRAGE()
    CONTROLER_CONTENU_FINAL(plan)
    CONTROLER_INTEGRITE_DOCUMENT(plan)
    avis = FAIRE_CONTROLER_PAR_UN_TIERS(plan)
    TANT QUE avis signale une faille ET passes < 2:
        corriger localement la partie visée ; avis = FAIRE_CONTROLER_PAR_UN_TIERS(plan) ; passes += 1
    SI faille persistante: QUALIFIER_ETAT_RESOLUTION(point) = "non résolu" ; SIGNALER_LES_LIMITES(point)
    PLACER_ET_NOMMER_LE_FICHIER()
    REDIGER_PLAN(plan)
    REDIGER_TRACABILITE_SEPAREE(état_partagé)
    RESTITUER_EN_BREF()
```

---

</details>


**Principe** : découpage « OU » et non « ET » — chaque option candidate à une vraie décision est développée comme un plan miniature complet et isolé ; ce n'est pas la fusion mais l'**arbitrage** qui recompose.

**Les 6 choix de conception**
- **Déclencheur de coupe** : `ORIENTER_CHOIX` classe la situation comme « vrai choix à instruire » (pas un fait manquant, pas une simple préférence) et `PRODUIRE_OPTIONS_DISTINCTES` produit plus d'une option matériellement différente.
- **Découpe** : une branche par option ; chacune hérite du cadrage racine sans le rejouer.
- **Effort par profondeur** : le nombre d'angles d'attaque (`CHOISIR_ANGLES_ATTAQUE`) et le nombre de tours du tournoi se réduisent avec la profondeur ; un sous-choix interne à une option ne redéclenche un tournoi complet que s'il reste un vrai choix.
- **Recomposition** : pas un merge additif — un arbitrage (`ARBITRER_A_L_AVEUGLE`, sur options anonymisées, jamais au nombre de voix), avec récupération tracée des morceaux valables des options perdantes.
- **Dépendances entre frères** : les branches sont volontairement isolées pendant leur développement (`ISOLER_LES_EVALUATIONS`) pour empêcher toute contamination ; après coup, on vérifie qu'aucune n'a *tacitement* présupposé le choix d'une autre (ce qui romprait leur indépendance).
- **Borne de profondeur** : `GARANTIR_DIVERSITE_METHODE` qui échoue à produire une option vraiment distincte arrête la récursion ; sinon `PROFONDEUR_MAX` de config.

```
FONCTION CYCLE_C(périmètre, profondeur, état_partagé):
    options = PRODUIRE_OPTIONS_DISTINCTES(périmètre)
    tentative = 0
    TANT QUE NON GARANTIR_DIVERSITE_METHODE(options) ET tentative < 2:        # BOUCLE DE DIVERSITE
        options.ajouter( CHERCHER_APPROCHES_NON_ENVISAGEES(périmètre) ) ; tentative += 1

    nature = ORIENTER_CHOIX(périmètre, options)
    SI nature == "fait manquant":
        moyen = CHOISIR_MOYEN_DE_LEVEE(...) ; MENER_VERIFICATION(moyen)
        retourner CYCLE_C(périmètre, profondeur, état_partagé)     # relance avec le fait acquis
    SI nature == "préférence utilisateur":
        PRESENTER_ALTERNATIVES_AU_CHOIX(options) ; choix = SOUMETTRE_ARBITRAGE_UTILISATEUR(options)
        retourner DEVELOPPER_OPTION(choix, périmètre, état_partagé)   # pas de tournoi, une seule branche

    # nature == "vrai choix à instruire"
    SI profondeur < PROFONDEUR_MAX ET len(options) > 1:
        branches = []
        POUR chaque option DANS options:
            EXIGER_HYPOTHESES_EXPLICITES(option) ; DEBUSQUER_HYPOTHESES_IMPORTEES(option)
            sp = DELIMITER_PERIMETRE(périmètre, sous_hypothèse=option)
            se = REUTILISER_ACQUIS(état_partagé) ; ISOLER_LES_EVALUATIONS(se)
            branches.ajouter( (option, CYCLE_C(sp, profondeur+1, se)) )

        POUR chaque (option,_) DANS branches:                                # ATTAQUE ADVERSARIALE
            POUR chaque angle DANS CHOISIR_ANGLES_ATTAQUE(option):
                ATTAQUER_UNE_OPTION(option)     # ne reçoit qu'action + faits, jamais le plaidoyer adverse
        SI ATTAQUER_TOUT_LE_CHAMP(options) == "tout tombe":
            CONTESTER_ENONCE_PROBLEME(périmètre)      # remonte jusqu'à la racine si besoin
            CONSTATER_IMPOSSIBILITE(périmètre)
            retourner échec vers le parent

        survivantes = [b pour b dans branches SI b.option non éliminée]
        DETECTER_ERREURS_CORRELEES(survivantes)
        QUALIFIER_INDEPENDANCE_OBTENUE(survivantes)

        TANT QUE len(survivantes) > 1:                                        # BOUCLE DE FRAGILITE
            cible = AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE(survivantes)
            SI NON ATTAQUER_UNE_OPTION(cible.option): retirer cible de survivantes

        gagnante = ARBITRER_A_L_AVEUGLE(survivantes, précédence=config)
        CONSERVER_OPTIONS_ECARTEES(branches \ gagnante)
        POUR chaque pièce récupérable d'une branche perdante:
            RATTACHER_TOUTE_PIECE_A_SON_ORIGINE(pièce, branche_origine)
            SI ETABLIR_DEPENDANCES_ENTRE_DECISIONS(pièce, plan_gagnant) compatible:
                intégrer la pièce au plan gagnant

        SI compromis matériel encore non tranchable (deux options restent défendables):
            CONSTRUIRE_BRANCHE_CONDITIONNELLE(gagnante, alternative)

        plan = gagnante.plan
        CONSIGNER_CE_QUI_A_TRANCHE(gagnante) ; QUALIFIER_ETAT_RESOLUTION(décision)

    SINON:
        plan = DEVELOPPER_OPTION(options[0], périmètre, état_partagé)

    retourner plan

FONCTION DEVELOPPER_OPTION(option, périmètre, état_partagé):
    # même bloc que TRAITER_FEUILLE ci-dessus : inconnues locales, actions,
    # attendus observables, retours arrière, risques locaux, calibrage des étapes.
```

**3. Boucles**
- *Boucle de diversité* : options trop proches en méthode → recherche d'approche non envisagée, bornée à 2 tentatives, sinon on accepte l'éventail obtenu et on le signale (`RENDRE_INCERTITUDE_VISIBLE`).
- *Boucle d'attaque/tout-le-champ* : si toutes les options tombent, remontée maximale jusqu'à `CONTESTER_ENONCE_PROBLEME` à la racine — pas de nouvelle génération d'options au même niveau, c'est le cadrage lui-même qui est remis en cause.
- *Boucle de fragilité* : tant qu'il reste plus d'une survivante, on attaque systématiquement l'hypothèse la plus fragile ; elle termine mécaniquement car chaque tour élimine ou confirme une branche (ensemble fini, décroissant).
- *Boucle d'indépendance* : erreurs corrélées détectées → dégrade `QUALIFIER_INDEPENDANCE_OBTENUE` plutôt que de re-boucler indéfiniment sur la recherche d'une source indépendante.

**4. Fonctions appelées plusieurs fois** : `PRODUIRE_OPTIONS_DISTINCTES` (racine et chaque sous-choix récursif), `ATTAQUER_UNE_OPTION` (chaque option, plusieurs passes possibles), `CHOISIR_ANGLES_ATTAQUE`, `ISOLER_LES_EVALUATIONS`, `ARBITRER_A_L_AVEUGLE` (à chaque niveau du tournoi), `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE`, `CONSERVER_OPTIONS_ECARTEES` — parce que l'architecture réplique tout le cycle sur chaque hypothèse rivale plutôt que de le dérouler une fois.

**5. Forces / faiblesses** : Excellente quand le vrai risque est le choix lui-même (décision à fort enjeu, plusieurs stratégies plausibles) ; garantit une décision robuste, non biaisée par le vote, avec traçabilité forte des options écartées. Coûteuse et mal adaptée quand le problème est surtout un problème d'exécution méthodique sans vrai dilemme : elle développe alors des options jusqu'au bout pour rien, et la couverture des objectifs multiples (`VERIFIER_COUVERTURE_OBJECTIFS`) doit être repassée après coup sur l'option gagnante, car ce n'est pas elle qui structure la récursion.

---

---


# Architecture 14 — Pipeline à jalons verrouillés


**Principe** : le travail avance en phases strictement ordonnées (cadrage → état/cible → inconnues → options → risques → étapes → gouvernance → contrôle final) ; chaque phase se termine par une porte de vérification qui, en cas d'échec, ne redémarre que la phase courante ou remonte d'une phase à la fois — jamais plus loin sans passer par un point d'escalade explicite vers l'utilisateur.

### Pseudo-code

```
PHASE 0 — CADRAGE
  LIRE_TECHNIQUES_AUTORISEES
  INVENTORIER_CAPACITES
  IDENTIFIER_DESTINATAIRE
  EVALUER_EXIGENCE_TACHE
  si tâche jugée hors périmètre de planification :
      DECLINER_SI_PAS_DE_PLAN ; FIN

  SEPARER_DEMANDE_ET_BESOIN
  DELIMITER_PERIMETRE
  CONTESTER_ENONCE_PROBLEME
  DETECTER_SOLUTION_IMPOSEE
  QUALIFIER_FORME_TRAVAIL
  BALAYER_EXIGENCES_TACITES
  TRAQUER_AJOUTS_SILENCIEUX
  ORDONNER_OBJECTIFS_SANS_ECARTER
  DETECTER_CONFLIT_OBJECTIFS
  tant que conflit non résolu (max 2 essais locaux) :
      SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre réponse ; ré-ORDONNER_OBJECTIFS_SANS_ECARTER
  si conflit toujours non résolu après 2 essais : CONSTATER_IMPOSSIBILITE ; FIN

  RECENSER_PREFERENCES ; RECENSER_CONTRAINTES_DURES ; RECENSER_OBLIGATIONS_FORMELLES
  EXPOSER_EXTERNALITES_CERTAINES
  === PORTE 0 : périmètre stable, objectifs ordonnés, pas de conflit ouvert ===

PHASE 1 — ÉTAT ET CIBLE
  ETABLIR_ETAT_ACTUEL
  FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION
  boucle (max 3) :
      VERIFIER_FIDELITE_CIBLE_BESOIN
      si échec : reformuler FORMULER_CIBLE_OBSERVABLE ; continuer
      sinon : sortir
  si échec persistant : SUSPENDRE_ENQUETE_ET_DEMANDER (retour PHASE 0 après réponse utilisateur)
  CHAINER_ETAT_ACTUEL_VERS_CIBLE
  === PORTE 1 : cible falsifiable, reliée à l'état actuel ===

PHASE 2 — INCONNUES (investigation)
  RECENSER_INCONNUES
  pour chaque inconnue : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION
  file = celles classées "bloque l'écriture" ; QUALIFIER_PORTEE_INCONNUE (chacune)
  ORDONNER_INCONNUES_SANS_ECARTER(file)

  tant que file non vide :                       # décroît à chaque tour → termine
      inconnue = file.pop_premier()
      DISTINGUER_INDETERMINE_ET_NON_CHERCHE
      DECIDER_D_INTERROGER_UTILISATEUR
      si oui :
          FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER  # attente bloquante, pas de rebouclage
      sinon :
          CHOISIR_MOYEN_DE_LEVEE
          selon moyen :
              inspection/source/calcul/test : MENER_VERIFICATION ou CHERCHER_ANTECEDENTS
              action réversible : LEVER_INCONNUE_PAR_ACTION_REVERSIBLE
              agent : DECIDER_D_OUVRIR_UN_AGENT
                      si oui : REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT
                               (PARALLELISER_ENQUETE si d'autres inconnues indépendantes sont prêtes)
                               INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
          CONSIGNER_PROVENANCE_FAIT ; JUGER_PEREMPTION_FAIT
          si périssable : INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
          ENONCER_LIMITES_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE ; RENDRE_INCERTITUDE_VISIBLE
          DETECTER_CONTRADICTION_ENTRE_SOURCES vs faits déjà établis
          si contradiction : DETECTER_ORIGINE_COMMUNE_SOURCES ; RESOUDRE_CONTRADICTION
      si nouvelles inconnues découvertes ET classées "bloquantes" : file.ajouter()
      si ARRETER_ORCHESTRATION signale rendement nul : sortir de la boucle, marquer le reste "non résolu, signalé"

  VERIFIER_ADOSSEMENT_AFFIRMATIONS(tous les faits établis)
  si affirmation non adossée : la réparer ou la retirer (boucle locale bornée à 2)
  === PORTE 2 : plus d'inconnue bloquante ouverte, tout fait est adossé et daté ===

PHASE 3 — OPTIONS ET DÉCISION
  PRODUIRE_OPTIONS_DISTINCTES ; CHERCHER_ANTECEDENTS
  boucle (max 3) :
      GARANTIR_DIVERSITE_METHODE
      si insuffisant : CHERCHER_APPROCHES_NON_ENVISAGEES ; refaire
      sinon : sortir
  pour chaque option : EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
      si hypothèse tacite détectée : rejeter l'option ou la faire réécrire (1 seule reprise par option)

  ISOLER_LES_EVALUATIONS
  CHOISIR_ANGLES_ATTAQUE
  pour chaque option restante : ATTAQUER_UNE_OPTION      # un appel par option
  ATTAQUER_TOUT_LE_CHAMP
  si le champ entier casse : CONSTATER_IMPOSSIBILITE
                              ou retour à PHASE 0 (reformulation), 1 seule fois globalement
  ARBITRER_A_L_AVEUGLE ; QUALIFIER_INDEPENDANCE_OBTENUE ; DETECTER_ERREURS_CORRELEES
  CONSERVER_OPTIONS_ECARTEES

  ORIENTER_CHOIX
  selon résultat :
      fait manquant     : retour PHASE 2 sur ce point précis (boucle bornée par le nb d'inconnues restantes)
      préférence requise: PRESENTER_ALTERNATIVES_AU_CHOIX ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre
      vrai choix        : trancher

  ETABLIR_DEPENDANCES_ENTRE_DECISIONS ; DISTINGUER_CHOIX_ET_CONSEQUENCE
  QUALIFIER_PORTEE_DECISION ; NOMMER_FAIT_QUI_FERAIT_BASCULER
  CONSIGNER_CE_QUI_A_TRANCHE
  === PORTE 3 : une option retenue, hypothèses explicites, arbitrage tracé ===

PHASE 4 — RISQUES
  RECENSER_RISQUES_PAR_ORIGINE
  pour chaque risque : QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT
                        QUALIFIER_REVERSIBILITE ; QUALIFIER_TERRITOIRE ; ANTICIPER_TIERS_REACTIF
  STATUER_SUR_RISQUE_RESIDUEL
  si résidu non trivial : SOUMETTRE_ARBITRAGE_UTILISATEUR ; attendre
  === PORTE 4 : chaque risque qualifié et statué ===

PHASE 5 — CONSTRUCTION DES ÉTAPES
  DERIVER_ACTIONS_DEPUIS_DECISIONS
  ORDONNER_PAR_PREREQUIS
  IDENTIFIER_ETAPES_SIMULTANEES
  boucle (max 2) :
      VERIFIER_SIMULTANEITE_POSSIBLE
      si conflit (ressource/verrou/approbateur) : re-sérialiser localement ; refaire
      sinon : sortir
  pour chaque étape :
      DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE
      si mécanique : CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
      DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC ; DEFINIR_RETOUR_ARRIERE
      EPROUVER_RETOUR_ARRIERE
      si non vérifiable : 1 relance de MENER_VERIFICATION, sinon marquer "retour arrière non garanti"
  CONSTRUIRE_BRANCHE_CONDITIONNELLE pour chaque inconnue d'exécution absorbée en Phase 2
  boucle (max 2) : CONTROLER_TAILLE_DES_ETAPES → scinder/fusionner si besoin
  ELAGUER_ETAPES_INUTILES
  RECENSER_INVARIANTS ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN
  si violation : corriger l'étape fautive (retour local, borné à 2) sinon CONSTATER_IMPOSSIBILITE
  AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE (départage d'ordre)
  PREVOIR_SUITE_EN_CAS_DE_SUCCES
  === PORTE 5 : chemin complet, invariants tenus sur toute branche ===

PHASE 6 — GOUVERNANCE
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION ; PLACER_POINTS_AUTORISATION
  DESIGNER_AUTORITE_AUTORISATION
  REPERER_POINTS_ENGAGEMENT
  VERIFIER_COUVERTURE_BLOQUANTS
  si couverture incomplète : ajouter les points manquants (boucle bornée à 2)
  RECENSER_RESSOURCES_EXECUTION ; RECENSER_DEPENDANCES_EXTERNES
  VERIFIER_FAISABILITE_PAR_EXECUTANT
  si l'exécutant ne peut pas : revoir l'étape (retour PHASE 5) ou SOUMETTRE_ARBITRAGE_UTILISATEUR
  PROPOSER_MARGES ; PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE  (offres, jamais imposées)

PHASE 7 — CONTRÔLE FINAL
  REUTILISER_ACQUIS (vérifie qu'aucun travail n'a été refait inutilement)
  VERIFIER_COUVERTURE_OBJECTIFS
  si objectif non couvert : retour PHASE 3 ou 5 sur cet objectif (borné à 1 aller-retour)
  VERIFIER_COHERENCE_ENSEMBLE
  RATTACHER_TOUTE_PIECE_A_SON_ORIGINE ; ISOLER_LE_HORS_PLAN ; SIGNALER_LES_LIMITES
  pour chaque point tranché : QUALIFIER_ETAT_RESOLUTION
  CONTROLER_CONTENU_FINAL
  FAIRE_CONTROLER_PAR_UN_TIERS → INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
  si le tiers casse quelque chose : retour à la phase concernée (1 seul tour de re-revue global)
  ELAGUER_LA_PROSE ; CONTROLER_INTEGRITE_DOCUMENT (boucle locale bornée à 2)
  RENDRE_ACTIONNABLE_PAR_AGENT
  REDIGER_PLAN ; REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER
  RESTITUER_EN_BREF
```

### Boucles

- **Boucle locale de porte** (chaque phase) : déclenchée par l'échec d'une vérification de fin de phase (ex. `VERIFIER_FIDELITE_CIBLE_BESOIN`, `VERIFIER_SIMULTANEITE_POSSIBLE`) ; ne remonte pas plus haut que la phase courante ; bornée à 2–3 tours puis escalade.
- **Boucle d'investigation** (Phase 2) : file d'inconnues qui décroît strictement (une inconnue résolue ne revient qu'exceptionnellement, sous forme d'une inconnue *nouvelle* et distincte) ; se termine quand la file est vide ou par `ARRETER_ORCHESTRATION`.
- **Boucle d'escalade inter-phase** : une porte qui échoue de façon répétée renvoie exactement d'une phase en arrière (jamais deux), sauf le cas `ATTAQUER_TOUT_LE_CHAMP` qui peut renvoyer jusqu'à la Phase 0 — plafonné à une occurrence dans tout le run.
- **Boucle d'attente utilisateur** : `SUSPENDRE_ENQUETE_ET_DEMANDER` / `SOUMETTRE_ARBITRAGE_UTILISATEUR` ne sont jamais des boucles au sens strict : elles arrêtent le flux et reprennent au même point avec la réponse, ce qui garantit qu'elles ne tournent jamais indéfiniment.
- **Garantie globale de terminaison** : chaque boucle locale a un plafond fixe de tours ; au-delà, elle échoue explicitement vers `CONSTATER_IMPOSSIBILITE` ou vers l'utilisateur — jamais vers une nouvelle tentative silencieuse.

### Fonctions appelées plusieurs fois
- `MENER_VERIFICATION`, `CHOISIR_MOYEN_DE_LEVEE` : une fois par inconnue.
- `ATTAQUER_UNE_OPTION` : une fois par option.
- `CONSIGNER_PROVENANCE_FAIT`, `JUGER_PEREMPTION_FAIT` : une fois par fait établi.
- `SOUMETTRE_ARBITRAGE_UTILISATEUR` : à chaque point de désaccord irréductible (conflit d'objectifs, risque résiduel, faisabilité).
- `DEFINIR_ATTENDU_OBSERVABLE`, `DEFINIR_RETOUR_ARRIERE`, `EPROUVER_RETOUR_ARRIERE`, `QUALIFIER_ETAT_RESOLUTION` : une fois par étape / par point.
- `VERIFIER_FIDELITE_CIBLE_BESOIN`, `CONTROLER_TAILLE_DES_ETAPES`, `VERIFIER_SIMULTANEITE_POSSIBLE` : rejouées à chaque tour de leur boucle de porte locale.

### Ce qui est laissé de côté
- `AMORCER_DEPUIS_PLAN_EXISTANT` : cette architecture démarre toujours d'une demande fraîche en Phase 0 ; elle n'a pas de point d'entrée alternatif sans casser sa discipline de verrouillage séquentiel.
- `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` : un pipeline à portes ne recomposerait pas proprement un sous-cycle de phases en cours de route — le surdimensionnement se traite uniquement par `CONTROLER_TAILLE_DES_ETAPES` / `ELAGUER_ETAPES_INUTILES`.

### Bilan
**Bien** : lisible, auditable, chaque étape sait exactement ce qu'elle doit avoir en main avant d'avancer ; convient à une exécution stricte de la contrainte « rien n'est reporté à l'exécution », car chaque porte est un point de non-retour explicite. **Mal** : rigide face à des inconnues qui traversent les phases (une inconnue découverte en Phase 5 doit reculer artificiellement jusqu'en Phase 2) ; lent sur les tâches simples car toutes les phases s'exécutent même quand elles seraient vides.

---

---


# Architecture 15 — Cascade à paliers bornés

<details><summary>Briques utilisées</summary>

```
FONCTION CONFRONTATION(question, dossier):
    ISOLER_LES_EVALUATIONS()                      # verrouille le mode aveugle pour tout ce qui suit

    angles = CHOISIR_ANGLES_ATTAQUE(question)
    methodes = GARANTIR_DIVERSITE_METHODE(question) # oblige les propositions à différer par la méthode

    propositions = []
    POUR chaque méthode DANS methodes:
        brief = REDIGER_BRIEF_AGENT(dossier, question, méthode)   # rien qui oriente
        SI DECIDER_D_OUVRIR_UN_AGENT(brief) == vrai:
            BORNER_UN_AGENT(condition_arrêt)
            retour = <sous-agent traite brief>
            proposition = INTEGRER_RETOUR_AGENT(retour)
            REFUSER_AUTO_CONFIRMATION(proposition)     # l'agent l'affirme, ça ne le rend pas vrai
        SINON:
            proposition = PRODUIRE_OPTIONS_DISTINCTES(brief)
        EXIGER_HYPOTHESES_EXPLICITES(proposition)       # rejetée si elle comble une inconnue tacitement
        propositions.ajouter(proposition)

    # attaque : chaque option reçoit seulement action + faits, jamais la défense d'une autre
    POUR chaque p DANS propositions:
        ATTAQUER_UNE_OPTION(p, dossier)
        DEBUSQUER_HYPOTHESES_IMPORTEES(p)
    ATTAQUER_TOUT_LE_CHAMP(propositions, dossier)       # ce qui ferait échouer TOUTES les options

    # arbitrage aveugle
    indep = QUALIFIER_INDEPENDANCE_OBTENUE(propositions)
    SI DETECTER_ERREURS_CORRELEES(propositions):
        <dégrader la confiance d'un accord apparent entre propositions>
    verdict = ARBITRER_A_L_AVEUGLE(anonymiser(propositions), précédence_explicite)

    # mise en forme du verdict
    CONSIGNER_CE_QUI_A_TRANCHE(verdict)
    QUALIFIER_ETAT_RESOLUTION(verdict)                  # tranché / avec compromis / branché / en attente / invalide
    NOMMER_FAIT_QUI_FERAIT_BASCULER(verdict)
    CONSERVER_OPTIONS_ECARTEES(propositions - {verdict.retenu})
    SI verdict.retenu n'était proposé par aucune proposition initiale:
        RATTACHER_TOUTE_PIECE_A_SON_ORIGINE(verdict.retenu)

    RETOURNER verdict
```

### `CONSTITUER_DOSSIER_INITIAL(demande)` — construit les faits, jamais un verdict

```
FONCTION CONSTITUER_DOSSIER_INITIAL(demande_ou_plan_existant):
    LIRE_TECHNIQUES_AUTORISEES() ; INVENTORIER_CAPACITES() ; EVALUER_EXIGENCE_TACHE()
    IDENTIFIER_DESTINATAIRE()
    SI demande == plan_existant: AMORCER_DEPUIS_PLAN_EXISTANT()
    SINON: SEPARER_DEMANDE_ET_BESOIN(demande)
    DELIMITER_PERIMETRE() ; ETABLIR_ETAT_ACTUEL()
    FORMULER_CIBLE_OBSERVABLE() ; VERIFIER_FIDELITE_CIBLE_BESOIN()
    RECENSER_CONTRAINTES_DURES() ; RECENSER_INVARIANTS()
    RECENSER_OBLIGATIONS_FORMELLES() ; DESIGNER_AUTORITE_AUTORISATION()
    RECENSER_PREFERENCES() ; RECENSER_RESSOURCES_EXECUTION() ; RECENSER_DEPENDANCES_EXTERNES()
    BALAYER_EXIGENCES_TACITES() -> pour chaque exigence remontée : DECIDER_D_INTERROGER_UTILISATEUR + FORMULER_QUESTION_ACTIONNABLE
    TRAQUER_AJOUTS_SILENCIEUX() ; EXPOSER_EXTERNALITES_CERTAINES()
    CHERCHER_ANTECEDENTS() ; REUTILISER_ACQUIS()
    DETECTER_SOLUTION_IMPOSEE() ; DETECTER_CONFLIT_OBJECTIFS() -> SI conflit: ORDONNER_OBJECTIFS_SANS_ECARTER()
    QUALIFIER_FORME_TRAVAIL() ; QUALIFIER_TERRITOIRE()

    inconnues = RECENSER_INCONNUES()
    POUR chaque i DANS ORDONNER_INCONNUES_SANS_ECARTER(inconnues):
        nature = CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION(i)
        SI nature == "exécution":
            QUALIFIER_PORTEE_INCONNUE(i) ; laisser pour la mise en forme (branche conditionnelle)
            CONTINUER
        # inconnue de construction : à lever maintenant
        QUALIFIER_PORTEE_INCONNUE(i)
        SI DISTINGUER_INDETERMINE_ET_NON_CHERCHE(i) == "simplement pas cherché":
            moyen = CHOISIR_MOYEN_DE_LEVEE(i)
            SELON moyen:
              inspection/source/calcul/test -> MENER_VERIFICATION(i)
              action réversible bornée      -> LEVER_INCONNUE_PAR_ACTION_REVERSIBLE(i)
              question                      -> DECIDER_D_INTERROGER_UTILISATEUR(i) ; FORMULER_QUESTION_ACTIONNABLE(i)
                                                SUSPENDRE_ENQUETE_ET_DEMANDER(i) ; attendre la réponse
        SINON: SUSPENDRE_ENQUETE_ET_DEMANDER(i)   # vraiment indéterminable : remonter, pas insister

    POUR chaque fait établi:
        CONSIGNER_PROVENANCE_FAIT(fait) ; SEPARER_OBSERVE_ET_SUPPOSE(fait) ; ENONCER_LIMITES_FAIT(fait)
        SI JUGER_PEREMPTION_FAIT(fait) == "périssable":
            INSCRIRE_REVERIFICATION_FAIT_PERISSABLE(fait)   # placée juste avant l'étape qui en dépendra
        REFUSER_AUTO_CONFIRMATION(fait)

    SI DETECTER_CONTRADICTION_ENTRE_SOURCES(faits):
        SI DETECTER_ORIGINE_COMMUNE_SOURCES(...): <une seule source en réalité, pondérer en conséquence>
        RESOUDRE_CONTRADICTION(...)   # date / version / périmètre / définition, ou marquer contesté

    RENDRE_INCERTITUDE_VISIBLE()
    RETOURNER dossier
```

### `METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts, dossier)` — met en forme, puis vérifie avant d'émettre

```
FONCTION METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts_choix, dossier):
    actions = DERIVER_ACTIONS_DEPUIS_DECISIONS(verdicts_choix)
    ordre = ORDONNER_PAR_PREREQUIS(squelette, actions)
    ordre = AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE(ordre)   # départage à validité égale
    simultanées = IDENTIFIER_ETAPES_SIMULTANEES(ordre)
    POUR chaque paire simultanée: VERIFIER_SIMULTANEITE_POSSIBLE(paire)
    POUR chaque inconnue d'exécution laissée en dossier: CONSTRUIRE_BRANCHE_CONDITIONNELLE(inconnue)
    POUR chaque étape:
        DEFINIR_ATTENDU_OBSERVABLE(étape) ; DEFINIR_CRITERES_ACCEPTATION(étape) ; DEFINIR_SIGNAUX_ECHEC(étape)
        DEFINIR_RETOUR_ARRIERE(étape) ; EPROUVER_RETOUR_ARRIERE(étape)
        DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE(étape)
        SI "mécanique": CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE(étape)
    PLACER_POINTS_VERIFICATION(ordre) ; PLACER_POINTS_AUTORISATION(ordre) ; PLACER_JALONS_CONSTAT(ordre)
    RECENSER_RISQUES_PAR_ORIGINE() -> QUALIFIER_VRAISEMBLANCE_RISQUE() -> QUALIFIER_RAYON_IMPACT() -> STATUER_SUR_RISQUE_RESIDUEL()
    ANTICIPER_TIERS_REACTIF() ; QUALIFIER_REVERSIBILITE() ; REPERER_POINTS_ENGAGEMENT()
    PROPOSER_MARGES() ; PROPOSER_AFFECTATION() ; PROPOSER_CHIFFRAGE()   # jamais imposés
    PRESENTER_ALTERNATIVES_AU_CHOIX(points laissés à l'utilisateur)
    CONTROLER_TAILLE_DES_ETAPES() ; ELAGUER_ETAPES_INUTILES()
    SIGNALER_LES_LIMITES() ; ISOLER_LE_HORS_PLAN()
    VERIFIER_COUVERTURE_OBJECTIFS() ; VERIFIER_COUVERTURE_BLOQUANTS() ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN()
    VERIFIER_COHERENCE_ENSEMBLE() ; VERIFIER_FAISABILITE_PAR_EXECUTANT()
    RENDRE_ACTIONNABLE_PAR_AGENT() ; PREVOIR_SUITE_EN_CAS_DE_SUCCES()
    ELAGUER_LA_PROSE() ; VERIFIER_ADOSSEMENT_AFFIRMATIONS() ; RENDRE_INCERTITUDE_VISIBLE()

    plan = REDIGER_PLAN(ordre, actions, ...)

    TANT QUE vrai:                                         # boucle de vérification finale
        rapport = CONTROLER_CONTENU_FINAL(plan)
        rapport += CONTROLER_INTEGRITE_DOCUMENT(plan)
        rapport += FAIRE_CONTROLER_PAR_UN_TIERS(plan)
        SI rapport.vide: SORTIR
        <corriger localement le plan selon rapport>          # jamais une nouvelle confrontation
        SI <2 corrections déjà tentées>: STATUER_SUR_RISQUE_RESIDUEL(rapport.restant) ; SORTIR

    REDIGER_TRACABILITE_SEPAREE() ; PLACER_ET_NOMMER_LE_FICHIER(plan)
    RESTITUER_EN_BREF()
    RETOURNER plan
```

Ces trois briques couvrent, à elles seules, la quasi-totalité des 129 identifiants. Ce qui suit montre, pour chaque architecture, **comment on arrive à `CONFRONTATION`, dans quel ordre, ce qui la déclenche, et comment un verdict peut rouvrir ce qui précède** — c'est là qu'elles diffèrent réellement.

---

</details>


**Principe** : trois paliers strictement ordonnés (PROBLÈME → STRUCTURE → CHOIX), chacun gagné par une confrontation ; un verdict ne peut rouvrir que le palier immédiatement précédent, et seulement un nombre de fois plafonné par un budget qui décroît — au-delà, on force la clôture par l'utilisateur.

### Pseudo-code

```
FONCTION PLANIFIER(demande):
    LIRE_TECHNIQUES_AUTORISEES() ; EVALUER_EXIGENCE_TACHE()
    SI DECLINER_SI_PAS_DE_PLAN(demande): RETOURNER   # porte d'entrée : pas un problème de planification

    dossier = CONSTITUER_DOSSIER_INITIAL(demande)
    budget = { PROBLEME: 1, STRUCTURE: 2 }           # borne de terminaison, décroissante

    # --- Palier 1 : PROBLEME ---
    verdict_p = CONFRONTATION("problème", dossier)
    SI verdict_p.état == "invalide":
        CONSTATER_IMPOSSIBILITE() ; RETOURNER
    cible = verdict_p.retenu

    # --- Palier 2 : STRUCTURE, avec droit de retour au palier 1 ---
    RÉPÉTER:
        verdict_s = CONFRONTATION("structure", dossier + {cible})
        SI verdict_s.remet_en_cause_le_problème:
            SI budget[PROBLEME] == 0:
                SOUMETTRE_ARBITRAGE_UTILISATEUR(verdict_s.désaccord) ; cible = réponse ; SORTIR RÉPÉTER
            budget[PROBLEME] -= 1
            REUTILISER_ACQUIS(dossier)               # ne redémontre pas ce qui reste valide
            verdict_p = CONFRONTATION("problème", dossier + {NOMMER_FAIT_QUI_FERAIT_BASCULER(verdict_s)})
            SI verdict_p.état == "invalide": CONSTATER_IMPOSSIBILITE() ; RETOURNER
            cible = verdict_p.retenu
            CONTINUER RÉPÉTER
        SINON: SORTIR RÉPÉTER
    squelette = verdict_s.retenu

    # --- Palier 3 : CHOIX, un par un, avec retour possible à la structure ---
    points = ORIENTER_CHOIX(squelette)
    verdicts_choix = {}
    POUR chaque p DANS ETABLIR_DEPENDANCES_ENTRE_DECISIONS(points):   # ordre de tranchage
        SI DISTINGUER_CHOIX_ET_CONSEQUENCE(p) == "conséquence mécanique": CONTINUER
        SI p.nature != "vrai choix":            # fait manquant / préférence / autorisation
            <résoudre hors confrontation : MENER_VERIFICATION ou question utilisateur> ; CONTINUER

        RÉPÉTER:
            v = CONFRONTATION(p, dossier + squelette)
            SI v.remet_en_cause_la_structure:
                SI budget[STRUCTURE] == 0:
                    SOUMETTRE_ARBITRAGE_UTILISATEUR(v.désaccord) ; SORTIR RÉPÉTER (garder v tel quel)
                budget[STRUCTURE] -= 1
                RETOURNER AU PALIER 2 avec fait_nouveau = NOMMER_FAIT_QUI_FERAIT_BASCULER(v)
                # (implémentation : goto Palier 2 ; à son retour, reprendre le palier 3 depuis p)
            SINON: SORTIR RÉPÉTER
        verdicts_choix[p] = v

    plan = METTRE_EN_FORME_ET_CONTROLER(squelette, verdicts_choix, dossier)
```

### 3. Les boucles

- **Boucle palier 2 (structure ↔ problème)** : déclenchée quand un verdict de structure nomme un fait qui invaliderait la cible. Remonte au palier 1, jamais plus loin. Bornée par `budget[PROBLEME]` (1 par défaut) ; à épuisement, `SOUMETTRE_ARBITRAGE_UTILISATEUR` coupe court — terminaison garantie en au plus 2 passages.
- **Boucle palier 3 (choix ↔ structure)** : déclenchée quand un choix litigieux révèle que le découpage retenu ne tient pas. Remonte au palier 2 (jamais directement au palier 1). Bornée par `budget[STRUCTURE]` (2 par défaut).
- **Boucle de vérification finale** (dans `METTRE_EN_FORME_ET_CONTROLER`) : contrôle après rédaction, corrige localement, jamais plus de 2 essais avant `STATUER_SUR_RISQUE_RESIDUEL`.
- Pas de boucle sur le palier 1 lui-même : un problème constaté impossible arrête net (pas de rejeu automatique).

### 4. Fonctions appelées plusieurs fois

`CONFRONTATION` (au moins 3 fois, souvent plus avec les reprises) ; `CONSIGNER_CE_QUI_A_TRANCHE`, `QUALIFIER_ETAT_RESOLUTION`, `NOMMER_FAIT_QUI_FERAIT_BASCULER` (une fois par confrontation) ; `CHOISIR_MOYEN_DE_LEVEE` / `MENER_VERIFICATION` (une fois par inconnue) ; `REUTILISER_ACQUIS` (à chaque réouverture, pour ne pas rejouer le dossier déjà validé) ; `SOUMETTRE_ARBITRAGE_UTILISATEUR` (potentiellement à chaque palier, en dernier recours).

### 5. Forces / faiblesses

**Bien** : la plus simple à raisonner et à implémenter ; la terminaison se prouve par un compteur trivial ; l'ordre problème→structure→choix colle exactement à l'intuition de dépendance (on ne discute pas un choix avant d'avoir un squelette stable). Facile à auditer a posteriori (on peut relire la pile des paliers comme un journal linéaire.

**Mal** : rigide — si deux choix litigieux indépendants pointent vers le même défaut de structure, on repasse par le palier 2 deux fois au lieu de fusionner l'information ; aucune parallélisation (les confrontations de choix, bien qu'indépendantes entre elles, sont traitées séquentiellement) ; le budget est arbitraire (pourquoi 1 et 2 ?) et peut couper une réouverture légitime au profit d'un arbitrage utilisateur qu'on aurait pu éviter.

---

---


# Architecture 16 — Le pipeline à portes


**Principe en une phrase :** le plan se construit en sept phases strictement ordonnées (cadrage → état/cible → inconnues → décisions → construction des étapes → risques/gouvernance → rédaction), et chaque phase ne se termine que si une porte de vérification explicite l'y autorise ; un échec de porte renvoie à une phase amont précise, jamais plus loin que nécessaire.

### Pseudo-code

```
PHASE 0 — Recevabilité
  LIRE_TECHNIQUES_AUTORISEES
  EVALUER_EXIGENCE_TACHE            # quelles techniques autorisées méritent d'être déployées ici
  INVENTORIER_CAPACITES
  IDENTIFIER_DESTINATAIRE
  QUALIFIER_FORME_TRAVAIL
  SI travail n'est pas de forme "planification" ALORS
    DECLINER_SI_PAS_DE_PLAN ; ARRÊT
  SI on part d'un plan existant ALORS AMORCER_DEPUIS_PLAN_EXISTANT

PHASE 1 — Cadrage du besoin
  SEPARER_DEMANDE_ET_BESOIN
  DELIMITER_PERIMETRE
  CONTESTER_ENONCE_PROBLEME
  DETECTER_SOLUTION_IMPOSEE
  TRAQUER_AJOUTS_SILENCIEUX
  POUR chaque dimension de BALAYER_EXIGENCES_TACITES :
    SI exigence tacite plausible ALORS
      FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE réponse
      intégrer la réponse dans RECENSER_PREFERENCES ou RECENSER_CONTRAINTES_DURES
  RECENSER_CONTRAINTES_DURES
  RECENSER_OBLIGATIONS_FORMELLES
  EXPOSER_EXTERNALITES_CERTAINES
  ORDONNER_OBJECTIFS_SANS_ECARTER
  SI DETECTER_CONFLIT_OBJECTIFS ALORS
    SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE réponse
  FORMULER_CIBLE_OBSERVABLE
  DEFINIR_CRITERES_ACCEPTATION

  tours := 0
  TANT QUE NON VERIFIER_FIDELITE_CIBLE_BESOIN ET tours < 3 :
    reformuler la cible ; tours += 1
  SI tours == 3 ET toujours infidèle ALORS
    SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE réponse         # PORTE 1

PHASE 2 — État et chemin
  ETABLIR_ETAT_ACTUEL
  QUALIFIER_TERRITOIRE
  CHAINER_ETAT_ACTUEL_VERS_CIBLE

PHASE 3 — Résolution des inconnues
  RECENSER_INCONNUES
  POUR chaque inconnue : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION ; QUALIFIER_PORTEE_INCONNUE
  file_bloquantes := inconnues de type "construction", ORDONNER_INCONNUES_SANS_ECARTER

  TANT QUE file_bloquantes non vide :
    inconnue := extraire la plus prioritaire
    SI REUTILISER_ACQUIS(inconnue) ALORS retirer, continuer     # déjà établi ailleurs
    DISTINGUER_INDETERMINE_ET_NON_CHERCHE
    tentatives := 0
    RESOLU := faux
    TANT QUE NON RESOLU ET tentatives < nb_moyens_disponibles :
      moyen := CHOISIR_MOYEN_DE_LEVEE(inconnue, moyens déjà essayés)
      SI moyen == "question" :
        DECIDER_D_INTERROGER_UTILISATEUR
        FORMULER_QUESTION_ACTIONNABLE ; SUSPENDRE_ENQUETE_ET_DEMANDER ; ATTENDRE
      SINON SI moyen == "agent" :
        RESPECTER_CADRE_AUTORISE
        DECIDER_D_OUVRIR_UN_AGENT
        SI oui : REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT ; lancer
                 INTEGRER_RETOUR_AGENT
      SINON SI moyen == "action réversible" :
        LEVER_INCONNUE_PAR_ACTION_REVERSIBLE
      SINON :
        MENER_VERIFICATION

      CONSIGNER_PROVENANCE_FAIT ; ENONCER_LIMITES_FAIT ; JUGER_PEREMPTION_FAIT
      SI périssable ALORS INSCRIRE_REVERIFICATION_FAIT_PERISSABLE
      REFUSER_AUTO_CONFIRMATION
      SI plusieurs sources convergent ALORS DETECTER_ERREURS_CORRELEES
      SI contradiction avec un fait déjà établi :
        DETECTER_CONTRADICTION_ENTRE_SOURCES ; DETECTER_ORIGINE_COMMUNE_SOURCES
        RESOUDRE_CONTRADICTION
      SEPARER_OBSERVE_ET_SUPPOSE ; RENDRE_INCERTITUDE_VISIBLE
      RESOLU := (le moyen a effectivement levé l'inconnue)
      tentatives += 1

    SI RESOLU ALORS retirer de la file
    SINON :
      SI l'inconnue bloque la cible elle-même ALORS CONSTATER_IMPOSSIBILITE ; ARRÊT / remonter
      SINON reclasser en inconnue d'exécution (réservée pour PHASE 5)

  PORTE 2 : aucune inconnue bloquante non résolue → sinon reboucler en tête de PHASE 3

PHASE 4 — Décisions
  ETABLIR_DEPENDANCES_ENTRE_DECISIONS
  POUR chaque décision, dans l'ordre des dépendances :
    ORIENTER_CHOIX
    SI "fait manquant" ALORS ajouter l'inconnue à PHASE 3, la résoudre, puis reprendre cette décision
    SINON SI "préférence utilisateur" ALORS demander directement ; ATTENDRE
    SINON :   # vrai choix
      PRODUIRE_OPTIONS_DISTINCTES ; GARANTIR_DIVERSITE_METHODE
      CHERCHER_APPROCHES_NON_ENVISAGEES ; CHERCHER_ANTECEDENTS
      EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
      SI une hypothèse est une inconnue non levée ALORS l'envoyer en PHASE 3, revenir ici
      ISOLER_LES_EVALUATIONS
      POUR chaque option : CHOISIR_ANGLES_ATTAQUE ; ATTAQUER_UNE_OPTION
      ATTAQUER_TOUT_LE_CHAMP
      QUALIFIER_INDEPENDANCE_OBTENUE
      ARBITRER_A_L_AVEUGLE
      SI compromis matériel ALORS
        PRESENTER_ALTERNATIVES_AU_CHOIX ; SOUMETTRE_ARBITRAGE_UTILISATEUR ; ATTENDRE
    DISTINGUER_CHOIX_ET_CONSEQUENCE
    CONSIGNER_CE_QUI_A_TRANCHE ; NOMMER_FAIT_QUI_FERAIT_BASCULER
    QUALIFIER_PORTEE_DECISION ; QUALIFIER_ETAT_RESOLUTION
    CONSERVER_OPTIONS_ECARTEES

  PORTE 3 : aucune décision à l'état "non résolu" → sinon reboucler sur la décision en cause

PHASE 5 — Construction des étapes
  DERIVER_ACTIONS_DEPUIS_DECISIONS
  DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE
  POUR chaque étape mécanique : CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
  ORDONNER_PAR_PREREQUIS
  IDENTIFIER_ETAPES_SIMULTANEES ; POUR chaque groupe : VERIFIER_SIMULTANEITE_POSSIBLE
  SI le plan est trop gros ALORS DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER   # (non utilisé — voir §exclusions)
  POUR chaque étape :
    DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC
    DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE ; QUALIFIER_REVERSIBILITE
  POUR chaque inconnue d'exécution résiduelle : CONSTRUIRE_BRANCHE_CONDITIONNELLE
  RATTACHER_TOUTE_PIECE_A_SON_ORIGINE

  TANT QUE NON CONTROLER_TAILLE_DES_ETAPES :
    scinder ou fusionner les étapes fautives
  ELAGUER_ETAPES_INUTILES

  PORTE 4 : CONTROLER_TAILLE_DES_ETAPES passe ET VERIFIER_COUVERTURE_OBJECTIFS passe
            → sinon, si le trou vient d'une décision manquante, retour PHASE 4 ; sinon reboucler ici

PHASE 6 — Risques et gouvernance
  RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT
  RECENSER_INVARIANTS
  TANT QUE NON VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN :
    corriger le chemin fautif en PHASE 5 ; revenir
  ANTICIPER_TIERS_REACTIF ; STATUER_SUR_RISQUE_RESIDUEL
  RECENSER_RESSOURCES_EXECUTION ; RECENSER_DEPENDANCES_EXTERNES
  SI NON VERIFIER_FAISABILITE_PAR_EXECUTANT ALORS redescendre en PHASE 5 (ou PHASE 1 si le destinataire est mal identifié)
  REPERER_POINTS_ENGAGEMENT
  PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION
  TANT QUE NON VERIFIER_COUVERTURE_BLOQUANTS : ajouter les points manquants
  PROPOSER_AFFECTATION ; PROPOSER_MARGES ; PROPOSER_CHIFFRAGE   # jamais imposés
  PREVOIR_SUITE_EN_CAS_DE_SUCCES
  SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN

PHASE 7 — Rédaction et contrôle final
  REDIGER_PLAN ; RENDRE_ACTIONNABLE_PAR_AGENT ; ELAGUER_LA_PROSE
  REDIGER_TRACABILITE_SEPAREE ; PLACER_ET_NOMMER_LE_FICHIER

  tours := 0
  RÉPÉTER
    VERIFIER_COUVERTURE_OBJECTIFS ; VERIFIER_COHERENCE_ENSEMBLE
    VERIFIER_ADOSSEMENT_AFFIRMATIONS ; REFUSER_AUTO_CONFIRMATION
    RENDRE_INCERTITUDE_VISIBLE ; SEPARER_OBSERVE_ET_SUPPOSE
    CONTROLER_INTEGRITE_DOCUMENT ; CONTROLER_CONTENU_FINAL
    FAIRE_CONTROLER_PAR_UN_TIERS ; INTEGRER_RETOUR_AGENT
    SI un contrôle échoue :
      router la correction vers la phase concernée (fait douteux→P3, décision→P4,
      étape→P5, risque→P6, rédaction→ici) ; tours += 1
  JUSQU'À (tout passe) OU (tours == 2)
  SI tours == 2 et échec persiste ALORS SIGNALER_LES_LIMITES sur le point litigieux

  RESTITUER_EN_BREF
```

### Les boucles

- **Boucle "porte 1" (fidélité cible↔besoin, PHASE 1)** : déclenchée par un échec de `VERIFIER_FIDELITE_CIBLE_BESOIN`. Remonte seulement à la reformulation de la cible dans la même phase. Bornée à 3 essais, puis bascule sur une question utilisateur — qui, par contrat, attend une réponse et ne boucle donc jamais indéfiniment.
- **Boucle de levée d'inconnue (PHASE 3)** : déclenchée pour chaque inconnue bloquante ; essaie les moyens de `CHOISIR_MOYEN_DE_LEVEE` un à un. Ne remonte nulle part — elle est locale à l'inconnue. Termine par épuisement des moyens (liste finie), aboutissant soit à la résolution, soit à `CONSTATER_IMPOSSIBILITE`, soit à un reclassement en inconnue d'exécution.
- **Boucle "porte 2"** : si une inconnue bloquante nouvelle apparaît après la première passe, on reboucle en tête de PHASE 3. Termine car l'ensemble des inconnues bloquantes ne peut que décroître (chaque résolution retire un élément, et une inconnue reclassée en "exécution" ne revient jamais dans cette file).
- **Boucle "décision → inconnue manquante" (PHASE 4)** : une décision qui bute sur un fait manquant envoie ce fait précis en PHASE 3, puis revient sur cette même décision. Termine car le fait, une fois établi, ne peut plus être "manquant" une seconde fois.
- **Boucle "porte 3"** : rebouclage sur la décision en litige tant qu'un état "non résolu" subsiste. Bornée par le nombre fini de décisions et par `CONSTATER_IMPOSSIBILITE` en secours.
- **Boucle de calibrage des étapes (`CONTROLER_TAILLE_DES_ETAPES`, PHASE 5)** : scinde/fusionne jusqu'à convergence ; termine car chaque correction rapproche strictement de la fourchette cible (une étape trop grosse scindée ne peut être rescindée indéfiniment sur un plan fini).
- **Boucle des invariants (PHASE 6)** : `VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN` échoue → retour PHASE 5 sur le chemin fautif. Chaque passage corrige au moins une violation ; bornée par le nombre fini de chemins × invariants.
- **Boucle de contrôle final (PHASE 7)** : la plus large — elle peut router vers n'importe quelle phase amont selon la nature de l'échec. Bornée explicitement à 2 tours ; au-delà, on consigne la limite plutôt que de reboucler (`SIGNALER_LES_LIMITES`), ce qui garantit la terminaison même en cas de défaut structurel non corrigible immédiatement.

### Fonctions appelées plusieurs fois

`MENER_VERIFICATION`, `CONSIGNER_PROVENANCE_FAIT`, `ENONCER_LIMITES_FAIT`, `JUGER_PEREMPTION_FAIT`, `REFUSER_AUTO_CONFIRMATION` — une fois par fait établi, potentiellement des dizaines de fois. `CHOISIR_MOYEN_DE_LEVEE` — une fois par tentative de levée. `ATTAQUER_UNE_OPTION`/`CHOISIR_ANGLES_ATTAQUE` — une fois par option de chaque décision. `DEFINIR_ATTENDU_OBSERVABLE`, `DEFINIR_RETOUR_ARRIERE`, `EPROUVER_RETOUR_ARRIERE` — une fois par étape. `SUSPENDRE_ENQUETE_ET_DEMANDER`/`FORMULER_QUESTION_ACTIONNABLE` — à chaque fois qu'une question doit remonter (cadrage, inconnue, arbitrage). `VERIFIER_COUVERTURE_OBJECTIFS`, `VERIFIER_COHERENCE_ENSEMBLE`, `VERIFIER_ADOSSEMENT_AFFIRMATIONS` — répétées à chaque tour de contrôle final.

### Ce qu'elle laisse de côté

- `AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE` : l'ordre de traitement des décisions est fixé par `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` (prérequis), pas par un critère de fragilité concurrent — les deux critères d'ordonnancement seraient redondants dans un pipeline à un seul passage.
- `DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER` : un pipeline à portes suppose un unique passage linéaire ; découper reviendrait à instancier récursivement tout le pipeline, ce que ce squelette ne prévoit pas (mentionné comme cas exceptionnel, non structurant).
- `ARRETER_ORCHESTRATION` : chaque phase borne elle-même son effort (porte de sortie) ; il n'y a pas d'orchestration ouverte à interrompre puisque les agents de PHASE 3 traitent chacun une inconnue isolée et bornée par `BORNER_UN_AGENT`.

### Forces et faiblesses

**Fait bien :** lisibilité maximale, traçabilité de "où en est-on", garantie qu'aucune phase n'avance sur du sable (chaque porte est un point de contrôle net). Idéal pour un exécutant humain qui veut suivre le raisonnement pas à pas, et pour l'auditabilité.
**Fait mal :** rigide face aux tâches où les inconnues et les décisions sont fortement enchevêtrées — une petite décision de PHASE 4 peut faire rebondir tout le monde en PHASE 3, avec un coût de "changement de phase" à chaque aller-retour. Peu adapté aux tâches très parallélisables ou très itératives, où l'on voudrait traiter les problèmes dans leur ordre naturel d'apparition plutôt que dans l'ordre imposé des phases.

---

---


# Architecture 17 — Tournoi adversarial d'options complètes


**Principe** : produire plusieurs plans entiers matériellement différents, les attaquer et les faire arbitrer à l'aveugle les uns contre les autres, et ne raffiner que le gagnant — la comparaison porte sur des plans complets, pas sur des décisions isolées.

### Pseudo-code

```
# --- Phase 0-1 : repris du bloc de cadrage (cadrage, état, cible) ----
techniques = LIRE_TECHNIQUES_AUTORISEES()
IDENTIFIER_DESTINATAIRE(); INVENTORIER_CAPACITES(); DELIMITER_PERIMETRE()
besoin = SEPARER_DEMANDE_ET_BESOIN()
DETECTER_SOLUTION_IMPOSEE(); CONTESTER_ENONCE_PROBLEME()
SI QUALIFIER_FORME_TRAVAIL() != "planification":
    DECLINER_SI_PAS_DE_PLAN(); STOP

etat = ETABLIR_ETAT_ACTUEL()
REPEAT:
    cible = FORMULER_CIBLE_OBSERVABLE(besoin)
UNTIL VERIFIER_FIDELITE_CIBLE_BESOIN(cible, besoin)             # boucle 1
criteres = DEFINIR_CRITERES_ACCEPTATION(cible)
contraintes = RECENSER_CONTRAINTES_DURES()
obligations = RECENSER_OBLIGATIONS_FORMELLES()
invariants = RECENSER_INVARIANTS()
objectifs = ORDONNER_OBJECTIFS_SANS_ECARTER()

# --- Phase 2 : socle de faits partagé par tous les concurrents ----------
inconnues_structurantes = RECENSER_INCONNUES()      # celles qui changeraient l'espace d'options
FOR i in inconnues_structurantes:
    SI CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION(i) == "construction":
        moyen = CHOISIR_MOYEN_DE_LEVEE(i)
        SI moyen == "agent" ET NON ARRETER_ORCHESTRATION(ctx):
            PARALLELISER_ENQUETE(inconnues_structurantes)   # un agent par domaine, en //
            FOR chaque agent: REDIGER_BRIEF_AGENT(); BORNER_UN_AGENT(); RESPECTER_CADRE_AUTORISE()
            FOR chaque retour: INTEGRER_RETOUR_AGENT(retour)
        SINON:
            fait = MENER_VERIFICATION(i)  # ou CHERCHER_ANTECEDENTS(i)
        CONSIGNER_PROVENANCE_FAIT(fait); VERIFIER_ADOSSEMENT_AFFIRMATIONS(fait)
socle = faits_etablis   # réutilisé par toutes les options, jamais redémontré

# --- Phase 3 : production des concurrents --------------------------------
REPEAT au plus 2 fois:                                         # boucle 2
    options = PRODUIRE_OPTIONS_DISTINCTES(socle, cible)
    diversifie = GARANTIR_DIVERSITE_METHODE(options)
    SI NON diversifie:
        options = regenerer_options_trop_proches(options)
    supplementaire = CHERCHER_APPROCHES_NON_ENVISAGEES(options)
    SI supplementaire: options.append(supplementaire)
UNTIL diversifie OR épuisé

FOR o in options:
    REUTILISER_ACQUIS(socle)          # o part du même socle, ne le redémontre pas
    EXIGER_HYPOTHESES_EXPLICITES(o)
    DEBUSQUER_HYPOTHESES_IMPORTEES(o)
    o.squelette = DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(o)
    o.squelette = ORDONNER_PAR_PREREQUIS(o.squelette)
    DERIVER_ACTIONS_DEPUIS_DECISIONS(o)
    FOR etape in o.squelette:
        DEFINIR_ATTENDU_OBSERVABLE(etape)
        DEFINIR_RETOUR_ARRIERE(etape)

# --- Phase 4 : attaque isolée de chaque concurrent ------------------------
ISOLER_LES_EVALUATIONS(options)     # aucune option ne voit la défense d'une autre
FOR o in options:                                              # boucle 3
    angles = CHOISIR_ANGLES_ATTAQUE(o)
    faille = ATTAQUER_UNE_OPTION(o, angles)   # ne reçoit que l'action + les faits
    o.risques = RECENSER_RISQUES_PAR_ORIGINE(o)
    FOR r in o.risques:
        QUALIFIER_VRAISEMBLANCE_RISQUE(r); QUALIFIER_RAYON_IMPACT(r)
    o.attaquable = faille

echec_general = ATTAQUER_TOUT_LE_CHAMP(options)     # une fois, sur l'ensemble
SI echec_general:
    CONSTATER_IMPOSSIBILITE()  OU  retour à Phase 0 pour recontester l'énoncé
    STOP ou boucle globale (voir plus bas)

DETECTER_ERREURS_CORRELEES(options)   # les failles trouvées sont-elles vraiment indépendantes ?

# --- Phase 5 : arbitrage à l'aveugle --------------------------------------
tours_tournoi = 0
REPEAT
    tours_tournoi += 1
    verdict = ARBITRER_A_L_AVEUGLE(options anonymisées, precedence_explicite)
    independance = QUALIFIER_INDEPENDANCE_OBTENUE(verdict)

    SI verdict == "aucune option ne respecte les contraintes dures":
        SI tours_tournoi < 2:
            options = PRODUIRE_OPTIONS_DISTINCTES(socle, cible, exclure=options)  # boucle 4
            # ... ré-exécuter Phases 3 et 4 pour ces nouvelles options
        SINON:
            CONSTATER_IMPOSSIBILITE(); STOP

    SI verdict == "arbitrage de valeur, pas de fait":
        SOUMETTRE_ARBITRAGE_UTILISATEUR(options)          # bloquant
        PRESENTER_ALTERNATIVES_AU_CHOIX(options)
        verdict = reponse_utilisateur                      # tranche et sort de la boucle
UNTIL verdict.gagnant defini                                # boucle 5

gagnant = verdict.gagnant
CONSERVER_OPTIONS_ECARTEES(options, gagnant)
QUALIFIER_PORTEE_DECISION(gagnant)
NOMMER_FAIT_QUI_FERAIT_BASCULER(gagnant)
CONSIGNER_CE_QUI_A_TRANCHE(gagnant)
RATTACHER_TOUTE_PIECE_A_SON_ORIGINE(gagnant)

# --- Phase 6 : raffinement du seul gagnant --------------------------------
FOR etape in gagnant.squelette:
    SI etape est un point de choix conditionnel:
        CONSTRUIRE_BRANCHE_CONDITIONNELLE(etape)
    CONTROLER_TAILLE_DES_ETAPES(etape)
    DEFINIR_SIGNAUX_ECHEC(etape)
    ra = DEFINIR_RETOUR_ARRIERE(etape)
    EPROUVER_RETOUR_ARRIERE(ra)

simultanees = IDENTIFIER_ETAPES_SIMULTANEES(gagnant.squelette)
FOR paire in simultanees:
    SI NON VERIFIER_SIMULTANEITE_POSSIBLE(paire): retirer(paire)

QUALIFIER_REVERSIBILITE(gagnant); REPERER_POINTS_ENGAGEMENT(gagnant)
ANTICIPER_TIERS_REACTIF(gagnant)
FOR r in gagnant.risques: STATUER_SUR_RISQUE_RESIDUEL(r)

REPEAT au plus 2 fois:                                       # boucle 6
    ok = VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN(gagnant, invariants)
    SI NON ok:
        chemin_fautif = identifier_chemin()
        # ré-attaque localement ce chemin, pas tout le tournoi :
        ATTAQUER_UNE_OPTION(chemin_fautif, CHOISIR_ANGLES_ATTAQUE(chemin_fautif))
        corriger(chemin_fautif)  # branche ou étape supplémentaire
UNTIL ok OR épuisé
SI NON ok:
    SUSPENDRE_ENQUETE_ET_DEMANDER("invariant non tenable sur ce plan")

# --- Phase 7 : gouvernance -------------------------------------------------
DESIGNER_AUTORITE_AUTORISATION(); PLACER_POINTS_AUTORISATION(gagnant)
PLACER_JALONS_CONSTAT(gagnant); PLACER_POINTS_VERIFICATION(gagnant)
REPEAT: ok = VERIFIER_COUVERTURE_BLOQUANTS(gagnant); SI NON ok: ajouter_point()
UNTIL ok                                                       # boucle 7
RECENSER_DEPENDANCES_EXTERNES(); ressources = RECENSER_RESSOURCES_EXECUTION()

REPEAT au plus 2 fois:                                        # boucle 8
    faisable = VERIFIER_FAISABILITE_PAR_EXECUTANT(gagnant, ressources)
    SI NON faisable:
        SI options_ecartees a un dauphin viable:
            gagnant = deuxieme_meilleur(options_ecartees)      # rejoue Phase 6, pas tout le tournoi
        SINON:
            SIGNALER_LES_LIMITES("aucune option n'est exécutable par ce destinataire")
UNTIL faisable OR épuisé

PROPOSER_MARGES(); PROPOSER_AFFECTATION(); PROPOSER_CHIFFRAGE()

# --- Phase 8 : nettoyage et contrôle final ---------------------------------
ELAGUER_ETAPES_INUTILES(gagnant); ISOLER_LE_HORS_PLAN(); SIGNALER_LES_LIMITES()
PREVOIR_SUITE_EN_CAS_DE_SUCCES()

avis_tiers = FAIRE_CONTROLER_PAR_UN_TIERS(gagnant)
INTEGRER_RETOUR_AGENT(avis_tiers)
DETECTER_ERREURS_CORRELEES(avis_tiers, verdicts_precedents)  # le tiers a-t-il un vrai chemin distinct ?

REPEAT au plus 2 fois:                                        # boucle 9
    VERIFIER_COUVERTURE_OBJECTIFS(objectifs, gagnant)
    VERIFIER_ADOSSEMENT_AFFIRMATIONS(gagnant)
    REFUSER_AUTO_CONFIRMATION()
    RENDRE_INCERTITUDE_VISIBLE()
    ok = VERIFIER_COHERENCE_ENSEMBLE(gagnant) ET CONTROLER_CONTENU_FINAL() ET CONTROLER_INTEGRITE_DOCUMENT()
UNTIL ok OR épuisé
SI NON ok: SUSPENDRE_ENQUETE_ET_DEMANDER()

ELAGUER_LA_PROSE(); RENDRE_ACTIONNABLE_PAR_AGENT()
REDIGER_PLAN(); REDIGER_TRACABILITE_SEPAREE()
PLACER_ET_NOMMER_LE_FICHIER(); RESTITUER_EN_BREF()
```

### Les boucles

- **Boucle 1** : fidélité cible/besoin, comme dans le bloc de cadrage.
- **Boucle 2** : régénération des options tant qu'elles ne sont pas méthodologiquement distinctes ; bornée à 2 tours.
- **Boucle 3** (implicite, `FOR` sur les options) : l'attaque est répétée pour chaque concurrent, isolément (`ISOLER_LES_EVALUATIONS`).
- **Boucle 4/5** (tournoi) : déclenchée par un arbitrage sans gagnant clair (toutes violent une contrainte dure) ou par un vrai désaccord de valeur ; remonte à la production de nouvelles options (jamais à un simple ajustement local) ; bornée à 2 tours de régénération puis `CONSTATER_IMPOSSIBILITE`, ou tranchée immédiatement par l'utilisateur si c'est un arbitrage de valeur.
- **Boucle 6** (invariants sur le gagnant) : corrige localement le chemin fautif en le ré-attaquant spécifiquement, sans relancer le tournoi ; bornée à 2 tentatives.
- **Boucle 8** (faisabilité côté exécutant) : si le gagnant n'est pas exécutable, on ne relance pas tout le tournoi — on repêche le dauphin déjà conservé par `CONSERVER_OPTIONS_ECARTEES`, ce qui borne intrinsèquement la boucle au nombre d'options produites.
- **Boucles 7, 9** : vérifications locales classiques, bornées à 2 passes.

Terminaison garantie par : la borne numérique sur chaque boucle, plus le fait que la boucle 8 consomme un ensemble fini et décroissant d'options écartées (elle ne peut pas tourner plus de fois qu'il y a d'options produites).

### Fonctions appelées plusieurs fois

- `PRODUIRE_OPTIONS_DISTINCTES` : à la production initiale et, potentiellement, en régénération après un tournoi sans gagnant.
- `ATTAQUER_UNE_OPTION` : une fois par option au tour principal, puis une fois de plus, ciblée, si un invariant casse sur le gagnant.
- `CHOISIR_ANGLES_ATTAQUE` : une fois par option attaquée.
- `VERIFIER_FAISABILITE_PAR_EXECUTANT` : potentiellement plusieurs fois si l'on doit redescendre dans la liste des dauphins.
- `CONSIGNER_PROVENANCE_FAIT` / `VERIFIER_ADOSSEMENT_AFFIRMATIONS` : pour chaque fait du socle partagé, puis à nouveau en contrôle final sur l'ensemble du plan raffiné.
- `VERIFIER_COHERENCE_ENSEMBLE` : une fois par tentative de la boucle 9.

### Ce que ça fait bien / mal

**Bien** : les options comparées sont de vrais plans entiers, pas des variantes de vocabulaire — `GARANTIR_DIVERSITE_METHODE` le garantit explicitement ; l'isolement des évaluations (`ISOLER_LES_EVALUATIONS`, `ARBITRER_A_L_AVEUGLE`) protège contre la contamination et le biais de plaidoyer ; avoir des dauphins déjà connus (`CONSERVER_OPTIONS_ECARTEES`) rend la boucle de repêchage (8) très bon marché.
**Mal** : coûteux — chaque option est développée jusqu'à un squelette complet avant d'être potentiellement jetée ; le socle partagé (Phase 2) doit être vraiment neutre, sinon il biaise silencieusement toutes les options de la même façon sans que le tournoi puisse le détecter ; les décisions fines à l'intérieur du plan gagnant ne bénéficient d'aucune mise en concurrence, seulement le choix de haut niveau.

### Fonctions volontairement laissées de côté
`QUALIFIER_TERRITOIRE`, `DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE`, `CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE` : ces fonctions instruisent un doute nœud par nœud sur le caractère mécanique d'une étape — orthogonal au principe ici, qui compare des plans entiers plutôt que d'interroger chaque étape individuellement.

---

---


# Architecture 18 — Vagues par dépendances


**Principe en une phrase** : au lieu de traiter toutes les inconnues puis toutes les décisions, le plan est construit par vagues successives de décisions mutuellement indépendantes (couches du graphe de dépendances), chaque vague menant son propre cycle enquête→décision→construction avant que la vague suivante ne s'ouvre.

### Pseudo-code

```
PHASE 0 — CADRAGE ET CARTOGRAPHIE (une seule fois)
  LIRE_TECHNIQUES_AUTORISEES ; INVENTORIER_CAPACITES ; RECENSER_RESSOURCES_EXECUTION
  IDENTIFIER_DESTINATAIRE ; SEPARER_DEMANDE_ET_BESOIN ; CONTESTER_ENONCE_PROBLEME
  DETECTER_SOLUTION_IMPOSEE
  DELIMITER_PERIMETRE ; RECENSER_CONTRAINTES_DURES ; RECENSER_OBLIGATIONS_FORMELLES
  RECENSER_PREFERENCES
  ORDONNER_OBJECTIFS_SANS_ECARTER ; DETECTER_CONFLIT_OBJECTIFS ; TRAQUER_AJOUTS_SILENCIEUX
  BALAYER_EXIGENCES_TACITES ; EXPOSER_EXTERNALITES_CERTAINES
  FORMULER_CIBLE_OBSERVABLE ; DEFINIR_CRITERES_ACCEPTATION ; VERIFIER_FIDELITE_CIBLE_BESOIN
  DECLINER_SI_PAS_DE_PLAN ; QUALIFIER_FORME_TRAVAIL
  ETABLIR_ETAT_ACTUEL ; CHAINER_ETAT_ACTUEL_VERS_CIBLE
  RECENSER_INCONNUES ; POUR chaque : CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION
  Construire le graphe provisoire des points de décision :
      ETABLIR_DEPENDANCES_ENTRE_DECISIONS
      POUR chaque nœud : QUALIFIER_TERRITOIRE  (familier → peut être groupé plus tard ;
                                                 reconfigurant → doit rester isolé en vague)
  --- CONTRÔLE DE SORTIE 0 ---
  SI graphe cyclique non cassable ou périmètre infidèle au besoin : boucler dans la phase
  SI aucune décision identifiable : DECLINER_SI_PAS_DE_PLAN

graphe.marquer_tous_les_noeuds("ouvert")
w = 0

TANT QUE il reste des nœuds "ouvert" :   // -- boucle de vagues, bornée par le nb de couches --
  w += 1
  vague = { nœuds "ouvert" dont tous les prédécesseurs sont "fermé" }

  --- B1 : ENQUÊTE LOCALE (limitée aux inconnues alimentant vague w) ---
  ORDONNER_INCONNUES_SANS_ECARTER(vague) ; QUALIFIER_PORTEE_INCONNUE(vague)
  DISTINGUER_INDETERMINE_ET_NON_CHERCHE(vague)
  SI les nœuds de la vague sont réellement indépendants (confirmé par le graphe) :
      PARALLELISER_ENQUETE : un agent par domaine de décision de la vague
      POUR chaque agent : REDIGER_BRIEF_AGENT ; BORNER_UN_AGENT
  POUR chaque inconnue bloquante de la vague :
      CHOISIR_MOYEN_DE_LEVEE → MENER_VERIFICATION / LEVER_INCONNUE_PAR_ACTION_REVERSIBLE /
          CHERCHER_ANTECEDENTS / DECIDER_D_INTERROGER_UTILISATEUR+FORMULER_QUESTION_ACTIONNABLE
      INTEGRER_RETOUR_AGENT ; REFUSER_AUTO_CONFIRMATION
      CONSIGNER_PROVENANCE_FAIT ; ENONCER_LIMITES_FAIT ; SEPARER_OBSERVE_ET_SUPPOSE
      JUGER_PEREMPTION_FAIT → INSCRIRE_REVERIFICATION_FAIT_PERISSABLE si périssable
      RENDRE_INCERTITUDE_VISIBLE
  DETECTER_CONTRADICTION_ENTRE_SOURCES → DETECTER_ORIGINE_COMMUNE_SOURCES → RESOUDRE_CONTRADICTION
  ARRETER_ORCHESTRATION (dès qu'un agent de plus ne changerait rien pour cette vague)
  VERIFIER_ADOSSEMENT_AFFIRMATIONS
  --- CONTRÔLE B1 ---
  SI une inconnue résolue révèle un nœud/une arête absente du graphe :
      RETOUR → PHASE 0 (insérer le nœud/l'arête, recalculer les couches ; borné par le
      nombre fini d'arêtes du graphe final — chaque passage en ajoute une, n'en retire jamais)
  SI inconnue bloquante irréductible : SUSPENDRE_ENQUETE_ET_DEMANDER

  --- B2 : DÉCISION LOCALE (uniquement les décisions de la vague w) ---
  POUR chaque décision de la vague :
      PRODUIRE_OPTIONS_DISTINCTES ; GARANTIR_DIVERSITE_METHODE
      CHERCHER_APPROCHES_NON_ENVISAGEES
      EXIGER_HYPOTHESES_EXPLICITES ; DEBUSQUER_HYPOTHESES_IMPORTEES
      ISOLER_LES_EVALUATIONS ; CHOISIR_ANGLES_ATTAQUE ; ATTAQUER_UNE_OPTION
      ATTAQUER_TOUT_LE_CHAMP → SI tout échoue : CONSTATER_IMPOSSIBILITE
      ARBITRER_A_L_AVEUGLE
      ORIENTER_CHOIX → PRESENTER_ALTERNATIVES_AU_CHOIX / SOUMETTRE_ARBITRAGE_UTILISATEUR /
                        DECIDER_D_INTERROGER_UTILISATEUR selon le cas
      AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE ; DISTINGUER_CHOIX_ET_CONSEQUENCE
      QUALIFIER_PORTEE_DECISION ; NOMMER_FAIT_QUI_FERAIT_BASCULER
      CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_ETAT_RESOLUTION ; CONSERVER_OPTIONS_ECARTEES
  VERIFIER_COHERENCE_ENSEMBLE (cumulée : vagues déjà fermées + vague w)
  --- CONTRÔLE B2 ---
  SI décision impossible faute de fait : RETOUR → B1 de la même vague w
  SI l'arbitrage révèle qu'une décision de la vague w contraint en réalité une décision
     déjà fermée en vague w' (w' < w) :
      RETOUR → réouvrir la vague w' précisément (pas tout le pipeline),
      rejouer B2 pour ce nœud, propager
      (borné : ETABLIR_DEPENDANCES_ENTRE_DECISIONS ne peut gagner que des arêtes correctes,
       jamais en reperdre — au plus E corrections, E = nombre final d'arêtes)

  --- B3 : CONSTRUCTION LOCALE ---
  DERIVER_ACTIONS_DEPUIS_DECISIONS(vague) ; ORDONNER_PAR_PREREQUIS (raccordé à la queue
      des vagues précédentes)
  IDENTIFIER_ETAPES_SIMULTANEES ; VERIFIER_SIMULTANEITE_POSSIBLE
  DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE ; CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE
  CONTROLER_TAILLE_DES_ETAPES ; ELAGUER_ETAPES_INUTILES
  DEFINIR_ATTENDU_OBSERVABLE ; DEFINIR_SIGNAUX_ECHEC
  DEFINIR_RETOUR_ARRIERE ; EPROUVER_RETOUR_ARRIERE
  CONSTRUIRE_BRANCHE_CONDITIONNELLE
  REUTILISER_ACQUIS (facts/étapes des vagues antérieures)
  RATTACHER_TOUTE_PIECE_A_SON_ORIGINE  (marque provenance = vague w, essentiel pour cibler
      les retours ultérieurs)
  --- CONTRÔLE B3 ---
  SI une décision "tranchée" ne peut être traduite en action concrète et bornée :
      RETOUR → B2 de la même vague w

  Fermer la vague w : marquer ses nœuds "fermé" dans le graphe

// -- fin de la boucle de vagues --

PHASE C — ASSEMBLAGE ET ASSURANCE GLOBALE (une seule fois)
  SI plan trop volumineux/fragmenté : DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER
  VERIFIER_COHERENCE_ENSEMBLE (globale, toutes vagues confondues)
  RECENSER_RISQUES_PAR_ORIGINE ; QUALIFIER_VRAISEMBLANCE_RISQUE ; QUALIFIER_RAYON_IMPACT ;
      QUALIFIER_REVERSIBILITE ; ANTICIPER_TIERS_REACTIF
  RECENSER_INVARIANTS ; VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN (plan assemblé complet)
  STATUER_SUR_RISQUE_RESIDUEL ; PROPOSER_MARGES
  RECENSER_DEPENDANCES_EXTERNES ; VERIFIER_FAISABILITE_PAR_EXECUTANT
  REPERER_POINTS_ENGAGEMENT ; PLACER_POINTS_AUTORISATION ; DESIGNER_AUTORITE_AUTORISATION
  PLACER_JALONS_CONSTAT ; PLACER_POINTS_VERIFICATION ; VERIFIER_COUVERTURE_BLOQUANTS
  PROPOSER_AFFECTATION ; PROPOSER_CHIFFRAGE
  EVALUER_EXIGENCE_TACHE ; RESPECTER_CADRE_AUTORISE
  --- CONTRÔLE DE SORTIE C ---
  SI défaut trouvé : RETOUR → la vague exacte responsable, identifiée via
      RATTACHER_TOUTE_PIECE_A_SON_ORIGINE (B2 si décision en cause, B3 si construction)
      (budget d'1 retour "assurance" par vague, au-delà : CONSTATER_IMPOSSIBILITE ou
      SUSPENDRE_ENQUETE_ET_DEMANDER)

PHASE D — RÉDACTION & CONTRÔLE FINAL
  REDIGER_PLAN ; REDIGER_TRACABILITE_SEPAREE ; SIGNALER_LES_LIMITES ; ISOLER_LE_HORS_PLAN
  PREVOIR_SUITE_EN_CAS_DE_SUCCES ; ELAGUER_LA_PROSE ; RENDRE_ACTIONNABLE_PAR_AGENT
  VERIFIER_COUVERTURE_OBJECTIFS ; CONTROLER_CONTENU_FINAL ; CONTROLER_INTEGRITE_DOCUMENT
  FAIRE_CONTROLER_PAR_UN_TIERS
  PLACER_ET_NOMMER_LE_FICHIER
  --- CONTRÔLE DE SORTIE D ---
  SELON défaut : RETOUR → vague précise / PHASE C / PHASE 0 (mêmes règles de borne qu'en A)

PHASE E — LIVRAISON
  RESTITUER_EN_BREF
```

### Les boucles
- **Boucle de vagues** elle-même : ce n'est pas un "retour d'échec", c'est le moteur normal de l'algorithme — elle se termine nécessairement car chaque itération ferme au moins un nœud du graphe fini de décisions.
- **B1→B1 / B2→B2** : bouclage local dans la vague en cours, borné par le nombre fini d'inconnues/décisions de cette vague.
- **B1/B2→Phase 0** : correction du graphe lui-même, bornée par le nombre fini d'arêtes que le graphe final peut recevoir (aucune arête n'est jamais retirée, donc pas de cycle infini).
- **B2→vague antérieure w'** : la signature de cette architecture — un retour très ciblé qui rouvre une vague déjà fermée, jamais tout le pipeline ; borné pour la même raison (monotonie du graphe).
- **PhaseC/PhaseD→vague w** : retour ciblé grâce à la provenance enregistrée par `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE`, plafonné à un budget global.

### Fonctions appelées plusieurs fois
Tout le contenu de B1/B2/B3 est rejoué **une fois par vague** (au lieu d'une fois pour tout le plan) : `PRODUIRE_OPTIONS_DISTINCTES`, `ATTAQUER_UNE_OPTION`, `CONSIGNER_CE_QUI_A_TRANCHE`, `DEFINIR_ATTENDU_OBSERVABLE`, etc. `ETABLIR_DEPENDANCES_ENTRE_DECISIONS` est consulté à chaque début de vague pour calculer la couche suivante. `REUTILISER_ACQUIS` et `RATTACHER_TOUTE_PIECE_A_SON_ORIGINE` sont appelés à chaque vague. `VERIFIER_COHERENCE_ENSEMBLE` est appelé de façon incrémentale (à chaque fermeture de vague, portée croissante) puis une fois de façon globale en phase C.

### Ce qu'elle fait bien / mal
Elle s'adapte à un travail hétérogène : les parties simples (peu d'inconnues, décisions indépendantes) se ferment vite en vague 1 sans attendre le reste ; elle permet un vrai parallélisme (`PARALLELISER_ENQUETE` par vague, puisque les décisions d'une même vague sont par construction indépendantes) ; ses retours sont chirurgicaux (on rouvre une vague, pas une catégorie fonctionnelle entière). En contrepartie, elle est plus complexe à implémenter — maintenir et corriger un graphe de dépendances vivant est lui-même source d'erreur — et sur un problème en réalité linéaire, le découpage en vagues ajoute de la charge sans bénéfice ; la cohérence globale n'est vérifiée complètement qu'en phase C, donc des incohérences transverses entre vagues éloignées peuvent rester longtemps invisibles.

### Fonctions laissées de côté
`AMORCER_DEPUIS_PLAN_EXISTANT` : l'architecture suppose une entrée par demande fraîche, pas une reprise depuis un plan existant (même emplacement possible en Phase 0, non modélisé ici pour rester net).

---

---
