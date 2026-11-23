# Décisions éditoriales

**Localisation actuelle des sources :** l’auteur a déplacé `new.txt`, `old.txt` et `chap1_revision.md` à `chap4_revision.md` de la racine vers `docs/`, sans changement de contenu. Accès : [`../docs/new.txt`](../docs/new.txt), [`../docs/old.txt`](../docs/old.txt), [`révision 1`](../docs/chap1_revision.md), [`révision 2`](../docs/chap2_revision.md), [`révision 3`](../docs/chap3_revision.md), [`révision 4`](../docs/chap4_revision.md). Les chemins et noms courts des décisions ci-dessous restent les traces historiques de leurs interventions ; ce rangement n’ajoute aucune décision éditoriale et ne modifie notamment pas DEC-109.

**Lecture du registre :** les décisions les plus récentes priment dans leur périmètre. Les formulations anciennes sont conservées comme historique ; les actualisations DEC-072 à DEC-080 du 21 novembre 2026 ne valident pas toutes les réponses de ChatGPT de `new.txt`. Les doublons historiques **DEC-055** (Yoon/Zio) et **DEC-060** (Ray/Samia) sont conservés sans renumérotation pour ne pas casser les références ; préciser le personnage ou le titre lorsqu'un renvoi serait ambigu.

## DEC-001 — Secondaires des cadeaux du père

- **Statut : CANON.**
- **Validation :** 19 novembre 2026, réponse explicite de l’auteur « oui je valide » au tableau des quatre secondaires.
- **Décision :** Fatal bleue +0 : principale Attaque +6, secondaires Vitesse +2 et PV +15 ; Gardien bleue +0 : principale Défense +5, secondaires PV +20 et Mana +10.
- **Justification :** corriger l’absence de secondaires des deux runes bleues conformément à la règle validée de deux secondaires dès +0, avec les valeurs approuvées par l’auteur.
- **Application :** fenêtres d’identification, fiches des niveaux 1, 9 et 10 et récapitulatifs d’équipement du chapitre 1. Bonus secondaires cumulés : PV +35, Vitesse +2, Mana +10. Aucun changement des caractéristiques naturelles, scènes ou gains de niveau.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md`, `lore/runes.md`, `lore/decisions.md`.
- **Questions en attente sur ces quatre valeurs :** aucune.

## DEC-002 — Composition runique du chapitre 2

- **Statut : RÉSOLUE par DEC-013 puis DEC-020.** Dix runes finales, cadeaux paternels conservés et huit ajouts maternels validés ; répartition désormais fixée à quatre Fatal, quatre Gardien et deux Énergie. Les questions et propositions ci-dessous sont historiques, ne pas les rouvrir comme si DEC-020 n’existait pas.
- **Source :** l’auteur indique « 4 Fatal, 2 Gardien, 2 Énergie » et délègue le choix des statistiques du chapitre 2.
- **Question :** s’agit-il des huit nouvelles runes du don maternel, en plus des deux cadeaux paternels, ou du total équipé ?
- **Justification de l’attente :** ne pas choisir silencieusement entre dix runes finales (5 Fatal, 3 Gardien, 2 Énergie) et huit runes finales (4 Fatal, 2 Gardien, 2 Énergie).
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `AGENTS.md`, `lore/runes.md` et futur chapitre 2 de `roman.md`.

## DEC-003 — Secondaires sans pourcentages

- **Statut : REMPLACÉE par DEC-004.** Conserver cette entrée comme historique, pas comme règle actuelle.
- **Validation initiale :** 19 novembre 2026, instruction de l’auteur « on evite les sub stats % ».
- **Décision :** utiliser des caractéristiques secondaires runiques en valeurs fixes, sans pourcentages.
- **Justification :** préférence explicite de l’auteur pour les secondaires sans pourcentages.
- **Portée :** ne modifie ni les principales ni les bonus d’ensemble en pourcentage. Les quatre secondaires de DEC-001 sont déjà conformes.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/runes.md`, `lore/decisions.md` et futures descriptions runiques dans `roman.md`.
- **Suite :** l’auteur rétablit ensuite les pourcentages pour le critique, la précision et la résistance ; voir DEC-004.

## DEC-004 — Pourcentages spécialisés et rangs de 1 à 6 étoiles

- **Statut : CANON pour les étoiles et Précision/Résistance ; HISTORIQUE pour les affixes CC/DCC, retirés par DEC-098 le 22 novembre 2026.** Les formulations d’adoption ci-dessous consignent la décision initiale, pas le catalogue actif de ces deux affixes.
- **Validation :** 19 novembre 2026, l’auteur demande de garder les pourcentages pour le taux critique, les dégâts critiques, la précision et la résistance, cite les quatre lignes de progression et demande l’ajout de rangs de 1 à 6 étoiles.
- **Décision :** ces quatre caractéristiques peuvent être exprimées en pourcentages, y compris en secondaires. Chaque rune possède un rang de 1 à 6 étoiles, indépendant du grade de couleur et de l’amélioration.
- **Justification :** dernière décision explicite de l’auteur, fondée sur l’inspiration Summoners War.
- **Tables :** les quatre lignes citées concernent les principales ; elles sont conservées dans `lore/systeme.md`. Elles ne définissent pas les valeurs ou gains des secondaires.
- **Remplace :** l’interdiction générale de DEC-003. Ne change pas les quatre secondaires validées par DEC-001.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `source.md`, `lore/systeme.md`, `lore/runes.md`, `lore/decisions.md`.
- **Questions en attente :** rang des deux cadeaux du chapitre 1 ; tables des autres principales ; valeurs et gains des secondaires ; adoption éventuelle de PV %, Attaque % et Défense %. Ne pas importer les autres règles du jeu par défaut.

## DEC-005 — Cadeaux paternels : deux runes bleues 6★ déjà +6

- **Statut : CANON pour le rang 6★, le grade bleu et l’amélioration +6 ; nombre de secondaires rectifié par DEC-006.** Les mentions de quatre secondaires ci-dessous sont historiques et ne doivent plus être appliquées.
- **Validation :** 19 novembre 2026, instructions successives de l’auteur : « le pere offre deux rune 6 etoile bleu », « +6 les deux runes », puis « donc avec deux substat natif et deux autre obtenue par evolution ».
- **Décision :** HAS-R001 et HAS-R002 sont offertes bleues, de rang 6★, déjà améliorées à +6. Chacune possède deux secondaires natives et deux secondaires supplémentaires acquises par amélioration, soit quatre secondaires au moment du don.
- **Priorité :** remplace leur ancien état +0 et l’absence de rang. Le maintien sans nouvelle amélioration pendant les trois années d’Académie reste prévu, désormais à +6.
- **Secondaires natives conservées :** Fatal : Vitesse +2 et PV +15 ; Gardien : PV +20 et Mana +10. Les deux nouvelles secondaires par rune et leurs valeurs restent à définir.
- **Principales :** les anciennes valeurs Attaque +6 et Défense +5 ne constituent pas une table validée pour des runes 6★ +6. Leurs nouvelles valeurs attendent arbitrage ; ne pas les recalculer automatiquement depuis une table externe non adoptée.
- **Divergence assumée :** le guide externe prévoit le renforcement de secondaires existantes aux premiers paliers pour une rune bleue, pas automatiquement deux ajouts à +6. La décision de l’auteur prévaut pour ces deux runes ; ne pas en déduire toute la progression des autres grades.
- **Questions en attente :** paliers exacts d’acquisition des deux secondaires ; valeurs finales des principales et des secondaires supplémentaires ; effet sur l’équilibre des premières scènes de combat ; adaptation de la Fatal à améliorer au chapitre 2, puisque le cadeau paternel est déjà +6.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/runes.md`, `lore/systeme.md`, `source.md`, `roman.md`. Le manuscrit doit être synchronisé après définition des valeurs, sans inventer de statistiques ni remplacer les scènes.

## DEC-006 — Respect de la progression des secondaires de la source

- **Statut : CANON pour la règle ; valeurs secondaires choisies par délégation éditoriale.**
- **Validation :** 19 novembre 2026, après avoir délégué le choix des statistiques à partir de la source, l’auteur rectifie : « pardon respecte la regle de la source ».
- **Décision :** pour une rune bleue native, +3 et +6 renforcent chacun une secondaire existante. La rune conserve deux secondaires à +6, gagne la troisième à +9 puis la quatrième à +12. Remplace la partie de DEC-005 qui prévoyait quatre secondaires à +6.
- **Règle générale adoptée :** à +3, ajouter si aucune secondaire n’est présente, sinon renforcer ; à +6, ajouter si une seule est présente, sinon renforcer ; à +9, ajouter si seulement deux sont présentes, sinon renforcer ; à +12, ajouter si seulement trois sont présentes, sinon renforcer. Le grade affiché évolue avec les ajouts. Le rang en étoiles ne change pas. **Complément ultérieur DEC-014 :** à +15, gain renforcé de principale et renforcement d’une des quatre secondaires, sans cinquième secondaire.
- **Principales des deux cadeaux :** Attaque +70 et Défense +70 à 6★ +6, calculées selon le tableau de la source : 22 à +0, gain de 8 par niveau jusqu’à +6.
- **Choix délégués des renforcements :** Fatal, Vitesse +2 → +4 à +3, puis PV +15 → +25 à +6 ; Gardien, PV +20 → +30 à +3, puis Mana +10 → +20 à +6. Le guide ne fournit pas de barème numérique des secondaires ; ces gains sont des choix pour le roman, pas des chiffres attribués à la source.
- **Retrait :** les ajouts intermédiaires de taux critique, précision, vitesse et résistance comme troisième et quatrième secondaires à +6 ne sont pas conservés.
- **Adaptation maintenue :** Mana en secondaire provient du canon propre au roman (DEC-001), pas du système de Summoners War. La correction porte sur la règle d’évolution, pas sur la suppression des caractéristiques originales du roman.
- **Fichiers concernés :** `roman.md`, `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/runes.md`, `lore/systeme.md`, `source.md`, `lore/decisions.md`.
- **Vigilance :** les bonus +70 modifient fortement l’échelle des débuts. Les scènes de combat restent préservées ; leur équilibre et la scène d’amélioration jusqu’à +3 au chapitre 2 devront être revus avec l’auteur, sans réécriture silencieuse.

## DEC-007 — Rang du butin et désignation des runes

- **Statut : CANON.**
- **Précision prioritaire du 21 novembre 2026 — DEC-077 :** les tranches ci-dessous fixent un **plafond d'étoiles**, pas un rang garanti ; un monstre niveau 30 peut donner une rune 1★, 2★ ou 3★. L'ancien libellé déterministe est historique. Voir les distributions conditionnelles spécifiques au seul niveau 30 dans DEC-077.
- **Validation :** 19 novembre 2026, l’auteur précise la règle propre au roman « rune 1 etoile obtenue sur monstre 1-10 2 etoile 11-20 etc » et demande de toujours indiquer rareté et étoiles.
- **Décision :** niveaux de monstre 1–10 → 1★, 11–20 → 2★, 21–30 → 3★, 31–40 → 4★, 41–50 → 5★, 51–60 → 6★. Le grade et la probabilité d’obtention ne sont pas définis par cette correspondance.
- **Présentation :** toute rune identifiable doit être désignée avec sa rareté et son rang en étoiles, une fois identifiée. Conserver une formulation générique pour les explications abstraites et ne pas inventer les informations inconnues.
- **Justification :** décision explicite de l’auteur, distincte des règles externes.
- **Conséquence :** la rune Vitesse rare (bleue) prévue comme butin sur l’alpha élite de niveau 25–27 est 3★. Les deux cadeaux paternels restent rares (bleus), 6★, +6, sans attribuer une provenance de chasse au père.
- **Questions en attente :** monstres au-delà du niveau 60 ; taux de butin ; rang des autres runes futures non documentées.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/runes.md`, `roman.md`, `source.md` et présent registre.

## DEC-008 — Runes équipables à tout niveau

- **Statut : CANON.**
- **Validation :** 19 novembre 2026, instruction de l’auteur « les rune sont équipable a tous niveau ».
- **Décision :** aucune condition de niveau du personnage pour équiper une rune, quels que soient rareté, étoiles et amélioration. Un emplacement disponible reste nécessaire.
- **Justification :** distinguer explicitement niveau des monstres pour l’obtention et niveau du porteur pour l’équipement.
- **Conséquence :** Hasol peut équiper les deux cadeaux rares (bleus), 6★, +6 au niveau 1. Les tranches de DEC-007 ne sont pas des prérequis d’équipement.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/runes.md`, `source.md` et présent registre. Aucune nouvelle scène n’est nécessaire dans `roman.md`, qui montre déjà cet équipement au niveau 1.
- **Questions en attente sur le niveau minimum :** aucune.

## DEC-009 — Classes et étoiles natives des personnages

- **Statut : CANON pour la correspondance ; rééchelonnement numérique À DÉFINIR.**
- **Validation :** 19 novembre 2026, l’auteur demande une recherche sur les statistiques d’un 4★ au niveau 1 et définit Légendaire ≈ 4★ natif, Astrale ≈ 5★ natif, Rare ≈ 3★ natif, Commune ≈ 2★ natif.
- **Décision :** utiliser cette correspondance comme référence de conception des personnages. Ne pas la confondre avec les étoiles des runes.
- **Justification :** nouvelle orientation explicite de l’auteur pour l’échelle des personnages.
- **Recherche :** exemples vérifiés dans les tableaux « Evolution Stats », rang 4★, colonne « Min », état non éveillé, des fiches Joker Vent, Rakshasa Feu et Danseur du ciel Vent. Résultats et liens dans `source.md`.
- **Limites :** aucune fiche unique par rareté ; pas de formule adoptée de conversion vers Mana ou Puissance arcanique ; pas d’import automatique d’éveil ou de plafonds de niveaux.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `source.md`, `lore/decisions.md`. Aucun changement numérique dans `roman.md` à ce stade.
- **Questions en attente :** échelle exacte de Hasol, adaptation de sa spécialisation magique et recalcul éventuel des niveaux 1, 9 et 10 et des gains intermédiaires.

## DEC-010 — Correction de la base statistique de Hasol au chapitre 1

- **Statut : CORRECTION APPLIQUÉE sur autorisation de l’auteur ; profil de référence sélectionné par l’assistant.**
- **Autorisation :** 19 novembre 2026, l’auteur demande « corrige chapitre 1 avec les bonne stats » après la recherche sur les 4★ natifs.
- **Choix de référence :** Danseur du ciel Vent non éveillé, rang 4★, niveau 1 : PV 2940, Attaque 199, Défense 182, Vitesse 100. Profil de soutien retenu plutôt qu’un attaquant pur ; ce choix n’est pas une statistique universelle de tous les légendaires.
- **Méthode :** remplacer la base des quatre caractéristiques puis conserver tous les gains déjà racontés. Par rapport à l’ancienne fiche, décalages constants : PV +2840, Attaque +189, Défense +172, Vitesse +90.
- **Fiche naturelle niveau 9 :** PV 3045, Attaque 211, Défense 191, Vitesse 113, Mana 310, Puissance arcanique 186.
- **Fiche naturelle niveau 10 :** PV 3058, Attaque 213, Défense 192, Vitesse 115, Mana 355, Puissance arcanique 211.
- **Conservé :** gains 1 → 2, 8 → 9, 9 → 10 ; Mana et Puissance arcanique ; bonus et identité des deux runes rares (bleues), 6★, +6 ; événements et relations.
- **Narration :** seuls les totaux chiffrés du premier équipement changent : Attaque 269 et Défense 252. Aucune réécriture des scènes.
- **Source :** fiche Wiki du Danseur du ciel Vent / Chasun, tableau « Evolution Stats », 4★, colonne « Min », ligne « Normal », et vitesse non éveillée ; lien et relevé dans `source.md`.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md`, `lore/personnages.md`, `lore/runes.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`.
- **Points encore ouverts :** l’échelle de Mana et Puissance arcanique n’est pas transposée depuis Summoners War ; la prépondérance magique décrite dépend d’un contexte et de règles non entièrement chiffrés. La croissance physique après rééchelonnement reste celle du roman, pas celle du jeu. Ces éléments devront être arbitrés avant de prétendre à un équilibrage complet.

## DEC-011 — Enseignement d’Orven sur les principales fixes et en pourcentage

- **Statut : CANON pour l’enseignement et la direction d’équilibrage ; placement résolu par DEC-023 au chapitre 4, assiette complétée par DEC-024.** Les formulations futures ci-dessous décrivent la décision initiale ; seuils réels et tables restent À DÉFINIR.
- **Validation :** 19 novembre 2026, l’auteur demande qu’Orven explique dans l’histoire l’avantage des principales fixes à bas niveau, puis celui des pourcentages avec la progression.
- **Décision :** prévoir cet enseignement dans une scène future avec Orven. Les principales PV %, Attaque % et Défense % sont admises ; aucune validation supplémentaire des secondaires en pourcentage n’en découle.
- **Justification :** décision narrative explicite de l’auteur et intérêt d’une évolution des choix d’équipement avec les caractéristiques naturelles.
- **Limites :** comparaison à rang en étoiles et amélioration comparables ; avantage dépendant des valeurs et de la caractéristique concernée, pas d’un niveau unique. Les secondaires et ensembles comptent toujours dans le choix d’une rune complète.
- **Vigilance :** la bascule rapide souhaitée devra être compatible avec les gains naturels du roman. Aucun seuil, ordre de calcul, arrondi ou formule de progression n’est inventé par cette décision.
- **Préservation :** pas de changement des deux runes rares (bleues), 6★, +6 du père ni de réécriture du chapitre 1. L’enseignement n’a pas encore eu lieu dans le manuscrit.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `AGENTS.md`, `lore/chronologie.md`, `lore/decisions.md` et futur passage concerné dans `roman.md`.
- **Questions en attente :** chapitre et scène ; exemples chiffrés ; tables des principales en pourcentage et point de bascule réel selon le profil.
- **Actualisation du 20 novembre 2026 — DEC-023 et DEC-024 :** scène désormais racontée au chapitre 4, sections IV et VII ; exemples +50 Attaque / +10 % et calcul du pourcentage sur la caractéristique naturelle. Le placement et ces exemples ne sont plus ouverts, sans résoudre les tables ou les calculs des ensembles et arrondis.

## DEC-012 — Explication des points de classe au chapitre 1

- **Statut : CANON, rappel d’une règle déjà validée.**
- **Demande :** 19 novembre 2026, l’auteur signale l’absence d’explication des points de classe et des limites d’équipe dans le chapitre 1.
- **Correction :** ajout ciblé dans l’introduction, après la présentation des raretés : Commune 5 points, Rare 10, Légendaire 20, Astrale 25 ; cinq membres et cinquante points maximum, deux plafonds simultanés.
- **Exemple :** deux légendaires et un rare représentent trois personnes et cinquante points ; les deux places restantes ne permettent pas de dépasser le plafond de points.
- **Justification :** rendre une règle fondamentale compréhensible dans le roman, sans exiger la lecture du plan ni attendre la formation de l’équipe de Hasol.
- **Préservation :** aucun changement de statistiques, d’événements, de composition d’équipe ou de révélation future. Aucun passage existant supprimé.
- **Fichiers concernés :** `roman.md`, `lore/decisions.md`, `lore/chronologie.md`.
- **Questions en attente :** aucune sur ces plafonds.

## DEC-013 — Huit runes maternelles 3★ et conservation des cadeaux paternels

- **Statut : CANON pour les contraintes du don ; répartition complétée par DEC-020.** L’ancienne proposition cinq Fatal, trois Gardien et deux Énergie ci-dessous est abandonnée ; la répartition active est quatre Fatal, quatre Gardien et deux Énergie. Les anciennes questions sur les nombres par ensemble sont résolues.
- **Validation :** 19 novembre 2026, l’auteur précise que Hasol garde les deux cadeaux de son père, ajoute huit runes 3★ entre vert et bleu, et doit avoir dix runes au total avec des ensembles Fatal et Gardien complets.
- **Cadeaux conservés :** HAS-R001, Fatal rare (bleue), 6★, +6 ; HAS-R002, Gardien rare (bleue), 6★, +6. Ne pas les remplacer ni les compter parmi les huit nouvelles acquisitions.
- **Don maternel :** huit runes supplémentaires 3★, de grades peu commun (vert) et rare (bleu). Le choix individuel des caractéristiques est délégué à l’assistant ; ne pas y inclure de rune commune blanche.
- **Équipement final :** dix runes équipées sur dix emplacements. Ensembles concernés par la liste de l’auteur : Fatal, Gardien et Énergie. Fatal complet exige quatre pièces, Gardien complet deux pièces ; ne pas réintroduire les Lame de l’archive.
- **Répartition exacte : À DÉFINIR.** L’auteur clarifie les types et le total sans arrêter une nouvelle distribution numérique explicite des dix pièces.
- **PROPOSITION de travail :** don de quatre Fatal, deux Gardien et deux Énergie, toutes 3★ peu communes (vertes) ou rares (bleues), donnant cinq Fatal, trois Gardien et deux Énergie en comptant les cadeaux paternels rares (bleus), 6★, +6. Les pièces Fatal et Gardien excédentaires ne complètent pas un deuxième ensemble. Ne pas présenter cette proposition comme validée.
- **Conséquences :** ancienne composition avec deux Lame et quatre bonus d’ensemble non applicable automatiquement ; recalculer les fenêtres du chapitre 2 après fixation de l’inventaire. La Fatal rare (bleue) à améliorer jusqu’à +3 doit être une des nouvelles runes 3★, pas le cadeau paternel déjà +6.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/runes.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md` et future restauration du chapitre 2 de `roman.md`. `old.txt` reste intact.
- **Questions en attente :** répartition numérique finale, répartition des grades vert/bleu et niveaux d’amélioration initiaux des huit nouvelles runes.

## DEC-014 — Principale à chaque amélioration et palier secondaire à +15

- **Statut : CANON.**
- **Validation :** 19 novembre 2026, l’auteur précise que la principale évolue à chaque amélioration, davantage à +15, et qu’une secondaire est ajoutée ou évolue à +3, +6, +9, +12 et +15.
- **Confirmation explicite :** l’auteur répond ensuite « je valide » à la formalisation de cette règle. Cette confirmation concerne DEC-014 et ne tranche pas les propositions de répartition du don maternel.
- **Décision :** la principale augmente à tous les niveaux réussis de +1 à +15 ; son gain final à +15 est renforcé. Les cinq paliers multiples de trois produisent aussi un ajout ou renforcement de secondaire, dans la limite de quatre secondaires.
- **Application :** conserver les conditions d’ajout de DEC-006 jusqu’à +12. À +15, une rune ayant suivi ces paliers a déjà quatre secondaires : renforcer l’une d’elles sans en ajouter une cinquième, en plus de l’augmentation renforcée de principale.
- **Justification :** dernière clarification explicite de l’auteur ; corrige la présentation précédente qui réservait l’effet de +15 à la principale seule.
- **Source :** l’augmentation de la principale à chaque niveau et son gain renforcé à +15 figurent dans le guide. L’effet supplémentaire sur une secondaire à +15 est une adaptation propre au roman, non attribuée au guide.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `source.md`, `lore/decisions.md`. Les deux cadeaux rares (bleus), 6★, +6 du chapitre 1 ne changent pas de valeurs.
- **Questions en attente :** ampleur chiffrée des gains secondaires aux futurs paliers et choix de la secondaire renforcée pour chaque rune concernée ; ne pas inventer de barème universel.

## DEC-015 — Normes magiques au niveau 60 et anomalie de Hasol

- **Statut : CANON pour les repères et le profil ; courbes chiffrées À DÉFINIR.**
- **Validation :** 19 novembre 2026, l’auteur fixe une norme de 1000 Mana au niveau 60, 600 de Puissance arcanique pour un soutien et 2000 pour un mage au même niveau ; il précise qu’Hasol dépassera largement la norme de Mana et possède des statistiques de mage malgré sa classe de soutien.
- **Décision :** utiliser ces nombres comme normes de comparaison, pas comme plafonds absolus ou résultats d’une formule linéaire. Hasol suit un profil de mage en Puissance arcanique et un profil hors norme en Mana.
- **Justification :** clarifier le contraste central entre sa classe de soutien, ses caractéristiques magiques élevées et son absence initiale de compétence offensive.
- **Portée :** ces repères sont propres au roman, pas tirés de Summoners War. Ils ne donnent pas les valeurs de tous les soutiens et mages ni le niveau exact où Hasol franchit 1000 Mana.
- **Préservation :** les fiches et gains déjà écrits ne sont pas recalculés à partir des seules normes ; la classe et les conditions de déblocage des compétences restent inchangées.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/personnages.md`, `source.md`, `lore/decisions.md` et futurs contrôles des fenêtres dans `roman.md`.
- **Questions en attente :** courbes de progression, gains futurs, niveau de franchissement de 1000 Mana et comparaison avec les caractéristiques physiques. La référence naturelle d'Hasol au niveau 60 est désormais fixée par DEC-054, sans déterminer les valeurs intermédiaires.

## DEC-016 — Reprise narrative du chapitre 1 avec le poids de groupe

- **Statut : CANON — version narrative validée par l’auteur dans DEC-018, après correction DEC-017.**
- **Autorisation :** 19 novembre 2026, après vérification de la notion de poids de groupe dans `old.txt`, l’auteur demande « donc maintenant refait le chapitre 1 ».
- **Méthode :** reprendre le chapitre 1 du manuscrit actuel, conserver ses scènes familiales et ses étapes, adapter le motif du refus de recrutement de l’archive avec les règles et statistiques récentes. Ne pas remplacer le texte par l’ancien chapitre non synchronisé.
- **Ajout principal :** section « Le poids d’une légendaire », Hasol niveau 3 ; groupe de deux classes rares et deux communes, quatre personnes pour trente points. Hasol pourrait devenir la cinquième personne et porter l’équipe à cinquante points. Le refus porte sur l’utilité immédiate de sa compétence et le poids de vingt points, pas sur un dépassement des plafonds.
- **Progression émotionnelle :** refus répétés, difficulté à justifier sa place, solitude accrue ; préparer le sens de l’acceptation future de Yoon sans la faire apparaître dans le chapitre 1.
- **Autres intégrations :** professeur expliquant les normes magiques au niveau 60 et le profil de mage d’Hasol malgré sa classe de soutien ; précision du rang 6★ des cadeaux et de leur équipement dès le niveau 1 ; orientation Soutien dans les fenêtres ; écho du poids de groupe lors du déblocage final.
- **Préservé :** statistiques naturelles et bonus actuels, les deux runes rares (bleues), 6★, +6, père vivant et relation non réconciliée, Zio, expulsion, plus de huit mille slimes, huit paliers rétroactifs, deux à dix cercles et emplacements, absence de compétence offensive.
- **Structure :** treize sections internes numérotées I à XIII ; un seul chapitre dans `roman.md` ; aucun chapitre 2 ajouté. `old.txt` inchangé.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`, `source.md`.
- **Questions préservées ouvertes :** compte exact et reliquat d’éliminations, courbes futures, don maternel détaillé. La révision ne tranche pas ces points.

## DEC-017 — Ordre chronologique des niveaux 8 et 9

- **Statut : CORRECTION APPLIQUÉE sur signalement de l’auteur.**
- **Demande :** 19 novembre 2026, l’auteur relève que la section VII annonce déjà le niveau 9 alors que la section VIII raconte son acquisition, et indique que Hasol devrait être niveau 8 en VII.
- **Correction :** niveau 8 dans la section VII et dans la réplique des harceleurs ; section VIII ouverte au niveau 8, puis passage au niveau 9 raconté au passé simple, sans retour en arrière ambigu. La montée n’est plus annoncée comme déjà survenue.
- **Transition temporelle :** le résumé des milliers d’éliminations en VII n’annonce plus prématurément la fin de l’année avant la scène de montée en VIII. Le total de plus de huit mille slimes avant l’expulsion est conservé ailleurs dans le chapitre.
- **Préservation :** gains 8 → 9, fiches des niveaux 9 et 10, runes rares (bleues), 6★, +6 et événements familiaux inchangés.
- **Fichiers concernés :** `roman.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`.
- **Questions en attente :** aucune sur cet ordre ; les seuils d’XP exacts restent non définis.

## DEC-018 — Validation du chapitre 1

- **Statut : VALIDÉ — CANON.**
- **Validation :** 19 novembre 2026, déclaration explicite de l’auteur : « ok , je valide le chapitre 1 ».
- **Périmètre :** version actuelle du chapitre 1 dans `roman.md`, « La légendaire inutile », treize sections I à XIII, après la reprise DEC-016 et la correction chronologique DEC-017.
- **Éléments validés :** scènes familiales, Révélation, cadeaux rares (bleus), 6★, +6, fiches actuelles, absence de compétence offensive, poids de classe et refus de recrutement, normes magiques, intervention de Zio, expulsion, dîner, chasse nocturne, Croissance runique et passage de deux à dix cercles et emplacements.
- **Ordre des niveaux confirmé :** niveau 8 en section VII, passage 8 → 9 en VIII, niveau 9 à l’expulsion, passage 9 → 10 durant la chasse nocturne.
- **Conséquence :** le chapitre devient la référence narrative validée. Toute modification rétroactive, même statistique ou destinée à adapter `old.txt`, nécessite une nouvelle autorisation explicite.
- **Limites :** ne valide pas les propositions encore ouvertes pour les chapitres suivants, notamment la répartition détaillée du don maternel, les calculs de pourcentage et les paramètres de Résonance runique. Le reliquat exact des éliminations reste inconnu ; ne pas le déduire arbitrairement du total approximatif raconté.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md`, `lore/decisions.md`, `source.md`. Aucun changement du texte de `roman.md` lors de l’enregistrement de cette validation.
- **Chapitre suivant :** chapitre 2 non intégré et non autorisé par cette seule validation.

## DEC-019 — Adaptation autorisée du chapitre 2 depuis l’archive

