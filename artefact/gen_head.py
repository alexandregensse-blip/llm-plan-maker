# -*- coding: utf-8 -*-
import re, html, json, io, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = next(q for q in (os.path.join(HERE, '..', 'analyse', '13-architecture-ardoise.md'),
                       '/work/analyse/13-architecture-ardoise.md') if os.path.exists(q))
OUT = os.path.join(HERE, 'ardoise.html')

raw = open(SRC, encoding='utf-8').read()
code = re.search(r'```\n(.*?)\n```', raw, re.S).group(1)

# --- mise a jour du pseudo-code -------------------------------------------
# Le pseudo-code source est anterieur a plusieurs decisions d'architecture.
# Les passages ci-dessous sont reecrits pour que le pseudo-code, les schemas
# et la prose disent la meme chose. Chaque motif doit apparaitre exactement
# une fois, sans quoi la generation echoue.

PATCHES = [
# --- confronter() : l'ordre des attaques n'est pas fixe, et l'attaque du
#     champ entier est un marquage, non une seconde epreuve.
("""CHOISIR_ANGLES_ATTAQUE
ordre des attaques : AVANCER_L_HYPOTHESE_LA_PLUS_FRAGILE d'abord
POUR chaque proposition : ATTAQUER_UNE_OPTION(action + faits seuls ; jamais le plaidoyer)
ATTAQUER_TOUT_LE_CHAMP                        # ce qui les ferait toutes tomber,
                                              # et les conditions d'un problème mal posé
SI tout le champ tombe :
    CONSTATER_IMPOSSIBILITE ; PRESENTER_ALTERNATIVES_AU_CHOIX
    → dette QUESTION (arbitrage). Jamais un arrêt.""",
 """CHOISIR_ANGLES_ATTAQUE
POUR chaque proposition : ATTAQUER_UNE_OPTION(action + faits seuls ; jamais le plaidoyer)
    # l'ordre n'est pas fixé : toutes sont attaquées avant tout arbitrage
ATTAQUER_TOUT_LE_CHAMP                        # un marquage, non une seconde épreuve
    hypothèses communes = intersection des listes écrites par
        EXIGER_HYPOTHESES_EXPLICITES sur chaque proposition
    # chacune a déjà été éprouvée par l'attaque individuelle. Le marquage ne
    # dit pas si elle tient, il dit ce que sa chute emporterait :
    #     propre à une proposition → cette proposition seule tombe
    #     commune à toutes         → le champ entier tombe
    et les conditions d'un problème mal posé"""),

# --- confronter() : indépendance faible, angles épuisés.
("""SI l'indépendance obtenue est faible ET des angles non utilisés restent :
    un concurrent est REPRODUIT avec un biais explicitement assigné
    (un angle de CHOISIR_ANGLES_ATTAQUE qu'aucun n'a porté)
    # terminaison : l'ensemble des angles est fini et décroît strictement""",
 """SI l'indépendance obtenue est faible :
    S'IL reste un angle de CHOISIR_ANGLES_ATTAQUE qu'aucun n'a porté :
        un concurrent est REPRODUIT avec ce biais explicitement assigné
        # terminaison : l'ensemble des angles est fini et décroît strictement
    SINON : l'indépendance obtenue est consignée telle quelle et la
        confrontation se poursuit. Rien à demander à l'utilisateur ; une
        faiblesse de méthode consignée n'est pas un point ouvert du plan."""),

# --- confronter() : c'est l'arbitre qui constate qu'aucune ne tient.
("""CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_PORTEE_DECISION""",
 """SI l'arbitre ne retient aucune proposition — champ entier tombé, ou aucune
   qui satisfasse les critères d'acceptation :
    CONSTATER_IMPOSSIBILITE ; PRESENTER_ALTERNATIVES_AU_CHOIX
    → dette QUESTION (arbitrage). Jamais un arrêt.
    # c'est l'arbitre qui le constate, jamais le planificateur seul

CONSIGNER_CE_QUI_A_TRANCHE ; QUALIFIER_PORTEE_DECISION"""),

# --- crible : une question sans réponse se clôt comme les autres.
("""# Chaque ligne se clôt par une disposition écrite : un objet, ou « vide ».""",
 """# Chaque ligne se clôt par une disposition écrite : un objet, ou « vide ».
# Une ligne à laquelle la lecture ne sait pas répondre se clôt elle aussi par
# un objet — une dette INCONNUE. « Sans réponse » n'est pas une disposition,
# et aucune ligne du crible ne reste ouverte."""),

# --- niveau 1 : reprise d'un besoin arrêté lors d'une passe antérieure.
("""confronter(« quelle lecture du besoin ? », crible)""",
 """SI un besoin arrêté lors d'une passe antérieure est à l'ardoise :
    REPRENDRE_PASSE_PRECEDENTE ; le confronter à la demande telle qu'elle
    arrive — éventuellement reprécisée au moment où le système est relancé
    SI rien dans cette demande ne le contredit :
        REUTILISER_ACQUIS : besoin, cible et critères sont conservés.
        Ce niveau n'est pas rejoué.
    SINON : la contradiction entre au crible, et les lectures sont remises
        en concurrence ci-dessous.

confronter(« quelle lecture du besoin ? », crible)"""),

# --- niveau 2 : conservation d'une structure arrêtée.
("""squelette = confronter(« quel chemin de l'état actuel à la cible ? », crible + faits)""",
 """SI un squelette arrêté lors d'une passe antérieure est à l'ardoise :
    REPRENDRE_PASSE_PRECEDENTE
    il n'est rejoué que si l'un de ces trois constats se lit à l'ardoise.
    Aucune appréciation n'entre ici :
        la cible a changé
        les critères d'acceptation ont changé
        un fait établi depuis contredit une hypothèse que ce squelette a
            nommée — même index de réouverture que la boucle 3
    SI aucun des trois ne se lit :
        REUTILISER_ACQUIS : le squelette est conservé tel quel et passe par
        le contrôle final comme à chaque fois. Ce niveau n'est pas rejoué.
    SINON : il concourt comme proposition ci-dessous.

squelette = confronter(« quel chemin de l'état actuel à la cible ? », crible + faits)"""),

# --- envoi des questions : la réponse qui ne tranche pas.
("""        « je ne sais pas »        → la question n'était pas actionnable :
            FORMULER_QUESTION_ACTIONNABLE à nouveau, avec
            PRESENTER_ALTERNATIVES_AU_CHOIX et QUALIFIER_PORTEE_DECISION
            (ce qui change si la réponse est fausse) — on explique, on ne tranche pas""",
 """        question restée sans réponse alors que d'autres en ont reçu une
                                  → traitée comme une réponse qui ne tranche
            pas. Une réponse partielle n'est pas une absence de réponse :
            ce qui est répondu clôt les dettes correspondantes, et chaque
            question laissée de côté suit la règle ci-dessous.
        réponse qui ne tranche pas → DECIDER_D_INTERROGER_UTILISATEUR d'abord :
            SI CHOISIR_MOYEN_DE_LEVEE rend un moyen encore disponible :
                la dette se retype en dette INCONNUE et n'est pas reposée ;
                elle est levée à l'apurement de la vague suivante, comme
                toute dette de ce type — l'utilisateur n'attend pas pour elle
            SINON SI la dette ne porte pas déjà la marque « reformulée » :
                FORMULER_QUESTION_ACTIONNABLE à nouveau, avec
                PRESENTER_ALTERNATIVES_AU_CHOIX et QUALIFIER_PORTEE_DECISION
                (ce qui change selon la réponse), dans le MÊME échange :
                l'utilisateur est là, il n'attend pas la vague suivante.
                La marque « reformulée » est inscrite sur la dette
                # une propriété de la dette, lue à l'ardoise. Pas un compteur.
            SINON : la question porte au-delà de ce que l'utilisateur peut
                savoir. On change d'objet : FORMULER_QUESTION_ACTIONNABLE sur
                le BESOIN — ce qu'il cherche à obtenir, et non la manière d'y
                parvenir. Les réponses alimentent le NIVEAU 1.
                Jamais une troisième formulation de la même question."""),

# --- réécriture : le cas où aucune décision close ne change le squelette.
("""          tout pas dont l'origine n'est ni un verdict, ni un fait, ni une réponse
          de l'utilisateur, ni une contrainte héritée est RETIRÉ — jamais gardé
          par prudence ; et l'origine désigne les pas neufs de la vague suivante""",
 """          tout pas dont l'origine n'est ni un verdict, ni un fait, ni une réponse
          de l'utilisateur, ni une contrainte héritée est RETIRÉ — jamais gardé
          par prudence ; et l'origine désigne les pas neufs de la vague suivante
  SINON : le squelette est conservé tel quel et la vague suivante n'a aucun
      pas neuf à interroger. Seules les dettes encore ouvertes l'occupent."""),
]

