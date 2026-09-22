# Fonctions unitaires disponibles

On dispose d'un système qui met à disposition les **133 fonctions unitaires** listées ci-dessous.
Chacune est atomique.
Chacune peut être appelée **autant de fois que nécessaire, à n'importe quel moment**, sur n'importe quel objet.

Le système est un agent LLM outillé.
Il sait lire, écrire, inspecter un système cible, chercher en ligne, ouvrir des sous-agents isolés, et interroger l'utilisateur.

**Le système doit produire un plan d'action détaillé, écrit dans un fichier.**
Il ne conduit pas l'exécution de ce plan : il le livre.

Quelques propriétés du système, qui contraignent toute architecture :

- Il a le droit d'enquêter avant de planifier — lire, inspecter, chercher, ouvrir des agents, interroger l'utilisateur, mener une action réversible et bornée.
  Il n'a pas le droit d'exécuter un engagement du plan.
- Rien n'est reporté à l'exécution : tout ce qui peut être vérifié, investigué, demandé ou décidé l'est avant que le plan soit écrit.
- Toute inconnue est réputée résoluble avant l'écriture du plan, au besoin en remontant à l'utilisateur.
  Classer une inconnue comme ne pouvant être levée qu'à l'exécution est l'exception : ce classement doit être contrôlé par le système, jamais décidé en silence.
- On ne sollicite jamais l'utilisateur sur ce que le système peut établir en autonomie.
  La question est un dernier recours.
- L'utilisateur décide, le système rapporte.
  Quand le système pose une question, il attend la réponse ; il ne continue pas sur une valeur par défaut.
- Le système ne raisonne jamais en coût.
  Une configuration dit quelles techniques sont autorisées.
- Le plan suit un template au format fixe, qui est donné au système.
  L'architecture n'a pas à définir ce format ; seul le contenu du plan grossit avec la complexité.
- Le livrable du système est le plan.
  Ce qui se passe après — validation par l'utilisateur, exécution, rejeu — est hors du système.

**L'ordre de la liste ci-dessous est aléatoire et ne porte aucune information.**
Les identifiants sont sémantiques : ils décrivent ce que la fonction fait, pas sa place dans un quelconque enchaînement.

---

**`ATTAQUER_UNE_OPTION`**
Chercher les modes de défaillance d'une option sans la défendre, en ne recevant que l'action et les faits.

**`PLACER_JALONS_CONSTAT`**
Placer des points où l'avancement se constate, distincts des autorisations.

**`DELIMITER_PERIMETRE`**
Établir ce qui est dedans et ce qui est dehors.

**`SEPARER_DEMANDE_ET_BESOIN`**
Distinguer ce qui est demandé de ce qui est voulu.

**`CLASSER_INCONNUE_CONSTRUCTION_OU_EXECUTION`**
Distinguer l'inconnue qui bloque l'écriture du plan, à lever avant de rédiger, de celle qui ne se révélera qu'à l'exécution et que le plan doit absorber.

**`STATUER_SUR_RISQUE_RESIDUEL`**
Dire d'un risque restant s'il est contenu, accepté, ou délégué à quelqu'un.

**`VERIFIER_COHERENCE_ENSEMBLE`**
Vérifier que l'assemblage tient, alors qu'un plan fait de bons morceaux peut être incohérent.

**`QUALIFIER_VRAISEMBLANCE_RISQUE`**
Qualifier la probabilité d'occurrence d'un risque, et non seulement son impact.

**`PROPOSER_MARGES`**
Offrir à l'utilisateur de dimensionner des réserves et de dire où elles sont placées. Jamais produit d'office.

**`INVENTORIER_CAPACITES`**
Établir de quoi on dispose : lecture, écriture, exécution, accès au système cible, sources, sous-agents, utilisateur joignable.

**`RECENSER_RESSOURCES_EXECUTION`**
Recenser le temps, le budget, les personnes, les accès, les créneaux dont disposera l'exécution du plan.

