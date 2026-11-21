# Audit d’intégration — chapitres 5 à 9

## Périmètre et statut

Intégration locale du 21 novembre 2026, sur autorisation explicite de l’auteur relayée dans la mission : chapitres 5 à 9 validés, chapitre 5 en **V2**, corrections techniques et fenêtres autorisées, sans réécriture générale.

**CANON :** les décisions explicites récentes priment sur les anciennes variantes du plan. Un nouvel arbitrage direct de l’auteur, reçu pendant l’intégration, valide le soin de Yoon et le remplacement actif de Lame par Arcanique. Le reliquat des éliminations reste non résolu ; la validation des textes ne le fixe pas silencieusement à zéro.

Fichiers de cette intervention : `roman.md` et le présent rapport seulement. Les références sont synchronisées séparément par la session principale ; ce rapport ne prétend pas les avoir modifiées. Aucun chapitre 10, commit ou push. `new.txt` et `old.txt` sont conservés intacts.

## 1. Provenance et frontières retenues

Les numéros ci-dessous désignent les lignes de `new.txt` au moment de l’intégration, pas les lignes du manuscrit résultant.

| Chapitre | Version retenue | Début et fin inclusifs | Contrôle des frontières |
|---|---|---|---|
| 5 — Le premier lien | V2, après le marqueur « Chap v2 » | 10967–15157 | Titre narratif → « Fin du chapitre 5 ». La première version, terminée ligne 10960, n’est pas importée. |
| 6 — Deux chemins, un même objectif | Texte complet transmis | 15170–18270 | Exclusion de l’introduction conversationnelle 15162–15168 et du commentaire postérieur à la fin. |
| 7 — Le talent d’une légende | Texte dont la validation est relayée par la transmission suivante | 18305–21697 | Les consignes « Chap7 codex » commencent après le texte ; elles servent à identifier les décisions, pas à remplir le roman. |
| 8 — La puissance des dix runes | Texte complet transmis | 22013–25089 | Courriel précédent et ancienne version du chapitre 9 suivante exclus. |
| 9 — Douze cercles | Dernière version complète, continuité du cadeau corrigée | 29195–33081 | Titre Markdown → fin en gras. Le récapitulatif « Continuité corrigée », la validation et les idées sur Ray/anneau/Aimant restent hors du récit. |

Les versions narratives retenues ont été lues entièrement. Les chapitres mobiles 1 à 4 ne sont pas réimportés. Les paragraphes, dialogues, scènes et fins des cinq textes sont conservés, sous les retouches ciblées recensées ici. Les blocs de notification sont convertis en HTML, sans prétendre récupérer des images absentes.

Les en-têtes de courriels, adresses, horaires d’envoi et commentaires de conversation sont hors des plages importées. Titres uniformisés en `# Chapitre N — …`, sections internes en `## I. …`, ancres `chapitre-5` à `chapitre-9`, séparateurs entre chapitres. Les lignes vides multiples de la transmission sont ramenées à des espacements Markdown ordinaires.

### Protection absolue du manuscrit existant

Le manuscrit antérieur complet a été conservé comme préfixe binaire exact pendant l'import, puis **seul son sommaire a été complété avec les liens 5 à 9**. Le corps des chapitres 1 à 4 reste identique octet pour octet. Référence : `/tmp/opencode/arcaniste-integration-20261121/avant/roman.md`.

- Longueur du manuscrit avant import : **206 156 octets**.
- SHA-256 de cet instantané avant import : `cd6580da3243670d7c98d4b1d4cdf91826ab5cc2a8fa3e2f1dc1a332507d581c`.
- Aucun octet des chapitres 1 à 4 n’est modifié, y compris leur mise en page et leurs fenêtres.
- Le sommaire final contient les liens 1 à 9 ; cette modification de navigation ne change aucun texte des chapitres protégés.

## 2. Fiche de continuité appliquée

