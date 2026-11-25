# Correction globale des raretés et des présentations de runes

## Autorisations — DEC-178 à DEC-180

L’auteur corrige la règle de rareté : une amélioration ordinaire +0→+15 ne recolore pas une rune. Après l’audit `audit_rarete_runes_2026_11_25.md`, il demande **« fait le fix »**, exige une présentation systématiquement complète (couleur, étoiles, amélioration, principale, secondaires et valeurs), puis délègue explicitement les informations manquantes : **« Oui, choisis selon les règles »**. Il demande enfin une **règle de maintien des documents personnages/runes** pour conserver la continuité sur toute l’histoire.

Ce périmètre autorise les corrections ciblées et les ajouts de fiches, pas une réécriture narrative générale, de nouvelles acquisitions racontées, un chapitre supplémentaire ou une publication.

## Références canoniques et traçabilité

- **`../lore/runes.md`** : unique référentiel des IDs, fiches complètes, valeurs et états par livre/vie/chapitre. Le bloc DEC-179 distingue les données connues des choix éditoriaux délégués ; les nouvelles valeurs ne constituent pas un barème universel.
- **`../lore/personnages.md`** : porteurs, équipement, réserves et transferts par étape, avec renvois vers les mêmes IDs ; pas de duplication des affixes.
- **DEC-180 / `../AGENTS.md`** : une modification de runes ou d’équipement n’est pas livrée comme terminée sans synchronisation de ces deux références et contrôle de la narration, des fenêtres et des dérivés.
- Archives `new.txt`, `old.txt` et copies de révisions conservées intactes. Les journaux de corrections exactes destinés aux tests sont des preuves de conservation, pas un inventaire éditorial concurrent.

## Choix délégués utiles au raccord

- La première Énergie maternelle traitée au chapitre 9 du I est **HAS-R009, rare bleue** ; la seconde est **HAS-R010, peu commune verte**. Toutes deux restent 3★, +9, données à Yoon avec leurs identités et affixes ; pas de nouvelles pierres.
- Les identités des Gardien conservées, rangées et rééquipées sont fixées dans le journal ; elles ne changent pas leurs étoiles lors d’une amélioration.
- Les seize pierres finales du I sont désormais présentées **rares bleues, 6★, +15** : cinq raretés déjà connues et onze raretés retenues par délégation, non une déduction depuis « rare minimum ». Les deux cadeaux paternels restent HAS-R001/002 ; quatorze IDs distincts documentent les autres pièces finales sans transformer les anciennes 2★/3★ en 6★.
- Les équipements du II ont des IDs propres à leur vie : sept pièces portées et une seconde Énergie en réserve, puis huit Vol de vie reçues et équipées le soir. Aucun transport matériel depuis le I.
- F01 du II reste **Énergie commune blanche, 1★, +3, Résistance +4 %, Vitesse +1 en gras**. La seconde expérience verte et la pierre blanche prometteuse sont des exemplaires distincts.
- La rune d’Iseria est analysée puis rendue intacte à +9 ; sa projection +15 reste conditionnelle. La rune temporelle reste une **identification partielle narrative**, pas une fiche ordinaire complétée en révélant ses secrets futurs.

## Invariants à conserver

1. Rareté et étoiles ne changent pas par amélioration ordinaire ; Savoir runique relève d’un pouvoir futur distinct.
2. Principales renforcées à chaque réussite ; secondaires aux paliers existants, quatre maximum. Seules les communes blanches à +0/+1/+2 n’ont aucune secondaire.
3. Aucun CC/DCC runique, PA %, PV % ou Défense % secondaires ajoutés ; Attaque % secondaire admise. Données déjà connues préservées.
4. Bonus d’ensemble séparés des affixes individuels ; aucune formule d’XP, d’arrondi, de coût ou statistique naturelle inventée.
5. Ni don, vente, destruction, acquisition datée ou rééquipement post-ellipse ajouté pour combler un trou de documentation.
6. L’anomalie des huit cercles rétroactifs du I reste 2/10 avant les cadeaux maternels ; le cercle anticipé du II a sa réserve et passe immédiatement à 8/8.
7. Sommaires, événements, relations, niveaux et compteurs conservés. Ajouts de Croissance du chapitre 1 du II toujours à relire.

## État des opérations

**Correction globale achevée :** référentiel, porteurs, présentations des deux manuscrits, SVG et lecteur local du I sont synchronisés. Les gardes de conservation sont adaptés aux seuls changements autorisés, sans renouvellement des fixtures historiques. Les règles actives et notices de reprise sont harmonisées ; les anciens comptes rendus restent des preuves datées avec renvoi vers DEC-178/179/180.

### Livre II — intégration et contrôles ciblés

