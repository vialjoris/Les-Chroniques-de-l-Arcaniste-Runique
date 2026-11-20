# Les Chroniques de l’Arcaniste Runique — Guide des agents

## 1. Rôle et langue

Accompagner l’auteur dans le développement éditorial, la continuité narrative et l’écriture de ce roman de fantasy LitRPG. Écrire exclusivement en français, y compris les analyses, questions et comptes rendus.

Les fichiers du projet sont la source de vérité. Ne pas inventer une information manquante pour masquer une incohérence. Signaler les limites des sources et demander un arbitrage lorsqu’elles affectent le travail demandé.

## 2. Priorité des sources éditoriales

1. Décisions explicites les plus récentes de l’auteur.
2. Règles et décisions officiellement validées.
3. Chapitres validés, pour les faits déjà racontés.
4. `PLAN_DIRECTEUR.md`, pour les événements futurs.
5. Propositions de développement.

Si deux sources officielles restent incompatibles, signaler la contradiction et demander clarification. Une demande de correction ne valide pas automatiquement toutes les propositions chiffrées du plan.

Employer explicitement les statuts suivants :

- **CANON** : information validée.
- **PROPOSITION** : idée non approuvée.
- **À DÉFINIR** : information manquante ou attendant validation.
- **CONTRADICTION** : incompatibilité à résoudre.

Dans le plan, `[VALIDÉ]` correspond au canon, `[À CONFIRMER]` à une information à définir et `[PROPOSITION]` à une proposition. Conserver ces nuances, y compris dans les sections qui mêlent plusieurs statuts.

Les inspirations externes répertoriées dans `source.md` ne sont pas des règles officielles du roman. Toute adoption doit résulter d’une décision explicite ou d’une délégation de l’auteur, limitée à son périmètre.

**Archive `old.txt` :** anciens chapitres 1 à 6 copiés par l’auteur, sans les dernières décisions et sans les fenêtres qui étaient des images. Des en-têtes précisent qu’il s’agit de reconstitutions, pas de copies mot pour mot. Utiliser ce fichier comme matériau narratif à auditer, jamais comme remplacement automatique du manuscrit ou des décisions actuelles. Le conserver intact. Reconstituer les fenêtres manquantes en HTML uniquement à partir de faits établis ; signaler toute statistique irrécupérable. Aucun chapitre 7 n’est présent dans cette copie. Voir la notice de provenance dans `source.md`.

### Transmission depuis les sessions mobiles — `new.txt`

L’auteur poursuit aussi le travail dans ChatGPT en mode conversation depuis son téléphone. Il déposera les nouveaux textes et décisions dans `new.txt` pour leur intégration au projet. Ce fichier est un support de transmission, pas un second manuscrit ni un remplacement automatique du canon.

Lorsqu’un nouvel apport est signalé :

1. Vérifier que `new.txt` existe et le lire intégralement ; ne pas supposer son contenu à partir d’une annonce.
2. Distinguer chapitres, extraits, variantes, commentaires de conversation et décisions de l’auteur. Ne pas traiter une réponse de ChatGPT ou une proposition non approuvée comme une décision explicite de l’auteur.
3. Comparer au manuscrit actuel pour repérer les passages déjà intégrés, les versions concurrentes et l’ordre des chapitres. Ne pas ajouter deux fois un texte ou un chapitre portant le même numéro.
4. Vérifier les règles récentes et les références : niveaux, XP, runes, ensembles, compétences, chronologie et relations. Demander un arbitrage sur toute contradiction matérielle non résolue par une décision explicite.
5. Intégrer les chapitres concernés dans l’unique `roman.md`, avec les titres cohérents et les fenêtres HTML/CSS. N’intégrer ni les instructions de conversation ni les commentaires éditoriaux au milieu du roman.
6. Ne pas remplacer un chapitre validé sans autorisation explicite de révision. Si un chapitre existe déjà en version de lecture, identifier la version retenue avant remplacement. Ne pas confondre la demande d’intégration avec une validation littéraire globale.
7. Mettre à jour les références nécessaires et rapporter quels chapitres, décisions et fenêtres ont été intégrés, ainsi que les points encore ouverts.
8. Conserver `new.txt` intact par défaut, comme trace de provenance. Ne pas le vider, le supprimer ou le renommer sans demande ; l’absence de nettoyage ne doit pas provoquer de doublon au prochain import.