- **Statut : VERSION DE LECTURE, non encore validée dans son ensemble.**
- **Autorisation :** 19 novembre 2026, l’auteur demande de réfléchir aux changements du chapitre 2 et de les appliquer.
- **Application :** chapitre 2 ajouté à la suite du chapitre 1 validé, sans modifier ce dernier ; `old.txt` intact. Retour nocturne, échange avec la mère, huit cadeaux, pédagogie des grades/étoiles/améliorations, première Fatal rare (bleue), 3★, +3, mannequin, trois loups de niveau 5, 36 XP, griffure, potion et retour familial conservés ou adaptés.
- **Choix de lecture délégués :** quatre nouvelles runes rares bleues et quatre peu communes vertes ; sept à +0 et une à +3 en fin de chapitre. Caractéristiques dans `runes.md` ; la répartition des ensembles est corrigée par DEC-020.
- **Garde-fous :** aucune modification des caractéristiques naturelles de niveau 10 ; bonus fixes et pourcentages d’ensemble affichés séparément ; aucun reliquat arbitraire de Croissance runique ; +3 éliminations admissibles seulement, sans nouveau cercle ni montée de niveau.
- **Entraînement :** défaite en 42 secondes, une touche portée et trois reçues ; exercice arrêté après trois touches, et non épuisement supposé de plusieurs milliers de PV.
- **Amélioration montrée :** HAS-R003, Fatal rare (bleue), 3★ : échec +0 → +1 sans changement de niveau, puis réussites +1, +2 et +3. Principale Attaque +7 → +22 selon le tableau 3★ (gain +5/niveau) ; secondaire Vitesse +2 → +4 à +3, gain choisi pour le roman. L’échec précoce conserve la divergence déjà prévue avec la source.
- **Fichiers concernés :** `roman.md`, `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `source.md`.
- **Statut de la lecture :** l’autorisation d’adapter n’est pas une validation de tous les nouveaux dialogues ou chiffres. Aucun chapitre 3 ajouté.

## DEC-020 — Quatre Fatal, quatre Gardien, deux Énergie

- **Statut : CANON pour la composition et les ensembles ; texte du chapitre 2 à relire.**
- **Validation :** 19 novembre 2026, correction explicite de l’auteur : « 5 Fatal, 3 Gardien et 2 Énergie non 4 fatal 4 gardien 2 energie », puis rappel des ensembles complets.
- **Décision :** dix runes finales : quatre Fatal, quatre Gardien, deux Énergie. Avec les deux cadeaux paternels rares (bleus), 6★, +6, le don maternel comprend donc trois Fatal, trois Gardien et deux Énergie, toutes 3★ peu communes (vertes) ou rares (bleues).
- **Ensembles :** Fatal par quatre ; Gardien et Énergie par deux. Un Fatal, deux Gardien, un Énergie : Attaque +35 %, Défense +15 % +15 % = +30 %, PV +15 %. Les cumuls Gardien sont additifs, pas multiplicatifs.
- **Correction :** HAS-R006, rune rare (bleue), 3★, +0 à principale PV +100, appartient à Gardien et non Fatal dans la version de lecture. Les valeurs fixes ne changent pas ; seuls la répartition des ensembles et le bonus Gardien sont corrigés.
- **Remplace :** la proposition cinq Fatal, trois Gardien et deux Énergie de DEC-013 et de la première version de lecture. DEC-013 reste valable pour huit ajouts maternels 3★ et conservation des cadeaux du père.
- **Fichiers concernés :** `roman.md`, `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/runes.md`, `lore/chronologie.md`, `lore/personnages.md`, `lore/decisions.md`.
- **Questions en attente sur les nombres par ensemble :** aucune. Les valeurs individuelles et les nouvelles scènes restent soumises à lecture avec le chapitre 2.

## DEC-021 — Révision ciblée du chapitre 1 depuis la transmission mobile

- **Statut : CANON — révision narrative validée par l’auteur dans DEC-022.** L’intégration initiale ne valait pas validation ; celle-ci a ensuite été donnée explicitement.
- **Autorisation :** 20 novembre 2026, l’auteur confirme que l’intitulé « Modif chap 2 » est une erreur et que cette scène concerne la section VII du chapitre 1, puis demande l’« upgrade du chapitre 1 » et l’actualisation des références.
- **Source :** `new.txt`, blocs « Refonte chap 1 » et « Modif chap 2 », conservés intacts. Les en-têtes de courriel et signatures ne sont pas intégrés au roman.
- **Section I :** nouvelle ouverture la veille des seize ans de Hasol ; souvenir de l’éveil du premier cercle à sept ans et de la soirée avec son père. Les raretés, la progression et les points d’équipe sont expliqués en dialogue. Les coûts 5/10/20/25 et les limites de cinq membres et cinquante points restent inchangés. Une précision rend explicite le remplacement du compagnon rare par un commun dans l’exemple à quarante points, plutôt qu’un ajout illégal au groupe déjà plein en points.
- **Section VII :** la scène développée remplace l’ancien épisode d’humiliation et le résumé de l’intervention de Zio, sans doublon. Hasol est niveau 8. Ray Corvus est un ami d’enfance, issu d’une famille liée commercialement aux Shun ; devenu mage de classe rare, il participe aux rires, minimise leur amitié et refuse de la défendre. Zio récupère le carnet, confronte Ray et encourage Hasol à reconnaître ses progrès au-delà du niveau.
- **Correction ultérieure — DEC-036 :** la mention historique « classe rare » pour Ray est remplacée par **Commune**, cinq points. Seul ce libellé est corrigé dans le chapitre 1, sans réécriture de la scène ou de leur relation.
- **Préservé :** sections II à VI et VIII à XIII, chapitre 2, statistiques, XP, runes, compétences, huit paliers rétroactifs, ordre des niveaux 8 → 9 → 10 et relation non réconciliée avec le père. Aucun niveau précis n’est attribué à Ray ou Zio pendant cette scène d’Académie.
- **Portée :** remplace seulement les deux passages concernés de la version DEC-018 et précise l’implication antérieure de Ray, auparavant à confirmer. N’autorise ni l’intégration des chapitres 3 et 4 ni l’adoption des nouvelles mécaniques présentes plus loin dans `new.txt`.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`. Les règles du système et l’inventaire runique ne changent pas.

## DEC-022 — Validation du chapitre 1 révisé

- **Statut : VALIDÉ — CANON.**
- **Validation :** 20 novembre 2026, après le compte rendu d’intégration DEC-021, l’auteur déclare « ok je valide », puis demande l’ajout des chapitres 3 et 4 et l’actualisation des références.
- **Périmètre :** chapitre 1 de `roman.md` après les remplacements ciblés des sections I et VII. Le souvenir familial et la scène de Ray et Zio sont désormais validés ; les autres sections restent celles de DEC-018.
- **Limite :** cette validation ne porte pas sur le chapitre 2 ni sur les propositions futures et les réponses de ChatGPT présentes dans `new.txt`.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`. Aucun nouveau changement du texte du chapitre 1.

## DEC-023 — Intégration des chapitres 3 et 4 depuis `new.txt`

- **Statut : INTÉGRATION AUTORISÉE.** Les faits et règles transmis sont documentés ; l’import ne constitue pas une validation littéraire globale de tous les chapitres. Le chapitre 4 est désigné comme validé dans la transmission mobile, dans les consignes qui suivent son texte ; cette provenance est conservée sans étendre la validation aux consignes de rédaction du chapitre 5.
- **Autorisation :** 20 novembre 2026, « ajoute les chapitre 3 et 4 en actualisant les references ».
- **Source :** textes complets « Le prix d’un rêve » et « La voie de l’artisan » de `new.txt`. Aucun recours à une reconstitution depuis `old.txt` ; sources conservées intactes, instructions de conversation exclues du manuscrit.
- **Chapitre 3 :** lendemain de la première chasse aux loups ; 78 secondes contre le mannequin au lieu de 42, griffure encore douloureuse, marché et tentation des Collines de Braise sans départ, présentation à Orven par la mère. Première commande : Énergie commune (blanche), 2★, +0 → +3, trois réussites et un échec au passage +2 ; première secondaire Défense, grade actuel peu commun (vert). Paiement et engagement à l’essai, montants non chiffrés.
- **Chapitre 4 :** première journée complète puis ouverture de la journée suivante chez Orven. Commande Gardien commune (blanche), 2★, +0 → +2 en trois tentatives (échec +0 → +1, puis deux réussites). Apprentissage des responsabilités envers les clients, coût personnel en Mana, comparaison des principales fixes et en pourcentage, découverte de l’endurance magique de Hasol et de sa fatigue mentale. Échange avec le père, toujours distant malgré son affection.
- **État final :** Hasol dix-neuf ans, niveau 10, dix cercles et emplacements occupés, mêmes dix runes et mêmes caractéristiques naturelles qu’au chapitre 2. Aucun monstre éliminé ni gain d’XP raconté dans ces deux chapitres ; aucune compétence nouvelle, pas de révélation des 30 % ni d’Œil runique. Orven connaît désormais ses dix cercles et sa capacité naturelle de Mana 355 ; le Mana disponible après travail n’est pas chiffré.
- **Structure :** le nouveau chapitre 4 est consacré à l’artisanat. Les anciens chapitres 4 à 7 deviennent 5 à 8 ; les références futures sont décalées sans suppression d’événements. La découverte chiffrée des échecs est donc réservée au chapitre 7. Aucun chapitre 5 rédigé ni ajouté par cette opération ; les nouvelles consignes sur sa progression et ses pouvoirs restent à arbitrer avant rédaction.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md` et les cinq références actives de `lore/`.
- **À DÉFINIR :** valeurs absentes des runes de marché ou d’atelier, statistiques détaillées des commandes et quantités de travail de la journée. La prise de conscience tardive du coût personnel en Mana malgré trois ans de théorie est un point de vraisemblance à relire, pas une autorisation de réécrire les études de Hasol.
- **CONTRADICTIONS de formulation relevées après import, laissées à arbitrer :** les chapitres 3 et 4 évoquent les « crocs » du loup pour la blessure antérieure, alors que le chapitre 2 montre une griffure ; le souvenir de « deux écrins » au chapitre 4 diffère du coffret unique au chapitre 1. L’affirmation que personne n’avait reconnu la manière de travailler de Hasol doit être nuancée au regard de l’encouragement de Zio sur son carnet, désormais validé. Aucun de ces passages n’a été réécrit silencieusement lors de l’import.
- **Résolution ultérieure — DEC-026 et DEC-027 :** les refontes autorisées des chapitres 3 puis 4 conservent la griffure, rétablissent le coffret unique et retirent l’affirmation absolue sur l’absence de reconnaissance antérieure. Hasol connaît le coût personnel en Mana ; le chapitre 4 développe son suivi dans une journée réelle plutôt qu’une découverte tardive de la règle. Les points de formulation ci-dessus décrivent désormais l’état avant révision, pas des contradictions encore actives.

## DEC-024 — Mana personnel, fatigue et assiette des principales en pourcentage

- **Statut : CANON pour les règles transmises retenues lors de l’intégration des chapitres 3 et 4 ; barèmes numériques À DÉFINIR.**
- **Source et périmètre :** consignes de réorganisation puis texte « La voie de l’artisan » dans `new.txt`, intégrés sur demande de l’auteur du 20 novembre 2026 (DEC-023). Complète DEC-011 et DEC-015 sans changer les fiches naturelles existantes.
- **Amélioration :** chaque tentative consomme des pierres de mana et du Mana personnel, même en cas d’échec. Le coût en Mana dépend de la difficulté, notamment du rang en étoiles, du grade et du palier visé. Aucune table définitive de coûts n’est inventée ; la comparaison d’une commune 2★ +0 → +1 avec une rare 6★ +14 → +15 illustre la difficulté, pas un tarif.
- **Limites :** le repos restaure le Mana ; les potions peuvent restaurer la réserve sans supprimer toute fatigue mentale. Une réserve encore suffisante ne garantit pas la concentration ou la sûreté du travail. Ni taux de régénération, ni volume quotidien universel, ni multiplicateur d’endurance n’est fixé.
- **Hasol :** Mana naturel 355 au niveau 10, bonus runique connu +20 ; son endurance dans l’atelier est un avantage distinct de Bénédiction runique et de la future mesure de ses échecs. Aucun gain de maîtrise automatique ni suppression de la fatigue.
- **Principales en pourcentage :** calculées sur la caractéristique naturelle, avant ajout des bonus fixes runiques. Les exemples +50 Attaque et +10 % donnent +20 à 200 naturels, +50 à 500 et +200 à 2000 ; ce sont des valeurs pédagogiques, pas les affixes de nouvelles runes définies. Cette assiette ne fixe ni le calcul des ensembles, ni Résonance runique, ni les arrondis, ni l’adoption de pourcentages en secondaires.
- **Échec :** les commandes racontées conservent leur niveau et leur intégrité après les échecs montrés ; ne pas extrapoler une règle universelle de destruction ou de dégradation à des paliers non documentés.
- **Fichiers concernés :** `lore/systeme.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md`, états dans `lore/personnages.md`, `lore/runes.md` et `lore/chronologie.md`.

## DEC-025 — Protocole comparable du mannequin, précision du chapitre 2

- **Statut : CANON pour le protocole choisi par l’auteur ; correction ciblée intégrée au chapitre 2.** Ne valide pas globalement le chapitre ni les autres propositions de révision.
- **Source :** l’auteur choisit « Même protocole » pour comparer les résultats de 42 et 78 secondes, puis demande explicitement la modification proposée du chapitre 2.
- **Décision :** adversaire simulé guerrier ordinaire niveau 10 ; arrêt à la troisième touche reçue ; temps mesuré jusqu’à cette touche. Hasol prévoit de conserver ces réglages pour ses essais comparatifs. Il s’agit de son exercice, pas d’une règle universelle de tous les mannequins.
- **Application :** bref ajout narratif et ligne de mesure dans la fenêtre initiale du chapitre 2, section VI. Résultat de 42 secondes, une touche portée, trois reçues, statistiques, équipement, XP et suite du chapitre inchangés.
- **Raccord restant :** lors de la révision du chapitre 3, expliciter la reprise des mêmes réglages et l’atteinte de la troisième touche au moment de l’arrêt à 78 secondes. Ne pas supposer que l’actuelle chute seule démontre déjà ce protocole. Les chapitres 1, 3 et 4 ne sont pas modifiés par cette opération.
- **Raccord résolu par DEC-026 :** le chapitre 3 reprend explicitement les mêmes réglages ; deux touches sont déjà reçues avant l’extrait final, puis le balayage constitue la troisième et entraîne la chute et l’arrêt à 78 secondes.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `lore/chronologie.md`, `lore/personnages.md`, `lore/decisions.md`. Aucun changement du système runique ou de l’inventaire.

## DEC-026 — Refonte littéraire autorisée du chapitre 3

- **Statut : RÉVISION AUTORISÉE, nouvelle version de lecture intégrée.** Les choix éditoriaux et le protocole sélectionnés par l’auteur sont établis ; cette autorisation ne vaut pas validation littéraire globale du nouveau texte.
- **Autorisation :** l’auteur demande « fait une refonte du chapitre 3 », après sauvegarde de l’état importé et clarification ciblée du chapitre 2 dans DEC-025.
- **Choix explicites de l’auteur :** expliquer les règles une fois puis les montrer ; réduire les reformulations émotionnelles ; Hasol compétente en théorie mais fragilisée par le jugement ; sa mère respectait son rêve de chasseuse et attendait qu’elle soit prête à envisager l’artisanat ; mère protectrice et Orven responsabilisant ; alléger les bilans et renforcer les enjeux concrets plutôt qu’ajouter des événements.
- **Périmètre narratif :** sept sections conservées, même journée après la chasse du chapitre 2, mêmes étapes : entraînement, marché, carte des collines, proposition maternelle, rencontre privée avec Orven, épreuve, engagement à l’essai, rémunération et retour. Le premier salaire reste la récompense centrale ; la pièce laissée sur le chevet raccorde l’ouverture du chapitre 4.
- **Entraînement — CANON, raccord DEC-025 :** guerrier ordinaire simulé niveau 10, mêmes réglages que la veille, arrêt à la troisième touche reçue et durée de 78 secondes contre 42. Deux touches déjà reçues avant les derniers échanges ; le balayage touche le mollet, provoque la chute et constitue la troisième. Aucun nombre de touches portées ni total de dégâts inventé pour ce nouvel essai.
- **Caractérisation :** Hasol pose des questions pratiques, compare l’équipement et effectue les contrôles qu’elle connaît ; l’échec ne lui fait pas oublier sa théorie. Sa mère vérifie le bandage et facilite la rencontre sans demander le travail à sa place. Orven évalue consignes, méthode et suivi des ressources, sans transformer l’épreuve en thérapie ou promettre la réussite.
- **Secret :** passifs et dix cercles révélés après fermeture de la porte de l’atelier ; les statistiques magiques restent privées. Aucun avantage d’endurance ou taux d’échec chiffré découvert dans ce chapitre.
- **Préservé :** niveau 10, dix cercles et dix emplacements occupés, équipement et caractéristiques inchangés, aucune XP ni élimination nouvelle, aucun achat, compétence nouvelle ou départ aux Collines de Braise. Épreuve ORV-R001 inchangée : réussite +1, échec +2, réussite +2, réussite +3 ; première secondaire Défense et passage au vert, 2★ conservées, valeurs non chiffrées.
- **Ressources et argent :** moyens de l’épreuve fournis par l’atelier ; montants, coûts, horaires exacts et réserve disponible non chiffrés. Hasol est prise à l’essai pour commencer sa première journée complète le lendemain. Pas de contrat définitif ni de client final inventé pour la rune de l’épreuve.
- **Continuité corrigée :** les souvenirs de la blessure dans le chapitre 3 parlent désormais d’une griffure, pas de crocs ou morsure. L’encouragement antérieur de Zio sur le carnet est reconnu. Les autres points de formulation du chapitre 4 relevés dans DEC-023 restent ouverts ; le chapitre 4 n’est pas modifié.
- **Fichiers concernés :** `roman.md` (chapitre 3 seulement), `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md`, `lore/decisions.md`, `lore/chronologie.md`, `lore/personnages.md`, `lore/runes.md`. Les modifications préexistantes du chapitre 2 et de ses références sont conservées.

## DEC-027 — Adaptation du chapitre 4 après la refonte du chapitre 3

- **Statut : RÉVISION AUTORISÉE, nouvelle version de lecture intégrée.** La déclaration de validation dans la transmission mobile concernait la version initialement importée ; la nouvelle rédaction attend la lecture de l’auteur et n’est pas réputée validée par la seule demande d’adaptation.
- **Autorisation :** après la refonte DEC-026, l’auteur demande « adapte le chapitre 4 en consequence ». Application des choix éditoriaux déjà formulés : explication unique puis pratique, Hasol compétente mais fragilisée, mère protectrice, Orven responsabilisant, tensions matérielles, fin dominée par la fierté et l’autonomie.
- **Structure et scènes conservées :** dix sections, première journée complète puis matin suivant. Pièce du chevet, arrivée à l’atelier, commande client, comparaison fixe/pourcentage, endurance de Mana, fatigue mentale, conseil à la cliente, rémunération, famille et nouvelle leçon restent présents. Section VIII renommée « Le travail du lendemain ».
- **Commande CLI-R001 inchangée :** Gardien commune (blanche), 2★, +0 → +2 en trois tentatives autorisées : échec au premier +1, réussite +1, confirmation du client puis réussite +2. Restitution au client, aucune secondaire ; principale et valeurs toujours non définies. Aucun résultat supplémentaire inventé.
- **Mana et compétences :** Hasol connaît théoriquement la dépense personnelle ; elle apprend à surveiller sa réserve au fil du travail, sans découverte incohérente après trois ans de théorie. Orven découvre sa capacité naturelle de 355, bonus runique connu +20 et réserve encore disponible non chiffrée ; aucune comparaison numérique d’endurance ou de taux d’échec. L’erreur de lecture +2 au lieu de +1 est repérée avant tout engagement et impose l’arrêt des améliorations ; repos mental distinct d’une potion de Mana.
- **Pédagogie :** une scène centrale sur les principales fixes et en pourcentage (exemples +50 et +10 % sur 200/500/2000 naturels). La cliente met la méthode en pratique : profil et équipement manquants, choix laissé ouvert, aucune vente forcée ou affixe inventé. La mère écoute le vécu de sa fille au lieu de refaire la leçon ; le carnet conserve quelques observations et une question sur les tables.
- **Famille et fin :** souvenir du coffret unique du père, pas de deux écrins. Hasol accepte l’affection mais reste déçue de la brièveté de leur échange ; aucun pardon ni réconciliation. Sa satisfaction ne dépend plus entièrement de cette réaction. Le lendemain, elle prépare le poste, signale une information manquante et propose sa comparaison sous contrôle d’Orven : autonomie débutante, pas maîtrise soudaine.
- **Invariants :** niveau 10, mêmes caractéristiques naturelles, dix cercles et dix runes personnelles, quatre Fatal/quatre Gardien/deux Énergie ; aucune nouvelle XP, élimination, acquisition, amélioration personnelle, compétence ou rencontre. Avantage des 30 % réservé au chapitre 7 ; Œil runique inconnu, Aura runique non obtenue. Les chapitres 1 à 3 et leurs modifications préexistantes restent intacts.
- **Fichiers concernés :** `roman.md` (chapitre 4 seulement), `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md`, `lore/decisions.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/runes.md`, `lore/systeme.md`. Sources `new.txt` et `old.txt` conservées, aucune publication par cette opération.

## DEC-028 — Niveau minimum d’utilisation d’une arme à aura

- **Statut : CANON — décision explicite de l’auteur.**
- **Actualisation :** DEC-075 fixe Aura runique ; DEC-078 donne cet actif au niveau 1 astral. Réponse directe ultérieure de l'auteur : **seuil d'utilisation de l'arme niveau 10 maintenu, sans exception**, même avec l'actif accessible au niveau 1.
- **Source :** l’auteur demande d’ajouter au chapitre 5 qu’« il faut minimum être niv 10 pour utiliser une arme avec aura », afin de justifier pourquoi Hasol n’y avait jamais eu recours.
- **Décision :** l’utilisateur de l’arme doit être niveau 10 ou plus pour utiliser une arme imprégnée d’une aura. Ne pas confondre le niveau du porteur avec celui du forgeron, ni cette condition avec l’équipement sans niveau minimum des runes (DEC-008).
- **Portée narrative :** Hasol restait sous le niveau 10 pendant ses années d’Académie ; cette possibilité ne lui était donc pas utilisable. Explication prévue au chapitre 5 autour de l’arme de Zio ou de la visite envisagée chez le forgeron. Aucun événement nouveau n’est ajouté aux chapitres existants, et aucune ignorance générale des auras n’est attribuée à Hasol.
- **Limites :** effets d’un essai sous le seuil, justification technique et éventuelles exceptions **À DÉFINIR**. Cette décision n’adopte ni coûts/durées supplémentaires ni l’ensemble du plan du chapitre 5, que l’auteur a indiqué vouloir lire après son commit.
- **Fichiers concernés :** `lore/systeme.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `lore/decisions.md`. `roman.md` reste intact ; chapitre 5 non rédigé.

## DEC-029 — Mort du père pendant un voyage commercial lointain

- **Statut : CANON — décision explicite de l’auteur, prioritaire sur l’ancien contexte de raid.**
- **Source :** après lecture des anciens échanges ajoutés à `new.txt`, l’auteur précise que le père est marchand et demande de le faire mourir « lors d’un voyage commercial lointain à la place ».
- **Décision :** le père de Hasol meurt plus tard dans le livre I pendant un voyage commercial lointain. L’absence de véritable réconciliation avec sa fille et les regrets associés restent établis.
- **Remplace :** l’ancien décès lors d’un raid figurant au plan et dans la réponse de ChatGPT archivée dans `new.txt`. La transmission reste intacte comme provenance ; ne pas rétablir le raid lors d’un futur import.
- **À DÉFINIR :** destination, durée et date du voyage, cause exacte du décès, modalités de l’annonce et éventuels témoins ; intensité et contenu du dernier échange difficile avec Hasol. Ne pas déduire d’un voyage une attaque, un accident, une maladie ou la présence d’Hasol au décès.
- **Limites :** événement futur, non encore raconté. Le père reste vivant dans les chapitres actuels. Aucun changement de métier, réconciliation anticipée, scène nouvelle ou modification du manuscrit.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`.

## DEC-030 — Format en trois livres, troisième et dernier tome

- **Statut : CANON pour le format ; intrigue et découpage du dernier livre À DÉFINIR.**
- **Actualisation prioritaire — DEC-079/080 :** onze réincarnations au livre II, treizième et dernière vie au livre III ; les interdictions historiques d'inventer d'autres boucles ne s'opposent pas à ces décisions explicites ultérieures. Les livres I et II ont chacun seize chapitres ; dénouement heureux et prologue familial du III désormais retenus, découpage détaillé encore ouvert.
- **Source :** l’auteur indique souhaiter « 3 livres », et précise que « le troisieme livre sera le dernier ».
- **Décision :** *Les Chroniques de l’Arcaniste Runique* est prévue comme une trilogie, le livre III constituant son dernier tome.
- **Préservé :** catastrophe finale du livre I à trente-quatre ans et début du livre II avec le retour à seize ans et la classe Arcaniste Astral. Aucun événement établi n’est déplacé par cette seule décision.
- **À DÉFINIR :** contenu du livre III, titre, période, frontière narrative entre les livres II et III, réponses aux mystères et dénouement final. Ne pas inventer de troisième chronologie, seconde régression, nouvelle classe ou conclusion heureuse/tragique.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `AGENTS.md`, `lore/decisions.md`. Aucun nouveau texte romanesque.

## DEC-031 — Premier sort offensif au niveau 40 et fin du livre I vers le niveau 45

- **Statut : CANON pour les jalons et l'intention du sort ; mécanique et placement détaillé À DÉFINIR.**
- **Source :** en discutant de la dernière partie du livre I, l'auteur précise qu'Hasol arrivera « vers le niv 45 » et qu'elle obtiendra « au niv 40 enfin un sort offensif », exploitant pleinement son Mana énorme.
- **Décision :** premier sort offensif au niveau 40, conçu pour exploiter pleinement sa réserve de Mana exceptionnelle. Hasol se situe autour du niveau 45 à la fin du livre I ; ne pas transformer cette approximation en niveau exact obligatoire.
- **Préservé :** classe légendaire Arcaniste runique et absence de sort offensif au début ; rôle de l'épée et des runes avant ce déblocage. Les auras d'arme utilisables en combat ne sont pas ce premier sort offensif. Aucun changement des fiches naturelles existantes ou de la progression déjà racontée.
- **À DÉFINIR :** nom, effet, cible, portée, durée, coût et récupération du sort ; relation chiffrée avec le Mana et la Puissance arcanique, conditions de déblocage supplémentaires éventuelles, chapitre et rythme d'apprentissage. Ne pas déduire de « pleinement » une dépense totale de la réserve, une formule de dégâts ou un effet ignorant les défenses.
- **Chronologie :** destiné à la dernière partie du livre I, dans le découpage souple envisagé à seize chapitres. Le chapitre exact et le positionnement par rapport au décès du père ne sont pas fixés. La catastrophe à trente-quatre ans reste établie ; ne pas attribuer automatiquement aux compagnons le niveau 45 d'Hasol.
- **Livre II :** cette décision ne transforme pas le sort offensif en passif accessible au niveau 1 d'Arcaniste Astral. Le devenir des compétences actives après le retour n'est pas fixé par l'accès déjà validé aux anciens passifs.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`, `AGENTS.md`. Aucun chapitre rédigé ou modifié.

## DEC-032 — Réputation vers vingt-cinq ans, richesse et ralentissement des cercles

- **Statut : CANON pour la trajectoire ; chiffres et découpage détaillé À DÉFINIR.**
- **Clarification historique du 21 novembre 2026 — DEC-076, remplacée pour Œil par DEC-097 le 22 novembre 2026 :** elle retenait les types fixes et les maxima accessibles non garantis. La règle active est le résultat final exact à +15 si Hasol effectue les améliorations et atteint ce palier ; Bénédiction, échecs et coûts restent inchangés.
- **Source :** l'auteur précise qu'avant le chapitre 13, vers vingt-cinq ans, Hasol devient une artisane réputée grâce à Œil runique, dispose de fonds colossaux et peut financer ses runes à +15. Elle arrête rapidement le farm intensif de petits monstres pour suivre son groupe en donjon ; l'XP vient surtout des boss et les paliers de 1 000 monstres sont peu souvent franchis.
- **Artisanat :** la réputation et la richesse sont déjà acquises vers vingt-cinq ans, pas à introduire seulement dans la dernière partie du livre I. Œil runique reste débloqué au niveau 20 après le sauvetage de Ray, donc avant ce jalon. Aucun niveau de personnage précis n'est attribué à Hasol à vingt-cinq ans.
- **Équipement :** les ressources financières permettent de financer les améliorations personnelles jusqu'à +15. Le nombre de runes déjà à +15 à chaque scène, leurs identités, rangs, grades, caractéristiques et remplacements restent à établir ; ne pas transformer cette capacité financière en amélioration instantanée ou automatiquement réussie. Œil runique révèle les caractéristiques finales prédéterminées, pas une garantie de réussite des tentatives.
- **Progression :** l'activité du groupe et les donjons remplacent le farm intensif ; les boss apportent l'essentiel de l'XP, sans barème ni règle de partage nouvellement définis. Le nombre d'éliminations admissibles reste distinct de l'XP : un boss ne représente pas des centaines de monstres pour Croissance runique au seul motif qu'il rapporte beaucoup d'expérience.
- **Cercles :** relativement peu de nouveaux cercles dans cette trajectoire ; compteurs et nombre exact à vingt-cinq ans À DÉFINIR. Le total en fin de livre I est désormais fixé à seize par DEC-056. Les premiers paliers rétroactifs et la trajectoire antérieure déjà établie ne sont pas recalculés par cette décision ; aucun nouveau palier n'est inventé sans suivi des éliminations admissibles.
- **Conséquences éditoriales :** montrer avant le chapitre 13 l'obtention d'Œil runique, la construction de sa réputation et l'évolution de ses moyens. Dans la suite, privilégier des enjeux de responsabilité, de disponibilité, de choix d'équipement et de coopération plutôt qu'une précarité devenue incompatible avec sa richesse. Ces axes de scènes restent des propositions, pas de nouveaux événements imposés.
- **Préservé :** niveau 40 pour le premier sort offensif et environ 45 à la fin du livre I (DEC-031), progression méritée, fatigue mentale et coût des améliorations. Aucun état futur n'est présenté comme déjà survenu dans le manuscrit.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/runes.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `AGENTS.md`.

## DEC-033 — Mort du père avant la large reconnaissance artisanale

- **Statut : CANON — précision explicite de l'auteur.**
- **Source :** l'auteur précise que « son pere doit mourir avant que sa reputation d'artisan [soit] reconnu[e] par tous ».
- **Décision :** le décès du père précède la large reconnaissance publique d'Hasol comme artisane. Il connaît ses débuts chez Orven, déjà racontés, mais ne voit pas sa pleine reconnaissance. La trajectoire vers la réputation et la richesse établies vers vingt-cinq ans (DEC-032) doit respecter cet ordre.
- **Préservé :** voyage commercial lointain (DEC-029), dernier échange difficile, absence de véritable réconciliation et regrets. Ni disparition de son affection ni nouvelle scène de rejet ne sont déduites de cette chronologie.
- **À DÉFINIR :** âge exact d'Hasol au décès, chapitre, ampleur d'une éventuelle reconnaissance locale à cette date, cause et circonstances du voyage, annonce et durée du deuil. La précision porte sur l'ordre des événements ; elle ne place pas automatiquement le décès avant Œil runique ou l'embauche chez Orven.
- **Conséquence éditoriale :** la réussite publique ne permettra pas à Hasol de montrer enfin son accomplissement à son père vivant. Ne pas lui attribuer rétroactivement la connaissance de cette réputation future.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`, `AGENTS.md`. Aucun changement du manuscrit.

## DEC-034 — Mariage futur d'Hasol et de Zio

- **Statut : CANON pour l'union future ; calendrier et développement À DÉFINIR.**
- **Source :** dans la discussion de la trajectoire du livre I, l'auteur ajoute qu'Hasol « sera marié[e] a zyo ». « Zyo » est compris comme Zio Notos, le frère de Yoon, sans création d'un personnage distinct ; conserver l'orthographe Zio.
- **Décision :** Hasol et Zio se marient au cours du livre I, avant son sacrifice final. Leur rapprochement doit être construit dans la durée et ne découle pas automatiquement de son intervention à l'Académie.
- **Préservé :** Zio connaît à peine Hasol dans la scène racontée au chapitre 1 ; il ne rejoint pas leur équipe officielle du seul fait de la romance. Yoon reste une partenaire à part entière, pas seulement la sœur du futur mari.
- **À DÉFINIR :** début de l'attirance, étapes réciproques de la relation, âge et date du mariage, liens avec la mort du père et la reconnaissance artisanale. Aucun enfant ou événement conjugal supplémentaire n'est établi.
- **Fin du livre I :** le sacrifice de Zio sauve aussi son épouse ; sa mort reste canonique, sans motif exclusif inventé pour son attaque ultime.
- **Livre II :** le mariage appartient à la première chronologie. Zio n'a aucun souvenir de cette vie ; l'union ne lui est pas imposée dans la seconde, dont les relations futures restent à construire.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`, `AGENTS.md`. Aucun texte actuel du manuscrit modifié ni romance introduite rétroactivement dans le chapitre 1.

## DEC-035 — Adhésions de Ray puis Zio et minimum de trois membres en donjon