| Chapitre | Point de départ et jalons conservés | Situation finale et limites |
|---|---|---|
| 5 | Hasol niveau 10, dix cercles, équipement maternel/paternel antérieur ; rencontre de Yoon, niveau 5, seize ans, et de Zio, Gardien rare niveau 45 ; deux chasses, morsure nouvelle, secours, soins, forgeron et confiance. | Duo officiel 2/5 et 30/50 ; Zio supervise sans rejoindre. Hasol 11 et Aura runique. Dix runes personnelles conservées ; aucun sacrifice immédiat. Progression intermédiaire de Yoon non chiffrée par l’import. |
| 6 | Travail d’Hasol et études de Yoon, Samia à l’Académie ; achat de runes de récupération, épée d’essai distincte de l’arme de chasse ; essais coûteux. | Infiltration découverte sur critique au lancement ; victoire sur les loups 7, 8, 9 dans le passage. Hasol reste 11, dix cercles et dix runes ; aucune nouvelle fiche naturelle extrapolée. |
| 7 | Mesure des deux propriétés de Bénédiction par Orven ; épreuve et commandes du Griffon d’Argent ; acquisition de deux Arcanique ; famille et entraînement conservés. | 4 Fatal, 2 Gardien, 2 Énergie, 2 Arcanique ; six +6 et quatre +3. Les deux cadeaux paternels rares bleus, 6★, +6 restent intacts ; deux Gardien maternelles stockées. Hasol reste 11. |
| 8 | Chasse du samedi, pertes défensives et critiques à l’épée, préparation du danger puis alpha niveau 12. | Victoire du duo sans activation d’Aura runique ; griffures au flanc, choc à l’épaule, bandages, soins et repos nécessaires. Aucun montant d’XP, nouveau niveau ou gain naturel inventé. |
| 9 | Travail rémunéré, ressources limitées, améliorations choisies à +9, chasses personnelles et exercices de Yoon sur plusieurs périodes. | Hasol 19, douze cercles, 4 Fatal + 4 Arcanique + 4 Gardien. Yoon 24 ; Domaine obtenu au 20. Les deux Énergie +9 passent à Yoon, ses anciennes +6 sont conservées. L’ensemble Vitesse reste un objectif, non un équipement acquis. |

Le père est vivant, affectueux mais distant ; la réaction au Griffon d’Argent ne devient pas une dispute majeure ajoutée au chapitre 7. Aucune réconciliation, décès, adhésion de Ray/Zio/Samia ou révélation d’Œil runique n’est anticipé. Le secret des cercles est confié aux personnes prévues ; les manifestations publiques de fin du chapitre 9 restent un point de vigilance de la source, sans témoins ou conséquences inventés.

## 3. Retouches techniques précises

### Yoon et éléments

- **Vague runique — CANON de la session :** attaque de **Lumière**, niveau 1, coût **5 Mana**, puissance annoncée **20 % de sa Puissance arcanique**, portée **10 mètres**, incantation **5 secondes**, aucune récupération. Fenêtre ajoutée après la présentation du sort, sans calculer des dégâts finaux face à une Défense inconnue.
- La lueur initiale bleutée est devenue blanche et dorée (11447) ; les ondes explicitement bleues/bleutées de ce sort sont devenues lumineuses (12035, 15802, 17886, 22517). Les couleurs bleues des runes ne sont pas changées. **Seule Vague est définie de Lumière, pas toute la classe Sage runique.**
- Incantation explicitée dans le premier tir (12035), commencement plutôt que tir instantané après le cercle de soin (12139), vague déjà préparée lorsqu’elle est déviée pendant la chute (12265). Contre l’alpha, Yoon commence l’incantation pendant qu’Hasol retient la gueule avec son épée, puis achève ses cinq secondes avant l’avertissement et le tir (raccord autour de 23793–23823). Aucun effet de contrôle ajouté. Les échanges de combat ne reçoivent pas un chronométrage complet artificiel.
- Résonance reste un **actif ciblé temporaire**, principales seules aux niveaux racontés ; aucune secondaire ou ensemble amplifié. L’évolution aux deux premières secondaires au niveau 40 n’est pas anticipée.
- Chant reste un cercle **vert posé**, autonome après lancement ; Yoon peut agir ensuite. Aucun retour au chant continuellement canalisé. **Dernier arbitrage CANON :** chaque impulsion restaure **10 % des PV maximums de Yoon toutes les cinq secondes**. Cette assiette et cette cadence sont désormais validées ; les scènes du cadeau Énergie sont donc conservées sans réserve de formule.
- Domaine reçoit explicitement sa couleur violette dans sa manifestation (31797) et sa fenêtre de niveau 20 : ralentissement, pas immobilisation, alliés épargnés, maintien en Mana, résistance partielle des puissants.
- Rappel élémentaire ajouté au chapitre 5 : Eau > Feu > Terre > Eau, dégâts finaux et précision ×1,25 dans le sens favorable, ×0,75 en sens inverse ; Lumière et Ténèbres neutres entre elles, chacune ×1,20 face au cycle et ×0,80 dans l’autre sens. Aucun total de dégâts dérivé de ces coefficients.

