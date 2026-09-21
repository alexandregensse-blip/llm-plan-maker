Tu vas concevoir une architecture d'algorithme. Pas la choisir : l'écrire.

CE QU'ON CONSTRUIT

Un skill — un jeu d'instructions destiné à être lu et suivi par un agent LLM outillé — dont l'unique livrable est un plan d'action détaillé, écrit dans un fichier.
Le système dispose de 130 fonctions unitaires, toutes utiles mais parfois optionnelles en fonction de l'utilisation du skill.
La question ouverte est : dans quel ordre et selon quelle logique les enchaîner pour produire ce plan.

Lis d'abord /work/analyse/fonctions-unitaires.md : il décrit le système et liste ses 130 fonctions.

**On veut une architecture unique, efficace dans tous les cas.**
Pas trois architectures aux domaines d'emploi distincts, pas de sélecteur en amont qui choisirait un régime.
Une seule, qui tienne aussi bien sur la demande de deux lignes que sur le travail qui excède ce qu'un seul contexte peut porter, aussi bien en territoire familier qu'en terrain inconnu à enjeu élevé.
Si un mécanisme ne tient pas sur l'un de ces cas, ce n'est pas un motif pour créer une variante : c'est un motif pour l'améliorer.



LES GRANDS PRINCIPES DU SKILL VISÉ

Ils sont non négociables. Toute architecture qui en viole un est inutilisable.

1. Rien n'est reporté à l'exécution. Tout ce qui peut être vérifié, investigué, demandé ou décidé l'est avant que le plan soit écrit. Une question ouverte dans un plan livré est un aveu d'enquête non faite.
2. Le système enquête mais n'engage rien. Il lit, inspecte, cherche, ouvre des agents, interroge l'utilisateur, mène des actions réversibles et bornées. Il n'exécute jamais un engagement du plan : le plan, c'est ce qu'il livre.
3. Les propositions concurrentes à l'aveugle sont le mécanisme central, à trois niveaux qui attrapent des erreurs différentes : le problème posé (planifie-t-on la bonne chose), la structure du plan (le découpage est-il le bon), et chaque choix litigieux pris isolément. Un arbitre distinct, qui ignore l'origine de chaque proposition, tranche — jamais au nombre de voix.
4. L'utilisateur décide, le système rapporte. Quand il pose une question, il attend ; il ne poursuit pas sur une valeur par défaut. Désaccord : il s'adapte. Besoin d'escalade : ça passe par l'utilisateur. Mais on ne sollicite jamais l'utilisateur sur ce que le système peut établir en autonomie : la question est un dernier recours, jamais un réflexe ni un moyen de se couvrir.
5. Le système ne raisonne jamais en coût. Il ne s'auto-limite pas, il n'estime rien. Une configuration décrète le nombre et le type d'agents autorisés par fonction, et quelles techniques sont mises en place ; c'est la seule borne.
6. Prioriser n'est pas écarter. Objectifs, inconnues : la priorité ordonne le travail, elle n'abandonne rien.
7. Le plan est impeccable par vérification, pas par filet. On ne planifie pas en supposant qu'on va se rater. Les impondérables sont exceptionnels et deviennent des branches — un plan n'est pas truffé de branches. Tout l'appareil de risque, de retour arrière et de points d'autorisation est une part mineure et optionelle, jamais le centre.
8. On ne refuse jamais pour cause de taille. Un travail trop gros se découpe en sous-plans traités séparément puis recomposés.
9. Le plan dit quoi faire. Pas ce que l'exécutant devra de toute façon lire ou vérifier lui-même. Le comment n'est dirigé que quand il n'est pas évident. Aucun archivisme, aucune justification : la traçabilité vit dans un fichier séparé. En introduction du plan livré : l'objectif du plan, rien de superflu.
10. Le format du plan est fixe : il est donné au système sous forme de template. Définir ce format n'est pas le travail de l'architecture, et aucune fonction ne le porte. Seul le contenu du plan grossit avec la complexité.
11. L'exécutant est un agent, le plus souvent celui-là même qui a produit le plan, après validation par l'utilisateur et nettoyage de son contexte. Le système s'arrête quand le plan est écrit : faire relire, approuver ou exécuter ce plan n'est pas une étape de l'algorithme.
12. Deux portes d'entrée : une demande, ou un plan existant dont on dérive le besoin — ce qui permet de retravailler un plan en plusieurs passes.
13. Un plan doit être clair, concis, bien ordonné, auto-porteur et si possible exécutable de maniere autonome.
14. Toute inconnue est réputée résoluble avant l'écriture du plan, au besoin en remontant à l'utilisateur. Classer une inconnue comme ne pouvant être levée qu'à l'exécution est l'exception : ce classement doit être contrôlé par le système lui-même, jamais décidé en silence — et ce contrôle ne se délègue pas à l'utilisateur, qui n'a pas à trancher ce que le système peut établir seul.



POINTS DÉJÀ TRANCHÉS — n'y reviens pas, ne les rouvre pas

- Le plan n'est pas daté et ne porte pas de péremption globale. Ce qui vieillit, ce sont les faits : le traitement correct est une étape de re-vérification des hypothèses, constats et axiomes, inscrite dans le plan. Rejouer un plan se fait à la demande de l'utilisateur, hors du système.
- Aucune fonction ne traque les retraits silencieux entre un plan source et un plan retravaillé. Un retrait que le contrôle final ne rend pas bruyant est un retrait qu'il fallait faire.
- Le système s'arrête au plan écrit. Le faire valider par l'utilisateur n'est pas une étape de l'algorithme : s'il faut y revenir, c'est que le besoin avait été mal cerné, ce qui est un défaut en amont et non une porte manquante en aval.
- L'indépendance des concurrents aveugles est considérée comme atteignable. Empiriquement, à modèle identique, les discours diffèrent réellement ; et quand ils ne diffèrent pas assez, biaiser explicitement un concurrent — lui demander autre chose — fonctionne. Traite-la comme un problème de méthode, pas comme une limite de fond.
- L'utilisateur qui ne répond pas : on attend. Qui répond « je ne sais pas » : on lui explique simplement de quoi il s'agit. Qui se contredit : c'est que son besoin est mal cerné, et c'est au système de le cerner mieux.



