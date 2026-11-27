# Tests de la refonte de lecture

## Bulles runes/classes — 27 novembre 2026

`test_bulles_fenetres.py` contrôle les deux manuscrits actuels sans écrire les
dérivés : segments hors fenêtres octet-identiques et ordonnés, compte/ordre des
fenêtres et associations `data-rune-id`, nombres/étoiles/améliorations, affixes
ordonnés et bonus chiffrés. Les deux étoiles décoratives entourant la rareté de
classe de la première Révélation ne sont pas un rang de rune ; leur seul libellé
exact est exclu du relevé numérique. Les anciens bonus de grade sans chiffre ne
sont pas des valeurs d'équipement et sont remplacés par la bulle de nom.

`fixtures/fenetres_avant_bulles_20261127.json` provient exclusivement des copies
avant intervention, dont les SHA-256 sont consignés. Les empreintes sont calculées
par famille de données sur des listes ordonnées, jamais sur des ensembles. La
suite permanente ne lit pas ces copies temporaires et ne renouvelle aucune preuve.

La nouvelle fixture `bulles_20261127_inverse.json` est un journal fermé de
présentation, pas un second inventaire : 253 éditions au I, 37 au II. Pour éviter
de recopier 179 fenêtres, les triplets `[début après, fin après, texte avant]`
en caractères Unicode sont du JSON compact UTF-8 compressé zlib/base64. Le helper
`before_bubble_presentation` exige le SHA-256 complet après, inverse les éditions
dans l'ordre décroissant et exige le SHA-256 avant. Valeur, rareté, préfixe ou
prose altérés sont refusés. Les anciennes fixtures DEC-179 et les empreintes
historiques sont inchangées et continuent de s'appliquer à cette restauration.
Les assertions textuelles historiques du I et les preuves d'import utilisent
cette seule restauration bornée, pas une normalisation générale des raretés.

Indépendamment du journal, le DOM actuel est contrôlé avec ses métadonnées : noms,
raretés, étoiles, paliers, principales et secondaires des inventaires sont
comparés au lore, notamment les 32 pièces de la vie 2. Les mutations de nom,
rareté machine, étoiles, amélioration, valeur et ordre d'affixes doivent échouer.
Les IDs sont découverts dans les métadonnées ; seuls les cas synthétiques ont des
IDs explicites. Les archives mobiles ont été déplacées vers
`docs/conversation/archive_2.txt` ; les recherches par ancres restent inchangées.

Les neuf variantes fermées (cinq runes, quatre classes) passent par le générateur
en mémoire, en mobile et bureau. Les contrastes CSS et SVG doivent atteindre
4,5:1 ; la bordure commune doit aussi contraster avec le blanc. Le violet astral
est celui de l'épique runique, pas la palette légendaire. Chaque nom possède un
complément de rareté en texte HTML réel dans la transcription, sans rôle ou
tabindex interactif. Les alternatives orientent vers le volet complet. Les SVG
conservent le texte compact dans `text/tspan`, toute la transcription dans `desc`,
et le vocabulaire fermé de primitives passives ; aucun assouplissement des tests
de sécurité. Iseria ne reçoit pas de classe astrale dans les fenêtres/alternatives.

Le lecteur conserve chaque fenêtre et ajoute un seul volet textuel explicite
pour celles ayant des raretés compactées ; les tables et icônes de ces volets
sont des duplications intentionnelles vérifiées séparément. Une fenêtre simple
sans ID reste acceptée ; une enveloppe GitHub sans ID reste refusée. Le contrat
CSS d'impression exige les raretés visibles et masque les volets redondants.
Ces tests structurels ne remplacent pas une vérification visuelle/lecteur d'écran,
ni un contrôle du filtre GitHub distant ou d'un PDF rendu.

## Corrections runiques DEC-178/179/180 — état actuel

Les deux manuscrits stabilisés sont contrôlés séparément : **153 fenêtres et
306 SVG au I**, **26 fenêtres et 52 SVG au II**. Les mentions 138/276 ou 110
ci-dessous décrivent des étapes historiques, pas les effectifs actuels.

`test_runes_livre_i.py` ajoute les contrats de rareté fixe et de fiches complètes.
Les deux nouveaux journaux copiés intégralement sont des preuves fermées de
conservation, **pas un second inventaire canonique** :