**`DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER`**
Découper un travail trop gros en parties traitées séparément, puis recomposer.

**`REUTILISER_ACQUIS`**
Ne pas re-démontrer ce qui est déjà établi et encore valide.

**`INSCRIRE_REVERIFICATION_FAIT_PERISSABLE`**
Transformer un fait jugé périssable en action de re-vérification inscrite juste avant l'étape qui en dépend.

**`ETABLIR_DEPENDANCES_ENTRE_DECISIONS`**
Établir quelles décisions en conditionnent d'autres, et lesquelles trancher en premier.

**`EXIGER_HYPOTHESES_EXPLICITES`**
Obliger chaque option à nommer ce qu'elle suppose, et refuser celle qui comble une inconnue tacitement.

**`LEVER_INCONNUE_PAR_ACTION_REVERSIBLE`**
Lever une inconnue en agissant, de façon réversible et bornée, quand aucun autre moyen ne la lève.

**`SIGNALER_LES_LIMITES`**
Dire ce que le plan ne couvre pas et ce qui a été volontairement laissé de côté.

**`CONSIGNER_PROVENANCE_FAIT`**
Consigner un fait établi avec son origine et son localisateur.

**`REDIGER_TRACABILITE_SEPAREE`**
Écrire, dans un fichier distinct du plan, ce qui a été tranché et par quoi, ce qui a été vérifié et avec quelles limites, ce qui a été attaqué et ce qui subsiste.

**`CHERCHER_ALTERNATIVE_A_UN_PAS_DIT_MECANIQUE`**
Sur une étape classée comme conséquence mécanique, chercher comment on aurait pu faire autrement.

**`RENDRE_INCERTITUDE_VISIBLE`**
Garantir que rien d'incertain n'est présenté comme acquis.

**`DEFINIR_ATTENDU_OBSERVABLE`**
Nommer l'observable précis qui dit qu'une étape a réussi.

**`SEPARER_OBSERVE_ET_SUPPOSE`**
Distinguer ce qui a été constaté de ce qui est présumé.

**`SUSPENDRE_ENQUETE_ET_DEMANDER`**
Constater qu'une inconnue bloquante ne se lève pas seule, suspendre, et remonter à l'utilisateur.

**`RENDRE_ACTIONNABLE_PAR_AGENT`**
Rendre le plan exploitable par un exécutant automatique.

**`CONTROLER_TAILLE_DES_ETAPES`**
Vérifier que les étapes sont à la bonne taille : assez fines pour qu'un attendu unique les valide, assez grosses pour que l'exécutant n'ait pas à re-planifier.

**`CONSTATER_IMPOSSIBILITE`**
Reconnaître que tous les chemins violent une contrainte dure, ou que la cible est inatteignable telle qu'elle est formulée.

**`ETABLIR_ETAT_ACTUEL`**
Établir d'où l'on part.

**`INTEGRER_RETOUR_AGENT`**
Reprendre ce qu'un agent rapporte sans le traiter comme une preuve du seul fait qu'il l'affirme.

**`CONSERVER_OPTIONS_ECARTEES`**
Enregistrer ce qui a été écarté et si cela reste viable.

**`REFUSER_AUTO_CONFIRMATION`**
Refuser de traiter comme vérifié ce qui vient de son propre raisonnement ou de l'affirmation d'un agent.

**`CONSTRUIRE_BRANCHE_CONDITIONNELLE`**
Écrire un chemin alternatif avec son critère de déclenchement et son repli.

**`DETECTER_ERREURS_CORRELEES`**
Avant de traiter un accord comme une confirmation, vérifier que les chemins de preuve étaient distincts.

**`CHOISIR_MOYEN_DE_LEVEE`**
Choisir le moyen le moins cher suffisant pour lever une inconnue : inspection, source, calcul, test, question, action.

**`DEFINIR_RETOUR_ARRIERE`**
Nommer le retour arrière d'une étape, ou constater qu'il n'existe pas.

