# Livre II — intégration du chapitre 2 validé

**Compléments DEC-179/180 intégrés :** les présentations de runes ont désormais leurs fiches complètes, données manquantes choisies sous délégation et suivies par IDs dans `../lore/runes.md` et `../lore/personnages.md`. Cinq fenêtres ajoutées portent le II à quinze fenêtres/trente SVG, sans toucher au chapitre 1 ni ajouter de chapitre. Les anciens comptes et réserves de présentation ci-dessous décrivent les étapes précédentes ; bilan courant dans `correction_rarete_et_fiches_runiques.md`. Les ajouts Croissance du chapitre 1 restent à relire.

## Autorisation et source retenue

**DEC-170/171 — 25 novembre 2026, session locale.** Après réception des refontes mobiles, l’auteur répond **« Je valide le texte »** à la question identifiant la dernière version du chapitre 2, puis donne le **GO d’intégration**. Il précise ensuite : **« apres l'ajout du chapitre 2 je ferai les relecture »**. L’ajout précède donc ses relectures ; il ne faut pas attendre celles-ci pour intégrer le texte sélectionné.

- **Archive conservée :** `docs/new.txt`, 108 260 lignes ; SHA-256 `70ceecfdbe699d54e844c42e64bef0c9f6e3288a313d7f7b1d6deb2462118a59`.
- **Version retenue :** `103069–108183`, titre « Les prodiges de l’Académie », douze sections I–XII. Les versions antérieures ne sont pas ajoutées ; les commentaires ChatGPT suivant la fin ne sont pas du roman.
- **Source unique :** `../livre_2_le_vertige_des_vies_oubliees.md`. Aucun chapitre du II ajouté au I, aucun brouillon concurrent.
- **Chapitre 1 :** conservé dans son état local à l’ouverture de cette intervention, SHA-256 `eed12b51da5554ef3671b7a035104451c6d746c9738b3d1acac6087a9ab9ea8b` pour le manuscrit qui ne contenait encore que ce chapitre. Les ajouts de Croissance dans III/VII restent **à relire** ; le reste est validé par DEC-156.

## Arbitrages confirmés avant intégration — DEC-170

1. **Samia :** classe **Ranger astral**, rang **Commun**, cinq points ; distinguer le nom de la rareté.
2. **Bénédiction niveau 20 :** −45 % relatifs de risque d’échec ; −25 % relatifs de risque de résultat non maximal. Au niveau 30 : 60 % / 50 % inchangés.
3. **Vague légendaire :** soin de 5 % des **PV maximaux de Yoon**, au membre ayant le plus faible **pourcentage de PV actuels**, Yoon comprise.
4. **Clôture au III :** douze runes uniques, même effet et prérequis différents ; douze usages chacune. Les douze prérequis seront définis lors du plan du III, pas dans cet import.

Les réserves correspondantes de `integration_mobile_2026_11_25.md` sont désormais historiques. Les règles du III ne sont pas des révélations à insérer dans ce chapitre du II.

## Continuité du chapitre reçu

- **Vie 2 :** Hasol seize ans au début, dix-neuf lors des Révélations communes de Samia/Yoon, vingt-quatre à la retraite d’Elric ; pas de mémoire consciente du I.
- **Mentorat :** Elric, Porte-bouclier commun, niveau 45 à la rencontre ; 42→50 ans sur huit années. Lame runique acquise par maîtrise ; prudence sur boss et raids avant niveau 20, pas règle universelle.
- **Artisanat :** recherche des runes de faible valeur conseillée par Elric, tri par Œil, démonstrations avec Orven, réserve sacrificielle distincte des équipements/commandes. Nature des secondaires indépendante de l’artisan ; valeurs finales exactes conditionnelles aux améliorations d’Hasol, sans réussite garantie.
- **Cercles et équipement :** deux cercles initiaux, huitième cercle obtenu dans les premiers mois avant le niveau dix ; huit Vol de vie rares (bleues), 4★, +6, en deux ensembles de quatre. Cadeaux paternels Fatal/Gardien rares (bleus), 6★, +6 rangés avec accord d’Armin, pas vendus ni sacrifiés. Pas de transfert implicite des identifiants du I.
- **Aura :** coût 200 Mana et une rune détruite ; arme d’Elric avant niveau dix d’Hasol, usage personnel au dix seulement ; critique d’activation déclenchant Infiltration pendant trente secondes, pas critique ordinaire à l’épée.
- **Groupes :** Hasol/Yoon/Elric, puis Hasol/Yoon/Samia après retraite : trois membres, 50 points. Ray et Zio surtout dans les raids ; pas ajoutés au trio au-delà du plafond.
- **Jalons :** niveau 20 et premier boss personnel de donjon ; Bénédiction 45 % / 25 %, puis niveau 30 et 60 % / 50 %. Pas de déblocage de Siphon avant le niveau 40.
- **Samia :** faible lumière violette puis rang Commun, Cartographie et Coup astral de Ténèbres ; peut blesser une cible invulnérable atteinte, sans dissiper ni traverser automatiquement l’interception. Arc conservé, dagues développées.
- **Secrets :** Iseria finance et fournit réellement les huit runes ; scène d’indices avant entrée d’Hasol sans aveu explicite. Hasol ignore accord et origine maternelle. Ray ne connaît pas Croissance ; ni filiation cachée, ni origine ancienne des portails, ni mécanique des êtres Astraux révélées ici.
- **À DÉFINIR préservé :** XP, niveaux finaux des personnages, nombre final de cercles et compteurs, fiches individuelles et devenirs détaillés des runes, valeurs de vol de vie par ensemble, ressources restantes, paramètres de compétences non transmis. Les jalons ne fixent pas de courbe universelle.