### Aura, critiques, artisanat et raccords

- Aura : **200 Mana, une rune définitivement détruite, 24 heures**, arme d’Hasol ou d’un allié ; première expérimentation sur l’épée d’essai, pas sur une rune équipée. L’enchantement du forgeron reste distinct de ce pouvoir.
- Infiltration : critique **au lancement** d’Aura, fenêtre de **30 secondes**, plancher égal à la Puissance arcanique actuelle, aucune réduction de Défense. Les critiques ordinaires de l’épée n’activent ni Infiltration ni un nouveau sacrifice de rune.
- Formules critiques reprises des directives de validation du chapitre 7, `new.txt` 21777–21785 : `CC = 5 + PA effective / 80 + Bonus CC` ; `DCC = 150 + PA effective / 100 + Bonus DCC`. Aucun surcritique ni dégâts finaux inventés. Le bonus Arcanique de 1 200 correspond à +15 points de CC et +12 points de DCC, pas au taux total d’Hasol.
- Bénédiction : 20/80 contre 14/80 = 25 % contre 17,5 % d’échec, soit **7,5 points** et **30 % de réduction relative**. Maximum de renforcement variable très fréquent, mais non garanti, sans fréquence numérique nouvelle ni choix d’affixe. Les gains antérieurs ne sont pas réécrits.
- Le Mana d’Hasol prétendument dépensé pendant la chasse sans activation racontée (14805) est remplacé par ses **forces** sollicitées. Aucun débit personnel fictif n’est ajouté ; l’anomalie de la source est conservée dans la réserve MANA-01.
- La fin du chapitre 6 renvoie aux occupations respectives **« À la reprise de la semaine »**, plutôt qu’au lendemain du samedi (18258).
- Le surnom paternel « ma princesse » n’est plus présenté au chapitre 7 comme inédit depuis longtemps : Hasol l’a entendu au chapitre 4, mais la proximité reste non retrouvée (21311).
- Le souvenir de l’annonce des nouvelles runes au chapitre 8 ne fixe plus « mercredi » alors que la scène correspondante du chapitre 7 précède le samedi : **« Je t’en ai parlé. »**, sans date inventée et sans changer l’attribution de la réplique (22191).

### Désignation et inventaire des runes

Les mentions nommées de pièces reçoivent leurs grades/étoiles établis ou **À DÉFINIR**, sans confondre un nom d’ensemble abstrait avec une rune acquise. Les pièces d’atelier non documentées ne se voient pas attribuer les étoiles de l’équipement personnel.