- **Statut : CANON — décisions explicites de l'auteur ; modalités et calendrier À DÉFINIR.**
- **Source :** l'auteur précise que Zio rejoindra Hasol, Yoon et Ray, et que le temps passé ensemble nourrira le rapprochement. Après avoir appris le sauvetage de Ray par Hasol, sa famille lui impose de l'aider ; Hasol accepte malgré les difficultés initiales parce que les donjons exigent au minimum trois personnes.
- **Ray :** l'aide commence sous pression familiale, pas par une transformation spontanée en compagnon repentant. Hasol accepte pour les possibilités concrètes d'une équipe de trois ; cela ne vaut ni pardon ni confiance immédiate. Les motivations personnelles de Ray et l'évolution sincère de son engagement sont à construire. Cette précision remplace l'ancien schéma où l'adhésion n'aurait eu lieu qu'après une confiance déjà reconquise.
- **Donjons :** accès exigeant au moins trois membres. Nature de la restriction (système, réglementation ou autre), contrôle, cas particuliers et maintien de l'effectif en cours d'expédition **À DÉFINIR** ; ne pas inventer ces mécanismes. Ce seuil ne change pas les chasses extérieures en solo ou en duo déjà racontées.
- **Composition corrigée par DEC-036 :** Hasol légendaire 20 + Yoon rare 10 = 30/50 à deux ; Ray **commun 5** porte le trio à **35/50**. Zio rare 10 rejoint plus tard le trio, soit quatre membres et **45/50**. Il reste une place et cinq points, sans cinquième recrue décidée. Les anciens totaux 40/50 puis 50/50 issus de la rareté erronée de Ray sont abandonnés.
- **Zio et Hasol :** rapprochement construit à travers les missions et le quotidien partagé après son adhésion ; mariage futur DEC-034 préservé. Le moment et les raisons précises de son entrée, sa progression et les étapes sentimentales restent à définir. Il n'est pas membre officiel lors des premières chasses où il supervise Hasol et Yoon.
- **Limites :** la famille de Ray apprend le sauvetage, pas automatiquement les secrets d'Hasol. Aucun motif commercial, chantage, transaction, spécialité de mage, règle d'XP ou niveau supplémentaire n'est créé par cette décision. La composition de la seconde chronologie reste distincte.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/systeme.md`, `lore/decisions.md`, `AGENTS.md`. Aucun chapitre actuel modifié.

## DEC-036 — Ray de classe commune et correction des points d'équipe

- **Statut : CANON — correction explicite et prioritaire de l'auteur.**
- **Source :** après le calcul fondé sur l'ancienne rareté, l'auteur corrige : « ray est commun [pas] rare donc 45/50 ».
- **Décision :** Ray est mage de classe **Commune**, cinq points, et non Rare. Cette correction s'applique à son apparition à l'Académie et au futur du livre I, pas à une transformation vécue par le personnage.
- **Totaux :** Hasol 20 + Yoon 10 = 30/50 ; avec Ray 5, trio à 35/50 ; avec Zio 10, quatre membres à 45/50. Une cinquième classe commune serait légalement possible à 50/50 et cinq membres, sans recrutement décidé.
- **Préservé :** aide imposée par la famille, acceptation pragmatique d'Hasol, minimum de trois membres en donjon et adhésion ultérieure de Zio. Niveau de Ray prévu au sauvetage inchangé, caractéristiques et compétences non inventées. Aucune rareté ne garantit l'issue d'un combat.
- **Manuscrit :** unique correction technique dans le chapitre 1, section VII, « classe rare de mage » remplacée par « classe commune de mage ». Aucune autre scène, aucun autre personnage de classe rare, ni chapitre suivant modifié.
- **Provenance :** les anciennes mentions de Ray rare dans `old.txt` et `new.txt` sont historiques et subordonnées à cette correction ; les sources sont conservées intactes. La seconde chronologie, dont les classes changent, n'est pas fixée par cette décision.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/systeme.md`, `lore/decisions.md`.

## DEC-037 — Ranger, évolution d'Œil runique et Main runique

- **Statut : CANON pour la classe, le rôle, les apprentissages futurs et les deux réponses explicites ; paramètres et calendrier À DÉFINIR.**
- **Actualisation prioritaire — DEC-078/080 :** l'ancien réapprentissage rapide de Main au livre II est remplacé : Main active et Œil avec pièges sont disponibles au niveau 1 astral ; Main ouvre coffres et portes sans restriction. Samia reste au livre I mais ne rejoint plus l'équipe principale des nouvelles vies. Les limitations historiques ci-dessous ne doivent pas annuler ce choix explicite.
- **Source :** l'auteur précise que le cinquième membre commun est un Ranger : archerie, détection des pièges et ouverture des coffres. Vers la fin du livre I, Hasol apprend auprès de lui ; elle obtient une évolution de l'Œil pour voir les pièges et Main runique active pour ouvrir les coffres, afin de couvrir ces fonctions sans Ranger indispensable dans le livre II.
- **Composition :** Hasol légendaire 20 + Yoon rare 10 + Ray commun 5 + Zio rare 10 + Ranger commun 5 = cinq membres et 50/50 points. La simple possibilité de cinquième recrue évoquée dans DEC-035/036 devient donc un recrutement futur prévu, sans nom, date ni niveau inventé.
- **Clarification explicite sur l'Œil :** l'auteur choisit « Même passif amélioré ». Œil runique conserve son nom et ses effets antérieurs, avec détection des pièges ajoutée ; pas d'Œil arcanique distinct ni de changement de nom.
- **Clarification explicite sur le livre II :** l'auteur choisit « Réapprentissage rapide » pour Main runique. Elle n'est pas accessible automatiquement au niveau 1 ; aucun transfert de toutes les actives n'est ajouté à la règle des anciens passifs. Le moment et les conditions de ce réapprentissage restent à préparer.
- **Apprentissage et identité :** le Ranger doit être un compagnon dont l'expérience précède les pouvoirs d'Hasol, pas un simple archer ajouté pour remplir les points. Identité, personnalité, motivation, recrutement et relation avec le groupe à construire. La fonction de mentor ne décide pas de son sort final ou de sa place dans la seconde vie.
- **Limites :** coûts, portée, durée, réussite, conditions de déblocage et protections concernées À DÉFINIR. La détection n'accorde pas un désamorçage universel, Main runique n'ouvre pas automatiquement toute serrure et n'est pas un sort offensif. Aucun changement de statistiques ou de chapitres déjà écrits.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/systeme.md`, `lore/decisions.md`, `AGENTS.md`.

## DEC-038 — Croissance runique évoluée : un cercle par cent boss personnels

- **Statut : CANON — règle et deux précisions explicitement choisies par l'auteur.**
- **Actualisation — DEC-078 :** compteurs remis à zéro à chaque nouvelle vie. Cette précision ne réinitialise pas le reliquat inconnu de la première vie et ne décide pas du report des cercles.
- **Source :** l'auteur situe vers le niveau 38 une évolution après cent boss de donjon personnellement achevés, ajoutant un cercle tous les cent boss quel que soit leur niveau. Aux questions de comptage, il choisit « Oui, premier cercle immédiat » et « Oui, deux compteurs distincts ».
- **Déclencheur :** cent boss de donjon achevés personnellement, vers le niveau 38. Ne pas imposer de niveau minimum exact absent de la formulation « vers » ; le coup final personnel compte, pas la seule présence dans le groupe ou la réception d'XP.
- **Effet ajouté :** un cercle de Mana par cent boss personnels, sans restriction sur leur niveau. Le premier est accordé au déclenchement sur les cent boss initiaux, le deuxième au total 200, puis 300, etc. Le nouvel effet ne remplace pas celui par mille monstres.
- **Cumul :** un boss avance les deux compteurs s'il remplit l'admissibilité de l'ancien. Il n'est qu'une élimination dans celui des mille monstres ; ne pas le convertir en cent monstres, ni recompter d'anciens paliers déjà récompensés. Les deux gains se cumulent si leurs seuils tombent sur la même élimination.
- **À DÉFINIR :** chapitre, calendrier, total de cercles, équipement lié aux nouveaux gains, rythme des boss suivants et modalités des compteurs au livre II. Aucun report des éliminations de première vie ni nouveau rang de rune n'est établi.
- **Préservé :** ralentissement des paliers de mille monstres après l'abandon du farm, forte XP des boss, premier sort offensif au niveau 40 et niveau final proche de 45. Cette évolution n'est pas un sort offensif et n'est pas révélée prématurément aux personnages.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`, `AGENTS.md`. Aucun chapitre actuel modifié.

## DEC-039 — Retraite devant un boss invocateur et besoin d'un Ranger

- **Statut : CANON pour la rencontre, la retraite et la proposition de Zio ; détails À DÉFINIR.**
- **Source :** l'auteur indique que le groupe de quatre affronte un boss niveau 32 invoquant en masse des monstres niveau 11 tant qu'un piège n'est pas désactivé. Le groupe finit par fuir ; Zio, le plus expérimenté, propose de recruter un Ranger avant de revenir au donjon.
- **Chronologie :** après l'adhésion de Zio, avant celle du Ranger ; les quatre sont Hasol, Yoon, Ray et Zio, 45/50 points. Le boss est niveau 32, les invocations niveau 11 ; aucun niveau du groupe ou d'Hasol n'en est déduit.
- **Fonction narrative :** le besoin du cinquième membre provient d'une difficulté vécue, pas du seul calcul de points. Les personnages se retirent au lieu de résoudre immédiatement le piège sans compétence établie ; l'expérience de Zio conduit à sa proposition de recrutement.
- **À DÉFINIR :** donjon, nature et emplacement du piège, modalités de désactivation, nombre et rythme des invocations, blessures et ressources, identité et arrivée du Ranger, déroulement et résultat de la seconde tentative. Ne pas inventer d'invulnérabilité du boss ni de victoire automatique après désactivation.
- **Compteurs :** XP et admissibilité des invocations aux compteurs de monstres à définir avant tout calcul. Aucune élimination personnelle de boss, seuil de Croissance runique ou ressource gagnée n'est réputé acquis par cette annonce.
- **Précision ultérieure — DEC-040 :** l'admissibilité des invocations au compteur initial de Croissance runique est désormais retenue sous les conditions habituelles de niveau et d'élimination personnelle. L'XP et les gains exacts restent ouverts ; le mécanisme doit servir au développement des cercles dans le livre II.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/systeme.md`, `lore/decisions.md`, `AGENTS.md`. Aucun texte du manuscrit modifié.

## DEC-040 — Exploitation du donjon invocateur dans la seconde vie

- **Statut : CANON — intention explicite de l'auteur ; scène et gains détaillés À DÉFINIR.**
- **Source :** l'auteur indique avoir choisi volontairement des invocations niveau 11 pour qu'Hasol s'en souvienne dans sa seconde vie et utilise ce donjon afin d'augmenter ses cercles grâce à son passif.
- **Décision :** le donjon de DEC-039 est une préparation narrative du livre II. Hasol garde le souvenir de son mécanisme et exploite les invocations en maintenant le piège actif pendant ses éliminations personnelles ; elles peuvent avancer le compteur de mille monstres sous ses conditions de niveau. Cette exploitation est voulue, pas une erreur à corriger par une interdiction de récompense inventée.
- **Seuils préservés :** niveau 11 des invocations compatible avec les tranches déjà définies pour Hasol 10–19 et 20–29. Dès Hasol niveau 30, l'exigence de monstres niveau 20+ exclut ces invocations du compteur initial. Le fonctionnement avant le niveau 10 dans la seconde vie reste à préciser ; la décision ne modifie pas silencieusement ces seuils.
- **Compteurs distincts :** les invocations ne sont pas des boss. Leur élimination n'alimente donc pas l'effet des cent boss ; maintenir le boss en vie ne fournit pas plusieurs victoires sur lui. Aucun cercle ni palier historique n'est recompté automatiquement.
- **Limites à construire :** niveau et chapitre de la visite, groupe remplissant le minimum de trois membres, cadence, ressources, XP, nombre d'éliminations et cercles gagnés. Ne pas inventer de plafond anti-farm, d'invocations gratuites sans limite ou d'exemption d'effectif. Le souvenir de ce mécanisme ne rend pas toute la mémoire d'Hasol infaillible.
- **Préservé :** retraite initiale à quatre puis recrutement du Ranger au livre I, mémoire imparfaite, progression et autres règles d'équipement. Aucune scène réécrite ou rédigée par cette seule annonce.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/systeme.md`, `lore/decisions.md`, `AGENTS.md`.

## DEC-041 — Samia Claire, Ranger et amie de Yoon

- **Statut : CANON — identité et lien explicitement fixés par l'auteur.**
- **Source :** l'auteur précise que « la ranger sera une fille Samia Claire, une amie de yoon de l'academie ».
- **Décision :** la cinquième membre prévue est **Samia Claire**, une femme, amie de Yoon à l'Académie. Classe Ranger commune, cinq points ; groupe final à cinq membres et 50/50, fonctions d'archerie et d'exploration inchangées.
- **Préservé :** Zio propose le recrutement après la retraite à quatre du donjon invocateur (DEC-039). Le lien préalable avec Yoon donne une connaissance existante sans définir encore la présentation, l'accord ou la motivation de Samia. Hasol apprend auprès d'elle vers la fin du livre I (DEC-037).
- **À DÉFINIR :** âge, niveau, apparence, personnalité, histoire de l'amitié, motivations, date d'arrivée et modalités de recrutement. Ne pas lui attribuer l'âge, le niveau ou les secrets d'Yoon par simple association ; aucune connaissance antérieure d'Hasol n'est fixée.
- **Livre II :** la réduction du besoin technique d'une Ranger ne décide pas de la relation ou de la place de Samia dans la seconde vie.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/systeme.md`, `lore/decisions.md`, `AGENTS.md`. Aucun chapitre actuel modifié.

## DEC-042 — Âge, niveau relatif et acceptation de Samia

- **Statut : CANON — précisions explicites de l'auteur.**
- **Source :** l'auteur précise « meme age que yoon, niveau un peu plus faible que yoon », puis indique qu'elle accepte de venir dès qu'elle apprend que Zio fait partie du groupe.
- **Décision :** Samia a le même âge que Yoon et un niveau légèrement inférieur au moment de son introduction. Son acceptation de venir est immédiate lorsqu'elle apprend la présence de Zio.
- **À DÉFINIR :** date de recrutement, âge et niveau chiffrés à cette date, écart exact, raison de l'intérêt pour Zio et éventuelle connaissance antérieure. Le niveau légèrement inférieur ne devient pas une loi permanente de progression ni une règle de rareté.
- **Limites :** ne pas supposer qu'elle a seize ans à un recrutement plus tardif, qu'elle connaît déjà personnellement Zio, qu'elle est amoureuse de lui ou qu'elle rivalise avec Hasol. L'auteur fixe le déclencheur de son accord, pas encore son motif profond.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`, `AGENTS.md`. Aucun chapitre actuel modifié.

## DEC-043 — Beauté, force et popularité de Zio

- **Statut : CANON — caractérisation explicite de l'auteur.**
- **Source :** l'auteur précise que « zio est tres beau, fort et donc tres populaire », après les décisions sur l'acceptation de Samia.
- **Décision :** Zio est très beau et fort ; ces qualités contribuent à sa grande popularité. Ce contexte éclaire l'intérêt de Samia pour sa présence dans le groupe sans définir à lui seul ses sentiments.
- **À DÉFINIR :** description physique, portée de la notoriété, réactions concrètes des personnages et nature précise de l'intérêt de Samia. Aucune connaissance personnelle antérieure ou rivalité amoureuse fixée.
- **Limites :** ne pas transformer sa popularité en arrogance, conduite séductrice, invulnérabilité ou gain de niveau. Sérieux, expérience, intervention à l'Académie et rapprochement progressif avec Hasol sont préservés.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/decisions.md`. Aucun texte du manuscrit modifié.

## DEC-044 — Érudition de Ray et proximité d'enfance avec Hasol

- **Statut : CANON — caractérisation et lien explicitement précisés par l'auteur.**
- **Source :** l'auteur décrit Ray comme un « vrai rat de bibliotheque », sachant énormément de choses, plus qu'Hasol, et explique par cela leur très grande proximité pendant l'enfance.
- **Décision :** Ray est très porté sur les livres et possède un bagage de connaissances supérieur à celui d'Hasol. Cette dimension intellectuelle et leur curiosité partagée complètent les jeux, projets d'aventures et liens commerciaux familiaux déjà établis.
- **À DÉFINIR :** lectures, domaines exacts, façon de partager ou d'exposer ses connaissances, limites et scènes d'enfance correspondantes. Aucune liste de compétences ou de sorts, spécialité magique ou information secrète ne sont ajoutées automatiquement.
- **Préservé :** classe commune, aide imposée par la famille après le sauvetage, coopération d'abord pragmatique, confiance à reconstruire. L'érudition ne justifie pas sa participation aux humiliations ; le passé affectueux rend cette rupture personnelle sans l'effacer.
- **Garde-fous :** ne pas rendre Ray omniscient ou toujours compétent en pratique, ni retirer les acquis théoriques d'Hasol. Son bagage général ne fixe pas une supériorité éternelle dans chaque domaine, notamment l'artisanat qu'elle développera.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/decisions.md`. Aucun passage du manuscrit validé réécrit par cette précision.

## DEC-045 — Validation du plan du livre I en seize chapitres

- **Statut : CANON pour les titres, l'ordre et les jalons du plan ; détails laissés ouverts non validés implicitement.**
- **Actualisation — DEC-072/079/080 :** chapitres 5 à 9 validés séparément ; le livre I se clôt sur l'activation temporelle et le basculement, le réveil ouvre le II. Les seize chapitres et onze réincarnations du livre II sont désormais décidés explicitement, sans valider tous les anciens découpages proposés.
- **Validation :** après la proposition actualisée en seize chapitres et la précision sur l'autodestruction de Zio, l'auteur déclare « je valides le plan des chapitres ».
- **Référence unique :** section 6 de `PLAN_DIRECTEUR.md`, désormais consolidée de 1 à 16. Les anciens découpages concurrents après le chapitre 8 sont remplacés ; leurs éléments utiles sont redistribués dans ce plan, sans réécrire le manuscrit ni les archives.
- **Début :** chapitres 1 à 4 préservés. Chapitre 5 : rencontre de Yoon, premières chasses et blessure, forgeron, équipe puis Hasol 10 → 11 et Aura runique. Chapitre 6 : vies parallèles, entraînement, expérimentation critique de l'aura et chasse du passage étroit ; ne pas raconter une seconde fois 10 → 11. Chapitres 7 et 8 : reconnaissance d'Orven, guilde, équipement amélioré puis loup alpha.
- **Ascension :** chapitre 9, douze cercles, Hasol 19 et Yoon 24 ; chapitre 10, sauvetage de Ray, niveau 20, Œil runique et aide imposée par sa famille, trio à 35/50. Chapitre 11 : Zio rejoint le groupe à 45/50, père mort pendant le voyage commercial sans réconciliation. Chapitre 12 : retraite devant le boss invocateur, recrutement de Samia à 50/50, reconnaissance et richesse installées vers vingt-cinq ans.
- **Maturité et fin :** chapitre 13, vie du groupe, rapprochement et mariage avec Zio, transmission de Samia et nouveaux usages d'Œil runique/Main runique. Chapitre 14 : centième boss personnel et évolution de Croissance runique vers le niveau 38. Chapitre 15 : premier sort offensif au niveau 40, apprentissage et préparation de la crise. Chapitre 16 : catastrophe à trente-quatre ans, environ niveau 45 ; Zio déclenche son **autodestruction**, l'explosion tue Zio et le démon stellaire, sauvant Hasol ; récupération de la rune temporelle. L'activation ouvre le livre II.
- **À DÉFINIR :** dates et scènes détaillées, niveaux intermédiaires de Yoon, courbe d'XP, paramètres d'Aura/Chant/Résonance encore ouverts, sorts et ultimes, inventaires futurs, conditions de décès du père, étapes affectives et sort précis de Samia dans la catastrophe. Les données de conversation ou de ChatGPT non arbitrées ne deviennent pas des règles par la seule validation du découpage.
- **Portée :** validation du plan du livre I uniquement, pas validation littéraire globale des versions de lecture 2 à 4, ni réécriture du chapitre 1, ni autorisation nouvelle de rédiger un chapitre. Les livres II et III restent à structurer ; aucun plan de douze ou seize chapitres pour ces livres n'est validé par extension.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `AGENTS.md`, `lore/chronologie.md`, `lore/personnages.md`, `lore/decisions.md`, `source.md`. Manuscrit et sources conservés.

## DEC-046 — Yoon soutien, choix des sorts, cercles et niveau final 54

- **Statut : CANON pour l'orientation, les formes choisies et les jalons ; paramètres numériques et suite du répertoire À DÉFINIR.**
- **Actualisation — DEC-050/074 :** Résonance ajoute les deux premières secondaires au niveau 40, sans devenir passive ; trois compétences de départ au niveau 1, dont Vague runique de Lumière. Après l'attente initiale, **l'auteur valide directement le 21 novembre 2026 le soin de 10 % des PV maximums de Yoon toutes les cinq secondes**. Les réserves historiques ci-dessous sur ces chiffres sont levées ; durée, coût et portée restent ouverts.
- **Source :** l'auteur précise que Yoon est une soutien plutôt qu'une soigneuse pure, dont le soin sur la durée reste très inférieur à celui d'une spécialiste ; il souhaite un contrôle de foule comme prochain sort. Il choisit « Domaine au niveau 20 », « Renforcement actif ciblé » et « Zone de soin posée », puis fixe Yoon niveau 54 à la fin du chapitre 16 et des zones en cercles d'écritures runiques au sol pour rappeler Sage runique.
- **Résonance runique :** actif ciblé, temporaire, seules principales des runes de l'allié choisi amplifiées, jamais secondaires ou ensembles. La variante d'aura passive est remplacée ; amplification, durée, portée, coût et récupération non fixés.
- **Soin :** Chant runique devient une zone posée, permettant à Yoon d'agir après le placement, pas une canalisation continue qui la rendrait immobile ou qui cesserait nécessairement dès sa concentration perdue. Ce remplacement porte sur le fonctionnement, pas sur une nouvelle scène déjà racontée. Paramètres de 10 % toutes les cinq secondes et cinq mètres/trente secondes du texte transmis restent à arbitrer, sans adoption automatique.
- **Contrôle :** prochain sort au niveau 20, Domaine des Entraves Runiques déjà prévu : ralentissement en zone, alliés épargnés, coût de maintien en Mana et résistance partielle des puissants conservés. Ni avancée au niveau 10 ni première entrave supplémentaire n'est retenue.
- **Visuel :** les zones de soin et de contrôle ont la forme de cercles au sol avec écritures runiques. Ne pas en déduire un empilement illimité, une permanence ou le caractère de piège, ni transformer l'actif ciblé en aura de groupe.
- **Progression :** niveau 5 à la rencontre, niveau 20 avant son niveau 24 au sauvetage, **niveau 54 en fin de chapitre 16**. Niveaux intermédiaires, statistiques, niveaux initiaux des capacités déjà disponibles à 5 et sorts après le niveau 20 restent à définir. Les coefficients d'XP envisagés ne sont pas adoptés par ce jalon.
- **Conséquences de rédaction :** adapter les anciennes scènes qui faisaient de l'interruption d'un chant maintenu la cause de la rupture du soin. La fragilité du soutien et les erreurs de placement restent des enjeux ; ne pas lui accorder pour autant les soins d'urgence ou les réparations d'une soigneuse pure. Aucun nouveau sort n'est ajouté à son répertoire sans décision.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `lore/pistes.md`, `AGENTS.md`. Aucun chapitre du manuscrit modifié.

## DEC-047 — Couleurs des zones de Yoon et idée de dégâts progressifs

- **Statut : CANON pour les couleurs du soin et du ralentissement ; PROPOSITION pour le nouveau cercle de dégâts.**
- **Source :** l'auteur fixe « vert pour le soin, violet pour le ralentissement », puis propose qu'« on peut imaginer un cercle de degat overtime rouge ».
- **Décision visuelle :** les cercles de soin sont verts et ceux de ralentissement violets, en conservant les écritures runiques au sol de DEC-046. Cette identité narrative ne modifie pas le CSS ou les conventions de couleur des bonus dans les fiches.
- **Piste conservée :** cercle rouge de dégâts sur la durée. Son adoption comme sort, son nom, sa puissance et ses conditions sont à définir. Le niveau 30 est une suggestion ultérieure de l'assistant, pas un choix de l'auteur ni une règle déduite du Domaine niveau 20.
- **Précision ultérieure — DEC-048 :** l'auteur retient ce sort sous le nom Tempête arcanique au niveau 50. Nom, forme et niveau sont désormais canoniques ; le niveau 30 suggéré est abandonné. Paramètres numériques et cumul restent ouverts.
- **Préservé :** Yoon soutien polyvalente et non soigneuse pure, Résonance active ciblée, soin en zone posée, prochain contrôle au niveau 20 et niveau 54 au chapitre 16. Aucun sort offensif supplémentaire n'est ajouté automatiquement à son répertoire.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/pistes.md`, `lore/decisions.md`. Aucun texte du manuscrit modifié.

## DEC-048 — Tempête arcanique de Yoon au niveau 50

- **Statut : CANON pour le sort, sa forme et son déblocage ; paramètres À DÉFINIR.**
- **Source :** l'auteur précise « sort niv 50 tempete arcanique --> cercle rouge degat overtime ».
- **Décision :** Yoon obtient au **niveau 50 Tempête arcanique**, sort actif en cercle rouge de dégâts sur la durée, avec les écritures runiques au sol de sa classe. Cette décision adopte et précise la piste de DEC-047, en remplaçant le niveau 30 suggéré par l'assistant.
- **Progression :** Domaine de contrôle au niveau 20 conservé ; Tempête arcanique 50 précède le niveau final 54 au chapitre 16. Chapitre exact, première utilisation et autres sorts éventuels restent à définir ; aucun pouvoir intermédiaire nouveau n'est ajouté automatiquement.
- **À DÉFINIR :** puissance, assiette, coût, durée, rayon, cadence, récupération, cibles, persistance éventuelle après sortie et cumul. Le nom ne donne pas des effets supplémentaires de vent, foudre, projection ou dégâts instantanés. L'absence d'effet sur les alliés n'est pas encore fixée pour ce cercle par analogie avec le Domaine.
- **Préservé :** Yoon soutien polyvalente, soins progressifs inférieurs à une spécialiste, Résonance active ciblée et cercles posés. Aucun chiffre de soin ou de dégâts n'est adopté par cette décision.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/pistes.md`, `lore/decisions.md`, `AGENTS.md`. Aucun texte du manuscrit modifié.

## DEC-049 — Second soin de Yoon au niveau 30 : marque runique sur un allié

- **Statut : CANON pour le niveau, le ciblage et le soin sur la durée ; nom et paramètres À DÉFINIR.**
- **Source :** l'auteur précise qu'au niveau 30, Yoon obtient un second soin sur la durée, cette fois sous forme d'une marque runique posée sur un allié.
- **Décision :** second soin, ciblé et progressif, obtenu au niveau 30. La marque est portée par l'allié plutôt qu'une zone posée au sol ; Chant runique en cercle reste distinct. Aucun nom officiel n'est choisi par cette description.
- **À DÉFINIR :** puissance et assiette, cadence, durée, coût, récupération, portée, nombre de marques, éventuelle mobilité ou interruption et cumul avec la zone ou plusieurs marques. Ne pas supposer un soin instantané, permanent, multi-cible ou automatiquement plus puissant que le soin de zone.
- **Préservé :** soutien et non soigneuse pure, Domaine des Entraves au niveau 20, Tempête arcanique au niveau 50, niveau final 54 au chapitre 16. Aucune capacité supplémentaire ni caractéristique nouvelle n'est déduite.
- **Chronologie :** chapitre exact et première utilisation à fixer. Le soin n'est pas utilisable lors du sauvetage de Ray où Yoon est niveau 24, ni dans les premières chasses niveau 5.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `AGENTS.md`. Aucun texte du manuscrit modifié.

## DEC-050 — Résonance runique évoluée au niveau 40, premières secondaires

- **Statut : CANON pour le niveau, l'extension et le maintien en actif ciblé ; paramètres À DÉFINIR.**
- **Source :** l'auteur indique qu'au niveau 40 son « passif » évolue pour prendre en compte les deux premières secondaires. Invité à préciser cette formulation par rapport au choix d'actif ciblé de DEC-046, il choisit **« Garder l'actif ciblé »**, avec amplification des deux premières secondaires de chaque rune de l'allié ciblé et ensembles exclus.
- **Décision :** à son niveau 40, Résonance runique conserve le ciblage actif temporaire et amplifie aussi les deux premières secondaires présentes sur chacune des runes équipées de l'allié choisi, en plus des principales. Pas de conversion en passif ni d'aura de proximité.
- **Limites :** troisième et quatrième secondaires et bonus d'ensemble exclus. Aucun affixe n'est créé sur une rune qui n'en possède pas ; si une seule secondaire est présente, seule celle-ci est concernée par l'extension. L'effet initial avant le niveau 40 reste limité aux principales, notamment lors du sauvetage où Yoon est niveau 24.
- **À DÉFINIR :** ordre exact déterminant les deux premières secondaires, coefficients, interactions et arrondis, durée, coût, portée, récupération, chapitre et première utilisation. Ne pas déduire une amplification fixe, un effet sur les statistiques naturelles ou le niveau des runes.
- **Préservé :** Domaine niveau 20, marque de soin niveau 30, Tempête arcanique niveau 50 et fin au niveau 54 ; aucun nouveau sort intermédiaire ajouté. Le niveau 40 de Yoon n'est pas celui d'Hasol ni une date commune imposée.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `lore/pistes.md`, `AGENTS.md`. Aucun texte du manuscrit modifié.

## DEC-051 — Statistiques naturelles de Yoon au niveau 60

- **Statut : CANON.**
- **Source :** l'auteur donne « HP: 10380 ATK: 417 DEF: 703 vit: 111 », demande un Mana de soutien et une Puissance arcanique de soutien avec 300 supplémentaires, puis précise que ces valeurs n'incluent pas ses runes. Enregistrement autorisé par « go ».
- **Décision :** au niveau 60, Yoon possède naturellement PV 10 380, Attaque 417, Défense 703, Vitesse 111, Mana 1 000 et Puissance arcanique 900. Les valeurs magiques appliquent les repères de DEC-015 : Mana normal 1 000 et Puissance arcanique de soutien 600 + 300.
- **Portée :** fiche hors runes et effets temporaires, propre à Yoon. Ne remplace pas son niveau 54 au chapitre 16, ne fixe aucune date d'atteinte du niveau 60, aucun équipement ni courbe de progression. Les statistiques aux autres niveaux restent à définir.
- **Préservé :** soutien polyvalente, pas soigneuse pure. Aucun coefficient de soin, de dégâts ou d'amplification n'est validé par ces valeurs.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre du manuscrit modifié.

## DEC-052 — Vitesse d'incantation, déplacement et esquive

- **Statut : CANON pour les effets qualitatifs ; paramètres À DÉFINIR.**
- **Source :** l'auteur précise « la vitesse augmente la vitesse d'incantation , la vitesse de deplacement --> l'esquive », puis autorise l'enregistrement par « go ».
- **Décision :** la caractéristique Vitesse augmente la vitesse d'incantation et la vitesse de déplacement ; la mobilité accrue favorise l'esquive par le mouvement.
- **Limites :** aucune probabilité automatique d'esquive, formule, proportion, limite ou valeur de temps n'est fixée. Aucun effet supplémentaire sur la vitesse d'attaque n'est déduit de cette précision.
- **Fichiers concernés :** `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre du manuscrit modifié.

## DEC-053 — Fiche future de Zio : niveaux, caractéristiques et inspiration

- **Statut : CANON pour les niveaux et la fiche naturelle ; inspiration désignée, adaptations détaillées À DÉFINIR.**
- **Source :** échange du 20 novembre 2026 : l'auteur fixe Zio au niveau 61 à la fin du livre I, l'autodestruction au niveau 50, puis au niveau 60 « HP: 11850 ATK: 648 DEF: 593 SPD: 115 », Mana et Puissance arcanique de soutien. Après présentation de la fiche naturelle avec Mana 1 000 et Puissance arcanique 600 selon DEC-015, l'auteur autorise l'intégration par « go ».
- **Décision :** au niveau 60, caractéristiques naturelles hors runes et compétences : PV 11 850, Attaque 648, Défense 593, Vitesse 115, Mana 1 000, Puissance arcanique 600. Niveau 61 lors du sacrifice au chapitre 16 ; autodestruction débloquée au niveau 50.
- **Inspiration :** guide du Paladin d'Eden Eternal pour les passifs et sorts ; glyphes comme référence pour les cercles runiques et les valeurs apportées par les runes. Classe Gardien, Rare, conservée. Aucun équipement ni pouvoir supplémentaire adopté automatiquement.
- **Limites :** pas de progression chiffrée déduite, de statistiques inventées au niveau 61, de plafond au niveau 60 ni de règle de butin au-delà de 60. L'issue canonique du sacrifice ne définit pas la formule de l'autodestruction.
- **À DÉFINIR :** compétences et passifs adaptés, soins éventuels, nom et paramètres de l'ultime, date de son déblocage, nombre de cercles, équipement détaillé et fiche au niveau 61. Les propositions de l'assistant restent non validées.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `source.md`, `AGENTS.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-054 — Statistiques naturelles de Hasol au niveau 60

