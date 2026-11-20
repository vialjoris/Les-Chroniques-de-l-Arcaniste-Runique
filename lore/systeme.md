# Système LitRPG — Règles runiques

Ce fichier est en cours de constitution : les sections ci-dessous documentent les décisions runiques récentes et ne remplacent pas encore toutes les règles de `PLAN_DIRECTEUR.md`. Sources : décisions explicites de l’auteur consignées dans `decisions.md` et article cité dans `../source.md`.

## 1. Trois dimensions distinctes d’une rune — CANON

| Dimension | Valeurs | Fonction |
|---|---|---|
| Grade de couleur | Commun blanc, Peu commun vert, Rare bleu, Épique violet, Légendaire orange | Détermine le nombre de secondaires dès +0 : respectivement 0, 1, 2, 3, 4 |
| Rang en étoiles | 1★, 2★, 3★, 4★, 5★, 6★ | Influence les valeurs de la principale selon les tables validées |
| Niveau d’amélioration | +0 à +15 | Indique l’amélioration de la rune ; les paliers visibles incluent +3, +6, +9, +12 et +15 |

Ne pas confondre ces dimensions : une rune bleue peut avoir un rang qui n’est pas trois étoiles. HAS-R001 et HAS-R002 sont des runes bleues 6★ déjà +6 au moment du don, avec deux secondaires natives renforcées chacune (DEC-006, qui rectifie DEC-005). Elles ne gagnent pas deux secondaires supplémentaires à +6.

## 2. Unités des caractéristiques — CANON

- Taux critique (ou chance critique), dégâts critiques, précision et résistance : pourcentages autorisés, en principales comme en secondaires.
- Les secondaires fixes restent exprimées en valeurs fixes : natives Vitesse +2 et PV +15 pour HAS-R001, renforcées à +4 et +25 ; natives PV +20 et Mana +10 pour HAS-R002, renforcées à +30 et +20. Les gains sont des choix éditoriaux délégués, pas des valeurs tirées d’un barème du guide.
- Une augmentation d’un taux doit être distinguée d’une multiplication relative : par exemple, un bonus de taux critique de +3 % désigne un ajout de trois points de pourcentage au taux, pas une hausse relative de 3 %.
- PV %, Attaque % et Défense % sont admis comme principales par DEC-011 ; leur adoption comme secondaires reste à confirmer. Ne pas confondre les deux décisions.
- Les bonus d’ensemble restent distincts des caractéristiques individuelles et conservent les valeurs validées du plan.

## 3. Tables des principales adoptées par l’auteur

Source : les quatre lignes du guide de JeuxOnLine reprises explicitement par l’auteur (DEC-004).

**Lecture d’une cellule : valeur à +0 / gain par niveau / valeur à +15.** Toutes les valeurs sont en pourcentage ; un gain représente des points de pourcentage. Ces tables concernent les **principales uniquement**, jamais les secondaires.

| Principale | 1★ | 2★ | 3★ | 4★ | 5★ | 6★ |
|---|---|---|---|---|---|---|
| Taux critique % | 1 / 1 / 18 | 2 / 1 / 19 | 3 / 2 / 37 | 4 / 2,25 / 41 | 5 / 2,5 / 47 | 7 / 3 / 58 |
| Dégâts critiques % | 2 / 1 / 19 | 3 / 2 / 37 | 4 / 2,25 / 43 | 6 / 3 / 57 | 8 / 3,33 / 65 | 11 / 4 / 80 |
| Précision % | 1 / 1 / 18 | 2 / 1 / 19 | 4 / 2 / 38 | 6 / 2,25 / 44 | 9 / 2,5 / 51 | 12 / 3 / 64 |
| Résistance % | 1 / 1 / 18 | 2 / 1 / 19 | 4 / 2 / 38 | 6 / 2,25 / 44 | 9 / 2,5 / 51 | 12 / 3 / 64 |

Le guide indique un gain renforcé de principale à +15. La valeur finale ne se déduit donc pas d’une simple formule « valeur initiale + quinze fois le gain ». Les gains fractionnaires du guide ne suffisent pas à définir toute la séquence d’arrondis : ne pas inventer les valeurs intermédiaires lorsque cette séquence n’est pas établie.

### Principales fixes des deux cadeaux paternels

L’auteur délègue le choix des statistiques à partir du tableau de la source. Pour Attaque et Défense, le rang 6★ donne 22 à +0 puis +8 par niveau jusqu’à +6 : **22 + 6 × 8 = 70**. HAS-R001 a donc Attaque +70 et HAS-R002 Défense +70. Cette formule ne doit pas être extrapolée à +15 sans respecter son gain final renforcé.

