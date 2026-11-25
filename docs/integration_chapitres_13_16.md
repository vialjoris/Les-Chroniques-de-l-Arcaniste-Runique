# Intégration du livre I — chapitre 13 XI, chapitres 14–16 et épilogue

**Rectification postérieure — DEC-178/179/180 :** l’ancien affichage orange des runes +15 par simple amélioration est corrigé dans le manuscrit et ses dérivés. Les seize pièces finales sont rares bleues 6★ +15 selon les données connues et les choix délégués ; fiches et identités dans `../lore/runes.md`, porteurs dans `../lore/personnages.md`. Les inconnues et contrôles datés ci-dessous restent la provenance de cet import, pas l’état des présentations actuelles. Voir `correction_rarete_et_fiches_runiques.md`.

## Périmètre et statut

Consignation du **23 novembre 2026**. Le GO de l’auteur autorise l’intégration locale du plan ; tous les chapitres **1–16 sont lus et validés**, notamment les 10–12 auparavant en lecture et l’ajout XI du 13. Pas de nouvelle rédaction du livre II, commit ou push autorisé. Les dix sections existantes du 13 et les chapitres précédents sont à préserver hors corrections ciblées demandées.

Cette note suit les **sources éditoriales**, pas les résultats techniques de génération/tests : leur contrôle relève de la passe d’intégration du manuscrit et des dérivés. `roman.md` reste le seul manuscrit ; ni cette note ni l’archive ne constituent une variante littéraire.

## État de l’archive et bornes

Source : [`new.txt`](new.txt), **74 252 lignes**, SHA-256 à la réception documentaire :

```text
26049b4c4489b6f7bf7925cb0592470e63bb8ff50c14f7b70d5f67789b6f9264
```

Le précédent import 1–12 s’arrêtait avant le nouvel apport **51619+**. Aucun nettoyage, déplacement ou réécriture des archives par cette intégration ; la différence de `new.txt` par rapport à Git est l’apport de l’auteur, pas une modification documentaire. Les repères ci-dessous sont des lignes 1-based de cette empreinte, non des offsets stables pour une future archive prolongée.

| Lignes de `new.txt` | Nature | Traitement |
|---|---|---|
| 51623–51821 | Dossier de règles donjons/portails/mémoire, contenant des paramètres explicitement provisoires | Consigner avec les arbitrages plus récents ; ne pas importer comme scène |
| 51826–52255 | Propositions concurrentes sur Croissance et essais de scène nocturne | Pas de deuxième fin du 13 ; extension des cent boss aux portails écartée |
| 52266–52850 | Ajout XI « La nuit où tout a changé » et titre/conclusion du 13 | Ajouter **XI seul**, texte 52268–52848, après la dernière phrase existante de X ; ne pas réimporter I–X |
| 52854–52862 | Rappel de coiffure de Zio | Cheveux courts, raccord ciblé |
| 52865–52985 | Dossier cercles naturels/Révélation, vocabulaire de théorie du monde | Actualiser les références ; pas de formule scientifique ajoutée |
| 52992–56881 | Chapitre 14 « Le centième boss » complet | Version retenue, sans en-têtes de courriel ni commentaire final |
| 56889–57010 | Propositions Siphon monocible puis zone Vent | Identité retenue ; valeurs chiffrées non validées |
| 57017–57623 | Développement, plan du 15 et corrections de barème | Distinguer propositions, faits ultérieurement racontés et barème final |
| 57625–62189 | Première rédaction du 15 | Variante remplacée ; ne pas doubler le chapitre |
| 62191–62285 | Discussions et versions successives des points | Seul barème final retenu : 100/100/100/250/400/800 |
| 62288 | « Refait le chapitre 15 » | Instruction de remplacement, hors roman |
| 62289–66825 | Seconde rédaction « Enfin, la magie » | **Version retenue**, quatorze sections ; pas la première rédaction |
| 66827–68154 | Grossesse, plans concurrents du 16, évolutions de Samia et choix de l’épilogue | Ne pas intégrer les variantes incompatibles avec le texte final |
| 68155–73963 | Chapitre 16 « Celle qui demeure », épilogue et mention de suite | **Version retenue** ; épilogue à partir de 73537 ; fin du livre à 73959, mention de suite à 73963 |
| 73965–74006 | Harmonisation « ma belle » → « ma princesse » pour Zio → Hasol | Correction ciblée à appliquer également aux chapitres antérieurs concernés ; pas aux autres locuteurs |
| 74007–74026 | Satisfaction de l’auteur et réponse de ChatGPT | Provenance, hors roman |
| 74029–74252 | Append Ténébria : parole d’auteur, développement, validation, reformulation | Dossier de lore/planification, pas une nouvelle scène du I |