- **Statut : CANON.**
- **Source :** l'auteur fournit « HP: 12180 ATK: 350 DEF: 250 SPD: 110 », Mana 3500 et Puissance arcanique 2150. Après comparaison aux chapitres existants et constat des 115 de Vitesse naturelle au niveau 10, il précise « ok vitesse 130 niv 60 », puis autorise l'enregistrement par « go » après présentation de la fiche naturelle hors équipement et effets temporaires.
- **Décision :** au niveau 60, Hasol possède naturellement PV 12 180, Attaque 350, Défense 250, Vitesse 130, Mana 3 500 et Puissance arcanique 2 150. La valeur de Vitesse 110 est abandonnée au profit de 130.
- **Portée :** référence future hors runes, ensembles et effets temporaires. Les fiches des niveaux 1, 9 et 10 et les gains déjà racontés sont préservés. Hasol termine toujours le livre I vers le niveau 45 ; aucune date ou vie d'atteinte du niveau 60 n'est fixée.
- **Limites :** aucune progression linéaire, valeur intermédiaire, formule de dégâts ou compétence nouvelle déduite. Les repères généraux de DEC-015 restent inchangés. L'intérêt comparé des principales fixes et en pourcentage dépend toujours de leurs valeurs réelles, sans bascule universelle garantie par cette fiche.
- **À DÉFINIR :** courbe naturelle après le niveau 10, niveau de franchissement de 1000 Mana, statistiques intermédiaires et équipement futur.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `source.md`, `AGENTS.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-055 — Huit cercles runiques pour Yoon au niveau 60

- **Statut : CANON.**
- **Source :** l'auteur propose d'abord douze cercles au niveau 60, puis rectifie explicitement : « quoique non c'est trop elle en dispose de 8 ».
- **Décision :** Yoon possède huit cercles runiques au niveau 60, distincts des cercles de sorts posés au sol. Le nombre de douze est abandonné.
- **Limites :** aucun palier d'obtention intermédiaire, nombre au niveau 54, inventaire ou état d'équipement n'est fixé. Ne pas déduire huit runes équipées ni une progression universelle applicable à tous les personnages. Son niveau 54 à la fin du livre I reste inchangé.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre modifié.

## DEC-055 — Huit cercles runiques pour Zio au niveau 60

- **Statut : CANON.**
- **Source :** l'auteur précise le 20 novembre 2026 : « zio dispose de 8 cercle runnique au niveau 60 ».
- **Décision :** Zio possède huit cercles runiques au niveau 60, soit huit emplacements pour ses runes. Le nombre jusque-là ouvert dans DEC-053 est fixé pour ce niveau.
- **Limites :** huit emplacements ne prouvent pas huit runes équipées. Inventaire, ensembles, affixes, grades, étoiles, améliorations, dates et modalités d'acquisition des cercles restent **À DÉFINIR**. Aucune progression universelle par niveau, aucun nombre au niveau 61 et aucun total de cercles d'Hasol ne sont déduits.
- **Fichiers concernés :** `lore/personnages.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/decisions.md`, `AGENTS.md`. Aucun chapitre modifié, aucun commit ni push.

## DEC-056 — Seize cercles runiques pour Hasol en fin de livre I

- **Statut : CANON.**
- **Source :** l'auteur précise « hasol dispose de 16 clercle runnique à la fin du livre I ».
- **Décision :** Hasol possède seize cercles runiques, soit seize emplacements, à la fin du livre I, au chapitre 16, vers le niveau 45 conformément à DEC-031 et DEC-045.
- **Préservé :** dix cercles dans les chapitres actuels, douze au chapitre 9 et évolution de Croissance runique au centième boss au chapitre 14. Aucun chapitre existant n'est réécrit.
- **Limites :** le total ne valide ni seize runes équipées, ni un inventaire, ni une répartition des gains entre les compteurs de mille monstres et de cent boss. Aucun report automatique des cercles ou compteurs au livre II, ni total au niveau 60 n'est fixé.
- **À DÉFINIR :** dates et modalités détaillées d'acquisition, compteurs finaux, occupation et équipement associés.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`. Aucun chapitre modifié, aucun commit ni push.

## DEC-057 — Cercles d'Hasol aux fins des livres II et III

- **Statut : CANON.**
- **Actualisation ciblée — DEC-136 :** la partie fixant **32 cercles/emplacements à la fin du livre II est retirée du canon**. Les lignes ci-dessous conservent la décision historique et sa provenance ; elles ne doivent plus fixer le total du II. Le jalon distinct de **36 cercles/emplacements à la fin du livre III** demeure canonique.
- **Raccord avec DEC-079 :** les **32 cercles de fin du livre II sont le jalon avant le dernier retour temporel**, pas un nombre validé au réveil de la vie 13. Le report des cercles reste non validé ; ne pas le confondre avec les compteurs de Croissance remis à zéro ou avec Mémoire conservée.
- **Source :** l'auteur demande « 32 rune fin livre II et livre III fin du livre 36 stocke cette informations », puis autorise l'enregistrement par « go » après reformulation en cercles et emplacements disponibles.
- **Décision :** Hasol dispose de **32 cercles runiques, soit 32 emplacements, à la fin du livre II**, et de **36 cercles runiques, soit 36 emplacements, à la fin du livre III**. Le jalon de seize cercles à la fin du livre I (DEC-056) est préservé.
- **Portée :** nombres de cercles disponibles, pas inventaires de runes équipées. Ces jalons de fin de tome ne sont pas des fiches au niveau 60 ; niveaux et âges correspondants, acquisition détaillée, compteurs, occupation et équipement restent **À DÉFINIR**. Aucun report automatique des cercles ou compteurs de la première vie vers la seconde n'est validé.
- **Limites :** aucune validation des répartitions, grades, étoiles, principales, secondaires, conventions de calcul ou totaux proposés dans les simulations. Aucun nouveau retour temporel, changement du dénouement du livre I ou découpage des livres II/III déduit.
- **Fichiers concernés :** `lore/personnages.md`, `lore/chronologie.md`, `lore/systeme.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-058 — Sorts et passifs du Gardien de Zio

- **Statut : CANON pour les noms, types, niveaux, effets qualitatifs et limites ; paramètres chiffrés À DÉFINIR.**
- **Source :** l'auteur répond « je valide » à la proposition de six actifs et trois passifs, comprenant leurs niveaux d'obtention et leurs limites. L'obtention de l'autodestruction au niveau 50 était déjà canonique par DEC-053 ; son nom devient Dernier Rempart.
- **Actifs :** Heurt du Gardien au niveau 1 (coup de bouclier renforcé par le Mana, déséquilibre et interruption non garantis) ; Défi du Gardien au 10 (provocation ciblée sans contrôle absolu) ; Égide protectrice au 20 (absorption limitée sur un allié, protection brisable, sans soin ni transfert automatique des blessures) ; Bénédiction de vigueur au 30 (soin personnel progressif limité, ni instantané ni restauration automatique des blessures graves) ; Rempart de lumière au 40 (protection directionnelle devant le bouclier, position et effet maintenus) ; Dernier Rempart au 50 (autodestruction, explosion au prix de sa propre vie).
- **Passifs :** Maîtrise du bouclier au niveau 1 (efficacité accrue lors d'un blocage correct, sans couverture de tous les angles) ; Ancrage du Gardien au 20 (résistance aux déséquilibres et déplacements forcés lorsqu'il prend appui pour défendre, sans immunité) ; Volonté inébranlable au 60 (meilleur maintien des protections malgré douleur et fatigue, sans annulation des dégâts, coûts ou incapacités, ni maintien après la mort).
- **Rôle :** protecteur de première ligne, magie de soutien et soin personnel secondaire ; Yoon reste soutien à part entière. La progression concerne Zio, pas une règle universelle des classes.
- **Continuité :** niveau 45 au chapitre 5, capacités disponibles jusqu'au niveau 40 ; aucun Dernier Rempart avant le niveau 50 ni Volonté inébranlable avant le niveau 60. Niveau de Zio à l'Académie toujours inconnu. Au chapitre 16, niveau 61, Dernier Rempart tue Zio et le démon stellaire et permet à Hasol de survivre ; motivations non réduites au seul statut d'époux.
- **À DÉFINIR :** coûts, durées, récupérations, puissances, portées, nombres de cibles, cumuls, interactions et modalités précises ; préparation de l'autodestruction, sécurité des alliés, dates et scènes de découverte. Aucun chiffre ni formule de dégâts adopté par cette validation.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-059 — Caractéristiques naturelles de Samia Claire au niveau 60

- **Statut : CANON.**
- **Source :** l'auteur précise : « samiaa claire stast level 60 hp 9060 atk 659 def 549 mana 950 puissance arcanique 2200 ». « samiaa claire » désigne Samia Claire, sans nouveau personnage.
- **Décision :** fiche naturelle au niveau 60, hors runes, ensembles et effets temporaires : PV **9 060**, Attaque **659**, Défense **549**, Mana **950**, Puissance arcanique **2 200**.
- **À DÉFINIR :** Vitesse, cercles, équipement, progression intermédiaire et date d'atteinte du niveau 60. Aucun niveau de fin de tome n'est déduit de cette fiche.
- **Limites :** classe Ranger commune et rôle d'archerie/exploration préservés ; aucun sort, coefficient de dégâts ou changement de classe déduit de la Puissance arcanique.
- **Fichiers concernés :** `lore/personnages.md`, `lore/decisions.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-060 — Caractéristiques naturelles de Ray Corvus au niveau 60

- **Statut : CANON.**
- **Source :** l'auteur précise : « ray stast level 60 hp 8760 atk 1472 def 458 mana 800 puissance  arcanique 2000 ».
- **Complément de l'auteur :** « vitesse 110 ».
- **Cercles — complément de l'auteur :** « nombre de cercle 10 » : Ray possède **dix cercles runiques au niveau 60**, soit **dix emplacements**. Occupation et étapes d'acquisition **À DÉFINIR** ; aucune progression universelle ni dix runes équipées déduites.
- **Décision :** fiche naturelle au niveau 60, hors runes, ensembles et effets temporaires : PV **8 760**, Attaque **1 472**, Défense **458**, Vitesse **110**, Mana **800**, Puissance arcanique **2 000**.
- **À DÉFINIR :** équipement, progression intermédiaire et date d'atteinte du niveau 60. Aucun niveau de fin de tome n'est déduit de cette fiche.
- **Limites :** classe de mage commune préservée ; aucune compétence ni formule de dégâts déduite de ces valeurs. Aucun changement de son état raconté au chapitre 1.
- **Fichiers concernés :** `lore/personnages.md`, `lore/decisions.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-060 — Niveau de Samia en fin de livre I et Vitesse au niveau 60

- **Statut : CANON.**
- **Source :** l'auteur précise : « fin livre I niv 52 vitesse niv 60 125 ».
- **Décision :** Samia Claire est **niveau 52 à la fin du livre I**. Sa **Vitesse naturelle au niveau 60 est 125**, complétant la fiche DEC-059.
- **Limites :** les autres caractéristiques de DEC-059 restent propres au niveau 60 ; aucune interpolation au niveau 52 ni courbe de progression validée. Date d'atteinte du niveau 60, caractéristiques au niveau 52, cercles, équipement et sort précis dans la catastrophe restent **À DÉFINIR**.
- **Fichiers concernés :** `lore/personnages.md`, `lore/decisions.md`, `lore/chronologie.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-061 — Sept cercles runiques pour Samia Claire

- **Statut : CANON pour le nombre ; rattachement chronologique À DÉFINIR.**
- **Source :** l'auteur précise : « nombre de cercle 7 », à la suite de la fiche de Samia.
- **Décision :** Samia Claire possède **sept cercles runiques**, soit **sept emplacements**.
- **À DÉFINIR :** rattachement à la fin du livre I au niveau 52 ou à la fiche de référence au niveau 60, étapes d'acquisition et occupation effective. Sept emplacements ne valident pas sept runes équipées ni un inventaire.
- **Fichiers concernés :** `lore/personnages.md`, `lore/decisions.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-062 — Ray et Samia, prodiges de classe commune

- **Statut : CANON.**
- **Source :** l'auteur précise que Ray est un prodige pour un personnage de classe commune, tout comme Samia, et que tous deux possèdent un nombre de cercles anormalement élevé pour leur classe.
- **Décision :** Ray et Samia sont des prodiges de classe commune ; leurs nombres de cercles runiques sont exceptionnels pour cette classe. Préserver les dix cercles de Ray au niveau 60 et les sept de Samia, dont le rattachement chronologique reste à définir.
- **Limites :** aucun changement de rareté, aucune cause particulière, compétence ou acquisition supplémentaire déduite. Cette précision ne règle pas les questions chronologiques et d'équipement ouvertes. La norme numérique, non fixée par cette décision, est ensuite établie à quatre cercles au niveau 60 pour les classes communes par DEC-064.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-063 — Yoon et Zio, haut du panier des classes rares en cercles

- **Statut : CANON.**
- **Source :** l'auteur précise « yoon, est dans le haut du panier des personnage de classe rare tout comme zio en nombre de cercle ».
- **Décision :** Yoon et Zio se situent dans le haut du panier des personnages de classe rare pour leur nombre de cercles runiques. Leurs huit cercles chacun au niveau 60 ne constituent pas la norme de cette classe.
- **Limites :** aucune norme, répartition, limite maximale ou progression de classe n'est fixée par cette décision. DEC-064 établit ensuite la norme des classes rares à six cercles au niveau 60. Cette précision ne change pas leur rareté et ne garantit pas une supériorité générale en statistiques ou en combat. Aucune cause particulière de ce nombre élevé n'est déduite.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre modifié.

## DEC-064 — Normes de cercles runiques par classe au niveau 60

- **Statut : CANON pour les classes commune, rare et légendaire ; classe astrale À DÉFINIR.**
- **Source :** l'auteur précise « la norme des classe rare et de 6 cercle level 60 , legendaire 8 cercle , commun 4 cercle ».
- **Décision :** au niveau 60, la norme est de quatre cercles runiques pour une classe commune, six pour une classe rare et huit pour une classe légendaire.
- **Portée :** normes de référence, pas plafonds ni nombres obligatoires. Les totaux individuels validés restent inchangés ; Yoon et Zio, avec huit cercles chacun au niveau 60, dépassent de deux la norme des classes rares.
- **À DÉFINIR :** norme astrale, paliers d'acquisition, répartition des écarts et plafonds éventuels. Ne pas extrapoler dix cercles pour les classes astrales ou une progression linéaire, ni déduire un équipement effectif.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre modifié.

## DEC-065 — Cercles des classes astrales : nombre inconnu, légendes au-delà de dix

- **Statut : CANON pour l'incertitude et l'existence des légendes ; nombre réel À DÉFINIR.**
- **Source :** l'auteur précise « ASTRAL inconu mais les legende parle de plus de 10 cercle ».
- **Décision :** le nombre de cercles des personnages de classe astrale est inconnu. Des légendes leur attribuent plus de dix cercles.
- **Limites :** l'existence de ces récits est établie, pas leur véracité chiffrée. Aucun nombre exact, plafond, niveau d'atteinte ou norme vérifiée au niveau 60 n'est fixé. Ne pas présenter onze ou douze cercles comme une valeur validée, ni attribuer automatiquement la connaissance de ces légendes à chaque personnage.
- **Fichiers concernés :** `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre modifié.

## DEC-066 — Livre II : hypothèse d'une collecte de mana accrue auprès d'Hasol

- **Statut : CANON pour l'émission future de l'hypothèse ; véracité et mécanisme À DÉFINIR.**
- **Source :** l'auteur indique que, dans le livre II, une hypothèse sera émise selon laquelle faire équipe avec Hasol permet de collecter davantage de mana et donc de recevoir des cercles de mana plus vite.
- **Décision narrative :** cette hypothèse sera formulée dans le livre II. Son auteur, les observations qui la motivent, la scène et le chapitre restent à définir.
- **Limites :** l'hypothèse n'est pas une règle confirmée du système. Aucun passif, aura, transfert de Mana, bonus chiffré, portée ou condition d'équipe n'est adopté. Ne pas confondre la collecte de mana évoquée avec une hausse établie de la réserve naturelle, de sa régénération ou de l'XP. Aucun mécanisme général de formation des cercles n'est fixé par cette décision.
- **Continuité :** ne pas en faire rétroactivement la cause certaine des nombres élevés de cercles des compagnons, ni annoncer cette hypothèse dans le livre I. Elle ne remplace pas les conditions validées de Croissance runique et ne change pas les totaux individuels connus.
- **Fichiers concernés :** `lore/decisions.md`, `lore/systeme.md`, `lore/chronologie.md`. Aucun chapitre modifié ou rédigé.

## DEC-067 — Cercles naturels et disponibilités du groupe au livre I

- **Statut : CANON pour la difficulté croissante et le calendrier relatif ; chiffres et dates À DÉFINIR.**
- **Source :** l'auteur précise que plus le niveau augmente, plus l'obtention des cercles naturels devient difficile. Il explique les dix cercles de Ray par d'innombrables chasses en duo avec Hasol dans sa tranche de niveaux 30–40 pendant les études de Yoon. Il confirme le cadre du livre I : Yoon ne combat avec Hasol que les week-ends et vacances au début, Ray a terminé l'Académie et Zio appartient à un autre groupe ; Zio rejoint l'équipe quand Yoon termine l'Académie.
- **Règle :** l'obtention des cercles naturels devient plus difficile à mesure que le niveau du personnage augmente. Aucun seuil, barème ou mécanisme chiffré n'est fixé ; ne pas appliquer automatiquement cette difficulté aux compteurs spécifiques de Croissance runique.
- **Calendrier :** après son recrutement, Ray chasse très fréquemment en duo avec Hasol durant ses propres niveaux 30–40, tandis que Yoon poursuit ses études et chasse avec Hasol les week-ends et vacances. Cette activité contribue à expliquer les dix cercles de Ray au niveau 60, sans fixer ses gains pendant cette période. Zio appartient à un autre groupe avant de rejoindre officiellement celui d'Hasol à la fin des études de Yoon, au chapitre 11 conformément à DEC-045.
- **Limites :** les chasses en duo ne constituent pas une dérogation au minimum de trois membres en donjon. Ne pas attribuer la tranche 30–40 de Ray à Hasol, avancer ses dix cercles à cette période ou inventer la composition de l'autre groupe de Zio. Durée, dates, niveaux et cercles intermédiaires restent à définir.
- **Distinction avec DEC-066 :** l'influence d'Hasol sur la collecte de mana demeure une hypothèse émise au livre II, pas une explication confirmée des gains du livre I.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`. Aucun chapitre modifié ou rédigé.

## DEC-068 — Ray au niveau 56 en fin de livre I

- **Statut : CANON.**
- **Source :** l'auteur précise « ray niv 56 fin livre I ».
- **Décision :** Ray est niveau 56 à la fin du livre I, au chapitre 16.
- **Limites :** caractéristiques, nombre de cercles et équipement au niveau 56 restent à définir. Sa fiche de référence et ses dix cercles au niveau 60 ne sont pas automatiquement acquis à ce stade. Cette précision ne valide pas les courbes de cercles proposées dans la conversation.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/decisions.md`. Aucun chapitre modifié.

## DEC-069 — Répertoire de mage de feu commun de Ray

- **Statut : CANON pour la spécialité, les noms, niveaux, effets qualitatifs et limites ; paramètres chiffrés À DÉFINIR.**
- **Source :** l'auteur précise « mage feu », puis répond « ok je valide » à la proposition de six actifs, trois passifs et risque des flammes pour les alliés.
- **Actifs :** Boule de feu au niveau 1, Souffle ardent au niveau 10, Trait incandescent au niveau 20, Mur de flammes au niveau 30, Déflagration au niveau 40 et Fournaise au niveau 50. Effets et limites détaillés dans `lore/systeme.md`.
- **Passifs :** Affinité du feu au niveau 1, Résistance à la chaleur au niveau 20 et Combustion maîtrisée au niveau 40. Pas de contrôle universel des incendies, d'immunité au feu, de sorts gratuits ou de régénération automatique de Mana.
- **Identité :** mage de feu de classe commune, techniques directes et Boule de feu emblématique ; maîtrise, tactique et équipement font la différence. Aucune omniscience, nouvelle rareté, flamme ignorant toute défense ou attaque gigantesque supplémentaire adoptée.
- **Risque allié :** les flammes peuvent menacer les compagnons dans leur trajectoire ou leur zone. Cette décision concerne Ray, sans généralisation automatique aux autres sorts du roman. Paramètres précis et interactions avec les protections à définir.
- **Continuité :** compétences jusqu'au niveau 20 seulement lors du sauvetage au niveau 22 ; les six actifs et trois passifs sont disponibles au niveau 56 final. Niveau à l'Académie et dates de déblocage restent ouverts. Les courbes de cercles proposées ne sont pas validées par cette décision.
- **À DÉFINIR :** coûts, puissances, portées, durées, récupérations, temps d'incantation, cumuls, maintien, interruptions et scènes d'apprentissage. Aucun calendrier universel de classe ni formule de dégâts fixé.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`. Aucun chapitre modifié ou rédigé.

## DEC-070 — Ray épuise rapidement son Mana

- **Statut : CANON pour la faible endurance magique ; paramètres À DÉFINIR.**
- **Source :** après validation du répertoire de feu, l'auteur précise « il essoufle vite son mana ».
- **Décision :** Ray épuise rapidement sa réserve de Mana en combat. Il doit doser ses sorts et ménager ses ressources malgré sa puissance offensive et ses nombreux cercles.
- **Compatibilité :** Combustion maîtrisée réduit les pertes à partir du niveau 40 sans faire disparaître cette faiblesse. Aucun changement de sa réserve naturelle de référence au niveau 60, fixée à 800, n'est déduit.
- **Limites :** coûts, régénération, récupération et nombre de sorts possibles restent à définir. Ne pas déduire une maladie, un essoufflement physique automatique ou une pénalité chiffrée.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/decisions.md`. Aucun chapitre modifié.

## DEC-071 — Dernier Rempart : sacrifice de PV réglable

- **Statut : CANON pour le choix et la relation qualitative ; paramètres À DÉFINIR.**
- **Source :** l'auteur précise que moins Zio conserve de PV en pourcentage, plus les dégâts sont importants, et qu'il choisira 0 % pour être certain de vaincre le démon. Interrogé sur le choix entre sacrifice réglable et puissance liée uniquement aux blessures préalables, il confirme « il peut choisir ».
- **Décision :** à l'activation de Dernier Rempart, Zio choisit les PV qu'il consomme. Plus le pourcentage conservé est faible, plus l'explosion est puissante. Un sacrifice partiel peut être non mortel ; à 0 % conservé, il meurt et la puissance du sort est maximale. Au chapitre 16, il choisit le sacrifice total et tue le démon stellaire en mourant, permettant à Hasol de survivre.
- **Correction de DEC-058 :** l'expression « au prix de sa propre vie » décrit le choix final, pas une obligation à chaque usage. Nom, niveau d'obtention 50, niveau final 61 et issue de la catastrophe inchangés. Ne pas obliger Zio à attendre d'être mortellement blessé avant le lancement.
- **À DÉFINIR :** formule et assiette exacte du pourcentage, valeurs de dégâts, granularité du choix, préparation, portée, récupération, Mana éventuel, interactions avec soins et protections, sécurité des alliés. Aucune proportionnalité, dégâts infinis, invulnérabilité ou victoire automatique contre toute cible déduits.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `lore/chronologie.md`, `lore/decisions.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`. Aucun chapitre modifié ou rédigé ; aucun commit ni push.

## DEC-072 — Validation des chapitres 5 à 9 et révisions séparées

- **Statut : CANON pour les validations et le workflow ; révisions 1 à 4 PROPOSITION jusqu'à lecture et approbation.**
- **Source :** décisions explicites de l'auteur dans la session du **21 novembre 2026**, précisant la sélection des textes transmis dans `new.txt`. La mention globale par ChatGPT de « chapitres 1 à 9 validés » ne remplace pas cet arbitrage ciblé.
- **Décision :** chapitres 5 à 8 validés et chapitre 9 dans sa dernière version corrigée validé ; retenir **la version 2 du chapitre 5**. Ajouts ciblés de fenêtres système et raccords minimaux autorisés aux chapitres 5 à 9, sans réécriture générale.
- **Préservation :** les chapitres 1 à 4 actuels de `roman.md` restent intacts ; **audit avant toute retouche**. Les propositions peuvent être conservées dans `chap1_revision.md` à `chap4_revision.md`, clairement marquées **PROPOSITION**. Elles ne constituent pas un second manuscrit canonique et ne remplacent que le chapitre explicitement approuvé après lecture. Conserver les brouillons jusqu'à instruction de l'auteur.
- **Demande complémentaire explicite de l'auteur dans la même session :** « inclure des pop-up avec les règles du lore en début et fin de chapitre ». Ajouter de courts **repères pour le lecteur**, à l'ouverture et à la clôture, sans les présenter comme des notifications nouvelles reçues par les personnages. L'ouverture ne révèle aucune découverte future ; la clôture récapitule seulement les règles acquises à ce point. Chapitres 1 à 4 : propositions séparées uniquement ; chapitres 5 à 9 : ajout ciblé au manuscrit autorisé. Pas de réécriture littéraire globale par cette demande.
- **Limites :** ne valide ni toutes les notes d'équilibrage de ChatGPT, ni les chapitres suivants, ni les plans détaillés des livres II/III. `new.txt` et `old.txt` restent intacts ; aucune autorisation implicite de publication.
- **Arbitrage complémentaire — rune de récupération, chapitre 6 :** l'auteur demande de « changer sa couleur » plutôt que supprimer les secondaires de la petite rune blanche 1★. Choix éditorial dans cette autorisation : **rare (bleue), 1★**, pour conserver les secondaires au pluriel sans inventer leurs types, valeurs ou une amélioration. Ne pas appliquer ce grade aux autres runes communes sacrifiées lors des essais.
- **Fichiers concernés :** `roman.md`, éventuels fichiers de révision, `AGENTS.md`, `PLAN_DIRECTEUR.md`, `source.md`, références de `lore/`. L'enregistrement de la décision ne signifie pas que chaque intégration ou audit est déjà réalisé.

## DEC-073 — Affinités : cycle élémentaire, Lumière et Ténèbres

- **Statut : CANON pour les rapports et coefficients ; détails de calcul À DÉFINIR.**
- **Source :** arbitrages explicites de l'auteur, session du **21 novembre 2026**, avec acceptation du tableau incluant la neutralité entre éléments identiques.
- **Décision :** **Eau > Feu > Terre > Eau** : avantage **×1,25** sur les dégâts finaux et la précision ; faiblesse inverse **×0,75**. **Lumière et Ténèbres sont neutres entre eux**, chacun ayant l'avantage sur les trois éléments du cycle (**×1,20**), avec faiblesse inverse (**×0,80**). Même élément : **×1**.
- **Portée :** toutes les attaques réellement élémentaires, pas seulement Aura runique. La précision est **multiplicative**, pas un ajout de points. Ne pas attribuer un élément à une attaque non identifiée par les sources.
- **À DÉFINIR :** plafonds, arrondis, cas multiélémentaires, ordre avec le plancher d'Infiltration et autres effets. Aucun supplément de dégâts ou d'esquive automatique déduit.
- **Fichiers concernés :** `lore/systeme.md`, `PLAN_DIRECTEUR.md`, fiches de compétences et fenêtres concernées ; présent registre.

## DEC-074 — Vague runique de Lumière et règles de Yoon

- **Statut : CANON pour Vague, les formes des capacités et le soin de Chant ; durée, coût et portée du soin À DÉFINIR.**
- **Source :** transmission `new.txt`, bloc « Instructions Codex — Nouvelle compétence de Yoon : Vague runique » et chapitres, puis **arbitrages explicites de l'auteur du 21 novembre 2026** : Lumière pour Vague seule, incantation cinq secondes, Résonance active ciblée et Chant posé. Les anciennes propositions « environ une seconde » et « sans affinité » sont remplacées.
- **Vague runique :** actif offensif au **niveau 1**, **5 Mana**, dégâts de base **20 % de la Puissance arcanique de Yoon**, portée **10 mètres**, incantation **5 secondes**, **aucun temps de recharge**, aucun effet supplémentaire adopté. Dégâts soumis à la Défense et aux affinités. L'élément **Lumière** concerne cette attaque, pas toute la classe Sage runique.
- **Départ :** Résonance runique, Chant runique et Vague runique disponibles dès le niveau 1. Yoon reste un soutien polyvalent, pas une mage offensive spécialisée ni une soigneuse pure.
- **Résonance :** actif ciblé temporaire, principales seulement avant 40 ; au niveau 40, ajoute les **deux premières secondaires de chaque rune** selon DEC-050. Troisième/quatrième secondaires et ensembles exclus ; aucune annulation de cette évolution par la note globale mobile résumant le fonctionnement initial.
- **Chant — réponse directe ultérieure de l'auteur, 21 novembre 2026 :** zone verte **posée et autonome**, soin **10 % des PV maximums de Yoon toutes les cinq secondes**. Yoon peut agir ensuite. Cette décision explicite lève l'attente de DEC-046 sur l'assiette, la quantité et la cadence ; elle ne découle pas de la seule note de ChatGPT. **Durée, coût et portée restent À DÉFINIR**, sans adopter cinq mètres/trente secondes ni appliquer ce taux aux autres soins.
- **Préservé :** Domaine 20, marque de soin 30, évolution de Résonance 40, Tempête arcanique 50, niveau final 54. Aucun élément des autres sorts de Yoon n'est déduit de Vague.
- **Fichiers concernés :** `lore/systeme.md`, `lore/personnages.md`, `PLAN_DIRECTEUR.md`, `roman.md` dans le périmètre ciblé autorisé par DEC-072 ; présent registre.

## DEC-075 — Aura runique : coût, durée et Infiltration au lancement critique

- **Statut : CANON pour les paramètres retenus ; interactions À DÉFINIR.**
- **Source :** déclaration de l'auteur dans `new.txt`, « le coup critique lors du lancement du sort aura runique », avec exemple **300 PA contre 1 000 Défense**, durée **30 secondes** et destruction d'une rune ; chapitres 5 v2/6 retenus et confirmations de la session du **21 novembre 2026** pour coût et durée.
- **Décision :** Aura runique coûte **200 Mana et une rune définitivement détruite par lancement** ; l'aura élémentaire dure jusqu'à **24 heures**. Première vie : déblocage au niveau 11, chapitre 5.
- **Infiltration runique :** déclenchée par un **critique au lancement d'Aura**, pendant les **trente premières secondes**. Les coups portés avec l'arme imprégnée ont un minimum de dégâts égal à la **PA effective d'Hasol**, sans réduction de ce plancher par la Défense. Le plancher ne plafonne pas un coup normalement supérieur et ne retire pas une quantité fixe de Défense.
- **Limites :** un critique ordinaire à l'épée ne déclenche jamais Infiltration. Après trente secondes, l'aura normale demeure jusqu'à son terme. Une nouvelle tentative paie le même coût ; pas de garantie de critique ou d'essais gratuits.
- **À DÉFINIR :** cumul/remplacement, ordre entre affinités, critiques des coups et plancher, arrondis. **Articulation tranchée par réponse directe ultérieure :** Aura niveau 1 astral, mais utilisation de l'arme à aura niveau 10 **sans exception** (DEC-028/078).
- **Fichiers concernés :** `lore/systeme.md`, `lore/personnages.md`, `PLAN_DIRECTEUR.md`, fenêtres et références des chapitres 5/6 ; présent registre.

## DEC-076 — Bénédiction, Arcanique et formules critiques