Le dépôt GitHub est déclaré **public** par l’auteur. Ne pas assimiler une demande d’intégration locale à une autorisation de commit ou de push. Avant une publication demandée, rappeler au besoin que les fichiers suivis, notamment le plan, `lore/`, `old.txt` et `new.txt`, peuvent révéler l’intrigue et les échanges de travail. Ne pas en déduire une autorisation de publier des données privées ou secrets éventuellement présents dans un apport.

**Choix confirmé par l’auteur :** l’accessibilité publique du roman, des révélations et des documents de travail ne le gêne pas. Respecter ce choix sans répéter systématiquement les avertissements sur les spoilers ni lui redemander de passer en privé. Cette acceptation ne remplace pas une autorisation de commit/push et ne couvre pas les secrets ou données privées de tiers qui pourraient apparaître dans un nouvel apport.

## 3. Lecture préalable et organisation du projet

Avant toute intervention, lire ce guide et les sources pertinentes. Avant un chapitre, consulter :

- `PLAN_DIRECTEUR.md` intégralement, ou `PLAN_DIRECTEUR_ARCANISTE_RUNIQUE.md` si ce nom le remplace ;
- `roman.md`, notamment les chapitres précédents et les passages concernés ;
- `lore/systeme.md` ;
- `lore/personnages.md` ;
- `lore/runes.md` ;
- `lore/chronologie.md` ;
- `lore/decisions.md` ;
- `source.md` et `style.css` lorsque le système ou les interfaces sont concernés.

Vérifier l’existence et le contenu réel de ces fichiers : un fichier absent ou vide ne fournit aucune règle. `lore/personnage.md`, initialement vide, a été renommé en `lore/personnages.md` lors de DEC-010. `lore/runes.md` est l’inventaire renseigné ; le fichier historique `lore/rune.md` au singulier est vide. Ne pas créer deux inventaires concurrents et ne pas considérer une référence partielle comme exhaustive.

## 4. Écriture littéraire

- Produire des chapitres longs, immersifs et riches en détails, sans remplissage artificiel.
- Développer les émotions, dialogues, descriptions sensorielles et relations entre personnages.
- Privilégier une narration naturelle plutôt qu’une succession de statistiques.
- Respecter le caractère, les motivations, les connaissances et l’évolution psychologique de chacun.
- Employer la troisième personne, principalement centrée sur Hasol, conformément au plan.
- Ne pas accélérer artificiellement les relations, réconciliations, apprentissages ou événements importants.
- Montrer la progression par les efforts, les choix, les limites, les coûts et les conséquences.
- Préserver les scènes et chapitres validés. Ne jamais les supprimer ou les réécrire sans autorisation.
- Une correction technique ciblée ne donne pas permission de modifier la trame ou les relations.
- Ne pas introduire prématurément de compétence, révélation ou événement futur.
- Distinguer ce que sait l’auteur de ce que sait chaque personnage. Les spoilers de la bible ne doivent pas apparaître involontairement dans leurs pensées ou dialogues.
- Ne pas rédiger le chapitre suivant sans autorisation.

## 5. Manuscrit et présentation

