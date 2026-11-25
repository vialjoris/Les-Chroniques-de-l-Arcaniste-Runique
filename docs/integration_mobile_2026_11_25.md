# Réception mobile du 25 novembre 2026

**Actualisation postérieure — DEC-170/171 :** l’auteur confirme le nom **Ranger astral**, rang Commun ; les chiffres de Bénédiction au 20 (**45 % / 25 %**) ; le soin de Vague sur les **PV maximaux de Yoon**, auto-ciblage possible ; douze runes de clôture uniques, même effet/prérequis différents, douze usages chacune, prérequis à préparer au plan du III. Il **valide** le chapitre 2 `103069–108183`, puis donne le GO d’intégration et annonce ses relectures après l’ajout. Les statuts non validé/non intégré et réserves correspondantes ci-dessous décrivent donc la réception initiale. Voir `integration_livre_2_chapitre_2.md`. Les ajouts de Croissance au chapitre 1 restent explicitement à relire ; aucun chapitre 3 ou publication autorisé.

## Périmètre et provenance

Archive : `docs/new.txt`, **108 260 lignes**, SHA-256 `70ceecfdbe699d54e844c42e64bef0c9f6e3288a313d7f7b1d6deb2462118a59`. Archive conservée intacte. La lecture antérieure est documentée jusqu'au chapitre 1 ; reprise avec recouvrement à 79570, lecture de toute la suite jusqu'à 108260, dont audit délégué intégral de 81496–95000. Comparaison avec HEAD : les **79 725 premières lignes sont identiques** ; la première différence est le séparateur de conversation à 79726, puis le nouvel apport. Le préfixe historique n'a donc pas été remplacé silencieusement. Ce relevé distingue les messages de l'auteur des développements de ChatGPT. Les bornes actuelles priment les anciens relevés décalés de quelques lignes ; ne pas réimporter le chapitre 1.

Le dépôt comportait déjà des modifications locales dans `AGENTS.md`, `PLAN_LIVRE_II.md`, `docs/integration_livre_2_chapitre_1.md`, `docs/new.txt`, `lore/chronologie.md` et `lore/decisions.md`. Elles sont préservées.

## Chapitre 2 : rédaction mobile autorisée, validation finale absente

- `79727` : demande de chapitre 2 ; premier essai partiel `79733–79927`.
- `79954–83670` : première version complète ; répétition des consignes locales DEC-157 à `79931–79949`, pas nouvelle décision distincte.
- `85937` : « Voilà go chapitre 2 » ; `86343` : demande de refaire le plan puis le texte.
- `86383–91389` : version complète en treize sections, explicitement en lecture à valider avant intégration (`91393`).
- `92068` : refonte demandée ; texte `92074–97236`, treize sections.
- `97489` : nouvelle refonte ; texte `97495–102875`, quatorze sections.
- `102888` : demande des runes poubelles dès Orven ; `103055` : refonte ; `103057` : l'idée d'anticiper les runes pourrait venir d'Elric.
- **Dernière version complète : `103069–108183`, douze sections I–XII**, titre inchangé « Les prodiges de l'Académie ». ChatGPT précise à `108189` qu'il s'agit d'une proposition de manuscrit. Les deux messages auteur suivants concernent les synergies, pas la validation du chapitre.

**Statut : PROPOSITION / version de lecture non intégrée.** Les GO mobiles sont réels et dépassent les anciens « chapitre 2 non autorisé » dans ce seul périmètre ; ils ne valent ni validation littéraire, ni autorisation de publier ou de rédiger le chapitre 3. Aucun brouillon concurrent n'est créé. La source du II conserve son seul chapitre 1 validé.

## Décisions reçues

Voir **DEC-158 à DEC-169** dans `../lore/decisions.md` : compétences d'Hasol, évolutions de Samia et Yoon, équipement et accord secret d'Iseria, changement du drame du chapitre 15, Savoir runique, clôture et cycle des portails, descendance et synergies. Ce sont des futurs validés dans leur périmètre explicite, **pas des événements déjà racontés dans un chapitre 2 validé**.

## Retouche ciblée du chapitre 1 du II — DEC-159

Auteur `85176` : demande d'un message pour les modifications de Croissance ; transfert `85180–85248`, puis précision explicite `85250`. Sections III et VII seulement : trois compteurs dès la Révélation (mille monstres admissibles hors portails, cent boss de donjon personnels, cinq mille démons personnels) et transmission de ces trois suivis à Elric. Seul le premier impose des prérequis de niveau d'ennemi ; les démons n'y sont pas comptés. Aucun palier immédiatement gagné, seuil avant dix, règle universelle d'accès aux raids ou nouveau savoir de Ray ajouté. Aura, neuf sections, fenêtre et reste du chapitre inchangés. Les ajouts locaux restent à relire ; la validation DEC-156 du texte antérieur n'est pas annulée ni étendue automatiquement à ces nouvelles formulations.

## Correction ciblée du livre I — DEC-168

L'auteur demande à `97371` que les secondaires découvertes soient identiques même si un autre artisan améliore, puis à `97427` de corriger le I si nécessaire. La règle existe déjà dans DEC-097 et `lore/systeme.md`. La réponse mobile situe à tort la scène au chapitre 9 : la fenêtre `095` et l'essai d'Orven sont au **chapitre 10** du manuscrit réel.