- Cadeaux paternels : Fatal et Gardien **rares bleues, 6★, +6** inchangées. La Gardien désignée seulement « de même qualité » au chapitre 7 est explicitée.
- Maternelles : **3★** conservées ; grades actuels ou association individuelle manquants signalés plutôt que déduits d’une distribution arbitraire des six +6/quatre +3.
- Deux premières Arcanique : grades, étoiles, valeurs et secondaires **À DÉFINIR**. Deux suivantes achetées au chapitre 9 : **2★, +6**, grades et affixes chiffrés **À DÉFINIR**. Aucun transfert de leur rang 2★ sur les deux premières.
- Les deux Énergie maternelles arrivées à +9 sont désignées **épiques violettes, 3★** : grade actuel résultant des règles d’ajout validées, distinct de leurs grades natifs rare bleu et peu commun vert. Aucun affixe ou gain chiffré supplémentaire n’est créé.
- Les deux anciennes runes personnelles de Yoon sont conservées à +6, sans ensemble, étoiles ou caractéristiques inventés.
- Les runes communes blanches 1★ achetées pour les essais sont distinctes des cadeaux et commandes ; la pierre blanche prise dans le lot avant son identification conserve un rang **À DÉFINIR**.

## 4. Fenêtres HTML

**61 fenêtres au total : 39 conversions de blocs/notifications transmis et 22 ajouts ciblés.** Les ajouts comprennent les douze fenêtres initiales et dix encadrés de repères demandés ensuite explicitement par l’auteur, un à l’ouverture et un à la clôture de chaque chapitre 5–9. Classes réutilisées : `system-window`, `character-sheet`, `rune-window`, `system-header`, `rune-bonus`, `temporary-bonus`, `upgrade-badge`, `legendary-text`, `passive-badge`, `success`, `level-up`, `monster`. Aucune modification de `style.css`.

| Chapitre | Conversions | Ajouts ciblés |
|---|---:|---|
| 5 | 5 : Résonance, statut runique, équipe, niveau 11, Aura | 7 : Zio 45 ; Yoon 5/seize ans ; Vague ; affinités ; seuil d’arme à aura ; deux encadrés de repères. |
| 6 | 2 : critique/Infiltration ; loups 7/8/9 | 4 : premier sacrifice pour Aura de Feu ; bilan du passage étroit ; deux encadrés de repères. |
| 7 | 5 : Arcanique ; réussite +6 de la guilde ; identification Arcanique ; équipement après remplacement ; bilan six +6/quatre +3 | 6 : formules critiques ; comparaison des séries ; deux observations sur Bénédiction ; résultat du mannequin sans durée exacte inventée ; deux encadrés de repères. |
| 8 | 5 : équipement partagé ; deux critiques ; identification de l’alpha ; élimination/XP non chiffrée | 3 : Résonance ciblée au moment décisif ; deux encadrés de repères. |
| 9 | 22 : améliorations, statuts, compteurs, critiques, onze/douze cercles, Arcanique 2★, ensemble Arcanique, cadeau Énergie, Domaine au 20, équipement final et Yoon 24 | 2 : encadrés de repères à l’ouverture et à la clôture. |

### Repères de début et de fin — demande complémentaire explicite

Les dix encadrés portent les titres **« REPÈRES DU LORE — OUVERTURE »** et **« REPÈRES DU LORE — CLÔTURE »**, ainsi que la mention visible **« Repères pour le lecteur — hors des notifications des personnages. »** Ils ne constituent donc ni des écrans nouvellement perçus par les personnages, ni des scènes ajoutées. Chacun contient quatre ou cinq puces courtes, après le titre et avant la première scène, ou après le dernier paragraphe narratif et avant la fin du chapitre.

