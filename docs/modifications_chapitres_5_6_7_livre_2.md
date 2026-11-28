# Livre II — Intégration des chapitres 4 à 7 et journal des adaptations

## Bilan final des contrôles

- **112 tests réussis** après adaptation bornée des tests historiques et ajout de contrôles des chapitres 4–7. Les anciennes empreintes de référence restent conservées. Journal de session : `/tmp/opencode/arcaniste-integration-20261128/tests-finalises.log`.
- Fenêtres contrôlées par `--check` : livre I **153 fenêtres / 306 SVG à jour** ; livre II **36 fenêtres / 72 SVG à jour**. Le lecteur historique `lecture.html` est à jour ; aucun second manuscrit du II créé.
- Empreintes pré-intervention vérifiées : **quatre conversations et livre I intacts**, y compris la modification de conversation présente à l'ouverture. Corps des chapitres 1–3 du II préservé ; sommaire complété.
- Contrôles de passivité renforcés pour les deux livres et leurs SVG, notamment ressources distantes dans les images Markdown et listes `srcset`, contenu actif et `foreignObject`. Ce n'est pas un audit de sécurité exhaustif.
- Relecture indépendante effectuée : ancienne réserve Ray explicitée, puis levée par l’arbitrage local DEC-214 (Mage de feu Commun aux 6–7, sans nouveau placement futur) ; proche de Carmela neutralisé, statut documentaire du chapitre 5 précisé.
- **Limites :** navigateur déconnecté, donc pas de nouvelle validation visuelle ; fiches de runes encore incomplètes et raccords futurs signalés dans ce journal. Les adaptations attendent la relecture de l'auteur. Un passage QA final supplémentaire a été interrompu : il n'est pas revendiqué comme achevé ; les tests et la revue indépendante sont les preuves disponibles.
- Aucun commit, push, publication ou déploiement réalisé.

## Périmètre et statut

Intégration locale sur le GO transmis par l'auteur : chapitres 5, 6 et 7 validés, correction des incohérences autorisée à condition de tout journaliser. Le chapitre 4 validé mais absent est intégré pour obtenir une lecture continue **1–7**. Aucun chapitre 8 rédigé ou intégré ; archives intactes, aucun commit/push ou publication.

**Les chapitres 4, 6 et 7 disposent d'une validation mobile retrouvée. Pour le chapitre 5, aucune validation mobile autonome n'a été retrouvée ; le GO local de l'utilisateur désigne explicitement les chapitres 5/6/7 comme validés et autorise leur intégration. Les versions adaptées présentes dans le manuscrit sont À REVALIDER**, particulièrement les raccords narratifs identifiés ci-dessous. Ce journal ne transforme pas une correction technique en validation littéraire. La synchronisation du lore et la génération des dérivés sont des lots distincts, confiés aux autres intervenants.

Les deux guides `AGENTS.md` (projet et configuration OpenCode), dont la section `Agent: integration`, ont été lus. La conversation `docs/conversation/28_11_2026.txt` a été lue **intégralement, lignes 1–17431**, par plages successives sans lacune. Le plan directeur a été lu intégralement ; les références système, personnages, runes, chronologie, décisions, sources et guides de fenêtres ont été consultées sur les champs concernés. Les anciennes grilles ne priment pas les dernières versions validées.

## 1. Versions réellement retenues

Tous les repères ci-dessous concernent `docs/conversation/28_11_2026.txt`. Ils désignent des lignes de l'archive reçue, pas celles du manuscrit après génération.