## 4. Amélioration de la principale et des secondaires — DEC-006 et DEC-014

La principale augmente **à chaque amélioration réussie**, de +1 à +15. Le passage de +14 à +15 accorde un gain de principale plus important que les passages ordinaires. Son augmentation n’est pas limitée aux multiples de trois.

**En parallèle**, les paliers +3, +6, +9, +12 et +15 ajoutent ou renforcent une secondaire, sans dépasser quatre secondaires. Les règles jusqu’à +12 suivent la source ; le palier secondaire à +15 est une adaptation explicite du roman (DEC-014).

| Palier | Condition d’ajout | Sinon |
|---|---|---|
| +3 | Aucune secondaire présente : ajouter la première | Renforcer une secondaire existante |
| +6 | Une seule secondaire présente : ajouter la deuxième | Renforcer une secondaire existante |
| +9 | Deux secondaires présentes : ajouter la troisième | Renforcer une secondaire existante |
| +12 | Trois secondaires présentes : ajouter la quatrième | Renforcer une secondaire existante |
| +15 | Aucune cinquième secondaire : les runes ayant suivi les paliers précédents en possèdent déjà quatre | Renforcer une secondaire existante, en plus du gain renforcé de la principale |

Les paliers d’ajout font évoluer le grade affiché : première secondaire, vert ; deuxième, bleu ; troisième, violet ; quatrième, orange. Le rang en étoiles reste distinct. Conserver aussi le grade d’origine dans l’historique pour distinguer une rune blanche améliorée d’une rune native légendaire.

Une rune bleue native renforce donc une secondaire à +3 puis une à +6 : elle garde deux secondaires à +6. Elle en gagne une troisième à +9 et une quatrième à +12. Une même secondaire peut être renforcée plusieurs fois ; les deux cadeaux ont ici une répartition documentée dans `runes.md`.

À +15, cette rune renforce encore une de ses quatre secondaires tout en recevant le gain final renforcé de sa principale. Ne pas présenter ces deux effets comme exclusifs et ne pas inventer de gain numérique universel pour les secondaires.

Les valeurs et gains numériques des secondaires ne sont pas fournis par l’article : les chiffres des deux cadeaux sont des choix individuels pour le roman, pas une table universelle. Mana reste une caractéristique propre au roman déjà validée, absente du système runique décrit par la source.

## 5. Obtention et désignation — règle propre au roman

**CANON — DEC-007 :** le rang d’une rune obtenue sur un monstre dépend du niveau de ce monstre.

| Niveau du monstre | Rang de la rune obtenue |
|---|---|
| 1 à 10 inclus | 1★ |
| 11 à 20 inclus | 2★ |
| 21 à 30 inclus | 3★ |
| 31 à 40 inclus | 4★ |
| 41 à 50 inclus | 5★ |
| 51 à 60 inclus | 6★ |

Cette règle est une création du roman, pas une règle extraite de Summoners War. Elle ne définit ni la probabilité d’obtenir une rune, ni son ensemble, ni sa rareté. Elle n’impose pas à chaque monstre de donner une rune. Les règles au-delà du niveau 60 restent à définir ; ne pas ajouter de rang supérieur à 6★ ni supposer une règle de plafonnement.

Toujours indiquer la rareté et les étoiles d’une rune identifiable dans le récit, les dialogues, fenêtres et références, une fois ces informations connues. Exemple : « rune Fatal rare (bleue), 6★, +6 ». Une explication abstraite du système ou un compteur d’emplacements n’exige pas d’inventer une rune précise. Une information inconnue dans une fiche documentaire doit rester « À DÉFINIR ».

Conséquence sur le butin futur prévu : la rune Vitesse rare (bleue) du loup alpha élite de niveau 25 à 27 sera 3★, sans fixer ses valeurs encore ouvertes. Les cadeaux achetés ou offerts ne changent pas de rang selon le niveau de leur nouveau propriétaire : les deux cadeaux paternels restent rares (bleus), 6★, +6.

### Équipement sans restriction de niveau — CANON

Toutes les runes sont équipables à tout niveau de personnage, quelle que soit leur rareté, leur rang en étoiles ou leur amélioration (DEC-008). Les tranches du tableau d’obtention concernent seulement le niveau du monstre dont provient le butin ; elles ne fixent aucun niveau minimum d’équipement. Un emplacement runique disponible reste nécessaire.