- **Statut : CANON pour Bénédiction, les formules et le remplacement de Lame ; lecture d’Œil HISTORIQUE, remplacée par DEC-097 ; maintien des affixes CC/DCC HISTORIQUE, remplacé par DEC-098 le 22 novembre 2026.**
- **Source :** chapitre 7 validé, notes de transmission `new.txt` « Bénédiction runique » / « Ensemble Arcanique » et confirmations explicites de l'auteur dans la session du **21 novembre 2026**. L'ancienne mention « +1 200 à confirmer » est remplacée par la valeur retenue dans le chapitre 7 validé.
- **Bénédiction :** environ **30 % d'échecs en moins relativement au taux d'Orven**, pas trente points. Second effet caché : un renforcement variable consécutif à une réussite atteint **très souvent le maximum autorisé**, sans garantie ni fréquence numérique adoptée. Aucun choix libre de caractéristique, dépassement de plafond ou renforcement supplémentaire ; les échecs restent coûteux. Ne pas modifier rétroactivement les améliorations antérieures.
- **Arcanique :** ensemble **quatre pièces, +1 200 Puissance arcanique** ; deux ou trois pièces inactives. Ensemble rare et très cher, influençant indirectement critiques et compétences à PA. L'équipement détaillé relève de `lore/runes.md`, pas d'une table universelle déduite du chapitre.
- **Critiques :** `CC (%) = 5 + PA effective / 80 + bonus directs de CC` ; `DCC (%) = 150 + PA effective / 100 + bonus directs de DCC`. Les attaques normales à l'épée sont concernées, pas seulement les sorts. À 100 % de CC ou davantage, l'action éligible est critique, sans surcritique supplémentaire ; aucun plafond artificiel ajouté. Ordre des contributions à la PA effective et arrondis à définir.
- **Fusion clarifiée par réponse directe ultérieure de l'auteur, 21 novembre 2026 :** **retirer Lame du système actif, remplacé par Arcanique**. L'ancienne règle Lame, deux pièces pour +12 % de chance critique, est conservée uniquement comme historique, sans réécriture des anciens chapitres. La contradiction initialement signalée est donc résolue. **Historique remplacé par DEC-098 :** cette clarification maintenait alors les affixes individuels CC/DCC de DEC-004 ; ils sont désormais retirés des principales et secondaires, sans modification des formules critiques.
- **Œil/Bénédiction — HISTORIQUE pour la lecture d’Œil, remplacée par DEC-097 le 22 novembre 2026 ; réponse directe de l'auteur du 21 novembre 2026 :** les **types de secondaires sont prédéterminés et identiques quel que soit l'artisan**. Œil montrait les **maxima accessibles si Hasol améliore**, pas une réalisation garantie de ces valeurs à +15. Un autre artisan obtient les mêmes types mais peut atteindre des valeurs plus faibles. **Bénédiction favorise les maxima sans garantie**, les échecs et leurs coûts subsistent. Cette clarification conservait types et potentiel et remplaçait l'ancienne promesse de valeurs finales figées/garanties ; elle ne modifiait pas les résultats passés. Bénédiction et les types prédéterminés restent inchangés sous DEC-097.
- **Fichiers concernés :** `lore/systeme.md`, `lore/runes.md`, `lore/personnages.md`, `PLAN_DIRECTEUR.md`, fenêtres des chapitres 7 à 9 ; présent registre.

## DEC-077 — Anneau de Ray et Aimant runique

- **Statut : CANON pour l'objet, le déclencheur, les effets qualitatifs, le plafond d'étoiles, l'exemple niveau 30 et les distributions de grades ; fréquence globale et dépendance étoiles/grade À DÉFINIR.**
- **Source :** déclarations et notes de `new.txt` sur le cadeau de la famille de Ray et Aimant au niveau 21, confirmées et corrigées par l'auteur dans la session du **21 novembre 2026**. Ne pas confondre cette provenance avec un texte de chapitre déjà rédigé.
- **Anneau :** remerciement familial après le sauvetage, remis personnellement par Ray ; **inventaire spécialisé réservé aux runes**, contrairement à l'inventaire ordinaire mélangeant les objets sans tri natif dédié. Aucun bonus statistique ou emplacement d'équipement supplémentaire établi.
- **Scène prévue :** Hasol feint de prendre la remise de l'anneau pour une demande en mariage afin de taquiner Ray ; humour, pas validation d'une romance ni véritable demande. La scène ne résout pas immédiatement tout le passif entre eux.
- **Première vie :** **Aimant runique au niveau 21**, condition : **avoir combattu avec un Anneau runique**. Interface volontairement vague : chances d'obtention de runes améliorées. Effets cachés : butins plus fréquents, davantage d'étoiles, meilleure qualité et grades élevés, dont légendaires. Aucun pourcentage affiché dans cette interface, butin garanti ou connaissance immédiate des effets cachés pour Hasol ; les distributions d'auteur documentées ci-dessous ne deviennent pas automatiquement son savoir.
- **Chaque nouvelle vie :** l'obtention doit être renouvelée après un **combat avec l'anneau** ; niveau exact dans les vies astrales à définir, sans disponibilité automatique au niveau 1 (DEC-078).
- **Réponse directe ultérieure de l'auteur, 21 novembre 2026 — précision de DEC-007 :** la tranche de niveau du monstre fixe le **plafond**, pas un rang garanti. Un monstre niveau 30 peut donner **1★, 2★ ou 3★**. **Conditionnellement à l'obtention d'une rune**, distribution ordinaire : **1★ 50 %, 2★ 35 %, 3★ 15 %** ; avec Aimant : **1★ 20 %, 2★ 30 %, 3★ 50 %**. Cet exemple s'applique **au seul monstre niveau 30** ; ne pas l'extrapoler à toute sa tranche ou à tous les niveaux. Aimant favorise donc les étoiles hautes sans dépasser le plafond.
- **Grades — réponse directe ultérieure de l'auteur, 21 novembre 2026 :** la phrase initialement corrompue est remplacée par les tables suivantes, **conditionnelles à l'obtention d'une rune**. Sans Aimant : **blanc 74 %, vert 20 %, bleu 5 %, violet 0,9 %, orange 0,1 %**. Avec Aimant : **blanc 39 %, vert 35 %, bleu 20 %, violet 5 %, orange 1 %**. Chaque table totalise **100 %**. L'auteur a expressément corrigé le violet ordinaire à **0,9 %** après une première version à 100,1 % ; il ne s'agit pas d'une normalisation automatique. Tables détaillées dans `lore/systeme.md`.
- **Articulation :** les étoiles et le grade restent distincts, et **leur indépendance n'est pas validée**. Ne pas multiplier les tables pour inventer les probabilités conjointes d'un rang et d'un grade. La fréquence globale d'obtention d'une rune n'est pas fixée par ces distributions conditionnelles.
- **Autres limites :** fréquence globale d'obtention d'une rune toujours inconnue, aucun monstre garanti de donner une rune. Capacité de stockage et report de l'objet/inventaire à travers les vies également inconnus. L'ouverture des portes/coffres n'appartient pas à Aimant : correction DEC-078.
- **Fichiers concernés :** `lore/systeme.md`, `lore/personnages.md`, `PLAN_DIRECTEUR.md`, `lore/chronologie.md` ; présent registre.

## DEC-078 — Classe astrale : capacités au niveau 1, exceptions et compteurs

- **Statut : CANON pour la liste, les corrections et le maintien du seuil d'arme à aura ; reports À DÉFINIR.**
- **Source :** arbitrages explicites de l'auteur dans la session du **21 novembre 2026**, complétant la transmission. La note mobile attribuait l'ouverture à Aimant : l'auteur corrige en **Main runique active**, coffres **et portes sans restriction**.
- **Niveau 1 d'Arcaniste Astral :** **Bénédiction runique**, **Croissance runique**, **Œil runique avec détection des pièges**, **Main runique active ouvrant coffres et portes sans restriction**, **Aura runique active**. La classe vaut vingt-cinq points. Ces dispositions concernent les vies astrales, pas une modification rétroactive de la première vie légendaire.
- **Remplace :** le réapprentissage rapide de Main prévu dans DEC-037 ; la formulation réductrice « anciens passifs seulement » ; l'attribution de l'ouverture à Aimant dans la fin de `new.txt`. Ne pas réintroduire une difficulté de serrure excluant certaines portes/coffres ; coût, portée et modalités non précisés restent ouverts, tout comme les limites de détection des pièges. Détecter n'accorde pas automatiquement leur désamorçage.
- **Exceptions :** **Aimant est redébloqué dans chaque vie après combat avec l'anneau**, niveau exact à définir ; **Mémoire runique n'est pas disponible avant R11**, puis est conservée pour la vie 13. Ne pas généraliser cette liste à toutes les anciennes actives ou transférer le premier sort offensif au niveau 1.
- **Croissance :** compteurs **à zéro à chaque nouvelle vie**. Ne pas appliquer cette remise à zéro au reliquat inconnu de la première vie ; elle ne décide pas du nombre de cercles disponibles/reportés ni de l'admissibilité des monstres avant le niveau 10.
- **Raccord de première vie — arbitrage direct complémentaire :** l'auteur choisit **« Inclure le reliquat »** dans les compteurs du chapitre 9. Les affichages 999/1 000 puis 1 998/2 000 suivent la progression cumulée **après les huit paliers déjà récompensés**, reliquat antérieur inclus, et non les seules éliminations depuis le niveau 10. La valeur isolée du reliquat reste inconnue ; aucun ancien millier recompensé et aucune élimination supprimée. Les douze cercles et scènes des nouveaux seuils sont conservés.
- **Réponse directe ultérieure de l'auteur, 21 novembre 2026 — point résolu :** Aura active **niveau 1 astral**, mais **seuil d'utilisation de l'arme à aura niveau 10 maintenu, sans exception** (DEC-028). Ne pas retirer la compétence ni montrer Hasol utilisant personnellement une arme à aura au niveau 1. Les recruteurs sont impressionnés par le **potentiel de la classe**, pas par une utilisation personnelle prématurée ; noms, identités et scènes de recrutement non définis, à ne pas inventer.
- **Fichiers concernés :** `lore/systeme.md`, `lore/personnages.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `lore/chronologie.md` ; présent registre.

## DEC-079 — Retours temporels, douze activations et Mémoire runique

- **Statut : CANON pour les boucles, signatures, jalons et déclenchement par détresse avant le coup fatal.**
- **Source :** déclarations successives de l'auteur dans `new.txt`, à partir de « Idée à transmettre à codex : lors de l'activation de la rune temporelle » et « Fin du livre 2 puis début du livre 3 », puis arbitrages de la session du **21 novembre 2026**. Les scènes détaillées de ChatGPT restent des propositions, pas des chapitres validés.
- **Frontière I/II :** le livre I s'achève sur **l'activation de la Rune temporelle, les sons et le basculement** après le sacrifice de Zio, Hasol survivante. **Le réveil ouvre le livre II**, exactement **une semaine avant la Révélation** ; ce repère s'applique à chaque retour.
- **Comptage :** vie 1 = livre I ; **R1 à R11 = vies totales 2 à 12**, livre II ; **vie 13 = livre III**. Douze activations au total : activation n = **12 DONG puis n DING**. La première mène à R1 ; la fin de Rk correspond à l'activation k+1. La dernière, à la fin de R11, comporte **12 DONG + 12 DING** et la rune est définitivement détruite, réduite en poussière.
- **Visuel :** horloge runique avec sablier ; progression à chaque DONG et à chaque DING. Les variantes d'aiguilles, verrouillage ou décoration proposées dans les réponses ne doivent pas devenir des contraintes supplémentaires non choisies.
- **Déclencheur narratif :** instabilité émotionnelle de l'hôte après les drames, notification puis activation. **Clarification directe ultérieure de l'auteur, 21 novembre 2026 :** face à sa propre fin, la détresse d'Hasol déclenche la rune **avant le coup fatal**, notamment en R5. Le récit s'attache au dernier instant ; il ne faut pas raconter une mort effective puis un retour déclenché après celle-ci. **Aucun nouveau déclencheur post mortem** : l'instabilité émotionnelle reste le mécanisme. Cette précision remplace les anciennes mentions abrégées de sa « mort » face au démon.
- **Mémoire :** Hasol seule conserve des souvenirs, imparfaits jusqu'en R11 ; flashs et cauchemars sont des fragments vécus, non des prédictions infaillibles. En **R11**, à la bibliothèque, le seuil « l'hôte a lu **plus de 100 000 livres** » débloque **Mémoire runique**, mémoire parfaite. Le souvenir intégral de Zio et du sacrifice de sa première vie provoque le dernier choc et retour. **Cumul des livres entre les vies À DÉFINIR.**
- **Actualisation ciblée — DEC-132 :** cette formulation générale est historique. En vie 2, Hasol n’a aucun souvenir des drames de la première vie. À partir de la vie 3, les fragments sont cumulatifs, incomplets et désordonnés, limités aux drames terminaux vécus depuis la vie 2 jusqu’à la vie précédente. La première vie ne redevient accessible qu’avec Mémoire runique en R11, qui restitue alors toutes les vies.
- **Vie 13 :** Mémoire conservée, souvenirs parfaits des douze vies, rune détruite, aucune nouvelle réinitialisation. Mémoire parfaite n'est pas omniscience : elle ne connaît pas les conséquences inédites des changements qu'elle provoque.
- **Limites :** ne pas imposer onze drames tous différents ; les répétitions sont expressément voulues. Reports d'objets, niveaux, cercles et autres ressources non déduits. Le zéro des compteurs de Croissance vient de DEC-078 ; les jalons de cercles de DEC-057 ne fixent pas les états à chaque réveil.
- **Fichiers concernés :** `lore/systeme.md`, `lore/personnages.md`, `lore/chronologie.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`, `source.md` ; présent registre.

## DEC-080 — Trilogie, conflit familial et trajectoires futures

- **Statut : CANON pour les directions explicites et jalons ci-dessous ; scènes, causalités et découpage détaillé À DÉFINIR.**
- **Source :** déclarations de l'auteur dans `new.txt` sur les drames successifs, « Le livre 2 aura 16 chapitre également », la dernière aventure heureuse avec Zio, Hasol grand-mère et la catastrophe de ses 45 ans ; confirmations ciblées dans la session du **21 novembre 2026**, dont le conflit familial et la composition astrale. Les synthèses de ChatGPT ne sont pas des décisions autonomes.
- **Format :** trilogie ; **seize chapitres pour les livres I et II**, nombre du III à définir. Le II couvre les onze réincarnations ; le III, la treizième et dernière vie. Les titres et sous-découpages proposés dans les réponses ne sont pas validés par ce seul format.
- **Conflit familial, première vie :** père aimant mais fier, très mauvaises relations avec le **Griffon d'Argent** ; il exige l'arrêt de la collaboration sans expliquer sa raison, Hasol défend son indépendance professionnelle. Séparation en colère, pas de réconciliation avant sa mort pendant le voyage commercial lointain. **Origine de l'aversion et cause du décès À DÉFINIR** ; ne pas attribuer sa mort à la guilde ni inventer trahison ou complot. Complète DEC-029/033 sans effacer l'affection.
- **R1/R2/R3 :** Ray meurt du poison d'un raid académique en R1, puis en R2 malgré sa présence plus précoce dans l'équipe et la participation d'Hasol au raid. Les cauchemars deviennent plus précis et permettent son **sauvetage en R3**. Le sauvetage ne déclenche pas à lui seul un nouveau retour ; **drame de fin de R3 à définir**. Poison, responsable éventuel et circonstances matérielles restent inconnus. Le potentiel moyen de ce Ray ne remplace pas le prodige du livre I dans toutes les vies.
- **R4/R5 :** R4, père mort lors du même voyage malgré une relation heureuse et Hasol interne à la plus prestigieuse Académie du monde ; R5, cauchemars puis père convaincu de renoncer au voyage et sauvé. Face au démon **vers 34 ans en R5**, Hasol est trop faible et sa détresse déclenche la rune **avant le coup fatal** (DEC-079 clarifiée), pas après une mort effective. Le mot « quatrième vie » dans l'échange est harmonisé comme **R4, vie totale 5**, pas comme une renumérotation de l'arc de Ray.
- **Après R5 :** amélioration progressive face au démon puis victoire dans une réincarnation encore non numérotée. Dans une vie ultérieure victorieuse, Hasol apprend à **45 ans** la mort de **Yoon et Zio**, célèbres aventuriers, lors d'un raid en donjon où Zio a tenté de protéger sa sœur ; le choc provoque des flashs et un retour. Ne pas inventer le raid, son responsable, le numéro de vie ou les drames intermédiaires ; ne pas faire de l'absence de romance la cause de leur décès.
- **Équipe des nouvelles vies :** **Samia ne rejoint plus l'équipe principale**, sans disparaître automatiquement du récit. Œil et Main couvrent les fonctions d'exploration (DEC-078). Les quatre Hasol Astrale/Yoon Rare/Zio Rare/Ray Commun réunis représentent **4/5 membres et 50/50 points** ; cette référence n'impose pas leur recrutement dans chaque vie. Aucun relèvement du plafond.
- **Livre III :** prologue avec Hasol **grand-mère**, célèbre pour sa classe astrale, racontant sa vie à la demande de son petit-fils pour endormir ses petits-enfants. Récit principal de sa dernière vie ensuite ; bonheur durable avec **Zio vivant, mariage, enfants et petits-enfants**. Leur relation doit être reconstruite, Zio n'ayant pas ses souvenirs. Nombre, noms, âges de la descendance et détails de la scène **À DÉFINIR** ; l'extrait rédigé par ChatGPT n'est pas automatiquement approuvé.
- **Enjeu du III :** grâce à Mémoire, Hasol déduit dès le début qu'une **catastrophe mondiale menace l'année de ses 45 ans** et prépare sa vie pour sauver le monde et ses proches. Ce danger ne remplace pas le dénouement du livre I vers 34 ans. Nature, origine, responsable, indices précis et lien éventuel avec le démon **À DÉFINIR**, sans causalité inventée à partir de la mort des Notos. La conclusion heureuse est retenue, pas les solutions détaillées proposées pour y parvenir.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/pistes.md`, `lore/systeme.md`, `AGENTS.md`, `source.md` ; présent registre. Aucun chapitre futur autorisé à la rédaction par le seul enregistrement.

## DEC-081 — Invocations infinies : stratégie des livres II et III

- **Statut : CANON pour le mécanisme, l'admissibilité, le coefficient d'XP et l'importance narrative ; gains exacts À DÉFINIR.**
- **Source :** précisions directes de l'auteur dans la session du 21 novembre 2026 : « les invocations compte pour croissance runique, mais donne 2 fois moins d'xp qu'un monstre classique », puis « rendre d'autant plus important d'exploité le dj avec les invocations infi dans le livre II et III ».
- **Décision générale :** les monstres invoqués alimentent le compteur de monstres de Croissance runique sous ses conditions habituelles d'élimination personnelle et de niveau admissible. Leur XP vaut **50 % de celle d'un monstre classique comparable (×0,5)** ; cela ne fixe pas une table générale d'XP.
- **Donjon de DEC-039/040 :** le boss niveau 32 produit des **invocations niveau 11 en nombre infini tant que le piège reste actif et le boss en vie**. L'infinité de production est désormais explicitement voulue, pas une limite laissée ouverte. Ne pas inventer de quota fini, d'épuisement du stock ou de plafond anti-farm pour neutraliser cette stratégie.
- **Direction narrative :** l'exploitation de ce donjon constitue un **levier majeur de progression dans les livres II et III**. La demi-XP renforce l'intérêt de gagner des cercles sans confondre le compteur d'éliminations et l'XP. Elle ne garantit pas une progression de niveaux négligeable : seuils d'XP et quantité effectivement obtenue restent inconnus. Au II, la mémoire imparfaite subsiste ; au III, sa mémoire parfaite permet de préparer l'exploitation sans rendre le combat gratuit.
- **Conditions maintenues :** les invocations niveau 11 sont admissibles avec Hasol niveau 10 à 29, pas à partir de 30 selon les seuils actuels. Fonctionnement de Croissance astrale avant 10 à préciser. Minimum trois membres en donjon, éliminations personnelles, Mana, fatigue, blessures et ressources ne sont pas annulés par le stock infini. Aucune entrée solitaire ou sécurité absolue déduite de Main runique.
- **Compteurs distincts :** les invocations niveau 11 ne sont pas elles-mêmes des boss ; elles ne créditent pas le compteur des cent boss. Le maintien du piège actif ne donne pas plusieurs victoires contre l'invocateur.
- **À DÉFINIR :** moment d'exploitation dans chaque livre et chaque vie, nombre effectif d'éliminations et cercles obtenus, débit d'invocation, XP de base, partage et arrondis, ressources et risque concret. Ne pas inventer de coefficient compensatoire, arrêt volontaire de l'XP ou pouvoir supprimant les seuils d'admissibilité.
- **Remplace :** les attentes de coefficient d'XP et de limite quantitative de production dans DEC-039/040 ; les autres inconnues de ces scènes subsistent. Ne pas attribuer dès maintenant de gains à des scènes non rédigées.
- **Fichiers concernés :** `lore/systeme.md`, `PLAN_DIRECTEUR.md`, `lore/chronologie.md`, `lore/personnages.md`, `lore/pistes.md`, `AGENTS.md`, `source.md` ; présent registre. Aucun chapitre futur rédigé.

## DEC-082 — Donjon convoité au livre II, privatisation recherchée au III

- **Statut : CANON pour les difficultés du II et l'objectif du III ; modalités et résultat À DÉFINIR.**
- **Source :** précision directe de l'auteur dans la session du 21 novembre 2026 : « dans le livre II, elle rencontrera des difficulté a maintenir le dj actif car d'autre groupe la gene et tue le boss, elle fera alors tous dans le livre III pour privatiser ce dj ».
- **Livre II :** d'autres groupes gênent l'exploitation d'Hasol et tuent le boss invocateur, interrompant ainsi la production entretenue par le piège. L'infinité des invocations n'est pas une exclusivité d'accès ni une garantie de maintien de la source. Ne pas inventer l'identité des groupes, leur connaissance de sa stratégie, une intention hostile ou des sabotages organisés.
- **Livre III :** forte de cette expérience, Hasol fait tout pour **privatiser le donjon** afin de sécuriser son accès et la continuité d'exploitation. Il s'agit d'un objectif majeur de préparation et de ressources, pas d'une propriété déjà acquise ni d'une réussite automatique. Cet objectif ne fixe pas l'ordre de tous ses autres projets.
- **À DÉFINIR :** autorité compétente, statut foncier ou règles d'accès, achat éventuel, concession, accord ou autre moyen, coût, calendrier, légitimité, exclusivité effective et résultat. Ne pas supposer que richesse, célébrité, Main runique ou titre astral donnent automatiquement un droit de propriété ou de fermeture.
- **Préservé :** conditions de DEC-081 (boss vivant, piège actif, XP ×0,5, éliminations admissibles, coûts et effectif). Mort du boss = fin de cette production ; réapparition du boss, réinitialisation ou nouvelle ouverture du donjon ne sont pas définies. Ne pas inventer une destruction définitive du donjon ou un calendrier de réapparition.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/chronologie.md`, `lore/personnages.md`, `lore/systeme.md`, `lore/pistes.md`, `AGENTS.md`, `source.md` ; présent registre. Aucun chapitre futur rédigé.

## DEC-083 — Direction humaine de la trilogie et vigilance sur les boucles

- **Statut : CANON pour les orientations éditoriales ; mise en scène détaillée À DÉFINIR.**
- **Source :** avis sur la direction de l’œuvre puis approbation explicite de l’auteur le 21 novembre 2026 : « je suis totalement d'accord , stocker cette conversation , l'écriture de la suite devra en tenir compte ». Échange conservé dans `lore/conversation_direction_oeuvre_2026-11-21.md`.
- **Boussole thématique :** livre I, trouver sa valeur et sa place ; livre II, éprouver les limites de la réussite et de la puissance face aux pertes ; livre III, construire une vie heureuse sans nouvelle chance temporelle. Ces axes guident l’écriture sans remplacer les événements validés ni imposer des titres.
- **Priorité humaine :** la progression chiffrée soutient le récit mais ne mesure ni la valeur personnelle ni le bonheur. Donner du poids aux années vécues, aux émotions, aux responsabilités et aux choix des compagnons plutôt qu’ajouter des pouvoirs, catastrophes ou retournements pour entretenir seuls l’intérêt.
- **Artisanat :** préserver sa valeur propre dans l’identité d’Hasol. Son métier, sa compétence et ses liens constituent déjà un accomplissement avant le sort offensif du niveau 40 ; celui-ci ne transforme pas rétrospectivement l’artisanat en simple attente de sa « vraie » vocation.
- **Livre II :** différencier les boucles par leurs effets intérieurs sur Hasol, pas seulement par leurs drames terminaux. Moduler le développement des vies ; éviter de répéter intégralement réveil, recrutement et équipement. Préserver les onze réincarnations, les seize chapitres et les répétitions expressément voulues, notamment les morts de Ray. Montrer aussi le bonheur, le travail et les liens réellement vécus : une vie interrompue n’est pas un simple essai sans valeur.
- **Puissance et obstacles :** ne pas neutraliser artificiellement les avantages validés d’Hasol. Déplacer les enjeux vers le temps, la coopération, la confiance, les intérêts divergents et les conséquences imprévues, sans inventer de limitations de système compensatoires. Le donjon peut porter des enjeux d’usage et de légitimité ; aucun conflit particulier ni hostilité des autres groupes n’est validé par cet échange (DEC-082).
- **Autonomie des proches :** chacun doit compter au-delà de sa fonction tactique. Samia reste une personne après sa transmission et hors de l’équipe astrale ; Yoon conserve sa trajectoire ; la coopération de Ray ne vaut pas pardon instantané. Les souvenirs conjugaux d’Hasol ne lui donnent aucun droit sur le Zio des nouvelles vies : choix et amour réciproques doivent se reconstruire.
- **Livre III :** assumer le prologue familial heureux déjà validé. L’intérêt repose sur la façon de construire ce bonheur et de résoudre la crise, pas uniquement sur l’incertitude de survie du couple. Mémoire parfaite ne signifie ni omniscience ni maîtrise des personnes et des conséquences nouvelles.
- **Limites :** aucune révision rétroactive, scène nouvelle, modification du système ou autorisation de rédiger le chapitre suivant. Les paramètres ouverts le restent ; l’appréciation critique archivée n’est pas une validation littéraire globale du manuscrit.
- **Fichiers concernés :** `lore/conversation_direction_oeuvre_2026-11-21.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md` et présent registre. Manuscrit inchangé.

## DEC-084 — Nouveaux personnages introduits au livre II et repris au livre III

- **Statut : CANON pour l’intention narrative ; nombre exact et détails À DÉFINIR.**
- **Source :** déclaration directe de l’auteur le 21 novembre 2026 : « dans les livre II je compte inclure 3 - 4 nouveau personnages qui seront repris dans le livre 3 », suivie de « stocker l'information ».
- **Décision :** introduire **trois à quatre nouveaux personnages au livre II**, puis les reprendre au **livre III**.
- **Répartition approuvée :** à la question proposant des compagnons proches d’Hasol, des alliés extérieurs ou un mélange des deux, l’auteur répond « melange des deux ». Ces nouveaux personnages comprendront donc **des compagnons proches et des alliés extérieurs**, sans répartition chiffrée ni domaine d’activité fixé.
- **À DÉFINIR :** nombre exact, identités, personnalités, rôles, relations, vies et moments d’introduction, place et trajectoires au livre III.
- **Limites :** aucune intégration automatique à l’équipe principale ni modification des plafonds de membres ou de points. Les suggestions de l’assistant sur leurs fonctions, leur introduction progressive ou l’asymétrie des souvenirs ne constituent pas des décisions supplémentaires de l’auteur. Aucun personnage ou événement inventé pour compléter cette intention ; aucune autorisation de rédaction nouvelle.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md` et présent registre. Manuscrit inchangé.

## DEC-085 — Antagonistes supplémentaires : piste à développer

- **Statut : PROPOSITION de l’auteur ; conception À DÉFINIR.**
- **Source :** échange du 21 novembre 2026 : « il faudra des antagoniste aussi je pense », puis, à la question de leur inclusion parmi les trois à quatre nouveaux personnages ou en supplément : « en supplement , pour te dire c'est pas encore fixe dans ma tete ». L’auteur demande ensuite la mise à jour de la documentation.
- **Piste retenue pour discussion :** envisager des antagonistes **en supplément** des trois à quatre compagnons proches et alliés extérieurs prévus par DEC-084. Ne pas les décompter de ce groupe.
- **À DÉFINIR :** confirmation et développement de cette piste, nombre, identités, motivations, moyens, liens avec Hasol, livres et moments d’apparition, éventuelle continuité entre les livres II et III et issues de leurs trajectoires.
- **Limites :** ne pas transformer cette intention encore hésitante en intrigue canonique. Les idées de l’assistant (opposition humaine, intérêts légitimes ou malveillance, réputation, alliances, imprévisibilité malgré les souvenirs) restent des **PROPOSITIONS**, pas des caractéristiques approuvées. Aucun antagoniste précis, complot commun, responsable des drames ou conflit autour du donjon n’est validé ; DEC-082 reste inchangée. Aucune autorisation de rédaction nouvelle.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/pistes.md` et présent registre. Manuscrit inchangé.

## DEC-086 — Armin Shun, Iseria Astrea et soins de Terre

- **Statut : CANON pour les identités et le profil maternel ; CANON pour l’origine supposée des Astrea, pas pour sa véracité ; statistiques et sorts choisis dans la délégation de l’auteur. Autres détails À DÉFINIR.**
- **Source :** déclaration directe du 21 novembre 2026 : « pere de hasol --> Armin Shun ; mere de hasol Iseria Astrea non d'epoux Shun ; Astrea est une fammille perdu dont un des ancien heros astral en serait le fondateur ; pas besoin de developper les stats du pere pour la mere elle des stats de soigneuse pure je te laissse choisir les sort et stats , element terre ».
- **Identités :** père **Armin Shun** ; mère **Iseria Astrea**, nom d’épouse **Shun**. Ne pas créer deux personnages pour ses deux noms.
- **Astrea :** famille perdue dont un ancien héros astral **serait** le fondateur. Conserver le conditionnel. Identité du héros, histoire, sens précis de « perdue », preuves, connaissances des personnages et moment de révélation **À DÉFINIR**. Ni disparition de tous les autres membres, ni statut de dernière survivante, ni hérédité astrale ou origine des pouvoirs d’Hasol établis.
- **Armin :** ne pas développer ses statistiques ; aucune fiche de combat nécessaire. Les décisions concernant son affection, son conflit avec le Griffon d’Argent et son décès restent inchangées.
- **Iseria :** soigneuse pure d’élément **Terre**. L’auteur délègue le choix de ses sorts et statistiques, pas la définition automatique de sa rareté, de son niveau courant, de ses cercles ou de son histoire.
- **Choix délégué — statistiques naturelles de référence au niveau 60 :** PV **9 600**, Attaque **310**, Défense **680**, Vitesse **108**, Mana **1 000**, Puissance arcanique **600**, hors runes, ensembles et effets temporaires. Référence choisie pour rester comparable aux fiches existantes ; ni niveau courant ni progression interpolée.
- **Choix délégué — sorts :** Baume tellurique (premiers secours ciblés), Sève réparatrice (soin ciblé sur la durée), Ancrage vital (stabilisation au contact), Purification des terres (traitement de poison identifié, non universel), Reconstitution tellurique (réparation progressive approfondie), Source nourricière (soin progressif de zone). Fonctions et limites détaillées dans `lore/personnages.md`. Niveaux de déblocage, disponibilité aux dates du récit et paramètres numériques **À DÉFINIR** ; ne pas les inventer lors d’une scène ni réécrire les soins déjà racontés.
- **Limites :** aucun soin de résurrection, régénération de membre, effacement automatique de fatigue ou guérison universelle. Le répertoire ne résout pas par avance l’empoisonnement de Ray au livre II. Terre n’accorde pas de géomancie offensive et ses multiplicateurs d’attaque ne sont pas des bonus de soin.
- **Fichiers concernés :** `lore/personnages.md`, `lore/systeme.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md` et présent registre. Aucun chapitre modifié ou rédigé.

## DEC-087 — Livre III : rapprochement entre classe astrale et origines Astrea

- **Statut : PROPOSITION de l’auteur ; scène et portée À DÉFINIR.**
- **Source :** idée exprimée le 21 novembre 2026 : « j'image une scene dans le livre 3 ou hasol avec sa memoire parfaite fait le lien entre sa classe astral et les origine de la famille de sa mere qui menerai a une piste our resoudre une difficulté ».
- **Piste :** au livre III, la mémoire parfaite d’Hasol lui permettrait de rapprocher sa classe astrale des origines de la famille maternelle Astrea. Ce rapprochement mènerait à une piste susceptible de résoudre une difficulté.
- **À DÉFINIR :** confirmation de la scène, place dans le livre III, souvenirs et indices rapprochés, nature du lien supposé, difficulté concernée, enquête ou actions qui en découlent, résultat et éventuel prix de la résolution.
- **Limites :** mémoire parfaite des faits vécus n’est ni omniscience ni révélation de faits jamais connus. Aucun lien causal entre ascendance et classe, transmission héréditaire, identité du fondateur ou origine des pouvoirs d’Hasol n’est confirmé. Le héros astral reste un fondateur supposé selon DEC-086. La difficulté n’est pas automatiquement la catastrophe mondiale, et une piste n’est pas une solution garantie. Ne pas anticiper cette déduction au livre I ni donner aux personnages un savoir non établi.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/pistes.md` et présent registre. Aucun chapitre rédigé ou modifié.