| Chapitre | Version retenue et raccords | Validation et exclusion des variantes |
|---|---|---|
| 4 — Cette fois, avec moi | I–XI : 2662–4286 ; XII remplacée par la nouvelle fin 4803–5115, sans son instruction éditoriale d'ouverture | « validé » à 4298 ; remplacement de fin demandé par l'auteur puis confirmé à 6407–6410 ; corrections Aura/Siphon 6357–6406. Ancienne XII hésitante et première rédaction 601–2409 exclues. |
| 5 — Le village sur la carte | Dernière version complète 6412–7624 ; scène de l'Académie remplacée par 7647–7731 ; témoignage du cousin raccordé au rêve du 6 | Aucune validation mobile autonome retrouvée ; le GO local de l'utilisateur dit explicitement 5/6/7 validés et autorise l'intégration. La première version 5117–6333, avec les explosions erronées d'Aura, n'est pas importée. La demande directe d'ajout de Zio et le rêve imposé par l'auteur complètent la version complète. |
| 6 — Préparer une place pour les vivants | 9498–10816, treize sections | « Je valide » à 10828 ; première version 8049–9309 exclue. Automatismes au front Hasol/Zio et réplique indirecte de Zio conservés dans la dernière rédaction. |
| 7 — Le poids du sang | 13941–15839, seize sections | « Je valide, riche en émotion » à 15854 ; première version 11684–13454 et plans proposant un mariage réussi exclus. La scène Samia est XIV, avant le décès d'Orven et les sons finaux, conformément à la dernière version validée. |

Les notes de ChatGPT, tableaux de propositions, invitations à poursuivre, commentaires hors manuscrit, compteurs de visions et explications des secrets d'auteur ne sont pas importés. Les décisions futures évoquées après le chapitre 7 ne constituent pas un chapitre 8 autorisé. L'archive comporte « un homme » pour le proche de Carmela ; cette précision est neutralisée en « un proche » conformément à DEC-193, sans fixer sexe, nom, identité ou fonction.

## 2. Préservation des chapitres 1–3

- Le sommaire est complété avec les quatre nouvelles entrées et les ancres `chapitre-4` à `chapitre-7`.
- **Aucun octet du corps des chapitres 1–3 n'est réécrit.** La comparaison couvre le segment allant de `<span id="chapitre-1">` à la fin du chapitre 3, en conservant sa fin de ligne d'origine.
- SHA-256 de ce segment préservé : `71132c89edef9f1657ab5ba990915a47dc1532d8b1e475bb2a03cbaf4c292dfc`.
- Les 26 fenêtres et leurs identifiants antérieurs restent inchangés à cette étape. Le générateur peut ensuite réécrire ses seules enveloppes selon son contrat habituel.

## 3. Corrections narratives et raccords — À REVALIDER

Les emplacements sont donnés par chapitre/section et phrase recherchable, afin de rester utilisables après génération.

