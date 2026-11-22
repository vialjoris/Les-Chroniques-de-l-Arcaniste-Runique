**Actualisation DEC-101/102 — quatre révisions validées et intégrées sans repères du lore en début/fin.** Comparaison : les quatre narrations étaient déjà celles de `roman.md` ; seules C3-F01/C4-F01 sont ajoutées, les 89 fenêtres modernisées préexistantes restent préservées. Copies de provenance conservées. Voir [`../docs/integration_chapitres_1_12.md`](../docs/integration_chapitres_1_12.md). Les mentions de propositions et de validation attendue ci-dessous décrivent la préparation historique, pas le statut actuel. Aucune illustration narrative ajoutée ; véritables fenêtres système conservées. La seconde passe graphique et le lecteur des douze chapitres sont contrôlés séparément.

# Audit des fenêtres — chapitres 1 à 4

## Actualisation du 22 novembre 2026 — DEC-091

**CANON — orientation de présentation :** la décision explicite de l’auteur dans `new.txt` (ligne 51618 au moment de la transmission) remplace la demande d’encadrés d’ouverture/clôture de DEC-072. Une partie lore consultable librement en fin de livre est désormais l’orientation retenue ; son contenu et son détail restent **À DÉFINIR**. Aucune annexe n’est rédigée ici.

**Effectué dans les propositions séparées :** suppression des huit blocs « REPÈRES DU LORE — OUVERTURE/CLÔTURE » et de leurs marqueurs C1-LO à C4-LC, deux par copie. Les quatre brouillons sont conservés, sans changement du texte hors blocs balisés ni des vraies fenêtres système, notamment C3-F01 et C4-F01. Décomptes des fenêtres avant → après : chapitre 1, 18 → 16 ; chapitre 2, 16 → 14 ; chapitre 3, 7 → 5 ; chapitre 4, 7 → 5. Repères : 8 → 0. Comparaison octet pour octet avec les copies avant suppression, une fois ces seuls blocs balisés retirés : réussie.

**Manuscrit, intervention distincte terminée par la session principale :** les dix repères des chapitres 5 à 9 sont également supprimés ; la comparaison au manuscrit antérieur confirme que seuls ces blocs ont été retirés. Le présent travail n’est pas un audit des chapitres 10 à 12.

**Historique conservé ci-dessous :** les anciens décomptes, contenus d’encadrés, contrôles et conseils de lecture décrivent la préparation du 21 novembre, non l’état actuel des copies. Ils ne rétablissent pas la demande remplacée par DEC-091. Les en-têtes de provenance des brouillons restent eux aussi historiques.

## Périmètre et provenance

- Audit préparé le **21 novembre 2026**, avant les copies de lecture, puis étendu le même jour sur demande explicite : « j’aimerais bien inclure des pop-up avec les règles du lore en début et fin de chapitre ». Le « go » autorise ces propositions séparées, pas leur validation ni leur remplacement dans le manuscrit.
- Source narrative fixe : `/tmp/opencode/arcaniste-integration-20261121/avant/roman.md`, SHA-256 `cd6580da3243670d7c98d4b1d4cdf91826ab5cc2a8fa3e2f1dc1a332507d581c`.
- Sources de contrôle lues intégralement : guide global `/home/dev/.config/opencode/AGENTS.md`, `AGENTS.md`, `PLAN_DIRECTEUR.md`, les quatre chapitres de cet instantané, `lore/systeme.md`, `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md`, `lore/decisions.md`, `source.md` et `style.css`.
- Aucune réimportation de `new.txt` ou d’`old.txt`. Les révisions locales DEC-026/027 priment sur les versions mobiles anciennes.
- Périmètre des propositions : **ajouts de fenêtres seulement**. Aucune phrase source supprimée ou remplacée, aucun raccord narratif nécessaire, aucune amélioration de prose, scène nouvelle ou réécriture de trame.
- Les copies sont des supports temporaires de lecture, pas des manuscrits concurrents. `roman.md` demeure l’unique manuscrit. Le chapitre 1 reste validé ; les statuts de lecture des chapitres 2 à 4 ne changent pas.

## Diagnostic et sélection