## DEC-088 — Apparences et repères d’âge des personnages du livre I

- **Statut : CANON pour les précisions explicites et les traits déjà racontés ; détails manquants À DÉFINIR ; raccord des cheveux de Ray résolu par l’arbitrage final.**
- **Source :** précisions directes du 21 novembre 2026 : « zio a deja des descriptions dans des chapitre pour l'apparance ; il faut rester raccord ; yoon cheveux violet vers le rose yeux comme son frere ; samia blonde yeux bleu forme parfaite , tres tres belle ; Armin a eu hasol a 26ans et iseria en avait 20 ; orven a 52 ans », puis « ray cheveux gris , yeux noir avec des lunettes , moins costaux que zio ».
- **Zio :** préserver les descriptions existantes. Au chapitre 5, section I : cheveux sombres soigneusement attachés, silhouette élancée, aisance sous l’équipement et grand bouclier dans le dos. Au chapitre 1 : voix grave et posée, épée et imposant bouclier. Plus costaud que Ray ne signifie pas carrure massive.
- **Yoon :** cheveux violets tirant vers le rose ; même couleur d’yeux que Zio. Teinte exacte **À DÉFINIR**, non retrouvée explicitement dans le manuscrit local ; ne pas la choisir arbitrairement.
- **Samia :** blonde, yeux bleus, très grande beauté et formes harmonieuses (l’auteur dit « forme parfaite »). Aucun tempérament ou lien amoureux déduit.
- **Ray — arbitrage final :** cheveux **sombres**, yeux noirs, lunettes, moins costaud que Zio. L’auteur avait d’abord indiqué des cheveux gris ; après signalement des cheveux sombres déjà racontés au chapitre 1, section VII, il précise « tu peux garde cheveux sombre en soit ». **Raccord résolu :** conserver les cheveux sombres pour toute la continuité, abandonner l’option grise sans inventer de transformation et sans retoucher le manuscrit.
- **Parents :** Armin **26 ans**, Iseria **20 ans**, à la naissance d’Hasol ; environ 42/36 ans à ses seize ans, 45/39 à ses dix-neuf ans, selon les anniversaires non fixés. Âge au décès d’Armin dépendant du calendrier encore ouvert du chapitre 11.
- **Ray — tenue, précision directe ultérieure :** « ray porte une robe de mage gris foncée ». Retenir une **robe de mage gris foncé** ; aucun bonus, enchantement, matériau ou grade d’équipement fixé par cette description. Aucune scène antérieure réécrite.
- **Orven :** **52 ans**, date de référence **À CONFIRMER** ; ne pas supposer cet âge constant au fil des ellipses.
- **Fichiers concernés :** `lore/personnages.md`, `lore/chronologie.md`, `PLAN_DIRECTEUR.md` et présent registre. Aucun chapitre modifié.

## DEC-089 — Vêtements variés et distinction entre quotidien et combat

- **Statut : CANON pour les habitudes vestimentaires ; détails des tenues À DÉFINIR selon les scènes.**
- **Source :** précision directe de l’auteur du 21 novembre 2026 : « yoon samia , comme hasol change regulierment de tenue et en combat leur tenu change , zio lui dispose d'une armure complete et lors des jours de repos il s'habille en civile avec des tenu qui change ; pareil pour ray qui a sa robe de combat et haille normal au quotidien ».
- **Hasol, Yoon et Samia :** vêtements quotidiens régulièrement renouvelés et tenues distinctes pour le combat ; ne pas les figer dans une tenue unique.
- **Zio :** armure complète de combat ; tenues civiles variées pendant le repos et la vie quotidienne. Cette précision complète ses descriptions existantes sans les remplacer ni lui imposer l’armure dans toutes les scènes.
- **Ray :** robe de mage gris foncé pour combattre ; vêtements ordinaires variés au quotidien. Précise l’usage de la robe fixée par DEC-088, sans en changer la couleur.
- **Iseria — complément direct de l’auteur :** « la mere de hasol porte tous le temps des robe de type elfique ». Elle porte toujours des **robes de style elfique**. Il s’agit d’un style constant, pas d’une robe unique ni d’une ascendance elfique établie ; couleurs, matières, coupes et éventuelles propriétés non fixées.
- **Iseria — qualité des robes et statut, précision directe :** « les robes sont de haut de gamme , comme celle reservé a la noblesse pourtant elle ne dispose pas de rang en tant que femme shun ». Ses robes sont haut de gamme, comparables aux tenues réservées à la noblesse ; elle n’a pas de rang nobiliaire en tant qu’épouse Shun. Cette opposition visuelle et sociale est **CANON** ; aucun titre natal Astrea, ancien privilège, droit vestimentaire, provenance des robes ou motif caché n’est établi. Le mot « réservées » ne suffit pas à définir une interdiction légale ni une transgression.
- **Armin — complément direct de l’auteur :** « son pere lui porte des tenue d'homme d'affaire ». Armin Shun porte des **tenues d’homme d’affaires**, en cohérence avec son activité commerciale ; coupes, couleurs et matières non fixées, sans costume moderne automatiquement importé dans la fantasy.
- **Limites :** aucun inventaire exhaustif de vêtements, aucune pièce, matière, protection chiffrée, propriété magique ou variation d’équipement runique déduits. Pas de changement automatique d’apparence physique, de caractère ou de statistiques selon les tenues. Aucun chapitre réécrit.
- **Fichiers concernés :** `lore/personnages.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md` et présent registre.

## DEC-090 — Conflit d’Armin avec le Griffon : maintenir le lecteur aux côtés d’Hasol

- **Statut : CANON pour le choix de focalisation ; cause du différend et connaissances d’Iseria À DÉFINIR.**
- **Source :** réponse directe de l’auteur le 21 novembre 2026 à la question sur l’hostilité d’Armin et le savoir d’Iseria : « j'aimé bien que le lecteur ne le sache pas ça permet d'etre dans le meme etat d'esprit d'hasol qui trouve injuste la situation ».
- **Décision :** ne pas révéler au lecteur les raisons de l’hostilité d’Armin envers le Griffon d’Argent dans le traitement de ce conflit au livre I. Maintenir le lecteur dans la même incertitude qu’Hasol, qui perçoit l’exigence de son père comme injuste et non justifiée.
- **Application :** pas de scène explicative entre les parents, de monologue intérieur révélateur d’Armin ou d’Iseria, ni de commentaire omniscient donnant au lecteur une explication refusée à Hasol. Montrer les réactions et le refus d’expliquer sans inventer d’indices désignant un complot ou une faute de la guilde.
- **Limites :** le sentiment d’injustice d’Hasol n’établit ni qu’Armin a objectivement tort ni qu’il a secrètement raison. La cause réelle et ce qu’Iseria en sait restent ouverts ; ne pas affirmer qu’elle sait ou ignore. Ces inconnues ne bloquent pas l’écriture du conflit dès lors qu’aucune scène ne les tranche implicitement. Aucun lien causal entre guilde, voyage et décès, aucune révélation ultérieure ou résolution obligatoire du mystère validés.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `AGENTS.md` et présent registre. Aucun chapitre modifié ou rédigé.

## DEC-091 — Retrait des repères du lore et préférence pour une partie finale

- **Statut : CANON pour le retrait des encadrés ; contenu de la partie finale À DÉFINIR.**
- **Source :** dernière demande directe de l’auteur dans `new.txt`, ligne 51618 au relevé du 22 novembre 2026 : « je n'ai pas aimé finalement avoir du lore au debut et fin de chapitre je refere limite avoir à la fin du livre une partie lore que lecteure peut consulter quand il veut ».
- **Décision :** remplace uniquement la demande d’encadrés éditoriaux de DEC-072. Retirer les repères d’ouverture et de clôture des chapitres ; conserver toutes les véritables fenêtres du système et le texte narratif.
- **Application :** dix encadrés retirés des chapitres 5 à 9 de `roman.md`, huit des propositions séparées des chapitres 1 à 4. Les chapitres 1 à 4 du manuscrit restent intacts, les brouillons sont conservés et les audits gardent les anciens décomptes comme historique.
- **Orientation :** privilégier une partie de lore en fin de livre, consultable librement. Aucun contenu d’annexe rédigé par cette opération ; sélection des règles, détail, organisation et gestion des révélations restent à définir. Aucune nouvelle règle canonisée ni autorisation de rédaction de la suite déduite.
- **Fichiers concernés :** `roman.md`, `chap1_revision.md` à `chap4_revision.md`, `AGENTS.md`, `source.md`, audits des chapitres 1 à 4 et 5 à 9, présent registre.

## DEC-092 — Reprise partielle des activités commerciales d’Armin

- **Statut : CANON pour la responsabilité et son effet sur la disponibilité ; modalités À DÉFINIR.**
- **Source :** demande directe de l’auteur dans `new.txt`, ligne 47053 au relevé du 22 novembre 2026 : « J aimerai inclure qu’elle a repris une partie des activité de so père ». L’auteur relie explicitement cette charge au retard de niveau d’Hasol malgré sa détermination de farmeuse, en plus des exigences de sa classe légendaire.
- **Décision :** après la mort d’Armin, Hasol reprend **une partie**, et non automatiquement la totalité, de ses activités commerciales. Ses responsabilités réduisent le temps disponible pour la chasse et contribuent à son décalage de niveau avec ses alliés ; elle reste très travailleuse et déterminée à suivre son groupe.
- **Placement :** préparation du chapitre 12, après le décès prévu au chapitre 11. Ce futur validé ne devient pas un événement déjà raconté dans le manuscrit local, qui s’arrête au chapitre 9 au moment de cette synchronisation.
- **Limites :** aucun montant, niveau, contrat précis, répartition des tâches, régime d’héritage ou pouvoir juridique n’est fixé. Les détails proposés ensuite par ChatGPT (fournisseurs, négociations, délégation aux employés, scènes et revenus) ne sont pas validés séparément par la seule demande. Ne pas supprimer l’artisanat, la chasse ni le ralentissement des cercles de DEC-032.
- **Fichiers concernés :** `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/chronologie.md`, présent registre ; provenance et réserves dans `lore/audit_transmission_chapitres_10_12.md`. Aucun chapitre réécrit.

## DEC-093 — Réception des chapitres 10 à 12 : intégration suspendue pour arbitrage

- **Statut : HISTORIQUE de réception et de suspension ; blocages du livre I désormais levés par DEC-097 à DEC-100.** Les nouvelles classes des vies futures restent non validées et ne bloquent pas le livre I. Les constats ci-dessous décrivent le contrôle initial, pas l’état d’avancement de l’import effectif. Aucune validation littéraire globale des textes 10 à 12 ; révisions 1 à 4 approuvées séparément par DEC-101.
- **Source :** actualisation de `new.txt` signalée par l’auteur ; tranche nouvelle 36601–51621 intégralement lue. Repères : chapitre 10 V2, 37170–41766 ; correction de fiche proposée, 41768–41848 ; chapitre 11, 41855–46997 ; chapitre 12, 47100–51614. Numéros valables pour ce relevé, non identifiants immuables.
- **Contradiction historique, résolue par DEC-097 le 22 novembre 2026 :** les nouveaux textes prévoyaient un résultat exact à +15 pour Hasol, contre les maxima accessibles non garantis de DEC-076. Lors de la réception, la synthèse de ChatGPT ne suffisait pas à révoquer cet arbitrage. L’auteur a depuis choisi explicitement le résultat final exact personnel d’Hasol ; ce seul blocage est levé, sans approbation des autres propositions ni intégration narrative.
- **Affixes critiques — résolu par DEC-098 :** retrait des principales et secondaires CC/DCC confirmé directement par l’auteur ; formules critiques inchangées.
- **Autres arbitrages :** tables de Puissance arcanique, plafond des ensembles de quatre pièces, fiches de runes dont secondaire Attaque en pourcentage et nouvelles classes des vies suivantes. Ces propositions ne deviennent pas canoniques par la seule présence d’un récapitulatif de ChatGPT. Détails, bornes et questions dans l’audit dédié.
- **Textes :** aucune seconde version du chapitre 10, aucun chapitre 11 ou 12 ne sont ajoutés au manuscrit pendant ce contrôle. Les trois textes restent intégralement disponibles dans `new.txt`. La phrase de ChatGPT « On considère donc le chapitre 11 […] comme validé » (47013) n’est pas assimilée à une validation explicite de l’auteur.
- **Préservation :** chapitres 1 à 9, `new.txt`, `old.txt` et références visuelles non modifiés par cette opération ; pas de publication. La décision indépendante DEC-092 est synchronisée sans importer les développements non arbitrés. La demande sur les repères du lore est traitée séparément.

## DEC-094 — Nom de plume de l’auteur

- **Statut : HISTORIQUE — remplacé pour le nom seulement par DEC-096.**
- **Source :** message direct de l’auteur, session du 22 novembre 2026 : « Nom de plume: Myoshi Twin ».
- **Décision :** consigner le nom de plume exact **Myoshi Twin** dans la présentation du projet.
- **Limites :** aucune recherche de disponibilité ni vérification de protection juridique effectuée ; ce choix ne modifie ni les identités Git ni la licence et n’autorise aucune publication.
- **Fichiers concernés :** `README.md` et présent registre. Manuscrit et archives inchangés.

## DEC-095 — Notice de droits réservés sur les textes originaux

- **Statut : CANON pour le choix de la notice ; attribution remplacée pour le nom seulement par DEC-096.**
- **Source :** accord direct de l’auteur, session du 22 novembre 2026 : « ok ajoute la », après proposition d’une notice de droits réservés et d’une mention courte dans le README.
- **Décision :** ajouter `COPYRIGHT.md` avec la mention « © 2026 Myoshi Twin — Tous droits réservés. » et les restrictions approuvées sur la reproduction, la redistribution, la traduction et l’adaptation des textes originaux, sauf autorisation préalable ou exception prévue par la loi. Ajouter un renvoi dans le README ; il s’agit d’une notice, pas d’une licence ouverte.
- **Portée et limites :** textes originaux du projet uniquement ; les éléments appartenant à des tiers restent soumis aux droits de leurs titulaires. Aucune propriété des visuels ni garantie contre la copie n’est affirmée. Aucune licence MIT ou Creative Commons ajoutée, aucune identité civile ou coordonnée déduite, aucune publication autorisée par cet accord.
- **Fichiers concernés :** `COPYRIGHT.md`, `README.md` et présent registre. Manuscrit, archives, images et configuration Git inchangés.

## DEC-096 — Nom réel de l’auteur et attribution de la notice

- **Statut : CANON pour le nom d’auteur Joris VIAL.**
- **Source :** message direct de l’auteur, session du 22 novembre 2026 : « Hum c'est dans mon github a mon nom réel donc autant mettre Joris VIAL directement ».
- **Décision :** utiliser le nom réel exact **Joris VIAL** dans `README.md`, sous le libellé « Auteur » et non « Nom de plume », et dans l’attribution de la notice : « © 2026 Joris VIAL — Tous droits réservés. ».
- **Remplacement limité :** remplace DEC-094 et l’attribution de DEC-095 pour le nom seulement. Ces décisions restent conservées comme historique ; la notice de droits réservés et ses conditions approuvées restent inchangées, sauf le nom attribué.
- **Limites :** aucun changement d’identité Git, aucune publication, aucun commit ni push autorisé par cette décision. Manuscrit, archives et visuels inchangés.
- **Fichiers concernés :** `README.md`, `COPYRIGHT.md` et présent registre.

## DEC-097 — Œil runique : résultat final exact à +15 pour Hasol

- **Statut : CANON ; remplace DEC-076 pour la lecture d’Œil seulement et lève ce seul blocage de DEC-093.**
- **Source :** arbitrage direct de l’auteur, session du 22 novembre 2026 : « Version des nouveaux textes : il montre le résultat final exact à +15 si Hasol effectue les améliorations. Les tentatives peuvent toujours échouer et consommer des ressources avant d’y parvenir. »
- **Décision :** Œil révèle le **résultat final exact à +15 si Hasol effectue les améliorations et atteint ce palier**. La prédiction porte sur son résultat personnel, pas sur une simple borne maximale accessible. Les types de secondaires restent prédéterminés et identiques quel que soit l’artisan.
- **Limites :** aucune prédiction des valeurs d’un autre artisan, aucun choix des affixes, aucune garantie de renforcements tous maximaux ni de réussite automatique. L’ordre exact des paliers intermédiaires, les coûts, taux, nombre de tentatives et délais ne sont pas fixés par cet arbitrage ; les paramètres non tranchés restent **À DÉFINIR**. Les tentatives peuvent toujours échouer et consommer des pierres de mana et du Mana personnel.
- **Remplacement limité :** l’ancienne lecture d’Œil aux maxima non garantis de DEC-076 est conservée comme historique. Les autres règles de DEC-076, dont Bénédiction, les formules critiques et le remplacement de Lame, restent intactes. Aucun gain déjà raconté n’est réécrit ; déblocage d’Œil inchangé au niveau 20 dans la première vie et au niveau 1 astral dans les nouvelles vies.
- **Suivi d’intégration actualisé par DEC-098 :** blocages Œil et affixes CC/DCC levés dans DEC-093 et l’audit 10–12 ; tables de PA, plafond d’ensembles, fiches de runes et classes restent à arbitrer. Aucune validation littéraire globale ni intégration des chapitres 10 à 12, aucune modification du manuscrit ou des archives, aucun commit/push.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `README.md`, `source.md`, `lore/systeme.md`, `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md`, `lore/pistes.md`, audits 5–9 et 10–12, présent registre.

## DEC-098 — Retrait des affixes runiques de taux critique et dégâts critiques

- **Statut : CANON ; remplace DEC-004 et DEC-076 pour les affixes CC/DCC seulement.** Le blocage correspondant de DEC-093 est levé ; DEC-097 reste inchangée.
- **Source :** réponse directe de l’auteur, session du 22 novembre 2026 : « oui je confirme » à la question exacte « confirmes-tu le retrait du taux critique et des dégâts critiques des principales et secondaires des runes, comme proposé dans la nouvelle transmission ? ».
- **Décision :** retirer le taux critique (chance critique, CC) et les dégâts critiques (DCC) du catalogue actif des principales et secondaires des runes. Précision et résistance restent admises en pourcentages. Conserver les anciennes tables CC/DCC comme historique remplacé, ainsi que la provenance et les inventaires anciens.
- **Limites :** les coups critiques, les formules existantes de DEC-076, Aura et Infiltration ne sont ni supprimés ni modifiés. Les termes de bonus directs des formules ne réautorisent pas ces affixes runiques. Aucune nouvelle formule, suppression de caractéristiques naturelles, table de PA, secondaire Attaque %, limite d’ensembles ou fiche de rune du chapitre 10 n’est validée par cette réponse.
- **Continuité à reprendre avec autorisation :** anciennes secondaires CC/DCC du butin Vitesse rare (bleu), 3★, +0, chapitre 10, dans le plan et le dossier mobile : statut historique explicité, remplacements À DÉFINIR. Aucun affixe CC/DCC individuel renseigné dans l’inventaire local ; les mentions narratives locales de critiques liés à la PA ne sont pas des affixes à remplacer. Aucun remplacement d’affixes inventé, aucune révision du manuscrit ou des propositions séparées. Les archives restent intactes.
- **Suivi :** Œil et retrait des affixes CC/DCC résolus ; tables de PA, plafond d’ensembles, fiches du chapitre 10 et classes toujours en attente (audit 10–12). Aucun chapitre importé, aucune validation littéraire globale, aucun commit/push.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `README.md`, `source.md`, `lore/systeme.md`, `lore/runes.md`, dossier mobile 10–16, audit 10–12 et présent registre.

## DEC-099 — Barèmes de PA runique et plafond des ensembles de quatre pièces

- **Statut : CANON — choix de l’assistant dans la délégation explicite de l’auteur, le 22 novembre 2026.** Lève les blocages PA/ensembles de DEC-093 ; ne valide pas globalement les textes 10 à 12.
- **Source :** réponses directes de l’auteur « reflechi aux valeur les plus pertinantes je te fais confiance » et « voir la precedente question, tu decides ». Les valeurs retenues par l’assistant sont consignées ci-dessous ; elles ne proviennent pas d’une adoption intégrale d’un guide externe.
- **Principale PA fixe, bornes +0 → +15 :** 1★ **10 → 40** ; 2★ **20 → 75** ; 3★ **30 → 150** ; 4★ **40 → 300** ; 5★ **50 → 600** ; 6★ **70 → 1 200**. Pas de PA en pourcentage. Aucune courbe chiffrée +1 à +14 n’est fixée ; conserver l’augmentation à chaque réussite et le gain renforcé à +15 de DEC-014.
- **Secondaire PA :** renforcements **+20, +40 ou +60**, cumulables sur la même secondaire selon les paliers ordinaires. Aucune probabilité ni modulation selon les étoiles n’est définie. Une valeur native +60 n’est pas universelle ; les fiches individuelles restent distinctes.
- **Ensembles :** au plus **deux activations de chaque type d’ensemble de quatre pièces par porteur**. Les principales et secondaires individuelles restent actives sur toutes les runes équipées, même au-delà de ce plafond. Les ensembles de deux pièces n’ont pas de plafond propre ; conserver leur cumul additif existant (deux Gardien = +30 % Défense). Aucune nouvelle assiette ni règle d’arrondi n’est adoptée.
- **Continuité :** pas d’impact sur les états des chapitres 1 à 9 audités ; ne pas inventer les principales intermédiaires de HAS-R011 à HAS-R014. PA naturelle hors runes, bonus runiques et effets temporaires restent séparés.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/runes.md`, audit 10–12, `source.md` et présent registre.

## DEC-100 — Deux fiches du chapitre 10 et secondaire Attaque %

- **Statut : CANON — confirmation directe des deux fiches par l’auteur, le 22 novembre 2026, via le questionnaire de la session.** Lève le blocage des fiches de DEC-093, sans validation littéraire globale des chapitres 10 à 12.
- **Vitesse rare (bleue), 3★, +0 :** principale **Vitesse +3** ; deux secondaires **Attaque +8 %** et **PA +60**. Cette confirmation admet **Attaque % en secondaire**, sans valider PV % ni Défense % en secondaires. Les anciens affixes CC/DCC du plan sont historiques, pas une transformation vécue de la rune. La projection complète à +15 n’est pas chiffrée par cette décision.
- **Énergie légendaire (orange), 4★, +9 d’Iseria :** principale **PV +25 %**, projection **+43 % à +15** ; secondaires **PA +60**, **Vitesse +4**, **Défense +30**, **Mana +20**. Projection personnelle d’Hasol : **PA +140** à +15, soit +20 et +60 supplémentaires, **ordre à +12/+15 inconnu** ; les trois autres secondaires restent inchangées.
- **Prêt :** rune examinée puis rendue intacte, **aucune amélioration effectuée**. +15 et PA +140 sont des projections conditionnelles, pas l’état réel de la pièce. La principale PV 4★ à +15 = 43 % est la fiche expressément approuvée ; elle ne suffit pas à créer une table générale ni une courbe intermédiaire.
- **Suivi :** fiches consignées séparément de l’état courant de fin du chapitre 9 en attendant confirmation de l’intégration. Aucun nouvel ID personnel attribué dans cette synchronisation documentaire ; coordination avec l’intégration requise pour éviter un doublon. Aucun autre inventaire ou changement de règle importé.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/runes.md`, `lore/personnages.md`, dossier mobile et audit 10–12, présent registre.

## DEC-101 — Validation des révisions 1 à 4 sans repères du lore ; roman non illustré

- **Statut : CANON — validation explicite des quatre révisions et choix de présentation, le 22 novembre 2026.** Actualise DEC-072/091, sans effacer leur historique.
- **Source :** « autre info les chapitre revision sont validé mais sans le lore en debut et fin ». Les versions préparées dans `chap1_revision.md` à `chap4_revision.md` sont approuvées toutes les quatre **sans les repères éditoriaux d’ouverture/clôture**. Leur remplacement dans l’unique `roman.md` est autorisé ; conserver les copies de provenance. Les véritables fenêtres du système restent présentes.
- **Illustrations :** l’ajout envisagé d’une image au chapitre 1 est annulé par « quoique non oublie le roman reste du texte », puis « les images seront pour le manhwa ». **Aucune illustration narrative dans le roman** ; cela ne supprime ni les fenêtres HTML du système ni leurs pictogrammes. L’image du couple en tête du README est conservée, distincte du manuscrit. Aucun manhwa n’est produit par cet arbitrage.
- **Limites :** aucune validation littéraire globale des nouveaux chapitres 10 à 12, aucune autorisation de rédaction du chapitre 13 ni de publication. Les changements de classes des vies futures restent non validés et ne bloquent pas le livre I. La chronologie de sortie sera actualisée après confirmation de l’import effectif, pas sur la seule validation ou demande d’intégration.
- **Fichiers concernés :** `AGENTS.md`, `README.md`, `PLAN_DIRECTEUR.md`, `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md`, audits pertinents, `source.md` et présent registre ; intégration du manuscrit suivie séparément.

## DEC-102 — Import effectif des chapitres 1 à 12 et synchronisation de sortie

- **Statut : import local confirmé le 22 novembre 2026 ; chapitres 1 à 9 validés, chapitres 10 V2, 11 et 12 en lecture sans validation littéraire globale.** Actualise le suivi de DEC-093/100/101 ; les suspensions précédentes restent historiques.
- **Source :** confirmation de la session principale et preuves dans `docs/integration_chapitres_1_12.md`. Les narrations approuvées 1–4 étaient déjà celles du manuscrit : deux fenêtres C3-F01/C4-F01 ajoutées, pas de remplacement par un ancien HTML. Les 89 fenêtres modernisées antérieures sont préservées. Textes 10 V2 : `new.txt` 37170–41766 ; 11 : 41855–46997 ; 12 : 47100–51614, hors courriels et commentaires. Les deux fenêtres d’Iseria sont complétées avec DEC-100 ; vingt-deux désignations ciblées sont documentées dans l’audit.
- **État de sortie du texte intégré :** Hasol vient d’avoir **vingt-cinq ans**, artisane reconnue et disposant de moyens financiers considérables ; reprend une partie des activités commerciales d’Armin, mort au 11 sans cause révélée ni réconciliation. Groupe de cinq : Hasol légendaire, Yoon rare, Ray commun, Zio rare, Samia commune, **5/5 et 50/50**. Les niveaux finaux, caractéristiques naturelles, XP, compteurs, réserves et équipement final détaillé restent **À DÉFINIR**, pas remplacés par les fiches de référence au niveau 60.
- **Progression racontée :** Hasol 19→20/Œil après sauvetage au 10, 20→21/Aimant après combat avec l’Anneau au 11 ; fin des études de Yoon et adhésion de Zio au 11 ; fuite puis retour victorieux au boss 32/invocations 11 avec Samia au 12. Main, détection des pièges par Œil, mariage, centième boss et premier sort offensif restent futurs. Aucun gain de cercle ou inventaire intégral +15 inventé.
- **Suivi des pièces :** `HAS-R015`, Vitesse rare (bleue), 3★, +0, propriété d’Hasol attestée et stockée dans son Anneau en fin du 10, toujours non équipée au début du 11 ; devenir ultérieur non établi. `ISE-R001`, Énergie légendaire (orange), 4★, +9, rendue intacte à Iseria au 10 ; projections +15 non réalisées. `ORV-R002`, Énergie d’essai commune (blanche), 1★, +0→+3, devenue peu commune (verte), Mana +10 apparu ; distincte de l’épreuve 2★ du chapitre 3.
- **Présentation :** 110 fenêtres après import éditorial, soit 89 préservées et 21 nouvelles ; modernisation des 21 et régénération/contrôles du lecteur suivis séparément, pas déclarés achevés par cette décision. Baseline de cette seconde passe : `/tmp/opencode/arcaniste-fenetres-20261122/etape-2/roman.avant-refonte.md`, SHA-256 `bd983162161efdb1acd6d2469339b2104cb6d93fc735fd5793722ca0d747cb3b` (preuve temporaire de session).
- **Limites :** aucune nouvelle règle ni classe des vies futures adoptée, aucun chapitre 13 rédigé ou autorisé, aucune illustration narrative. Archives et copies de révision conservées. Aucun commit, push ni déploiement.
- **Fichiers concernés :** `AGENTS.md`, `README.md`, `PLAN_DIRECTEUR.md`, `source.md`, références de `lore/` et audits d’avancement. Manuscrit modifié par l’intervention d’intégration distincte, pas par cette synchronisation documentaire.

## DEC-103 — Fenêtres en couleur dans l’aperçu GitHub du manuscrit

- **Statut : CANON — choix de présentation et délégation technique explicites, le 22 novembre 2026.** Précise DEC-101 sans annuler le roman non illustré ; ne change aucun statut littéraire de DEC-102.
- **Source :** correction de l’auteur « non… fenêtres dans .md… lecture.html ne fonctionne pas depuis github », puis choix « je veux de la couleur, la technique c’est toi qui choisi… depuis preview github » (extraits de la session). La priorité est la lecture de `roman.md` dans l’aperçu GitHub, pas un lecteur HTML externe.
- **Choix technique délégué :** SVG locaux purs dérivés de la source HTML des fenêtres, affichés par `picture` avec variantes bureau/mobile ; transcription textuelle complète dans un `details` dépliable, dans le même `roman.md`. Les classes racines et identifiants restent stables. Aucun SVG inline destiné au rendu GitHub, `foreignObject`, raster incorporé, script, CDN ou police distante. Cette exception concerne exclusivement l’affichage des véritables fenêtres du système ; aucune illustration narrative, notamment au chapitre 1, n’est réautorisée. L’image du couple dans le README est conservée.
- **Motif vérifié :** HTML/CSS permet généralement cette présentation, mais GitHub filtre styles et classes. Le test via l’API Markdown officielle a répondu HTTP 200 avec `<div>Fenêtre de test</div>`, sans styles ; preuve temporaire de session : `/tmp/opencode/arcaniste-github-20261122/test-css-inline.html`. Un second test HTTP 200 conserve `picture`, `source`, `media`, `img`, `details` et `summary` : `/tmp/opencode/github-window-probe.html`. Ces sondes prouvent l’acceptation du balisage testé, pas une validation visuelle sur tous les appareils.
- **Source unique et maintenance :** tout le texte utile et toutes les données restent dans le HTML textuel de `roman.md`. Les SVG de `assets/fenetres/` sont des dérivés régénérables par `scripts/generer_fenetres.py`, pas un canon primaire ni un second manuscrit. Éditer le texte puis régénérer et contrôler `--check` ; ne pas corriger les SVG à la main. Le lecteur local extrait cette même source ; `lecture.html` et `style.css` restent des exports facultatifs pour lecture locale et impression.
- **Limites :** données, narration et octets hors fenêtres inchangés ; aucune règle LitRPG modifiée, aucun chapitre validé par cette présentation, aucune rédaction nouvelle. Inclure tous les SVG dérivés lors d’une publication autorisée, faute de quoi les liens seront cassés. Aucune publication Git, aucun commit/push, aucun déploiement GitHub Pages autorisé ou réalisé par cette décision. Le rendu de documents futurs plus volumineux reste à contrôler selon les limites de GitHub, sans créer automatiquement un second manuscrit.
- **Fichiers concernés :** `roman.md`, dérivés `assets/fenetres/`, générateurs et tests associés pour l’implémentation ; `AGENTS.md`, `README.md`, `docs/fenetres_litrpg.md`, `docs/fenetres_github.md` et présent registre pour le suivi.

