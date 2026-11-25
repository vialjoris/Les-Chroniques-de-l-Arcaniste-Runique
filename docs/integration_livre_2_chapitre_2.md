# Livre II — intégration du chapitre 2 validé

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

**Revue indépendante :** avis favorable sur conservation, données des fenêtres, périmètre d’autorisation et maintien des protections du chapitre 1. Audit statique d’accessibilité des 18 nouveaux SVG : textes des transcriptions identiques aux deux variantes, aucun débordement selon les coordonnées/longueurs déclarées, images alternatives et transcriptions présentes, aucun contenu actif. Limites : pas de navigateur connecté, donc ni mesure du rendu réel, ni contrôle clavier/lecteur d’écran, ni conformité RGAA complète revendiquée ; alternative de Vague peu descriptive et contraste des titres à vérifier s’ils sont réduits sous le seuil du grand texte. Aucune donnée ou narration n’a été changée pour cet audit.