Le décompte porte sur les blocs HTML de premier niveau dont la première classe est `system-window`, `character-sheet` ou `rune-window` ; les en-têtes imbriqués ne sont pas comptés. Une fenêtre portant deux de ces classes n’est comptée qu’une fois.

| Chapitre | Fenêtres source | Ajouts dans les scènes | Repères lecteur ajoutés | Total de blocs | Copie de lecture |
|---|---:|---:|---:|---:|---|
| 1 — La légendaire inutile | 16 | 0 | 2 | 18 | `chap1_revision.md`, créée pour l’extension explicite. |
| 2 — La véritable valeur d’une rune | 14 | 0 | 2 | 16 | `chap2_revision.md`, créée pour l’extension explicite. |
| 3 — Le prix d’un rêve | 4 | 1 | 2 | 7 | `chap3_revision.md`, C3-F01 conservé. |
| 4 — La voie de l’artisan | 4 | 1 | 2 | 7 | `chap4_revision.md`, C4-F01 conservé. |

**Diagnostic initial conservé :** les chapitres 1 et 2 sont déjà riches en interfaces et ne nécessitent pas de notifications supplémentaires au milieu des scènes. L’extension explicite justifie désormais leurs deux nouvelles copies, uniquement pour les repères éditoriaux d’ouverture et de clôture. Ces repères ne sont pas des événements du système vécus par les personnages. La richesse de vie des scènes existantes n’est pas retravaillée dans ce périmètre.

## Extension — huit encadrés de repères pour le lecteur

**PROPOSITION de présentation, pas nouveau CANON.** Chaque chapitre possède exactement deux encadrés intitulés « REPÈRES DU LORE — OUVERTURE » et « REPÈRES DU LORE — CLÔTURE ». Leur sous-titre précise : « Pour le lecteur — repères éditoriaux, pas une notification reçue par les personnages. » Aucun personnage ne les ouvre, ne les partage ou n’en reçoit une connaissance nouvelle.

- **Ouverture :** après le titre du chapitre et son séparateur déjà présent, immédiatement avant la première section et toute première scène. Les ancrages locaux des nouvelles copies 1 et 2 sont présents avant le chapitre ; aucun ancrage source n’est supprimé ou déplacé par une insertion.
- **Clôture :** après le dernier paragraphe narratif, avant le séparateur et la mention de fin lorsqu’ils existent ; au chapitre 4, immédiatement après la dernière phrase, sans inventer de nouvelle mention de fin. Le dernier paragraphe en gras du chapitre 1 reste avant l’encadré.
- **Forme :** classes existantes `system-window` et `system-header`, listes HTML de trois à cinq puces courtes (quatre ici, sauf cinq pour C2-LC). Les trois bonus d’ensemble de C2-LC emploient `rune-bonus`. Aucun tableau de statistiques, aucune nouvelle règle ou valeur inventée.