- Conserver le roman complet dans l’unique fichier `roman.md`.
- Séparer clairement les chapitres par des titres Markdown numérotés et des séparateurs `---`.
- Ne pas placer de brouillons alternatifs ou de fiches de préparation au milieu du texte validé.
- Conserver `style.css` séparé du manuscrit.
- Utiliser des blocs HTML pour les fenêtres du système et réutiliser les classes existantes : `.system-window`, `.character-sheet`, `.rune-window`, `.rune-bonus`, `.temporary-bonus`, `.upgrade-badge`.
- Préserver également les classes utiles existantes, dont `.system-header`, `.legendary-text`, `.success-text` et `.passive-badge`.
- Afficher les caractéristiques naturelles dans la couleur normale du texte.
- Afficher les bonus runiques en bleu avec `rune-bonus` et les bonus temporaires en vert avec `temporary-bonus`.
- Afficher les niveaux d’amélioration dans des bulles HTML, par exemple `<span class="upgrade-badge">+3</span>`. La notation narrative peut être `【 +3 】` ou `【 +6 】`.
- Ne pas confondre une notification verte de réussite avec un effet temporaire : les libellés et classes doivent rester explicites.
- Ne pas supposer que tous les moteurs Markdown chargent le CSS externe. Vérifier l’environnement de rendu avant de promettre un résultat visuel.
- À chaque mention d’une rune identifiable, indiquer sa rareté (grade ou couleur explicite) et son rang en étoiles, y compris dans les fenêtres, fiches, dialogues et descriptions une fois l’identification acquise. Exemple : « rune Fatal rare (bleue), 6★, +6 ». Le nom d’ensemble ne remplace pas la rareté. Les explications sur les runes en général et les compteurs d’emplacements ne décrivent pas une rune particulière. Si une rareté ou un rang manque dans une référence, noter « À DÉFINIR » plutôt que l’inventer.

## 6. Contrôles LitRPG obligatoires

Avant et après chaque chapitre, contrôler :

- niveaux, XP connue et progression de chaque personnage ;
- caractéristiques naturelles, séparées des bonus d’équipement ;
- principales et secondaires de chaque rune équipée ;
- ensembles et conditions d’activation ;
- cercles de mana et emplacements disponibles ou occupés ;
- compétences débloquées et conditions de déblocage ;
- effets temporaires, portée, durée et coût lorsqu’ils sont définis ;
- composition des équipes et limites ;
- blessures, soins, consommables et ressources ;
- chronologie, âges et contraintes d’emploi du temps ;
- secrets connus par chaque personnage.

Ne jamais inventer une formule d’XP, une table de progression, un ordre de calcul ou une règle d’arrondi absent des sources. Afficher les bonus séparément si les totaux ne peuvent pas être calculés selon une règle validée.

Les classes valent respectivement 5 points pour Commune, 10 pour Rare, 20 pour Légendaire et 25 pour Astrale. Une équipe comporte au maximum cinq membres et cinquante points de classe. La rareté ne garantit pas la victoire.

**Équivalence d’inspiration des personnages — DEC-009 :** Commune ≈ monstre 2★ natif de Summoners War ; Rare ≈ 3★ natif ; Légendaire ≈ 4★ natif ; Astrale ≈ 5★ natif. Hasol relève donc de la référence 4★ native. Cette échelle est distincte des étoiles des runes. Elle ne fixe pas une fiche universelle par classe et n’autorise pas à remplacer les statistiques naturelles déjà validées sans arbitrage. Comparer des données au même niveau, rang et état d’éveil ; ne pas confondre les statistiques au niveau 1 avec les maxima affichés en tête des fiches externes. Mana et Puissance arcanique nécessitent une adaptation propre au roman.

Les gains naturels sont automatiques et non distribués manuellement. Ne pas transformer la rumeur d’une influence des activités sur les gains en loi confirmée.

**Base actuelle de Hasol — DEC-010 :** au niveau 1, PV 2940, Attaque 199, Défense 182 et Vitesse 100, d’après le Danseur du ciel Vent non éveillé, 4★, niveau 1. La correction demandée par l’auteur conserve les gains naturels déjà racontés et recalcule les fiches 9 et 10 ; elle n’importe pas la courbe de progression du jeu. Mana et Puissance arcanique restent inchangés en attendant une éventuelle décision d’échelle magique. Consulter `lore/personnages.md` pour les fiches actualisées.