- `fixtures/corrections_runes_livre1_dec179.json` : 126 remplacements,
  de `9d27a766…` à `1e4221ee…` ;
- `fixtures/corrections_runes_livre1_dec179_complements.json` : 11 remplacements,
  de `1e4221ee…` à `a26785c2…`.

Le helper `before_approved_rune_corrections` inverse le deuxième journal puis le
premier, en ordre décroissant des positions **en caractères Unicode**, après
vérification de l'empreinte source et du texte exact de chaque tranche. Chaque
étape doit retrouver son empreinte antérieure ; un aller-retour testé doit aussi
reconstruire exactement la source actuelle. Les empreintes des journaux eux-mêmes
sont protégées. Aucun fichier temporaire n'est requis à l'exécution.

Cette inversion intervient **avant** DEC-168, les descriptions historiques et la
recherche du préfixe historique. Pour le contrat GitHub, elle intervient également
avant le retrait des enveloppes, afin de respecter les positions documentées.
Les 138 anciennes fenêtres, les anciens segments narratifs, cellules, textes,
sommaires et SHA-256 restent vérifiés sans nouvelle baseline ni exemption générale.
Les tests DEC-168 conservent leurs mutations propres sur l'état restauré.
Les identifiants historiques sont comparés sur cette restauration ; unicité,
types, sécurité, enveloppes et texte de **tous** les SVG restent vérifiés sur la
source actuelle, y compris les quinze nouvelles fenêtres.

Les attendus métier sont lus indépendamment dans `lore/runes.md` : toutes les
lignes des tableaux d'inventaire sont comparées par ID et palier, en conservant
l'ordre des affixes. Les cadeaux initiaux et la première Fatal à +0, documentés
en prose, ont des attendus explicites. Les fiches individuelles, les états réels
et projections, les paliers de secondaires, les affixes interdits, la composition
des équipements, le don à Yoon et le stockage de ses anciennes pierres sont
contrôlés séparément. Les seize finales restent HAS-R001/002 et HAS-R016 à 029,
rares bleues 6★ +15 ; aucune ancienne 2★/3★ n'est transformée en 6★.
Le suivi des porteurs renvoie aussi à `lore/personnages.md`, sans calculer de
caractéristiques naturelles ni figer un inventaire après une ellipse.

Les tables de statistiques naturelles et les badges de classe sont comparés
avant/après par identifiant, indépendamment des corrections d'inventaire. La
légendaire d'Iseria reste orange, 4★, +9, avec une projection +15 conditionnelle.
Les deux fenêtres de Rune temporelle sont des **exceptions narratives explicites
d'identification partielle** : ni étoiles inventées ni fiche ordinaire exigée.

Les mutations couvrent valeur, ordre, suppression, doublon, déplacement, insertion
de préfixe et narration hors journal. Des mutations d'étoiles, de rareté et
d'affixes échouent aussi au contrôle métier sans utiliser le journal d'inversion.
Le II est désormais contrôlé par contrats ciblés sur ses trois chapitres (9/12/18
sections), sa provenance bornée par ancres, ses progressions, ses 32 runes de vie 2
et ses 52 SVG. Les fixtures historiques ne sont pas renouvelées. Les anciens
libellés de coloration restent des traces de provenance, pas des règles actives.

Limites : les comparaisons automatisées ne constituent pas une revue littéraire,
une validation visuelle GitHub/mobile ni un audit RGAA complet. Une future
correction éditoriale autorisée nécessite une nouvelle preuve bornée ; ne pas
renouveler les anciennes empreintes pour contourner un échec.

Validation locale actuelle : **90 tests réussis**. Le contrôle métier du I parcourt **124 lignes
d'inventaire** et **78 états canoniques**, en plus des fiches individuelles.
`generer_fenetres.py --check` confirme **153 fenêtres / 306 SVG à jour** ; son
ciblage explicite confirme **26 fenêtres / 52 SVG à jour** pour le II, et
`generer_lecture.py --check` confirme le lecteur à jour. Ces contrôles n'écrivent
ni manuscrit, ni lore, ni dérivé ; aucun commit ou push n'est effectué.

## Source actuelle du livre I