**`EXPOSER_EXTERNALITES_CERTAINES`**
Recenser ce que la demande entraîne de sûr hors de son périmètre — surcoût, précédent créé, couplage introduit — et s'assurer que le demandeur l'a compris.

**`PROPOSER_AFFECTATION`**
Offrir à l'utilisateur de désigner qui exécute quoi. Jamais produit d'office.

**`FORMULER_QUESTION_ACTIONNABLE`**
Poser une question tranchable, et exposer ce qui se joue derrière elle : ce qui change selon la réponse, pour que l'utilisateur puisse répondre même lorsqu'il ne connaissait pas l'enjeu.

**`RESPECTER_CADRE_AUTORISE`**
Respecter les techniques autorisées et le processus établi ; ne pas improviser de lancement d'agent non prévu.

**`RATTACHER_TOUTE_PIECE_A_SON_ORIGINE`**
Rattacher toute pièce du plan qu'aucune option n'avait proposée à ce dont elle dérive.

**`VERIFIER_FIDELITE_CIBLE_BESOIN`**
Vérifier que la cible mesure bien le besoin, et non une chose satisfaisable sans produire l'effet voulu.

**`TRAQUER_AJOUTS_SILENCIEUX`**
Détecter les objectifs qu'on s'est ajoutés à soi-même, non demandés.

**`DESIGNER_AUTORITE_AUTORISATION`**
Dire qui peut donner une autorisation, et s'assurer que ce n'est pas celui qui exécute.

**`RECENSER_INCONNUES`**
Lister ce qu'on ne sait pas.

**`QUALIFIER_RAYON_IMPACT`**
Dire jusqu'où s'étend la casse : combien de systèmes, d'utilisateurs, de processus en aval sont touchés.

**`REPERER_POINTS_ENGAGEMENT`**
Identifier où le plan ferme des options ou consomme des ressources.

**`DECLINER_SI_PAS_DE_PLAN`**
Énoncer qu'il n'y a pas de problème de planification ici, et s'arrêter.

**`QUALIFIER_ETAT_RESOLUTION`**
Dire dans quel état un point est laissé : tranché, tranché avec compromis, branché, en attente, non résolu, invalide.

**`ISOLER_LE_HORS_PLAN`**
Garder séparé ce qui mérite d'être noté sans faire partie du chemin.

**`ORDONNER_OBJECTIFS_SANS_ECARTER`**
Recenser les objectifs multiples et les ordonner. La priorité ordonne le travail, elle n'abandonne aucun objectif.

**`RECENSER_RISQUES_PAR_ORIGINE`**
Distinguer les risques préexistants, ceux que le plan introduit, ceux qui subsistent après mitigation, ceux qu'on sait ignorer.

**`BORNER_UN_AGENT`**
Donner à un agent une condition d'arrêt explicite.

**`ELAGUER_ETAPES_INUTILES`**
Retirer toute étape dont l'absence ne changerait pas le résultat.

**`DETECTER_CONFLIT_OBJECTIFS`**
Repérer des objectifs qui ne peuvent pas être atteints ensemble. Un conflit est un symptôme, pas un arbitrage à rendre.

**`IDENTIFIER_DESTINATAIRE`**
Savoir qui lira le plan et qui l'exécutera, avec quel contexte.

**`BALAYER_EXIGENCES_TACITES`**
Passer le problème au crible de dimensions non mentionnées (sécurité, montée en charge, maintenabilité, coût, accessibilité) pour faire remonter une exigence tacite. Faire remonter et demander, jamais imposer.

**`QUALIFIER_PORTEE_INCONNUE`**
Dire, pour une inconnue, ce qu'elle peut changer.

**`ENONCER_LIMITES_FAIT`**
Dire ce qu'un fait ne prouve pas.

**`QUALIFIER_FORME_TRAVAIL`**
Distinguer le travail dont le chemin est connu ou découvrable de celui dont la valeur consiste à lever des inconnues.