Hasol peut donc équiper dès le niveau 1 la rune Fatal rare (bleue), 6★, +6 et la rune Gardien rare (bleue), 6★, +6 offertes par son père. Ne pas ajouter de restriction liée au niveau du personnage.

## 6. Équivalence des classes avec les étoiles natives de Summoners War

**CANON — DEC-009 :** il s’agit d’une référence d’inspiration pour les personnages, distincte du rang en étoiles de leur équipement.

| Rareté de classe du roman | Référence Summoners War |
|---|---|
| Commune | Monstre 2★ natif |
| Rare | Monstre 3★ natif |
| Légendaire | Monstre 4★ natif |
| Astrale | Monstre 5★ natif |

Hasol, de classe légendaire, doit donc être comparée à un 4★ natif. Les statistiques varient d’un monstre à l’autre au sein d’une même rareté ; il n’existe pas une fiche unique de 4★. Comparer au même niveau, rang actuel et état d’éveil. Les données au rang 6★ niveau maximum ne décrivent pas un 4★ au niveau 1.

Les exemples vérifiés sont conservés dans `../source.md`. Cette équivalence n’adopte pas automatiquement le système d’évolution des personnages, les plafonds de niveaux, l’éveil ou les formules de dégâts du jeu. Mana et Puissance arcanique n’ont pas d’équivalent direct dans les fiches de combat consultées ; ne pas les calculer par une conversion inventée.

**Correction appliquée au chapitre 1 — DEC-010 :** base naturelle de Hasol au niveau 1 : PV 2940, Attaque 199, Défense 182, Vitesse 100, suivant le Danseur du ciel Vent non éveillé, 4★, niveau 1. Ses gains naturels déjà racontés sont conservés : les fiches des niveaux 9 et 10 sont recalculées à partir de cette nouvelle base, sans importer une courbe de progression de Summoners War. Mana et Puissance arcanique gardent leurs valeurs précédentes. Le rééquilibrage éventuel de l’échelle magique reste ouvert ; la comparaison brute entre Attaque et Puissance arcanique ne peut pas être interprétée comme une formule de dégâts.

## 7. Principales fixes et principales en pourcentage — DEC-011

**CANON — intention de progression :** les principales en valeur fixe favorisent les personnages de bas niveau ; les principales en pourcentage deviennent rapidement plus avantageuses avec la croissance des caractéristiques naturelles. Cet enseignement est désormais raconté au chapitre 4, section IV, puis mis en pratique dans le conseil à une cliente, section VII (DEC-023 et DEC-024).

Les principales PV %, Attaque % et Défense % sont admises par cette décision. Leur présence en principales ne valide pas les mêmes caractéristiques en pourcentage comme secondaires ; cette question reste distincte.

Comparer des runes à rang en étoiles et amélioration comparables, et tenir compte de leur grade et de leurs secondaires pour juger l’équipement complet. La supériorité d’une principale ne suffit pas à établir celle de toute la rune. Ne pas transformer le conseil en règle universelle indépendante des valeurs.

**Assiette CANON — DEC-024 :** une principale en pourcentage se calcule sur la caractéristique naturelle, avant l’ajout des bonus fixes runiques. L’exemple pédagogique du chapitre 4 compare Attaque +50 et Attaque +10 % : pour 200 naturels, +50 contre +20 ; pour 500, +50 contre +50 ; pour 2000, +50 contre +200. Ces valeurs ne constituent ni une table par étoiles ni deux nouvelles runes identifiées dans l’inventaire.

La vitesse de bascule recherchée est une intention d’équilibrage ; aucun seuil de niveau universel ni barème de progression naturelle n’est fixé. Les ensembles, l’interaction avec Résonance runique et les arrondis ne sont pas définis par cette seule assiette. Si les chiffres ne permettent pas une bascule rapide, signaler l’écart et demander un arbitrage plutôt que modifier les gains validés.

Les principales fixes Attaque +70 et Défense +70 des deux cadeaux rares (bleus), 6★, +6, restent inchangées au chapitre 1. Leur remplacement futur doit être raconté et consigné, pas imposé rétroactivement.

### Ensembles complets et cumul Gardien — DEC-020