**Repères magiques — DEC-015 :** norme de Mana au niveau 60 : 1000 ; norme de Puissance arcanique au niveau 60 : 600 pour un soutien, 2000 pour un mage. Ce sont des repères, pas des plafonds ni une progression linéaire. Hasol a une classe de soutien mais une Puissance arcanique de profil mage, et un Mana hors norme destiné à dépasser largement 1000. Ne pas confondre son rôle avec son profil statistique, ni importer une statistique de soutien pour limiter sa magie. Le niveau de franchissement et les valeurs futures exactes restent à définir. Cette puissance ne débloque aucun sort offensif à elle seule.

## 7. Identité, grades et amélioration des runes

Chaque rune possède une principale. Le nombre de secondaires présentes dès +0 dépend du grade :

| Grade | Couleur | Secondaires à +0 |
|---|---|---:|
| Commun | Blanc | 0 |
| Peu commun | Vert | 1 |
| Rare | Bleu | 2 |
| Épique | Violet | 3 |
| Légendaire | Orange | 4 |

Quatre secondaires constituent le maximum. **La principale augmente à chaque amélioration réussie de +1 à +15, avec un gain renforcé à +15** (DEC-014). En plus, une secondaire est ajoutée ou renforcée aux paliers **+3, +6, +9, +12 et +15**. Jusqu’à +12, appliquer les règles adoptées dans DEC-006 : à +3, ajouter si aucune secondaire n’est présente, sinon renforcer ; à +6, ajouter si une seule est présente, sinon renforcer ; à +9, ajouter si seulement deux sont présentes, sinon renforcer ; à +12, ajouter si seulement trois sont présentes, sinon renforcer. Une rune bleue native conserve deux secondaires à +6, trois à +9 et quatre à +12. À +15, les runes ayant suivi cette progression possèdent déjà quatre secondaires : en renforcer une, sans en créer une cinquième. Les ajouts font évoluer le grade affiché, pas les étoiles. L’effet sur une secondaire à +15 est une adaptation propre au roman, prioritaire sur la source.

**Unités des secondaires :** le taux critique, les dégâts critiques, la précision et la résistance peuvent s’exprimer en pourcentages. La décision de l’auteur rétablissant ces pourcentages remplace l’interdiction générale précédente ; voir DEC-004 dans `lore/decisions.md`. Les secondaires fixes déjà validées restent inchangées. L’usage de PV %, Attaque % et Défense % reste à confirmer : ne pas déduire leur adoption de cette liste.

**Rang en étoiles :** chaque rune possède un rang de 1 à 6 étoiles, distinct du grade de couleur et du niveau d’amélioration +0 à +15. Consigner ce rang dans l’inventaire. Un rang supérieur permet de meilleures valeurs de principale selon les tables validées ; il ne fixe pas le nombre de secondaires, qui dépend du grade à +0. Les deux cadeaux du père sont 6★ et déjà +6. Les tables de progression citées par l’auteur concernent les principales, pas les secondaires ; voir `lore/systeme.md`.

**Obtention — règle propre au roman :** monstres niveaux 1–10 → runes 1★ ; 11–20 → 2★ ; 21–30 → 3★ ; 31–40 → 4★ ; 41–50 → 5★ ; 51–60 → 6★. Le rang dépend du niveau du monstre, pas de celui du porteur. Le cas des monstres au-delà de 60 reste à définir : ne pas créer de septième étoile ni supposer un plafonnement automatique. Cette règle ne fixe ni la rareté ni une probabilité de butin et ne signifie pas que chaque monstre donne une rune.

**Équipement sans niveau minimum :** toutes les runes sont équipables à tout niveau de personnage, indépendamment de leur rareté, de leurs étoiles et de leur amélioration. Ne jamais transformer une tranche de niveau d’obtention en condition d’équipement. Un emplacement runique disponible reste nécessaire. Hasol peut donc équiper ses deux cadeaux rares (bleus), 6★, +6 dès le niveau 1 (DEC-008).