PATCHES += [
# --- confronter() : une proposition dont le socle n'est pas etabli n'est
#     pas attaquee. Une attaque conditionnelle ne rend rien.
("""    toute hypothèse qui est une inconnue non levée → dette INCONNUE,
        et la proposition attend la quittance de cette dette""",
 """    toute hypothèse qui est une inconnue non levée → dette INCONNUE,
        et la proposition attend la quittance de cette dette AVANT d'être
        attaquée. Attaquer une proposition dont le socle n'est pas établi ne
        rend qu'un résultat conditionnel — « elle tombe si l'hypothèse est
        fausse » — c'est-à-dire rien. La confrontation entière attend, puisque
        toutes les propositions sont attaquées avant tout arbitrage."""),

# --- le routeur des defauts nommait les types dans l'ancien vocabulaire
("""    fait douteux            → INCONNUE
    décision mal fondée     → CHOIX
    pas trop gros           → CONTRAT""",
 """    fait douteux            → dette INCONNUE
    décision mal fondée     → dette CHOIX
    pas trop gros           → dette CONTRAT"""),

]

# Le pseudo-code source dit « pas » la ou tout le document dit « etape ».
LEXIQUE = [
    ("la suite ordonnée de pas qui relie l'état", "la suite ordonnée d'étapes qui relie l'état"),
    ("interrogation des pas neufs", "interrogation des étapes neuves"),
    ("pas_neufs = les pas que RATTACHER_TOUTE_PIECE_A_SON_ORIGINE désigne comme\n              nés de la version courante (première vague : tous)",
     "etapes_neuves = les étapes que RATTACHER_TOUTE_PIECE_A_SON_ORIGINE désigne\n              comme nées de la version courante (première vague : toutes)"),
    ("POUR chaque pas neuf, trois questions :", "POUR chaque étape neuve, trois questions :"),
    ("RECENSER_INCONNUES(pas) ; EXIGER_HYPOTHESES_EXPLICITES(pas)",
     "RECENSER_INCONNUES(étape) ; EXIGER_HYPOTHESES_EXPLICITES(étape)"),
    ("DEBUSQUER_HYPOTHESES_IMPORTEES(pas)", "DEBUSQUER_HYPOTHESES_IMPORTEES(étape)"),
    ("ORIENTER_CHOIX(pas)", "ORIENTER_CHOIX(étape)"),
    ("DEFINIR_ATTENDU_OBSERVABLE(pas)", "DEFINIR_ATTENDU_OBSERVABLE(étape)"),
    ("ce n'est pas un pas,", "ce n'est pas une étape,"),
    ("CONTROLER_TAILLE_DES_ETAPES(pas)", "CONTROLER_TAILLE_DES_ETAPES(étape)"),
    ("servie par le pas N", "servie par l'étape N"),
    ("# pas que personne n'a demandés", "# étapes que personne n'a demandées"),
    ("objectif servi par aucun pas", "objectif servi par aucune étape"),
    ("le seul moyen de lever est de FAIRE le\n                pas, l'inconnue",
     "le seul moyen de lever est de FAIRE\n                l'étape, l'inconnue"),
    ("ou plus d'un pas en dépend", "ou plus d'une étape en dépend"),
    ("qu'elle peut changer plus d'un pas", "qu'elle peut changer plus d'une étape"),
    ("DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(pas)", "DECOUPER_EN_SOUS_PLANS_ET_FUSIONNER(étape)"),
    ("tout pas dont l'origine n'est ni un verdict, ni un fait, ni une réponse\n          de l'utilisateur, ni une contrainte héritée est RETIRÉ",
     "toute étape dont l'origine n'est ni une décision close, ni un fait, ni une\n          réponse de l'utilisateur, ni une contrainte héritée est RETIRÉE"),
    ("l'origine désigne les pas neufs de la vague suivante", "l'origine désigne les étapes neuves de la vague suivante"),
    ("pas neuf à interroger", "étape neuve à interroger"),
    ("aucun pas du squelette non interrogé", "aucune étape du squelette non interrogée"),
    ("avant que l'attendu du pas ne la révèle", "avant que l'attendu de l'étape ne la révèle"),
    ("juste avant le pas qui en dépend", "juste avant l'étape qui en dépend"),
    ("aucun pas sans\n                                              # origine", "aucune étape sans\n                                              # origine"),
    ("pas trop gros           → dette CONTRAT", "étape trop large        → dette CONTRAT"),
    ("SI une ardoise de passe antérieure existe", "SI un registre de passe antérieure existe"),
    ("si oui → la dette se retype INCONNUE. La question est un dernier recours.",
     "si oui → la dette se retype en dette INCONNUE, levée à l'apurement.\n        La question est un dernier recours."),
    ("groupés en une ligne d'ardoise", "groupés en une seule ligne de l'ardoise"),
]
PATCHES += [(a, b) for a, b in LEXIQUE if a != b]