Un ensemble Fatal nécessite quatre pièces, Gardien et Énergie deux pièces. Le chapitre 2 possède quatre Fatal, quatre Gardien et deux Énergie : un Fatal, deux Gardien, un Énergie. Les deux paires Gardien apportent +15 % Défense chacune, soit +30 % au total, sans multiplication des deux bonus. Une pièce isolée n’ajoute pas un ensemble ; les caractéristiques individuelles de la pièce restent néanmoins applicables.

### Principales 3★ de la version de lecture du chapitre 2

Choisies à partir du tableau de la source dans la délégation de l’auteur : principales à +0 Attaque +7, Défense +7, PV +100, Vitesse +3. HAS-R003, Fatal rare (bleue), 3★, passe de +0 à +3 avec Attaque +7 → +12 → +17 → +22, soit +5 par niveau. Les secondaires de cet inventaire et leur gain chiffré sont des choix éditoriaux, pas des valeurs attestées par le guide.

## 8. Mana et Puissance arcanique — repères du roman

**CANON — DEC-015 :** les valeurs suivantes sont des normes de comparaison au niveau 60, pas des plafonds absolus ni une formule de progression.

| Caractéristique | Profil de référence | Norme au niveau 60 |
|---|---|---:|
| Mana | Référence générale donnée par l’auteur | 1000 |
| Puissance arcanique | Classe de soutien | 600 |
| Puissance arcanique | Mage | 2000 |

Hasol possède une classe fonctionnellement **de soutien**, mais sa Puissance arcanique suit un profil **de mage**, pas le profil ordinaire d’un soutien. Sa réserve de mana est hors norme et dépassera largement 1000. Le niveau exact de franchissement et ses valeurs finales ne sont pas encore fixés.

Ce décalage est au cœur du personnage : ses caractéristiques magiques ne lui donnent pas une compétence offensive. Au début, elle ne peut pas exploiter cette puissance comme un mage malgré ses statistiques. Ne pas changer sa classe ou lui accorder un sort pour expliquer les chiffres.

**Futur CANON — DEC-031 :** un premier sort offensif se débloque au niveau 40 et exploite pleinement la réserve de Mana exceptionnelle de Hasol. Elle termine le livre I autour du niveau 45. Il s'agit d'un événement futur, distinct de l'utilisation combattive d'une aura d'arme ; aucune compétence offensive de ce type n'est à introduire avant le niveau 40. Nom, effet, portée, coût, durée, récupération et lien chiffré avec le Mana ou la Puissance arcanique restent **À DÉFINIR**. « Exploiter pleinement » ne signifie pas automatiquement consommer toute la réserve, infliger des dégâts égaux au Mana, ignorer la Défense ou garantir une victoire.

Ces repères complètent l’échelle propre au roman ; ils ne sont pas extraits des fiches de Summoners War. La rareté légendaire, le rôle de soutien et le profil statistique magique sont trois informations distinctes. L’équivalence Légendaire ≈ 4★ natif ne signifie pas qu’Hasol doit reprendre toutes les caractéristiques d’un monstre de soutien.

Les valeurs actuelles du manuscrit restent Mana 30 et Puissance arcanique 20 au niveau 1, 310 et 186 au niveau 9, 355 et 211 au niveau 10. Les nouveaux repères ne les remplacent pas automatiquement et ne définissent pas leurs valeurs intermédiaires. Ne pas calculer les gains par division des normes par soixante ; la progression et la date du dépassement restent à établir.

## 9. Coût des améliorations et fatigue — CANON, DEC-024

