# Fenêtres LitRPG : source textuelle, modèles et exports

## 1. Périmètre et sources

`livre_1_l_ascension_d_une_legende_oubliee.md` reste le manuscrit unique du livre I et son point d’entrée principal sur GitHub.
La source HTML textuelle de chaque fenêtre y est conservée intégralement dans
un `details` dépliable, sous son affichage SVG local dérivé (DEC-103).
Voir le [guide GitHub](fenetres_github.md) pour les enveloppes et leur génération.
`style.css` porte la présentation de l’export local ;
`scripts/generer_lecture.py` produit `lecture.html`, un dérivé facultatif à
régénérer, jamais à modifier à la main. Ce guide ne valide ni chapitre, ni valeur, ni règle LitRPG.
Les décisions éditoriales et leurs statuts restent dans `AGENTS.md` et `lore/`.

Les modèles ci-dessous sont des **gabarits techniques NON CANON**. Les champs
`{{…}}` sont des marqueurs à remplacer manuellement : le générateur ne fait pas
de substitution. Reprendre uniquement les données autorisées et connues au point
du récit ; une donnée manquante reste **À DÉFINIR**, jamais zéro par défaut.
Ne pas ajouter un champ simplement parce que le modèle le propose.

La source des fenêtres est du texte HTML, pas une capture d’écran ni un SVG
à éditer. Les SVG sont une exception technique d’affichage des seules fenêtres
du système, pas une autorisation d’illustrations narratives : l’auteur réserve
ces dernières au manhwa. Ne pas réintroduire les encadrés éditoriaux de lore en
ouverture ou clôture de chapitre.

## 2. Charte et classes

| Élément | Contrat de présentation locale dans `style.css` |
|---|---|
| Fond des fenêtres | Blanc `#FFFFFF` |
| Texte courant, statistiques naturelles | Anthracite `#242424` |
| Bordure | Doré `#D1AB61`, 1 px |
| Titre principal | `#A17B35`, **20 px**, graisse **750** |
| Séparateurs | `#D8BF8F` pour le titre, les tables et `hr` |
| Forme | Coins de 14 px, ombre discrète ; adaptation mobile à 480 px |
| Bonus runiques | `.rune-bonus`, bleu `#175b9b` |
| Effets temporaires | `.temporary-bonus`, vert `#22643b` |
| Notification de réussite | `.success-text`, vert `#22643b`, sans signifier un effet temporaire |

Les SVG dérivés reprennent cette charte pour GitHub ; les classes et le CSS du
HTML source ne suffisent pas à la faire apparaître dans son aperçu Markdown.
Conserver les classes de compatibilité, même lorsqu’on ajoute les classes modernes :

- Racine : `.system-window`, `.character-sheet` ou `.rune-window`, plus `.lit-window`.
  Ne pas imbriquer des fenêtres racines. Les combinaisons historiques de classes
  racines restent possibles sur le même élément.
- En-tête : `.system-header.lit-window__header` ; pictogramme : `.lit-window__icon`.
- Lignes : `.lit-window__row` ; valeur courte : `.lit-window__value`.
- Sections : `.lit-window__section`, `.lit-window__section-title` ; tables :
  `.lit-window__stats` ou `.lit-window__inventory`.
- Préserver `.legendary-text`, `.success-text`, `.passive-badge`,
  `.upgrade-badge` et les associations existantes entre bonus et valeurs.

La classe de présentation `.lit-window__runic-value` permet aussi de colorer en
bleu une valeur runique explicitement projetée, sans changer son texte ni ses
classes historiques (exemple existant : fenêtre `099`, analyse d’Œil). Elle ne
signifie pas que la projection est déjà réalisée : les libellés « actuelle »,
« finale » et la condition d’amélioration restent indispensables. Une projection
n’est jamais un effet temporaire vert ; un palier `+9` ou `+15` n’est pas un bonus.

Une statistique naturelle reste hors de tout `span` de bonus. Une réussite
n’est pas un bonus temporaire. Donner un libellé visible à chaque catégorie :
la couleur seule ne transmet pas le sens. Ne pas ajouter de fond sombre,
de styles inline ou d’emoji multicolore.