Les bornes identifient les versions, pas une autorisation d’insérer les commentaires entourant les textes. La validation littéraire actuelle de l’auteur est distincte du simple « c’est validé » employé par ChatGPT dans certaines réponses mobiles.

## Décisions consignées

| Décision | Sujet | Limites principales |
|---|---|---|
| DEC-110 | Réception et validation du livre I complet | Pas de suite ni publication implicite |
| DEC-111 | Donjons, portails et mémoire | 24 h provisoire ; effectif distinct des points ; mémoire parfaite à R11 seulement |
| DEC-112 | Trois compteurs, cercles et équipement | Portails uniquement aux 5 000 ; aucun affixe/ID de remplacement inventé |
| DEC-113 | Cercles naturels et Siphon | Vent neutre ; coefficients et autres chiffres ouverts |
| DEC-114 | Samia, deuil et Présage des failles | Plusieurs proches morts ; carte initiale au II et mort solitaire non imposées |
| DEC-115 | Iseria, grossesse, survivants, Rune temporelle et épilogue | Devenir de l’enfant, origine profonde de la rune et formule du déclencheur ouverts |
| DEC-116 | Ténébria et faille astrale | Validation qualifiée, pas tous les détails et dialogues de ChatGPT |

### Éléments de continuité à préserver

- Iseria : mort en forêt pendant une cueillette au 14, portail blanc non repéré, **56 h après notification** ; la notification est celle des portails, pas un avis automatique de décès.
- Hasol : début du 14 niveau 38/treize cercles ; centième boss de **donjon**, Manticore des Cendres niveau 41, **13→14**. Au 15, niveau 40/Siphon, **15 à 5 000** puis **16 à 10 000** démons personnels cumulés. Ne pas compter ces démons aux mille ni leurs boss aux cent boss de donjon.
- Équipement agrégé : 4 Fatal/4 Arcanique/4 Vitesse/1 Gardien, puis deuxième Gardien ; 6★, grade **natif** rare minimum, +15, grade **affiché** orange. Deux Énergie finales 6★, natives rares (bleues), +15 : **faits du 15 validé**, pas une prétendue réponse explicite au questionnaire. Pas d’évolution des étoiles ni de remplacements individuels déduits ; conserver les identités historiques.
- Siphon : actif de Vent neutre, zone, dégâts PA, vol Mana, recharge ; les propositions 120 %, 75 %, 8 m, 100 Mana, 20 s, 1 200 Mana restent non adoptées. Aura et Infiltration gardent leurs paramètres propres.
- Samia : plusieurs proches morts, pas toute sa famille ; blonde et Ranger commune au I. Présage approximatif ~10 h au 15, carte par couleur au 16 ; isolement sans jalousie de la grossesse. Passif au début du II, carte évoluée immédiate non fixée.
- Hasol 34 ans, grossesse découverte vers **sept semaines**, Zio informé avant l’orange. Ni sexe/prénom ni naissance/destin de l’enfant inventés. Zio se sacrifie par Dernier Rempart et tue le démon ; **Yoon, Ray, Samia survivent**, contrairement à l’ancien plan.
- Zio → Hasol : **« ma princesse »**. Épilogue du I : Hasol a **quinze ans, à la veille de ses seize ans et de la Révélation**, 12 DONG + 1 DING ; Iseria : **« Astrae vaël norien… thara sel ven. »**, sens « Qu’Astrae soit avec nous… Ça a commencé. » Hasol ne comprend pas le dialecte. Ne pas appliquer cette veille à tous les retours par défaut.
- **Section XV du 16, 73117–73535 :** Rune temporelle découverte par les chasseurs d’inventaire près du lieu de chute du démon, remise à Hasol pour expertise, puis laissée plusieurs jours dans son coffret. Œil l’identifie partiellement, grade/rang indéterminés. Notification d’instabilité émotionnelle pendant le deuil, activation involontaire, cadran/sablier 12 DONG + 1 DING. Cette scène est présente dans le texte retenu, avant l’épilogue ; ni nouvelle scène à inventer ni intervalle jusqu’à 45 ans à combler.