- Chaque tentative d’amélioration consomme **des pierres de mana et du Mana personnel de l’artisan**, qu’elle réussisse ou échoue.
- Le coût en Mana augmente avec la difficulté, notamment selon le rang en étoiles, le grade et le palier d’amélioration visé. Les valeurs exactes et l’usage du grade d’origine ou du grade actuel dans une future table restent **À DÉFINIR** ; ne pas inventer de formule.
- La réserve disponible limite le travail possible. Le repos restaure le Mana ; des potions peuvent restaurer la réserve sans supprimer toute fatigue mentale. Les rythmes de récupération, les effets chiffrés des potions et le nombre de tentatives réalisables par jour restent **À DÉFINIR**.
- La fatigue mentale limite la concentration même lorsqu’il reste du Mana. Posséder une grande réserve ne garantit ni précision, ni expérience, ni réussite. Ne pas déduire d’un soin magique une récupération automatique de l’attention.
- Au chapitre 4, Orven découvre l’endurance de Hasol : **355 Mana naturels**, bonus runique connu **+20**, réserve disponible partiellement consommée mais non chiffrée. Ce constat ne donne ni un ratio d’endurance par rapport aux apprentis ni le taux d’échec de Bénédiction runique, réservé au chapitre 7.
- Les ressources de l’épreuve du chapitre 3 sont fournies par l’atelier. Le chapitre 4 montre des commandes de clients avec budget et tentatives autorisées limités ; l’apprentie ne peut pas engager des ressources ou un palier supplémentaire sans autorisation.
- Les échecs montrés aux chapitres 3 et 4 consomment les ressources mais laissent les runes intactes à leur niveau précédent. Cela n’établit pas les conséquences de tous les échecs aux paliers non racontés.
- L’absence de montant ou de décompte de Mana dans une ancienne fenêtre ne signifie pas que le coût est nul. Aucun débit rétroactif chiffré n’est ajouté aux chapitres précédents.
- **Précision narrative — DEC-027 :** Hasol connaît le coût personnel en Mana avant sa première journée complète. Le chapitre 4 adapté montre l’apprentissage du suivi de sa réserve et de ses limites en situation, pas la découverte tardive de la règle. Aucune modification des coûts, de la régénération ou des caractéristiques n’en découle.

## 10. Armes imprégnées d’une aura — seuil d’utilisation, CANON DEC-028

- Il faut être **au minimum niveau 10 pour utiliser une arme imprégnée d’une aura**. Le seuil concerne le personnage qui utilise l’arme, pas l’artisan qui l’a enchantée.
- Cette restriction est distincte de l’équipement des runes, qui reste sans niveau minimum (DEC-008). Elle ne fixe aucune condition supplémentaire pour les armes ordinaires.
- Hasol ne pouvait donc pas utiliser une telle arme pendant ses années d’Académie, où elle restait sous le niveau 10. Le seuil explique pourquoi elle n’avait pas eu recours à cette possibilité auparavant ; il ne signifie pas qu’elle ignorait l’existence des auras.
- L’explication est prévue au chapitre 5, à l’occasion de la découverte de l’aura de l’arme de Zio et de l’éventuelle visite chez le forgeron. Elle n’a pas encore été racontée.
- Les conséquences exactes d’une tentative d’utilisation sous le niveau 10 restent **À DÉFINIR** : ne pas inventer blessure, rejet de l’arme, perte d’enchantement ou consommation de Mana. Aucune exception liée à l’origine de l’aura n’est établie.
- Cette décision ne valide pas à elle seule les coûts, durées, effets ou modalités des enchantements et d’Aura runique encore à arbitrer pour la suite.

## 11. XP des boss, compteurs et moyens d'Hasol — futur CANON DEC-032

- Dans la trajectoire future d'Hasol, l'essentiel de l'XP provient des boss de donjon après l'abandon rapide du farm intensif de petits monstres au profit du groupe. Aucun montant, bonus de boss, mécanisme de partage ou barème d'XP universel n'est défini par cette orientation.
- Croissance runique suit les monstres admissibles, pas le volume d'XP. Une élimination de boss ne doit pas être transformée en plusieurs centaines d'éliminations parce qu'elle rapporte beaucoup d'XP. Le seuil de 1 000 reste inchangé ; l'attribution des éliminations en groupe ne se déduit pas du seul partage d'XP et reste à préciser avant un calcul détaillé.
- Cette activité permet de monter de niveau tout en franchissant peu souvent les seuils de mille monstres. L'évolution ultérieure DEC-038 ajoute un autre mode de gain sans modifier cette observation sur le compteur initial. Le nombre total de cercles à vingt-cinq ans et en fin de livre reste **À DÉFINIR**, sans calcul automatique depuis le niveau du personnage.
- Vers vingt-cinq ans, Œil runique contribue à la réputation artisanale et à des moyens financiers colossaux, suffisants pour financer des améliorations personnelles jusqu'à +15. La capacité à payer ne garantit ni la réussite de chaque tentative ni un travail illimité ; temps, Mana et fatigue restent applicables.
- La vue des caractéristiques finales prédéterminées à +15 ne fixe pas les probabilités de réussite et ne change pas les affixes. Les runes effectivement améliorées doivent être suivies individuellement, sans créer un inventaire futur chiffré absent des sources.

## 12. Équipes et accès aux donjons — CANON DEC-035

