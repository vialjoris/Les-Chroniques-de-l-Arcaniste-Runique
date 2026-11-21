# Les Chroniques de l’Arcaniste Runique — Guide des agents

## 1. Rôle et langue

Accompagner l’auteur dans le développement éditorial, la continuité narrative et l’écriture de ce roman de fantasy LitRPG. Écrire exclusivement en français, y compris les analyses, questions et comptes rendus.

Les fichiers du projet sont la source de vérité. Ne pas inventer une information manquante pour masquer une incohérence. Signaler les limites des sources et demander un arbitrage lorsqu’elles affectent le travail demandé.

**Format cible actualisé — DEC-079/080 :** trilogie ; seize chapitres pour chacun des livres I et II, découpage du livre III à définir. Le livre I raconte la première vie et se termine sur l'activation de la Rune temporelle ; le réveil ouvre le livre II, une semaine avant la Révélation. Le livre II couvre onze réincarnations (vies 2 à 12) ; le livre III, la treizième et dernière vie. Ces boucles résultent des décisions explicites de l'auteur, pas d'une déduction du format trilogie. La catastrophe mondiale de ses 45 ans au livre III ne remplace pas le dénouement du livre I vers 34 ans.

**Arbitrages du 21 novembre 2026 — DEC-072 à DEC-080 :** ils priment les états historiques ci-dessous. Consulter leurs limites dans `lore/decisions.md`, notamment les paramètres encore ouverts ; ne pas traiter toute réponse de ChatGPT dans `new.txt` comme une décision de l'auteur.

**Plan du livre I validé — DEC-045 :** seize chapitres, titres, ordre et jalons détaillés dans `PLAN_DIRECTEUR.md`. Les anciens découpages concurrents après le chapitre 8 sont remplacés : douze cercles au 9, sauvetage/Œil/Ray au 10, Zio et décès du père au 11, Samia et renommée vers vingt-cinq ans au 12, mariage/transmission au 13, centième boss au 14, sort offensif au 15, catastrophe et autodestruction de Zio au 16. Hasol 10 → 11 et Aura runique sont placés au chapitre 5, sans deuxième passage identique au 6. Les paramètres et dates laissés ouverts ne sont pas validés implicitement. La validation du plan ne valide pas les textes en lecture ni les plans des livres II/III, et ne constitue pas une autorisation nouvelle de rédaction.

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

- **Tenues — DEC-089 :** varier les vêtements selon les activités. Hasol, Yoon et Samia changent régulièrement de tenue et s’habillent différemment pour combattre. Zio : armure complète au combat, tenues civiles variées au repos. Ray : robe de mage gris foncé au combat, habits ordinaires variés au quotidien. Aucun costume permanent, bonus d’équipement ou changement de runes implicite ; préserver les descriptions déjà racontées.
- **Direction éditoriale approuvée — DEC-083 :** consulter `lore/conversation_direction_oeuvre_2026-11-21.md` avant la rédaction de la suite. La dimension humaine prime sur l’escalade : valeur propre de l’artisanat, années réellement vécues, bonheur dans les vies interrompues, autonomie des proches et amour librement reconstruit avec Zio. Différencier les boucles par l’évolution intérieure d’Hasol, sans supprimer les répétitions validées ni répéter tous les démarrages. Ne pas affaiblir artificiellement ses pouvoirs pour créer des obstacles ; travailler aussi temps, confiance, coopération et conséquences. Samia doit compter au-delà des fonctions transmises. Le prologue heureux du III déplace l’intérêt vers la construction du bonheur, sans annuler les enjeux. Cette orientation n’autorise aucune révision rétroactive ni rédaction nouvelle.
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
- **Révisions séparées — DEC-072 :** les chapitres 1 à 4 actuels de `roman.md` restent intacts. Leur audit précède toute retouche ; les propositions de lecture peuvent être conservées dans `chap1_revision.md` à `chap4_revision.md`, clairement marquées **PROPOSITION**, sans devenir un second manuscrit canonique. Ne remplacer que le chapitre explicitement approuvé après lecture. Les chapitres 5 à 9 sont validés ; ajouts ciblés de fenêtres et raccords minimaux autorisés, pas de réécriture générale. Pour le chapitre 5, retenir la version 2 ; pour le 9, la dernière version corrigée. Conserver les brouillons jusqu'à instruction de l'auteur.
- **Repères du lore — DEC-072 :** encadrés courts à l'ouverture et à la clôture des chapitres, demandés par l'auteur. Ce sont des aides pour le lecteur, pas de nouvelles notifications perçues par les personnages. Ne rappeler que les règles connues à ce stade : aucune révélation de compétence, de butin ou de vie future. Les ajouts des chapitres 1 à 4 restent dans leurs propositions séparées jusqu'à validation.
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