### Badges : deux catégories distinctes

Ajouter la classe commune `.lit-badge` au modificateur choisi :

| Catégorie | Libellé | Modificateur |
|---|---|---|
| Classe | Commune | `lit-badge--common` |
| Classe | Rare | `lit-badge--rare` |
| Classe | Légendaire | `lit-badge--legendary` |
| Classe | Astrale | `lit-badge--astral` |
| Rune | Commune (blanche) | `lit-badge--rune-common` |
| Rune | Peu commune (verte) | `lit-badge--rune-uncommon` |
| Rune | Rare (bleue) | `lit-badge--rune-rare` |
| Rune | Épique (violette) | `lit-badge--rune-epic` |
| Rune | Légendaire (orange) | `lit-badge--rune-legendary` |

Les fonds sont pastel ; la classe légendaire est dorée, le grade légendaire
d’une rune est orange. Ne pas les intervertir. La rareté de classe ne donne pas
le rang d’une rune. Pour chaque rune identifiable, préciser son grade ou sa
couleur et son rang `{{rang}}★`, puis son amélioration si connue ; le nom
d’ensemble ne remplace pas ces données. L’amélioration se présente dans
`<span class="upgrade-badge">+{{palier}}</span>`.

## 3. Identité et types de fenêtres

Chaque fenêtre porte un `data-window-id` unique et stable dans le manuscrit.
Les identifiants existants utilisent une suite comme `001`, `002`, etc. Avant
un ajout, relever les identifiants déjà présents, choisir un identifiant libre
et conserver les anciens, même si une fenêtre change de position. Ne pas
recycler un identifiant supprimé ni renuméroter toutes les fenêtres. La suite
n’impose aucun nombre maximal de fenêtres ni de chapitres ; au-delà de trois
chiffres, conserver la valeur entière sans troncature.

`data-window-type` est un vocabulaire technique fermé pour ce guide, indépendant
des classes CSS. Utiliser l’un des types ci-dessous ; un nouveau type nécessite
une mise à jour explicite du contrat, pas une variante orthographique improvisée.
Les références sont des exemples réellement présents, pas des données à recopier.

| Type | Usage | Exemple existant par `data-window-id` |
|---|---|---|
| `revelation` | Révélation de classe | `001` |
| `personnage` | Fiche ou identité | `006` |
| `niveau` | Passage de niveau | `007` |
| `caracteristiques` | Gains ou évolution naturelle | `012` |
| `competence` | Acquisition, description active ou passive | `013` |
| `rune` | Identification d’une rune | `002` |
| `amelioration` | Tentative, réussite ou échec | `020`, `021` |
| `equipement` | Équipement ou effets de runes équipées | `003` |
| `effet-temporaire` | Effet actif limité | `042` |
| `ensemble` | Ensemble runique | `053` |
| `monstre` | Identification de monstre ou boss | `010` |
| `combat` | Résultat et gains de combat | `011` |
| `equipe` | Composition et points du groupe | `046` |
| `croissance` | Compteurs, cercles et emplacements | `014` |
| `bilan` | Synthèse d’activité | `030` |
| `inventaire` | Liste structurée de runes | `019` |
| `entrainement` | Résultat d’exercice | `024` |
| `regle` | Message du système énonçant une règle | `043` |

Un boss utilise `monstre`, pas un nouveau type `boss`. Une compétence passive
utilise `competence`, pas `passive`. Ces attributs ne créent aucune mécanique
et ne sont pas des ancres HTML `id`.

## 4. Composant commun et pictogramme local

Ce modèle décrit la **source HTML textuelle**, avant son enveloppe de publication
GitHub générée. Son SVG inline décoratif sert au lecteur local, pas au rendu
Markdown GitHub, qui le filtre. Ne pas remplacer la source textuelle par une image.

Copier cette enveloppe complète, remplacer les marqueurs, choisir la classe
racine adaptée, puis remplacer le paragraphe du corps par une variante de la
section suivante. Placer le bloc à la marge gauche du Markdown, avec une ligne
vide avant et après. Dans le bloc, écrire du HTML, pas du Markdown imbriqué.

