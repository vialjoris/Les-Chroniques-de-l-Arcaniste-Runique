# LES CHRONIQUES DE L'ARCANISTE RUNIQUE
## Dossier de transmission à Codex — plan narratif, canon et trajectoires

> **Statut du document :** synthèse du canon établi dans les échanges et propositions de structuration. Les passages indiqués **[VALIDÉ]** sont des décisions de l'auteur ; **[À CONFIRMER]** signale une valeur ou une décision encore ouverte ; **[PROPOSITION]** désigne une piste créative que Codex ne doit pas imposer comme canon.
> **Cadre validé — DEC-045 :** les seize chapitres du livre I, leurs titres, leur séquence et leurs jalons constituent désormais le plan canonique. Cette validation ne vaut ni validation littéraire des textes 1 à 4, dont les statuts propres sont conservés, ni adoption des paramètres encore ouverts, ni autorisation de rédiger le manuscrit. Elle ne valide aucun découpage des livres II et III.
>
> **Instruction fondamentale :** lire ce document et les chapitres déjà rédigés avant d'écrire ; ne jamais réécrire silencieusement une décision validée. Le manuscrit complet se trouve dans un unique `roman.md` ; les fichiers de référence sont distincts.

---

# 1. Identité et intention du roman

- **Titre :** *Les Chroniques de l'Arcaniste Runique*.
- **Livre I :** *L'Ascension d'une légende oubliée*.
- **Format cible [VALIDÉ — DEC-030] :** trilogie ; le livre III sera le dernier. La répartition précise des arcs entre les livres II et III et le dénouement final restent à définir. La catastrophe à la fin du livre I et le retour temporel au début du livre II sont conservés.
- **Genre :** fantasy LitRPG, aventure, progression, drame, relations humaines, runes et classes.
- **Protagoniste :** Hasol Shun, fille de bonne famille, yeux turquoise, longs cheveux brun sombre attachés en queue-de-cheval.
- **Voix :** troisième personne centrée principalement sur Hasol, prose française immersive, scènes développées, émotions incarnées par des gestes et des interactions, dialogues naturels, rythme non précipité.
- **Principe dramatique :** Hasol possède une classe légendaire et d'immenses statistiques magiques mais aucune compétence offensive au début ; son génie ne se révèle que par le système runique et une endurance forgée par les échecs.
- **Progression :** méritée, graduelle, avec limites concrètes, entraînement, blessures, argent, temps, XP et coopération.
- **Ne pas révéler prématurément :** les pouvoirs futurs, la tragédie finale, la rune temporelle, la véritable nature de la seconde chronologie.

# 2. Hiérarchie des classes et expérience [VALIDÉ]

**Équivalence d’inspiration validée par l’auteur — DEC-009 :** Commune ≈ 2★ natif de Summoners War ; Rare ≈ 3★ natif ; Légendaire ≈ 4★ natif ; Astrale ≈ 5★ natif. Cette correspondance concerne les personnages, pas les étoiles des runes. Les exemples externes au niveau 1 sont documentés dans `source.md`. Sur demande de correction de l’auteur, le chapitre 1 utilise désormais les quatre caractéristiques de départ du Danseur du ciel Vent non éveillé, rang 4★, niveau 1 (DEC-010). Mana et Puissance arcanique conservent leurs valeurs antérieures, faute de conversion définie.

| Rareté | Points d'équipe | Remarques |
|---|---:|---|
| Commune | 5 | Très répandue |
| Rare | 10 | Plus spécialisée ; progression en XP plus rapide que Légendaire à niveau comparable |
| Légendaire | 20 | Exceptionnelle ; meilleure probabilité de gros gains de caractéristiques, mais plus d'XP nécessaire |
| Astrale | 25 | Moins de dix cas recensés dans l'histoire, tous célèbres |

- Les classes ne déterminent **pas** mécaniquement la victoire. Équipement, niveau, compétences et expérience comptent.
- Les statistiques naturelles augmentent à chaque niveau sans répartition manuelle par le personnage. La rareté influence les chances de gains élevés, sans garantie déterministe.
- Rumeur non prouvée : les activités pratiquées avant de monter de niveau pourraient influer sur les gains ; ne pas présenter comme une loi confirmée.
- Équipe : **5 membres maximum, 50 points de classe maximum**. Hasol (20) + Yoon (10) = 30/50 ; avec Ray commun (5), trois membres et 35/50 ; puis avec Zio rare (10), quatre membres et 45/50 (DEC-035 corrigée par DEC-036). Samia Claire, Ranger commune (5), complète le groupe à cinq membres et 50/50. Placements validés par DEC-045 : duo au chapitre 5, Ray au 10, Zio au 11, Samia au 12. Dates exactes à définir ; aucun de ces états futurs n'est déjà survenu.
- **Donjons [VALIDÉ — DEC-035] :** minimum trois membres pour accéder aux donjons. Cette contrainte motive l'acceptation de Ray par Hasol, distincte d'un pardon. Les modalités précises de cette condition restent **[À CONFIRMER]**, sans inventer contrôle magique, sanction ou dérogation ; elle ne s'applique pas aux chasses extérieures déjà racontées.
- Si Hasol monte de niveau durant une période de chasse partagée, examiner systématiquement si Yoon doit monter aussi : sa classe rare nécessite moins d'XP. Ne pas inventer une formule d'XP précise si elle n'est pas définie.

# 3. Runes et amélioration [VALIDÉ sauf précisions]

## 3.1 Grades et affixes

**Toutes les runes ont une caractéristique principale.** Le grade fixe le nombre de **caractéristiques secondaires présentes dès +0** :

| Couleur | Grade | Secondaires à +0 | Total principal + secondaires |
|---|---|---:|---:|
| Blanc | Commun | 0 | 1 |
| Vert | Peu commun | 1 | 2 |
| Bleu | Rare | 2 | 3 |
| Violet | Épique | 3 | 4 |
| Orange | Légendaire | 4 | 5 |

**Quatre caractéristiques secondaires est le maximum.** Ne jamais présenter une rune bleue +0 avec « aucune secondaire ».

**[VALIDÉ — dernière décision de l’auteur du 19 novembre 2026]** Le taux critique, les dégâts critiques, la précision et la résistance peuvent être exprimés en pourcentages, y compris en secondaires. Cette décision remplace l’interdiction générale des secondaires en pourcentage (DEC-003). Les secondaires fixes des cadeaux du père restent inchangées. PV %, Attaque % et Défense % restent à confirmer ; voir `lore/decisions.md`, DEC-004.

## 3.1 bis Rang en étoiles [VALIDÉ]

Chaque rune possède un rang de **1 à 6 étoiles**, indépendant de son grade de couleur et de son niveau d’amélioration. Le grade détermine le nombre initial de secondaires ; le rang influence les valeurs de la principale selon les tables définies. Une rune bleue n’est donc pas nécessairement une rune trois étoiles.

**Règle propre au roman — DEC-007 :** les runes obtenues sur les monstres de niveaux 1–10 sont 1★ ; 11–20, 2★ ; 21–30, 3★ ; 31–40, 4★ ; 41–50, 5★ ; 51–60, 6★. Le cas des monstres de niveau supérieur à 60 reste à définir. Ne pas en déduire une rareté ou une chance de butin. Toujours préciser rareté et étoiles lorsqu’une rune identifiable est mentionnée ; les caractéristiques encore inconnues restent explicitement à définir dans les références.

**Équipement — DEC-008 :** les runes sont équipables à tout niveau du personnage, indépendamment de leur rareté, de leurs étoiles et de leur amélioration, sous réserve de disposer d’un emplacement. Les tranches ci-dessus ne concernent que l’obtention sur les monstres. Hasol peut équiper ses deux cadeaux rares (bleus), 6★, +6 au niveau 1.

L’auteur adopte les quatre lignes de progression des principales de taux critique, dégâts critiques, précision et résistance issues du guide cité dans `source.md`. Elles sont reproduites dans `lore/systeme.md` sous la forme valeur à +0 / gain par niveau / valeur à +15. Ne pas appliquer ces tables aux secondaires. Les deux cadeaux du chapitre 1 sont 6★ +6 ; leurs principales Attaque et Défense valent chacune +70 selon le tableau 6★ de la source. Les autres tables non documentées restent à définir.

## 3.2 Niveaux d'amélioration