LE MATÉRIAU

Deux fichiers, produits par des sous-traitants dont aucune production ne sera retenue.
Ne leur fais aucune confiance : ils servent de gisement, rien de plus.

/work/analyse/11-trois-architectures.md est ton matériau principal.
Il contient trois architectures — A le greffe, B les contrats emboîtés, C le brouillon-sonde — précédées du dépouillement de dix-huit architectures antérieures, et suivies d'une auto-évaluation.
Ces trois-là visent chacune une qualité au détriment des autres, et c'est précisément ce qu'on ne veut pas.
Elles énoncent aussi quatre « règles communes » et un format de plan : nous ne les avons ni validées ni rejetées, c'est à toi de juger si elles valent quelque chose.

Le dépouillement des dix-huit qui ouvre ce fichier est fiable : tu peux t'appuyer dessus tel quel, et notamment sur ses colonnes À RETENIR et À NE PAS FAIRE.
Les dix-huit architectures elles-mêmes sont dans /work/analyse/09-architectures-candidates.md, mais tu n'as pas à les relire : n'y va que si le dépouillement mentionne un mécanisme dont tu veux le détail exact.

Ton travail commence par dépouiller A, B et C, et se termine par autre chose qu'elles.



PREMIÈRE PARTIE — DÉPOUILLEMENT

Analyse les trois architectures A, B et C, une par une, toi-même.
Puis, en t'appuyant sur le dépouillement des dix-huit, nomme les mécanismes retenus là-bas que A, B et C ont manqués ou mal traités, et que tu comptes reprendre.

Rends un tableau, une ligne par architecture, avec :

- son nom ;
- une note sur 5 pour chacun des cinq critères ci-dessous ;
- une appréciation en deux ou trois phrases, de ta main ;
- À RETENIR : les mécanismes précis qui méritent d'être repris, ou « rien » ;
- À NE PAS FAIRE : les erreurs précises qu'elle commet, ou « rien de notable ».

Les cinq critères de notation :

SUIVABILITÉ — ces instructions seront lues et suivies par un modèle de langage, pas exécutées par un programme.
Une architecture qui exige de tenir un graphe vivant, des drapeaux d'invalidation, une file recalculée à chaque tour ou un compteur de rebonds par couple de phases sera jouée, pas suivie.

FIDÉLITÉ — respecte-t-elle les principes ci-dessus ?
Nomme celui qu'elle viole, le cas échéant.

BOUCLES — les retours et les vérifications sont-ils déclenchés par de l'observable ?
Remontent-ils au bon endroit ?
La terminaison découle-t-elle de la structure, ou est-elle décrétée par un plafond arbitraire ?

USAGE DES FONCTIONS — lesquelles sont rappelées, quand, sur quels objets, et ces répétitions ont-elles un sens ?
Une architecture qui déroule les fonctions une par une dans l'ordre ne vaut rien.
Regarde aussi ce qu'elle laisse de côté et si l'omission se défend.

PROPORTIONNALITÉ — que produit-elle sur une tâche triviale, et sur une tâche lourde ?
Imposer la même cérémonie aux deux est un défaut grave.



DEUXIÈME PARTIE — PRÉ-CONSTRUCTION

Avant d'écrire quoi que ce soit, un paragraphe qui énonce ce que ton architecture cherche à réussir et sur quel principe d'organisation elle repose.
Elle doit réussir simultanément ce que A, B et C se partageaient : l'exhaustivité vérifiable, la tenue d'un travail trop gros, et la proportionnalité avec chasse au tacite.
Dis explicitement comment tu t'y prends pour que ces trois exigences ne se détruisent pas l'une l'autre — c'est le cœur du travail, et c'est là que le tour précédent a renoncé.



TROISIÈME PARTIE — L'ARCHITECTURE

Une architecture en pseudo-code lisible.
Elle ne doit être la reprise d'aucune des vingt-et-une, même améliorée : elle est le fruit de ton travail et tire le meilleur du matériau et de tes réflexions.
Tu peux évidemment exploiter des mécanismes que tu juges bons, à condition qu'ils servent une architecture qui est la tienne.

Rends :

- son nom et son principe en une phrase ;
- le pseudo-code complet, utilisant les identifiants exacts des fonctions ;
- les boucles : lesquelles, déclenchées par quoi, jusqu'où elles remontent, et ce qui garantit qu'elles terminent ;
- les fonctions appelées plusieurs fois, et pourquoi ;
- les fonctions laissées de côté, et la justification rigoureuse de leur exclusion ;
- les invariants que l'architecture tient en permanence, s'il y en a.



QUATRIÈME PARTIE — AUTO-ÉVALUATION

Tu notes ton architecture sur les cinq mêmes critères, avec la même sévérité que pour A, B et C.
Puis tu dis, franchement : ce que tu n'as pas réussi à résoudre ; et ce qui manque encore, que ni les vingt-et-une ni la tienne ne traitent.



CONTRAINTES QUI TE CONCERNE

- N'ouvre aucun sous-agent.
- Ne crée ni ne modifie aucun fichier. Rends ta réponse directement.
- Sois tranchant dans le dépouillement. Une notation qui ménage tout le monde ne sert à rien.
- Réponds en français.