## Présentation et limites

Intégration du texte validé, pas nouvelle rédaction. Titres et fenêtres adaptés aux conventions du manuscrit ; nom de classe de Samia raccordé à l’arbitrage explicite. Les fenêtres conservent leur source HTML textuelle et leurs images locales dérivées dans `assets/fenetres-livre-2/`. Aucun nouveau paramètre n’est déduit de la mise en page. Les relectures littéraires annoncées restent à faire après l’ajout.

Livre I et archive préservés ; modifications locales antérieures non annulées. Aucun chapitre 3, commit/push, déploiement, secret ou intervention en production. Risques principaux : confusion classe/rang de Samia, transfert indu d’inventaire du I, fausse validation des ajouts de Croissance, divulgation des secrets d’Iseria et conservation du texte mobile. Contrôles finaux à consigner après exécution.

## Intégration réalisée et contrôles

- **Deux chapitres**, respectivement **neuf et douze sections**, sans chapitre 3. Le texte utile complet du chapitre 2 est comparé à la transmission `103069–108183`, après les seuls raccords de nom de classe et neutralisation du balisage de présentation. Aucun commentaire après `108183` importé.
- **Quatre occurrences explicites** du nom de classe de Samia deviennent « Ranger astral ». Rang Commun, cinq points, emplois génériques « jeune Ranger », propos de la foule et mentions de Zéphyr préservés.
- **Neuf nouvelles fenêtres**, `L2-C2-F01` à `L2-C2-F09` : secondaire Vitesse découverte ; Lame runique ; palier de Croissance ; niveau 10 ; description d’Infiltration ; activation d’Infiltration 30 s ; Révélation de Samia ; paramètres de Vague ; compteur de boss +1. Aucun bonus, niveau de compétence, caractéristique ou affixe supplémentaire ajouté. Les titres de compétences mentionnés dans la narration ne deviennent pas tous des fenêtres.
- **18 nouveaux SVG**, bureau/mobile, soit **20 SVG pour les dix fenêtres du II**, chapitre 1 compris. Source HTML intégrale dans les `details`, chemins isolés dans `assets/fenetres-livre-2/`. Génération et contrôle idempotents ; aucun contenu actif, ressource distante, police distante ou image matricielle incorporée.
- **Chapitre 1 intégralement préservé**, octet pour octet, empreinte `eed12b51da5554ef3671b7a035104451c6d746c9738b3d1acac6087a9ab9ea8b` vérifiée par test ; sa fenêtre et ses deux SVG inchangés. Le test maintient notamment les ajouts de Croissance à relire.
- `python3 -m unittest discover -s tests -v` : **71 tests réussis**, dont 14 pour le II. Conservation intégrale, structure, classe/rang de Samia, Bénédiction, Vague et auto-soin, groupes, retraite, données HTML/SVG et caractère passif contrôlés.
- `python3 scripts/generer_fenetres.py --check` : **138 fenêtres / 276 SVG du I à jour**, sans régénérer ni modifier le livre I pendant l’ajout du II.
- Contrôle ciblé sans écriture du II avec `produire` : **10 fenêtres / 20 SVG à jour**, inventaire exact des dérivés et texte identique. Manuscrit : **176 353 octets** ; aucun changement de générateur ni de dépendance.
- `git diff --check -- . ':!docs/new.txt'` : réussi ; archive exclue du contrôle d’espacement pour ne pas corriger ses espaces de provenance.
- SHA-256 du manuscrit du II intégré : `d2724f31e857595529c8c19974f0cc01c508d0bd2a2a0ca30600706da2a16489`.
- Livre I inchangé pendant cet ajout : `9d27a766bef9706867ebbf658ba4dd2ecfb46b885cbf6a4e5d850ad3ae0caa2b`. Archive inchangée : empreinte ci-dessus confirmée après import.