- Jalons affichés : **【 +3 】, 【 +6 】, 【 +9 】, 【 +12 】, 【 +15 】** ; les niveaux intermédiaires +1, +2, etc. existent.
- **Précision de l’auteur — DEC-014 :** la principale augmente à chaque amélioration réussie de +1 à +15, avec un gain plus important à +15. Une secondaire est aussi ajoutée ou renforcée à +3, +6, +9, +12 **et +15**. Les règles d’ajout jusqu’à +12 suivent DEC-006 ; à +15, les quatre secondaires déjà présentes impliquent le renforcement de l’une d’elles, pas une cinquième. Ce palier secondaire final est une adaptation propre au roman.
- Les tentatives peuvent échouer ; elles consomment des ressources (pierres de mana) ; préciser les conséquences exactes d'un échec seulement si établies dans le chapitre.
- **Bénédiction runique** : passif initial de Hasol augmentant les chances de réussite, sans les garantir.
- En chapitre 7 après insertion du chapitre d'artisanat (DEC-023), Orven établit que Hasol subit environ **30 % d'échecs en moins que lui, en relatif**, et non « 30 points de pourcentage » (exemple pédagogique : 40 % d'échec pour Orven contre 28 % pour Hasol). Le chiffre exact de chaque série de tests peut être créé de manière cohérente, sans prétendre à une probabilité universelle.
- **Coût et limites — DEC-024 :** chaque tentative consomme des pierres de mana et du Mana personnel, même en cas d'échec. Difficulté selon étoiles, grade et palier ; barèmes **[À CONFIRMER]**. Repos et potions restaurent le Mana sans supprimer toute fatigue mentale. La grande réserve de Hasol donne de l'endurance, pas une maîtrise automatique. Enseignement raconté au chapitre 4, distinct de la mesure des échecs au chapitre 7.
- **Œil runique** : déblocage **uniquement au niveau 20**, après le sauvetage de Ray ; révèle les caractéristiques finales prédéterminées d'une rune à +15. Personne ne connaît ni ne prédit ce pouvoir avant sa découverte.

## 3.3 Ensembles officiels

| Ensemble | Pièces | Bonus |
|---|---:|---|
| Fatal | 4 | +35 % Attaque |
| Vitesse | 4 | +30 % Vitesse |
| Énergie | 2 | +15 % PV |
| Gardien | 2 | +15 % Défense |
| Lame | 2 | +12 % chance critique |

Le bonus d'ensemble s'active selon le nombre de runes de cet ensemble équipées. Préciser dans `systeme.md` l'ordre exact des opérations (bonus plat, pourcentage, arrondis) **avant** de publier des totaux calculés complexes ; sinon afficher les bonus séparément sans fabriquer un total.

## 3.3 bis Principales fixes et principales en pourcentage [VALIDÉ — DEC-011]

L’auteur souhaite qu’Orven explique dans l’histoire que les principales en valeur fixe sont plus avantageuses à bas niveau, quand les caractéristiques naturelles sont encore faibles. Avec leur croissance, les principales en pourcentage deviennent rapidement plus intéressantes.

Présenter ce principe comme un conseil d’équipement contextualisé, à rang en étoiles et amélioration comparables, pas comme une supériorité absolue de toute rune en pourcentage sur toute rune fixe. Le point de bascule dépend des valeurs comparées et de la caractéristique naturelle concernée ; aucun niveau universel n’est fixé. L’intention d’une bascule rapide devra être vérifiée avec la progression chiffrée du roman avant de publier un exemple.

Cette décision admet les principales PV %, Attaque % et Défense %, sans adopter ces mêmes unités en secondaires. **Assiette précisée par DEC-024, racontée au chapitre 4 :** pourcentage calculé sur la caractéristique naturelle, avant ajout des bonus fixes runiques. Comparaison pédagogique +50 Attaque / +10 % : +20 à 200 naturels, +50 à 500, +200 à 2000. Ces exemples ne définissent pas de nouvelles tables. Le barème complet, les ensembles et les arrondis restent à documenter. Ne pas modifier rétroactivement les deux cadeaux rares (bleus), 6★, +6 du père.

## 3.4 Deux runes initiales de Hasol

> **Dernière décision prioritaire — DEC-006, 19 novembre 2026 :** les cadeaux sont **bleus 6★ déjà +6**. Conformément à la source, +3 et +6 renforcent deux secondaires existantes, sans ajout ; une rune bleue conserve deux secondaires à +6, gagne la troisième à +9 et la quatrième à +12. Les renforcements individuels ci-dessous sont des choix éditoriaux délégués, pas un barème fourni par le guide. La Fatal bleue à améliorer jusqu’à +3 au chapitre 2 devra être une autre rune si cette scène est conservée.

- Son père lui offre **deux runes bleues 6★ déjà +6** lors de la Révélation à 16 ans : **Fatal, principale Attaque +70** ; **Gardien, principale Défense +70**. Les principales suivent le tableau 6★ de la source : 22 à +0 et +8 par niveau, soit 70 à +6.
- **Secondaires natives à +0 validées dans DEC-001 :** Fatal, **Vitesse +2 et PV +15** ; Gardien, **PV +20 et Mana +10**. **Valeurs renforcées à +6 choisies par délégation dans DEC-006 :** Fatal, **Vitesse +4 et PV +25** ; Gardien, **PV +30 et Mana +20**. Les fiches des niveaux 1, 9 et 10 du chapitre 1 affichent les valeurs renforcées séparément des caractéristiques naturelles.
- Les deux runes restent équipées à +6 pendant les trois années de l’Académie ; ne pas les retirer ni les améliorer davantage avant le moment prévu.
- Ne pas confondre **statistiques naturelles** et **bonus runiques**.

## 3.5 Présentation des interfaces

- `roman.md` contient du Markdown et des blocs HTML ; un `style.css` externe est chargé dans l'aperçu VS Code via `.vscode/settings.json` : `"markdown.styles": ["./style.css"]`.
- Dans les fiches : caractéristiques naturelles en couleur normale, bonus de runes en bleu (`class="rune-bonus"`), buffs temporaires en vert (`class="temporary-bonus"`).
- Bulles d'amélioration visuellement marquées, par exemple `<span class="upgrade-badge">+6</span>` ; l'intitulé narratif peut utiliser `【 +6 】`.
- Fenêtres HTML réutilisables : `system-window`, `character-sheet`, `rune-window`, `system-header`, `legendary-text`, `success-text`, `passive-badge`.
- L'aperçu Markdown natif de GitHub ne charge pas arbitrairement le CSS ; le rendu stylé suppose VS Code configuré ou un site dédié.

# 4. Personnages et relations [VALIDÉ]

## Hasol Shun
- Âge 16 à la Révélation ; 19 ans à l'expulsion et au niveau 10 ; 34 ans environ à la fin du livre I.
- Classe **Arcaniste runique**, Légendaire ; deux cercles de mana avant la Révélation (premier à 7 ans, second à 10 ans).
- Départ : aucun sort offensif, grandes statistiques de Mana et Puissance arcanique, faibles capacités physiques.
- **Profil magique — DEC-015 :** classe de soutien mais Puissance arcanique comparable au profil d’un mage. Repères normaux au niveau 60 : Mana 1000 ; Puissance arcanique 600 pour un soutien, 2000 pour un mage. Hasol est hors norme en Mana et dépassera largement 1000 ; le niveau du franchissement et ses valeurs futures exactes restent à fixer. Ces normes ne sont pas des plafonds et ne constituent pas une formule de progression. Ne pas lui accorder de sort offensif pour autant.
- Traits : travailleuse, sensible, tenace, apprend progressivement à coopérer et à utiliser ses limites comme ressort tactique ; ne devient pas arrogante après ses premiers succès.
- Passifs : Bénédiction runique dès le niveau 1 ; Croissance runique au niveau 10 ; Œil runique au niveau 20.
- **Progression future [VALIDÉ — DEC-031] :** premier sort offensif au niveau 40, conçu pour exploiter pleinement sa réserve de Mana exceptionnelle ; Hasol atteint environ le niveau 45 à la fin du livre I. Nom, effet, coût, conditions détaillées et valeurs de caractéristiques restent **[À CONFIRMER]**. L'usage combattif d'une aura sur une arme n'est pas ce premier sort offensif.
- **Maturité artisanale [VALIDÉ — DEC-032 et DEC-045] :** construction dès les chapitres 10 et 11, réputation installée au chapitre 12, vers vingt-cinq ans, avant le chapitre 13. Hasol est déjà une artisane réputée grâce à Œil runique et dispose de fonds colossaux permettant de financer ses runes jusqu'à +15. Son niveau de personnage et son inventaire exact à cette date restent **[À CONFIRMER]**. Elle privilégie les donjons avec son groupe et l'XP des boss plutôt que le farm intensif : sa croissance en niveaux ne signifie pas une multiplication rapide des cercles.
- Motivation immédiate : devenir suffisamment forte pour ne plus être blessée lors des chasses avec Yoon et pouvoir protéger sa partenaire.

## Père de Hasol
- Affectueux durant l'enfance, l'appelle « ma princesse », finance son éducation et offre les deux runes bleues.
- Sa fierté se transforme en inquiétude et en distance pendant les trois années d'échec ; **il est vivant pendant le chapitre 1**.
- Meurt **au chapitre 11, pendant un voyage commercial lointain, avant la large reconnaissance de la réputation artisanale d'Hasol** — DEC-029, DEC-033 et placement DEC-045. Il connaît ses débuts chez Orven, mais ne voit pas sa pleine reconnaissance publique. Le dernier échange difficile et l'absence de réconciliation satisfaisante préservent la douleur du non-dit ; date, intensité et contenu de cette conversation, destination, cause exacte du décès et modalités de l'annonce restent **[À CONFIRMER]**.
- Éviter la caricature du père cruel : l'amour persiste sous les maladresses.

## Mère de Hasol
- Aimante, attentive, liée aux soins et à l'artisanat runique.
- Apprend à Hasol la valeur des runes, lui donne huit runes supplémentaires au chapitre 2, puis la met en relation avec Orven.
- Présence émotionnelle stable, mais peut s'inquiéter du surmenage de sa fille.

## Maître Orven
- Orthographe canonique : **Orven**, pas Orwen.
- Marchand / artisan runique avec plus de 25 ans d'expérience.
- Rencontre au chapitre 3 ; devient employeur et mentor de Hasol.
- **Ne découvre la supériorité chiffrée de Hasol sur le taux d'échec qu'au chapitre 7** (ancien chapitre 6, décalé par DEC-023). Au chapitre 4, seule l'endurance liée à son Mana est remarquée.
- Recommande Hasol à la grande guilde **Griffon d'Argent** pour des améliorations jusqu'à +6, afin qu'elle gagne des ressources pour ses propres runes.
- **Enseignement raconté — DEC-011 et DEC-024 :** chapitre 4, section IV, puis conseil à une cliente en VII ; intérêt des principales fixes à bas niveau et des pourcentages avec la croissance, calcul sur les caractéristiques naturelles. Ne pas le répéter ensuite comme une première découverte.

## Yoon Notos
- 16 ans au début de son arc ; classe **Sage runique**, Rare.
- **Rôle [VALIDÉ — DEC-046] :** soutien polyvalent, pas soigneuse pure. Son soin sur la durée reste très inférieur à celui d'une soigneuse spécialisée ; son apport combine renforcement, placement des zones et contrôle du terrain.
- Niveau 5 lors de la rencontre au chapitre 5. Les niveaux de fin des chapitres 5 à 8 restent **[À CONFIRMER]** : les deux chasses du chapitre 5 rendent obsolète l'ancienne trajectoire automatique 5→7→8. Le chapitre 9 montre sa progression et le déblocage du niveau 20 avant son niveau 24 au sauvetage du chapitre 10 (DEC-045).
- **Résonance runique [DEC-046 et DEC-050] : actif ciblé**, amplifiant temporairement **les caractéristiques principales des runes équipées** d'un allié choisi. Avant le niveau 40 de Yoon, les secondaires sont exclues ; **au niveau 40, l'évolution inclut aussi les deux premières secondaires de chaque rune**. Les troisième et quatrième secondaires et les bonus d'ensemble restent exclus. Ce n'est pas une aura passive ; amplification, durée, coût, portée, récupération et règle précise d'ordre des secondaires **[À CONFIRMER]**.
- **Chant runique [DEC-046] : zone de soin posée**, prodiguant des soins progressifs modestes relativement à une soigneuse pure. Yoon peut agir après l'avoir posée ; ne plus lui imposer un chant continuellement maintenu par concentration. Cadence, valeur, assiette, rayon, durée, coût et cumul **[À CONFIRMER]** ; l'ancien exemple 10 % toutes les cinq secondes n'est pas adopté automatiquement.
- Fréquente l'Académie en semaine, chasse avec Hasol le week-end.
- **Prochain sort au niveau 20 [confirmé DEC-046] : Domaine des Entraves Runiques**, contrôle de foule par zone de ralentissement, alliés épargnés, Mana consommé pour le maintien ; adversaires puissants partiellement résistants. Aucun nouveau sort de contrôle au niveau 10 n'est ajouté. Paramètres chiffrés **[À CONFIRMER]**.
- **Second soin au niveau 30 [VALIDÉ — DEC-049] :** Yoon pose une marque runique sur un allié pour un soin sur la durée, distinct du cercle de soin au sol. Nom du sort, puissance relative, durée, coût, portée, nombre de marques et cumul avec le soin de zone **[À CONFIRMER]**. Ne pas le transformer en soin instantané, en régénération permanente ou en soin de groupe automatique.
- **Évolution au niveau 40 [VALIDÉ — DEC-050] :** Résonance conserve sa forme active ciblée et ajoute les deux premières secondaires de chaque rune aux caractéristiques amplifiées. Pas de transformation en passif, pas de création d'affixes manquants ni d'amplification des ensembles.
- **Signature visuelle [DEC-046] :** ses zones au sol sont des cercles parcourus d'écritures runiques, rappelant sa classe de Sage runique. Cela concerne les zones de soin et de contrôle, sans imposer un fonctionnement de zone à Résonance, qui reste ciblée. Ne pas inventer permanence, empilement illimité ou effet de piège.
- **Couleurs [VALIDÉ — DEC-047 et DEC-048] :** vert pour le soin, violet pour le ralentissement, rouge pour **Tempête arcanique, obtenue au niveau 50**, zone de dégâts sur la durée. La suggestion de niveau 30 est remplacée. Puissance, coût, durée, rayon, cadence et règles de cumul restent **[À CONFIRMER]** ; aucun usage avant le niveau 50.
- À l'époque du sauvetage de Ray, niveau **24**.
- **Fin du chapitre 16 [VALIDÉ — DEC-046] : niveau 54**, tandis qu'Hasol est autour de 45. Dates et gains intermédiaires, caractéristiques et compétences ultérieures **[À CONFIRMER]** ; ce jalon ne donne pas de formule d'XP ni de gain de statistiques automatique à recopier.
- **Tempête arcanique [VALIDÉ — DEC-048] :** sort actif de zone au niveau 50, cercle rouge au sol avec écritures runiques, dégâts progressifs. Son acquisition précède le niveau final 54 ; chapitre précis et première utilisation à fixer, sans lui attribuer une attaque instantanée, des effets météorologiques ou une immunité des alliés non décidés.
- Relation avec Hasol : partenariat durable, confiance construite par l'action, complicité et différences de rythme ; éviter que Yoon soit une simple source de buff.

## Zio Notos
- Frère aîné de Yoon ; classe **Gardien**, Rare ; niveau **45** prévu au chapitre 5 après décalage DEC-023, pas attribué à son intervention passée à l'Académie.
- **Présence et popularité [VALIDÉ — DEC-043] :** Zio est très beau et fort, ce qui le rend très populaire. Détails physiques et portée exacte de sa notoriété **[À CONFIRMER]** ; cette popularité n'impose ni arrogance ni comportement séducteur et ne garantit pas la victoire.
- A défendu Hasol d'intimidateurs à l'Académie.
- **Union future [VALIDÉ — DEC-034 et DEC-045] :** Zio devient l'époux d'Hasol dans le livre I. L'auteur écrit « Zyo », compris comme Zio Notos, personnage existant ; conserver l'orthographe canonique Zio. Rapprochement amorcé par la vie partagée au chapitre 11, puis amour et mariage au chapitre 13 ; dates, âges et étapes précises restent **[À CONFIRMER]**. Construire une relation progressive et réciproque, distincte de sa reconnaissance pour l'intervention à l'Académie.
- Intervient pour sauver Hasol et Yoon au chapitre 5 ; conseille de prévoir les dangers au lieu de seulement réagir.
- Au dénouement du livre I, chapitre 16, son ultime est une **autodestruction** : l'explosion tue Zio et le **démon stellaire**, permettant à Hasol de survivre. Ce n'est pas une mort par simple épuisement (DEC-045).
- **Adhésion future [VALIDÉ — DEC-035, DEC-036 et DEC-045] :** au chapitre 11, après Ray, Zio rejoint officiellement Hasol, Yoon et Ray ; leur équipe compte alors quatre membres et 45/50 points. Le temps partagé en mission et au quotidien construit le rapprochement avec Hasol. Date et circonstances précises restent **[À CONFIRMER]** ; il reste superviseur extérieur au début. Ni ce groupe ni le mariage ne sont automatiquement reproduits dans la seconde chronologie.

## Ray Corvus
- Étudiant de l'Académie impériale, classe **mage**, **Commune — correction prioritaire DEC-036**, soit cinq points d'équipe. **[VALIDÉ — DEC-021]** Apparaît dès le chapitre 1, section VII ; son niveau à cette date reste **[À CONFIRMER]**. Le niveau **22** est prévu lors du futur sauvetage, pas attribué rétroactivement à l'Académie.
- **[VALIDÉ — DEC-021]** Ami d'enfance de Hasol, leurs familles étant liées commercialement ; ils jouaient dans les jardins Shun et projetaient des aventures communes. Il devient complice des humiliations : rit, minimise leur amitié et ne défend pas Hasol lorsque son carnet est arraché. Zio le confronte ; Ray part sans présenter d'excuses. Sa spécialité magique reste **[À CONFIRMER]**.
- **Savoir et amitié [VALIDÉ — DEC-044] :** véritable rat de bibliothèque, Ray possède de très nombreuses connaissances, davantage qu'Hasol. Leur proximité d'enfance vient notamment de cette curiosité et de ce savoir partagés ; ils passaient beaucoup de temps ensemble. Domaines précis, lectures, scènes d'enfance et limites de ce savoir **[À CONFIRMER]**. Ne pas le rendre omniscient, annuler les acquis théoriques d'Hasol ou utiliser son érudition comme excuse de son comportement à l'Académie.
- Au chapitre 10 (DEC-045), Hasol et Yoon le sauvent d'un loup alpha élite de niveau 25 à 27. **[VALIDÉ — DEC-035]** Sa famille, informée du sauvetage, lui impose d'aider Hasol. Les débuts sont difficiles ; elle l'accepte parce qu'un duo limite leurs possibilités et que les donjons exigent au moins trois membres. Coopération utilitaire d'abord, confiance et éventuelles réparations sincères construites ensuite, sans conversion instantanée.
- Son intégration porte l'équipe à trois membres et 35/50 points (DEC-036).

## Samia Claire — Ranger [VALIDÉ, DEC-037 ET DEC-041]
- **Samia Claire est une femme, amie de Yoon à l'Académie.** Cinquième membre prévu du groupe du livre I, classe **Ranger, Commune**, cinq points : archerie, détection des pièges et ouverture des coffres. Il ne s'agit pas d'un simple rôle de dégâts à distance.
- **Âge et niveau [VALIDÉ — DEC-042] :** même âge que Yoon, niveau légèrement inférieur lors de son introduction ; valeurs exactes au recrutement à fixer selon la chronologie. Ne pas la maintenir artificiellement à seize ans si Yoon a vieilli ni inventer un écart chiffré de niveaux. Apparence, personnalité, équipement et compétences détaillées **[À CONFIRMER]**.
- **Acceptation [VALIDÉ — DEC-042] :** Samia accepte de venir dès qu'elle apprend que Zio fait partie du groupe. La raison exacte de cet intérêt reste **[À CONFIRMER]** : ne pas déduire automatiquement une attirance amoureuse, une connaissance antérieure de Zio ou une rivalité avec Hasol. Ne pas réduire Samia à une place dans la composition ou à une source de pouvoirs.
- **Contexte précisé — DEC-043 :** beauté, force et popularité de Zio donnent un contexte à l'intérêt de Samia. Ses sentiments précis et la façon dont elle les exprime restent à construire, sans triangle amoureux imposé.
- **Motif du recrutement [VALIDÉ — DEC-039 et DEC-045] :** au chapitre 12, après l'adhésion de Zio, les quatre affrontent en donjon un boss niveau 32 qui invoque en masse des monstres niveau 11 tant qu'un piège n'est pas désactivé. Ils fuient ; Zio, le plus expérimenté, propose de recruter une Ranger avant de revenir. Samia est déjà une amie de Yoon (DEC-041) et rejoint le groupe dans ce chapitre ; modalités de présentation, conditions détaillées d'adhésion et résultat de la seconde expédition restent **[À CONFIRMER]**. Le niveau 32 est celui du boss, pas celui d'Hasol.
- Au chapitre 13, dans la progression vers la fin du livre I, Hasol apprend auprès de Samia l'ouverture des coffres et la détection des pièges. Cet apprentissage long conduit à une amélioration d'Œil runique et à l'obtention de Main runique, sans niveau exact ni recette de déblocage définis ; pas de capacités gratuites dès le recrutement.
- Œil runique garde son nom et sa lecture des caractéristiques finales des runes ; il gagne la détection des pièges. Main runique est un sort actif d'ouverture des coffres. Coûts, portée, limites, délai de récupération et types de pièges ou serrures couverts restent **[À CONFIRMER]**.
- Livre II : Hasol doit pouvoir assurer ces fonctions sans recrutement indispensable d'une Ranger. Elle retrouve le passif selon la règle des anciens passifs et **réapprend rapidement Main runique**, pas automatiquement au niveau 1. Cela ne décide ni du sort de Samia ni de sa place éventuelle dans la seconde vie.

# 5. Progression vérifiée de Hasol

## Fiches naturelles déjà établies

| Niveau | PV | Attaque | Défense | Vitesse | Mana | Puissance arcanique |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2940 | 199 | 182 | 100 | 30 | 20 |
| 9 | 3045 | 211 | 191 | 113 | 310 | 186 |
| 10 | 3058 | 213 | 192 | 115 | 355 | 211 |

**Méthode de correction — DEC-010 :** nouvelle base de niveau 1 issue du profil de soutien 4★ non éveillé de la source ; conservation des gains naturels déjà racontés. Les fiches 9 et 10 sont celles du roman recalculées, pas les statistiques de niveaux 9 et 10 de Summoners War. **Précision DEC-015 :** le rôle de soutien d’Hasol n’impose pas un profil magique de soutien : sa Puissance arcanique est celle d’un mage et son Mana dépassera largement la norme de 1000 au niveau 60. Les repères ordinaires sont 600 de Puissance arcanique pour un soutien et 2000 pour un mage au niveau 60 ; les courbes exactes restent à définir, sans remplacer les fiches actuelles par interpolation.

- Passage 1→2 : +10 PV, +1 Attaque, +0 Défense, +1 Vitesse, +28 Mana, +17 Puissance arcanique.
- Passage 8→9 : +12 PV, +1 Attaque, +0 Défense, +2 Vitesse, +24 Mana, +16 Puissance arcanique.
- Passage 9→10 : +13 PV, +2 Attaque, +1 Défense, +2 Vitesse, +45 Mana, +25 Puissance arcanique.
- **Attention :** ces fiches représentent les statistiques **naturelles**. Ajouter séparément les deux principales runiques et les quatre secondaires à leurs valeurs renforcées de +6, documentées dans `lore/runes.md`.
- Les autres niveaux ne sont pas chiffrés ici ; ne pas interpoler comme s'il existait une table officielle.

## Croissance runique

- Niveau 10 : +1 cercle et +1 emplacement **par tranche de 1 000 monstres admissibles tués** ; application rétroactive.
- Après plus de 8 000 slimes de niveau 1 éliminés sur trois ans : **8 tranches**, soit passage de **2 à 10 cercles / emplacements**, avec seulement 2 runes équipées à l'instant du déblocage.
- Monstres admissibles : niveaux de Hasol 10–19 → monstres de niveau 1+ ; 20–29 → niveau 10+ ; 30–39 → niveau 20+, et ainsi de suite.
- Entre niveau 10 et niveau 19, Hasol tue **au moins 2 000 monstres admissibles supplémentaires en solo**, permettant 10→11→12 cercles/emplacements. Éviter de compter deux fois les 8 000 premiers.
- **Rythme ultérieur [VALIDÉ — DEC-032] :** Hasol abandonne rapidement le farm intensif de petits monstres pour suivre son groupe en donjon. Son XP provient surtout des boss, tandis que les seuils de 1 000 monstres sont franchis peu souvent. Ne pas convertir un gros gain d'XP en nombreuses éliminations ou en cercle supplémentaire. Le moment précis de cette transition et le nombre final de cercles restent **[À CONFIRMER]** ; aucun gain rétroactif n'est ajouté.
- **Évolution future [VALIDÉ — DEC-038 et DEC-045] :** au chapitre 14, vers le niveau 38, après avoir personnellement achevé cent boss de donjon, Croissance runique gagne un effet supplémentaire : un cercle par tranche de cent boss personnellement achevés, quel que soit leur niveau. Les cent premiers donnent immédiatement le premier cercle lors de l'évolution ; les suivants arrivent à 200, 300, etc. L'ancien effet de mille monstres demeure. Un boss peut avancer les deux compteurs s'il satisfait aussi l'admissibilité de l'ancien, sans compter plusieurs éliminations dans ce dernier. « Vers le niveau 38 » est un repère de trajectoire, pas un niveau minimum supplémentaire imposé. Total de cercles et calendrier exact **[À CONFIRMER]**.

# 6. PLAN NARRATIF DU LIVRE I — CHAPITRES 1 À 16 [VALIDÉ — DEC-045]

> L'auteur valide le plan des chapitres par « je valides le plan des chapitres » : titres, ordre et jalons des seize chapitres du livre I sont **CANON** (DEC-045). Les chapitres 1 à 4 sont présents dans le manuscrit, avec leurs statuts littéraires distincts ci-dessous, intégralement préservés. L'insertion de « La voie de l'artisan » maintient les anciennes trames 4 à 7 aux places 5 à 8 (DEC-023). La validation ferme notamment le placement de Hasol 10→11 et d'Aura runique à la fin du chapitre 5 ; elle ne valide pas les paramètres encore ouverts ni les réponses de ChatGPT par défaut. Aucun chapitre nouveau n'est autorisé à la rédaction par cette seule validation. Les livres II et III ne reçoivent aucun découpage validé, à douze ou à seize chapitres.

## Chapitre 1 — « La légendaire inutile » [TEXTE VALIDÉ — DEC-018 ET DEC-022]

**Validation de l’auteur le 19 novembre 2026 :** version actuelle de `roman.md`, après reprise DEC-016 et correction DEC-017. Niveau 8 en section VII, passage au niveau 9 en section VIII ; treize sections au total. Les corrections runiques sont intégrées. Toute modification rétroactive demande une nouvelle autorisation ; les questions des chapitres suivants ne remettent pas silencieusement ce texte en chantier.

**Révision DEC-021 validée le 20 novembre 2026 — DEC-022 :** les sections I et VII sont actualisées depuis les deux premiers apports de `new.txt`, puis approuvées par « ok je valide ». L'auteur confirme que « Modif chap 2 » désigne en réalité la scène d'Académie du chapitre 1. Les sections II à VI et VIII à XIII, les statistiques et le chapitre 2 sont préservés. Cette validation ne porte pas sur le chapitre 2 ou les propositions futures.

**Période :** enfance de Hasol → 16 ans → trois années d'Académie → 19 ans, niveau 10.

**Ouverture actualisée — DEC-021 :** la veille de ses seize ans, Hasol peine à dormir et se remémore l'éveil de son premier cercle à sept ans. Scène de joie avec son père, puis soirée près de la cheminée : il explique la Révélation, les quatre raretés, les gains naturels et les limites des équipes avec cinq pièces de bois. Elle souhaite un groupe où chacun s'entraide ; il lui promet son soutien même en cas de classe commune ou de difficultés. Retour à la veille de la Révélation ; deuxième cercle à dix ans, livres, cours et salle d'entraînement évoqués. L'exposition passe par leur relation, sans changer les règles.

**Révélation :** cérémonie au temple, stèle dorée, émergence de la classe légendaire **Arcaniste runique**, Bénédiction runique. Joie familiale et fierté publique. Pas de prophétie temporelle.

**Cadeaux :** le père offre deux runes **bleues 6★ +6**, Fatal (principale Attaque +70 ; secondaires renforcées Vitesse +4 et PV +25) et Gardien (principale Défense +70 ; secondaires renforcées PV +30 et Mana +20), équipées immédiatement sur les deux cercles. Chacune conserve deux secondaires selon la règle de la source. La famille célèbre.

**Académie :** impossibilité de lancer des sorts malgré la forte Mana/Puissance arcanique ; entraînement physique et à l'épée, premières moqueries. Montrer le contraste entre gains magiques et besoins physiques. Exemple de passage au niveau 2 fixé dans le canon.

**Poids de groupe — reprise autorisée DEC-016 :** conserver l’explication des quatre coûts de classe et des deux plafonds, puis montrer leur effet humain dans une scène de refus au niveau 3. Un groupe de quatre (deux rares, deux communs) pèse trente points ; avec Hasol, cinq membres et cinquante points seraient légaux. Il la refuse néanmoins parce que sa compétence ne l’aide pas directement au combat. Ne pas reproduire une comparaison de « deux rares ou quatre communes » comme si ces remplacements tenaient dans l’unique place restante. Préparer la blessure relationnelle qui donnera son sens au choix futur de Yoon.

**Profil magique — reprise DEC-016 validée dans DEC-018 :** un professeur explique les normes au niveau 60 et le contraste soutien/mage de DEC-015 lors d’un entretien évoqué dans la section du niveau 9. Ces chiffres sont des repères, pas des prédictions ou une promesse de compétence offensive.

**Dégradation sur trois ans :** déceptions des enseignants, élèves qui progressent vers le niveau 30, Hasol qui n'atteint que le niveau 9, plus de 8 000 slimes de niveau 1 tués pour 1 XP chacun. Insérer des scènes de travail répétitif sans les rendre mécaniques : saisons, fatigue, obsession, évolution des relations. **Scène développée DEC-021, section VII, Hasol niveau 8 :** son ancien ami Ray Corvus participe aux rires, minimise leur amitié et reste passif pendant la confiscation du carnet. Zio le fait rendre, confronte Ray et encourage Hasol à noter ses progrès, sans combat ni réconciliation avec Ray. Cette scène remplace l'ancien épisode et le résumé de l'intervention, sans doublon. Le père se distancie par peur et déception sans cesser de l'aimer ; la mère demeure un soutien.

**Expulsion :** Académie refuse de prolonger sa scolarité ; scène de solitude et humiliation. Dîner familial pénible, père déçu, mère protectrice ; **père vivant**. Hasol sort secrètement la nuit.

**Point culminant :** dernier slime pour +1 XP, niveau 9→10 ; gain naturel exact +13 PV, +2 Attaque, +1 Défense, +2 Vitesse, +45 Mana, +25 Puissance arcanique. Désespoir devant de nouveaux gains magiques inutilisables, puis déblocage de **Croissance runique**. Huit paliers rétroactifs : 2→10 cercles/emplacements, 2/10 runes équipées. La chasse jugée inutile prend un sens nouveau.

**Fin :** espoir intime et décision de prouver sa valeur ; aucune puissance instantanée artificielle, aucun sort offensif. Préserver la blessure relationnelle avec le père.

**Contrôle avant validation :** fiches naturelles lvl1/lvl9/lvl10 exactes ; deux secondaires pour chaque rune bleue ; ne pas afficher « aucune secondaire » ; ne pas appliquer un ensemble avec une seule Fatal et une seule Gardien.

## Chapitre 2 — « La véritable valeur d'une rune » [TRAME VALIDÉE ; TEXTE EN LECTURE — DEC-019]

Le texte est présent à la suite du chapitre 1 dans `roman.md`, avec les fenêtres HTML reconstruites. La composition quatre Fatal, quatre Gardien et deux Énergie est explicitement validée par DEC-020 ; les scènes adaptées et les valeurs individuelles déléguées restent à relire. Aucun changement du chapitre 1 validé.

**Point de départ :** Hasol revient de sa nuit de Révélation personnelle, toujours fragile mais pleine d'espoir. Sa mère perçoit le changement et accepte de l'aider à comprendre le potentiel runique.

**Séquence 1, pédagogie incarnée :** discussion à l'atelier maternel : cercles, emplacements, caractéristique principale, secondaires, grades, améliorations, ensembles. Éviter une exposition sèche : montrer des pierres, leurs textures, le coût et les choix. Expliquer que dix emplacements sont remarquables, mais qu'une rune seule ne suffit pas.

**Séquence 2, don — DEC-013 et répartition corrigée DEC-020 :** la mère offre **huit runes supplémentaires 3★**, de grades **peu commun (vert) et rare (bleu)** : **trois Fatal, trois Gardien, deux Énergie**. Hasol conserve les cadeaux paternels rares (bleus), 6★, +6, HAS-R001 et HAS-R002. Total validé : **quatre Fatal, quatre Gardien, deux Énergie**, dix runes équipées sur dix emplacements. L’ancienne proposition cinq Fatal, trois Gardien et deux Énergie est abandonnée ; pas de Lame. L’inventaire individuel de la version de lecture figure dans `lore/runes.md`.

**Séquence 3, ensembles :** quatre ensembles complets de trois types : un Fatal (4) +35 % Attaque, deux Gardien (2 + 2) +15 % Défense chacun, soit +30 %, et un Énergie (2) +15 % PV. Aucun Lame. Les pièces isolées ne donnent pas de nouvel ensemble. Ne pas rendre Hasol invincible.

**Séquence 4, amélioration :** Hasol commence à améliorer une nouvelle rune **Fatal rare (bleue), 3★, jusqu’à 【 +3 】**, distincte du cadeau paternel rare (bleu), 6★, déjà +6 ; progression par tentatives et ressources, Bénédiction runique utile mais non infaillible. Les secondaires et leur évolution doivent être consignées. Les exemples d’anciens brouillons sur la distribution de bonus ne sont pas automatiquement canon.

**Séquence 5, test réaliste :** mannequin simulant un guerrier ordinaire de niveau 10, arrêt à la troisième touche reçue ; temps mesuré jusqu'à cette touche. Hasol conserve ces réglages pour ses essais comparatifs (DEC-025). Elle perd en **42 secondes**, porte **1 coup** et en reçoit **3**. L'échec montre que l'équipement ne remplace ni réflexes ni technique. Le chapitre 3 refondu explicite désormais la reprise de ce protocole à 78 secondes (DEC-026), sans nouvelle modification du chapitre 2.

**Séquence 6, première chasse :** Bois des Crocs Gris ; combat contre **trois loups de niveau 5**, **12 XP chacun, soit 36 XP** pour Hasol si elle reçoit l'intégralité des éliminations. Elle subit une griffure au bras, utilise une potion et constate sa fragilité. Compteur Croissance runique depuis l'activation : **3 / 1 000**, sous réserve de la convention de suivi adoptée.

**Fin :** désir d'améliorer à la fois son jeu d'épée, son équipement et son économie. Une force naissante, pas un triomphe total.

**Vérification :** 10/10 runes, deux cadeaux paternels rares (bleus), 6★, +6 conservés, huit ajouts maternels 3★ verts ou bleus, composition arrêtée avant rédaction des fiches, Fatal et Gardien complets, ensembles calculés sans Lame, 36 XP, blessure et potion, nouvelle Fatal rare (bleue), 3★, +3 clairement identifiée.

## Chapitre 3 — « Le prix d'un rêve » [TRAME VALIDÉE ; REFONTE EN LECTURE — DEC-026]

Texte initial transmis dans `new.txt` et intégré par DEC-023, puis refondu sur demande explicite de l'auteur (DEC-026). Nouvelle version à relire, sans validation littéraire globale implicite. Sept sections et événements conservés ; journée suivant la chasse du chapitre 2, Hasol niveau 10 du début à la fin. Aucun gain d'XP, nouvelle élimination ou changement des dix runes personnelles. Les autres chapitres restent intacts.

**Direction éditoriale choisie par l'auteur :** théorie acquise mais assurance fragilisée, moins de reformulations et de bilans ; les gestes et le travail portent davantage le sens. La mère protège sans décider à sa place, Orven évalue méthode et consignes. Le premier salaire est la récompense propre à ce chapitre ; l'endurance magique et l'enseignement fixe/pourcentage restent au chapitre 4.

**Ouverture :** Hasol travaille les déplacements et la garde après les loups ; nouvelle épreuve avec le même guerrier ordinaire simulé niveau 10 et arrêt à la troisième touche reçue. Deux touches sont déjà reçues avant les derniers échanges ; le balayage au mollet constitue la troisième et entraîne la chute et l'arrêt à **1 minute 18 secondes**, contre 42 la veille (DEC-025 et DEC-026). Progrès technique montré par le recul et les appuis, sans victoire ni total de dégâts inventé. Griffure encore douloureuse, carnet technique bref et arrêt avant un nouvel essai.

**Économie :** une rune Fatal verte lui fait envie, mais son prix la dépasse ; développer la frustration matérielle et le coût des pierres de mana. Son rêve exige une source de revenus.

**Risque extérieur :** elle apprend l'existence des **Collines de Braise** et de gobelins rouges de **niveau 11** ; ce territoire est dangereux à ce stade. Ne pas l'envoyer les vaincre facilement : la tension vient de l'écart entre ambition et préparation.

**Rencontre Orven :** sa mère la présente à **Maître Orven**, marchand et spécialiste des runes depuis plus de 25 ans. Mentor compétent, prudent, pas admirateur aveugle. Il est surpris par les dix cercles mais ne quantifie pas encore le bonus d'échec de Hasol.

**Choix de la mère — DEC-026 :** elle attendait qu'Hasol soit prête à envisager l'artisanat sans abandonner son rêve de chasseuse ; la demande de financer ses propres améliorations ouvre cette possibilité. Elle refait le bandage et propose la rencontre, mais Hasol formule elle-même sa demande de travail. Passifs et dix cercles sont révélés une fois la porte de l'atelier fermée ; aucune statistique magique partagée à ce stade.

**Premier travail :** Orven lui confie l'amélioration de runes **blanches jusqu'à +3**. Première rune **ORV-R001, Énergie commune (blanche), 2★** : +1 réussite, +2 échec, nouvelle tentative +2 réussite, +3 réussite ; apparition d'une caractéristique secondaire de Défense à +3. **Règle résolue par DEC-006 :** une rune blanche native sans secondaire en gagne une à +3 et son grade affiché devient peu commun (vert) ; conserver son grade d’origine dans l’historique. La principale PV et la secondaire Défense restent non chiffrées. L’échec au passage +2 est une divergence préexistante du roman avec la source, distincte de l’adoption de la règle d’évolution des secondaires. Ressources fournies par l'atelier, rune jamais équipée par Hasol.

**Fin :** premier paiement et engagement à l'essai pour le lendemain ; fierté concrète, sans disparition immédiate du doute. Orven reconnaît le travail et exige le respect des commandes et des ressources, sans qualifier Hasol de prodige. Retour avec la mère puis préparation des affaires, mention « Pas encore » pour les collines et pièce laissée sur le chevet en raccord avec le chapitre 4. Ni nouveau dialogue avec le père ni réconciliation ; bilans répétitifs réduits.

**Vérification :** nom Orven ; aucune découverte des 30 % avant Ch7 ; échec au +2 ; coût des consommables ; récompense financière sans montant inventé.

## Chapitre 4 — « La voie de l'artisan » [ADAPTATION EN LECTURE — DEC-027]

**Provenance :** version initiale de `new.txt`, désignée comme validée par les consignes mobiles qui la suivent, importée par DEC-023. Après la refonte du chapitre 3, l'auteur autorise explicitement son adaptation (DEC-027). La nouvelle rédaction est à relire, sans validation littéraire implicite ni adoption automatique des consignes du chapitre 5.

**Période :** première journée complète à l'atelier, lendemain de l'épreuve du chapitre 3, puis début de la journée suivante. Dix sections, Hasol dix-neuf ans, niveau 10, dix emplacements occupés, équipement personnel inchangé.

**Apprentissage :** préparation et suivi des commandes, respect des budgets et ressources d'autrui. **CLI-R001, Gardien commune (blanche), 2★, +0 → +2** : un échec au premier passage +1 puis deux réussites, trois tentatives autorisées, rune rendue au client sans secondaire.

**Deux ressources — DEC-024, mise en pratique dans DEC-027 :** chaque tentative consomme pierres de mana et Mana personnel, succès ou échec. Hasol connaît cette dépense ; elle apprend à suivre sa réserve pendant une journée complète, pas à découvrir une règle élémentaire après trois ans de théorie. Difficulté selon étoiles, grade et palier ; aucune valeur définitive de coût ni table inventée. Le repos et les potions restaurent le Mana sans supprimer toute fatigue mentale.

**Principales fixes et pourcentages — DEC-011 complétée :** une scène centrale avec les exemples +50 Attaque et +10 % sur 200, 500 et 2000 naturels, sans les transformer en nouvelles runes d'inventaire. Assiette naturelle avant bonus fixes, mais ensembles et arrondis toujours ouverts. Valeur affective des cadeaux paternels évoquée par le souvenir du coffret unique, sans remplacement. La cliente met la méthode en pratique : profil et équipement à demander avant tout choix, pas de reprise intégrale du cours avec elle, la mère ou le carnet.

**Découverte émotionnelle :** Orven constate l'endurance de Hasol, Mana naturel 355 et bonus connu +20, réserve disponible non chiffrée. Son Mana trouve une utilité réelle, mais l'artisan lui fait arrêter le travail lorsqu'elle commence à mal lire une consigne. Ni maîtrise automatique, ni découverte des 30 %.

**Famille et fin :** mère attentive ; père affectueux mais absorbé par son travail, distance non résolue. Hasol poursuit son rêve de chasseuse tout en donnant une valeur propre au métier. Aucune nouvelle XP, compétence, élimination, amélioration personnelle ou rencontre de Yoon ; griffure refermée mais sensible.

**Direction de la révision — DEC-027 :** le premier salaire appartient au chapitre 3 ; ici, la progression repose sur la commande réellement rendue, le suivi d'une journée et les premières initiatives. Section VIII « Le travail du lendemain » : rémunération sans nouveau discours sur la valeur humaine, supervision maintenue. La mère écoute son expérience, le père ne la réconcilie pas avec lui, mais sa réaction ne décide plus seule de la satisfaction d'Hasol. Fin dominée par la fierté et l'autonomie : poste préparé, information manquante signalée, question apportée et comparaison commencée sous contrôle. Tous les événements et les dix sections sont conservés.

## Chapitre 5 — « Le premier lien » [PLAN VALIDÉ — DEC-045]

**Portée de la validation :** les deux chasses, la visite chez le forgeron et la fin Hasol 10→11 avec Aura runique sont désormais placées dans ce chapitre. L'ancienne fin au niveau 10 est abandonnée. Aucun texte du chapitre 5 n'est ajouté par cette décision. DEC-046 tranche les formes de Yoon : Résonance active ciblée, soin progressif en zone runique posée. Leurs paramètres restent **[À CONFIRMER]**, sans adoption automatique des chiffres ou des autres réponses de ChatGPT.

**Objectif :** introduire une coopération authentique et un danger qui force Hasol à admettre ses limites.

**Rencontres :** retrouver **Zio Notos**, classe rare Gardien, niveau 45, qui l'avait défendue à l'Académie. Introduire sa sœur **Yoon Notos**, 16 ans, **Sage runique rare**, niveau **5**.

**Découverte du pouvoir de Yoon :** présenter ses talents de soutien et les demandes de recrutement qu'elle reçoit. **Résonance runique**, active ciblée, amplifie temporairement les **caractéristiques principales des runes équipées sur la cible**, et rien d'autre. Son soin sur la durée, inférieur à une spécialisation de soins, est une zone posée en cercle d'écritures runiques. Montrer le besoin de placement et de protection sans l'immobiliser dans un chant continu ; paramètres chiffrés à définir. Les deux capacités sont utilisables lors de la rencontre niveau 5, mais leur niveau initial exact d'obtention reste à arbitrer.

**Chasse :** premiers combats en binôme, apprentissage du rythme et de la communication. Hasol protège Yoon et se fait **mordre au bras** ; la scène doit faire mal et rappeler le danger réel. Zio intervient et évite un pire résultat.

**Leçon de Zio :** « anticiper » au lieu de seulement « réagir » ; développer son conseil en dialogue et en observation tactique. Il ne résout pas les problèmes de Hasol à sa place.

**Arme de Terre et forgeron — [VALIDÉ, DEC-028 et DEC-045] :** l'arme de Zio conduit à une visite chez le forgeron ; il finance l'enchantement de Terre de l'arme d'Hasol. Le porteur doit être au minimum niveau 10 pour utiliser une arme imprégnée d'une aura. Hasol vient seulement d'atteindre ce seuil ; elle ne pouvait pas y recourir pendant ses années d'Académie, sans que cela signifie qu'elle ignorait cette technique. Ne pas inventer d'explication physiologique ni de conséquence d'un essai sous le seuil. Cette restriction ne concerne pas l'équipement des runes, toujours sans niveau minimum. Durée et paramètres non arbitrés de l'enchantement restent **[À CONFIRMER]**, pas automatiquement un mois.

**Secret :** Yoon et Zio découvrent les **dix cercles/emplacements** de Hasol et promettent de ne pas en parler. L'information reste limitée.

**Équipe :** Hasol et Yoon deviennent partenaires durables, **2/5 membres, 30/50 points**. Yoon étudie à l'Académie en semaine, chasse avec Hasol le week-end.

**Seconde chasse :** laisser à Hasol le temps de récupérer après la morsure avant la reprise ; ne pas imposer le lendemain. Le binôme apprend à anticiper ensemble, sans effacer la blessure par commodité.

**Fin [VALIDÉ — DEC-045] :** Hasol passe **10→11** et débloque **Aura runique** ; le niveau final de Yoon reste **[À CONFIRMER]**. Première confiance réciproque, mais limites et inquiétude persistantes. Les paramètres transmis dans `new.txt` — coût de 200 Mana, rune sacrifiée, durée de 24 heures, effet détaillé — ne sont pas adoptés par raccourci : ils restent à arbitrer. Ne pas tester immédiatement le pouvoir avec une rune équipée ni inventer d'autres chiffres.

## Chapitre 6 — « Deux chemins, un même objectif » [PLAN VALIDÉ — DEC-045]

**Provenance et raccord :** trame issue de l'ancien chapitre 5 d'`old.txt`, conservée dans ses journées de travail, d'étude et de coopération. Hasol a déjà atteint le niveau 11 au chapitre 5 : ne pas répéter 10→11, ni inventer un passage au niveau 12 pour compenser. Infiltration runique n'est pas validée par une réponse de ChatGPT.

**Concept :** alternance entre les deux vies : Hasol travaille chez Orven en semaine et s'entraîne à l'épée le soir ; Yoon étudie à l'Académie, s'entraîne et chasse dans son cadre scolaire.

**Progression de Yoon :** montrer ses cours, ses chasses et son travail personnel, ainsi que sa vie hors d'Hasol. Niveaux exacts après les deux chasses du chapitre 5 et gains suivants **[À CONFIRMER]**. L'exemple de deux niveaux pour Yoon contre un pour Hasol n'est pas une règle universelle ni une formule d'XP.

**Progression de Hasol :** amélioration de la précision, de la discipline, des réflexes et de la lecture des adversaires ; les revenus d'Orven servent à l'achat de ressources, pas à une montée instantanée de puissance.

**Aura runique :** expérimentation pendant l'entraînement, avec découverte critique d'une évolution du pouvoir ; mécanisme et paramètres encore ouverts à définir avant rédaction. Cette exploration ne remplace ni les journées parallèles des deux partenaires ni la coopération en chasse par un simple tutoriel d'Aura.

**Retrouvailles du week-end :** commencer par des **loups de niveau 5**, puis confronter le duo à des loups de **niveau 7, 8 et 9**. L'espace se resserre ; les personnages exploitent un **passage étroit** pour limiter les attaques simultanées.

**Tactique :** Yoon choisit quand cibler Hasol avec Résonance runique, active (DEC-046), et où poser sa zone de soin ; Hasol utilise placement, garde et épée pour abattre **trois loups** dans le passage. Éviter que le renforcement ou le soin règlent tout : coordination, limites de placement et fatigue restent perceptibles, sans paramètre numérique inventé.

**Résultat :** Hasol reste au niveau **11** en l'absence de nouvelle décision ; gains exacts et niveau final de Yoon **[À CONFIRMER]**. **Pas de blessure majeure**, dix cercles toujours. Aura runique est déjà débloquée, son expérimentation progresse ; aucun autre déblocage gratuit. Le duo gagne en assurance sans devenir invincible.

**Vérification :** suivre réellement les activités et l'XP de Yoon sans figer l'ancienne suite 5→7→8 ; ne pas attribuer à Résonance un effet sur secondaires/ensembles. Préserver le combat des loups de niveaux 7, 8 et 9 dans le passage étroit.

## Chapitre 7 — « Le talent d'une légende » [PLAN VALIDÉ — DEC-045 ; DÉCALAGE DEC-023]

**Motivation :** Hasol veut éviter de souffrir à chaque chasse et surtout ne plus mettre Yoon en danger. Elle comprend qu'elle doit améliorer significativement ses runes avant le samedi suivant.

**Provenance :** ancien chapitre 6 d'`old.txt`, à adapter aux décisions actuelles sans réimporter ses anciennes statistiques ni ses Lame.

**Observation d'Orven :** après une série suffisamment large d'améliorations, Orven compare ses résultats à ceux de Hasol. Il constate **30 % d'échecs en moins, relativement à son propre taux**. Il la qualifie de **prodige** ; la surprise est authentique et justifiée par son expérience de plus de 25 ans.

**Recommandation :** Orven la recommande à une grande guilde, **Griffon d'Argent**, qui a besoin de quelqu'un pour monter des runes jusqu'à **【 +6 】**. Enjeux : réputation d'Orven, regard sceptique des professionnels, prix des ressources, exigences de qualité.

**Semaine de travail :** scènes concrètes d'améliorations pour la guilde, succès et échecs, fatigue, gains financiers, achats de pierres de mana et amélioration des propres runes de Hasol. Garder un équilibre entre artisanat et entraînement.

**Équipement final du chapitre :** **10 runes équipées : 6 au niveau 【 +6 】 et 4 au niveau 【 +3 】**. Composition à conserver depuis l’inventaire actualisé du chapitre 2 selon DEC-013, sans réintroduire les deux Lame de l’ancienne version. Les deux cadeaux rares (bleus), 6★, déjà +6 comptent dans les six +6 : ne pas raconter leur première amélioration à ce niveau. Les huit autres runes sont les acquisitions maternelles 3★, sous réserve d’un remplacement explicitement autorisé et raconté. Les niveaux exacts par identifiant doivent être consignés dans `runes.md`.

**Niveaux personnages :** Hasol **11**, sauf nouvelle décision préalable ; niveau de Yoon **[À CONFIRMER]**. Pas de nouvelle compétence. La récompense est une montée en puissance runique, pas une montée de niveau arbitraire. La guilde constitue un débouché professionnel, pas une notoriété déjà équivalente à celle de ses vingt-cinq ans.

**Fin :** anticipation du samedi et du prochain défi commun.

## Chapitre 8 — « La puissance des dix runes » [PLAN VALIDÉ — DEC-045 ; DÉCALAGE DEC-023]

**Ouverture :** samedi au **Bois des Crocs Gris** ; Hasol et Yoon comparent leurs progrès depuis la première chasse. Les six runes +6 et les quatre +3 doivent produire une différence **visible** dans les gestes et les combats.

**Première série :** les loups auparavant dangereux sont maintenant mieux gérés ; montrer ce qui a changé (défense, force, préparation, timing, meilleure coopération), sans gommer le coût en mana de Yoon ni les limites de Hasol.

**Montée en tension :** indices d'un prédateur supérieur : traces, silence du bois, réactions des loups. L'arrivée du **loup alpha niveau 12** doit être préparée, pas surgir comme un boss arbitraire.

**Combat final :** l'alpha reste une menace ; Yoon place sa Résonance au bon moment, Hasol utilise les contraintes du terrain, garde ses appuis, bloque une attaque qui l'aurait auparavant blessée. Construire plusieurs échanges avec une adaptation tactique et des conséquences réelles.

**Climax émotionnel :** Hasol réalise qu'elle a réellement progressé et qu'elle peut désormais mieux protéger sa partenaire ; ne pas transformer cela en invulnérabilité ni en proclamation publique de son secret.

**Progression :** niveaux finaux et gains d'XP **[À CONFIRMER]**, depuis Hasol 11 et le niveau de Yoon encore à fixer. Ne pas imposer l'ancienne option 8 ou 9 pour Yoon ; si Hasol gagne un niveau, vérifier aussi l'XP de Yoon.

**Fin :** première grande victoire du duo, méritée, fatigue et confiance renouvelée ; premiers projets ambitieux et transition vers une progression sur plusieurs périodes. **Ray n'apparaît pas encore dans un sauvetage.**

## Chapitre 9 — « Douze cercles » [PLAN VALIDÉ — DEC-045]

**Durée et travail :** plusieurs périodes d'entraînement, de travail à l'atelier et de farm initial, pas une progression instantanée. Conserver le coût des ressources, la fatigue, la prudence, les changements de terrain et les inquiétudes de la mère et d'Orven. Hasol discipline ses suivis : XP, éliminations personnelles admissibles, pierres et runes sont distincts.

**Deux nouveaux cercles :** au moins **2 000 éliminations personnelles admissibles supplémentaires**, notamment en solo, permettent les deux nouveaux paliers **10→11→12 cercles/emplacements**. Préserver le reliquat historique inconnu sans le remettre arbitrairement à zéro ni recompter les huit paliers déjà récompensés. Les deux nouveaux emplacements reçoivent des runes **peu communes (vertes), rangs À DÉFINIR**, suivies par identifiants.

**Équipement avant Ray :** douze runes progressivement à **【 +6 】**, composition canonique **4 Fatal + 4 Vitesse + 2 Énergie + 2 Gardien**, soit les quatre ensembles actifs. Depuis les quatre Fatal, quatre Gardien et deux Énergie de DEC-020, acquérir quatre Vitesse, passer de quatre à deux Gardien et utiliser les deux nouveaux emplacements. Raretés et rangs des pièces non encore identifiées, remplacements, principales, secondaires et calendrier restent **[À CONFIRMER]** ; ne pas réintroduire des Lame ni prétendre remplacer des Lame inexistantes.

**Deux trajectoires :** montrer Yoon à l'Académie, ses choix, sa personnalité et sa vie hors d'Hasol, ainsi que leurs différences de rythme sans jalousie simpliste. Son passage au **niveau 20** et **Domaine des Entraves Runiques** doivent être montrés ou explicitement racontés avant son niveau 24 : ralentissement des ennemis dans le cercle lumineux, alliés épargnés, Mana consommé pour le maintien et résistance partielle des adversaires puissants.

**Situation finale :** Hasol **niveau 19**, Yoon **niveau 24**, avant le sauvetage. Hasol commence à privilégier le groupe plutôt que le farm intensif. Ne pas bloquer son niveau 19 jusqu'à un âge arbitraire ; dates et durée des périodes restent à construire.

## Chapitre 10 — « Ceux qui riaient autrefois » [PLAN VALIDÉ — DEC-045]

**Retrouvailles et danger :** Ray Corvus, **mage commun niveau 22**, et d'autres anciens de l'Académie reconnaissent Hasol et la sous-estiment. Un **loup alpha élite niveau 25 à 27** met leur groupe en danger. Hasol et Yoon choisissent de les sauver malgré le passé ; Yoon utilise Domaine des Entraves Runiques et Résonance, Hasol ses douze runes +6. Le danger, les blessures et les conséquences ne sont pas effacés par une démonstration triomphale ; pertes éventuelles **[À CONFIRMER]**.

**Révélation :** Hasol porte le **coup fatal**, passe **19→20** et débloque **Œil runique pour la première fois**. Ni elle, ni Yoon, ni Orven ne prédisent ce pouvoir. Surprise et expérimentation prudente : lecture des caractéristiques finales prédéterminées à +15, sans réussite garantie des améliorations.

**Butin conservé de l'ancien plan :** **rune Vitesse rare (bleue), 3★, +0**, principale **Vitesse**, secondaires **chance critique et dégâts critiques** ; valeurs exactes **[À CONFIRMER]**. Son rang vient du niveau du monstre ; ne pas la monter immédiatement à +15 par facilité.

**Dette puis coopération :** après avoir appris le sauvetage, la famille de Ray lui impose d'aider Hasol. Hasol et Yoon débattent des possibilités et des risques ; Hasol accepte pour accéder aux donjons, **minimum trois membres**. Trio **3/5, 35/50 points** : Hasol 20 + Yoon 10 + Ray 5. Forme précise de la pression familiale, réactions de l'Académie ou des guildes, témoignages et risque de révélation des cercles restent à construire ; la famille n'apprend pas automatiquement les secrets d'Hasol.

**Réparation en plusieurs scènes :** distinguer trois étapes, sans pardon instantané : aide d'abord contrainte, coopération éprouvée en mission, puis engagement personnel choisi au fil des chapitres suivants. Des excuses éventuelles ne rétablissent pas immédiatement la confiance. Spécialité magique de Ray et limites **[À CONFIRMER]**.

## Chapitre 11 — « Le dernier départ » [PLAN VALIDÉ — DEC-045]

**Le trio à l'épreuve :** premières expéditions difficiles, protection, contrôle runique et magie offensive doivent se coordonner. Le savoir livresque de Ray devient utile sans le rendre omniscient ni effacer son comportement passé. Début d'un engagement personnel au-delà de la dette ; coopération ne signifie pas confiance déjà acquise.

**Zio rejoint officiellement le groupe :** quatre membres, **4/5, 45/50 points**. Son rôle initial de superviseur extérieur est préservé. Missions et quotidien partagé ouvrent les premiers rapprochements avec Hasol, sans couple déjà établi ni mariage immédiat ; raisons et date exacte de son adhésion **[À CONFIRMER]**.

**Artisanat :** Œil runique donne ses premiers résultats économiques ; Orven reste mentor, pas distributeur de contrats. La pleine notoriété et les fonds colossaux de ses vingt-cinq ans ne sont pas encore acquis d'un seul coup.

**Départ du père et mort :** après un dernier échange difficile avec Hasol, son père part en voyage commercial lointain ; sa mort est annoncée, **sans véritable réconciliation**, avant la large reconnaissance artisanale de sa fille. Préserver l'affection sous les maladresses et plusieurs occasions manquées de dialogue ; pas de retour au contexte de raid. Date, destination, cause, contenu et intensité du dernier échange, modalités de l'annonce **[À CONFIRMER]**.

**Deuil :** plusieurs scènes, réactions propres à la mère et aux compagnons, conséquences durables. La mort du père n'est ni un simple obstacle à lever ni une douleur résolue par la prochaine réussite.

## Chapitre 12 — « La légende prend sa place » [PLAN VALIDÉ — DEC-045]

**La limite des quatre :** Hasol, Yoon, Ray et Zio affrontent un **boss de donjon niveau 32** qui invoque en masse des **monstres niveau 11** tant qu'un piège reste actif. Ils fuient. Zio, le plus expérimenté, propose de recruter une Ranger avant le retour. Le niveau 32 n'est pas attribué à Hasol ; ni invulnérabilité du boss, ni désactivation ou victoire automatiques ne sont ajoutées.

**Samia Claire :** Yoon présente son amie de l'Académie, une femme **Ranger commune**, cinq points, spécialisée dans l'archerie, la détection des pièges et l'ouverture des coffres. Même âge que Yoon, niveau légèrement inférieur au recrutement ; chiffres **[À CONFIRMER]**. Elle accepte dès qu'elle apprend la présence de Zio, beau, fort et populaire ; ses sentiments précis, son motif profond et une éventuelle connaissance antérieure restent à construire, sans rivalité amoureuse imposée. Groupe complet : **5/5, 50/50 points**.

**Retour au donjon :** seconde tentative à construire pour montrer l'utilité de Samia et la nouvelle coopération ; déroulement et issue **[À CONFIRMER]**, pas de victoire garantie par le seul recrutement. Piège, rythme des invocations, blessures, ressources et XP restent à établir avant tout calcul.

**Reconnaissance installée :** la réputation construite depuis les chapitres 10 et 11 s'affirme **vers vingt-cinq ans**, avant le chapitre 13. Grâce à Œil runique, Hasol est une artisane réputée et dispose de **fonds colossaux** pour financer ses runes jusqu'à +15. Montrer l'accumulation du travail, des résultats et des responsabilités, pas une richesse gagnée en un épisode. Inventaire exact, grades, rangs et calendrier des +15 **[À CONFIRMER]** ; les moyens de payer ne garantissent pas la réussite de toutes les améliorations.

**Rythme de progression :** Hasol privilégie désormais les donjons du groupe ; l'essentiel de l'XP vient des boss, mais peu de nouveaux cercles proviennent des mille monstres. Niveau à vingt-cinq ans et total de cercles **[À CONFIRMER]**. Ne pas convertir l'XP en multiples éliminations.

## Chapitre 13 — « Ce que nous construisons » [PLAN VALIDÉ — DEC-045]

**Des années vécues :** missions, vie ensemble et responsabilités artisanales ; la précarité des débuts n'est plus l'obstacle central. Argent et influence créent des choix, des attentes et des limites de disponibilité ; temps, Mana et fatigue demeurent. Développer les conséquences de l'ancien surnom et de la reconnaissance nouvelle.

**Relations réciproques :** Ray choisit son engagement au-delà de l'obligation familiale ; la réparation ne repose pas sur une seule scène. Yoon et Samia ont leurs aspirations et leur place propre. Hasol et Zio se rapprochent, construisent leur amour puis se marient ; calendrier, âges et étapes **[À CONFIRMER]**, aucun enfant imposé. Ne pas réduire Yoon à la sœur du mari ni Samia à une capacité utile.

**Transmission longue :** Hasol apprend auprès de Samia la détection des pièges et l'ouverture des coffres. Cet apprentissage conduit au **même Œil runique amélioré**, qui garde son nom et sa lecture des runes, et à **Main runique active** pour les coffres. Ni deux pouvoirs gratuits au recrutement ni désamorçage ou ouverture universels. Niveaux, étapes de déblocage, coûts, portée et limites **[À CONFIRMER]** ; aucun premier sort offensif avant le niveau 40.

## Chapitre 14 — « Le centième boss » [PLAN VALIDÉ — DEC-045]

**Jalon vers le niveau 38 :** Hasol achève personnellement son **centième boss de donjon**. Le combat peut se dérouler en groupe ; c'est son coup final qui compte, pas sa seule présence ou l'XP reçue. Le niveau 38 reste approximatif, pas un seuil minimum ajouté.

**Croissance runique évolue :** un cercle est accordé **immédiatement** pour les cent boss initiaux, puis un autre aux totaux 200, 300, etc., **quel que soit le niveau des boss**. L'ancien effet par mille monstres admissibles demeure. Un même boss avance les deux compteurs s'il satisfait aussi les conditions de l'ancien, en restant une seule élimination dans ce dernier. Conserver **deux compteurs distincts**, sans recompter les paliers déjà récompensés ni traduire un gros gain d'XP en multiples victimes.

**Conséquences :** total de cercles, équipement associé, rythme des prochains boss et ressources **[À CONFIRMER]** ; pas de grand total inventé ni de report automatique des compteurs au livre II. Les indices de menace mondiale se précisent sans révéler aux personnages l'apocalypse ou la rune temporelle.

## Chapitre 15 — « Enfin, la magie » [PLAN VALIDÉ — DEC-045]

**Niveau 40 :** Hasol obtient enfin son **premier sort offensif**, qui exploite pleinement son immense réserve de Mana. Éveil du pouvoir puis apprentissage : essais, limites, coûts et adaptation tactique, pas une maîtrise instantanée. Nom, effet, cibles, portée, durée, coût et récupération **[À CONFIRMER]** ; « pleinement » n'impose ni vidange automatique de la réserve ni formule Mana/dégâts. Ne pas le confondre avec Aura runique, une aura d'arme ou Main runique.

**Dernière campagne :** préparer la crise et les choix du groupe ; les alliés restent nécessaires malgré le nouveau sort. Conserver le lien avec l'artisanat, les responsabilités et la vie partagée : ce chapitre n'est pas un unique combat de démonstration. La puissance ne garantit pas de pouvoir protéger tout le monde.

## Chapitre 16 — « Celle qui demeure » [PLAN VALIDÉ — DEC-045]

**Catastrophe :** Hasol a **trente-quatre ans**, environ **niveau 45** ; **Yoon est niveau 54** (DEC-046). L'événement apocalyptique emporte Yoon, Ray et les proches concernés ; construire les pertes à partir des vies et des choix développés, pas par une liste expéditive. La situation précise de Samia reste **[À CONFIRMER]** dans le cadre où Hasol demeure seule survivante parmi les proches concernés, sans inventer une scène de mort individuelle.

**Ultime de Zio : AUTODESTRUCTION.** Zio, devenu le mari d'Hasol, déclenche une explosion qui **le tue et tue le démon stellaire**, permettant à Hasol de survivre. Ce n'est ni un simple épuisement ni une attaque dont l'issue pour le démon resterait indécise. Préserver ses motivations propres sans les réduire à son seul statut d'époux ; paramètres de l'ultime **[À CONFIRMER]**, sans restriction cosmique ajoutée.

**Fin du livre I :** Hasol récupère sur l'ennemi une **rune arcanique temporelle — rareté et rang en étoiles À DÉFINIR**. Son activation **ouvre le livre II**, elle n'est pas racontée ici. Le retour est de **trente-quatre à seize ans, soit dix-huit ans en arrière**, pas quinze. Aucune nouvelle régression ni explication cosmique n'est créée.

# 7. GARDE-FOUS TRANSVERSAUX DU LIVRE I

- **Durée :** les quinze années de dix-neuf à trente-quatre ans se répartissent en plusieurs périodes dans les chapitres 9 à 16 ; ne pas les réduire à une ellipse unique. Les dates intermédiaires restent à construire, en respectant réputation et richesse vers vingt-cinq ans avant le chapitre 13.
- **Provenance et remplacement :** les anciennes propositions après le chapitre 8 sont remplacées par l'unique séquence 9 à 16 ci-dessus. Leurs détails utiles sont redistribués, non maintenus comme un découpage concurrent. `old.txt` reste une source historique intacte, subordonnée aux décisions récentes ; les trames 5 à 8 gardent leur place. DEC-045 valide le cadre 1 à 16, pas les anciennes variantes numériques ou les paramètres laissés ouverts.
- **Famille et deuil :** préserver l'amour maladroit du père, le non-dit et les conséquences du décès au-delà du chapitre 11. Il connaît les débuts chez Orven, pas la pleine réussite publique de sa fille. La mère et chaque compagnon réagissent différemment.
- **Menace :** les modalités d'indices tels que déséquilibres magiques, raids plus fréquents ou monstres inhabituels restent des **[PROPOSITIONS]** de mise en scène. Ni origine de l'apocalypse ni rune temporelle ne doivent être expliquées prématurément.
- **Coopération :** Orven reste mentor ; Yoon, Ray, Zio et Samia ont leurs choix et leurs limites. Construire les missions, les responsabilités, les décisions éthiques et les pertes sur la durée. Richesse, niveau, rareté et nombre d'emplacements ne garantissent aucune victoire.
- **Séparation des vies :** le donjon invocateur prépare le réemploi voulu au livre II (DEC-040), sans télégraphier ce futur aux personnages du livre I. Les anciens passifs, dont Œil runique amélioré, sont accessibles au niveau 1 dans la seconde vie selon les règles à préciser ; Main runique est réapprise rapidement, pas transférée automatiquement avec toutes les actives. Aucun report des compteurs ou des cercles n'est fixé. Mariage et composition de la première vie ne sont pas imposés à la seconde.
- **Statuts :** aucun jalon futur n'est déjà survenu dans le manuscrit. La validation du plan ne valide pas littérairement les versions de lecture des chapitres 2 à 4, ne rouvre pas le chapitre 1 et n'autorise aucune rédaction nouvelle. Les livres II et III conservent leurs directions et propositions propres, sans plan de chapitres validé par DEC-045.

# 8. LIVRE II — DIRECTION CANONIQUE

## Prémisse [VALIDÉ]

- Hasol active la rune temporelle et revient **à 16 ans, juste avant la première Révélation**.
- Sa nouvelle classe est **Arcaniste Astral**, rareté **Astrale** (25 points d'équipe).
- La classe conserve un fonctionnement apparenté à l'Arcaniste runique, mais **tous les passifs acquis durant la première vie sont accessibles dès le niveau 1** ; leurs effets exacts dans la seconde vie restent **[À CONFIRMER]**.
- Hasol est **la seule à conserver des souvenirs** de la chronologie précédente : émotions vives, souvenirs importants, mais dates et détails secondaires parfois flous.
- Les autres personnages **n'ont aucun souvenir** de la première chronologie ; leurs **classes et personnalités sont mystérieusement différentes**. La cause reste **[À CONFIRMER]** et ne doit pas être résolue d'avance.
- **Autonomie d'exploration [VALIDÉ — DEC-037] :** l'amélioration d'Œil runique acquise en première vie relève du passif conservé, avec détection des pièges. Main runique, active, fait l'objet d'un réapprentissage rapide, pas d'un accès automatique au niveau 1. Prévoir ce réapprentissage avant les explorations qui reposeraient sur l'ouverture des coffres ; niveau et conditions à définir. La composition du livre II n'exige donc pas de Ranger pour ces fonctions, sans interdire ce rôle ni imposer la disparition du personnage.
- **Souvenir exploité [VALIDÉ — DEC-040] :** Hasol se souvient du donjon au boss niveau 32 et aux invocations niveau 11 maintenues par le piège (DEC-039). Dans sa seconde vie, elle l'utilise volontairement pour augmenter ses cercles par Croissance runique en laissant le mécanisme actif le temps de ses éliminations personnelles. Le niveau 11 a été choisi par l'auteur pour cet usage, pas seulement pour le combat du livre I. Avec les seuils déjà validés, ces monstres sont admissibles entre les niveaux 10 et 29 d'Hasol, pas dès le niveau 30 qui exige des monstres niveau 20+. Niveau exact de la scène, gains, nombre d'invocations, ressources et XP restent **[À CONFIRMER]**, sans accès solitaire implicite au donjon ni équivalence entre invocations et boss.

## Arcs possibles [PROPOSITIONS]

Les anciens essais de découpage du livre II et du livre III, proposés en douze unités avant la discussion d'un rythme à seize chapitres, sont conservés dans [`lore/pistes.md`](lore/pistes.md). Ils ne sont pas validés par DEC-045 et ne constituent pas un second plan canonique.

1. **La Révélation différente :** Hasol reconnaît le temple et ses parents, mais la stèle révèle l'Arcaniste Astral. Le choc émotionnel prime sur la démonstration de puissance. Son père vivant la bouleverse.
2. **Les visages familiers, les inconnus :** retrouvailles avec Yoon, Zio, Ray et Orven ; leurs différences empêchent Hasol de « rejouer » mécaniquement le passé. Elle doit apprendre à les connaître de nouveau.
3. **L'avantage et son prix :** passifs accessibles tôt, mais limitations matérielles, XP et connaissances incomplètes ; Hasol peut anticiper certaines catastrophes, pas contrôler toutes les variables.
4. **Les choix qui changent le monde :** chaque intervention modifie les trajectoires ; interroger ce que signifie sauver des proches devenus différents.
5. **L'énigme des classes altérées :** indices graduels sur les différences entre chronologies ; ne pas imposer de solution sans décision de l'auteur.
6. **Le démon et le temps :** réexaminer l'apocalypse et la rune temporelle ; enjeux personnels et cosmiques réunis.
7. **Exploitation du donjon connu — intention validée DEC-040, scène à construire :** transformer le souvenir d'une retraite de la première vie en préparation d'une progression choisie. Hasol garde délibérément le piège actif pour les invocations, avec une équipe répondant aux conditions d'accès. Ce souvenir précis reste compatible avec une mémoire globalement imparfaite ; ne pas en déduire la connaissance infaillible de tous les donjons.

# 8 bis. LIVRE III — DERNIER LIVRE DE LA TRILOGIE

- **[VALIDÉ — DEC-030] :** un troisième livre est prévu et constitue le dernier tome.
- **[À CONFIRMER] :** titre, période, intrigue propre, articulation avec la fin du livre II, résolution des mystères et sort final des personnages.
- Cette décision ne déplace pas automatiquement les événements établis des livres I et II. Elle n'établit ni nouveau retour temporel, ni troisième chronologie, ni nouvelle classe, ni fin heureuse ou tragique.
- Toute répartition détaillée entre les livres II et III reste une **[PROPOSITION]** tant que l'auteur ne l'a pas choisie.

# 9. Questions ouvertes à trancher avant rédaction définitive

1. **Point résolu le 19 novembre 2026 — cadeaux initiaux :** deux runes bleues 6★ +6, principales Attaque +70 et Défense +70 ; deux secondaires renforcées chacune, valeurs et historique dans `lore/runes.md`. Voir DEC-001, DEC-005 et la correction prioritaire DEC-006 dans `lore/decisions.md`.
2. **Règle d’amélioration résolue par DEC-006 puis DEC-014 :** principale augmentée à chaque niveau, plus fortement à +15 ; secondaire ajoutée ou renforcée à +3, +6, +9, +12 et +15, avec un maximum de quatre. À +15, renforcer une des quatre secondaires présentes. Les gains numériques des secondaires restent à définir en dehors des deux cadeaux déjà documentés.
3. **Règles d'arrondi et ordre de calcul des bonus d'ensemble**, ainsi que le traitement des PV maximums lors d'un changement d'équipement.
4. **Répartition précise des six runes +6 et quatre runes +3 à la fin du chapitre 7**, avec identifiants persistants.
5. **Niveaux exacts de Yoon après les chasses du chapitre 5 et aux chapitres 6 à 8 ; gains et niveaux finaux du chapitre 8.** Hasol 10→11 et Aura runique en fin de chapitre 5 sont résolus par DEC-045 : ne pas répéter ce passage au chapitre 6. Résonance active ciblée et soin en zone posée, Domaine au niveau 20 et Yoon 54 au chapitre 16 sont fixés par DEC-046. Leurs paramètres numériques, les niveaux d'obtention initiaux, les compétences après le niveau 20, ainsi que les paramètres d'Aura et de son évolution restent à arbitrer ; aucun coût de 200 Mana ou effet de 24 heures n'est adopté par défaut.
6. **Identités, rangs et valeurs des nouvelles runes du chapitre 9**, calendrier des 2 000 éliminations personnelles admissibles et reliquat historique. La composition douze runes +6 est fixée : quatre Fatal, quatre Vitesse, deux Énergie, deux Gardien. Documenter le passage de quatre à deux Gardien et l'acquisition de quatre Vitesse avec deux nouveaux emplacements ; aucun remplacement de Lame. Valeurs exactes de la Vitesse rare (bleue), 3★, +0 du chapitre 10 encore à confirmer.
7. **Spécialité magique de Ray** et niveau lors de son apparition au chapitre 1. Son rôle antérieur est désormais fixé par DEC-021 : ami d'enfance devenu complice des humiliations, sans excuses abouties lors de l'intervention de Zio.
8. **Échelle et règles des pierres de mana, prix et récompenses**, si l'auteur souhaite des montants numériques réguliers.
9. **Chronologie détaillée des quinze années** du livre I et dates des scènes. Les placements sont résolus par DEC-045 : mort du père et adhésion de Zio au chapitre 11, Samia et réputation installée vers vingt-cinq ans au 12, mariage et transmission au 13, centième boss au 14, premier sort offensif au 15, catastrophe au 16. Restent notamment les circonstances du décès, la durée du deuil, les étapes sentimentales, le calendrier exact des apprentissages et leur mécanique, l'issue du retour au donjon, les inventaires futurs et le sort individuel de Samia dans la catastrophe.
10. **Mécanique exacte des passifs de la classe astrale** et origine des changements de la seconde chronologie.
11. **Coûts personnels en Mana des améliorations**, récupération et fatigue : règles qualitatives établies au chapitre 4, barèmes et grade de référence pour le coût à définir. La principale en pourcentage utilise désormais la statistique naturelle ; cela ne résout pas le calcul des ensembles et arrondis.
12. **Proposition de coefficients d'XP et courbe de référence**, conservée avec son statut non adopté dans `lore/pistes.md`. Ne pas appliquer un barème ni l'ajouter au récit avant arbitrage ; l'auteur ne souhaite pas d'exposition détaillée de l'XP dans le roman.

# 10. Structure de dépôt recommandée

```text
Les-Chroniques-de-l-Arcaniste-Runique/
├── roman.md                  # Unique manuscrit, tous les chapitres
├── style.css                 # Affichage HTML dans VS Code / site
├── AGENTS.md                 # Consignes d'écriture et de maintenance Codex
├── PLAN_DIRECTEUR.md         # Ce document
├── .vscode/
│   └── settings.json
└── lore/
    ├── personnages.md        # États des personnages + historique par chapitre
    ├── runes.md              # Inventaire runique par ID, grade, affixes, améliorations
    ├── systeme.md            # Règles canoniques du LitRPG
    ├── chronologie.md        # Âges, périodes, événements, spoilers
    └── questions_ouvertes.md # Points non validés
```

## Format conseillé pour `runes.md`

Pour chaque rune, consigner : ID stable (ex. `HAS-R001`), propriétaire, état équipée/inventaire, ensemble, grade, rang de 1 à 6 étoiles, niveau d'amélioration, principale et valeur, chaque secondaire et valeur, date/chapitre d'acquisition, date/chapitre des améliorations, éventuel remplacement. Ne jamais remplacer les caractéristiques d'une rune existante sans événement narratif explicite.

## Format conseillé pour `personnages.md`

Pour chaque personnage : âge à la date du chapitre, classe/rareté, niveau, XP connue, stats naturelles, compétences et déblocages, cercles/emplacements, IDs des runes équipées, buffs temporaires distincts, blessures, relations, informations connues et inconnues. Conserver un historique des modifications par chapitre, pas seulement l'état actuel.

# 11. Consignes de fonctionnement pour Codex

1. **Avant un chapitre :** lire `AGENTS.md`, `PLAN_DIRECTEUR.md`, `lore/systeme.md`, `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md` et les chapitres précédents pertinents dans `roman.md`.
2. **Proposer une fiche de chapitre** (date/période, protagonistes, niveau initial/final, runes, événements, scènes, enjeux, continuité) ; ne pas modifier le canon sans accord.
3. **Rédiger un chapitre long et immersif** : scènes vécues, descriptions sensorielles utiles, émotions crédibles, dialogues et tactique claire. Éviter les résumés déguisés en chapitres.
4. **Conserver le manuscrit dans un seul `roman.md`** ; ajouter les nouveaux chapitres à la suite avec titres Markdown et séparateurs `---`.
5. **Fenêtres de système en HTML** compatibles avec les classes CSS existantes ; stat naturelle en texte normal, bonus runique bleu, buff temporaire vert, badges d'amélioration visibles.
6. **Contrôler la logique :** XP et niveaux, 50 points / 5 membres, cercles, nombres de runes, secondaires par grade, ensembles, coût et échecs d'amélioration, blessures et guérison, jours d'Académie de Yoon, secrets connus par chaque personnage.
7. **Après validation du chapitre :** mettre à jour `personnages.md`, `runes.md`, `chronologie.md` et éventuellement `systeme.md` ; consigner les changements et les points en suspens.
8. **Ne pas écrire les révélations futures dans les dialogues ou pensées des personnages** tant qu'ils n'ont aucune raison de les connaître. La bible contient des spoilers réservés à l'auteur et à Codex.
9. **Ne pas confondre proposé et validé.** Demander l'arbitrage de l'auteur sur toute contradiction ou information canonique manquante qui influe matériellement sur le chapitre.
10. **Respecter le plan canonique des seize chapitres du livre I — DEC-045**, leurs titres, leur ordre et leurs jalons, en distinguant les paramètres encore ouverts. Préserver les statuts littéraires propres des textes 1 à 4 ; la validation du plan n'autorise ni leur réécriture ni la rédaction d'un nouveau chapitre. Les corrections de systèmes et de caractéristiques ne sont pas une permission de changer les relations ou l'ordre des événements. Aucun découpage des livres II et III n'est validé par extension.

# 12. Prompt de démarrage Codex (à copier)

> Tu travailles sur le roman français LitRPG « Les Chroniques de l'Arcaniste Runique ». Commence par lire intégralement `AGENTS.md`, `PLAN_DIRECTEUR.md`, `roman.md` et les fichiers `lore/`. Distingue strictement les éléments [VALIDÉ], [À CONFIRMER] et [PROPOSITION]. Ne modifie pas encore le manuscrit. Le plan du livre I compte seize chapitres dont les titres, la séquence et les jalons sont validés par DEC-045 ; cela ne valide aucun découpage des livres II et III, ni les paramètres encore ouverts. Le chapitre 1 révisé est validé (DEC-022) ; les chapitres 2 à 4 sont présents avec leurs statuts littéraires distincts et ne reçoivent aucune nouvelle validation implicite. Ne les réécris pas et ne réimporte pas les textes de `new.txt`. Prépare d'abord la continuité du prochain chapitre autorisé et la liste courte des arbitrages nécessaires. Hasol 10→11 et Aura runique sont placées à la fin du chapitre 5 ; ne pas répéter ce passage au chapitre 6. Les paramètres d'Aura et les niveaux intermédiaires de Yoon restent à établir. La validation du plan n'autorise pas à rédiger : attends mon accord explicite pour le chapitre concerné, puis respecte la séquence canonique 1 à 16, avec une prose longue, immersive, des statistiques établies et des fenêtres HTML stylées, avant de synchroniser les références.

---

**Principe de transmission :** ce document est une bible de continuité et un plan de production, pas un substitut au texte validé des chapitres. Les scènes approuvées ont priorité sur toute proposition nouvelle.