**`DETECTER_CONTRADICTION_ENTRE_SOURCES`**
Repérer que deux sources ne disent pas la même chose.

**`ORDONNER_INCONNUES_SANS_ECARTER`**
Classer les inconnues par ce qu'elles peuvent changer et par le coût de leur levée. On ordonne, on n'écarte pas.

**`LIRE_MODELE_DE_PLAN`**
Lire le modèle de document imposé au plan livré, avant toute rédaction.

**`EPROUVER_AUTONOMIE_DU_TEXTE`**
Soumettre le plan seul à un lecteur qui n'a rien vu de l'enquête, et lui demander non pas de l'exécuter mais de dire où il devrait redemander quelque chose.

**`ISOLER_LES_EVALUATIONS`**
Empêcher la contamination entre évaluations censées être indépendantes : ne jamais montrer une proposition à l'autre avant qu'elles soient formées, ne jamais donner à l'attaquant le plaidoyer de ce qu'il attaque.

**`RECENSER_CONTRAINTES_DURES`**
Recenser ce que le plan n'a pas le droit de franchir.

**`GARANTIR_DIVERSITE_METHODE`**
S'assurer que les options diffèrent par la méthode ou l'angle d'optimisation, et non par le vocabulaire.

**`CONTROLER_REPORT_A_L_EXECUTION`**
Vérifier qu'une inconnue classée « à lever seulement à l'exécution » l'est à bon droit : indéterminable maintenant, aucun moyen disponible, signal de révélation nommable, portée limitée — et le classement n'est pas auto-confirmé.

**`VERIFIER_FAISABILITE_PAR_EXECUTANT`**
Vérifier que celui qui recevra le plan a les accès, outils, compétences et contexte que le plan présuppose.

**`DEFINIR_SIGNAUX_ECHEC`**
Nommer ce qu'on verra en premier si une étape échoue.

**`PLACER_POINTS_AUTORISATION`**
Décider où une autorisation extérieure est requise avant de continuer.

**`RESTITUER_EN_BREF`**
Dire en quelques lignes ce qui a été produit, ce qui attend l'utilisateur, et où c'est.

**`PRESENTER_ALTERNATIVES_AU_CHOIX`**
Présenter deux options de haut niveau côte à côte quand l'utilisateur doit trancher lui-même.

**`QUALIFIER_PORTEE_DECISION`**
Dire ce qui change si la réponse à ce point est fausse.

**`REPRENDRE_PASSE_PRECEDENTE`**
Reconnaître un plan issu d'une exécution antérieure du skill, et reprendre son registre : faits établis avec leur provenance, décisions closes, limites énoncées — sans redériver le besoin ni réétablir ce qui tient.

**`AMORCER_DEPUIS_PLAN_EXISTANT`**
Partir d'un plan existant plutôt que d'une demande, en dérivant le besoin du plan lui-même.

**`NOMMER_FAIT_QUI_FERAIT_BASCULER`**
Nommer, pour un point tranché, le fait non établi qui le ferait basculer.

**`RECENSER_PREFERENCES`**
Recenser ce qui est souhaité sans être exigé, et le tenir séparé des contraintes.

**`VERIFIER_COUVERTURE_BLOQUANTS`**
Vérifier que toute partie capable de bloquer reçoit un point de passage dans le plan.

**`RECENSER_OBLIGATIONS_FORMELLES`**
Identifier les autorisations formelles requises. Les signaler et demander, jamais les imposer.

**`CONTESTER_ENONCE_PROBLEME`**
Mettre en cause le problème tel qu'il est posé, avant de résoudre quoi que ce soit à l'intérieur.

**`CHERCHER_ANTECEDENTS`**
Chercher ce qui a déjà été fait pour des besoins similaires : en local, dans le dépôt, en ligne.

**`ATTAQUER_TOUT_LE_CHAMP`**
Chercher ce qui ferait échouer toutes les options à la fois, et les conditions d'un problème mal posé.

**`IDENTIFIER_ETAPES_SIMULTANEES`**
Identifier les étapes qui peuvent être menées de front.