- Donner un identifiant unique et stable à chaque rune, par exemple `HAS-R001`.
- Conserver propriétaire, ensemble, grade, couleur, principale, secondaires, amélioration, état, provenance et historique.
- Une amélioration ne crée pas une nouvelle identité et ne remplace pas arbitrairement les affixes.
- Distinguer les runes personnelles des runes confiées par un client ou un mentor.
- Les tentatives consomment des ressources et peuvent échouer ; ne pas inventer les autres conséquences d’un échec.
- **Coût et fatigue — DEC-024, enseignés au chapitre 4 :** chaque tentative consomme des pierres de mana et du Mana personnel, réussite ou échec. Le coût dépend de la difficulté (étoiles, grade, palier), sans barème numérique validé. Distinguer capacité naturelle, bonus runiques et réserve disponible. Le repos et les potions restaurent le Mana sans supprimer toute fatigue mentale ; la grande réserve de Hasol donne de l’endurance, pas une maîtrise automatique.
- Bénédiction runique augmente les chances de réussite sans garantir le succès.
- Les rangs de 1 à 6 étoiles sont adoptés ; ne pas importer automatiquement les six emplacements fixes, tarifs ou règles de destruction de Summoners War.

**État actuel — DEC-006 :** les deux cadeaux du père sont une Fatal et une Gardien **bleues, 6★, déjà +6**, avec chacune deux secondaires natives renforcées, sans ajout à +3 ou +6. Fatal : principale Attaque +70, secondaires Vitesse +4 et PV +25. Gardien : principale Défense +70, secondaires PV +30 et Mana +20. Les principales suivent le tableau de la source (`22 + 6 × 8 = 70`) ; les gains des secondaires sont des choix éditoriaux dans le cadre de la délégation de l’auteur, pas un barème fourni par le guide. Les runes restent équipées sans nouvelle amélioration pendant les trois années d’Académie. Voir `lore/runes.md` pour l’historique.

Ensembles validés : Fatal, quatre pièces, +35 % Attaque ; Vitesse, quatre pièces, +30 % Vitesse ; Énergie, deux pièces, +15 % PV ; Gardien, deux pièces, +15 % Défense ; Lame, deux pièces, +12 % chance critique. Ne pas remplacer ces valeurs par celles d’une source externe.

**Principales fixes et pourcentages — DEC-011 complétée par DEC-024 :** Orven explique ce principe au chapitre 4, section IV, puis le met en pratique avec une cliente en VII. Les principales fixes favorisent le bas niveau ; les pourcentages prennent l’avantage avec la croissance naturelle selon les valeurs comparées. Les principales PV %, Attaque % et Défense % sont admises, sans validation automatique de ces unités en secondaires. **Le pourcentage de principale est calculé sur la caractéristique naturelle, avant ajout des bonus fixes runiques.** Cela ne fixe pas l’ordre de calcul des ensembles, Résonance runique ou les arrondis. Comparer à rang en étoiles et amélioration comparables ; aucun niveau universel de bascule. Ne plus traiter cet enseignement comme une première découverte future.

## 8. Garde-fous de continuité

