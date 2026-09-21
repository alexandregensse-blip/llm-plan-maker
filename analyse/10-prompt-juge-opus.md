Tu vas concevoir trois architectures d'algorithme. Pas les choisir : les écrire.

CE QU'ON CONSTRUIT

Un skill — un jeu d'instructions destiné à être lu et suivi par un agent LLM outillé — dont l'unique livrable est un plan d'action détaillé, écrit dans un fichier.
Le système dispose de 129 fonctions unitaires, toutes utiles mais parfois optionnelles en fonction de l'utilisation du skill.
La question ouverte est : dans quel ordre et selon quelle logique les enchaîner pour produire ce plan.

Lis d'abord /work/analyse/fonctions-unitaires.md : il décrit le système et liste ses 129 fonctions.



LES GRANDS PRINCIPES DU SKILL VISÉ

Ils sont non négociables. Toute architecture qui en viole un est inutilisable.

1. Rien n'est reporté à l'exécution. Tout ce qui peut être vérifié, investigué, demandé ou décidé l'est avant que le plan soit écrit. Une question ouverte dans un plan livré est un aveu d'enquête non faite.
2. Le système enquête mais n'engage rien. Il lit, inspecte, cherche, ouvre des agents, interroge l'utilisateur, mène des actions réversibles et bornées. Il n'exécute jamais un engagement du plan : le plan, c'est ce qu'il livre.
3. Les propositions concurrentes à l'aveugle sont le mécanisme central, à trois niveaux qui attrapent des erreurs différentes : le problème posé (planifie-t-on la bonne chose), la structure du plan (le découpage est-il le bon), et chaque choix litigieux pris isolément. Un arbitre distinct, qui ignore l'origine de chaque proposition, tranche — jamais au nombre de voix.
4. L'utilisateur décide, le système rapporte. Quand il pose une question, il attend ; il ne poursuit pas sur une valeur par défaut. Désaccord : il s'adapte. Besoin d'escalade : ça passe par l'utilisateur.
5. Le système ne raisonne jamais en coût. Il ne s'auto-limite pas, il n'estime rien. Une configuration decrete le nombre et le type d'agents par fonction sont autorisées, et quelles techniques sont mises en place ; c'est la seule borne.
6. Prioriser n'est pas écarter. Objectifs, inconnues : la priorité ordonne le travail, elle n'abandonne rien.
7. Le plan est impeccable par vérification, pas par filet. On ne planifie pas en supposant qu'on va se rater. Les impondérables sont exceptionnels et deviennent des branches — un plan n'est pas truffé de branches. Tout l'appareil de risque, de retour arrière et de points d'autorisation est une part mineure et optionelle, jamais le centre.
8. On ne refuse jamais pour cause de taille. Un travail trop gros se découpe en sous-plans traités séparément puis recomposés.
9. Le plan dit quoi faire. Pas ce que l'exécutant devra de toute façon lire ou vérifier lui-même. Le comment n'est dirigé que quand il n'est pas évident. Aucun archivisme, aucune justification : la traçabilité vit dans un fichier séparé. En introduction du plan livré : l'objectif du plan, rien de superflu.
10. Le format du plan est fixe. Seul son contenu grossit avec la complexité.
11. L'exécutant est un agent, le plus souvent celui-là même qui a produit le plan, après validation par l'utilisateur et noettoyage de son contexte.
12. Deux portes d'entrée : une demande, ou un plan existant dont on dérive le besoin — ce qui permet de retravailler un plan en plusieurs passes.
13. Un plan doit être clair, concis, bien ordonné, auto-porteur et si possible exécutable de maniere autonome.



LE MATÉRIAU

/work/analyse/09-architectures-candidates.md contient dix-huit architectures produites par des sous-traitants peu fiables.
Ne leur fais aucune confiance. Aucune ne sera retenue apres ton travail, qui les remplacera.
Elles servent uniquement de gisement : certaines ont trouvé un mécanisme juste, beaucoup ont commis des erreurs qu'il faut savoir nommer pour ne pas les refaire.
Ton travail commence par les dépouiller, et se termine par autre chose qu'elles.



PREMIÈRE PARTIE — DÉPOUILLEMENT

Analyse les dix-huit, une par une, toi-même.
Rends un tableau, une ligne par architecture, avec :

- son numéro et son nom ;
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

Avant d'écrire quoi que ce soit, un paragraphe qui énonce, pour chacune des trois architectures que tu vas produire, ce qu'elle cherche à réussir et sur quel principe d'organisation elle repose.
Les trois doivent viser des choses différentes — trois variantes d'une même idée ne valent qu'une.
Toutefois, les trois architectures doivent répondre pleinement et efficacement au specifications : en produire trois n'autorise pas de compromis de qualité pour ton rendu.



TROISIÈME PARTIE — LES TROIS ARCHITECTURES

Trois architectures en pseudo-code lisible.
Aucune ne doit être la reprise d'une des dix-huit, même améliorée : elles sont le fruit de ton travail et tirent le meilleur des 18 architectures candidates et de tes réflexions.
Tu peux évidemment exploiter des mécanismes que tu juges bons, à condition qu'ils servent une architecture qui est la tienne.

Pour chacune :

- son nom et son principe en une phrase ;
- le pseudo-code complet, utilisant les identifiants exacts des fonctions ;
- les boucles : lesquelles, déclenchées par quoi, jusqu'où elles remontent, et ce qui garantit qu'elles terminent ;
- les fonctions appelées plusieurs fois, et pourquoi ;
- les fonctions laissées de côté, et la justification rigoureuse de leur exclusion ;
- dans quel cas cette architecture est particulierement adaptée.



QUATRIÈME PARTIE — AUTO-ÉVALUATION

Tu notes tes trois architectures sur les cinq mêmes critères, avec la même sévérité que pour les dix-huit.
Puis tu dis, franchement : laquelle des trois te semble la plus solide et pourquoi ; ce que tu n'as pas réussi à résoudre ; et ce qui manque encore, que ni les dix-huit ni tes trois ne traitent.



CONTRAINTES QUI TE CONCERNE

- N'ouvre aucun sous-agent.
- Ne crée ni ne modifie aucun fichier. Rends ta réponse directement.
- Sois tranchant dans le dépouillement. Une notation qui ménage tout le monde ne sert à rien.
- Réponds en français.