| Emplacement | Avant, dans la version mobile | Après, dans le manuscrit | Raison et source |
|---|---|---|---|
| 4 I, vision du loup | « L'explosion de mana frappa violemment la créature. » après Aura | La rune se désagrège ; une aura de Terre enveloppe l'épée. Le critique puis les deux frappes et la croix rouge sont conservés. | Correction directe de l'auteur après le premier 5, 6357–6406 ; Aura ne fait pas de dégâts de zone. Critique au lancement, pas critique d'épée : DEC-075, système § Aura/Infiltration et chapitre 3 XVI. Aucune valeur de dégâts ajoutée. |
| 4 II, ellipse avant le niveau 40 | Aura qualifiée d'arme principale et surnom associé aux « explosions de mana » | Aura est un atout d'imprégnation ; Hasol abat les groupes à l'épée imprégnée. | Même correction Aura/Siphon. **Siphon n'est pas substitué avant son acquisition au 40** ; aucun sort précoce ajouté. |
| 4 XI, Mur de flammes | « Pour Aura runique ? », puis Aura provoque une explosion | « Pour Siphon runique ? » ; onde de vent frappant les démons regroupés autour d'Hasol ; résultat observé par Ray | Substitution explicitement proposée puis retenue à 6385–6410. Les flammes de Ray ne sont pas dissipées par un pouvoir inventé de Siphon : l'ancienne phrase « Lorsque les flammes se dissipèrent » devient simplement l'observation du résultat. |
| 4 XI, combinaison après Déflagration | « combiner Déflagration avec Aura runique » | « combiner Déflagration avec Siphon runique » | Même correction directe. Pas de fusion de sorts ni de multiplicateur nouveau. |
| 4 XI, quatre Fatal | Quatre nouvelles Fatal complètent l'équipement au bilan des 36 cercles ; préparation non exprimée | Phrase précisant les pièces préparées en réserve, équipées au fil des nouveaux cercles, avant le même bilan de quatre Fatal supplémentaires | Raccord DEC-175/176/177 : préparer les cercles attendus. Ne chiffre ni paliers intermédiaires, ni dates, ni achats nouveaux ; 32 → 36 et dix activations inchangés. |
| 5 VIII, arrivée devant l'Académie | Version complète sans Zio | Remplacement par le passage ultérieur : directeur ayant appelé Zio, joie de Yoon, Hasol recouvrant machinalement sa bague | Demande directe de l'auteur, 7641–7735. Aucun personnage ne commente le geste ; aucune pensée explicative ou romance acquise n'est ajoutée. |
| 5 X, combat et retour | Zio absent du combat malgré son ajout à l'arrivée | Zio tient les démons à distance avec son bouclier pendant Fournaise, puis rejoint sa sœur après la victoire | Raccord annoncé dans la réponse 7735 : Zio participe aussi au combat. Hasol attend toujours l'extinction du feu avant de s'élancer. Aucune nouvelle compétence, valeur ou issue. |
| 5 XII, témoignage du cousin | « Samia m'avait promis de m'apprendre à tirer à l'arc… » ; sacrifice raconté seulement par sa mère | Ajout « Samia est restée derrière pour nous laisser le temps de fuir… », puis la promesse d'apprendre l'arc | L'auteur impose ce témoignage dans la vision du 6, 7736–7877. La dernière rédaction du 6 demande expressément d'harmoniser la source du rêve ; le garçon entend et connaît ce qui s'est passé, sans savoir magique ajouté. |
| 6 VI, Rempart de lumière | Protection directionnelle maintenue, puis Zio semble avancer sans transition | Zio laisse retomber sa protection avant de reprendre sa progression avec Hasol | DEC-058 : effet directionnel avec maintien de position. Clarification de séquence, sans coût ni durée inventés. |
| 6 VII, Déflagration sur le boss | Hasol recule mais Zio entraîne le boss dans la direction opposée, sans sortie claire de la zone de feu | Hasol recule, Zio s'écarte à son tour pour dégager la ligne de tir | DEC-069/070 et système de Ray : ses flammes menacent ses alliés ; aucune immunité automatique. Les mêmes attaques et la même victoire sont conservées. |
| 7 I, rêve de Carmela | « Un homme vint la rejoindre, un document à la main. » (archive 13983) | « Un proche vint la rejoindre, un document à la main. » | DEC-193 et rappel prioritaire DEC-206/AGENTS : le proche n'a ni sexe, ni identité, ni fonction fixés. Neutralisation ciblée confirmée par les relais décisions et lore ; remise du rapport et prénom entendu inchangés. |
| 7 III, piste Astrea | Hasol se souvient d'un mot prononcé par Iseria à ses seize ans, lors de la découverte de sa classe | Hasol relit « Carmela A. » et demande si l'initiale aide ; Ray consulte son livre et propose Astrea | Le souvenir ciblé correspond à l'épilogue du I, absent de sa mémoire consciente à ce stade ; aucune réplique équivalente n'est racontée dans les chapitres 1–3 du II. DEC-131/132/197 et absence d'omniscience. La piste vient du document déjà trouvé et de la recherche explicitement en cours, sans ajouter une phrase maternelle rétroactive. Même portrait, identification, hypothèse puis confirmation de parenté. |
| 4 IX, classe dans le bilan du raid ; 7 V, déclaration à Carmela | « Arcaniste runique » comme nom de la classe actuelle d'Hasol | **Arcaniste Astral**, rang astral inchangé | Intitulé déjà révélé au chapitre 1 du II, fenêtre `L2-C1-F01`, et cadre DEC-078. Ce n'est pas une évolution de classe en cours de chapitre. |

### Changements de trajectoire validés dans la source, pas corrections inventées