**`REDIGER_BRIEF_AGENT`**
Donner à un agent le périmètre, les faits établis, la question et le format attendu — et rien qui oriente. Ce qui est déjà établi y voyage, pour que personne ne refasse le travail. Un agent qui juge reçoit les critères ET le besoin, puis relire ce brief pour en retirer ce qui oriente : ordre de présentation, qualificatif, fait donné avec sa conclusion, trace d'une proposition rivale.

**`DISTINGUER_ETAPE_ESSENTIELLE_ET_MECANIQUE`**
Distinguer l'étape qui mérite d'exister de celle qui n'est que la suite automatique d'une autre.

**`VERIFIER_INVARIANTS_SUR_TOUT_CHEMIN`**
Vérifier qu'aucun chemin du plan, branches comprises, n'atteint la cible en franchissant une contrainte dure.

**`AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE`**
Entre deux ordres également valides, choisir celui qui met à l'épreuve l'hypothèse la plus fragile en premier.

**`REDIGER_PLAN`**
Écrire les étapes, leurs attendus, leurs retours arrière, les autorisations, les branches.

**`MENER_VERIFICATION`**
Exécuter effectivement une vérification : lire, chercher, inspecter, mesurer.

**`DETECTER_SOLUTION_IMPOSEE`**
Repérer qu'une solution est prescrite là où le sujet est un problème.

**`PRODUIRE_OPTIONS_DISTINCTES`**
Produire des approches matériellement différentes, pas des reformulations.

**`VERIFIER_SIMULTANEITE_POSSIBLE`**
Vérifier que deux étapes dites simultanées ne se disputent ni ressource, ni verrou, ni approbateur, ni précondition cachée.

**`EVALUER_EXIGENCE_TACHE`**
Déterminer, parmi les techniques autorisées, lesquelles méritent d'être déployées sur cette tâche.

**`RECENSER_INVARIANTS`**
Recenser ce qui doit rester vrai pendant toute transition, pas seulement à l'arrivée.

**`DECIDER_D_INTERROGER_UTILISATEUR`**
Distinguer ce qui relève d'une préférence ou d'une autorisation de ce qui est moins cher à vérifier soi-même.

**`ARBITRER_A_L_AVEUGLE`**
Trancher entre des propositions anonymisées, selon une précédence explicite, jamais au nombre de voix.

**`ORDONNER_PAR_PREREQUIS`**
Ordonner les étapes par contraintes réelles, non par récit ou par habitude.

**`ELAGUER_LA_PROSE`**
Retirer du plan ce qui ne change rien à ce que fera le lecteur : justifications, répétitions, et ce que l'exécutant devra de toute façon lire ou vérifier lui-même.

**`CONSIGNER_CE_QUI_A_TRANCHE`**
Consigner, pour chaque point, ce qui l'a emporté et pourquoi.

**`QUALIFIER_INDEPENDANCE_OBTENUE`**
Nommer honnêtement le degré d'indépendance réellement atteint entre deux évaluations, sans le surestimer.

**`PLACER_ET_NOMMER_LE_FICHIER`**
Choisir où le plan vit et sous quel nom.

**`ORIENTER_CHOIX`**
Devant plusieurs chemins, trier entre : il manque un fait, il faut une préférence de l'utilisateur, ou il y a un vrai choix à instruire.

**`VERIFIER_COUVERTURE_OBJECTIFS`**
Vérifier que chaque objectif requis est servi par au moins une action et qu'il est prouvable.

**`EPROUVER_RETOUR_ARRIERE`**
Distinguer un retour arrière vérifié d'un retour arrière simplement affirmé.

**`DECIDER_D_OUVRIR_UN_AGENT`**
Juger si un contexte séparé peut changer ce qu'on fera, ou seulement rendre l'histoire plus convaincante.

**`ANTICIPER_TIERS_REACTIF`**
Quand un acteur touché peut s'adapter, anticiper qu'il réagisse au plan plutôt qu'il ne le subisse.