## DEC-104 — Références visuelles limitées au design, indépendamment de leurs annotations

- **Statut : CANON — précision explicite de l’auteur, le 22 novembre 2026.** Complète les garde-fous d’apparence de DEC-088/089 sans modifier les anciennes décisions.
- **Source :** demande de l’auteur dans la session : « les références visuelles même si elles comportent du texte ne sont là que pour le design ». L’auteur souhaite des descriptions du roman raccord aux visuels retenus, pas l’import de leurs annotations.
- **Décision :** utiliser ces références pour le design uniquement ; aucun texte inscrit sur une image ne valide à lui seul une identité, une classe, un pouvoir ou une règle. Ray reste un **mage de feu commun** (DEC-036/069) ; ignorer « Arcaniste runique » sur sa planche.
- **Samia :** elle reste **blonde au livre I**. L’auteur annonce un changement de couleur de cheveux dans sa « seconde vie » ; la **couleur exacte est À DÉFINIR**. Cette formulation ne définit aucune mécanique de réincarnation propre à Samia ; ne pas en extrapoler souvenirs, pouvoirs ou parcours.
- **Limites :** aucune réécriture du manuscrit ni modification d’image par cette consignation ; aucune règle de pouvoir modifiée, aucune rédaction nouvelle ou publication autorisée. Les paramètres visuels non confirmés restent à définir plutôt qu’être déduits des annotations.
- **Fichiers concernés :** `AGENTS.md`, `source.md` et présent registre ; raccords descriptifs éventuels suivis séparément.

## DEC-106 — Raccords descriptifs autorisés aux designs retenus

- **Statut : CANON — correction et ajouts ciblés explicitement autorisés le 22 novembre 2026.** Applique DEC-104 et précise DEC-088/089, sans modifier les arbitrages du chapitre 13 consignés par DEC-105.
- **Source :** validation de la recommandation précédente par l’auteur : « je valides fait les changements et ajout ». Périmètre : coiffure de Zio, portraits brefs d’Armin et Iseria au chapitre 1, barbe et lunettes d’Orven dès sa rencontre au chapitre 3.
- **Zio :** cheveux **bruns, coupés court**, en remplacement des cheveux attachés préservés historiquement par DEC-088. Correction au chapitre 5, section I, et des deux reprises de la même incohérence au chapitre 13 (près de Samia et à la cérémonie). Silhouette, équipement, gestes, émotion et déroulement des scènes préservés ; aucun changement de coiffure intermédiaire inventé. DEC-088 est conservée comme historique, supplantée sur ce seul point.
- **Armin :** portrait au registre commercial dans le souvenir des sept ans d’Hasol : mèches brunes, traits nets et veste sombre à col haut bordée de fins galons dorés. Tenue d’affaires fantasy en application de DEC-089, sans costume moderne ni vieillissement artificiel du père dans ce souvenir.
- **Iseria :** portrait auprès d’Hasol à la Révélation : longs cheveux rose pâle, robe claire de coupe elfique aux broderies dorées et au tombé soigné, raccord à la qualité vestimentaire de DEC-089. Aucun titre ou ascendance déduit ; couleurs des yeux non fixées.
- **Vérification visuelle :** références d’Armin et Iseria consultées uniquement sur une planche temporaire réduite de 780 × 600 pixels, dérivée des fichiers de leurs dossiers `references-visuelles/`. Cheveux et vêtements utilisés comme design, pas les textes, ornements ou effets lumineux comme règles, pouvoirs ou statut social.
- **Orven :** lunettes et barbe déjà présentes aux chapitres 6–7, ajoutées dès son introduction au chapitre 3 ; cheveux grisonnants et gestes d’artisan préservés, sans nouvel âge de scène fixé.
- **Limites :** six passages descriptifs uniquement dans `roman.md` ; fenêtres, statistiques, runes, compétences, événements, dialogues et statuts littéraires inchangés. Samia blonde au livre I et Ray mage de feu commun inchangés. Images, archives et copies de révision non modifiées ; aucune rédaction de chapitre nouveau, aucun commit ni push.
- **Fichiers concernés :** `roman.md`, `lore/personnages.md` et présent registre. Les anciennes notices du plan sur les cheveux attachés relèvent désormais de l’historique DEC-088, pas d’un arbitrage concurrent.

## DEC-105 — Chapitre 13 : amour réciproque, mariage et transmission longue

- **Statut : CANON pour les décisions explicites ci-dessous ; rédaction autorisée,
  chapitre intégré comme VERSION DE LECTURE NON VALIDÉE LITTÉRAIREMENT.**
- **Source :** réponses de l’auteur au questionnaire et synthèse, puis « go »
  explicite, transmis dans la mission locale de rédaction du 22 novembre 2026.
  Pas de nouvel apport annoncé dans `new.txt`, pas d’import ou de modification
  de cette archive. DEC-104, ajouté pendant le travail, reste consacré aux références
  visuelles ; le présent identifiant est le suivant disponible.
- **Mariage :** Hasol épouse Zio vers **vingt-huit ans** ; cérémonie intime et fin
  de chapitre dans leur vie commune apaisée. Le texte part de la fin du 12 à
  vingt-cinq ans et de l’expédition prévue dans dix jours. Aucun enfant inventé.
- **Hasol :** la jalousie envers Samia, qui a aussi des vues sur Zio, lui fait
  reconnaître ses sentiments. Pas de rivalité artificielle ou prolongée, pas de
  droit de possession sur Zio ni de faute attribuée à Samia pour ses sentiments.
- **Zio :** coup de foudre secret pour Hasol dès ses premiers jours à l’Académie,
  admiration de sa détermination ; le temps partagé transforme le fantasme ou
  l’engouement adolescent en amour mature. Il fait le premier pas et sa déclaration
  malgré son manque de confiance sentimental. Hasol apprend ce passé en dialogue
  et confidences, pas par omniscience. Aucune romance établie rétroactive ; son
  intervention à l’Académie n’attend aucune récompense ni contrepartie affective.
- **Samia :** comprend rapidement l’amour de Zio pour Hasol et leurs sentiments
  réciproques, renonce à ses sentiments de jeunesse et soutient Zio. Conserve
  autonomie, amitiés, projets et place dans l’équipe après la transmission ; ni
  rivale prolongée, ni simple outil d’apprentissage. Dans la version de lecture,
  développe des exercices d’observation pour d’autres chasseurs ; leur organisation
  est un choix de mise en scène, pas une institution ou règle universelle validée.
- **Yoon :** sœur de Zio et **meilleure amie de Samia**, souhaite qu’Hasol devienne
  sa belle-sœur ; elle n’impose pas les sentiments ou les décisions des autres.
- **Transmission :** apprentissage auprès de Samia sur **plusieurs années**,
  détection des pièges par le **même Œil runique** conservant la lecture des runes,
  puis **Main runique active** pour ouvrir les coffres. Ni détection = désamorçage,
  ni ouverture universelle ou pouvoir astral coffres/portes sans restriction au I.
  Niveaux, coûts, portée, récupération, protections couvertes et conditions
  universelles de déblocage **À DÉFINIR** ; scènes d’acquisition ne valant pas recette.
- **Intégration :** dix sections, environ **10 100 mots** ; deux sources HTML
  `C13-F01` (Œil amélioré) et `C13-F02` (Main). Ajout à `roman.md` uniquement,
  préfixe 1–12 vérifié identique octet pour octet à la copie de début de travail
  (SHA-256 `ad1b690d57563906e9654d4c7d5b15c69da07805448e0b6c18d7efb9e98ba123`).
  Contrôle effectué avant les raccords descriptifs concurrents DEC-106 : il ne
  revendique pas l’identité du préfixe après ces retouches distinctes autorisées.
  Fiche préalable et suivi : `docs/preparation_chapitre_13.md`.
- **Préservé :** chapitres 1–9 validés, 10–12 toujours en lecture ; groupe de cinq,
  50/50 points ; artisanat et responsabilités commerciales d’Hasol, deuil et
  inconnues d’Armin, engagement choisi de Ray. Aucun niveau, XP, fiche naturelle,
  cercle, compteur, butin individuel ou inventaire nouveau chiffré. Pas de fiches
  du 60, pas de total du 9 arbitrairement figé après les ellipses.
- **Suite :** centième boss au **14**, vers le niveau 38, toujours futur ; premier
  sort offensif au **15**, niveau 40, toujours futur. Aucun chapitre 14 autorisé,
  aucune validation littéraire globale du 13, aucun commit/push ou déploiement.
  Génération SVG/enveloppes GitHub et lecteur confiée à la session principale,
  non exécutée pendant cette rédaction.
- **Fichiers concernés :** `roman.md`, `PLAN_DIRECTEUR.md`, `AGENTS.md`,
  `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md`, `lore/systeme.md`,
  présent registre et fiche du chapitre 13. Archives, scripts, styles et SVG non
  modifiés par l’agent de rédaction.

## DEC-107 — Salon des Shun et apprentissage sans anticipation du pouvoir

- **Statut : CANON — corrections ciblées explicitement autorisées le 22 novembre 2026.** Aucune validation littéraire globale du chapitre 13 ni autorisation de rédiger le 14.
- **Source :** l’auteur précise que la famille possède une belle demeure et que son salon n’est pas petit ; il demande également de retirer du passage d’apprentissage auprès de Samia la formulation laissant supposer qu’Hasol attend une évolution de son passif.
- **Demeure :** salon familial spacieux, compatible avec le standing des Shun. « Maison Shun » reste une désignation valable du foyer et des activités familiales ; ni palais, noblesse, plan des pièces ou agrandissement inventés.
- **Audit du manuscrit :** dix mentions du « petit salon » familial corrigées aux chapitres 7, 10, 11, 12 et 13 ; dimension explicitée au 13, adjectif retiré ailleurs. Les deux petits salons du Griffon d’Argent (10 et 11) sont distincts et préservés. Salle d’entraînement, jardins, mobilier, petits objets, souvenirs et images du deuil compatibles conservés.
- **Focalisation :** au chapitre 13, section II, conserver le recul d’Hasol et l’apprentissage concret par les explications, exercices et erreurs corrigées avec Samia, sans attente ni contraste anticipant une nouvelle lecture magique. L’évolution ultérieure d’Œil et l’acquisition de Main restent celles de DEC-105 ; aucune règle de compétence modifiée.
- **Limites :** onze passages du manuscrit seulement ; fenêtres et tous les octets hors de ces substitutions préservés. Aucun niveau, statistique, rune, événement ou relation modifié. Décor architectural détaillé et paramètres non fixés des compétences restent **À DÉFINIR**. Aucun commit ni push.
- **Fichiers concernés :** `roman.md`, `lore/personnages.md` et présent registre.

## DEC-108 — Résidence du couple et suites de la demeure Shun

- **Statut : CANON — précision et raccords ciblés demandés explicitement par l’auteur le 22 novembre 2026.** Aucune validation littéraire globale des chapitres 10–13 ni autorisation de rédiger le 14.
- **Source :** « zio et hasol habite dans la demeure shun , iseria sa mere et aussi dans la demeure dans une suite secondaire, depuis la mort de armin elle a du mal a rester dans la suite princpale c'était donc hasol qui l'avait recuperé » (demande directe de la session).
- **Décision :** Hasol et Zio habitent ensemble dans la demeure Shun. Iseria y réside toujours, dans une suite secondaire ; depuis la mort d’Armin, elle a du mal à rester dans la suite principale, qu’Hasol a reprise. Cette organisation préserve la présence de la mère et la nuance de son deuil, sans rejet ni rupture familiale.
- **Audit et application :** mentions d’habitation, retours au foyer, chambres et scènes domestiques des chapitres 1–13 vérifiés ; aucune habitation séparée incompatible ou petit logement du couple identifié. Un paragraphe ajouté au chapitre 13, section X, dans les semaines de vie commune suivant le mariage, explicite la demeure et les suites. Les visites de Zio avant la relation, sa présence croissante ensuite et les rendez-vous avec Iseria restent compatibles et sont préservés. Aucun changement aux chapitres 1–12 ni remplacement général de « maison » par « demeure ».
- **À DÉFINIR :** dates exactes du changement de suite d’Iseria, de la reprise par Hasol et de l’installation de Zio. Ne pas imposer un déménagement immédiat après le décès ou une cohabitation conjugale avant la relation du chapitre 13. Cette résidence ne décide ni donation, ni propriété, ni héritage, ni organisation détaillée des pièces.
- **Limites :** un seul ajout narratif ; autres octets du manuscrit, fenêtres, images et archives inchangés. Aucun niveau, statistique, rune, compétence ou événement futur modifié. Aucun commit ni push.
- **Fichiers concernés :** `roman.md`, `lore/personnages.md`, `lore/chronologie.md` et présent registre.

## DEC-109 — Validation littéraire du chapitre 13 corrigé

- **Statut : CANON — validation littéraire explicite de l’auteur le 22 novembre 2026.** Actualise le statut de lecture de DEC-105, sans réécrire les décisions historiques.
- **Source :** déclaration directe de l’auteur dans la session : « chapitre 13 validé ».
- **Version retenue :** chapitre 13 « Ce que nous construisons » actuellement dans `roman.md`, avec les raccords déjà appliqués : cheveux bruns courts de Zio (DEC-106), salon familial spacieux et apprentissage concret auprès de Samia sans anticipation d’une évolution de pouvoir (DEC-107), résidence d’Hasol et Zio dans la demeure Shun, suite principale reprise par Hasol et Iseria dans une suite secondaire (DEC-108). La validation vise ce texte corrigé, pas la seule version initiale de DEC-105.
- **État éditorial :** chapitres **1–9 et 13 validés** ; **10 V2, 11 et 12 restent en lecture sans validation littéraire globale**. Les relations, le mariage intime vers vingt-huit ans et les apprentissages sur plusieurs années racontés au 13 sont validés, sans romance établie rétroactive à l’Académie ni retrait de Samia du groupe de cinq, 50/50 points.
- **Limites :** niveaux, XP, caractéristiques naturelles, cercles, compteurs, inventaires détaillés et paramètres non fixés d’Œil/Main restent **À DÉFINIR**. Dates des changements de suite et de l’installation de Zio, cause du décès d’Armin et différend avec le Griffon restent ouverts. Ni fiches au niveau 60 appliquées, ni total du chapitre 9 figé après les ellipses, ni pouvoir astral coffres/portes sans restriction transféré au livre I.
- **Suite :** centième boss au 14 et premier sort offensif au 15 toujours futurs ; **aucune rédaction du chapitre 14 autorisée**. Aucune validation des classes proposées des vies futures ni autorisation de publication.
- **Consignation documentaire uniquement :** aucun changement au manuscrit, aux fenêtres, images ou archives ; aucun commit, push ou déploiement. Empreinte SHA-256 du manuscrit lors de la consignation : `9458d378fb0634383cb7c43bd9ef06db763328b981bd05e6aa863901b26d1f9c`.
- **Fichiers concernés :** `AGENTS.md`, `PLAN_DIRECTEUR.md`, `README.md`, `lore/personnages.md`, `lore/chronologie.md`, `lore/runes.md`, `lore/systeme.md`, documents de suivi d’intégration et présent registre.

## DEC-110 — Réception des chapitres 13 XI à 16 et validation du livre I

- **Statut : CANON — intégration autorisée et validation littéraire explicite.** Consignation du 23 novembre 2026 ; ne pas attribuer cette date aux échanges mobiles antérieurs.
- **Sources :** nouvel apport `docs/new.txt`, lignes 51619–74252 ; confirmation actuelle de l’auteur : tous les chapitres 1–16 ont été lus et validés, y compris les 10–12 et l’ajout XI du 13. Le GO autorise la réalisation de l’intégration, pas un commit ou un push.
- **Versions :** préserver les dix sections déjà validées du 13 ; ajouter seulement XI « La nuit où tout a changé » (52268–52848). Chapitre 14 : 52992–56881. Chapitre 15 : seconde rédaction, 62289–66825, et non la première 57625–62189. Chapitre 16 : 68155–73963, épilogue compris. Les corrections ciblées demandées par l’auteur priment les formulations de ces copies : cheveux courts de Zio, surnom « ma princesse », plafonds de points et séparation des compteurs.
- **État courant :** livre I complet en seize chapitres validés ; les anciennes notices « 10–12 en lecture », « 14 non autorisé » et « jalons 14–16 futurs » sont historiques. Le statut de validation ne dispense pas de conserver les paramètres non définis ni d’identifier une contradiction.
- **Provenance et limites :** `docs/integration_chapitres_13_16.md`. Archives conservées intactes ; aucun texte de conversation n’entre dans le roman. Aucun chapitre du livre II n’est autorisé par cette intégration.

## DEC-111 — Donjons, portails et limites de la mémoire

- **Statut : CANON**, sauf valeurs explicitement provisoires. Sources : dossier mobile 51623–51821, correction finale des plafonds 57558–57623 et 62266–62285, chapitres 14–16 validés ; arbitrages directs de l’auteur repris dans la demande d’intégration.
- **Donjons :** emplacements fixes, réexploration et réinitialisation après mort du boss ; délai exact **À DÉFINIR**, 24 h n’étant qu’une référence provisoire. Exploitation et accès sont des enjeux économiques, sans droit de propriété automatique. Limites habituelles : cinq membres et cinquante points ; minimum trois membres conservé. Les sorties de monstres sont anormales et distinctes de leur fonctionnement ordinaire.
- **Portails :** lieux et moments imprévisibles, pas de réinitialisation ; ouverture 48 h après apparition, sortie des démons possible, fermeture par mort du boss sans effacement automatique des démons déjà sortis. Prévision spécialisée environ dix heures avant apparition, localisation initialement approximative. Conditions d’entrée anticipée, effectif maximal, portée et paramètres non établis **À DÉFINIR**.
- **Barème final couleur / niveau ordinaire / boss / points :** blanc 10/30/100 ; vert 20/40/100 ; bleu 30/50/100 ; violet 40/60/250 ; orange 50/70/400 ; rouge 60/80/800. Les anciens 100 universels et 120/150/300 sont remplacés. Points de rareté ≠ nombre de chasseurs. Groupe d’Hasol à 50 points : jusqu’à 200 points de renforts en violet et 350 en orange, pas nécessairement autant de personnes.
- **Mémoire :** les souvenirs des donjons effectivement connus ne donnent ni omniscience ni prédiction fiable des portails d’une autre vie. Pas de compétence de prédiction accordée à Hasol au III, à Œil, Aimant ou Main. Mémoire parfaite seulement à partir de R11 (DEC-078/080), malgré les raccourcis de ChatGPT dans le nouvel apport.
- **Catastrophes :** distinguer la bataille orange vers 34 ans du livre I et la catastrophe mondiale à 45 ans au III ; la nouvelle origine de la faille (DEC-116) ne démontre pas une cause unique de tous les dérèglements.

## DEC-112 — Trois compteurs et équipement de fin du livre I

- **Statut : CANON.** Sources : 13 XI ; chapitre 14, notamment 54062–54225 et 56142–56639 ; chapitre 15 retenu ; arbitrage explicite d’exclusivité des compteurs confirmé pour l’intégration.
- **Croissance :** conserver le compteur de mille monstres admissibles et ses seuils historiques. À l’événement mondial de fin du 13, nouveau compteur indépendant de **5 000 éliminations personnelles de monstres de portails**, sans restriction de niveau, initialement 0/5 000, sans cercle immédiat. **Les démons de portails alimentent seulement ce compteur**, pas celui des mille. Les boss de portails ne sont pas des boss de donjon pour le compteur de cent.
- **Chapitre 14 :** Hasol niveau 38, treize cercles au départ. Centième boss de donjon personnellement achevé : Manticore des Cendres niveau 41 ; premier gain immédiat **13→14**, puis nouveaux paliers à 200, 300, etc., sans restriction du niveau du boss de donjon. Un boss de donjon peut toujours avancer l’ancien compteur de mille s’il est admissible. Pas de double récompense des anciens paliers.
- **Chapitre 15 :** **14→15 à 5 000**, puis **15→16 à 10 000** éliminations personnelles cumulées de démons de portails. Ni 15 000 requis au second palier ni compte remis à zéro fictif entre les deux gains. Le treizième cercle est attesté au début du 14 ; sa date et sa cause exactes après le 9 restent **À DÉFINIR**.
- **Équipement attesté au début du 14 :** quatre Fatal, quatre Arcanique, quatre Vitesse, une Gardien, 13/13 ; puis deuxième Gardien au quatorzième cercle, 14/14. Toutes 6★, grade **natif** rare (bleu) minimum, +15 ; grade **affiché** à ce stade légendaire (orange), quatre secondaires maximum. Améliorer ne change pas les étoiles. Cadeaux paternels Fatal/Gardien conservés et montés jusqu’à +15 ; ne pas réécrire leurs fiches historiques à +6.
- **Fin du 15 :** deux Énergie supplémentaires, 6★, **natives rares (bleues)**, +15, pour 16/16, sont des **faits du texte validé**, et non une réponse explicite validant la suggestion du questionnaire. La seconde est décrite « comme la première » (66005–66007). Grade affiché orange, affixes **À DÉFINIR**. Pas de transformation des anciennes Énergie 3★ données à Yoon ni des Arcanique 2★ en nouvelles 6★. Identités et provenance des remplacements, principales/secondaires finales, ressources et stocks **À DÉFINIR** ; aucun ID de remplacement inventé. Voir `lore/runes.md`.
- **Yoon au 14 :** six cercles et six runes équipées, septième en réserve ; ne pas appliquer automatiquement ses huit cercles de référence du niveau 60.

## DEC-113 — Cercles naturels, Révélation et Siphon runique

- **Statut : CANON pour l’identité et les distinctions ; paramètres chiffrés non validés.** Sources : dossier 52865–52985, échanges 56889–57010 et 57542, chapitre 15 validé, précision directe de neutralité du Vent.
- **Cercles :** niveaux et apparition naturelle des cercles sont distincts. L’absorption du mana ambiant et l’influence des combats sont une théorie du monde, pas une formule scientifique démontrée. Révélation institutionnelle à seize ans, associée à l’accumulation suffisante de mana ; le premier cercle d’Hasol à sept ans demeure compatible. Les cercles accordés par Croissance s’ajoutent aux cercles naturels, sans conférer son mécanisme aux autres.
- **Siphon runique :** premier sort offensif direct d’Hasol, actif obtenu au **niveau 40**, au chapitre 15 ; **Vent, zone, dégâts fondés sur la PA, vol de Mana, récupération entre usages**. Sert notamment à restaurer sa réserve pour relancer Aura ; pas de maîtrise instantanée ou de Mana illimité.
- **Vent :** neutre ; ne pas l’ajouter au cycle Eau/Feu/Terre ni inventer un avantage contre Lumière/Ténèbres.
- **À DÉFINIR :** coefficients de dégâts et vol, assiette détaillée, rayon/portée, coût, durée/incantation, recharge chiffrée, plafond et règles de transfert. Les 120 % PA, 75 % PA, 8 m, 100 Mana, 20 s et 1 200 Mana proposés par ChatGPT ne sont **pas canon**. Aura 200 Mana/24 h/rune sacrifiée et Infiltration 30 s restent les règles distinctes déjà validées.

## DEC-114 — Deuil, Présage des failles et trajectoire de Samia

- **Statut : CANON pour les événements racontés et les précisions directes.** Sources : chapitres 15–16 validés ; interventions auteur 67412, 67568–67570 et 67680.
- **Livre I :** un portail bleu non traité à temps détruit le village familial ; **plusieurs proches** meurent, pas toute sa famille déclarée morte. Samia conserve ses cheveux blonds, son identité et sa classe de Ranger commune. Le deuil nourrit la chasse obsessionnelle partagée avec Hasol, puis l’isolement quand Hasol ralentit ; elle n’est ni jalouse de la grossesse ni privée d’affection ou d’autonomie.
- **Présage des failles :** passif acquis au 15, prévision approximative environ dix heures avant manifestation. Évolue au 16 en carte magique affichant les portails détectés par couleur. La carte ne crée ni ne contrôle les portails ; portée, exhaustivité, précision métrique et coûts éventuels **À DÉFINIR**.
- **Livre II :** portails déjà présents lors du retour d’Hasol et passif de Samia disponible dès le début. Premiers bleus au même moment chronologique que dans la première vie, pas automatiquement avancés avec les blancs. Version cartographique complète dès le départ **À DÉFINIR** : c’est une recommandation de ChatGPT, pas une précision de l’auteur.
- **PROPOSITIONS non transformées en canon :** mort de Samia partie seule protéger son village au II ; nouvelle classe/affinité détaillée et mécanisme des cheveux blancs des vies futures. Les images soleil/lune servent la direction de personnage, sans prouver des souvenirs de vies antérieures chez Samia. Mémoire imparfaite d’Hasol au début du II conservée.

## DEC-115 — Mort d’Iseria, grossesse et nouvelle conclusion du livre I

- **Statut : CANON.** Sources : chapitre 14 validé ; annonce de grossesse et chapitre 16 validés ; instruction directe 67814 et harmonisation 73965–74006.
- **Iseria :** meurt au chapitre 14, en forêt pendant une cueillette, submergée par des démons d’un portail blanc non repéré ; **56 h après la notification** (48 h avant ouverture + 8 h), non une notification automatique de décès. Soigneuse de Terre, elle n’obtient pas de sort offensif pour sortir de cette scène. Recherche, panier et découverte par le groupe sont racontés ; niveau réel d’Iseria non déduit de sa fiche de référence.
- **Grossesse :** Hasol a 34 ans, découvre une grossesse d’environ **sept semaines** et informe Zio avant le portail orange proche de la demeure Shun. Elle retrouve un désir d’avenir et ralentit ; aucune faiblesse combattive automatique. Prénom, sexe, naissance et devenir de l’enfant **À DÉFINIR**, sans prolongement inventé jusqu’à 45 ans.
- **Bataille orange :** boss Démon stellaire niveau 70, démons ordinaires 50, formation de 400 points incluant les 50 du groupe. Dernier Rempart volontaire de Zio niveau 61 le tue et tue le démon. **Yoon, Ray et Samia survivent au 16**, remplacent les décès de l’ancien plan ; funérailles et deuil sont racontés. Hasol n’est plus l’unique survivante de ce groupe. Niveaux finaux de référence conservés : Hasol environ 45, Yoon 54, Ray 56, Samia 52 ; ne pas inventer leurs statistiques finales.
- **Surnom :** Zio s’adresse à Hasol par « ma princesse », également employé par Armin. Harmonisation ciblée, sans remplacer les paroles d’autres personnages.
- **Conclusion retenue :** épilogue **dans le livre I**, Hasol a quinze ans, à la veille de ses seize ans et de la Révélation ; cauchemar du cadran, **douze DONG puis un DING**, réveil terrifié, réconfort auprès d’Iseria. Elle murmure **« Astrae vaël norien… thara sel ven. »**, sens pour le lecteur : « Qu’Astrae soit avec nous… Ça a commencé. » Hasol ne comprend pas l’ancien dialecte. Ni explication d’Astrae ni omniscience maternelle importées.
- **Rune temporelle, section XV :** retrouvée par les chasseurs chargés de l’inventaire près du lieu où le Démon stellaire s’est effondré, transmise à Hasol pour expertise puis laissée plusieurs jours dans son coffret. Œil l’identifie partiellement comme Rune temporelle, **grade et étoiles indéterminés**. Pendant son deuil, notification « Instabilité émotionnelle détectée », activation involontaire, cadran/sablier puis 12 DONG + 1 DING. Aucun lien causal détaillé avec la mort ou un souhait volontaire déduit ; pas d’ellipse jusqu’à 45 ans.
- **Remplace :** réveil R1 seulement en ouverture du II, une semaine avant Révélation, et activation imposée comme toute dernière scène du I : elle est suivie de l’épilogue. Le retour la veille ne s’étend **pas automatiquement** à R2–R11 ou à la vie 13. Origine profonde de la Rune temporelle, grade/étoiles, formule du déclencheur et devenir de l’enfant **À DÉFINIR**. Aucun chapitre 17.

## DEC-116 — Ténébria et réouverture de la faille astrale

- **Statut : CANON pour le noyau exposé puis validé ; propositions de scènes séparées.** Source complète : append `docs/new.txt` **74029–74252**. Auteur : origine décrite à 74029, puis **« je valide . » à 74228** après le développement 74030–74226. La reformulation ChatGPT 74229–74252 est postérieure à cette validation : elle ne constitue pas une seconde décision autonome.
- **Noyau validé :** un ancêtre du clan Astrea avait scellé une faille astrale, sans détruire les démons. Dans la première vie, Ténébria souffrant de sa vie imposée découvre un grimoire de magie noire dans la bibliothèque royale, lance avec colère un sort d’invocation sans mesurer sa portée et rouvre la faille. Les démons retrouvent ainsi un accès au monde par les portails ; elle n’a pas voulu condamner l’humanité.
- **Mécanisme et chronologie acceptés par la validation du développement précédent :** Ténébria a quatre ans de plus qu’Hasol ; premiers portails de la première vie vers Hasol 28/Ténébria 32. Au retour temporel, le sceau ne retrouve pas entièrement son état initial ; lors de la Révélation de Ténébria à seize ans, sa classe de Mage Noir astrale résonne avec la faille fragilisée. Portails dès Hasol douze ans/Ténébria seize ans dans la deuxième vie, donc déjà présents lorsque Hasol revient à seize ans. Ce mécanisme proposé avant « je valide » est désormais retenu, pas une loi universelle de tous les retours.
- **Dossier familial validé dans ses grandes lignes, non encore raconté au livre I :** Ténébria est la sœur d’Hasol ; le clan Astrea l’a soustraite à ses parents pour en faire une sauveuse et l’utilise contre les démons. Sa souffrance doit être comprise avant la révélation progressive de sa responsabilité au II. L’ampleur des connaissances d’Iseria, la prophétie, les détails du clan, de l’enlèvement et du pouvoir impérial restent **À DÉFINIR** ; ne pas en tirer une hérédité automatique des classes.
- **PROPOSITIONS / limites :** promesse d’un souhait dans le grimoire, question « Pourquoi personne ne m’aime ? », scène de confrontation avec Hasol et répliques exactes sont des suggestions, pas des scènes validées mot pour mot. Un oncle devenu empereur est évoqué par ChatGPT sans identité, calendrier ou causalité documentée : **À DÉFINIR**, pas une fiche créée. Ne pas importer ces révélations dans les pensées des personnages du I. Aucun nom, sort, statistique ou serviteur supplémentaire inventé.
- **Questions :** dates absolues, chronologie ultérieure des couleurs hors bleus, état de la faille lors des retours suivants, topologie des mondes et rapport aux sorties anormales de donjons ouverts. Le fait que les bleus restent synchronisés entre vies demeure valable ; aucune loi d’accélération uniforme des couleurs déduite.
- **Actualisation de révélation — DEC-131 :** le noyau de bible ci-dessus reste canonique, mais il est interdit de le dire, le suggérer ou le préfigurer au chapitre 1 du II. Ténébria y est seulement innocente dans la situation actuelle et injustement accusée. La révélation historique est réservée à plus tard, après compréhension de sa souffrance.

## DEC-117 — Organisation des manuscrits et préparation du livre II

- **Statut : CANON pour l’organisation demandée ; plan du II en préparation, non validé automatiquement.** Demandes directes de l’auteur dans la session du 23 novembre 2026 : mise à jour de `new.txt`, demande d’un plan du livre II, renommage de `roman.md` avec le titre du livre I et travail sur une branche `livre2` ; précision : « le livre 2 sera écrit dans un fichier md du nom du livre 2 ».
- **Organisation :** un manuscrit Markdown distinct par livre, nommé selon son titre. Le livre I, *L’Ascension d’une légende oubliée*, devient `livre_1_l_ascension_d_une_legende_oubliee.md`, sans modification de son contenu. Les mentions historiques de `roman.md` renvoient à ce fichier renommé ; ne pas recréer de copie concurrente.
- **Livre II :** son plan est conservé séparément dans `PLAN_LIVRE_II.md`. Son futur manuscrit portera son titre ; aucun titre non validé ne doit être imposé par le choix du nom de fichier. Le plan doit distinguer décisions explicites, propositions de structure et paramètres ouverts.
- **Périmètre :** travail local sur `livre2`, lecture de la transmission, préparation du plan et raccords nécessaires des outils et références. Aucun chapitre du II, aucune réécriture du livre I, aucun commit/push ni déploiement autorisé par cette demande. `docs/new.txt` reste intact comme provenance.
- **Remplace :** l’obligation d’un fichier `roman.md` unique pour l’ensemble du projet ; l’unicité de la source narrative reste exigée pour chaque livre.