| Repère | Contenu retenu | Justification temporelle et sources |
|---|---|---|
| C1-LO — ouverture | Révélation à seize ans ; quatre raretés de classe ; coûts 5/10/20/25 ; deux plafonds cinq membres et cinquante points. | Règles publiques de l’univers, expliquées en section I. Aucune annonce de la classe d’Hasol, de sa rareté personnelle, de ses futurs passifs ou des dix cercles. |
| C1-LC — clôture | Naturel distinct des bonus ; Mana ne donnant pas seul un sort offensif ; équipement runique sans niveau minimum avec place libre ; effet initial de Croissance par mille éliminations admissibles et rétroactivité. | Enseignements et déblocage déjà lus dans les sections III, VIII et XII. DEC-008/010/015/018/022 ; aucun nouveau cercle ni nouveau seuil accordé. Les conditions d’admissibilité restent celles de la fenêtre source, pas « mille monstres quelconques ». |
| C2-LO — ouverture | Cercle, emplacement et occupation distincts ; grade/étoiles/amélioration distincts ; bonus séparés du naturel ; équipement ne remplaçant pas la technique. | Informations accessibles après le chapitre 1, sans annoncer les huit nouveaux cadeaux ou leurs ensembles avant la scène. Les deux cadeaux rares (bleus), 6★, +6 sont déjà équipés en fin du chapitre 1, mais aucune nouvelle fiche redondante n’est ajoutée. |
| C2-LC — clôture | Fatal quatre pièces +35 % Attaque ; Gardien deux pièces +15 % Défense, deux paires +30 % ; Énergie deux pièces +15 % PV ; principale à chaque réussite et gain renforcé final ; rune rare native à deux secondaires encore à +3. | Règles déjà enseignées en sections III à V ; DEC-006/014/020. Pas d’ensemble Lame actif, pas d’Arcanique anticipé, pas de total complexe ni d’arrondi supplémentaire. |
| C3-LO — ouverture | Bénédiction sans garantie ; ressources consommées lors d’un échec possible ; ensemble selon pièces équipées ; comparaison des pertes lors d’un remplacement. | Chapitres 1 et 2 déjà lus ; aucun effet caché de Bénédiction ni taux chiffré d’Orven. Le contrôle d’un remplacement reste une application des ensembles et affixes connus, pas une prédiction de découverte. |
| C3-LC — clôture | Première secondaire et passage au vert d’une rune commune à +3, sans changement d’étoiles ; travail d’atelier distinct de l’équipement personnel ; suivi des tentatives et ressources ; nouvel accord avant tout dépassement. | Épreuve et consignes déjà lues en sections V et VI ; DEC-006/026. Les règles professionnelles sont explicitement contextualisées « à l’atelier » ; aucune notification automatique de contrat. |
| C4-LO — ouverture | Propriété des lots ; limites de commande ; principale/secondaires distinctes du nom d’ensemble ; nécessité des contrôles malgré le passif. | Consignes et connaissances établies au chapitre 3. Ne dévoile pas la découverte de l’endurance, la limite de fatigue ou la comparaison fixe/pourcentage avant leurs scènes. |
| C4-LC — clôture | Chaque tentative dépense pierres et Mana ; difficulté/coût liés notamment aux étoiles, grade et palier ; principale en pourcentage sur le naturel avant bonus fixes ; réserve distincte de l’attention et du repos mental. | Enseignements du chapitre 4, sections II, IV à VI ; DEC-024/027. Aucun coût chiffré, solde, récupération, ratio d’endurance ou ordre de calcul des ensembles. |

**Garde-fous des décisions récentes :** DEC-072 à DEC-080 relues pour cette extension. Les cycles élémentaires, Vague de Lumière de Yoon et son incantation de cinq secondes ne sont pas introduits avant sa rencontre au chapitre 5. Arcanique et les effets cachés/chiffres de Bénédiction ne sont pas révélés avant le chapitre 7. Lame n’est pas réintroduit comme ensemble actif. Aucun repère de butin n’est nécessaire : le plafond d’étoiles de DEC-077 n’est donc pas transformé en rang garanti, et aucune probabilité de grade ou d’étoiles ni Aimant n’est annoncé.

**Limite de fidélité signalée :** le texte source du chapitre 1 décrit historiquement le rang d’obtention comme déterminé par tranche ; DEC-077 précise désormais qu’il s’agit d’un plafond. Ce passage source est conservé mot pour mot sur instruction de préservation, sans réécriture silencieuse. Les nouveaux repères évitent de reproduire la formulation dépassée ; sa correction éventuelle dans le texte exige un arbitrage distinct de cet ajout d’encadrés.

## Ajout C3-F01 — État de départ de l’épreuve

- **Emplacement exact :** chapitre 3, section V « La première commande », après le paragraphe commençant par « Orven prit sur un plateau une Énergie commune » et finissant par « sans engager d’énergie. » ; ligne 4615 de l’instantané. Avant « — Jusqu’à +3 ? demanda-t-elle. »
- **Justification :** la consultation est déjà racontée ; sa visualisation donne un point de comparaison avec le grade vert final sans doubler toutes les réussites intermédiaires.
- **Contenu :** Énergie commune (blanche), 2★, +0 ; principale PV, sans valeur ; aucune secondaire. Aucun identifiant documentaire affiché au personnage.
- **Source :** paragraphe d’insertion, suivi ORV-R001 dans `lore/runes.md`, DEC-026. La rune reste un travail de l’atelier, pas un ajout à l’équipement personnel.
- **Limites :** ni valeur de PV, gain de principale, secondaire future prédite, propriétaire final, prix, coût ou solde de Mana inventé. Défense n’apparaît qu’au palier +3 déjà raconté.
- **Résultat :** 5 fenêtres dans les scènes, plus 2 encadrés lecteur, soit 7 blocs ; 7 sections conservées.