- Une équipe compte au maximum cinq membres et cinquante points de classe. Les deux plafonds s'appliquent simultanément ; une place libre ne suffit pas si le budget de points est épuisé.
- L'accès aux donjons demande **au minimum trois membres**. Les chasses extérieures en solo et en duo ne sont pas interdites par cette règle.
- Le duo Hasol/Yoon (20 + 10 = 30 points) ne remplit pas ce minimum. L'adhésion de Ray **commun**, cinq points (DEC-036), porte le groupe à trois membres, 35/50, accès rendu possible sous cette condition d'effectif. Ne pas en déduire qu'il n'existe aucune autre condition de donjon.
- Zio rare rejoint ultérieurement le trio : quatre membres, 45/50 (20 + 10 + 5 + 10). Le futur Ranger commun prévu par DEC-037 ajoute cinq points : cinq membres et 50/50. Le calendrier reste à définir ; cette adhésion future de Zio ne vaut pas entrée dès sa première supervision.
- Nature, contrôle et exceptions de la restriction de donjon, statut d'un accompagnateur extérieur et conséquences d'une perte de membre en cours d'expédition restent **À DÉFINIR**. Ne pas inventer verrou magique, sanction, partage d'XP ou règle de butin.

## 13. Ranger et apprentissages futurs d'Hasol — CANON DEC-037

- La Ranger commune du groupe est **Samia Claire** (DEC-041) ; elle combine archerie, détection des pièges et ouverture des coffres. Les techniques et compétences exactes du personnage ne sont pas encore décrites.
- Vers la fin du livre I, Hasol apprend ces fonctions d'exploration auprès de Samia. Cet apprentissage conduit à une **amélioration du même passif Œil runique**, qui conserve son nom et ses effets de lecture des runes tout en permettant de voir les pièges. Ce n'est ni un second passif ni un renommage en Œil arcanique.
- **Main runique** est un sort actif permettant d'ouvrir les coffres, acquis à la suite de cet apprentissage. Il ne s'agit pas du premier sort offensif du niveau 40 ; aucun effet de combat n'est établi pour Main runique.
- Déclencheurs exacts de l'évolution, niveaux, coûts, portée, durée, récupération, difficulté, types de pièges et coffres concernés restent **À DÉFINIR**. Détecter ne signifie pas automatiquement désamorcer ; ouvrir des coffres ne signifie pas contourner toute protection ou réussir sans limite.
- Dans le livre II, l'évolution d'Œil runique appartient à l'ancien passif accessible avec Arcaniste Astral ; les adaptations détaillées de cette classe restent à documenter. **Main runique doit être réapprise rapidement**, selon des conditions encore à définir. Aucun accès automatique au niveau 1 ou transfert global des anciennes compétences actives n'est adopté.
- Après ce réapprentissage, Hasol pourra couvrir ces fonctions sans Ranger indispensable dans l'équipe. Cela ne supprime pas l'intérêt de cette classe ni ne fixe le devenir du personnage dans la seconde chronologie.

### Cas futur du boss invocateur — DEC-039

- Un boss de donjon niveau 32 invoque en masse des monstres niveau 11 tant qu'un piège n'est pas désactivé. Le groupe de quatre doit fuir et Zio propose un Ranger avant le retour ; il s'agit d'un cas narratif précis, pas du fonctionnement universel des boss ou des donjons.
- Position et nature du piège, débit et limites des invocations, moyens de le repérer et de le désactiver, comportement du boss après désactivation et résultat du retour **À DÉFINIR**. La désactivation n'établit pas une victoire automatique ; aucune invulnérabilité préalable du boss n'est fixée.
- **Admissibilité précisée par DEC-040 :** les invocations de ce donjon peuvent alimenter Croissance runique lorsqu'Hasol les élimine personnellement et remplit les conditions de niveau du compteur initial. L'auteur prévoit qu'elle exploite ce mécanisme dans sa seconde vie. XP, partage, cadence, nombre exact d'invocations et gains restent **À DÉFINIR** ; ne pas inventer un plafond, une interdiction de farm ou une source infinie d'XP.
- **Fenêtre connue :** les monstres niveau 11 satisfont les seuils de l'ancien effet quand Hasol est niveau 10–19 (monstres 1+) et 20–29 (monstres 10+). Dès son niveau 30, ils ne satisfont plus l'exigence de monstres 20+. L'accès au passif dès le niveau 1 d'Arcaniste Astral ne définit pas à lui seul son admissibilité avant le niveau 10.
- Garder le piège actif pour produire des invocations ne signifie pas achever le boss plusieurs fois. Les invocations niveau 11 ne sont pas des boss et n'alimentent pas le compteur de cent boss de DEC-038. Les conditions d'accès à trois membres restent applicables ; le souvenir d'Hasol et son autonomie technique n'accordent pas une entrée en solo.