Les tests et les deux générateurs ciblent désormais
`livre_1_l_ascension_d_une_legende_oubliee.md`, renommé depuis `roman.md`
sans modification de contenu. Chaque livre possède son propre manuscrit nommé
selon son titre validé ; les tests actuels protègent le livre I, pas un manuscrit
commun à la trilogie. Les chemins temporaires et les noms de fixtures ci-dessous
sont des références historiques inchangées, pas des sources concurrentes.

## Import final du livre I — 23 novembre 2026

`test_import_livre_i.py` vérifie les seize chapitres uniques, dans l'ordre, puis
un épilogue non numéroté. Les SHA-256 supplémentaires des corps 1–12 et du 13
I–X proviennent de la copie **avant intervention d'intégration**
`/tmp/opencode/roman-baseline-test-writer-13.md`. Ils ne remplacent aucune fixture
ancienne et ne dépendent pas de la présence de cette copie lors des exécutions.
Le sommaire est hors de ces corps ; seule la clôture du 13 et ses séparateurs
peuvent être déplacés après la nouvelle section XI.

Les anciennes empreintes restent appliquées. Le helper historique inverse
uniquement onze corrections textuelles exactes antérieures à cet import
(descriptions visuelles DEC-104/106 et salon DEC-107), et retire les seuls liens
de sommaire ajoutés correspondant à des titres réellement présents. Il ne
supprime pas arbitrairement du texte, ne normalise pas la narration et ne
renouvelle pas les fixtures. La protection supplémentaire avant import empêche
également de rétablir les anciennes descriptions. Un test de mutation vérifie
qu'un ancien lien de sommaire altéré reste détecté.

### Correction ciblée de l'Œil — DEC-168

Les empreintes originales restent inchangées, y compris celle du chapitre 10.
`before_approved_oeil_corrections` inverse uniquement les deux paragraphes HTML
contigus de la fenêtre `095` et la réplique d'Orven autorisés par DEC-168
(`docs/new.txt:97371,97427`). Chaque remplacement exige le texte exact et une
occurrence unique dans le chapitre 10 ; aucun autre chapitre n'est normalisé.
Cette inversion est appliquée au préfixe historique et au calcul des empreintes
avant import. Le texte des fenêtres est comparé à la fixture après cette seule
inversion autorisée, sans exemption de fenêtre ni renouvellement de manifeste.

Un contrôle distinct exige les nouveaux textes exacts, une seule fois, dans la
fenêtre `095` du chapitre 10 et dans la narration pour la réplique : revenir à
l'ancienne version ne suffit donc pas à faire réussir la suite. Les mutations
couvrent nature aléatoire, mauvais palier, réplique altérée, suppression du
paragraphe voisin, doublon et ajout narratif ; les changements hors chapitre 10
ne sont pas inversés. Les fichiers JSON historiques ne sont pas modifiés.

La source mobile est recherchée par titres et fins de chapitres, jamais par
numéro de ligne ou nombre total de lignes. Pour les 14–16, la dernière version
complète est retenue ; la section XI du 13 est contrôlée séparément. Les
paragraphes de soixante caractères au moins, sans chiffres ni tableaux, sont
comparés dans l'ordre après normalisation des espaces, apostrophes, Markdown et
entités HTML. Le texte des transcriptions HTML compte, pas seulement la narration
hors fenêtres. Les exceptions explicites sont le surnom « ma princesse », le
raccord de trente secondes d'Infiltration, la précision sur les cheveux d'Hasol
et « une partie » de la famille de Samia, ainsi que la réplique de Ray qui rappelle
le niveau quarante sans inventer vingt-quatre niveaux d'attente ; leur résultat est
aussi vérifié.
Suppression, altération et inversion de paragraphes sont testées par mutations.
Ces ancres protègent largement la prose, sans prétendre comparer chaque fragment
court ou chiffré de l'archive : une revue éditoriale reste nécessaire.

Les contrats ciblés couvrent les compteurs distincts de 5 000/10 000 démons et
100 boss, la progression 13→14→15→16, les ensembles d'équipement, Siphon qualitatif
sans formule numérique, les douze DONG et l'unique DING. Le contrôle du surnom
n'interdit pas la relation familiale légitime « ma belle-sœur ».