| Chapitre | Règles rappelées à l’ouverture | Règles rappelées à la clôture |
|---|---|---|
| 5 | Dix emplacements ; dimensions d’une rune ; plafonds d’équipe et poids des classes. | Aura disponible au niveau onze, coût, sacrifice, durée et seuil du porteur. |
| 6 | Aura déjà connue, ressources et limites d’endurance ; aucune annonce d’Infiltration. | Condition critique d’Infiltration, plancher, trente secondes et absence de garantie. |
| 7 | Bénédiction qualitative, consommation des tentatives et limites des commandes ; aucune mesure anticipée des deux effets. | Réduction relative observée, maximum variable non garanti, quatre pièces Arcanique et limites des runes. |
| 8 | Résonance limitée aux principales ; critique à l’épée distinct ; Chant posé et soin connu. | Placement et coordination, contrepartie défensive, zone de soin et blessures persistantes. |
| 9 | Coûts de +9, paliers, condition des quatre pièces sans les annoncer acquises ; XP distincte des éliminations. | Douze emplacements, composition Fatal/Arcanique/Gardien et bonus séparés ; non-double-comptage ; Domaine au niveau vingt. |

**Fidélité :** aucun paragraphe narratif, dialogue ou écran antérieur n’est remplacé pour ces ajouts. Les repères n’annoncent ni compétence encore inconnue au point d’insertion, ni révélation future, ni retour temporel, ni calendrier astral. Aucun affixe, statistique naturelle ou reliquat historique n’est inventé. La résolution Œil/Bénédiction documentée ci-dessous reste inchangée et n’est pas introduite prématurément dans ces encadrés.

### Nettoyage ciblé après revue — écrans des personnages

Les remarques de fabrication « chronométrage exact non transmis », « valeurs non transmises », « aucun dégât chiffré déduit en l’absence des défenses de la cible » et « sans total naturel ou complexe reconstitué » sont retirées des fenêtres perçues par les personnages. La remarque sur les défenses non déductibles des seuls taux critiques est également retirée de l’écran. Leurs limites restent documentées ici : durée exacte du mannequin inconnue, valeurs d’affixes manquantes, défenses adverses et ordre des calculs insuffisants pour des totaux fiables. Aucune donnée manquante n’est remplacée par un chiffre inventé.

Les cinq libellés de compteur « suivi transmis » ont été nettoyés puis, **après arbitrage direct de l'auteur**, deviennent **« Progression cumulée depuis le huitième palier »**, reliquat antérieur inclus. Les nombres ne changent pas ; les commentaires HTML hors des fenêtres rappellent cet arbitrage, sans donner une valeur isolée au reliquat. Les trois mentions des anciennes runes +6 de Yoon repérées par la revue reçoivent explicitement **grades et rangs en étoiles À DÉFINIR**. Ces corrections sont distinctes des dix encadrés de repères et n'en changent pas le décompte.

Les bonus runiques sont bleus, les effets temporaires de Résonance/Infiltration verts ; les niveaux naturels restent sans classe de bonus. Les réussites ne sont pas étiquetées comme bonus temporaires. Aucun total naturel inconnu, réserve courante de Mana, XP nécessaire, Défense de monstre, coût d’amélioration, affixe ou durée précise de combat absent de la source n’est fabriqué.

La vérification HTML ne constitue pas une validation visuelle : le CSS externe nécessite un moteur qui le charge ; aucun rendu stylé universel sur GitHub n’est promis.

## 5. Réserves et anomalies ouvertes

### RÉSOLU par arbitrage direct — Chant runique

La source affirme **10 % des PV maximums de Yoon toutes les cinq secondes** (11393 ; rappel 22765–22767), puis utilise cette formule pour motiver le cadeau des Énergie et l’amélioration des soins (31221–31253, 31521–31527, 31643–31645). DEC-046 laissait ces paramètres ouverts ; **l’auteur valide désormais explicitement cette assiette et cette cadence**, avec zone posée autonome. Le blocage antérieurement identifié est levé.

**Traitement :** scènes et formulations conservées ; les quatre commentaires HTML de réserve SOINS-01 à SOINS-04 sont retirés. Aucun PV maximum de Yoon, montant de soin absolu, rayon, durée ou coût manquant n’est inventé. La décision chiffrée récente prévaut sans transformer Yoon en soigneuse pure ni effacer les blessures et le besoin de repos racontés.