## Qualification du dossier Ténébria

1. **Parole d’auteur — 74029 :** Ténébria responsable du retour des portails au I ; livre de magie noire à la bibliothèque royale ; colère liée à sa vie injuste ; invocation rouvrant une faille scellée par un ancêtre. Le sort reconnecte les mondes, sans expliquer chaque apparition de portail.
2. **Développement ChatGPT — 74030–74226**, suivi du **« je valide . » auteur — 74228** : mécanisme de sceau encore fragilisé après retour, résonance à la Révélation de Ténébria, écart de quatre ans entre les sœurs et chronologie 32/28 au I puis 16/12 au II retenus dans leur périmètre. Ténébria n’a pas voulu la destruction du monde. Grandes lignes du clan ayant imposé sa vie et l’exploitant ensuite comme sauveuse ; révélation progressive au II.
3. **Reformulation ChatGPT — 74229–74252 :** ne vaut pas une seconde validation. Les âges et le mécanisme figuraient déjà avant le « je valide » ; leur consignation ne repose donc pas sur cette seule reformulation.
4. **PROPOSITIONS / À DÉFINIR :** contenu exact de la promesse du grimoire, scène de confrontation et répliques, prophétie détaillée, enlèvement et organisation du clan, identité et trajectoire de l’oncle empereur, paramètres de classe et état de la faille lors des autres retours. Rien de cela n’autorise à révéler cette sœur dans le manuscrit du I ou à inventer des caractéristiques et une hérédité astrale.

## Écarts résolus et limites non résolues

**Raccord ciblé du chapitre 16, section X :** « Pendant plusieurs minutes, ils réussirent à faire reculer le boss » devient « Pendant quelques secondes, ils réussirent à faire reculer le boss ». La phrase suivante termine les trente secondes d’Infiltration runique : ce raccord retire la contradiction de durée sans changer les actions, les effets de la compétence ou l’issue du combat.

**Raccord descriptif du chapitre 13, section XI :** « Il passa une main dans ses longs cheveux noirs » devient « Il passa une main dans les longs cheveux brun sombre d’Hasol ». Le geste de Zio vise explicitement les cheveux d’Hasol, sans ambiguïté avec ses propres cheveux bruns courts.

**Raccord du chapitre 15 :** dans la réplique de Ray, « tu attends vingt-quatre niveaux » devient « tu attends le niveau quarante ». Le premier sort offensif est débloqué au niveau 40 ; aucun point de départ au niveau 16 ne justifie l’ancien décompte. La correction reprend le niveau canonique sans inventer une nouvelle durée.

**Écarts résolus par décision plus récente :** décès de Yoon/Ray et unique survivante au I remplacés ; réveil initial déplacé à l’épilogue la veille ; plafonds de portails successifs remplacés ; extension des cent boss aux portails écartée ; mémoire parfaite précoce de certaines réponses ChatGPT rejetée ; suggestion de double comptage portails/mille écartée. Ce ne sont plus des contradictions nécessitant de rouvrir le choix de l’auteur.

