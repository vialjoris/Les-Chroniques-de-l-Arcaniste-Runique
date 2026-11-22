# Tests de la refonte de lecture

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
globale des textes en lecture. Pendant un import, ne pas interpréter les tests
de conservation du manuscrit comme une validation : attendre la nouvelle baseline
explicitement fournie avant de les relancer et d’en tirer une preuve.

Les tests CSS vérifient les déclarations contractuelles, non le rendu calculé :
contrastes réels, débordements, impression et comportement des lecteurs d’écran
nécessitent également une revue visuelle/accessibilité. Le contrôle des fenêtres
est éditorial/structurel et ne valide aucune nouvelle règle de lore.

## Présentation colorée dans l’aperçu Markdown GitHub

Les fixtures ci-dessus restent inchangées. La phase GitHub part de la source
`/tmp/opencode/arcaniste-github-20261122/roman.md`, SHA-256
`aef0ae36950a34bb3bf7cfb1dce08f31c3a282528226fe5ad045e3da8d3d8f23`.
La fonction publique `extraire_source_fenetres(source: str) -> str` doit retrouver
exactement cette empreinte depuis le manuscrit enveloppé, sans dépendre de la
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

Ces tests ne contactent pas l’API GitHub et ne prétendent pas simuler son filtre.
GitHub filtre le CSS inline : ajouter du HTML avec `style` n’est donc pas une
solution de présentation pour son aperçu Markdown. La conservation distante de
`picture/source/img/details/summary` doit être prouvée séparément par l’intégration.
Le rendu réel desktop/mobile, les ombres, la lisibilité, les polices, les coupures
et l’absence de troncature nécessitent aussi une revue navigateur distincte :
présence du texte dans un SVG ne garantit pas à elle seule sa visibilité à l’écran.