Correction locale limitée à deux paragraphes de cette fenêtre et une réplique d'Orven : nature des secondaires indépendante de l'artisan ; valeurs finales exactes conditionnelles aux améliorations personnelles d'Hasol jusqu'à +15. L'expérience reste réalisée par Hasol ; mêmes échecs, ressources, rune Énergie commune (blanche), 1★, +0→+3, puis secondaire Mana +10. Aucune nouvelle démonstration ajoutée, aucune modification du chapitre 9. Les SVG `095.svg` et `095-mobile.svg` sont régénérés depuis le HTML.

## Points à arbitrer avant intégration du chapitre 2

1. **Nom de classe de Samia :** auteur `84392` « Livre 2 ranger astral », puis `84406` rang commun confirmé. Les dernières refontes affichent « Ranger ». « Ranger astral » pourrait être le nom et Commun le rang ; ne pas trancher silencieusement. Au III, son **rang Astral** remplace la proposition légendaire antérieure ; « Exécutrice astrale » reste le nom déjà retenu.
2. **Bénédiction niveau 20 :** amélioration validée, mais **45 % / 25 %** sont des chiffres proposés par ChatGPT (`83875–83879`), repris sans arbitrage numérique explicite. Le niveau 30 **60 % / 50 %** est en revanche expressément retenu par l'auteur à `83844`.
3. **Soin de Vague légendaire :** 5 % des PV de **Yoon** vers le membre au plus faible **pourcentage** de PV est explicite (`85871`, `85905`). Base « PV maximaux » et auto-ciblage sont des précisions de ChatGPT ; à confirmer avant de figer la fenêtre.
4. **Slimes, niveaux et cercles :** règle explicite `85250` : seuls les mille monstres ont des prérequis de niveau d'ennemi. Le huitième cercle avant dix ne fixe pas à lui seul les tranches admissibles avant dix ni une courbe d'XP. Les refontes ne doivent pas créer huit réserves de Mana distinctes. Les jalons de sauvegarde DEC-145 restent prioritaires.
5. **Douze runes de clôture / unicité :** objectif de douze runes, douze usages chacune, explicitement demandé. Articulation avec les Runes astrales uniques de DEC-143 à préciser : douze objets uniques distincts de même fonction ou exception à l'unicité ? Aucune fabrication/duplication ni activation différée adoptée par déduction. Ressources, acquisitions, usages restants après les premières vies et repos après clôture magique restent à définir.

## Erreurs de réponses non importées

- Le prêt Énergie légendaire (orange), 4★, +9 du I n'est **pas** transformé en cadeau acquis : DEC-100 et restitution intacte conservés. Le « oui je valide » `91544` porte notamment sur la conservation des propriétés par Savoir, pas sur une réécriture rétroactive implicite de ce prêt.
- Bleu→orange demande deux transitions de rareté, pas les trois annoncées par ChatGPT à `91576`.
- Le délai minimal de retour de 72 h concerne le **portail disparu**, pas une suspension mondiale des apparitions. Un autre portail peut se manifester pendant ce délai.
- Catastrophe mondiale du III à **45 ans**, pas 46 ; pas déjà vécue par Hasol au II. Pas de mémoire parfaite avant R11.
- Le mécanisme des drames et des rangs Astraux est révélé au III ; pas de révélation au chapitre 2, pas de règle universelle détaillée inventée sur tous les traumatismes.
- Coup astral au II peut blesser une cible invulnérable atteinte ; **ne dissipe pas** ce statut. La dissipation future de Danse astrale appartient au III.
- La nouvelle Lame runique est une **compétence**, pas le retour de l'ancien ensemble Lame retiré par DEC-076.

## Contrôles et limites

Intégration documentaire locale et corrections ciblées des chapitres 10 du I et 1 du II seulement. Archive inchangée ; aucun chapitre 2 ajouté, chapitre 3, commit, push, déploiement, accès à des secrets ou intervention en production. Les risques sont éditoriaux (survalidation, secrets révélés trop tôt, confusion entre rares et Astraux, compteurs et sauvegardes), pas une modification de code exécutable. Résultats des contrôles techniques consignés après exécution.

### Résultats techniques

- `python3 -m unittest discover -s tests -v` : **65 tests réussis**, dont contrôle des trois compteurs dans les sections III/VII, texte exact de DEC-168 et mutations refusant les autres changements du chapitre 10.
- Les premiers contrôles avaient détecté la correction éditoriale autorisée : garde-fous adaptés par inversion exacte et réversible des seuls textes de DEC-168, sans renouveler les empreintes ni les fixtures historiques. `tests/fixtures/` sans diff.
- `python3 scripts/generer_fenetres.py --check` : **138 fenêtres, 276 SVG à jour** ; seuls les deux dérivés de `095` ont changé.
- `python3 scripts/generer_lecture.py --check` : lecteur local à jour après régénération ; trois lignes modifiées correspondant aux deux paragraphes et à la réplique.
- Livre I : comparaison à HEAD après application en mémoire des deux remplacements ciblés, **identité exacte** ; aucun autre octet modifié. Livre II : seulement **18 lignes ajoutées**, en deux passages, aucune suppression ; sa fenêtre et ses dérivés restent identiques.
- Archive : SHA-256 final identique à celui de réception. Manuscrits finaux : I `9d27a766bef9706867ebbf658ba4dd2ecfb46b885cbf6a4e5d850ad3ae0caa2b` ; II `eed12b51da5554ef3671b7a035104451c6d746c9738b3d1acac6087a9ab9ea8b`.
- Revue indépendante des nouvelles décisions : pas de survalidation matérielle relevée dans le périmètre audité. Ces contrôles ne valent ni validation littéraire des nouvelles formulations, ni preuve de rendu GitHub distant ou de publication.