`test_securite_documents.py` contrôle **tout** le manuscrit et le lecteur, y
compris hors fenêtres : ni script, base, formulaire, redirection meta refresh,
gestionnaire d'événement ni ressource externe. Des injections artificielles
vérifient ces refus. Les SVG dérivés ont désormais un vocabulaire fermé de
primitives passives ; liens, filtres, images et animations sont refusés, avec
mutations sur un asset temporaire. Ces contrôles ne sont pas un assainisseur
universel de contenu HTML ni une preuve du filtre distant de GitHub.

Validation finale locale : **54 tests réussis**, plus `generer_fenetres.py --check`
(138 fenêtres, 276 SVG) et `generer_lecture.py --check`. Aucun test n'écrit dans
le manuscrit ou les dérivés réels ; aucune publication n'est effectuée.

## Exécution et protections historiques

Depuis la racine, avec l’interpréteur disposant des dépendances du générateur :

```sh
python3 -m pip install -r requirements-lecture.txt
python3 -m unittest discover -s tests -v
```

Les tests eux-mêmes utilisent uniquement la bibliothèque standard. Aucun navigateur,
réseau, téléchargement ou changement du manuscrit n’est lancé. Les appels CLI écrivent
dans des répertoires temporaires, avec des chemins comprenant espaces et esperluettes.

`fixtures/roman_avant.json` vient exclusivement de la baseline éditoriale approuvée
`/tmp/opencode/arcaniste-fenetres-20261122/etape-2/roman.avant-refonte.md` :
SHA-256 `bd983162161efdb1acd6d2469339b2104cb6d93fc735fd5793722ca0d747cb3b`.
Elle protège douze chapitres et 110 fenêtres dans leur ordre, dont les textes
identiques répétés ne sont pas dédupliqués. Les 111 SHA-256 des segments narratifs sont
stockés comme 111 blocs binaires de 32 octets concaténés puis encodés en base64 ;
chaque segment est comparé séparément, à sa position. La comparaison relit les octets
UTF-8 sans normaliser les fins de ligne. Les nombres de fenêtres, segments, chapitres,
tables et la répartition par chapitre proviennent du manifeste, pas des tests.
Le manifeste est calculé après l’import éditorial validé, avant la refonte des
21 nouvelles fenêtres, jamais depuis le résultat de cette refonte.
Les identifiants numériques historiques 001–089 restent associés à leurs fenêtres ;
les nouvelles fenêtres reçoivent 090–110. Leur ensemble est vérifié sans imposer
une renumérotation séquentielle dans l’ordre du manuscrit.

Les chapitres ajoutés après cette baseline ne nécessitent aucun renouvellement de
fixture. `historical_prefix` retrouve la borne exacte du préfixe grâce au SHA-256
existant du dernier segment narratif : aucun `rstrip`, aucune découpe approximative
au prochain titre. Tous les octets historiques, y compris les fins de ligne et la
fin du chapitre 12 après sa dernière fenêtre, restent contrôlés. Après cette borne,
seul le début d'un nouveau chapitre (numéro supérieur au dernier historique),
précédé éventuellement d'espaces, d'un séparateur `---` et de l'ancre dédiée
`<span id="chapitre-N"></span>`, est admis. Le numéro de l'ancre doit correspondre
exactement à celui du titre ; aucun texte arbitraire avant ou entre les deux n'est
toléré. Cette prise en charge ne change ni la borne ni les empreintes historiques.
Le nombre de
chapitres ou de fenêtres ajoutés n'est pas figé. Les contrôles historiques portent
sur le préfixe ; structure, identifiants uniques, types, enveloppes, sécurité et
correspondance du texte SVG/HTML portent sur **toutes** les fenêtres découvertes.

Dans les fenêtres, seuls les espaces et les entités HTML sont normalisés ; ✦◆✓ sont
ignorés uniquement dans les headers. Le SVG décoratif n’entre pas dans le texte.
Les étoiles ★, signes +, pourcentages, séparateurs de milliers et associations des
bonus à leurs valeurs restent protégés. Les cinq tables sont contrôlées par lignes
et cellules, pas seulement par texte aplati. Aucun nouveau décor n’est autorisé
implicitement.