## Ajout C4-F01 — Fiche de commande, pas notification omnisciente

- **Emplacement exact :** chapitre 4, section II « Ce que la pierre exige », après « Une Gardien commune, blanche, deux étoiles, à +0, devait être rendue dans la matinée. Le propriétaire demandait +2 ; trois tentatives au maximum étaient prévues dans le budget. » ; ligne 4869 de l’instantané. Avant « Hasol suivit du doigt la limite inscrite. »
- **Justification :** matérialiser la limite écrite que la scène met ensuite à l’épreuve. L’en-tête « FICHE DE COMMANDE » désigne le document consulté, non une nouvelle capacité de suivi automatique du système.
- **Contenu :** Gardien commune (blanche), 2★, état initial +0 ; objectif +2 ; trois tentatives au maximum. Pas de réussite promise.
- **Source :** paragraphe d’insertion, suivi CLI-R001 dans `lore/runes.md`, DEC-027.
- **Limites :** principale non nommée : l’ensemble Gardien et le souhait du client ne prouvent pas son affixe. Ni budget monétaire, pierres disponibles, coût en Mana, échéance horaire précise ou statut d’équipement du client inventé.
- **Résultat :** 5 fenêtres dans les scènes, plus 2 encadrés lecteur, soit 7 blocs ; 10 sections conservées.

## Contrôles de continuité

- **CANON préservé :** Hasol niveau 8 en section VII du chapitre 1, passage au niveau 9 en VIII, puis au niveau 10 pendant la chasse nocturne. Aucun niveau de Ray ou Zio attribué rétroactivement.
- **CANON préservé :** au niveau 1, PV 2940, Attaque 199, Défense 182, Vitesse 100 ; Mana 30, Puissance arcanique 20. Caractéristiques naturelles séparées des bonus runiques. Aucun nouveau calcul ni fiche interpolée.
- **Équipement préservé :** deux cadeaux paternels rares (bleus), 6★, +6 inchangés ; dix cercles après Croissance. Au chapitre 2, huit cadeaux maternels 3★ complètent dix runes : quatre Fatal, quatre Gardien, deux Énergie. HAS-R003 seule Fatal maternelle rare (bleue), 3★, portée à +3 ; aucune confusion avec HAS-R001.
- **Statuts préservés :** la composition DEC-020 est CANON, les affixes individuels maternels gardent le statut de lecture de DEC-019. Les copies ne les valident pas par extension.
- **Épreuve et commande distinctes :** ORV-R001, Énergie commune (blanche), 2★, +0 → peu commune (verte), 2★, +3, avec un échec au passage +2 ; CLI-R001, Gardien commune (blanche), 2★, +0 → +2, en trois tentatives dont un échec initial. Aucune acquisition personnelle ni nouvelle tentative ajoutée.
- **Entraînement préservé :** troisième touche comme arrêt ; 42 secondes et une touche portée au chapitre 2, 78 secondes au chapitre 3. Pas de dégâts ou de PV épuisés déduits de ces résultats.
- **XP et éliminations :** 36 XP et trois éliminations supplémentaires au chapitre 2 seulement ; aucun total d’XP, seuil suivant ou reliquat historique fixé à zéro. Aucune nouvelle XP aux chapitres 3 et 4.
- **Mana :** 355 naturels au niveau 10, bonus connu +20, réserve réellement disponible non chiffrée. Aucun coût, taux de récupération ou effet de potion inventé. L’endurance ne devient pas une maîtrise ou un succès garanti.
- **Compétences et secrets :** Bénédiction et Croissance seules ; pas d’Aura, Œil, sort offensif ou avantage de 30 % prématuré. Les consultations insérées n’exposent que les données déjà accessibles dans leur scène. Yoon, ses cycles et Vague ne sont pas introduits dans les chapitres 1 à 4.
- **Vie et relations :** griffure, coffret paternel unique, premier salaire, fierté concrète, fatigue mentale et distance avec le père préservés ; aucune scène ajoutée ou retirée.

## Inconnues conservées et points non traités