- Cinq fenêtres ajoutées (`L2-C2-R01` à `R05`) : pierre blanche prometteuse à +0 ; Gardien verte de la deuxième expérience à +0 puis +6 ; tableau des sept runes portées et de la réserve ; tableau des huit Vol de vie reçues, avant équipement. Les données de chaque ligne reprennent le référentiel DEC-179.
- Une précision narrative complète l’état +0 de la rune d’exercice F01, sans changer sa fiche +3, sa couleur blanche ou Vitesse +1 en gras. Les dix anciennes fenêtres, dont Lame et Croissance 7→8, restent identiques.
- **Quinze fenêtres et trente SVG** : génération idempotente, aucun texte hors cadre selon les coordonnées/longueurs déclarées. Les tableaux ont été examinés en rendu Chrome local : équipement en mobile et Vol de vie en bureau, données lisibles sans coupure observée. Ce contrôle ne prouve ni rendu GitHub distant, ni accessibilité complète.
- **27 tests ciblés II réussis**, incluant comparaison à l’inventaire et aux porteurs, champs complets, chronologie des présentations, absence de divulgation de l’accord d’Iseria, inversions exactes des six corrections autorisées, tests de mutations et conservation des protections précédentes. Le chapitre 1 reste protégé par son empreinte, après retrait strict de la navigation.
- Nouvelle fixture de corrections II dédiée ; les fixtures historiques sont conservées. Ces contrôles ciblés ont précédé la stabilisation du I ; la suite globale a ensuite été vérifiée sur les deux livres, sans renouveler aveuglément les anciennes empreintes.

### Livre I — intégration complète

- **27 fenêtres existantes** corrigées ou complétées ; **15 fenêtres ajoutées** sans renumérotation, soit **153 fenêtres / 306 SVG** au total.
- Les sept fenêtres de rareté de l’audit et leurs reprises narratives sont corrigées ; les fiches partielles, tableaux d’équipement et sept exemplaires individuels restants ont été complétés depuis le référentiel. Les deux lots génériques restent génériques, sans inventaire artificiel.
- Pièces finales : HAS-R001/002 et HAS-R016 à 029, seize rares bleues 6★ +15 ; aucun ancien exemplaire 2★/3★ transformé en 6★. Paire donnée à Yoon : mêmes HAS-R009 bleue/HAS-R010 verte, 3★ +9 ; anciennes runes de Yoon rangées, pas vendues/données.
- Rune d’Iseria et rune du marchand déjà orange conservées ; projections conditionnelles explicitement non acquises et améliorations non garanties. La petite verte du chapitre 12 appartient au jeune chasseur et est évoquée ensuite par Orven, pas par Zio.
- SHA-256 I final : `a26785c286e66efe96466aa355d08aba4a002a670c32d52491e261d47d257575`. Source initiale avant correction globale : `9d27a766bef9706867ebbf658ba4dd2ecfb46b885cbf6a4e5d850ad3ae0caa2b`.
- Deux étapes de conservation : **126 corrections exactes**, puis **11 compléments exacts**, inversées dans cet ordre logique inverse pour reconstituer la source initiale octet pour octet. Les deux journaux sont de nouvelles fixtures ciblées ; les deux fixtures historiques suivies sont inchangées.

### Contrôles de clôture

- `python3 -m unittest discover -s tests` : **95 tests réussis**, dont 27 contrats du II et les contrôles indépendants du I. Ils comparent notamment **124 lignes de présentation à 78 états canoniques**, les fiches individuelles, paliers/secondaires autorisés, identités et étoiles fixes, transferts, occupations, statistiques naturelles et badges de classe préservés. Les mutations de valeur, ordre, suppression, duplication, déplacement ou insertion sont détectées.
- `python3 scripts/generer_fenetres.py --check` : **153 fenêtres / 306 SVG à jour**. `python3 scripts/generer_lecture.py --check` : lecteur local à jour. Contrôle sans écriture du II via `produire` : **15 fenêtres / 30 SVG à jour**.
- Rune et porteur ont été vérifiés ensemble : les journaux de corrections ne servent pas d’inventaire canonique et n’exemptent ni les fenêtres ni les chapitres de contrôle. Les anciennes empreintes sont appliquées après inversion exacte des changements autorisés.
- Contrôles géométriques Chromium de l’intégration I : 12 268 éléments puis 1 346 éléments des compléments mesurés, aucun débordement signalé ; lecteur vérifié à 320/390/1280 px sans débordement horizontal. Contrôle visuel supplémentaire de la session principale : 034 mobile (blanche +3 avec Défense), 079 bureau (paire bleue/verte et anciennes runes de Yoon) et C12-R01 mobile (marchand réel +9 / projection +15), textes complets et lisibles sans coupure observée. Ce sont des rendus locaux, pas une preuve du filtre GitHub ou une certification RGAA.
- Taille des sources finales : I **1 431 593 octets**, II **186 956 octets**. Générateurs, dépendances et CSS inchangés ; pas de ressource distante ou de contenu actif ajouté.
- SHA-256 II final : `9ceadd42efe738a957883e48eb22bd46a09e448133c7304b1ca8a44f7e52f731` ; chapitre 1 protégé par son empreinte historique après retrait exact de la navigation. Les ajouts Croissance de ce chapitre restent à relire.
- Archives conservées : `docs/new.txt` `70ceecfdbe699d54e844c42e64bef0c9f6e3288a313d7f7b1d6deb2462118a59`, `docs/old.txt` `3ebf4def051aaf2746f846ee1b5f9d4f0091be393e604a3d9f183d297569c3c4`.
- Aucun nouveau chapitre, commit, push, déploiement ou intervention en production.
