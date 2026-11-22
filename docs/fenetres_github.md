# Fenêtres du système dans l’aperçu GitHub

## Lecture et périmètre

Ouvrir [`roman.md`](../roman.md) dans l’onglet **Preview / Aperçu** de GitHub.
C’est le manuscrit unique et le point d’entrée principal. Chaque fenêtre présente
une image SVG locale en couleur et une **version textuelle complète** dépliable
dans le même fichier. Les variantes bureau/mobile utilisent `picture` et `source`.

DEC-103 répond à la demande de couleur depuis l’aperçu GitHub, avec choix
technique délégué. C’est une exception d’affichage pour les véritables fenêtres
du système, pas une illustration narrative. DEC-101 reste applicable : aucune
image de scène au chapitre 1, illustrations narratives réservées au manhwa,
image du couple conservée dans le README. Ni données, ni narration, ni statuts
des chapitres ne sont changés par cette présentation.

## Pourquoi ne pas utiliser simplement HTML/CSS ?

HTML et CSS permettent généralement cette mise en forme dans un navigateur.
Mais l’aperçu Markdown de GitHub filtre le HTML : styles et classes ne sont pas
conservés pour appliquer notre charte. Un lien vers `style.css`, des styles inline
ou un SVG inline ne résolvent donc pas le besoin dans cet aperçu.

Les SVG **référencés comme images** portent leur propre rendu vectoriel : fond
blanc, texte anthracite, bordures dorées, badges pastel, bonus runiques bleus et
effets temporaires verts. Les libellés restent explicites ; la couleur ne doit
jamais être l’unique moyen de distinguer les catégories.

### Preuves disponibles et limites