```html
<div class="system-window lit-window" data-window-id="{{identifiant_libre}}" data-window-type="{{type_autorisé}}">
  <div class="system-header lit-window__header">
    <svg class="lit-window__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m12 3 8 5v8l-8 5-8-5V8Z M12 7v10 M8 10l8 4"/></svg>
    {{TITRE_EXPLICITE}}
  </div>
  <p>{{texte_établi}}</p>
</div>
```

Ce SVG reprend le motif géométrique local du manuscrit : primitives originales
en style trait, monochromes, sans bibliothèque distante ni icône Lucide copiée.
Il fonctionne sans sprite externe, police d’icônes, CDN ou téléchargement.
Pour une variante, remplacer seulement les primitives par un dessin local
adapté (`path`, `circle`, `rect`, `line`, `polyline`, `polygon`). Ne pas copier
une bibliothèque tierce en supposant sa licence acquise.

Les pictogrammes sont décoratifs : le titre porte tout le sens. Conserver
`aria-hidden="true"` et `focusable="false"`. Ce modèle n’a aucun `id` SVG,
donc aucune collision lors de sa répétition. Éviter `defs`, filtres et références
`url(#…)` ; si une référence interne est indispensable, rendre ses identifiants
uniques par fenêtre. Aucun script, gestionnaire `on…`, `foreignObject`, image
incorporée ou lien externe dans les pictogrammes.

## 5. Variantes de corps HTML

Chaque fragment remplace **le corps uniquement** de l’enveloppe précédente.
Les titres proposés décrivent le type, pas une nouvelle scène. Les marqueurs
ne doivent pas subsister dans une version de lecture destinée à l’auteur.
Échapper les valeurs textuelles en HTML (`&amp;`, `&lt;`, `&gt;` et les
guillemets dans les attributs). Aucun calcul automatique n’est fourni.

### Révélation — `revelation`, racine `system-window`

Titre : « RÉVÉLATION DE CLASSE ». Choisir le modificateur de badge de **classe**.

```html
<h3>{{nom}}</h3>
<p class="lit-window__row"><strong>Classe éveillée :</strong> <span>{{classe}}</span></p>
<p class="lit-window__row"><strong>Orientation :</strong> <span>{{orientation}}</span></p>
<p><strong>Rareté de classe :</strong> <span class="lit-badge {{modificateur_classe}}">{{rareté}}</span></p>
<p><strong>Niveau :</strong> {{niveau}}</p>
<p><strong>Cercles de mana :</strong> {{cercles}}</p>
<p><strong>Emplacements runiques :</strong> {{emplacements}}</p>
```

### Personnage — `personnage`, racine `character-sheet`

Titre : « FICHE DE PERSONNAGE ». Répéter les lignes de statistiques nécessaires.
Conserver les données naturelles séparées des bonus, sans total non validé.

```html
<h3>{{nom}}</h3>
<p>{{classe}} — <span class="lit-badge {{modificateur_classe}}">{{rareté_classe}}</span></p>
<p><strong>Niveau :</strong> {{niveau}} — <strong>XP connue :</strong> {{xp_ou_À_DÉFINIR}}</p>
<table class="lit-window__stats">
  <caption>Caractéristiques naturelles, hors bonus</caption>
  <thead><tr><th scope="col">Caractéristique</th><th scope="col">Valeur naturelle</th></tr></thead>
  <tbody><tr><th scope="row">{{caractéristique}}</th><td>{{valeur_naturelle}}</td></tr></tbody>
</table>
<p><strong>Bonus runiques :</strong> <span class="rune-bonus">{{bonus_validés}}</span></p>
<p><strong>Effet temporaire :</strong> <span class="temporary-bonus">{{effet_actif_établi}}</span></p>
<p><strong>Cercles / emplacements occupés :</strong> {{état_établi}}</p>
```

### Niveau, caractéristiques et gains — `niveau`, `caracteristiques` ou `combat`

Racine `system-window`. Choisir le type selon l’objet principal de la fenêtre.
Titre : « NIVEAU SUPÉRIEUR », « GAINS NATURELS » ou « RÉSULTAT DU COMBAT ».