Ces contrôles sont locaux et automatisés. Ils ne remplacent ni les relectures annoncées, ni une nouvelle revue visuelle navigateur, ni une preuve de rendu GitHub distant ou de publication.

### Ajout de navigation demandé après intégration

À la demande explicite « il faut un sommaire comme dans le livre 1 », ajout d'un
`## Sommaire` numéroté pour les **deux seuls chapitres existants**, avec liens
`#chapitre-1` et `#chapitre-2` et ancres `span` immédiatement devant leurs titres.
Aucun chapitre futur n'est annoncé. Titres, narration, fenêtres, styles et SVG
inchangés ; aucune régénération nécessaire. L'empreinte historique du chapitre 1
ci-dessus reste contrôlée après retrait exact de ces seuls ajouts de présentation,
sans renouvellement de fixture. Les tailles et empreintes du manuscrit complet
consignées plus haut décrivent l'état antérieur à cet ajout de navigation.

Contrôles après cet ajout : **73 tests réussis**, dont 16 pour le II ; comparaison
octet pour octet avec la copie locale avant ajout après ce seul retrait exact ;
double génération en mémoire idempotente des dix fenêtres et vingt SVG, tous
identiques aux fichiers existants ; `git diff --check` réussi. Aucun générateur
n'a écrit dans le manuscrit ou les dérivés pendant ces contrôles.

**Revue indépendante :** avis favorable sur conservation, données des fenêtres, périmètre d’autorisation et maintien des protections du chapitre 1. Audit statique d’accessibilité des 18 nouveaux SVG : textes des transcriptions identiques aux deux variantes, aucun débordement selon les coordonnées/longueurs déclarées, images alternatives et transcriptions présentes, aucun contenu actif. Limites : pas de navigateur connecté, donc ni mesure du rendu réel, ni contrôle clavier/lecteur d’écran, ni conformité RGAA complète revendiquée ; alternative de Vague peu descriptive et contraste des titres à vérifier s’ils sont réduits sous le seuil du grand texte. Aucune donnée ou narration n’a été changée pour cet audit.

## Retouches de relecture des fenêtres — DEC-172/173

1. **F01, fiche complète :** l’auteur souhaite toute la rune avec Vitesse en gras, puis délègue le choix d’une rune conforme aux règles. Rune d’exercice `L2-ORV-R001` choisie : Énergie 1★, native commune (blanche), +0→+3, Résistance +1 %→+4 %, première secondaire **Vitesse +1**. **Correction DEC-178 : le grade actuel reste commun (blanc)** ; le passage au vert de la première version de la fiche est annulé. Résistance suit la table canonique 1★ ; Vitesse +1 est un choix délégué, pas un barème universel. Fiche HTML complète et SVG ; seule la phrase d’identification de la rune blanche d’Orven est précisée dans la narration. Aucun équipement personnel ou ensemble actif déduit.
2. **F02, description :** à la demande de l’auteur, ajout dans la notification de Lame runique des deux effets déjà racontés : compréhension des techniques d’escrime ; assimilation, précision et automatismes de la lame. Aucun chiffre, coût, bonus supplémentaire ou nouvelle information sur les vies futures. Paragraphes narratifs environnants inchangés.

Les identifiants, les dix fenêtres du livre et les vingt SVG sont conservés. Seuls les quatre SVG F01/F02 changent ; le chapitre 1, la navigation et les autres fenêtres restent identiques. Les gardes de conservation neutralisent uniquement les modifications précises autorisées, sans exempter un chapitre ou toutes les descriptions. Les empreintes et tailles précédentes du manuscrit complet sont historiques après ces retouches. Les ajouts de Croissance du chapitre 1 restent à relire ; aucune nouvelle publication autorisée.

## Raccord de relecture avant le huitième cercle — DEC-174