Historique conservé intégralement dans `fixtures/roman_avant_passe1.json` : baseline
initiale à neuf chapitres, 89 fenêtres et 90 segments. Sa preuve de réussite précède
l’import éditorial ; cette archive n’est pas appliquée au manuscrit à douze chapitres.

Exception de présentation explicitement arbitrée pour l’étape 1 : la fenêtre 17
peut ajouter un unique `passive-badge` autour du mot existant « Passive », dans
« Type : Passive — Légendaire ». Son empreinte textuelle reste strictement vérifiée.
Cette exception ne permet ni suppression des badges existants, ni modification
des classes de bonus, ni ajout d’une catégorie ou valeur ; toutes les autres
classes protégées restent comparées au manifeste original.
Ce badge est déjà présent dans la baseline de l’étape 2 : aucune exception n’est
nécessaire dans la fixture courante. Tout nouvel ajout de classe protégée doit faire
l’objet d’un arbitrage explicite ; aucune valeur de bonus n’est exemptée.

**Ne jamais renouveler le manifeste pour faire passer une refonte visuelle.**
Un renouvellement nécessite une nouvelle décision éditoriale explicite puis une
revue de la nouvelle source de référence. `lecture_support.manifest(source)` permet
de recalculer les données depuis cette source approuvée, jamais depuis un résultat
dont on cherche à masquer une régression. Aucun test ne renouvelle la fixture.

Pour préparer un manifeste depuis une **nouvelle baseline explicitement approuvée** :

```sh
python3 tests/lecture_support.py --baseline "/chemin/vers/baseline approuvée.md"
```

Cette commande affiche seulement le JSON : elle ne remplace aucune fixture.
Conserver d’abord la preuve de conservation de l’étape précédente, puis examiner
séparément le diff éditorial autorisé. Après cette revue seulement, remplacer le
manifeste par patch en conservant la fixture de la première étape comme historique.
Les comptages sont recalculés par le même helper. Les exceptions de présentation
arbitrées sont des métadonnées explicites de fixture, jamais déduites automatiquement
ni appliquées aux classes de valeurs des bonus. Les nombres actuels décrivent la
baseline de refonte à 110 fenêtres et douze chapitres, pas une validation littéraire
globale des textes en lecture. Un ajout autorisé en fin de manuscrit conserve cette
baseline ; il n'est pas une validation littéraire. Une révision du contenu historique
requiert en revanche l'arbitrage éditorial décrit ci-dessus.

Les tests CSS vérifient les déclarations contractuelles, non le rendu calculé :
contrastes réels, débordements, impression et comportement des lecteurs d’écran
nécessitent également une revue visuelle/accessibilité. Le contrôle des fenêtres
est éditorial/structurel et ne valide aucune nouvelle règle de lore.

## Présentation colorée dans l’aperçu Markdown GitHub

Les fixtures ci-dessus restent inchangées. La phase GitHub part de la source
`/tmp/opencode/arcaniste-github-20261122/roman.md`, SHA-256
`aef0ae36950a34bb3bf7cfb1dce08f31c3a282528226fe5ad045e3da8d3d8f23`.
La fonction publique `extraire_source_fenetres(source: str) -> str` doit retrouver
exactement cette empreinte pour le préfixe historique extrait du manuscrit enveloppé, sans dépendre de la
présence future du fichier temporaire. Elle est idempotente et laisse intacte une
source historique non enveloppée.

`test_fenetres_github.py` contrôle chaque fenêtre : un `picture` avec source mobile
à 600 px et image de secours, chemins stricts `assets/fenetres/ID[-mobile].svg`,
alternative non vide, puis un `details` fermé contenant le corps HTML original.
Seul le texte du `summary.lit-window__transcript-toggle` est exclu du calcul
canonique : ni un autre `summary`, ni une autre balise portant cette classe ne
bénéficie de l’exception. Les contrôles historiques des 111 segments, 110 textes,
identifiants, tables et associations bonus/valeurs continuent de s’appliquer.
Aucune illustration narrative n’est autorisée par cet assouplissement.