## 14. Évolution de Croissance runique après cent boss — futur CANON DEC-038

- **Déclencheur :** cent boss de donjon achevés personnellement par Hasol ; ce jalon survient vers le niveau 38 dans la trajectoire prévue. Le niveau 38 n'est pas une condition minimale supplémentaire fixée pour le déblocage. Achever personnellement ne signifie pas devoir combattre seule : un combat de groupe peut compter si elle porte le coup final.
- **Nouvel effet :** un cercle de Mana par tranche de cent boss de donjon personnellement achevés, **quel que soit leur niveau**. Ne pas ajouter de seuil de niveau de boss ou de dégressivité non décidée.
- **Premier gain immédiat :** les cent boss qui déclenchent l'évolution donnent son premier cercle ; les gains suivants correspondent aux totaux 200, 300, etc. Ne pas demander cent autres boss pour ce premier gain ni compter les cent initiaux deux fois.
- **Cumul confirmé :** l'ancien effet par mille monstres admissibles reste actif. Un même boss peut avancer le compteur des boss et, s'il remplit les conditions de l'ancien effet, celui des mille monstres. Il reste une seule élimination dans le compteur initial ; son XP ne le transforme pas en un grand nombre de monstres.
- **Suivi :** conserver deux compteurs distincts et leurs gains déjà attribués. Si les deux seuils sont franchis sur le même boss, chaque effet accorde son gain ; ne pas réattribuer les anciens paliers du compteur de mille au moment de l'évolution.
- **État futur :** aucun centième boss ni cercle supplémentaire n'est réputé déjà acquis dans les chapitres actuels. Le total de cercles, l'équipement associé, le nombre de boss avant la fin du livre et le chapitre exact restent **À DÉFINIR**.
- **Livre II :** l'évolution relève du passif futur hérité, mais ses compteurs dans la seconde vie et leur éventuel report ne sont pas fixés. Ne pas transférer automatiquement les cent boss ou les cercles gagnés de la première chronologie.

## 15. Sage runique de Yoon : soutien et cercles au sol — CANON DEC-046

| Capacité | Forme fixée | Obtention et usage connus |
|---|---|---|
| Résonance runique | Renforcement actif ciblé, temporaire, principales des runes ; ajoute les deux premières secondaires de chaque rune au niveau 40 | Disponible à la rencontre niveau 5 ; niveau initial exact à définir ; évolution 40, DEC-050 |
| Chant runique | Zone de soin progressif posée ; pas de canalisation continue | Disponible à la rencontre niveau 5 ; niveau initial exact à définir |
| Domaine des Entraves Runiques | Zone de contrôle de foule par ralentissement des ennemis | Prochain sort, niveau 20 ; pas de déblocage déplacé au niveau 10 |
| Second soin, nom à définir | Marque runique posée sur un allié ; soin sur la durée ciblé | Niveau 30, DEC-049 ; distinct du cercle de soin au sol |
| Tempête arcanique | Zone posée de dégâts sur la durée, cercle rouge runique | Niveau 50, DEC-048 ; aucun usage anticipé au niveau 30 |