### RÉSOLU par arbitrage direct — compteurs et reliquat historique

Le chapitre 1 protège un total **supérieur à 8 000**, huit paliers déjà récompensés et un reliquat inconnu. La source mobile du chapitre 9 présentait 999/1 000 puis 1 998/2 000 comme de nouvelles éliminations depuis le niveau 10, sans raccorder ce reliquat. L'auteur choisit explicitement **« Inclure le reliquat »**.

**Traitement :** les cinq affichages suivent la progression cumulée **après les huit paliers déjà récompensés, reliquat antérieur inclus**. La mention « depuis le niveau 10 » est retirée. Les valeurs 999, 1 000, 1 998, 1 999 et 2 000, les scènes et les douze cercles sont conservés ; aucun ancien millier récompensé une seconde fois ni reliquat abandonné. **À DÉFINIR :** seulement sa valeur isolée et le nombre exact d'éliminations réellement nouvelles depuis le niveau 10, qui ne sont pas nécessaires à ces affichages.

### RÉSOLU par arbitrage direct — Arcanique et Lame

La validation relayée du chapitre 7 (21763–21830) fixe **Arcanique, quatre pièces, +1 200 PA**, remplaçant les anciens ensembles de critique. Le canon antérieur nommait **Lame, deux pièces, +12 % de chance critique**. **L’auteur tranche désormais : retirer Lame du système actif, remplacé par Arcanique ; conserver l’historique inchangé.** La synchronisation des références relève de la session principale.

**Traitement :** Arcanique utilisé conformément aux décisions récentes ; aucune Lame introduite et aucune modification des chapitres 1–4. La résolution est explicite, pas une suppression silencieuse de l’historique.

La dernière composition autorisée au chapitre 9, **4 Fatal + 4 Arcanique + 4 Gardien**, remplace l’ancien futur du plan **4 Fatal + 4 Vitesse + 2 Énergie + 2 Gardien**. Ce n’est pas une transformation de runes ni un achat de Vitesse raconté. Les anciennes obligations « douze +6 » ne sont pas réappliquées aux pièces +9 explicitement présentes.

### Autres limites à conserver visibles