**`PLACER_POINTS_VERIFICATION`**
Décider où l'on vérifie, avant que l'erreur ne se propage.

**`DERIVER_ACTIONS_DEPUIS_DECISIONS`**
Faire des décisions tranchées des actions concrètes.

**`QUALIFIER_TERRITOIRE`**
Distinguer l'environnement familier et prévisible de celui où l'issue d'une étape reconfigure la suivante.

**`CHERCHER_APPROCHES_NON_ENVISAGEES`**
Chercher activement une approche que personne n'a proposée.

**`CHAINER_ETAT_ACTUEL_VERS_CIBLE`**
Relier l'état actuel à la cible, en remontant depuis la cible, en descendant depuis l'état, ou les deux.

**`QUALIFIER_REVERSIBILITE`**
Dire ce qu'il en coûte de revenir en arrière, et si c'est seulement possible.

**`FORMULER_CIBLE_OBSERVABLE`**
Convertir l'intention en état final observable et falsifiable.

**`DISTINGUER_INDETERMINE_ET_NON_CHERCHE`**
Distinguer ce qui est vraiment indéterminable maintenant de ce qu'on a simplement omis d'aller chercher.

**`PARALLELISER_ENQUETE`**
Ouvrir un agent par domaine d'enquête séparable, en parallèle.

**`VERIFIER_ADOSSEMENT_AFFIRMATIONS`**
Vérifier que toute affirmation sur laquelle repose une décision ou une action est adossée à un fait établi, y compris celles apparues tard.

**`CONTROLER_CONTENU_FINAL`**
Vérifier avant d'émettre : chaque attendu falsifiable, aucune préférence promue en contrainte, aucune étape sans origine, rien d'incertain présenté comme acquis.

**`RESOUDRE_CONTRADICTION`**
Déterminer si la divergence tient à une date, une version, un périmètre ou une définition, puis trancher ou marquer le point comme contesté.

**`JUGER_PEREMPTION_FAIT`**
Juger combien de temps un fait reste vrai.

**`PROPOSER_CHIFFRAGE`**
Offrir à l'utilisateur de chiffrer effort, coût ou délai. Jamais produit d'office.

**`CONTROLER_INTEGRITE_DOCUMENT`**
Vérifier que le document ne se contredit pas lui-même : terminologie stable, pas de section dupliquée, pas de renvoi vers une étape inexistante.

**`DETECTER_ORIGINE_COMMUNE_SOURCES`**
Repérer que deux sources apparemment distinctes n'en font qu'une.

**`DISTINGUER_CHOIX_ET_CONSEQUENCE`**
Distinguer un vrai choix de la suite mécanique d'un choix déjà fait.

**`RECENSER_DEPENDANCES_EXTERNES`**
Identifier ce qui dépend de tiers : personnes, services, approbations, créneaux.

**`PREVOIR_SUITE_EN_CAS_DE_SUCCES`**
Prévoir la continuation qui s'enclenche quand la cible est atteinte.

**`ARRETER_ORCHESTRATION`**
Constater qu'un agent de plus ne changerait rien.

**`LIRE_TECHNIQUES_AUTORISEES`**
Lire la configuration et établir quelles techniques sont permises.

**`SOUMETTRE_ARBITRAGE_UTILISATEUR`**
Exposer un compromis matériel à l'utilisateur avant que le plan ne le referme.

**`FAIRE_CONTROLER_PAR_UN_TIERS`**
Faire relire le plan par un contexte qui ne l'a pas écrit.

**`DEBUSQUER_HYPOTHESES_IMPORTEES`**
Repérer la contrainte ou la préférence introduite sans être dite.

**`DEFINIR_CRITERES_ACCEPTATION`**
Définir à quoi on reconnaîtra que la cible est atteinte, objectif par objectif.

**`CHOISIR_ANGLES_ATTAQUE`**
Déterminer par quoi une décision peut casser, et donc sous quel angle l'attaquer.