**À DÉFINIR :** valeurs des affixes d’ORV-R001, principale exacte et valeurs de CLI-R001, prix et rémunérations, coûts en pierres/Mana, solde de réserve, reliquat historique, ordre de calcul et arrondis des ensembles. Aucun de ces points ne bloque les deux fenêtres volontairement limitées.

Les références contiennent des entrées historiques remplacées et des identifiants de décision réutilisés (notamment DEC-055 et DEC-060). La lecture suit leurs titres et les décisions explicites les plus récentes ; cet audit ne les corrige pas et n’en tire aucun fait nouveau pour les scènes. Aucune CONTRADICTION matérielle ne nécessite d’inventer une valeur pour les deux ajouts sélectionnés.

## Présentation et garantie de préservation

- Classes déjà définies dans `style.css` seulement : `rune-window`, `system-window`, `system-header`, `rune-bonus`, `upgrade-badge`. Principale PV en bleu comme affixe runique, niveaux +0/+2 en badges. Pas de bonus temporaire fictif ni d’assimilation du grade vert à un buff.
- Aucun script, ressource distante, dépendance ou modification de CSS. Le rendu stylé dépend du moteur Markdown et de son chargement du CSS ; aucune promesse de style sur GitHub.
- Chaque copie porte son statut, la date de préparation et le SHA-256 du segment source : du titre `# Chapitre N` jusqu’avant l’ancre du chapitre suivant ; pour le chapitre 4, jusqu’à la fin de l’instantané. Les séparateurs de fin présents dans ces segments sont conservés.
- **Garantie de périmètre :** aucune écriture dans `roman.md`, `new.txt`, `old.txt`, le plan, les règles ou le CSS. Les seuls fichiers créés ou modifiés par cette mission sont cet audit et `chap1_revision.md` à `chap4_revision.md`. Les changements d’autres sessions restent hors de cette intervention.
- **Contrôle de fidélité effectué avec succès sur les quatre copies :** retirer l’en-tête, les marqueurs et leurs lignes de séparation ajoutées, puis les deux blocs balisés Cn-LO/Cn-LC (et C3-F01 ou C4-F01) restitue exactement chaque segment source, octet pour octet en UTF-8. Les SHA-256 de référence sont : chapitre 1 `2ffa996edf5c5b77e42df35ef52c110f9ac77d7536f8f6cec5e0331c7f3cc4bf` ; chapitre 2 `8a4bfc2922c69ddfb90d1eb8a9f98d9fa3d8cc2defeb6f7d3beb6274487e23b8` ; chapitre 3 `71081458b50f19a365170012c7bd930aa09d996eb5f23774357367f0fc0a8026` ; chapitre 4 `8d49d9319831380f12964e2a516a1b9b88c48174abedc1193f32c6ca14aea0f6`. Aucun texte d’origine n’est réécrit, y compris les blancs de fin de segment.
- **Contrôles de l’extension exécutés avec succès :** exactement huit encadrés lecteur, un d’ouverture et un de clôture par copie ; trois à cinq puces chacun ; deux ou trois ajouts balisés par copie ; treize, dix, sept et dix sections conservées ; classes présentes dans `style.css`. Balises HTML équilibrées vérifiées avec le parseur standard de Python. Les chapitres 1 à 4 de `roman.md` demeurent identiques à l’instantané fixe. Aucun test de rendu visuel ni chargement automatique du CSS dans un aperçu Markdown n’est revendiqué.
- Aucun commit, push ou déploiement. Impacts sécurité/performance/exploitation : documents statiques locaux uniquement ; le principal risque est éditorial (prendre une proposition pour le canon), explicitement couvert par les en-têtes et l’absence de remplacement.

## Ordre de lecture conseillé

1. **Ce fichier**, pour la portée, les limites et les huit repères.
2. `chap1_revision.md` puis `chap2_revision.md`, deux encadrés lecteur chacun et aucune notification de scène supplémentaire.
3. `chap3_revision.md`, deux repères et C3-F01 en section V.
4. `chap4_revision.md`, deux repères et C4-F01 en section II.

Après lecture seulement, l’auteur peut retenir, refuser ou déplacer chaque fenêtre. Aucune intégration au manuscrit n’est effectuée par cette préparation.