## DEC-118 — Innocence de Ténébria dans la deuxième vie

- **Statut : CANON.** Auteur, `docs/new.txt:74254` : les accusations sont injustes « car dans cette vie tenebria n'a rien fait ».
- Elle n’a pas provoqué les portails par une nouvelle invocation. Complète DEC-116 sans effacer sa réouverture accidentelle de première vie ni convertir la résonance involontaire actuelle en faute personnelle. Pas de règle universelle sur tous les retours déduite.
- Provenance détaillée et limites : `docs/integration_livre_2.md`. Cette référence vaut aussi pour DEC-119–128, consignées le 23 novembre 2026, sans dater artificiellement les échanges mobiles.

## DEC-119 — Premier drame du II : Ray et le loup alpha

- **Statut : CANON pour le premier drame et le contexte ; réception contextuelle pour le sauvetage suivant.** Auteur 74321–74323 : onze drames incluant Ténébria/Astrea ; mort de Ray dans les bois contre le loup alpha ; Hasol astrale populaire dans un groupe solide ; Zio la trouve hors de portée et n’a pas le même coup de cœur.
- **Remplace le poison de R1 et l’ancien double échec de DEC-080.** L’auteur valide ensuite le drame de Samia (75306) présenté après Ray sauvé en vie 3 (75272–75274) : retenir cet enchaînement vie 2 Ray mort / vie 3 Ray sauvé puis Samia, sans valider les scènes détaillées de ChatGPT.
- Meilleur ami et Ray hors équipe de vie 2 conservés ; modalités du sauvetage, âges, niveaux et annonce **À DÉFINIR**. Lunettes récupérées et souvenir conscient précis du sauvetage du I non validés. Classe Stratège runique rare dès vie 4 : **PROPOSITION**, la phrase auteur 75048 étant une question, non une adoption des précisions de la réponse.
- **Actualisation — DEC-133 :** le statut de proposition de la classe de Ray est historique ; l’arbitrage direct ultérieur la rend canonique en vie 4.
- La mémoire imparfaite demeure ; l’amour de Zio n’est pas dû à Hasol. Aucun chapitre du I révisé.

## DEC-120 — Yoon légendaire et présentation à Hasol

- **Statut : CANON.** Auteur 74728 : Yoon présentée après la Révélation de sa classe légendaire pour sa complémentarité avec Hasol astrale.
- Concerne le II, sans modifier Yoon rare au I. L’écart d’âge demeure : environ treize ans au retour initial d’Hasol, Révélation trois ans plus tard environ. Ni rencontre de chasse immédiate à treize ans, ni nouveaux sorts automatiquement importés.
- **Conséquence :** l’ancien quatuor astral à 50 points n’est plus une composition courante valide : 25+20+10+5 = 60 ; 65 si Ray devient rare. Hasol/Yoon/Ray commun = 50, mais avec Ray rare = 55. Plafonds et minimum de trois membres non modifiés ; compositions réelles **À DÉFINIR**.
- Doctrine militaire et vétéran obligatoire aux donjons (74623–74727) : **PROPOSITIONS de ChatGPT**, non règles adoptées par cette déclaration.

## DEC-121 — Parcours d’élite de Zio et mauvaise entente avec Ténébria

- **Statut : CANON pour les précisions auteur.** 74830/74832, doublon de la même intervention : une année commune d’Académie et certaines opérations de portails partagées au II. 74931 : groupe d’élite rare avec la sauveuse théorique, avance de niveau ; très mauvaise entente réciproque, motif de son départ vers le groupe de sa sœur au I.
- Remplace la relation amicale/confiance particulière proposée par ChatGPT dans la réponse précédente. Causes tactiques ou éthiques, dialogues de démission, calendrier et composition exacte **À DÉFINIR** ; aucune romance avec Ténébria déduite.
- Complète les causes du départ laissées ouvertes par DEC-035/067, **sans autoriser de réécriture ou ajout au I validé**.

## DEC-122 — Samia transformée dès la vie 2 et spécialiste des portails

- **Statut : CANON pour le changement initial, la rareté et le statut stratégique.** Auteur 75132 : changement de classe et d’apparence direct ; 75178 : commune traitée aussi bien qu’une Astrale ; correction 75206 : découverte des **portails**, pas des donjons.
- Passif dès le début déjà fixé par DEC-114. **À DÉFINIR :** nom exact de classe, apparence détaillée, affinité, carte complète dès le départ et paramètres. *Marcheuse astrale*, blanc argenté, Ténèbres et tempérament lunaire détaillé restent proposés par ChatGPT, pas confirmés par la seule phrase auteur.
- Ne pas adopter de gains statistiques légendaires, mémoire de vies antérieures, exhaustivité de détection ou utilité limitée au seul repérage. Samia garde une vie propre hors de l’équipe principale.

## DEC-123 — Drames validés de Samia et Ténébria au II

- **Statut : CANON pour les drames approuvés ; placements détaillés À DÉFINIR.** Auteur 75306 : « Drame samia -> je valide on avait deja fait cette pistes ensemble . » Piste 75270–75274 : après Ray sauvé en vie 3, Samia meurt en protégeant les siens face à un portail bleu sans renforts suffisants. Actualise le statut de proposition de DEC-114.
- Raccord avec l’avertissement d’Hasol dans la piste antérieure 62198 à préparer ; pas de cauchemar omniscient de faits jamais vécus. Famille intégralement morte, niveaux personnels et déroulement non fixés.
- Auteur 75307 : validation de Ténébria, déclenchement temporel à la **lecture de sa mort**, alors qu’Hasol la connaît peu ; surprise du lecteur et ouverture de la découverte de sa sœur.
- Vie 9, rapport impérial, cause du décès, vie suivante d’enquête, preuves et révélation au chapitre 14 : **PROPOSITIONS de placement/mise en scène**. Aucun mécanisme de rune automatiquement sensible à la parenté établi.
- **Actualisation — DEC-135 :** le placement en vie 9 est historique. La mort de Ténébria passe en vie 8, chapitre 11 ; le rapport impérial et la cause restent des propositions.

## DEC-124 — Armin sauvé par les vacances et indice d’Iseria

- **Statut : CANON pour la solution et la révélation limitée ; CONTRADICTION de nom à arbitrer.** Auteur 75430 : dans la vie où Armin est sauvé, Iseria révèle que le « griffon ardent » est lié à sa famille ; Hasol écoute son père sans en apprendre davantage. Auteur 75557 : annuler le voyage commercial et partir tous les trois en vacances pour apaiser l’ambiance familiale.
- Compatible avec R5/vie 6 de DEC-080. Pas d’escorte améliorée comme solution, pas de catastrophe sur la route abandonnée affirmée sans validation, destination/durée **À DÉFINIR**.
- **Griffon Ardent / Griffon d’Argent : CONTRADICTION** avec le nom du I/DEC-080. Ni renommage rétroactif ni seconde guilde inventée. Mémoire effacée d’Armin et généalogie impériale détaillée ne sont pas validées par l’intervention d’Iseria.

## DEC-125 — Progression accélérée et instinct artisanal d’Hasol au II

- **Statut : CANON pour la direction explicite.** Auteur 75704 : davantage de cercles grâce aux portails ; compréhension et pratique artisanales beaucoup plus rapides, comme des milliers d’heures d’expérience ; Orven stupéfait dès les premiers essais.
- **Qualification historique :** cette direction avait été dite compatible avec les **32 cercles en R11** de DEC-057. DEC-136 retire désormais ce total sans annuler l’accélération ; niveau, cercles et équipement de fin du II restent ouverts. DEC-132 précise séparément la mémoire. Coûts, fatigue, échecs, apprentissages et ressources demeurent.
- La scène de fabrication/inscription de rune de ChatGPT et le nom « Orven Vals » ne sont pas adoptés. Les paramètres de Croissance astrale et de ses évolutions restent à détailler.

## DEC-126 — Croissance Astrea astrale et compteurs personnels de Ténébria

- **Statut : CANON pour le déclencheur, l’effet familial et la condition de groupe ; modalités À DÉFINIR.** Auteur 75898 : Croissance évolue dès reconnaissance de Ténébria comme sœur ; un membre Astrea astral dans le groupe profite aussi du passif ; groupe des sœurs pour le donjon infini au III. Auteur 75978 : Ténébria a ses propres compteurs, qui augmentent seulement si Hasol est dans son groupe.
- **À DÉFINIR :** graphie du libellé Astrea/Astrae, seuils transmis, emplacements, éliminations créditées, état des compteurs hors groupe et reports entre vies. Suspension sans remise à zéro et exclusivité des éliminations personnelles pour le bénéficiaire sont des formalismes de ChatGPT, non une décision auteur supplémentaire.
- **CONTRADICTION d’accès à arbitrer au III :** deux Astrales totalisent 50 points mais le minimum de trois membres de DEC-035/111 demeure. L’auteur parle d’un groupe, ne valide pas l’entrée en duo proposée ensuite par ChatGPT. Aucune exception ou troisième membre gratuit inventé.
- Ne confirme pas l’hypothèse générale DEC-066 pour tous les compagnons et ne transfère pas les compteurs d’Hasol à Ténébria.

## DEC-127 — Actif de vol de vie de Ténébria

- **Statut : CANON pour l’actif et le changement d’usage.** Auteur 76036 : vol de vie monocible sur elle-même ou un allié ; jusque-là utilisé sur elle seule, ce comportement change avec Hasol.
- Nom officiel, niveau, durée, coût, recharge, efficacité et déclencheurs **À DÉFINIR**. Première utilisation sur Hasol au chapitre 14 et circonstances de combat : **PROPOSITIONS**, pas texte validé.

## DEC-128 — Portails rouges réservés au livre III

- **Statut : CANON.** Auteur 76623 : rouges au III, pas au II. Barème rouge conservé (DEC-111), aucune apparition au II, même lorsqu’une vie atteint 45 ans.
- Ne démontre pas l’origine de la mort des Notos, un calendrier universel des couleurs ou une cause unique de la catastrophe mondiale.
- **Limite générale de cet apport :** le plan ChatGPT 76040–76621 n’a pas de validation globale auteur. Les quatre drames vie 4/Orven, vie 7/défaite et pertes civiles, vie 8/liberté d’Iseria, vie 10/séparation des sœurs restent des **PROPOSITIONS**. Titres, placements et détails de Carmela/oncle empereur/effacement de mémoire restent ouverts. Réveil final au III, pas en clôture du II.
- **Actualisation ultérieure :** cette liste de quatre drames décrit l’état de réception de l’apport. DEC-134 résout Orven ; DEC-135 déplace le drame d’Iseria en vie 9/ch.12 ; DEC-137 le résout. Deux drames restent ouverts aux chapitres 10 et 14.

## DEC-129 — Titre et fichier du livre II

- **Statut : CANON — validation explicite de l’auteur dans la session du 23 novembre 2026.** Source : « Le Vertige des vies oubliées validé ».
- **Titre :** le livre II s’intitule *Le Vertige des vies oubliées*.
- **Manuscrit :** conformément à DEC-117, sa source unique est `livre_2_le_vertige_des_vies_oubliees.md`, distincte du plan `PLAN_LIVRE_II.md` et du manuscrit du livre I.
- **Limites :** cette validation remplace uniquement le statut « titre à définir » et les anciennes propositions de titre. Elle ne valide ni les titres des seize chapitres, ni leur découpage proposé, ni les quatre drames encore ouverts, et n’autorise la rédaction d’aucun chapitre, commit ou push.
- **Historique :** DEC-130 a ensuite validé la structure ; DEC-134/135 ont résolu Orven et actualisé les placements. Cette ligne conserve la portée initiale de DEC-129.
- **Fichiers concernés :** `AGENTS.md`, `README.md`, `PLAN_DIRECTEUR.md`, `PLAN_LIVRE_II.md`, `lore/chronologie.md`, présent registre et création du manuscrit titré.

## DEC-130 — Validation de la structure en seize chapitres du livre II

- **Statut : CANON pour la structure — validation explicite de l’auteur dans la session du 23 novembre 2026.** Après clarification de la portée du « go », l’auteur choisit « Valider le plan » avec la limite proposée : valider le découpage actuel, ses seize titres et ses placements, en laissant explicitement ouverts les quatre drames signalés.
- **Décision :** les seize titres de `PLAN_LIVRE_II.md`, leur ordre, la répartition des vies absolues 2–12/R1–R11 et les jalons déjà canoniques sont validés. La vie 13 reste réservée au livre III.
- **Restent À DÉFINIR :** drame d’Orven au chapitre 6 ; issue et éventuelles pertes civiles au chapitre 10 ; devenir et éventuelle privation de liberté d’Iseria au chapitre 11 ; issue et éventuelle séparation des sœurs au chapitre 14. Les propositions actuelles ne deviennent pas canon par cette validation de structure.
- **Actualisation — DEC-134/135/137 :** la liste ci-dessus est l’état historique de DEC-130. Orven et Iseria sont résolus. Les deux drames ouverts sont ceux des chapitres 10 et 14.
- **Limites :** les scènes détaillées, dialogues, paramètres LitRPG, niveaux, équipements, compositions d’équipe et modalités des transitions restent à préparer ou arbitrer selon leur statut propre. Aucun chapitre n’est autorisé à la rédaction ; aucun commit/push n’est autorisé.
- **Fichiers concernés :** `AGENTS.md`, `README.md`, `PLAN_DIRECTEUR.md`, `PLAN_LIVRE_II.md`, `lore/chronologie.md` et présent registre. Le manuscrit du II reste limité à son titre.

## DEC-131 — Réserver l’histoire de la faille après la souffrance de Ténébria

- **Statut : CANON — arbitrage direct de l’auteur.** Au chapitre 1 du livre II, Ténébria est décrite uniquement dans sa situation actuelle : innocente de l’apparition des portails et accusée injustement.
- **Décision :** ne jamais dire, suggérer ni préfigurer dans ce chapitre qu’elle a rouvert la faille dans la première vie. La révélation historique de DEC-116 doit intervenir plus tard, après que sa souffrance a été comprise.
- **Portée :** DEC-116 reste vraie dans la bible ; seul son calendrier de révélation est resserré. Aucun dialogue, indice symbolique ou pensée d’Hasol ne doit contourner cette réserve.

## DEC-132 — Mémoire cumulative à partir de la vie 3

- **Statut : CANON — arbitrage direct de l’auteur ; remplace les formulations générales antérieures sur la mémoire imparfaite.**
- **Vie 2 :** Hasol ne se rappelle aucun drame de la première vie.
- **À partir de la vie 3 :** après chaque réincarnation, elle reçoit des fragments cumulatifs, incomplets et désordonnés des drames terminaux vécus depuis la vie 2 jusqu’à la vie précédente. Elle ne reçoit pas les faits ordinaires exhaustifs, une chronologie fiable ou des événements jamais vécus.
- **R11 :** la première vie reste entièrement inaccessible jusque-là. Mémoire runique restitue alors toutes les vies, première incluse ; mémoire parfaite ne vaut toujours pas omniscience.

## DEC-133 — Ray Stratège runique rare en vie 4

- **Statut : CANON — arbitrage direct de l’auteur.** Ray devient **Stratège runique, Rare**, en vie 4.
- **Conséquences :** cette version vaut dix points. Avec Hasol astrale 25 et Yoon légendaire 20, le trio totaliserait 55 points et ne constitue donc pas une formation de donjon admissible sous le plafond actuel de 50. Les formations réelles restent **À DÉFINIR** ; aucun relèvement du plafond ou retrait automatique d’un personnage n’est déduit.
- **Limites :** ce changement ne modifie ni le mage de feu commun du livre I ni les versions antérieures de Ray. Répertoire, statistiques, cercles, apparence de classe et cause du changement restent **À DÉFINIR**.

## DEC-134 — Mort indirecte d’Orven au chapitre 6

- **Statut : CANON — arbitrage direct de l’auteur.** Le drame d’Orven est fixé au chapitre 6, vie 4.
- **Causalité :** Hasol termine sa formation beaucoup plus vite ; Iseria rend donc moins souvent visite à Orven. Dans la première vie, Iseria avait repéré une toux inquiétante, donné des tisanes adaptées et son alerte avait permis une prise en charge. Dans la vie 4, la toux n’est pas repérée, la maladie progresse et Orven meurt.
- **Limites :** causalité indirecte, sans faute morale d’Hasol ou d’Iseria. Les tisanes ne sont pas un remède miraculeux : l’élément déterminant de la première vie était l’alerte et la prise en charge. Maladie, calendrier, soins, annonce et scène restent **À DÉFINIR**.
- **Conséquence de plan à cette étape :** Orven n’est plus un drame ouvert. DEC-137 résout ensuite Iseria ; deux drames restent actuellement à définir.

## DEC-135 — Inversion des vies 8 et 9 aux chapitres 11 et 12

- **Statut : CANON — choix explicite de l’auteur ; remplace DEC-130 sur ce seul ordre.**
- **Chapitre 11 :** « La mort d’une inconnue », vie 8. Hasol apprend la mort de Ténébria alors qu’elle la connaît peu. Support, cause et modalités restent **À DÉFINIR**.
- **Chapitre 12 :** « Le prix de la victoire », vie 9. Hasol cherche Ténébria plus tôt ; Ténébria l’aide à sauver un village ; la victoire contre le démon est maintenue dans cette vie. **Actualisation DEC-137 :** village de Samia sauvé, puis Iseria exécutée ; le drame n’est plus ouvert.
- **Limites :** village exact, menace, déroulement de l’aide et modalités de la victoire non fixés. L’ancienne proposition de perte de liberté d’Iseria n’est pas validée automatiquement. Les chapitres 13–16 et autres placements restent inchangés sauf raccords de numérotation nécessaires.
- **Drames ouverts :** chapitre 10, issue et éventuelles pertes ; chapitre 12, drame d’Iseria ; chapitre 14, séparation éventuelle des sœurs.

## DEC-136 — Progression de fin du II sans total de 32 cercles

- **Statut : CANON — arbitrage direct de l’auteur ; remplace la partie de DEC-057 relative à la fin du livre II.**
- **Retrait :** le jalon de **32 cercles et 32 emplacements à la fin du II** n’est plus canonique. Ne pas en déduire 32 runes, une courbe ou un inventaire.
- **Direction :** Hasol termine le II nettement plus puissante que dans la première vie grâce aux portails présents tôt et à l’urgence permanente de chasse, à sa progression artisanale accélérée et à Armin maintenu vivant dans les vies ultérieures pour gérer les affaires Shun, ce qui réduit sa charge administrative.
- **À DÉFINIR :** niveau, total de cercles, compteurs, équipement, inventaire et mesure exacte de l’écart de puissance.
- **Préservé :** seize cercles en fin du I et **36 cercles/emplacements en fin du III**. Le retrait ciblé ne modifie pas automatiquement le jalon du III ni les règles de report.

## DEC-137 — Pacte Astrea et exécution d’Iseria en vie 9

- **Statut : CANON — arbitrages directs de l’auteur dans la session du 23 novembre 2026.**
- **Pacte :** après l’enlèvement de Ténébria, un pacte imposé concerne Iseria, Armin et leur future famille : le clan doit les laisser vivre à l’écart ; Iseria doit garder le silence sur Ténébria et rompre tout contact avec elle et les Astrea. Hasol n’est pas connue du clan comme fille d’Iseria. Publiquement, elle est une Shun ; ce nom très répandu ne permet pas de la relier à Iseria.
- **Prophétie et surveillance :** la prophétie ne mentionne qu’un enfant d’Iseria comme sauveur du monde. Après avoir obtenu Ténébria, le clan croit cet enfant identifié. Quand Hasol révèle à son tour une classe astrale, les Astrea la surveillent comme une Astrale extérieure potentiellement manipulable, toujours sans connaître sa filiation.
- **Vie 9, chapitre 12 :** avertie par les fragments de la mort de Ténébria en vie 8, Hasol la cherche plus tôt. Elles sauvent le village de Samia et Hasol vainc le démon. Leur rapprochement déclenche une enquête qui révèle qu’Hasol est la seconde fille d’Iseria et une seconde enfant astrale cachée. Le clan se retourne contre Iseria.
- **Condamnation :** l’empereur actuel est le frère d’Iseria, donc l’oncle d’Hasol et Ténébria. Il considère le pacte rompu, condamne sa sœur à mort et fait exécuter la sentence. La mort d’Iseria déclenche 12 DONG + 9 DING.
- **Limites :** formulation exacte du pacte, danger menaçant le village, procédure, accusation officielle, lieu et méthode d’exécution, recours et tentatives de sauvetage restent à préparer. Ne pas présenter Iseria, Hasol ou Ténébria comme moralement responsables de cette injustice. Aucun chapitre n’est autorisé.

## DEC-138 — La matriarche Astrea sauve Iseria en vie 10

- **Statut : CANON — arbitrages directs de l’auteur dans la session du 23 novembre 2026.**
- **Matriarche :** la grand-mère d’Hasol et Ténébria est la mère d’Iseria et de l’empereur, matriarche de la famille Astrea et garante du pacte familial.
- **Secret du trône :** l’empereur n’a obtenu la couronne que par une manœuvre au détriment d’un autre de ses frères, initialement destiné à régner. Le frère lésé ignore cette vérité. La matriarche connaît les faits et détient le levier nécessaire : si la noblesse les apprenait, elle pourrait se rebeller en se ralliant au frère écarté.
- **Vie 10 :** grâce aux fragments cumulatifs de l’exécution d’Iseria, Hasol sollicite la matriarche assez tôt et la convainc d’intervenir. Celle-ci menace de révéler l’accession irrégulière et impose le respect du pacte. L’empereur recule ; Iseria n’est pas exécutée dans cette vie.
- **À DÉFINIR :** nature exacte de la manœuvre, preuves détenues, identité et caractère du frère lésé, arguments d’Hasol, scène d’intervention et conséquences politiques. La menace ne valide pas une rébellion effectivement déclenchée. Le drame d’Iseria est résolu ; seuls les drames des chapitres 10 et 14 restent ouverts.

## DEC-139 — Filiation officielle de Ténébria et mémoire d’Armin

- **Statut : CANON — précisions directes de l’auteur dans la session du 23 novembre 2026.**
- **Filiation publique :** aux yeux du monde, Ténébria est la fille biologique de l’empereur actuel et de son épouse. Ténébria elle-même croit cette filiation et ignore qu’Iseria et Armin sont ses véritables parents ainsi qu’Hasol sa sœur.
- **Détenteurs de la vérité :** Iseria ; l’ancien empereur et son épouse **Carmela Astrea** ; l’empereur actuel et son épouse. Carmela est aussi la mère d’Iseria et de l’empereur actuel, la grand-mère d’Hasol et Ténébria, la matriarche Astrea et l’intervenante de DEC-138.
- **Armin :** Iseria a effacé par magie toute existence de Ténébria de sa mémoire : première fille, enlèvement et pacte. Motif précis, consentement, coût, sort utilisé, date et conséquences psychiques restent **À DÉFINIR** ; ne pas déduire qu’Iseria peut réécrire librement tous les souvenirs.
- **Portée :** la fausse filiation protège le récit impérial et explique que le rapprochement des sœurs menace le clan. Elle n’est pas révélée au chapitre 1 et ne doit pas préfigurer la responsabilité historique de Ténébria. Modalités administratives, témoins, date de présentation comme princesse et histoire publique de sa naissance restent à préparer.

## DEC-140 — Elric Arowell, mentor de chasse d’Hasol

- **Statut : CANON — décisions directes de l’auteur dans la session du 23 novembre 2026.**
- **Identité et introduction :** Elric Arowell apparaît au chapitre 1 du livre II, vie 2. L’Académie le désigne comme mentor de chasse d’Hasol. Il revient dans plusieurs réincarnations et est destiné à reparaître au livre III.
- **Profil :** **42 ans et niveau 45** lors de leur rencontre ; classe **Porte-bouclier**, rareté Commune, cinq points. Tank vétéran très orienté soutien, équipé d’un bouclier et d’une épée.
- **Compétences :** une attaque offensive d’élément Terre, des capacités de provocation et d’étourdissement. Noms, niveaux, coûts, portées, durées, récupérations et résistances restent **À DÉFINIR** ; aucun contrôle absolu déduit.
- **Aura :** Hasol applique Aura runique à l’épée d’Elric pendant leur mentorat. Élément, moment, combat et rune sacrifiée restent à préparer selon les règles existantes ; Elric niveau 45 peut utiliser l’arme imprégnée.
- **Retraite :** les années de mentorat passent rapidement dans le récit. Huit ans après leur rencontre, Elric atteint 50 ans et prend sa retraite de chasseur, usé par l’accumulation des combats ; Hasol a alors environ 24 ans. Aucune blessure terminale unique, maladie ou incapacité précise n’est déduite. Son éventuel rôle de conseiller après la retraite reste **À DÉFINIR**.
- **Équipes :** Hasol astrale 25 + Yoon légendaire 20 + Elric commun 5 = 50 points. Cette compatibilité ne valide pas une équipe permanente ni l’ajout de Ray/Zio au-delà du plafond.
- **À DÉFINIR :** apparence, personnalité, histoire, motivations, scènes précises, évolution selon les vies et rôle détaillé au III. Aucun chapitre n’est autorisé par cette décision.

## DEC-141 — Hasol et Ray, une amitié troublée par les visions

- **Statut : CANON pour la trajectoire affective ; PROPOSITION pour la scène de déclaration — arbitrage direct de l’auteur dans la session du 23 novembre 2026.**
- **Livre II :** la proximité avec Ray constitue un fil des onze vies. Les visions poussent Hasol à s’intéresser à lui plus que nécessaire ; le temps réellement passé ensemble nourrit un attachement sincère qui dépasse un peu l’amitié, jusqu’à des pensées amoureuses. Les visions orientent son attention, elles ne créent pas à elles seules tous ses sentiments.
- **Limite intime :** malgré cet attachement, Hasol sent au fond d’elle que Ray n’est pas le bon partenaire amoureux pour elle. Cette intuition ne lui donne pas une connaissance consciente de son mariage avec Zio ni de la première vie avant Mémoire runique.
- **PROPOSITION autorisée :** une scène peut montrer Ray lui déclarant ses sentiments et Hasol déclinant poliment. Cette possibilité ne fixe ni une déclaration effective, ni des sentiments amoureux de Ray dans toutes les vies, ni sa réaction après le refus.
- **Mémoire — DEC-132 préservée :** aucun souvenir des drames du I en vie 2 ; fragments cumulatifs des seuls drames terminaux des vies 2 et suivantes à partir de la vie 3, première vie inaccessible jusqu’à R11. Ne pas transformer ces visions en souvenirs romantiques complets, en prophétie ou en preuve d’un amour réciproque.
- **À DÉFINIR :** vies et chapitres où l’attachement se développe, placement éventuel de la déclaration, paroles et suites du refus. Ne pas reproduire automatiquement la même évolution à chaque vie, dévaloriser Ray comme simple substitut de Zio ou modifier le livre I. Aucun chapitre n’est autorisé par cette décision.

## DEC-142 — L’anneau offert par Ray et le dilemme d’Hasol au livre III

- **Statut : CANON pour le jalon et le conflit intérieur — décision directe de l’auteur dans la session du 23 novembre 2026 ; placement et mise en scène À DÉFINIR.**
- **Livre II :** dans une vie encore à placer, Ray offre de nouveau l’Anneau runique à Hasol, cette fois avec de véritables sentiments amoureux. Elle accepte l’anneau mais lui dit devoir encore réfléchir sur le plan sentimental. Cela ne constitue ni une acceptation de couple ni le refus poli immédiat envisagé en DEC-141 ; l’issue ultérieure reste ouverte.
- **Confirmation explicite de l’auteur : scène obligatoire au livre II.** Le don de l’anneau par Ray amoureux et l’acceptation d’Hasol accompagnée de sa demande de réflexion doivent être montrés en scène, pas seulement évoqués ou résumés. Seuls la vie, le chapitre et les détails de mise en scène restent **À DÉFINIR** ; cette obligation ne constitue pas un GO de rédaction immédiate.
- **Suite CANON — précision ultérieure de l’auteur :** un drame survient avant qu’Hasol donne sa réponse sentimentale à Ray au livre II. L’attente est interrompue ; aucun refus poli ni accord définitif ne doit être inséré avant ce drame. Nature du drame, vie, chapitre et lien éventuel avec un retour temporel restent **À DÉFINIR** ; ne pas déduire une nouvelle mort de Ray ou un drame supplémentaire distinct des jalons prévus. Cette précision remplace l’issue laissée ouverte pour cette scène, sans fixer la réponse qu’Hasol aurait donnée.
- **Système préservé — DEC-077/078 :** le passif concerné est **Aimant runique**, à redébloquer dans chaque vie après un combat en portant l’Anneau. La remise de l’objet seule ne déclenche pas le passif ; niveau exact et délai avant combat restent **À DÉFINIR**. L’anneau n’est pas une bague de fiançailles ni un emplacement supplémentaire par cette décision.
- **Livre III :** avec sa mémoire complète, Hasol se rappelle ce cadeau et les sentiments de Ray. Elle se trouve horrible de vouloir exploiter ces sentiments pour obtenir l’anneau et gagner en puissance, mais juge ce gain nécessaire. Ce jugement de nécessité appartient à Hasol : il n’établit pas qu’exploiter Ray soit objectivement la seule solution.
- **Limites :** le projet conscient d’exploitation au III n’est pas attribué rétroactivement à Hasol au II. Il ne confirme ni une manipulation accomplie au III, ni la répétition certaine des sentiments de Ray dans la dernière vie. Manière de solliciter l’anneau, degré de franchise, décision effective et conséquences relationnelles restent **À DÉFINIR**. Préserver la sincérité de l’attachement de DEC-141 et l’autonomie de Ray ; aucun chapitre autorisé, aucun changement au livre I.

## Questions de système toujours ouvertes

- Barème numérique des gains secondaires, au-delà des choix individuels consignés pour les deux cadeaux ; règle d’apparition résolue par DEC-006.
- Bornes de PA et renforcements PA/plafond d’ensembles résolus par DEC-099 ; deux fiches et Attaque % secondaire confirmés par DEC-100. Courbe PA +1 à +14, probabilités des renforcements, PV %/Défense % en secondaires et classes futures hors **Ray Stratège runique rare en vie 4** restent ouvertes. Cette classe ne modifie pas le livre I ; le retrait CC/DCC est résolu par DEC-098.
- Ordre des opérations et arrondis des bonus d’ensemble.
- Reliquat d’éliminations après les huit paliers rétroactifs de Croissance runique.
- Durée, coût et portée de Chant (DEC-074), fréquence globale des runes, distributions d'étoiles hors exemple niveau 30 et dépendance éventuelle étoiles/grade (DEC-077), cumul du seuil de livres et report des cercles entre vies (DEC-079).
- **Points résolus :** tables conditionnelles de grades (violet ordinaire corrigé à 0,9 %) et activation temporelle par détresse **avant** le coup fatal, le 21 novembre 2026 ; Œil, actualisé le 22 novembre par DEC-097 : types prédéterminés et résultat final exact à +15 si Hasol effectue les améliorations et atteint ce palier, sans réussite automatique des tentatives. La lecture aux maxima non garantis de DEC-076 est historique, pas une question encore ouverte.
- **Points résolus par réponses directes ultérieures du 21 novembre 2026 :** soin de Chant 10 % PV max de Yoon/5 secondes ; Lame retiré du système actif au profit d'Arcanique ; rang de butin limité par un plafond ; Aura niveau 1 astral avec seuil d'utilisation de l'arme niveau 10 maintenu sans exception. Ne pas rouvrir ces arbitrages sur la base des formulations historiques précédentes.

La validation de DEC-001 ne tranche pas ces questions.