**Actualisation DEC-175/176 :** le relevé initial ci-dessous est remplacé pour le bref état 7/8 et le retrait de cinq compléments. Une seconde Énergie est préparée en réserve et équipée immédiatement au huitième cercle : **8/8, 4 Fatal / 2 Gardien / 2 Énergie**. Six pièces hors cadeaux sont ensuite rangées au passage aux Vol de vie. La sélection avec Orven/Ray, les cadeaux, la visite envisagée et le dialogue de surprise restent conservés.

L’auteur précise qu’Hasol possède déjà **sept runes**, choisies avec **Orven et Ray** : quatre Fatal dont celle d’Armin, deux Gardien dont celle d’Armin, une Énergie. Le texte est raccordé à cet état avant le palier, puis au nouvel emplacement : **7/7→7/8**, pas deux seules runes jusqu’à la remise. Cinq compléments non identifiés individuellement ; aucun grade, étoile, affixe, prix ou calendrier d’achat inventé. Ensembles : Fatal 4/4 et Gardien 2/2, Énergie 1/2 inactif.

Au huitième cercle, Hasol veut retourner voir Orven le soir même ; Elric lui dit de ne pas être trop pressée et annonce une surprise de l’Académie, sans révéler les huit runes ni l’origine maternelle. Plus loin, les cadeaux d’Armin sont distingués parmi les sept runes portées ; leur scène de rangement est conservée. Les cinq autres runes sont aussi retirées et rangées avant d’équiper les huit Vol de vie. Aucun sacrifice ni vente implicite.

Correction limitée aux passages autorisés et raccords comptables indispensables ; fenêtres et SVG inchangés par DEC-174, contrairement aux retouches F01/F02 précédentes. Les contrôles de conservation exhaustive gardent la transmission d’origine comme référence et neutralisent seulement ces corrections exactes.

## Réserve immédiate et notification complète — DEC-175/176

**Clarification ultérieure prioritaire — DEC-177 :** la règle vise la préparation d’**au moins une rune lorsqu’un cercle est attendu**, pas une occupation absolument immédiate après un gain massif imprévisible. L’auteur qualifie les huit cercles rétroactifs du I d’**anomalie** : ses états 2/10 et les cadeaux maternels du lendemain restent donc inchangés et justifiés. La contradiction signalée plus bas est **résolue** ; aucune réserve de huit pièces, modification du don ou correction des chiffres du I n’est demandée après cet arbitrage. Au II, le gain est anticipé : la réserve préparée, l’équipement immédiat et F03 sont conservés.

L’auteur impose une règle pour **tous les personnages** : aucun emplacement runique disponible laissé vide. Il choisit expressément de **préparer une réserve puis l’équiper immédiatement** à l’ouverture du cercle, plutôt que tolérer un délai jusqu’à la prochaine visite en boutique. Cela ne crée aucune rune automatiquement et n’autorise pas à inventer des affixes ni à réécrire tous les anciens chapitres.

Au chapitre 2, Hasol prépare avec Orven et Ray une seconde Énergie, conservée hors équipement tant qu’elle n’a que sept cercles. Elle l’équipe immédiatement au huitième : composition 4/2/2, **8/8**, sans appliquer à cette réserve les caractéristiques de la rune d’exercice d’Orven. Les six pièces hors cadeaux sont retirées et rangées lorsqu’elle équipe les huit Vol de vie ; le coffret paternel et la scène avec Armin restent conservés. Les grades, étoiles et affixes de ces six pièces restent non définis.

La fenêtre `L2-C2-F03` conserve sa notification et indique désormais **« Cercles de mana : 7 → 8 »**, **« Emplacements runiques : 8 »**. Seuls ses deux SVG sont régénérés pour DEC-176 ; les F01/F02 précédemment corrigées et toutes les autres fenêtres sont préservées. La règle d’affichage avant/après vaut pour les nouvelles notifications de gain de cercle dont les comptes sont établis, pas un chiffrage inventé de tous les compteurs historiques.

**Signalement initial, RÉSOLU par DEC-177 :** trois fenêtres du livre I conservent 2/10 entre le déblocage de Croissance et le don maternel (lignes 3273/3422/3669 à cette réception). Initialement signalé comme contradictoire, cet état est ensuite justifié par l’auteur : huit cercles imprévisibles sont une anomalie, pas une progression attendue sans réserve. Aucun changement du I ou don/stock rétroactif inventé ; identités, affixes et compositions non transmis restent à définir.