for old, new in PATCHES:
    assert code.count(old) == 1, 'motif introuvable ou ambigu : ' + old[:60]
    code = code.replace(old, new)

parts = re.split(r'^(════+.*?)$', code, flags=re.M)

chunks = {}
for i in range(1, len(parts), 2):
    lab = parts[i].strip('═ ').strip()
    chunks[lab.split('—')[0].split('(')[0].strip()] = parts[i+1].strip('\n')

mot = chunks['LE MOTEUR'].split('\n')

def seg(start, end=None):
    """Decoupe LE MOTEUR entre deux ancres textuelles, insensible aux decalages."""
    i = next(k for k, l in enumerate(mot) if start in l)
    j = next(k for k, l in enumerate(mot) if k > i and end in l) if end else len(mot)
    return '\n'.join(mot[i:j]).strip('\n')

# --- vocabulaire unifie ---------------------------------------------------
# Le pseudo-code source employait un vocabulaire metaphorique. Il est renomme
# ici pour n'avoir qu'un seul vocabulaire dans tout le document.
VOCAB = [
    ("DETTE « INCONNUE »",        "ENTRÉE « FAIT MANQUANT »"),
    ("DETTE « QUESTION »",        "ENTRÉE « À SOUMETTRE »"),
    ("DETTE « CHOIX »",           "ENTRÉE « DÉCISION »"),
    ("DETTE « CONTRAT »",         "ENTRÉE « SOUS-PLAN »"),
    ("DETTE « BRANCHE »",         "ENTRÉE « BRANCHE »"),
    ("dettes INCONNUE",      "entrées FAIT MANQUANT"),
    ("dettes QUESTION",      "entrées À SOUMETTRE"),
    ("dettes CHOIX",         "entrées DÉCISION"),
    ("dettes CONTRAT",       "entrées SOUS-PLAN"),
    ("dette INCONNUE",       "entrée FAIT MANQUANT"),
    ("dette QUESTION",       "entrée À SOUMETTRE"),
    ("dette CHOIX",          "entrée DÉCISION"),
    ("dette CONTRAT",        "entrée SOUS-PLAN"),
    ("dette BRANCHE",        "entrée BRANCHE"),
    ("item `INCONNUE`",      "entrée FAIT MANQUANT"),
    ("au POINT DE VAGUE",    "à l'ENVOI DES QUESTIONS"),
    ("POINT DE VAGUE",       "ENVOI DES QUESTIONS"),
    ("au point de vague",    "à l'envoi des questions"),
    ("point de vague",       "envoi des questions"),
    ("SORTIE DE VAGUE",      "SORTIE D'ITÉRATION"),
    ("est PIVOT",           "est DÉTERMINANT"),
    ("fait pivot",          "fait déterminant"),
    ("le fait comme pivot", "le fait comme déterminant"),
    ("CRIBLE DIFFÉRENTIEL",    "SECOND PASSAGE DU CRIBLE"),
    ("crible différentiel",    "second passage du crible"),
    ("squelette",            "enchaînement"),
    ("CONTRE_ÉPREUVE",       "CONTRÔLE DU CLASSEMENT"),
    ("contre-épreuve",       "contrôle du classement"),
    ("APUREMENT",            "RÉSORPTION"),
    ("apurement",            "résorption"),
    ("de l'ardoise",         "du registre"),
    ("à l'ardoise",          "au registre"),
    ("l'ardoise",            "le registre"),
    ("ardoise",              "registre"),
    ("dettes",               "entrées"),
    ("dette",                "entrée"),
    ("quittance",            "clôture"),
    ("VAGUE",                "ITÉRATION"),
    ("vagues",               "itérations"),
    ("vague",                "itération"),
    ("défaut_de_contrat",    "défaut_de_sous_plan"),
    ("honorer(contrat)",     "traiter(sous_plan)"),
    ("honorer",              "traiter"),
    ("contrats",             "sous-plans"),
    ("CONTRAT",              "SOUS-PLAN"),
    ("contrat",              "sous-plan"),
]
import re as _re
_IDENT = _re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")