Les deux SVG par fenêtre sont découverts depuis les identifiants du manuscrit,
sans liste manuelle. Leurs dimensions, XML, palette et absence de code actif,
d’image embarquée ou de ressource distante sont vérifiés. Le texte porté par les
éléments SVG `text`/`tspan` doit correspondre au texte complet du corps HTML, dans
le même ordre, après suppression des espaces de mise en page. Une empreinte dans
les métadonnées n’est pas une preuve d’affichage. Les chiffres et séparateurs
restent contrôlés indépendamment par le manifeste historique du HTML.

Le lecteur local doit retirer ces enveloppes et conserver les SVG décoratifs
originaux et les tables ; ses tests CLI historiques sans enveloppe restent actifs.
La CLI confirmée du nouveau générateur est également testée : génération sans
argument, `--check` (0 à jour, 1 périmé, 2 erreur), `--help` et arguments invalides.
Chaque cas copie le script dans un projet temporaire sous `/tmp/opencode`, avec
une fenêtre de test et un dossier d’assets isolé : aucun test CLI n’écrit dans le
manuscrit ou les assets réels. Les contrôles couvrent déterminisme depuis une
source vierge, idempotence sans réécriture, source restaurée octet-identique,
SVG manquant/périmé, enveloppe absente, entrées invalides et refus de suppression
automatique d’un SVG obsolète. Les instantanés incluent les octets et dates de
modification afin de prouver que `--check` n’écrit pas, même en échec.
Les collisions de noms dérivés (`A` et `A-mobile`) doivent être refusées avant
toute écriture. Une interruption `OSError` simulée lors du remplacement atomique
du manuscrit vérifie que l’ancienne source reste intacte et que le fichier voisin
temporaire est nettoyé. L’extraction accepte aussi une source mixte, avec fenêtre
enveloppée et ancienne fenêtre sans identifiant, sans relâcher le contrôle strict
des identifiants lors du build SVG. Les versions approuvées de Markdown et Pillow
sont protégées par un test de contrat des dépendances.

Les cas anti-régression simulent plusieurs chapitres ajoutés, puis des altérations
du début, d'une fenêtre, du dernier segment et des derniers octets historiques.
Un autre cas génère les SVG d'une nouvelle fenêtre dans le projet temporaire :
l'ajout seul passe, les identifiants/types absents, le mauvais chemin d'image et un
texte SVG altéré dans chacune des deux variantes échouent.

Après la fin d'un ajout éditorial autorisé, faire générer les dérivés par l'agent
responsable, puis vérifier avec l'interpréteur disposant des dépendances :

```sh
python3 scripts/generer_fenetres.py
python3 scripts/generer_lecture.py
python3 scripts/generer_fenetres.py --check
python3 -m unittest discover -s tests -v
```

Les deux premières commandes écrivent les dérivés (et l'enveloppe des nouvelles
fenêtres), contrairement à la suite de tests. Ne pas conclure sur des écritures
éditoriales en cours ni renouveler les empreintes pour corriger un SVG manquant.

Ces tests ne contactent pas l’API GitHub et ne prétendent pas simuler son filtre.
GitHub filtre le CSS inline : ajouter du HTML avec `style` n’est donc pas une
solution de présentation pour son aperçu Markdown. La conservation distante de
`picture/source/img/details/summary` doit être prouvée séparément par l’intégration.
Le rendu réel desktop/mobile, les ombres, la lisibilité, les polices, les coupures
et l’absence de troncature nécessitent aussi une revue navigateur distincte :
présence du texte dans un SVG ne garantit pas à elle seule sa visibilité à l’écran.

## Import du livre II

`test_import_livre_ii.py` contrôle les deux chapitres intégrés dans leur source
unique : neuf sections au chapitre 1, douze au chapitre 2, aucun chapitre 3.
L'empreinte du chapitre 1 protège son état local antérieur à cet import, y compris
les retouches de Croissance encore à relire ; elle ne vaut pas validation de ces
retouches. Les contrôles historiques de ce chapitre restent limités à son texte.
Le sommaire demandé ensuite par l'auteur reprend le modèle du I pour les deux
seuls chapitres existants. Son retrait exact et celui des deux ancres immédiatement
devant leurs titres permettent de conserver l'empreinte historique sans la
renouveler. Les titres déduits du manuscrit doivent correspondre aux liens et aux
ancres uniques ; les mutations de lien, libellé, ancre, doublon, chapitre futur et
ajout entre ancre et titre sont refusées. Une mutation narrative reste intacte
après ce retrait et échoue au contrôle d'empreinte : aucune normalisation générale.