**Repères magiques — DEC-015 :** norme de Mana au niveau 60 : 1000 ; norme de Puissance arcanique au niveau 60 : 600 pour un soutien, 2000 pour un mage. Ce sont des repères, pas des plafonds ni une progression linéaire. Hasol a une classe de soutien mais une Puissance arcanique de profil mage, et un Mana hors norme destiné à dépasser largement 1000. Ne pas confondre son rôle avec son profil statistique, ni importer une statistique de soutien pour limiter sa magie. Le niveau de franchissement et les valeurs intermédiaires restent à définir. Cette puissance ne débloque aucun sort offensif à elle seule.

**Hasol au niveau 60 — DEC-054 :** caractéristiques naturelles hors runes, ensembles et effets temporaires : PV 12 180, Attaque 350, Défense 250, Vitesse 130, Mana 3 500, Puissance arcanique 2 150. La Vitesse 130 remplace la proposition initiale 110 ; préserver les 115 naturels du niveau 10. Cette référence future ne fixe ni courbe de progression, ni statistiques intermédiaires, ni date d'atteinte du niveau 60 ; fin du livre I toujours vers le niveau 45.

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

**Obtention — DEC-007 actualisée par DEC-077 :** le niveau du monstre fixe un **plafond** d'étoiles : niveaux 1–10 → 1★ maximum ; 11–20 → 2★ ; 21–30 → 3★ ; 31–40 → 4★ ; 41–50 → 5★ ; 51–60 → 6★. Les rangs inférieurs restent possibles ; le niveau du porteur ne fixe pas le butin. Exemple validé pour le monstre niveau 30 seulement : 1★/2★/3★ à 50/35/15 % ordinairement et 20/30/50 % avec Aimant. Ne pas extrapoler ces proportions aux autres niveaux. Les distributions de grades sont consignées dans `lore/systeme.md` ; la fréquence d'obtention d'une rune reste inconnue. Le cas des monstres au-delà de 60 reste à définir, sans septième étoile ni plafond automatique.

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

Ensembles actifs validés : Fatal, quatre pièces, +35 % Attaque ; Vitesse, quatre pièces, +30 % Vitesse ; Énergie, deux pièces, +15 % PV ; Gardien, deux pièces, +15 % Défense ; Arcanique, quatre pièces, +1 200 Puissance arcanique. **DEC-076 retire Lame du système actif**, sans supprimer son historique ni réécrire les événements anciens. Ne pas remplacer ces valeurs par celles d'une source externe.

**Principales fixes et pourcentages — DEC-011 complétée par DEC-024 :** Orven explique ce principe au chapitre 4, section IV, puis le met en pratique avec une cliente en VII. Les principales fixes favorisent le bas niveau ; les pourcentages prennent l’avantage avec la croissance naturelle selon les valeurs comparées. Les principales PV %, Attaque % et Défense % sont admises, sans validation automatique de ces unités en secondaires. **Le pourcentage de principale est calculé sur la caractéristique naturelle, avant ajout des bonus fixes runiques.** Cela ne fixe pas l’ordre de calcul des ensembles, Résonance runique ou les arrondis. Comparer à rang en étoiles et amélioration comparables ; aucun niveau universel de bascule. Ne plus traiter cet enseignement comme une première découverte future.

## 8. Garde-fous de continuité