CORRECTIONS = [
    ("le nombre de entrées", "le nombre d'entrées"),
    ("de entrée", "d'entrée"),
    ("les quatre épreuves passées", "les cinq conditions satisfaites"),
    ("NIVEAU 3", "NIVEAU 3 — la décision, troisième niveau de confrontation"),
]

# Le renommage change le genre et l'initiale des mots : les elisions sont
# refaites apres coup, sinon le pseudo-code sort avec « le enchainement ».
ELISION = [
    (r"\b([Ll])a (entrée|itération)", r"\1'\2"),
    (r"\b([Ll])e (entrée|enchaînement|itération)", r"\1'\2"),
    (r"\bde (entrée|itération|enchaînement)\b", r"d'\1"),
    (r"\bde la (entrée|itération)\b", r"de l'\1"),
    (r"\bdu (entrée|enchaînement|itération)\b", r"de l'\1"),
    (r"\bà le (entrée|enchaînement|itération)\b", r"à l'\1"),
]

def unify(text):
    """Applique le vocabulaire unifie sans jamais toucher un identifiant de fonction."""
    before = sorted(_IDENT.findall(text))
    out = text
    for a, b in VOCAB:
        out = out.replace(a, b)
    for x, y in CORRECTIONS:
        out = out.replace(x, y)
    for pat, rep in ELISION:
        out = _re.sub(pat, rep, out)
    after = sorted(_IDENT.findall(out))
    assert before == after, "un identifiant de fonction a ete modifie"
    return out