- Yoon est une soutien polyvalente. Son soin sur la durée reste très inférieur à celui d'une soigneuse pure ; ce principe qualitatif ne donne ni taux, ni plafonnement ni ratio universel de soins.
- Elle pose ses zones en **cercles au sol avec des écritures runiques**, signature de Sage runique. Rayon, portée de placement, durée, limites de cumul, mobilité ou déplacement éventuel des cercles et interactions entre zones restent **À DÉFINIR**.
- **Couleurs narratives — DEC-047 et DEC-048 :** vert pour la zone de soin, violet pour la zone de ralentissement, rouge pour Tempête arcanique au niveau 50. Ces couleurs décrivent les effets dans le monde ; elles ne remplacent pas les conventions HTML des bonus runiques et temporaires.
- **Tempête arcanique — DEC-048 :** sort actif de zone infligeant des dégâts sur la durée. Nom et niveau 50 fixés ; coût, puissance, assiette des dégâts, durée, rayon, cadence, récupération, alliés éventuellement affectés, persistance hors zone et cumul avec les autres cercles **À DÉFINIR**. Le nom ne donne ni foudre, vent, projection ou effet offensif instantané supplémentaires. Ne pas déduire des compétences d'Hasol une formule applicable à ce sort de Yoon.
- **Marque de soin — DEC-049 :** au niveau 30, second soin sur la durée sous forme d'une marque runique posée sur un allié. Ce libellé est descriptif, pas un nom officiel décidé. Le ciblage distingue ce soin du cercle au sol ; ne pas supposer qu'il affecte plusieurs personnes ou reste actif indéfiniment. Coût, durée, cadence, assiette, puissance par rapport au cercle, récupération, portée, nombre de marques et cumul **À DÉFINIR**. Ce sort ne garantit pas la puissance de soins d'une soigneuse pure.
- Le soin est posé, permettant à Yoon d'agir ensuite ; l'ancienne version qui exigeait un chant constamment maintenu par concentration est remplacée. Cela ne définit pas le temps de lancement, le maintien en Mana ou les possibilités exactes de plusieurs sorts simultanés. Le coût de maintien déjà établi du Domaine n'est pas supprimé par analogie.
- Résonance affecte l'allié choisi, pas automatiquement tous les alliés proches. Avant le niveau 40 de Yoon, seules les principales sont amplifiées. Au niveau 40, DEC-050 ajoute les deux premières secondaires présentes sur chaque rune ; les secondaires suivantes et les bonus d'ensemble restent exclus. Principales fixes ou en pourcentage, modalités de calcul et amplification numérique à définir.
- **Évolution de Résonance — DEC-050 :** l'actif ciblé reste actif ciblé, sans conversion en aura passive. Une rune sans secondaire ne reçoit pas d'affixe, une rune n'en ayant qu'une ne bénéficie que de celle-ci. L'ordre exact désignant les deux premières secondaires (apparition ou affichage), les coefficients appliqués et leur interaction avec les autres contributions restent **À DÉFINIR** ; ne pas inventer un facteur identique pour toutes les caractéristiques ou une règle d'arrondi.
- Paramètres de soin de la transmission (10 % des PV maximums de Yoon toutes les cinq secondes, cinq mètres, trente secondes) non adoptés automatiquement. Avant une démonstration chiffrée, définir l'assiette et vérifier le résultat par rapport au rôle de soutien souhaité.
- Le niveau final de Yoon est **54 au chapitre 16** ; Domaine au niveau 20, marque de soin au 30, évolution de Résonance au 40 et Tempête arcanique au 50 sont établis. Caractéristiques, gains intermédiaires, paramètres et autres capacités éventuelles restent **À DÉFINIR**. Ce repère est distinct du niveau final approximatif 45 d'Hasol, sans nouvelle formule d'XP.

## 16. Questions à définir

- Tables complètes par rang des principales PV, Attaque, Défense, Vitesse, Mana et éventuelles autres caractéristiques, au-delà des valeurs adoptées ci-dessus.
- Valeurs initiales et gains des secondaires, distincts des tables ci-dessus.
- Barèmes numériques des renforcements des secondaires, au-delà des valeurs individuelles des deux cadeaux.
- Arrondis intermédiaires et calcul des bonus d’ensemble.
- Effets exacts de précision et résistance, taux naturels de critique et dégâts critiques, plafonds éventuels et calculs associés.
- Les valeurs individuelles du don maternel dans la version de lecture du chapitre 2 restent à valider avec le texte (DEC-019). La composition quatre Fatal, quatre Gardien, deux Énergie est fixée par DEC-020, sans nouvelle question sur les nombres par ensemble.
- Obtention de runes sur les monstres de niveau supérieur à 60 et probabilités de butin.
- Progression naturelle de Hasol : croissance physique après la nouvelle base 4★ et progression magique cohérente avec DEC-015. Les normes magiques au niveau 60 sont connues, mais les courbes et le niveau de franchissement de 1000 Mana par Hasol restent à définir.
- Tables des principales permettant de vérifier la bascule rapide souhaitée entre fixe et pourcentage ; l’explication et l’assiette naturelle sont désormais établies au chapitre 4, sans ordre de calcul des ensembles ou arrondis supplémentaires.
- Coûts en Mana et en pierres par tentative, traitement du grade initial ou actuel, régénération, effets des potions et limites de travail ; ne pas transformer les exemples ou la réserve 355 en barème.

Ne pas appliquer automatiquement les coûts, les restrictions d’emplacements, les règles de retrait ou de destruction, ni l’absence d’échec jusqu’à +3 de Summoners War. Le roman prévoit un échec lors d’une tentative de passage à +2 au chapitre 3.
