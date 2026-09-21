# Dix-huit architectures candidates — pseudo-code seul

Chacune décrit une façon d'enchaîner les fonctions unitaires du système pour
produire un plan. Elles ont été produites indépendamment, par des auteurs qui
ne se voyaient pas. L'ordre est aléatoire et ne porte aucune information.

Seul le pseudo-code est reproduit ici : toute prose d'accompagnement a été
retirée.

---


# Architecture 01 — Pipeline à sas

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

---


# Architecture 02 — Deux vagues et un filet de sécurité global

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

---


# Architecture 03 — Colonne vertébrale contradictoire

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

---


# Architecture 04 — Agenda piloté par un graphe de dépendances

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

---


# Architecture 05 — La file de travail pilotée par les dépendances

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

---


# Architecture 06 — Chaînage par dépendances

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

---


# Architecture 07 — L'arbre des objectifs

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

---


# Architecture 08 — File de travail à point fixe

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

---


# Architecture 09 — Cascade de passes contradictoires

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

---


# Architecture 10 — L'épreuve récursive (produire / attaquer / arbitrer, à toutes les échelles)

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

---


# Architecture 11 — L'arbre d'enquête

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

---


# Architecture 12 — Spirale incrémentale (squelette puis épaississement)

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

---


# Architecture 13 — Le tournoi d'options

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

---


# Architecture 14 — Pipeline à jalons verrouillés

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

---


# Architecture 15 — Cascade à paliers bornés

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

---


# Architecture 16 — Le pipeline à portes

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

---


# Architecture 17 — Tournoi adversarial d'options complètes

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

---


# Architecture 18 — Vagues par dépendances

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

---