- Le chapitre 1 restauré est à préserver ; toute correction doit rester dans le périmètre autorisé.
- **Chapitre 1 validé le 19 novembre 2026 — DEC-018 :** la version actuelle de `roman.md`, après reprise DEC-016 et correction DEC-017 (niveau 8 en section VII, passage au niveau 9 en VIII), est la référence narrative. Ne pas la modifier rétroactivement sans nouvelle autorisation, y compris pour adapter les chapitres d’`old.txt`. La validation ne porte pas sur les propositions ouvertes des chapitres suivants et n’autorise pas leur rédaction.
- **Révision ciblée DEC-021 validée le 20 novembre 2026 — DEC-022 :** les sections I et VII ont été actualisées depuis `new.txt` puis approuvées : ouverture familiale la veille de la Révélation avec souvenir à sept ans ; scène développée de Ray et Zio pendant l’Académie, Hasol niveau 8. « Modif chap 2 » était un intitulé erroné confirmé par l’auteur, pas un déplacement au chapitre 2. Les autres sections restent préservées. Ray est un ami d’enfance devenu complice des humiliations ; il part sans excuses, et Zio intervient une seule fois. Ne pas attribuer à Ray ou Zio, dans ce souvenir, les niveaux prévus lors des retrouvailles futures. La validation ne s’étend pas au chapitre 2 ou aux propositions futures.
- **Chapitres 3 et 4 intégrés — DEC-023 :** textes complets de `new.txt` ajoutés sur demande du 20 novembre 2026, sans réécriture globale ni modification des deux premiers chapitres. Le chapitre 3 est une intégration autorisée sans validation littéraire implicite ; le chapitre 4 est désigné comme validé dans la transmission mobile. Hasol reste niveau 10, dix cercles et dix runes personnelles inchangées. Le chapitre 4 « La voie de l’artisan » décale les anciennes trames 4 à 7 vers 5 à 8 ; le chapitre 5 n’est pas rédigé par cet import. Les nouvelles consignes mobiles qui affectent ses niveaux et compétences restent à arbitrer avant rédaction, sans valider une réponse de ChatGPT par défaut.
- **Chapitre 3 refondu — DEC-026 :** nouvelle version de lecture sur demande explicite de l’auteur, événements et sept sections conservés, autres chapitres inchangés. Moins de reformulations, Hasol compétente en théorie mais fragilisée par le jugement ; sa mère respectait son rêve et attendait qu’elle soit prête à envisager l’artisanat, Orven la responsabilise par le travail. Le premier salaire reste le point culminant. Protocole du mannequin identique au chapitre 2 (DEC-025), troisième touche et arrêt à 78 secondes explicités. Ne pas réimporter silencieusement le chapitre 3 initial de `new.txt` ni anticiper les découvertes du chapitre 4.
- **Chapitre 4 adapté — DEC-027 :** nouvelle version de lecture autorisée après DEC-026, dix sections et événements conservés, autres chapitres préservés. Hasol connaît théoriquement le coût personnel en Mana ; elle apprend à suivre sa réserve dans une journée réelle. Fixe/pourcentage : une explication puis mise en pratique, pas de répétition du cours à la mère et dans le carnet. Le coffret paternel reste unique, la blessure une griffure ; ne pas effacer la reconnaissance antérieure de Zio. Fin orientée vers la fierté et l’initiative sous supervision, sans réconciliation avec le père. Le statut validé de la version mobile initiale ne vaut pas validation de la nouvelle rédaction ; ne pas réimporter l’ancienne version depuis `new.txt`.
- Le père de Hasol est vivant au chapitre 1. Préserver l’amour sous les maladresses et la blessure relationnelle non résolue.
- Hasol n’a aucun sort offensif au début. Dix emplacements ne la rendent pas immédiatement invincible.
- Croissance runique se débloque au niveau 10. Huit paliers rétroactifs font passer de deux à dix cercles et emplacements, avec deux runes équipées.
- Ne pas compter deux fois les éliminations déjà récompensées. Si le reliquat historique est inconnu, ne pas le fixer arbitrairement à zéro.
- Écrire **Orven**, pas Orwen. Après insertion du chapitre d’artisanat (DEC-023), il ne découvre l’avantage chiffré de Hasol qu’au chapitre 7 : environ 30 % d’échecs en moins relativement à son propre taux, pas trente points de pourcentage. Au chapitre 4, il découvre seulement son endurance liée au Mana, distincte de ce taux.
- Résonance runique de Yoon amplifie seulement les principales des runes équipées sur sa cible, pas les secondaires ni les ensembles.
- Yoon a une progression et une personnalité propres ; elle ne se réduit pas à un bonus pour Hasol.
- Œil runique ne se débloque qu’au niveau 20, après le sauvetage prévu. Personne ne doit prédire ce pouvoir avant sa découverte.
- Les futurs validés des livres I et II doivent rester séparés des événements déjà racontés dans les références.