```html
<p><strong>Personnage :</strong> {{nom}}</p>
<p class="lit-window__row"><strong>Niveau :</strong> <span>{{avant}} → {{après}}</span></p>
<p><strong>XP gagnée :</strong> {{gain_connu_ou_À_DÉFINIR}}</p>
<table class="lit-window__stats">
  <caption>Gains naturels établis</caption>
  <thead><tr><th scope="col">Caractéristique</th><th scope="col">Gain naturel</th></tr></thead>
  <tbody><tr><th scope="row">{{caractéristique}}</th><td>{{gain}}</td></tr></tbody>
</table>
```

Supprimer les lignes sans objet. Aucun gain d’XP, seuil, arrondi ou progression
intermédiaire ne doit être déduit pour compléter le tableau.

### Compétence active ou passive — `competence`, racine `system-window`

Titre : « COMPÉTENCE ACQUISE » ou le titre déjà établi. Corps actif :

```html
<h3>{{nom_compétence}}</h3>
<p><strong>Type :</strong> <span class="lit-badge">Active</span></p>
<p>{{description_validée}}</p>
<p><strong>Cible / portée :</strong> {{paramètres_connus_ou_À_DÉFINIR}}</p>
<p><strong>Coût / durée / récupération :</strong> {{paramètres_connus_ou_À_DÉFINIR}}</p>
<p><strong>Conditions et limites :</strong> {{conditions_établies}}</p>
```

Pour une passive, remplacer la ligne « Type » par celle-ci et ne conserver
que les paramètres réellement pertinents :

```html
<p><strong>Type :</strong> <span class="passive-badge">Passive</span></p>
```

Un badge n’autorise pas à transformer un actif ciblé en aura ou en passif.

### Identification de rune — `rune`, racine `rune-window`

Titre : « IDENTIFICATION DE RUNE ». Conserver l’identité stable de la rune,
distincte de l’identifiant de fenêtre. Répéter les secondaires connues seulement.

```html
<h3>{{ensemble_ou_nom}}</h3>
<p><strong>Identifiant :</strong> {{identifiant_rune}}</p>
<p><strong>Grade :</strong> <span class="lit-badge {{modificateur_grade_rune}}">{{grade_et_couleur}}</span> — <strong>Rang :</strong> {{rang}}★ — <strong>Amélioration :</strong> <span class="upgrade-badge">+{{palier}}</span></p>
<p><strong>Principale :</strong> <span class="rune-bonus">{{principale_et_valeur}}</span></p>
<p><strong>Secondaire :</strong> <span class="rune-bonus">{{secondaire_et_valeur}}</span></p>
<p><strong>Propriétaire / état :</strong> {{propriétaire_et_état_connus}}</p>
```

### Amélioration réussie ou échouée — `amelioration`, racine `rune-window`

Titre : « TENTATIVE D’AMÉLIORATION ». Partie commune :

```html
<p><strong>Rune :</strong> {{nom}} <span class="lit-badge {{modificateur_grade_rune}}">{{grade_et_couleur}}</span>, {{rang}}★</p>
<p><strong>Tentative :</strong> <span class="upgrade-badge">+{{avant}}</span> → <span class="upgrade-badge">+{{visé}}</span></p>
```

Ajouter **un seul** résultat. Réussite :

```html
<p><strong>Résultat :</strong> <span class="success-text">Réussite</span></p>
<p><strong>Amélioration atteinte :</strong> <span class="upgrade-badge">+{{atteint}}</span></p>
<p><strong>Changements établis :</strong> <span class="rune-bonus">{{affixes_et_valeurs_après}}</span></p>
<p><strong>Ressources consommées :</strong> {{données_connues_sans_barème_inventé}}</p>
```

Échec :

```html
<p><strong>Résultat :</strong> Échec</p>
<p><strong>État après la tentative :</strong> {{état_établi}}</p>
<p><strong>Ressources consommées :</strong> {{données_connues_sans_barème_inventé}}</p>
```