**Points encore À DÉFINIR, sans les combler :** origine exacte du treizième cercle après le 9 ; dates absolues et remplacement individuel des runes ; affixes finaux et stocks ; valeurs de Siphon ; portée/exhaustivité de Présage ; délai de réinitialisation des donjons ; entrée anticipée et effectif des portails ; origine profonde de la Rune temporelle, grade/étoiles et formule du déclencheur ; devenir de l’enfant ; détails familiaux et impériaux du dossier Ténébria ; état de la faille et des couleurs lors des vies suivantes. La synchronisation des premiers bleus est une précision validée, pas la prédiction de chaque portail.

La catastrophe mondiale à 45 ans au III n’est pas la bataille orange à 34 ans au I. La nouvelle origine de la faille ne démontre pas une cause commune avec les sorties anormales de donjons. Les variantes où Zio meurt sans employer Dernier Rempart puis Hasol achève le démon ne remplacent pas son autodestruction fatale du texte final. L’activation de la section XV est conservée ; seul le réveil, désormais en épilogue du I, remplace l’ancien découpage.

## Références mises à jour

`AGENTS.md`, `PLAN_DIRECTEUR.md`, `README.md`, `source.md`, `lore/decisions.md`, `lore/systeme.md`, `lore/personnages.md`, `lore/runes.md`, `lore/chronologie.md`, `lore/pistes.md` et notices de suivi historiques reliées à cette réception. Les anciens comptes rendus gardent leurs preuves datées ; leur statut courant est surchargé par DEC-110–116.

**Exploitabilité :** aucun changement de déploiement, dépendance ou procédure de génération revendiqué ici. Aucun secret ni donnée privée supplémentaire recopié depuis les en-têtes de courriel. Pas de commit/push ; contrôles du manuscrit, des fenêtres et des dérivés à consigner par la passe responsable, sans inventer leurs résultats.

## Contrôles d’intégration locale

- Lecture de la transmission couverte collectivement : historique 1–26000 et 26001–51618 par deux agents de lecture ; nouvel apport 51619–74252 par les agents de documentation et d’intégration.
- Conservation octet pour octet des chapitres 1–12 et des sections I–X du 13, du début du chapitre 1 à la dernière phrase de X : SHA-256 `5888c49291d669a04ff28d0c2a3ce3912ef11454149eaa5c1fab67a227ac6a8d`. Les ajouts du sommaire sont extérieurs à ce préfixe narratif.
- Ajout de **26 fenêtres**, soit **52 SVG** : total **138 fenêtres et 276 SVG**. Les SVG historiques sont inchangés ; les deux générateurs confirment que les dérivés et `lecture.html` sont à jour.
- Empreintes des archives vérifiées inchangées, dont `docs/new.txt` et les copies de provenance 1–4. `git diff --check -- . ':!docs/new.txt'` réussit ; le contrôle global signale seulement trois espaces de fin de ligne de l’apport utilisateur, conservé intact.
- Revue éditoriale indépendante favorable après les raccords ciblés ci-dessus ; aucune scène de Ténébria importée dans le manuscrit.
- Audit structurel des 26 nouvelles fenêtres : transcriptions complètes, variantes mobile/bureau et aucun dépassement de cadre détecté par les coordonnées textuelles SVG. Ce contrôle ne remplace pas une validation visuelle.
- **Limite de validation :** navigateur de bureau déconnecté ; rendu effectif, navigation clavier et lecture d’écran non vérifiés. Les titres de fenêtres restent des `div` et les tableaux sans `caption`, conformément aux modèles existants ; aucune conformité RGAA globale revendiquée.
- **Validation automatisée finale :** `TMPDIR=/tmp/opencode PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s tests -v` : **54 tests réussis**, après régénération du lecteur et application des trois raccords ciblés. Les deux commandes de génération avec `--check` et le contrôle du diff hors archive réussissent également. Aucune ancienne fixture de conservation renouvelée.
- **Sécurité :** audit des documents complets et des 276 SVG sans contenu actif, ressource distante ou fichier dérivé manquant ; tests ajoutés pour les injections hors fenêtres et les primitives SVG hostiles. Le convertisseur reste un outil pour sources revues, pas un assainisseur de HTML arbitraire.