- **4 XII :** fiançailles et Anneau runique dès la nouvelle fin, pas une réponse encore suspendue au 5.
- **5 :** Samia meurt en protégeant l'évacuation ; sa famille est sauvée. Le portail de l'Académie est fermé ; Ray, Yoon et Zio survivent.
- **6 — raccord résolu par DEC-214 :** réveil la nuit avant la séparation, après la Révélation de Ray. L’auteur confirme localement qu’il n’a pas changé de classe : **Mage de feu Commun, cinq points**, conservé en vie 4 et dans la continuité du 7. L’ancienne réserve DEC-205 est levée ; le placement rare dès vie 4 est remplacé, sans nouvelle vie/date fixée pour le futur Stratège. Les trois chasseurs du raid de l’Académie représentent **35 points**, les cinq héros réunis au village **65 points de raid**, admissibles dans un **raid de 100 points**, pas dans un groupe permanent de 50. Les autres chasseurs restent non chiffrés ; aucun effectif total inventé. Mise à jour documentaire seulement, aucune retouche du manuscrit par DEC-214.
- **6 fin :** le retour survient à l'annonce de la condamnation d'Iseria et à son enlèvement, pas après une exécution racontée. Douze DONG, quatre DING.
- **7 :** Iseria est sauvée, **mariage interdit et fiançailles rompues**. Hasol garde la bague ; Ray apprend les cauchemars, pas le mécanisme des runes. Carmela confirme sa parenté. Ni Ténébria, ni carnets de grossesse découverts.
- **7 fin :** visite anodine de Zéphyr conservée en XIII, échange avec Samia en XIV ; Orven meurt en XV puis entretien sur l'infusion en XVI, douze DONG/cinq DING. L'infusion préventive suffisante est une décision directe de cet apport, pas une règle universelle de guérison ni une résurrection.

## 4. Présentation uniquement

- Titres harmonisés avec le manuscrit : `## Chapitre N — Titre`, sections `### I. …`, ancres stables et séparateurs `---`.
- Les répétitions de titre « Livre II — Chapitre N », les marques de clôture hétérogènes et les instructions de remplacement sont normalisées sans inclure les notes de conversation.
- La feuille de calcul du **4 V** reste une **table Markdown d'ensembles**, avec 32 pièces/neuf activations et le projet de quatre Fatal, pas une notification magique ou une acquisition déjà réalisée.
- Le document **Autorisation permanente** du **7 II** reste une **citation Markdown**. Ce papier portant une signature et un sceau n'est pas transformé en fenêtre du Système ni en illustration narrative.
- Les véritables présentations système sont converties en HTML source : fond, couleurs, bulles et comportement responsive viennent exclusivement du CSS/générateur existant, aucun style global ajouté.
- Les classes du raid utilisent les bulles de nom, palette de classe correcte, `data-rarity`, titre explicite et complément textuel `.lit-sr-only`, lisible sans couleur. Samia reste commune/blanche. Pas de fiche d'Iseria ou révélation de Prophète au II.
- Aucune image distante, police, script ou ressource réseau ajoutée. Aucun SVG généré par ce lot.

## 5. Fenêtres ajoutées et relais technique

**10 nouvelles sources HTML**, soit **36 fenêtres au total**. Initialement livrées nues par ce lot d'intégration, elles ont depuis reçu leurs enveloppes GitHub et variantes SVG via le relais technique ; les tests et le contrôle du rendu sont encore en cours à cette mise à jour.

| ID invisible | Contenu | Type |
|---|---|---|
| `L2-C4-F01` | Coup critique / Infiltration dans la vision du loup, sans durée supplémentaire inventée | activation |
| `L2-C4-F02` | Niveau 40 et Siphon : 120 % PA, 75 %, 8 m, 20 s, 100 Mana, plafond 1 200 | compétence |
| `L2-C4-F03` | Raid 100/100, 13 chasseurs ; 25+20+5+5+45 | groupe |
| `L2-C4-F04` | Mur de flammes au 30 et danger pour les alliés | compétence |
| `L2-C4-F05` | Déflagration et Combustion maîtrisée au 40 | compétence |
| `L2-C4-F06` | Bilan agrégé 36/36 et dix activations, sans fiche individuelle fictive | équipement |
| `L2-C4-F07` | Fournaise au 50, concentration et Mana continu | compétence |
| `L2-C4-F08` | Anneau : accessoire à inventaire exclusivement runique | équipement |
| `L2-C5-F01` | Aimant acquis après le combat avec l'anneau ; seule amélioration des chances affichée | compétence |
| `L2-C5-F02` | Portail bleu : démons 30, boss 50, capacité 100 points, 48 heures | portail |