- **Parents — DEC-086 :** Armin Shun et Iseria Astrea, nom d’épouse Shun. Iseria est une soigneuse pure de Terre ; statistiques de référence au niveau 60 et répertoire délégués dans `lore/personnages.md`, pas niveau présent ou disponibilité automatique de tous les sorts. Pas de statistiques à développer pour Armin. Astrea est une famille perdue dont un héros astral **serait** le fondateur : conditionnel obligatoire, pas d’hérédité astrale ni de dernière survivante déduites. Connaissances des personnages et révélation au lecteur restent à définir.
- Le chapitre 1 restauré est à préserver ; toute correction doit rester dans le périmètre autorisé.
- **Chapitre 1 validé le 19 novembre 2026 — DEC-018 :** la version actuelle de `roman.md`, après reprise DEC-016 et correction DEC-017 (niveau 8 en section VII, passage au niveau 9 en VIII), est la référence narrative. Ne pas la modifier rétroactivement sans nouvelle autorisation, y compris pour adapter les chapitres d’`old.txt`. La validation ne porte pas sur les propositions ouvertes des chapitres suivants et n’autorise pas leur rédaction.
- **Révision ciblée DEC-021 validée le 20 novembre 2026 — DEC-022 :** les sections I et VII ont été actualisées depuis `new.txt` puis approuvées : ouverture familiale la veille de la Révélation avec souvenir à sept ans ; scène développée de Ray et Zio pendant l’Académie, Hasol niveau 8. « Modif chap 2 » était un intitulé erroné confirmé par l’auteur, pas un déplacement au chapitre 2. Les autres sections restent préservées. Ray est un ami d’enfance devenu complice des humiliations ; il part sans excuses, et Zio intervient une seule fois. Ne pas attribuer à Ray ou Zio, dans ce souvenir, les niveaux prévus lors des retrouvailles futures. La validation ne s’étend pas au chapitre 2 ou aux propositions futures.
- **Chapitres 3 et 4 intégrés — DEC-023 :** textes complets de `new.txt` ajoutés sur demande du 20 novembre 2026, sans réécriture globale ni modification des deux premiers chapitres. Le chapitre 3 est une intégration autorisée sans validation littéraire implicite ; le chapitre 4 est désigné comme validé dans la transmission mobile. Hasol reste niveau 10, dix cercles et dix runes personnelles inchangées. Le chapitre 4 « La voie de l’artisan » décale les anciennes trames 4 à 7 vers 5 à 8 ; le chapitre 5 n’est pas rédigé par cet import. Les nouvelles consignes mobiles qui affectent ses niveaux et compétences restent à arbitrer avant rédaction, sans valider une réponse de ChatGPT par défaut.
- **Chapitre 3 refondu — DEC-026 :** nouvelle version de lecture sur demande explicite de l’auteur, événements et sept sections conservés, autres chapitres inchangés. Moins de reformulations, Hasol compétente en théorie mais fragilisée par le jugement ; sa mère respectait son rêve et attendait qu’elle soit prête à envisager l’artisanat, Orven la responsabilise par le travail. Le premier salaire reste le point culminant. Protocole du mannequin identique au chapitre 2 (DEC-025), troisième touche et arrêt à 78 secondes explicités. Ne pas réimporter silencieusement le chapitre 3 initial de `new.txt` ni anticiper les découvertes du chapitre 4.
- **Chapitre 4 adapté — DEC-027 :** nouvelle version de lecture autorisée après DEC-026, dix sections et événements conservés, autres chapitres préservés. Hasol connaît théoriquement le coût personnel en Mana ; elle apprend à suivre sa réserve dans une journée réelle. Fixe/pourcentage : une explication puis mise en pratique, pas de répétition du cours à la mère et dans le carnet. Le coffret paternel reste unique, la blessure une griffure ; ne pas effacer la reconnaissance antérieure de Zio. Fin orientée vers la fierté et l’initiative sous supervision, sans réconciliation avec le père. Le statut validé de la version mobile initiale ne vaut pas validation de la nouvelle rédaction ; ne pas réimporter l’ancienne version depuis `new.txt`.
- Le père de Hasol est vivant au chapitre 1. Préserver l’amour sous les maladresses et la blessure relationnelle non résolue.
- **Mort future du père — DEC-029 et DEC-033 :** pendant un voyage commercial lointain, avant la large reconnaissance publique d’Hasol comme artisane, sans véritable réconciliation. Il connaît ses débuts chez Orven mais ne voit pas sa pleine réussite reconnue. Date, cause, destination et annonce restent à définir ; ne pas déduire une attaque ou un accident, ni effacer son affection.
- Hasol n’a aucun sort offensif au début. Dix emplacements ne la rendent pas immédiatement invincible.
- **Progression future — DEC-031 :** premier sort offensif au niveau 40, exploitant pleinement sa réserve de Mana exceptionnelle ; Hasol arrive vers le niveau 45 à la fin du livre I. Effet, coût et autres paramètres restent à définir. Ne pas le confondre avec une aura d’arme, l’introduire prématurément, inventer une formule Mana/dégâts ou le rendre automatiquement accessible au niveau 1 dans le livre II au titre des anciens passifs.
- **Maturité future — DEC-032 :** avant le chapitre 13 du découpage de travail, vers vingt-cinq ans, Hasol est une artisane réputée grâce à Œil runique et possède des fonds colossaux pour financer ses runes jusqu’à +15. Ne pas prolonger artificiellement la précarité des débuts ni garantir les réussites. Elle délaisse rapidement le farm intensif pour les donjons avec son groupe, gagne surtout de l’XP sur les boss mais peu de nouveaux cercles : XP et éliminations admissibles sont distinctes. Niveau à vingt-cinq ans, nombre exact de cercles et inventaire amélioré restent à définir, sans changement des états présents.
- **Armes à aura — DEC-028 et DEC-078 :** niveau 10 minimum pour le personnage utilisant une arme imprégnée d'une aura, **y compris Hasol astrale**. Aura runique est disponible dès le niveau 1 astral, mais ne permet pas à Hasol de manier personnellement une arme imprégnée avant le niveau 10. Son potentiel impressionne les recruteurs ; ne pas transformer ce potentiel en usage prématuré ni inventer une scène de recrutement. Ne pas confondre avec les runes, équipables sans niveau minimum.
- Croissance runique se débloque au niveau 10. Huit paliers rétroactifs font passer de deux à dix cercles et emplacements, avec deux runes équipées.
- **Évolution future de Croissance runique — DEC-038 :** vers le niveau 38, cent boss de donjon personnellement achevés déclenchent un nouvel effet : un cercle tous les cent boss, quel que soit leur niveau. Premier cercle immédiat au centième, puis à 200, 300, etc. Cumul avec l'ancien compteur de mille monstres si le boss y est admissible, en gardant les deux suivis distincts et sans recompter les anciens gains. **DEC-056 fixe seize cercles runiques, soit seize emplacements, à la fin du livre I**, vers le niveau 45 ; répartition des gains, occupation effective et report au livre II restent à définir. Préserver les dix cercles actuels et les douze du chapitre 9.
- Ne pas compter deux fois les éliminations déjà récompensées. **Raccord validé du chapitre 9 :** les compteurs après les huit premiers paliers incluent le reliquat historique, sans le chiffrer séparément ; ils ne suivent pas uniquement les éliminations depuis le niveau 10. Ne pas fixer ce reliquat arbitrairement à zéro.
- Écrire **Orven**, pas Orwen. Après insertion du chapitre d’artisanat (DEC-023), il ne découvre l’avantage chiffré de Hasol qu’au chapitre 7 : environ 30 % d’échecs en moins relativement à son propre taux, pas trente points de pourcentage. Au chapitre 4, il découvre seulement son endurance liée au Mana, distincte de ce taux.
- **Résonance runique — DEC-046 et DEC-050 :** actif ciblé, amplifie seulement les principales avant le niveau 40 de Yoon ; à partir de son évolution au niveau 40, inclut aussi les deux premières secondaires présentes sur chaque rune de l'allié ciblé. Les troisième/quatrième secondaires et bonus d'ensemble restent exclus. Pas de conversion en passif ; ordre des secondaires, coefficients et paramètres à définir. Ne pas appliquer l'évolution aux premières chasses ou au sauvetage niveau 24.
- **Yoon précisée — DEC-046 actualisée par DEC-074 :** soutien Sage runique, pas soigneuse pure. Résonance est un **actif ciblé**, pas une aura passive. Chant runique est une **zone de soin posée**, pas un chant continuellement canalisé ; elle peut agir ensuite. L'auteur valide **10 % des PV maximums de Yoon toutes les cinq secondes**, sans en déduire un soin instantané des blessures ou une guérison de soigneuse pure. Ses zones de soin/contrôle sont des cercles d'écritures runiques au sol. Domaine des Entraves au niveau 20, Yoon **54 au chapitre 16**. Amplification, portée, durée et coûts non fixés restent à définir.
- **Couleurs et Tempête arcanique — DEC-047/048 :** vert pour le soin, violet pour le ralentissement ; au **niveau 50**, Yoon obtient **Tempête arcanique**, cercle rouge runique de dégâts sur la durée. La proposition de niveau 30 est remplacée. Effets chiffrés, coût, portée, durée, cibles et cumul restent à définir ; aucun usage anticipé ou effet de tempête supplémentaire déduit du nom.
- **Second soin de Yoon — DEC-049 :** au niveau 30, marque runique posée sur un allié, soin sur la durée ciblé distinct du cercle au sol. Nom officiel, coût, puissance, durée, nombre de marques et cumul à définir. Ne pas en faire un soin instantané ou permanent, ni lui accorder la puissance d'une soigneuse pure. Pas d'usage avant ce niveau, notamment au sauvetage où Yoon est niveau 24.
- Yoon a une progression et une personnalité propres ; elle ne se réduit pas à un bonus pour Hasol.
- **Cercles de Zio — DEC-055 :** huit cercles runiques au niveau 60, soit huit emplacements. Inventaire, occupation effective, étapes d'acquisition et nombre au niveau 61 restent à définir ; ne pas en déduire une progression universelle par niveau.
- **Zio — DEC-053 :** autodestruction obtenue au niveau 50 ; niveau 61 lors du sacrifice final du livre I. Fiche naturelle au niveau 60, hors runes et compétences : PV 11 850, Attaque 648, Défense 593, Vitesse 115, Mana 1 000, Puissance arcanique 600 (profil de soutien). Ne pas extrapoler les statistiques au niveau 61. Le Paladin d'Eden Eternal inspire ses passifs et sorts, ses glyphes servant de référence pour les bonus runiques dans les cercles ; ni renommage de Gardien, ni compétence, soin, inventaire ou nombre de cercles validé automatiquement. Voir `source.md` et `lore/personnages.md`.
- **Union future — DEC-034 :** Hasol épousera Zio Notos dans le livre I. « Zyo » dans la déclaration de l'auteur est compris comme Zio, sans personnage distinct. Construire progressivement leur relation réciproque ; ni romance déjà établie à l'Académie, ni date ou enfant ne sont fixés. L'adhésion ultérieure de Zio à l'équipe est désormais validée séparément par DEC-035. Le mariage de la première vie ne s'impose pas dans le livre II, où Zio ne conserve aucun souvenir.
- **Groupe et donjons — DEC-035 corrigée par DEC-036 :** Ray est un mage de classe **commune**, cinq points, pas rare. Il aide d'abord Hasol sous la pression de sa famille après le sauvetage ; elle accepte pour accéder aux donjons, minimum trois membres. Le trio pèse 35/50 points ; adhésion utile ne signifie pas confiance ou pardon immédiat. Zio rejoint ensuite officiellement le trio et le temps partagé nourrit leur rapprochement : quatre membres, 45/50 points (20 + 10 + 5 + 10), avant l'arrivée du Ranger prévue par DEC-037. Date d'entrée de Zio à définir, rôle initial de superviseur extérieur préservé. Modalités du seuil de donjon à définir, sans nouvelle interdiction des chasses extérieures.
- **Ranger et transmission — DEC-037/041/042, actualisées par DEC-078/080 :** au livre I, **Samia Claire**, Ranger commune, amie de Yoon à l'Académie, rejoint comme cinquième membre (5/5, 50/50). Même âge que Yoon, niveau légèrement inférieur à son introduction ; elle accepte dès qu'elle apprend la présence de Zio. Motif de cet intérêt et chiffres d'introduction à définir, sans attirance automatique. Hasol apprend auprès d'elle la détection des pièges par Œil runique et l'ouverture des coffres par Main runique active. Dans les vies astrales, Œil avec détection des pièges et Main ouvrant coffres et portes **sans restriction** sont disponibles dès le niveau 1 : cela remplace le réapprentissage prévu auparavant. Ne pas attribuer l'ouverture à Aimant runique. Samia ne rejoint plus l'équipe principale de ces nouvelles vies, sans disparition automatique du récit ; les quatre Hasol/Yoon/Zio/Ray réunis pèsent 50/50 points pour 4/5 membres.
- **Motif de recrutement du Ranger — DEC-039 :** les quatre, après l'entrée de Zio, fuient un boss de donjon niveau 32 qui invoque en masse des monstres niveau 11 tant qu'un piège n'est pas désactivé. Zio propose de recruter un Ranger avant le retour. Ne pas fixer le niveau d'Hasol à 32 par confusion, inventer l'issue du retour ou attribuer XP et éliminations des invocations sans règle établie.
- **Invocations infinies et réemploi — DEC-040/081 :** levier majeur des **livres II et III**. Le boss niveau 32 produit des monstres niveau 11 **en nombre infini tant que le piège reste actif et le boss en vie**. Les monstres invoqués comptent sous les conditions habituelles d'élimination personnelle et de niveau : compatibles ici avec Hasol 10 à 29, pas à partir de 30 (monstres 20+ exigés). Leur XP vaut **×0,5 celle d'un monstre classique comparable**. Avant 10, base d'XP, partage, arrondis et gains effectifs restent à définir. Ne pas inventer de quota anti-farm, compter ces invocations comme des boss, accorder une entrée solitaire ou supprimer fatigue et coûts. Mémoire imparfaite au II, parfaite mais non omnisciente au III.
- **Concurrence et privatisation — DEC-082 :** au livre II, d'autres groupes gênent Hasol et tuent le boss, interrompant les invocations. Au livre III, elle fait tout pour privatiser ce donjon afin de sécuriser l'exploitation. Modalités, autorité, coût, calendrier et résultat à définir ; aucun droit de propriété automatique, groupe malveillant, réapparition du boss ou destruction définitive du donjon inventé.
- Dans la première vie, Œil runique ne se débloque qu'au niveau 20, après le sauvetage prévu. Personne ne doit prédire ce pouvoir avant sa découverte. La disponibilité au niveau 1 ne concerne que les nouvelles vies astrales (DEC-078).
- Les futurs validés des livres I et II doivent rester séparés des événements déjà racontés dans les références.

