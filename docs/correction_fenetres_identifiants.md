# Correction globale des fenêtres — identifiants et retours de ligne

## Périmètre

Correction locale de présentation uniquement, sans commit ni push. Les données
canoniques, leur ordre et la narration hors fenêtres sont préservés. Les SVG sont
régénérés depuis le HTML des manuscrits ; aucun SVG n’a été corrigé à la main.

## Résultat de l’audit dynamique

| Livre | Fenêtres source | SVG bureau/mobile | Fenêtres avec ID visible corrigées | Occurrences `data-rune-id` | IDs uniques |
|---|---:|---:|---:|---:|---:|
| I | 153 | 306 | 42 | 144 | 44 |
| II | 26 | 52 | 1 (`L2-C3-F04`) | 48 | 46 |
| **Total** | **179** | **358** | **43** | **192** | — |

Les 32 identifiants visibles de `L2-C3-F04` ont rejoint les lignes `<tr>` ; les
16 métadonnées déjà présentes dans les fenêtres antérieures du II sont
conservées. Les préfixes sont découverts depuis les métadonnées et l’inventaire,
sans liste métier figée : `CLI`, `GRI`, `HAS`, `L2-HAS`, `MAR`, `ORV`, `REC` et
`YOO` dans les fenêtres actuelles.

Les contrôles retrouvent zéro identifiant documentaire dans le texte visible des
179 fenêtres, leurs transcriptions et les 358 SVG. Les `data-window-id` restent
stables et invisibles. Les identifiants de runes restent attachés à la fiche ou à
la ligne correspondante via `data-rune-id`.

## Corrections techniques

- `generer_fenetres.py` refuse désormais un `data-rune-id` non sûr ou recopié
  dans le texte de sa fenêtre.
- Le calcul des retours SVG regroupe les couples courts libellé/valeur signée et
  valeur/unité lorsqu’ils tiennent dans la largeur disponible.
- Les milliers et pourcentages utilisent des espaces insécables dans les sources
  de fenêtres. Les contrôles géométriques ne trouvent plus de séparation entre
  une valeur numérique et `%`, sur bureau comme sur mobile.
- Les en-têtes historiques `.system-header` et modernes
  `.lit-window__header` suivent le même rendu SVG et fournissent le titre de
  l’alternative d’image.
- Le CLI accepte des chemins explicites pour générer et contrôler le livre II,
  sans remplacement de chaîne en mémoire ni mélange des répertoires d’assets.
- Le lecteur local masque dynamiquement les éventuelles mentions Markdown d’un
  identifiant connu, tout en conservant les métadonnées nécessaires aux outils.

Les dix couples détectés par l’audit géométrique générique du livre I après
correction sont des faux positifs : deux paragraphes ou cellules successifs
distincts (`+1 cercle de Mana`, puis `+1 emplacement`, par exemple), et non une
caractéristique séparée de sa valeur. Aucun cas équivalent ne subsiste dans un
même flux de texte.

## Commandes et contrôles exécutés

```sh
python3 scripts/generer_fenetres.py
python3 scripts/generer_fenetres.py --check
python3 scripts/generer_fenetres.py \
  --input livre_2_le_vertige_des_vies_oubliees.md \
  --output-dir assets/fenetres-livre-2 \
  --asset-prefix assets/fenetres-livre-2
python3 scripts/generer_fenetres.py --check \
  --input livre_2_le_vertige_des_vies_oubliees.md \
  --output-dir assets/fenetres-livre-2 \
  --asset-prefix assets/fenetres-livre-2
python3 scripts/generer_lecture.py
python3 scripts/generer_lecture.py --check
python3 -m unittest discover -s tests -v
```

Résultats ciblés :

- contrôles `--check` des deux livres : succès, respectivement `153/306` et
  `26/52` ;
- `lecture.html --check` : succès ; aucun identifiant visible, contenu actif ou
  ressource distante ;
- inventaires de fichiers : exactement 306 SVG pour le I et 52 pour le II ;
- enveloppes : exactement un `picture` et un `details` par fenêtre, chemins
  distincts corrects pour les deux livres ;
- sécurité passive : aucun script, gestionnaire d’événement, `foreignObject`,
  image incorporée ou ressource distante dans les dérivés ; le test de sécurité
  documentaire existant réussit ;
- `git diff --check` ciblé : succès.

La suite existante exécute 52 tests mais reste rouge : 2 échecs et 10 erreurs.
Les contrats historiques attendent encore les identifiants dans le texte,
l’inversion DEC-179 antérieure, deux chapitres seulement dans le II, l’ancienne
description de Siphon et d’anciens condensats de chapitres. Les tests n’ont pas
été modifiés, conformément au périmètre ; leur adaptation est déléguée au lot
`test-writer` suivant.

## Limites et points de vigilance

- Aucun rendu distant GitHub ni audit RGAA complet n’a été exécuté. Les contrôles
  couvrent la structure, le texte, les chemins, la géométrie SVG et la sécurité ;
  une revue visuelle navigateur reste recommandée à 320 px et en bureau.
- Trois mentions documentaires (`L2-HAS-R017`, `L2-HAS-R001`, `L2-HAS-R002`)
  existent dans deux paragraphes narratifs du livre II. Elles sont hors fenêtres
  et n’ont pas été modifiées, car ce lot interdit tout changement de narration
  hors fenêtres. Le générateur du lecteur sait les masquer si un export du II est
  demandé, mais l’aperçu Markdown brut du II les conserve : un arbitrage
  éditorial séparé est nécessaire pour les retirer de la source.
- `docs/new.txt`, `references-visuelles/`, les PNG et les archives n’ont pas été
  modifiés par cette intervention. Les changements concurrents déjà présents y
  restent intacts.
