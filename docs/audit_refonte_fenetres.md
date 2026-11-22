# Audit de la refonte des fenêtres LitRPG

## Actualisation : lecture directe sur GitHub — DEC-103

L’audit ci-dessous décrit la refonte HTML/CSS initiale et son lecteur local.
La cible a ensuite été précisée par l’auteur : **couleurs dans l’aperçu GitHub
de `roman.md`**, sans passage obligatoire par `lecture.html`.

Les 110 fenêtres comportent désormais une image SVG responsive et une
transcription textuelle complète dans le même manuscrit. **220 SVG dérivés**
préparent les formats bureau/mobile. Ce sont des représentations du système,
pas des illustrations narratives. La source textuelle reste inchangée et le
lecteur local retrouve son HTML original par extraction des seules enveloppes.

**34 tests passent** ; le moteur GitHub officiel a conservé les images, variantes
et transcriptions des 110 fenêtres lors d’une requête HTTP 200. Les détails,
preuves et limites de cette correction figurent dans `fenetres_github.md`.

## Périmètre et séparation des interventions

Intervention du 22 novembre 2026. La demande porte sur toutes les fenêtres du
manuscrit officiel, pas seulement sur les modèles des prochains chapitres.

Deux étapes distinctes évitent de confondre mise en forme et révision éditoriale :

1. **Présentation du manuscrit initial, chapitres 1–9 :** 89 fenêtres modernisées,
   sans modification de la narration ni des données des fenêtres.
2. **Apports autorisés pendant le travail :** validation des révisions 1–4 sans
   repères du lore, intégration des textes 10 V2, 11 et 12 après arbitrages, puis
   harmonisation des 21 fenêtres supplémentaires. Les changements éditoriaux et
   leurs sources sont détaillés dans `integration_chapitres_1_12.md`.

Les nouveaux barèmes et fiches relèvent des décisions explicites ou déléguées
DEC-097 à DEC-101, jamais d'une déduction graphique. Les chapitres 10–12 sont
intégrés en lecture, sans validation littéraire globale. Aucun chapitre 13,
aucune illustration narrative, aucun nouvel encadré de lore.

## Inventaire contrôlé

| Chapitre | Avant intégration éditoriale | Après intégration éditoriale |
|---|---:|---:|
| 1 | 16 | 16 |
| 2 | 14 | 14 |
| 3 | 4 | 5 |
| 4 | 4 | 5 |
| 5 | 10 | 10 |
| 6 | 4 | 4 |
| 7 | 9 | 9 |
| 8 | 6 | 6 |
| 9 | 22 | 22 |
| 10 | — | 10 |
| 11 | — | 5 |
| 12 | — | 4 |
| **Total** | **89** | **110** |

Une racine peut porter plusieurs classes historiques : le décompte utilise les
plages HTML imbriquées, pas la somme des occurrences de classes. Les fenêtres
composites restent uniques. Les notifications seulement racontées dans la prose
des anciens chapitres ne sont pas transformées en nouvelles scènes système.

Types couverts : révélation de classe, fiches et caractéristiques, niveaux,
compétences actives/passives, identification et amélioration de runes, équipement,
ensembles, effets temporaires, compteurs de Croissance, équipe, monstres et boss,
combats, entraînements, bilans et règles affichées.

## Preuves de conservation

- Manuscrit initial : SHA-256
  `091957208d12697f1d0cdbeec6b39d4137bb66dfd3a551abd18c7b384993922f`.
- Première passe : 89 textes de fenêtres et leurs associations de valeurs
  préservés ; **90 segments intercalaires identiques octet pour octet** ; cinq
  tableaux conservés. Suite initiale : **19 tests réussis**.
- Seuls les signes décoratifs `✦`, `◆`, `✓` des en-têtes sont remplacés par
  des SVG. Les étoiles de rang, opérateurs, nombres et textes utiles restent
  protégés, y compris `★ LÉGENDAIRE ★`.
- L'intégration éditoriale a conservé les 89 fenêtres modernisées, les narrations
  approuvées 1–4 et les anciens chapitres 5–9 ; elle ajoute deux fenêtres de
  révision et dix-neuf fenêtres des chapitres 10–12. Une QA indépendante a
  comparé les textes transmis et leurs limites d'intégration.
- Baseline après intégration, avant seconde passe graphique : SHA-256
  `bd983162161efdb1acd6d2469339b2104cb6d93fc735fd5793722ca0d747cb3b`.
  Cette référence comporte **110 fenêtres et 111 segments intercalaires**.
- Les fixtures de tests contiennent des empreintes et des métadonnées, pas un
  second manuscrit. Leur renouvellement demande une décision éditoriale explicite.