Sondes du 22 novembre 2026 via l’[API Markdown officielle](https://docs.github.com/en/rest/markdown/markdown) :

- Le test de styles a répondu HTTP 200 avec seulement
  `<div>Fenêtre de test</div>`, sans styles ni classes. Trace temporaire :
  `/tmp/opencode/arcaniste-github-20261122/test-css-inline.html`.
- Le test d’enveloppe a répondu HTTP 200 en conservant `picture`, `source`,
  `media`, `img`, `details` et `summary`. Trace temporaire :
  `/tmp/opencode/github-window-probe.html`.

Un contrôle supplémentaire a soumis **les 110 fenêtres** au moteur Markdown
officiel : **HTTP 200**, avec conservation de leurs 110 images, 110 sources
mobiles et 110 transcriptions dépliables. Le texte de chaque transcription
retournée a été comparé à sa source ; les 220 chemins d’assets ont été vérifiés.
Preuves de session : `preuve-github.json` et `github-render.html` sous
`/tmp/opencode/arcaniste-github-20261122/`.

Cette vérification porte sur toutes les fenêtres, pas sur la page hébergée du
manuscrit complet. L’acceptation du balisage par l’API ne prouve pas le chargement
des assets depuis un dépôt où ils ne sont pas encore publiés. Le rendu des SVG
se contrôle séparément sur bureau/mobile, avec zoom, clavier et transcription.
Les preuves temporaires de session ne sont pas des dépendances du dépôt.

**Validation automatisée finale : 34 tests réussis**, sans renouvellement de la
fixture éditoriale. Les 111 segments hors fenêtres, les données et leurs
associations restent protégés. L’extraction des enveloppes restitue exactement
le manuscrit d’entrée de cette adaptation : SHA-256
`aef0ae36950a34bb3bf7cfb1dce08f31c3a282528226fe5ad045e3da8d3d8f23`.
Le lecteur local facultatif est lui aussi identique octet pour octet à sa version
antérieure. Le générateur refuse les collisions de fichiers ; ses écritures sont
atomiques et `--check` ne répare pas silencieusement les sorties.

La sortie réelle du moteur GitHub a ensuite été contrôlée avec Chromium à
**1280×900, 390×844 et 320×844** : 110 images chargées par taille, variante bureau
ou mobile correctement sélectionnée, aucune image déformée ni débordement
horizontal détecté. Les 220 SVG ont été importés dans le DOM pour mesurer les
textes et les badges : aucun dépassement du cadre observé. Les contrastes et
l’ouverture/fermeture des transcriptions au clavier ont été contrôlés.

Rapports et captures de session : `audit-svg/` sous le même répertoire temporaire.
Cette preuve associe le HTML réellement filtré par GitHub aux assets locaux ;
elle ne revendique pas une publication du dépôt. Elle ne constitue pas non plus
une certification RGAA complète : le recours à des images de texte impose de
conserver la transcription et de poursuivre les essais de zoom/lecteurs d’écran.

## Source unique et fichiers dérivés

- **Source éditable :** tout le texte utile et toutes les données de chaque
  fenêtre restent dans le HTML de `roman.md`, à l’intérieur du `details`.
  Les classes racines et `data-window-id` restent stables.
- **Dérivés :** `assets/fenetres/ID.svg` et `assets/fenetres/ID-mobile.svg`, où
  `ID` est l’identifiant de la fenêtre. Ce ne sont ni une autre version du roman,
  ni une source primaire du canon. Ne pas les corriger à la main.
- **Générateur :** `scripts/generer_fenetres.py` découvre les fenêtres depuis
  le manuscrit. Aucun nombre de fenêtres ni registre parallèle ne doit servir
  de plafond aux futurs chapitres.

L’enveloppe produite associe une image bureau, une source mobile et un `details`
contenant le HTML complet. Les modèles HTML **NON CANON** du
[guide LitRPG](fenetres_litrpg.md) servent à préparer cette source ; remplacer
leurs marqueurs par les seules données autorisées, puis générer l’enveloppe.
Ne pas recopier un exemple de documentation comme un fait du récit.

Les SVG sont purs : texte `text`/`tspan` et primitives vectorielles locales,
sans `foreignObject`, raster incorporé, JavaScript, police distante ou CDN.
Les variantes mobile et bureau dérivent de la même source textuelle, jamais
de deux saisies manuelles de statistiques.

## Maintenance avant publication

1. Modifier la source HTML textuelle de la fenêtre dans `roman.md`, en préservant
   son identifiant et le contenu extérieur aux fenêtres. Une correction de
   présentation n’autorise aucun changement de données ou de narration.
2. Installer les dépendances du générateur dans l’environnement Python du projet
   (`Pillow==12.1.1` est fixé dans `requirements-lecture.txt`), puis régénérer les
   fenêtres depuis la racine :

   ```sh
   python3 -m pip install -r requirements-lecture.txt
   python3 scripts/generer_fenetres.py
   python3 scripts/generer_fenetres.py --check
   ```

3. Examiner le diff du Markdown et des SVG ; contrôler la conservation du texte
   utile, des valeurs, de leur ordre et de leurs catégories. Lancer les tests :

   ```sh
   python3 -m unittest discover -s tests -v
   ```

4. Contrôler les images et la transcription dans le rendu ciblé. Un test vert
   ne remplace pas la revue visuelle ni l’autorisation éditoriale.
5. **Lorsqu’un commit/push est explicitement autorisé**, inclure le Markdown et
   tous les SVG dérivés nécessaires. Publier uniquement le Markdown casserait
   les liens d’images. Cette procédure n’autorise elle-même aucune publication.

`--check` vérifie les enveloppes et les SVG sans écrire : code `0` si tout est à
jour, `1` si une régénération est nécessaire, `2` en cas d’erreur. Le générateur
signale les SVG obsolètes à examiner et retirer explicitement, sans les effacer
automatiquement. Aucun autre drapeau de génération n’est supposé ici.

## Export local facultatif

`scripts/generer_lecture.py` extrait la source des fenêtres pour produire
`lecture.html`, sans doubler les fenêtres avec leurs images et leurs `details`.
Le lecteur retrouve ainsi la présentation HTML/CSS locale. Régénérer cet export
si nécessaire ; ne jamais le modifier à la main.

Télécharger `lecture.html` et `style.css`, puis ouvrir le HTML dans un navigateur.
Il sert à la lecture locale et à l’impression, pas de détour obligatoire pour
lire sur GitHub. Aucun site GitHub Pages n’est déployé par cette adaptation.
Les commandes et limites PDF/EPUB sont dans le [guide LitRPG](fenetres_litrpg.md).

## Taille, performances et dépannage

Selon les [limites de texte officielles de GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits#text-limits),
GitHub tente généralement le rendu des fichiers de moins de **2 MB** ; des
fichiers complexes peuvent néanmoins dépasser le temps de rendu disponible.
Ce n’est pas une garantie de rendu sous ce seuil. Le manuscrit mesure
**983 845 octets après adaptation**, contre 941 526 avant les enveloppes.
Les **220 SVG occupent 2 301 305 octets au total**, répartis en petits fichiers
locaux ; une seule variante est choisie pour chaque image affichée. Aucun
blocage par taille n’est établi par ces seules mesures.
Il n’existe pas ici de limite Markdown stricte de 1 MiB à en déduire.

L’allongement vers la trilogie et la multiplication des fenêtres devront être
surveillés : poids du Markdown, nombre et poids des images, temps d’affichage
et lisibilité réelle. Ne pas promettre aujourd’hui le rendu de toute la trilogie
future, ni créer automatiquement un second manuscrit ou découper la source.

- **Image absente :** vérifier le chemin relatif, le SVG suivi dans le dépôt et
  sa présence dans la même publication que le Markdown. Déplier le texte pour
  lire les données ; ne pas les recréer depuis une capture.
- **Image périmée :** corriger la source textuelle puis régénérer ; ne pas
  masquer l’écart en éditant directement le SVG.
- **Couleurs absentes dans la transcription :** c’est le repli textuel filtré
  par GitHub, pas un défaut à contourner par du CSS inline.
- **Rendu tronqué ou indisponible :** distinguer absence d’assets, cache et
  limite du moteur GitHub ; contrôler la taille finale et le rendu réel avant
  de proposer un changement de diffusion à l’auteur.

Aucun commit, push ou déploiement n’est réalisé par cette documentation.