### Continuité récente à contrôler avant chaque chapitre

- **Affinités — DEC-073 :** Eau > Feu > Terre > Eau : avantage ×1,25, faiblesse inverse ×0,75 sur dégâts finaux et précision. Lumière et Ténèbres sont neutres entre elles ; chacune a l'avantage sur les trois éléments du cycle (×1,20), avec faiblesse inverse (×0,80). Même élément neutre. Toutes les attaques réellement élémentaires sont concernées ; précision multiplicative, pas ajout de points. Arrondis, plafonds et cas multiélémentaires à définir.
- **Yoon — DEC-074 :** Vague runique est une attaque de Lumière disponible au niveau 1 : 5 Mana, 20 % de sa Puissance arcanique, portée 10 mètres, incantation 5 secondes, aucune récupération. Cette affinité ne s'étend pas à toute sa classe. Résonance reste active ciblée ; Chant reste une zone posée autonome à 10 % des PV maximums de Yoon toutes les cinq secondes, valeur désormais explicitement validée.
- **Vies astrales — DEC-078 :** au niveau 1 : Bénédiction runique, Croissance runique, Œil runique avec détection des pièges, Main runique active ouvrant coffres et portes sans restriction, Aura runique active. Aimant runique doit être obtenu à nouveau dans chaque vie après un combat avec un Anneau runique ; niveau exact dans ces vies à définir. Les compteurs de Croissance repartent de zéro à chaque nouvelle vie ; ne pas en déduire le nombre de cercles reportés, ni remettre à zéro le reliquat inconnu de la première vie. Mémoire runique n'est obtenue qu'en R11, puis conservée pour la vie 13.