Ne pas déduire de destruction, perte de palier ou nouvel affixe d’un échec.
Ne pas supprimer la consommation ou la possibilité d’échec lors d’une réussite.

### Bonus d’équipement, ensemble et effet temporaire

Types `equipement`, `ensemble`, `effet-temporaire` ; racine `system-window`
ou `rune-window` pour un ensemble. Titre explicite selon le cas. Fragments
indépendants, à utiliser uniquement lorsque la catégorie existe dans la scène :

```html
<p><strong>Bonus runique :</strong> <span class="rune-bonus">{{caractéristique_et_bonus}}</span></p>
<p><strong>Ensemble :</strong> {{nom_ensemble}} — {{pièces_actives}} — <span class="rune-bonus">{{effet_validé}}</span></p>
<p><strong>Effet temporaire actif :</strong> {{source}} — <strong>Cible :</strong> {{cible}}</p>
<p class="temporary-bonus">{{effet_temporaire_validé}}</p>
<p><strong>Durée et limites :</strong> {{données_connues_ou_À_DÉFINIR}}</p>
```

Ne pas colorer en vert une augmentation naturelle permanente. Ne pas calculer
de total lorsque l’ordre d’application des bonus n’est pas validé.

### Monstre ou boss — `monstre`, racine `system-window`

Titre : « IDENTIFICATION — MONSTRE » ou « IDENTIFICATION — BOSS » selon la source.

```html
<h3>{{nom_identifié}}</h3>
<p><strong>Type :</strong> {{type_connu}}</p>
<p><strong>Niveau :</strong> {{niveau_connu_ou_À_DÉFINIR}}</p>
<p><strong>Informations révélées :</strong> {{informations_accessibles_dans_la_scène}}</p>
```

Une fiche du système ne doit pas révéler par défaut les secrets de la bible.
N’ajouter statistiques, affinités ou récompenses que si elles sont établies.

### Équipe — `equipe`, racine `system-window`

Titre : « COMPOSITION DE L’ÉQUIPE ». Répéter une ligne par membre réellement présent.

```html
<table>
  <caption>Membres et points de classe</caption>
  <thead><tr><th scope="col">Membre</th><th scope="col">Classe et rareté</th><th scope="col">Points</th></tr></thead>
  <tbody><tr><th scope="row">{{nom}}</th><td>{{classe}} — <span class="lit-badge {{modificateur_classe}}">{{rareté}}</span></td><td>{{points}}</td></tr></tbody>
</table>
<p><strong>Effectif :</strong> {{effectif}} / {{limite_validée}}</p>
<p><strong>Points de classe :</strong> {{total}} / {{plafond_validé}}</p>
```

### Croissance et cercles — `croissance`, racine `system-window`

Titre : « CROISSANCE RUNIQUE ». Séparer les compteurs ; ne pas convertir
automatiquement XP, niveau, éliminations et boss les uns dans les autres.

```html
<p><strong>Compteur concerné :</strong> {{nom_du_compteur}}</p>
<p><strong>Progression :</strong> {{valeur_connue}} / {{seuil_validé}}</p>
<p><strong>Cercles runiques :</strong> {{avant}} → {{après}}</p>
<p><strong>Emplacements disponibles :</strong> {{disponibles}}</p>
<p><strong>Emplacements occupés :</strong> {{occupés_connus_ou_À_DÉFINIR}}</p>
```

### Bilan et inventaire — `bilan` ou `inventaire`

Pour un bilan (`system-window`), titre « BILAN D’ACTIVITÉ » et lignes explicites :

```html
<p><strong>Période :</strong> {{période_établie}}</p>
<p><strong>Résultats :</strong> {{résultats_connus}}</p>
<p><strong>Ressources restantes :</strong> {{ressources_connues_ou_À_DÉFINIR}}</p>
```

Pour un inventaire de runes (`character-sheet`), titre « INVENTAIRE RUNIQUE ».
Garder **trois colonnes** pour la disposition mobile existante. Répéter les
lignes sans condenser plusieurs runes d’identités différentes en une seule.