- **RÉSOLU par arbitrage direct — Œil runique/Bénédiction :** les types de secondaires révélés sont prédéterminés et restent identiques quel que soit l'artisan ; Œil affiche les valeurs maximales accessibles si Hasol améliore la rune. Un autre artisan peut obtenir les mêmes types avec des valeurs plus faibles. Bénédiction favorise les maxima sans les garantir, et les tentatives peuvent toujours échouer. Aucun Œil anticipé dans les chapitres 5 à 9, ni garantie d'obtenir toutes les valeurs affichées.
- **CANON rappelé par l’auteur — arme à aura :** le niveau minimum 10 du porteur reste applicable même à un Arcaniste astral de niveau 1, sans exception. Le chapitre 5 conserve cette condition ; aucune scène de seconde vie n’est ajoutée.
- **CANON récent, hors des scènes importées — butin :** la tranche de niveau du monstre fixe un plafond d’étoiles, pas un rang garanti. Exemple validé au niveau 30 : runes 1★/2★/3★ selon 50 %/35 %/15 % ordinairement, 20 %/30 %/50 % avec Aimant. Ne pas extrapoler ces proportions aux autres niveaux. Aucune table générale, garantie de butin ni acquisition anticipée d’Aimant n’est introduite ; les étoiles des runes déjà acquises ne sont pas recalculées rétroactivement.
- **TEMPS-01 :** la V2 fait reprendre la chasse le dimanche suivant la morsure, après examen et soins maternels. Le plan demandait de laisser récupérer Hasol sans imposer le lendemain. Cette chronologie transmise est conservée ; aucun délai fictif d’une semaine ajouté. La source montre toujours douleur, bandage et surveillance.
- **À DÉFINIR — progression de Yoon :** niveau 5 à la rencontre, niveau 11 antérieur évoqué au chapitre 9, puis 13, 20, 22 et 24. Les dates et seuils intermédiaires ne sont pas reconstitués depuis l’XP d’Hasol. Yoon garde ses cours et ses propres chasses ; pas de disponibilité générale en semaine avec Hasol.
- **À DÉFINIR — inventaire individuel :** quels identifiants maternels sont retirés/rééquipés, quelles six pièces sont +6 et quelles quatre +3 au chapitre 7, quelles Fatal atteignent +9, grades et affixes précis des Arcanique, caractéristiques intermédiaires après le niveau 10. Le récit ne permet pas un calcul complet d’équipement sans arbitrage ; aucun remplacement d’identité ou affixe silencieux.
- **RÉSOLU — rune de récupération :** l'auteur demande de changer la couleur plutôt que de supprimer les secondaires. La petite rune examinée au chapitre 6, section III, est donc **rare (bleue), 1★** ; choix éditorial autorisé dans DEC-072, sans affixe ni amélioration inventés. Les autres communes blanches du lot, notamment celles des essais, ne changent pas de couleur. Le devenir individuel de cette pièce bleue reste inconnu.
- **Limite de lecture des combats :** cinq secondes d’incantation de Vague sont désormais explicites à plusieurs jalons, mais les autres tirs ne reçoivent pas de chronologie seconde par seconde. Les distractions des ennemis restent des réactions aux impacts, pas un ralentissement ou une interruption garantis du sort.
- **À DÉFINIR — impacts des calculs :** ordre des ensembles, Résonance, plancher d’Infiltration, affinités et critiques ; arrondis et défenses adverses. Les formules de taux ne suffisent pas à reconstituer des dégâts finaux.
- **Vigilance — secret :** les cercles montrés autour d’Hasol près de la fontaine en fin du chapitre 9 peuvent être vus. Aucun témoin, rumeur ou divulgation automatique n’est ajouté pour combler ce point.

## 6. Contrôles de livraison

- **Réussi :** corps intégral des chapitres 1 à 4 identique octet pour octet à l'instantané ; seuls les liens 5 à 9 ont été ajoutés au sommaire initial.
- **Réussi :** neuf titres de chapitre, chacun unique, dans l’ordre 1–9 ; neuf ancres uniques ; aucun chapitre 10.
- **Réussi :** HTML analysé avec pile des balises ouvrantes/fermantes ; aucune fermeture inattendue ni balise non fermée, balises vides HTML prises en compte.
- **Réussi :** 61 en-têtes de fenêtres dans les chapitres ajoutés, soit 51 initiaux + 10 repères ; cinq ouvertures et cinq clôtures, quatre ou cinq puces chacune ; classes CSS existantes uniquement.
- **Réussi après revue :** expressions éditoriales signalées absentes des paragraphes des fenêtres ; cinq compteurs renommés sans changer leurs valeurs ; les dix encadrés sont placés après les titres ou avant les fins de chapitre, sans révélation anticipée.
- **Réussi :** la ligne d’arbitrage Œil/Bénédiction ajoutée par la session principale est conservée exactement.
- **Réussi :** aucun en-tête de courriel, adresse ou introduction conversationnelle importé dans l’ajout.
- **Réussi :** `new.txt` et `old.txt` identiques aux copies de provenance ; aucun de ces fichiers nettoyé.
- **Limite :** contrôles structurels et de continuité ciblés, pas validation littéraire nouvelle, audit exhaustif des statistiques impossibles à récupérer, ni arbitrage des réserves.

Preuves de travail locales : scripts et patchs générés, journal des retouches, inventaire des fenêtres et résultat des contrôles dans `/tmp/opencode/arcaniste-integration-20261121/`. Ces fichiers temporaires ne constituent pas un deuxième manuscrit suivi dans le dépôt. Aucun accès à des secrets, changement de dépendance, service, déploiement ou publication ; impacts sécurité/performance limités à l’allongement d’un document Markdown/HTML statique.