Le relais technique confirme la génération des **20 nouveaux SVG** sous `assets/fenetres-livre-2/`, soit **72 SVG pour 36 fenêtres**. Les contrôles automatisés et du rendu restent en cours ; aucune nouvelle génération n'est effectuée pour la neutralisation du proche, située hors fenêtre. Les sources utilisent `data-window-id` ; les identifiants ne sont pas du texte destiné au lecteur.

### Réserves sur les fiches individuelles — pas de fausse complétude

Les nouveaux chapitres ne fixent pas les fiches individuelles des 32/36 pierres de la vie 3, ni les grades/étoiles/affixes des deux Gardien examinées au 7 XIII. **Aucune fiche de la vie 2 n'est copiée entre vies.** Le bilan de 36 est un décompte d'ensembles ; le projet Attaque/PA n'est pas converti en valeurs effectivement obtenues.

Le relais lore a réservé des IDs temporels propres dans `lore/runes.md`, notamment les quatre Fatal `L2-V3-HAS-R033` à `036` et les candidates d'atelier `L2-V5-ORV-R001/002`, avec les valeurs absentes à définir. Ce sont des limites réelles : **les présentations détaillées de ces exemplaires restent à compléter** si elles sont souhaitées ou exigées avant livraison définitive. La prose mobile de la comparaison artisanale est conservée sans fabriquer des chiffres ni livrer deux fiches chiffrées inventées. La synchronisation des références n'est pas une preuve de complétude des données manquantes.

## 6. Contrôles réalisés dans ce lot

- Extraction structurelle avec `Reperes` du générateur, sans génération : **36 racines HTML valides, IDs uniques, pas d'imbrication de fenêtres**.
- Structure des chapitres 4/5/6/7 : **12 / 13 / 13 / 16 sections** ; aucune section littéraire perdue dans les conversions.
- Sons vérifiés : chapitre 4, aucun retour ; chapitre 5, **12 DONG/3 DING** ; chapitre 6, **12/4** ; chapitre 7, **12/5**.
- Comparaison du corps des chapitres 1–3 : identique, empreinte ci-dessus.
- Recherche dans les quatre chapitres ajoutés : aucune note hors manuscrit, URL distante, explication de Rune de Vision, Prophète, Mémoire parfaite ou Stratège runique importée.
- La validation graphique bureau/mobile, les tests automatisés complets et la vérification des dérivés **restent au relais technique**. Aucun résultat de rendu navigateur ou conformité RGAA n'est revendiqué ici.

## 7. Points de vigilance restants

1. Revalidation littéraire des adaptations du tableau §3, en particulier la piste Astrea sans souvenir du I, les raccords de combat, le témoignage du cousin et l'intitulé de classe.
2. Présentations individuelles de runes incomplètes : conserver les réserves explicites, ne pas annoncer une conformité exhaustive DEC-179 tant qu'elles ne sont pas complétées dans le périmètre autorisé.
3. Les nouveaux points de sauvegarde sont relatifs ; aucun âge, niveau ou inventaire chiffré de l'ancienne grille ne doit leur être appliqué par défaut. Ne pas figer l'équipement à 36 après les années d'ellipses du 5.
4. Les nouveaux fragments oniriques gardent leur mystère ; aucune connaissance générale des secrets de Vision/Notos/Shun n'est acquise par les personnages. Le modèle historique de comptage ne doit pas réapparaître dans une fenêtre.
5. Les révélations ultérieures sur Zéphyr, l'âme, le bébé et Héritage runique restent documentaires, hors des chapitres 4–7. Le chapitre 8 reste à construire.
6. Enveloppes et SVG générés par le relais technique ; terminer les contrôles mobile/bureau, transcription et tests. Aucune dépendance Symfony, Shopware ou Vue ajoutée : manuscrit Markdown/HTML et générateurs Python existants uniquement.