```html
<table class="lit-window__inventory" role="table">
  <caption>Runes inventoriées au moment de la scène</caption>
  <thead><tr><th scope="col">Rune, grade, rang et amélioration</th><th scope="col">Principale</th><th scope="col">Secondaires</th></tr></thead>
  <tbody>
    <tr><td>{{identifiant_rune}} — {{nom}} <span class="lit-badge {{modificateur_grade_rune}}">{{grade_et_couleur}}</span>, {{rang}}★, <span class="upgrade-badge">+{{palier}}</span></td><td><span class="rune-bonus">{{principale}}</span></td><td><span class="rune-bonus">{{secondaires_connues}}</span></td></tr>
  </tbody>
</table>
```

Pour `entrainement` ou `regle`, conserver l’enveloppe commune avec des paragraphes
étiquetés décrivant uniquement le résultat ou le message établi. Une règle du
système n’est pas un encadré éditorial de lore.

## 6. Générer et contrôler l’export local facultatif

Pour la lecture GitHub principale, générer d’abord les fenêtres selon
[`fenetres_github.md`](fenetres_github.md). Le lecteur local utilise la source
textuelle des fenêtres, sans leur affichage SVG ni leur repli dépliable : il ne
doit pas présenter chaque fenêtre deux fois.

Depuis la racine du dépôt, avec Python 3 et son module `venv` disponibles :

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-lecture.txt
python3 scripts/generer_lecture.py --help
python3 scripts/generer_lecture.py
python3 scripts/generer_lecture.py --check
python3 -m unittest discover -s tests -v
```

L’installation de `Markdown` peut demander le réseau ; **la génération et la
lecture une fois la dépendance installée n’en ont pas besoin**. La version est
fixée dans `requirements-lecture.txt`. Aucun navigateur n’est lancé par les tests.

Le point d’entrée `main()` utilise par défaut `livre_1_l_ascension_d_une_legende_oubliee.md`, `lecture.html` et
`style.css` à la racine. Options :

| Option | Effet |
|---|---|
| `--input CHEMIN` | Source Markdown UTF-8 |
| `--output CHEMIN` | HTML produit ; ne doit remplacer ni source ni CSS |
| `--css CHEMIN` | CSS local lié, **non copié** ; chemin relatif calculé depuis la sortie |
| `--check` | Compare le dérivé aux octets attendus, sans l’écrire |
| `--help` | Aide et codes de sortie |

Codes : `0` succès, `1` erreur ou lecteur absent/périmé, `2` arguments invalides.
Le sommaire du lecteur est recalculé depuis les chapitres sans modifier le
manuscrit. Pour ouvrir le résultat, utiliser le navigateur sur `lecture.html`
en conservant la feuille CSS à son emplacement relatif.

### Contrôles de conservation et changements éditoriaux

Les tests protègent la source de référence via `tests/fixtures/roman_avant.json` :
segments narratifs à leur position, ordre et texte des fenêtres, associations
bonus/valeurs, classes et cellules des tables. Une refonte purement visuelle
doit préserver chaque octet hors fenêtres et les données utiles des fenêtres.
Les SHA-256 détectent les différences ; ils ne prouvent pas leur autorisation.

Les nombres présents dans une fixture décrivent **son étape de référence**,
pas un plafond du manuscrit. Un import ou une révision autorisés peuvent changer
ces jalons, mais ne doivent pas masquer une régression de présentation.
Voir [`tests/README.md`](../tests/README.md) pour les limites exactes du contrôle.

**Ne jamais renouveler le manifeste pour rendre artificiellement les tests verts.**
Il faut une décision éditoriale explicite ou une délégation explicite couvrant
la nouvelle référence, conserver la preuve de conservation de l’étape précédente,
puis examiner séparément le diff éditorial autorisé. Une fois cette revue faite :

```sh
python3 tests/lecture_support.py --baseline "/chemin/vers/baseline approuvée.md"
```

Cette commande affiche le JSON sans modifier la fixture. Son remplacement et
l’adaptation des jalons des tests se font ensuite par patch revu, dans le
périmètre délégué. Le générateur ne renouvelle jamais le manifeste.

### Revue manuelle et dépannage

- CSS absent : vérifier le lien relatif et la présence de `style.css` ; ne pas
  corriger à la main le dérivé. Régénérer avec les bons chemins.
- Dépendance absente : réactiver le même environnement virtuel et installer
  `requirements-lecture.txt` avec son interpréteur.
- `--check` en échec : régénérer après avoir contrôlé le diff des sources.
- Test de conservation en échec : identifier le segment ou la fenêtre concernée,
  distinguer changement autorisé et régression ; ne pas mettre à jour la fixture
  par réflexe.
- Vérifier à largeur mobile, au zoom, au clavier et avec un lecteur d’écran :
  titres lisibles, libellés sans dépendance à la couleur, en-têtes de colonnes
  présents, absence de débordement et de troncature. Les tests CSS ne mesurent
  ni le contraste calculé ni une conformité RGAA complète.

## 7. Diffusion, sécurité et formats de livre

### HTML local et GitHub : deux modes de rendu

**GitHub est prioritaire : ouvrir `livre_1_l_ascension_d_une_legende_oubliee.md` en aperçu.** GitHub filtre les
styles, classes et SVG inline ; le CSS externe ou inline n’y fournit pas cette
présentation. Les images SVG locales référencées par `picture` portent les
couleurs ; le `details` conserve toute la version textuelle dans le manuscrit.
Le guide [GitHub](fenetres_github.md) distingue les preuves d’acceptation du
balisage des contrôles visuels à réaliser.

`lecture.html` accompagné de `style.css`, avec leurs chemins relatifs conservés,
est un export facultatif à télécharger et ouvrir localement. Cliquer sur le
fichier HTML du dépôt n’équivaut pas à accéder à un site publié. Aucun GitHub
Pages n’est déployé par cette adaptation. Le lecteur et ses pictogrammes
n’utilisent ni JavaScript ni ressources distantes.

Le générateur accepte le HTML/SVG **local de confiance** du manuscrit : ce n’est
pas un assainisseur de contenus non fiables. Sa CSP restrictive est une défense
complémentaire, pas une garantie absolue pour tout contenu ou moteur. Examiner
les apports avant conversion ; ne pas injecter de scripts, ressources externes
ou attributs exécutables. Les SVG simples et répétés évitent des dépendances et
requêtes réseau ; éviter les effets lourds et mesurer les longs documents dans
le navigateur réellement utilisé.

### PDF et impression

Utiliser l’impression du navigateur depuis le lecteur. Les règles `@media print`
retirent ombres, pictogrammes et navigation ; elles permettent aux grandes fenêtres
de se répartir sur plusieurs pages, tentent de garder titres et paragraphes
ensemble et répètent les en-têtes de table. Ce ne sont pas des garanties de
pagination identique entre moteurs. Contrôler l’aperçu PDF : une fenêtre plus
haute qu’une page ne doit pas être forcée en bloc insécable. Vérifier les tableaux,
les coupures et la lisibilité des bonus sans dépendre de l’impression en couleur.

### EPUB 3

Il n’existe pas d’exporteur EPUB dans le générateur actuel. Une conversion devra
adapter et empaqueter HTML/XHTML, CSS et SVG locaux dans un EPUB 3, vérifier les
liens, identifiants et contraintes du format, puis valider le paquet avec
EPUBCheck. Tester ensuite sur les moteurs et appareils ciblés : Grid, SVG,
polices système, couleurs et pagination peuvent différer malgré le repli CSS
existant. Ni compatibilité certifiée EPUB, ni prise en charge de toutes les
plateformes Kindle ne sont promises par ce guide.

## 8. Retour arrière ciblé

Avant intervention, relever `git status` et le diff, et conserver une sauvegarde
de l’état de départ. En cas de régression, restaurer par **patch ciblé** les seules
fenêtres ou règles CSS introduites par l’intervention, sans écraser les changements
éditoriaux ou les modifications préexistantes d’autres intervenants. Ne pas utiliser
de `git reset --hard` ni de restauration globale du manuscrit. Régénérer ensuite
`lecture.html`, relancer `--check` et les tests avec la référence approuvée, puis
contrôler les fenêtres concernées à l’écran et à l’impression.