### Don maternel et équipement du chapitre 2 — DEC-013

Hasol conserve HAS-R001, Fatal rare (bleue), 6★, +6 et HAS-R002, Gardien rare (bleue), 6★, +6. Sa mère ajoute huit runes 3★ de grades peu commun (vert) et rare (bleu), pour dix runes équipées au total. Ne pas remplacer les cadeaux paternels et ne pas ajouter dix runes maternelles. Les types retenus sont Fatal, Gardien et Énergie ; Fatal et Gardien doivent être complets. Ne pas réintroduire les deux Lame ou les runes maternelles blanches d’`old.txt`.

**Répartition désormais validée — DEC-020 : quatre Fatal, quatre Gardien, deux Énergie au total**, soit trois Fatal, trois Gardien et deux Énergie parmi les huit cadeaux maternels 3★ verts ou bleus. Fatal fonctionne par quatre, Gardien et Énergie par deux. Deux paires Gardien donnent deux bonus de +15 % Défense, soit +30 % ; pas de cinquième pièce nécessaire. Les caractéristiques individuelles de la version de lecture du chapitre 2 sont des choix délégués de l’assistant, à distinguer de cette répartition explicitement validée. La Fatal rare (bleue) à améliorer jusqu’à +3 est HAS-R003, une nouvelle rune 3★ ; celle du père reste 6★, +6. L’ancienne proposition cinq Fatal, trois Gardien et deux Énergie est abandonnée.

## 9. Contenu des références

- `lore/personnages.md` : identité, âge, apparence, personnalité, motivations, classe, rareté, niveau, XP connue, caractéristiques naturelles, compétences, cercles, emplacements, relations, évolution psychologique, blessures, dernier chapitre d’apparition et historique. Séparer les futurs validés de l’état présent.
- `lore/runes.md` : identifiant, propriétaire, nom, ensemble, grade, couleur, rang de 1 à 6 étoiles, amélioration, principale, secondaires, état équipée/stockée/vendue/détruite, obtention, historique et ensembles actifs. Marquer les valeurs non validées.
- `lore/systeme.md` : classes, XP, caractéristiques, Mana et Puissance arcanique, cercles, équipement, grades, améliorations, ensembles, compétences, équipes et conditions d’évolution. Distinguer règles établies et questions ouvertes.
- `lore/chronologie.md` : événements racontés, futurs validés et propositions dans des sections distinctes ; âges, niveaux et changements connus.
- `lore/decisions.md` : sujet, statut, justification sourcée, fichiers concernés et questions en attente. Ne pas inventer la justification ou la date d’une ancienne décision.
- `source.md` : provenance des inspirations, liens et limites de transposition ; ce n’est pas une copie du canon.

## 10. Workflow éditorial

### Avant rédaction

1. Lire les sources et vérifier leur état réel.
2. Préparer une fiche de continuité : période, point de départ, personnages, scènes obligatoires, émotions, enjeux, combats, niveaux, équipement, secrets à préserver et situation finale.
3. Signaler les contradictions et les décisions manquantes.
4. Attendre les validations nécessaires et l’autorisation de rédiger.

### Après rédaction et validation d’un chapitre

1. Vérifier la cohérence avec les chapitres précédents.
2. Contrôler niveaux, caractéristiques, runes, compétences, ressources et chronologie.
3. Mettre à jour `lore/personnages.md`.
4. Mettre à jour `lore/runes.md`.
5. Mettre à jour `lore/chronologie.md`.
6. Actualiser `lore/systeme.md` et `lore/decisions.md` si nécessaire.
7. Fournir un résumé des changements effectués.
8. Signaler les incohérences et questions non résolues.

Ne pas présenter un état futur planifié comme déjà survenu. Conserver un historique par chapitre et ne jamais modifier rétroactivement un chapitre validé sans autorisation.