Pour le chapitre 2, la comparaison à `docs/new.txt:103069–108183` protège tout le
texte utile, dans son ordre, après retrait du balisage de présentation. Les
adaptations autorisées sont précisément bornées : noms explicites « Ranger
astral » de Samia (appellations génériques et Zéphyr inchangés), puis retouches
de relecture DEC-172 à DEC-176. Celles-ci couvrent la seule identification de la
rune d'exercice et sa fiche complète F01 (Résistance +4 %, première secondaire
Vitesse +1 en gras), les deux paragraphes de description de Lame dans F02,
les raccords des sept runes avec Orven/Ray, la seconde Énergie en réserve équipée
immédiatement au huitième cercle, le rangement des deux cadeaux et des six
autres runes, et les comptes 7→8 cercles / huit emplacements de F03. Les
remplacements exacts sont vérifiés avant comparaison, sans exemption générale
des fenêtres, descriptions ou de la section IV et sans renouveler la source.
Les tests couvrent aussi Vague runique, Bénédiction, les groupes à cinquante
points et la retraite d'Elric. Les neuf affichages du chapitre 2 gardent leurs
identifiants stables `L2-C2-F01` à `L2-C2-F09`.

DEC-179 ajoute cinq présentations `L2-C2-R01` à `R05`, soit **quinze fenêtres et
trente SVG** pour le II. `fixtures/corrections_runes_livre2_dec179.json` décrit
les six blocs du journal d'intégration : position en lignes, longueur en caractères
Unicode, SHA-256 des octets UTF-8 du bloc après et remplacement antérieur exact.
Les blocs sont vérifiés puis inversés de la fin vers le début, jamais retirés par
une exemption générale des nouvelles fenêtres. Leur contenu, valeur, insertion,
déplacement et duplication sont éprouvés par mutations. Une mutation hors journal
reste intacte après inversion et échoue à la comparaison de la source antérieure.
Les tests ne dépendent pas de la présence future du journal temporaire.

Cette inversion précède celles de DEC-172/174/175/176/178 pour la comparaison
intégrale à la transmission. Le SHA-256 historique hors F01 de DEC-178 reste
`8c25952b4307d21e5f12a9af961cba21ee10727b96e85567d30a037b2e4a57de` :
aucune baseline historique n'est renouvelée. Les dix anciennes fenêtres restent
comparées octet pour octet avant/après DEC-179 et le chapitre 1 est inchangé.

Des attendus indépendants du journal contrôlent rareté/couleur, étoiles,
amélioration, principale, secondaires et valeurs des seize IDs d'équipement de la
vie 2, ainsi que leur correspondance au ledger `lore/runes.md`. Les expériences
blanche +0 sans secondaire et verte +0/+6 avec une/deux secondaires sont vérifiées
séparément, avec Vitesse +1 en gras dans R03 en HTML et dans les deux SVG.
Le double affichage « grade actuel/natif » de F01 demeure légitime : aucun faux
positif de duplication de grade, et aucune promotion au vert à +3.
Les tests protègent les sept pièces portées plus une réserve avant le gain,
la remise des huit Vol de vie après ouverture du coffret mais avant équipement,
l'absence de révélation de leur origine à Hasol, et les états des porteurs dans
`lore/personnages.md` (DEC-180). Les PA +100 sont des choix propres à ces pièces,
pas un barème intermédiaire universel. Savoir runique n'est pas exposé dans le II.
Les quinze enveloppes ont des identifiants uniques, alternatives non vides,
transcriptions fermées et en-têtes de tableau à portée colonne. Ces contrôles
structurels ne remplacent pas une revue RGAA visuelle et avec lecteur d'écran.

Les SVG sont contrôlés sans écriture depuis `produire`, avec chemins isolés sous
`assets/fenetres-livre-2/` : variantes mobile/bureau, XML passif, correspondance
exacte des dérivés, absence d'images obsolètes et génération idempotente. La CLI
par défaut du générateur reste réservée au livre I ; utiliser la procédure II de
`docs/fenetres_github.md` pour régénérer ce livre.
