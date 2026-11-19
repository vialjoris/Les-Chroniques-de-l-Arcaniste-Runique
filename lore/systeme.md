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

**CANON — intention de progression :** les principales en valeur fixe favorisent les personnages de bas niveau ; les principales en pourcentage deviennent rapidement plus avantageuses avec la croissance des caractéristiques naturelles. Orven expliquera ce principe dans une scène future, dont le placement n’est pas encore fixé.

Les principales PV %, Attaque % et Défense % sont admises par cette décision. Leur présence en principales ne valide pas les mêmes caractéristiques en pourcentage comme secondaires ; cette question reste distincte.

Comparer des runes à rang en étoiles et amélioration comparables, et tenir compte de leur grade et de leurs secondaires pour juger l’équipement complet. La supériorité d’une principale ne suffit pas à établir celle de toute la rune. Ne pas transformer le conseil en règle universelle indépendante des valeurs.

La vitesse de bascule recherchée est une intention d’équilibrage ; aucun seuil de niveau universel, barème de progression naturelle ou ordre de calcul nouveau n’est fixé. Avant un exemple chiffré, vérifier les valeurs des deux principales, l’assiette du pourcentage, les arrondis et la progression du personnage. Si les chiffres ne permettent pas une bascule rapide, signaler l’écart et demander un arbitrage plutôt que modifier les gains validés.

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

Ces repères complètent l’échelle propre au roman ; ils ne sont pas extraits des fiches de Summoners War. La rareté légendaire, le rôle de soutien et le profil statistique magique sont trois informations distinctes. L’équivalence Légendaire ≈ 4★ natif ne signifie pas qu’Hasol doit reprendre toutes les caractéristiques d’un monstre de soutien.

Les valeurs actuelles du manuscrit restent Mana 30 et Puissance arcanique 20 au niveau 1, 310 et 186 au niveau 9, 355 et 211 au niveau 10. Les nouveaux repères ne les remplacent pas automatiquement et ne définissent pas leurs valeurs intermédiaires. Ne pas calculer les gains par division des normes par soixante ; la progression et la date du dépassement restent à établir.

## 9. Questions à définir

- Tables complètes par rang des principales PV, Attaque, Défense, Vitesse, Mana et éventuelles autres caractéristiques, au-delà des valeurs adoptées ci-dessus.
- Valeurs initiales et gains des secondaires, distincts des tables ci-dessus.
- Barèmes numériques des renforcements des secondaires, au-delà des valeurs individuelles des deux cadeaux.
- Arrondis intermédiaires et calcul des bonus d’ensemble.
- Effets exacts de précision et résistance, taux naturels de critique et dégâts critiques, plafonds éventuels et calculs associés.
- Les valeurs individuelles du don maternel dans la version de lecture du chapitre 2 restent à valider avec le texte (DEC-019). La composition quatre Fatal, quatre Gardien, deux Énergie est fixée par DEC-020, sans nouvelle question sur les nombres par ensemble.
- Obtention de runes sur les monstres de niveau supérieur à 60 et probabilités de butin.
- Progression naturelle de Hasol : croissance physique après la nouvelle base 4★ et progression magique cohérente avec DEC-015. Les normes magiques au niveau 60 sont connues, mais les courbes et le niveau de franchissement de 1000 Mana par Hasol restent à définir.
- Placement de l’explication d’Orven sur principales fixes et pourcentages ; tables et règles de calcul permettant de vérifier la bascule rapide souhaitée.

Ne pas appliquer automatiquement les coûts, les restrictions d’emplacements, les règles de retrait ou de destruction, ni l’absence d’échec jusqu’à +3 de Summoners War. Le roman prévoit un échec lors d’une tentative de passage à +2 au chapitre 3.
