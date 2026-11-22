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