## Charte et lecteur

Fond blanc, texte anthracite, bordures et séparateurs dorés, titres dorés en
20 px gras, badges pastel distincts pour classes et grades runiques. Les bonus
runiques restent bleus ; les effets temporaires verts sont distincts des
notifications de réussite et des projections de caractéristiques.

Chaque fenêtre reçoit un identifiant stable, un type et un pictogramme SVG
monochrome inline, décoratif et non focalisable. Les dessins sont locaux, sans
chargement de bibliothèque, police d'icônes ou script distant.

`lecture.html` est généré depuis `roman.md` par `scripts/generer_lecture.py` et
charge `style.css`. Le manuscrit reste la source officielle. Les commandes,
modèles et limites des formats sont dans `fenetres_litrpg.md`.

## Contrôles de rendu

Première passe contrôlée avec **Chrome 157 headless**, par CDP, à 1280×900,
390×844 et 320×844, puis en média d'impression et en ouverture locale `file://` :

- 89 fenêtres examinées à chaque largeur ; aucun débordement ni contenu tronqué
  détecté ; palette et SVG vérifiés ; cinq tableaux conservés dans l'arbre
  d'accessibilité.
- Contrastes mesurés : texte anthracite 15,52:1, bleu 6,99:1, vert 7,11:1 ;
  titres dorés 3,89:1, admissibles à la taille et graisse retenues ; badges
  examinés au moins à 5,69:1.
- Navigation au clavier et lien d'évitement testés ; les icônes et la navigation
  sont masquées à l'impression sans retirer les données des fenêtres.

**Seconde passe terminée : 110 fenêtres identifiées, 110 modernisées.** Les
identifiants historiques `001` à `089` et leurs blocs restent identiques ; les
nouveaux blocs reçoivent `090` à `110`, sans renumérotation des anciens.

- **20 tests automatisés réussis** : 110 textes de fenêtres, 111 segments
  intercalaires, cinq tableaux et leurs cellules, associations de bonus, douze
  chapitres, identifiants, SVG locaux et protections du générateur.
- `python3 scripts/generer_lecture.py --check` confirme que le lecteur est à jour ;
  la génération est déterministe et ne remplace jamais le manuscrit ou le CSS,
  y compris par un lien physique.
- **110 fenêtres contrôlées à chacune des largeurs 1280, 390 et 320 pixels** avec
  Chrome 157 headless, en ouverture locale `file://` : aucun débordement de carte,
  troncature ou contraste insuffisant détecté. Aucune illustration narrative.
- Les projections runiques de la fenêtre `099` sont bleues, sous leurs libellés
  conditionnels, et jamais classées comme effets temporaires.
- Le média d’impression a été revérifié sur les 110 fenêtres. Un PDF de contrôle
  natif Chromium a aussi été généré hors du dépôt : texte extractible jusqu’à la
  fin du chapitre 12, PDF balisé et sans JavaScript. Il compte 854 pages au format
  Letter par défaut ; **ce n’est pas une maquette éditoriale prête à publier**.

Preuves de session dans `/tmp/opencode/arcaniste-fenetres-20261122/` : baselines et
résultats des étapes 1 et 2, puis `audit-final/rapport.json`, captures des fenêtres
aux trois largeurs et PDF de contrôle. Les empreintes permanentes et les tests du
dépôt restent la référence reproductible lorsque les artefacts temporaires ne
sont plus disponibles.

Fichiers de livraison : `roman.md`, `style.css`, `lecture.html`,
`scripts/generer_lecture.py`, `requirements-lecture.txt`, `.gitignore`, `tests/`,
les guides et audits dans `docs/`, ainsi que `README.md` et `AGENTS.md`. Les
références de `lore/`, le plan, les sources et les en-têtes des quatre archives de
révision ont été actualisés séparément pour l’intégration éditoriale approuvée.

## Limites et livraison

Les contrôles ciblés ne constituent pas une certification RGAA complète.
L'inventaire empilé sur mobile conserve ses en-têtes et sa structure accessible ;
des rappels visuels de colonnes pourraient encore améliorer son confort de lecture.

Les styles d'impression et les replis HTML/CSS préparent de futurs exports.
Aucun EPUB n'est produit ou certifié ici : empaquetage EPUB 3, validation et essais
dans les liseuses restent nécessaires. L'affichage Markdown de GitHub ne garantit
pas le rendu du lecteur HTML et de sa feuille CSS.

Les modifications préexistantes, les archives mobiles et les visuels doivent être
préservés. Aucun commit ni push n'est autorisé par cette intervention.
