# Audit de la rareté des runes — DEC-178

**Suite autorisée et réalisée — DEC-179/180 :** après cet audit, l’auteur a demandé le correctif global, imposé des fiches complètes et délégué les données manquantes. L’ordre des Énergie maternelles et les onze raretés finales ont donc été fixés dans l’inventaire, puis les présentations corrigées dans les deux livres. Ce rapport conserve les constats initiaux, pas des erreurs encore ouvertes. Les totaux actuels sont 153 fenêtres/306 SVG pour le I et 15 fenêtres/30 SVG pour le II. Voir `correction_rarete_et_fiches_runiques.md` pour choix, conservation et contrôles finaux.

## Périmètre et règle de référence

Demande auteur : **« Regarde si l'erreur ne c'est pas produit ailleur »**, après correction de F01 du chapitre 2 du II. Vérification des deux manuscrits, fenêtres HTML et SVG, générateurs, CSS, modèles et références éditoriales. Deux audits indépendants en lecture seule : livre I/images d’un côté, références/technique/livre II de l’autre. Ce rapport n’autorise pas une réécriture générale des chapitres validés.

**Règle prioritaire :** une amélioration ordinaire de +0 à +15 ne change **ni la rareté ni les étoiles**. La principale et les secondaires progressent aux paliers établis ; leur nombre ne redéfinit pas la couleur. Savoir runique d’Iseria est un pouvoir distinct, non une justification rétroactive des changements de rareté du I.

## Résultat principal

**Oui : quatre familles d’erreurs subsistent dans le livre I**, affectant directement **sept fenêtres et quatorze SVG**. Elles sont dans le contenu source ; les images reproduisent ce texte. **Aucune autre transformation de rareté n’est repérée dans le livre II hors F01, désormais corrigée.**

Les numéros de ligne ci-dessous sont ceux du manuscrit I au moment de l’audit. Ils sont des repères de réception, pas des identifiants à maintenir après correction ; les `data-window-id` restent stables.

## 1. Livre I : corrections certaines et limites

| Passage | Preuve et erreur | Correction certaine | Fenêtres |
|---|---|---|---|
| Chapitre 3, épreuve d’Orven | Rune Énergie explicitement commune blanche, 2★, +0 (4857/4867), puis dite verte à +3 (4935, 4947–4950, 4985, 5051) | Reste **commune blanche, 2★, +3**. Principale, secondaire Défense, tentatives et échec conservés | `034` |
| Chapitre 9 puis transmission à Yoon | Deux Énergie maternelles identifiées à +0 : une rare bleue et une peu commune verte, 3★ (3853–3854). Elles deviennent à tort « épiques violettes » à +9 (20227, 22008 et reprises) | La paire reste **une rare bleue et une peu commune verte, 3★, +9** ; troisième secondaire et bonus d’ensemble conservés. L’ordre individuel de passage sur l’établi n’est pas établi | `070`, `079` |
| Chapitre 10, autre essai d’Orven | Énergie commune blanche, 1★, +0 (26028–26036), puis vert/peu commun à +3 (26120, 26132, 26186, 27935) | Reste **commune blanche, 1★, +3** ; première secondaire **Mana +10**, échec et coûts inchangés | `098` |
| Chapitres 14–15, équipement final | Tous les grades affichés deviennent orange parce que +15/quatre secondaires (41359, 41439, 43844, 44528, 47958 et pièces individuelles) | Supprimer la transformation automatique. Conserver **6★, rare minimum, +15** pour l’agrégat, sans inventer la rareté exacte de chaque pièce | `C14-F01`, `C14-F09`, `C15-F10` |

Les sept identifiants correspondent à leurs deux variantes dans `assets/fenetres/` : `{ID}.svg` et `{ID}-mobile.svg`. Il faut corriger le HTML source et les mentions narratives autorisées, puis régénérer les SVG et `lecture.html` ; ne pas retoucher les dérivés à la main.

### Pièces finales dont le grade exact est connu

Cinq des seize runes finales restent **rares bleues, 6★, +15** :

- Fatal paternelle, connue rare bleue à +6 puis conservée à +15 ;
- Gardien paternelle, même continuité ;
- seconde Gardien, explicitement rare bleue avant équipement (41561–41573, 43801) ;
- première Énergie finale, explicitement rare bleue à l’origine (46219/46239) ;
- seconde Énergie finale, décrite comme la première, rare bleue à l’origine (47933–47935).

Les **onze autres pièces** sont seulement attestées **rares minimum**. Ce minimum n’autorise ni « toutes bleues » ni « toutes orange ». La correction générale peut conserver ce minimum sans fixer les onze raretés individuellement. Les Énergie finales 6★ ne sont pas les anciennes Énergie maternelles 3★ transmises à Yoon.

### Identités à ne pas inventer

- Dans `070`, la première Énergie portée à +9 n’est pas identifiée comme la bleue ou la verte. La rareté du lot est connue, pas l’ordre de traitement. Ne pas choisir arbitrairement une couleur pour cette pièce isolée.
- Les Gardien maternelles sélectionnées ou retirées ne sont pas toujours identifiées individuellement parmi deux bleues et une verte.
- Les inconnues légitimes des Arcanique de remplacement, runes clientes et autres inventaires incomplets ne sont pas résolues par DEC-178.