# --- helpers -------------------------------------------------------------
def esc(s):
    return html.escape(s, quote=False)

def pre(txt):
    return ('<details class="fold"><summary>Pseudo-code</summary>'
            '<pre class="listing"><code>' + esc(unify(txt)) + '</code></pre></details>')

def trim_cls(diagram):
    """Retire les classDef qu'aucun noeud du schema n'utilise."""
    used = set(re.findall(r"^\s*class\s+\S+\s+(\w+)\s*$", diagram, re.M))
    keep = []
    for line in diagram.split("\n"):
        m = re.match(r"\s*classDef\s+(\w+)\b", line)
        if m and m.group(1) not in used:
            continue
        keep.append(line)
    return "\n".join(keep)


def plate(n, label, diagram):
    return ('<figure class="plate">'
            '<figcaption><span class="plate-n">Schéma ' + n + '</span>'
            '<span class="plate-l">' + label + '</span></figcaption>'
            '<div class="plate-body"><pre class="mermaid">' + trim_cls(diagram) + '</pre></div>'
            '</figure>')

MM = ('%%{init: {"theme":"base","themeVariables":{'
      '"background":"transparent","primaryColor":"#25333B","primaryTextColor":"#DCE6E9",'
      '"primaryBorderColor":"#6E8C99","lineColor":"#93AEBA","secondaryColor":"#2E404A",'
      '"tertiaryColor":"#1C282E","tertiaryTextColor":"#DCE6E9","secondaryTextColor":"#DCE6E9",'
      '"noteBkgColor":"#2E404A","noteTextColor":"#DCE6E9","edgeLabelBackground":"#162126",'
      '"fontFamily":"IBM Plex Mono, ui-monospace, monospace","fontSize":"16px"},"flowchart":{"nodeSpacing":48,"rankSpacing":64,"padding":16,"useMaxWidth":false,"wrappingWidth":520,"htmlLabels":true,"diagramPadding":14}} }%%\n')

CLS = ('\n  classDef dette fill:#42272A,stroke:#B4695C,color:#EBC9C0;'
       '\n  classDef quit fill:#22382F,stroke:#5E9B84,color:#C3DED2;')