Revue documentaire indépendante de DEC-175/176, avant DEC-177 : avis favorable, sans création automatique de rune, faux passif ou inventaire chiffré non transmis ; ancien état 7/8 qualifié comme remplacé et cas 2/10 du I alors soumis à arbitrage. Ce dernier est désormais résolu par la précision de l’auteur.

**Contrôle visuel local des retouches F01/F02 :** les deux SVG mobiles ont été rendus avec le Chrome headless installé, puis les captures PNG examinées : fiche complète lisible, Vitesse +1 effectivement en gras, description de Lame complète et sans texte coupé observé. Captures temporaires sous `/tmp/opencode/relecture-fenetres-livre-2/`, non dépendances du dépôt. Ce contrôle direct des SVG locaux ne prouve ni le rendu filtré par GitHub, ni la navigation clavier/lecteur d’écran ; aucune conformité RGAA complète revendiquée.

## Résolution du cas du livre I — DEC-177

Après la proposition de corriger les anciennes fenêtres 2/10, la question posée à l’auteur explicitait le besoin d’une provenance pour huit réserves hypothétiques. L’auteur ne valide pas cette proposition : il précise que seuls les cercles attendus doivent être préparés, **au minimum une rune**, et que les huit gains du I sont une anomalie. Les trois chiffres 2/10, la transition et le don maternel sont donc **préservés**, pas remplacés arbitrairement par 10/10. Aucune modification du livre I n’a été effectuée pendant ces retouches de relecture du II ; la contradiction documentaire initiale est levée par la précision de portée.

### Contrôles finaux des retouches DEC-172 à DEC-177

- **77 tests réussis**, dont 20 pour le II : conservation par inversions exactes des seuls raccords autorisés, récit des sept runes puis réserve immédiate, composition 4/2/2, six pièces rangées hors cadeaux, F01 complète et Vitesse en gras, F02 descriptive, F03 à 7→8 et huit emplacements, autres fenêtres et navigation préservées. Les gardes historiques du I restent réussis, sans nouvelle fixture ni correction matérielle de ses états 2/10.
- Contrôle `produire` sans écriture : **10 fenêtres / 20 SVG à jour**, inventaire exact et idempotence. Les seuls dérivés changés par les retouches sont les six SVG bureau/mobile de F01/F02/F03 ; aucun générateur ou dépendance modifié.
- F03 mobile également rendu avec Chrome headless puis capture examinée : deux nouveaux champs lisibles, aucune coupure observée. Contrôle local direct des SVG, pas preuve de rendu GitHub ni audit clavier/lecteur d’écran.
- Archive inchangée : `70ceecfdbe699d54e844c42e64bef0c9f6e3288a313d7f7b1d6deb2462118a59`. Livre I inchangé pendant ces retouches : `9d27a766bef9706867ebbf658ba4dd2ecfb46b885cbf6a4e5d850ad3ae0caa2b`. Ajouts de Croissance du chapitre 1 du II toujours à relire ; aucun chapitre 3, commit/push ou publication.

## Correction de rareté à +3 — DEC-178

L’auteur précise qu’une rune blanche reste blanche de +0 à +15. F01 conserve donc **grade actuel et natif Communs (Blancs)**, racine `white-grade`, badges communs neutres ; plus de marqueur vert de rareté. Énergie 1★, +3, Résistance +4 % et **Vitesse +1 en gras** sont préservés. L’apparition de la secondaire reste racontée : progression des affixes et rareté sont deux mécanismes distincts.

Seuls le HTML de F01, ses deux SVG et son contrat de test changent dans le manuscrit/rendu. Tout le texte hors F01 est protégé octet par octet par l’empreinte `8c25952b4307d21e5f12a9af961cba21ee10727b96e85567d30a037b2e4a57de` ; les 18 autres SVG restent identiques à la baseline de cette correction. Contrôle visuel local mobile avec Chrome headless : deux badges Communs blancs/neutres, pas de badge vert, Vitesse +1 toujours en gras, fiche lisible. Les règles actives sont précisées par DEC-178 ; un audit séparé recherche les autres occurrences de l’ancienne interprétation sans inventer leur grade initial.

**Audit terminé :** voir `audit_rarete_runes_2026_11_25.md`. Aucune autre transformation de rareté dans le II ; sept fenêtres du I et quatorze SVG directement concernés, plus reprises narratives/documentaires et inconnues à distinguer. Livre I non modifié par l’audit. **78 tests réussis**, sans présenter les anciennes fixtures du I comme une validation de ses grades selon la règle corrigée.