- **Vitesse — DEC-052 :** augmente la vitesse d'incantation et de déplacement ; cette mobilité favorise l'esquive. Aucun taux automatique d'esquive ni effet supplémentaire sur la vitesse d'attaque défini.
- **Cercles — DEC-063 à DEC-065 :** normes au niveau 60 : Commune 4, Rare 6, Légendaire 8 ; Astrale inconnue, les légendes évoquant plus de dix sans vérification. Normes, pas plafonds. Yoon et Zio ont huit cercles chacun au niveau 60 et sont dans le haut du panier des classes rares. Les références au niveau 60 ne fixent pas les nombres en fin de livre I.
- **Difficulté naturelle — DEC-067 :** l'obtention des cercles naturels devient plus difficile avec le niveau. Ne pas inventer de formule ni appliquer automatiquement cette difficulté aux compteurs de Croissance runique. Les courbes proposées dans `lore/pistes.md` restent non validées.
- **Disponibilités au livre I — DEC-067 :** Yoon chasse avec Hasol seulement les week-ends et vacances pendant ses études. Ray, qui a terminé l'Académie, effectue énormément de chasses en duo avec Hasol durant ses propres niveaux 30–40. Zio appartient alors à un autre groupe et rejoint celui d'Hasol quand Yoon termine l'Académie, au chapitre 11. Dates et durées à définir ; chasses à deux distinctes des donjons exigeant trois membres.
- **Ray — DEC-068 à DEC-070 :** mage de feu commun, niveau 56 en fin de livre I. Six actifs et trois passifs détaillés dans `lore/systeme.md` ; au sauvetage niveau 22, compétences jusqu'au niveau 20 seulement. Ses flammes peuvent menacer ses alliés et il épuise rapidement son Mana. Combustion maîtrisée, au niveau 40, ne supprime pas cette faiblesse. Ne pas inventer coûts, récupération ou nombre de sorts avant épuisement. Ses dix cercles sont fixés au niveau 60, pas encore au niveau 56.
- **Fin du livre I :** Hasol environ 45, Yoon 54, Ray 56, Zio 61, Samia 52. Ne pas leur attribuer les fiches naturelles de référence au niveau 60 ; consulter `lore/personnages.md` pour les états et inconnues.
- **Hypothèse du livre II — DEC-066 :** l'idée que faire équipe avec Hasol accroît la collecte de mana et accélère les cercles sera émise, mais sa vérité n'est pas confirmée. Ne pas en faire une aura, un passif ou une explication certaine dans le livre I.