### Propagation et ambiguïtés, sans surcompter les erreurs

La paire maternelle est qualifiée à tort d’épique/violette dans **21 mentions**, fenêtres comprises, aux repères : 20227, 20247, 20271, 21409, 21420, 21468, 21482, 21555, 21623, 21715, 21735, 21811, 21932, 21994, 22008, 22063, 22141, 22233, 22265, 23256, 23592. Ce sont les reprises des **mêmes deux pierres**, pas 21 changements indépendants.

Six autres fenêtres portent des réserves « grade actuel À DÉFINIR » à examiner : **`060`, `062`, `068`, `069`, `078`, `087`**. Certaines raretés peuvent être déduites des exemplaires conservés, d’autres nécessitent encore une identité individuelle. Elles ne sont **pas comptées parmi les sept transformations directement erronées**. Les corriger toutes ajouterait douze SVG, mais il ne faut pas confondre clarification et changement de rareté faux.

## 2. Références actives à harmoniser

L’audit a identifié huit groupes résiduels dans **trois fichiers actifs** :

| Fichier | Reprises de l’ancienne règle |
|---|---|
| `lore/runes.md` | ORV-R001 au +3 ; ORV-R002 au +3 ; HAS-R004/005/008/010 devenant bleues à +6 ; HAS-R009/010 devenant violettes à +9 ; Fatal « épique à +9 » ; équipement final orange à +15 ; distinction des grades natifs du butin et des anciennes « évolutions de couleur » |
| `PLAN_DIRECTEUR.md` | Épreuve d’Orven au +3 (repère 362), équipement final (565/573), prompt de reprise réutilisable demandant grades natifs/distincts des affichés (722) |
| `AGENTS.md` | Bilan de fin du I conservant « grade affiché orange distinct du natif » ; la priorité DEC-178 en tête et le paragraphe général d’amélioration sont déjà corrigés |

Dans `lore/systeme.md`, deux formulations de coût selon « grade d’origine ou actuel » (repères 394/616 à la réception) nécessitent aussi de préciser leur sens : les deux ne divergent plus par une amélioration ordinaire. Une éventuelle question après Savoir runique doit être distinguée et ne fixe aucune nouvelle formule de coût.

### Provenance et historiques

Les anciens choix sont repris dans des notices datées : `docs/integration_chapitres_1_12.md`, `docs/integration_chapitres_13_16.md`, `source.md`, `lore/audit_fenetres_1_4.md`, `lore/audit_chapitres_5_9.md`, `lore/decisions.md` et la première fiche F01 dans `docs/integration_livre_2_chapitre_2.md`. Ils doivent rester lisibles comme historique, avec un renvoi vers DEC-178 si nécessaire, pas être réécrits comme si la règle avait toujours été correcte.

`docs/new.txt`, `docs/old.txt` et les quatre copies de révision sont des archives à conserver intactes. Leurs occurrences ne sont pas des corrections automatiques à appliquer au manuscrit.

## 3. Ce qui n’est pas en cause

- Le générateur SVG lit les classes et textes HTML : **il ne calcule pas la rareté depuis le niveau d’amélioration ou le nombre de secondaires**. Le CSS définit les palettes, pas une progression de rareté. Les modèles utilisent des champs fournis, sans imposer blanc→vert.
- `lecture.html` reprend les anciennes erreurs du I ; il devra être régénéré **après** correction autorisée de sa source, pas corrigé manuellement.
- Au II, la seconde expérience reste verte sans changement de grade ; les cadeaux paternels restent rares bleus +6 ; les huit Vol de vie restent rares bleus +6. Les autres fenêtres ne font pas changer une rune de rareté.
- Au I, la Fatal maternelle rare bleue +3 (`021`) est correcte, tout comme les cadeaux paternels +6, les commandes Gardien blanches qui restent blanches, et la rune d’Iseria **déjà légendaire orange** à +9.
- Classes de personnages, couleurs de portails, soins/contrôles, vêtements et compétences ne sont pas des grades de rune à remplacer.

## 4. État réel à la clôture de cet audit

- **F01 du II corrigée**, rareté commune blanche à +3, Vitesse +1 en gras conservée ; deux SVG synchronisés et contrôle visuel mobile local effectué.
- Règle prioritaire DEC-178 enregistrée ; `AGENTS.md` (en tête et règle générale), `lore/systeme.md` (en tête et paliers) et la fiche `L2-ORV-R001` dans `lore/runes.md` corrigés.
- **Livre I et ses images non modifiés par cet audit.** Les sept fenêtres ci-dessus et leurs mentions narratives restent à corriger dans une intervention ciblée ; raretés précises non attestées à ne pas inventer.
- **78 tests réussis** après le correctif F01. Ce résultat vérifie les protections techniques et le correctif ciblé ; les anciens tests du I protègent aussi l’état historique et ne constituent pas une preuve de conformité de tous ses grades à DEC-178.
- Aucun chapitre nouveau, commit, push ou publication.