### Don maternel et équipement du chapitre 2 — DEC-013

Hasol conserve HAS-R001, Fatal rare (bleue), 6★, +6 et HAS-R002, Gardien rare (bleue), 6★, +6. Sa mère ajoute huit runes 3★ de grades peu commun (vert) et rare (bleu), pour dix runes équipées au total. Ne pas remplacer les cadeaux paternels et ne pas ajouter dix runes maternelles. Les types retenus sont Fatal, Gardien et Énergie ; Fatal et Gardien doivent être complets. Ne pas réintroduire les deux Lame ou les runes maternelles blanches d’`old.txt`.

**Répartition désormais validée — DEC-020 : quatre Fatal, quatre Gardien, deux Énergie au total**, soit trois Fatal, trois Gardien et deux Énergie parmi les huit cadeaux maternels 3★ verts ou bleus. Fatal fonctionne par quatre, Gardien et Énergie par deux. Deux paires Gardien donnent deux bonus de +15 % Défense, soit +30 % ; pas de cinquième pièce nécessaire. Les caractéristiques individuelles de la version de lecture du chapitre 2 sont des choix délégués de l’assistant, à distinguer de cette répartition explicitement validée. La Fatal rare (bleue) à améliorer jusqu’à +3 est HAS-R003, une nouvelle rune 3★ ; celle du père reste 6★, +6. L’ancienne proposition cinq Fatal, trois Gardien et deux Énergie est abandonnée.

## 9. Contenu des références

**Dernier Rempart — CANON, DEC-071 :** sacrifice de PV réglable par Zio. Plus le pourcentage conservé est faible, plus l'explosion est puissante ; un sacrifice partiel n'impose pas sa mort. Conserver 0 % est fatal et maximise le sort : choix volontaire au dénouement pour vaincre le démon stellaire. Remplace l'obligation de mourir à chaque usage suggérée par DEC-058, sans changer le déblocage au niveau 50 ni le sacrifice final au niveau 61. Formule, assiette précise et interactions restent à définir ; ni dégâts infinis ni victoire automatique universelle.

**Compétences de Zio — CANON, DEC-058 :** actifs : Heurt du Gardien au niveau 1, Défi du Gardien au 10, Égide protectrice au 20, Bénédiction de vigueur au 30 (soin personnel progressif), Rempart de lumière au 40 (protection directionnelle maintenue), Dernier Rempart au 50 (nom officiel de l'autodestruction). Passifs : Maîtrise du bouclier au 1, Ancrage du Gardien au 20, Volonté inébranlable au 60. Effets et limites dans `lore/systeme.md` ; paramètres chiffrés à définir, ni invulnérabilité ni contrôle absolu des ennemis. Au chapitre 5, niveau 45, capacités jusqu'au 40 seulement. Ne pas les attribuer rétroactivement à l'Académie ni étendre ce calendrier à toutes les classes.

**Cercles futurs d'Hasol — CANON, DEC-057 :** 32 cercles runiques (32 emplacements) à la fin du livre II, 36 à la fin du livre III. Les seize de fin du livre I restent validés par DEC-056. Ne pas associer ces jalons au niveau 60, supposer les emplacements occupés, valider les équipements simulés ou en déduire un report automatique entre les deux vies. Niveaux, acquisition et inventaires restent à définir.

- `lore/personnages.md` : identité, âge, apparence, personnalité, motivations, classe, rareté, niveau, XP connue, caractéristiques naturelles, compétences, cercles, emplacements, relations, évolution psychologique, blessures, dernier chapitre d’apparition et historique. Séparer les futurs validés de l’état présent.
- `lore/runes.md` : identifiant, propriétaire, nom, ensemble, grade, couleur, rang de 1 à 6 étoiles, amélioration, principale, secondaires, état équipée/stockée/vendue/détruite, obtention, historique et ensembles actifs. Marquer les valeurs non validées.
- `lore/systeme.md` : classes, XP, caractéristiques, Mana et Puissance arcanique, cercles, équipement, grades, améliorations, ensembles, compétences, équipes et conditions d’évolution. Distinguer règles établies et questions ouvertes.
- `lore/chronologie.md` : événements racontés, futurs validés et propositions dans des sections distinctes ; âges, niveaux et changements connus.
- `lore/decisions.md` : sujet, statut, justification sourcée, fichiers concernés et questions en attente. Ne pas inventer la justification ou la date d’une ancienne décision.
- `lore/pistes.md` : synthèse des propositions non validées et questions issues des échanges, dont les anciens découpages des livres II et III et les coefficients d’XP envisagés. Ce fichier n’est pas une source de canon ; consulter ses statuts et les décisions plus récentes avant réutilisation. Il ne remplace ni les archives ni le plan validé du livre I.
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
