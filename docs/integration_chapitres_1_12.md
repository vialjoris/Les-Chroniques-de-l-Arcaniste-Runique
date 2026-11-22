# Intégration du livre I — chapitres 1 à 12

## Autorisation et statuts — 22 novembre 2026

- **CANON :** l’auteur approuve les quatre révisions séparées : « autre info les chapitre revision sont validé mais sans le lore en debut et fin ». Les encadrés avaient déjà été retirés par DEC-091.
- **CANON :** les chapitres 5 à 9 conservent leur validation et leur texte. Aucun nouvel arbitrage de niveau, d’équipement ou de compétence n’y est appliqué.
- **TEXTES EN LECTURE :** les chapitres 10 V2, 11 et 12 sont intégrés sur demande, après les arbitrages techniques de session. Leur import n’est pas une validation littéraire globale de ces trois textes.
- **À DÉFINIR :** les paramètres absents restent ouverts. L’import ne valide ni les nouvelles classes proposées pour les vies suivantes, ni une nouvelle composition astrale, ni le chapitre 13.
- Aucun encadré de lore, commentaire de conversation, courriel ou illustration n’est ajouté au manuscrit. L’auteur a abandonné la demande d’image pour le roman ; les images sont destinées au manhwa.
- `roman.md` reste l’unique manuscrit officiel. Les quatre fichiers `chapN_revision.md` sont conservés comme **copies de révision approuvées / archives préservées**, avec changement de leurs seuls en-têtes de statut.

## Provenance des textes

Ces numéros de ligne repèrent `new.txt` au moment de cet import ; ils ne sont pas des identifiants immuables. La lecture de la transmission est répartie dans la session principale et ses sous-agents. Le présent travail a relu intégralement les trois tranches narratives ci-dessous, la correction de fiche et l’audit de transmission, sans prétendre relire seul tout l’historique antérieur.

| Source retenue | Bornes | Traitement |
|---|---|---|
| `chap1_revision.md` à `chap4_revision.md` | Corps après le marqueur de début du chapitre de lecture | Comparaison avec le manuscrit ; pas de réimportation des anciennes versions mobiles |
| Chapitre 10 V2 — Ceux qui riaient autrefois | `new.txt`, 37170–41766 | Huit sections I–VIII, texte intégral, dix fenêtres HTML présentes dans la source |
| Correction de la fiche d’Iseria | `new.txt`, 41768–41848 | Données confirmées ensuite par l’auteur ; remplacement des deux fiches incomplètes, pas insertion du commentaire de ChatGPT |
| Chapitre 11 — Le dernier départ | `new.txt`, 41855–46997 | Dix sections I–X ; cinq notifications textuelles converties en HTML |
| Chapitre 12 — La légende prend sa place | `new.txt`, 47100–51614 | Onze sections I–XI ; quatre notifications fusionnées converties en HTML |

Les en-têtes de courriel précédant les chapitres et les commentaires entre les tranches sont exclus. Aucune variante antérieure du chapitre 10 ni récapitulatif des vies suivantes n’est ajouté. Voir aussi `../lore/audit_transmission_chapitres_10_12.md` : son état « intégration suspendue » décrit le contrôle antérieur aux arbitrages et au présent import, pas le résultat actuel.

## Révisions 1 à 4 : intégration sans régression graphique

La comparaison hors fenêtres établit que les quatre narrations approuvées sont déjà celles du manuscrit. Il n’est donc pas nécessaire de remplacer leurs segments par les anciennes copies HTML.

- Chapitres 1 et 2 : aucune modification du corps du manuscrit.
- Chapitre 3 : ajout unique de **C3-F01**, état initial de l’Énergie commune (blanche), 2★, +0 ; principale PV non chiffrée, aucune secondaire.
- Chapitre 4 : ajout unique de **C4-F01**, commande Gardien commune (blanche), 2★, +0, objectif +2, trois tentatives maximum.
- Les anciennes mentions « AJOUT PROPOSÉ » restent dans les corps archivés pour leur provenance, mais ne sont pas importées dans le roman.
- Les **89 fenêtres déjà modernisées** restent strictement identiques, données et HTML compris. Aucune ancienne présentation n’écrase leur refonte.

La conformité aux copies approuvées porte sur les lignes narratives, en ignorant les lignes vides, séparateurs, ancres et commentaires de préparation ; elle ne prétend pas que les anciennes et nouvelles mises en page HTML sont identiques.

## Corrections techniques limitées

### Fiches du chapitre 10

Les arbitrages directs de la session priment l’état encore ouvert de l’audit initial :

- **Œil — DEC-097 :** résultat final exact à +15 si Hasol effectue les améliorations et atteint ce palier ; échecs et dépenses maintenus. Aucun résultat d’un autre artisan ni ordre intermédiaire garanti n’est ajouté.
- **Affixes — DEC-098 :** CC/DCC retirés des affixes runiques ; mécanismes critiques inchangés. Aucun remplacement de statistique dans les chapitres antérieurs.
- **Vitesse rare (bleue), 3★, +0 :** principale Vitesse +3 ; secondaires Attaque +8 % et Puissance arcanique +60, fiche confirmée directement par l’auteur. La rune n’est ni améliorée ni équipée par cet import ; sa projection complète à +15 n’est pas inventée.
- **Énergie légendaire (orange), 4★, +9 d’Iseria :** principale PV +25 % ; secondaires PA +60, Vitesse +4, Défense +30, Mana +20. Projection personnelle à +15 : PV +43 %, PA +140, autres secondaires inchangées. Les deux gains de PA +20/+60 gardent leur ordre indéterminé. Les données complètent les fenêtres existantes C10-F06 et C10-F08, sans doublon de fiche ou de PA. La rune est rendue intacte à +9.

Les bornes de PA principale et les renforcements secondaires PA retenus dans la délégation, ainsi que les plafonds d’activation d’ensembles confirmés dans la session, ne servent à calculer aucune caractéristique manquante du récit. Pas d’interpolation entre +0 et +15, de probabilité de renforcement ou de total effectif ajouté.

### Désignations et structure

- Vingt-deux substitutions ciblées précisent des mentions de runes dans les nouveaux chapitres : Vitesse rare (bleue), 3★ ; Énergie d’Iseria légendaire (orange), 4★ ; Énergie d’essai commune (blanche), 1★, puis peu commune (verte) à +3 ; rune commune (blanche), 1★, sacrifiée avant le premier donjon.
- Le lot de récupération blanc/vert du 11, la rune légendaire du marchand et la rune verte du débutant au 12 gardent leurs rangs **À DÉFINIR**. Aucun rang, affixe ou ID documentaire n’est inventé. Les explications génériques sur les runes ne sont pas transformées en pièces identifiées.
- Les titres de sections deviennent des titres Markdown ; les fins de chapitre reprennent la présentation existante. Le sommaire comporte douze entrées et douze ancres uniques.
- Les neuf notifications du 11 et du 12 sont structurées en HTML sans nouveau chiffre. Les libellés des champs remplacent uniquement les ruptures de ligne ou collages de la transmission ; les valeurs et résultats sont conservés.

L’ordre des scènes et la narration des trois tranches sont conservés, hors ces précisions de désignation. Aucune correction stylistique générale, scène supplémentaire, suppression de dialogue ou modification des relations n’est effectuée.

## Inventaire des fenêtres après import éditorial

| Chapitre | Fenêtres après import | Modification de cet import |
|---|---:|---|
| 1 | 16 | Aucune |
| 2 | 14 | Aucune |
| 3 | 5 | C3-F01 ajoutée |
| 4 | 5 | C4-F01 ajoutée |
| 5 | 10 | Aucune |
| 6 | 4 | Aucune |
| 7 | 9 | Aucune |
| 8 | 6 | Aucune |
| 9 | 22 | Aucune |
| 10 | 10 | C10-F01 à C10-F10 |
| 11 | 5 | C11-F01 à C11-F05 |
| 12 | 4 | C12-F01 à C12-F04 |
| **Total** | **110** | **89 préservées + 21 nouvelles dans le manuscrit** |

Les 21 nouvelles comprennent les deux fenêtres des révisions approuvées et les 19 des chapitres 10 à 12. Parmi ces 19, dix existaient déjà en HTML dans la transmission et neuf étaient textuelles.

Cette étape est une **intégration éditoriale avant la seconde passe graphique** : les nouvelles fenêtres utilisent les classes compatibles existantes, sans régression des 89 anciennes. La modernisation détaillée des 21 nouvelles et la vérification du lecteur relèvent de la passe suivante ; aucun résultat visuel final n’est promis par cet audit.

## Continuité contrôlée et limites

- Fin du 9 préservée : Hasol 19, Yoon 24, douze cercles ; 4 Fatal / 4 Arcanique / 4 Gardien, cadeaux paternels rares (bleus), 6★, +6 inchangés.
- 10 : alpha élite 26, coup fatal d’Hasol, niveau 19→20 puis première découverte d’Œil. Ray 22 ; trio 3/5, 35/50, période d’essai et pardon non acquis. Anneau spécialisé remis sans statistique ni capacité chiffrée supplémentaire.
- 11 : niveau 20→21 après combat avec l’anneau, Aimant sans taux affiché. Mur de flammes après Ray 30 ; disponibilité scolaire de Yoon maintenue. Zio rejoint à la fin de ses études : 4/5 et 45/50. La tranche de chasses de Ray 30–40 reste peu détaillée : aucune borne 40 ajoutée artificiellement.
- Dispute, voyage commercial et décès d’Armin sans réconciliation ; cause du décès, destination et origine de l’hostilité envers le Griffon non révélées. Le deuil ne disparaît pas avec la victoire contre le mannequin rare 20, deux touches reçues.
- 12 : responsabilités commerciales partielles, pas reprise totale automatique ; boss 32 et invocations 11, fuite à quatre puis recrutement de Samia commune : 5/5 et 50/50. Retour victorieux après interruption du mécanisme ; coup fatal d’Hasol, aucun gain de cercle inventé. Samia ouvre le coffre avec ses outils.
- Pas de Main runique ou de détection des pièges par Œil débloquée au recrutement. Les premiers échanges d’apprentissage présents dans la transmission ne sont pas transformés en déblocage ; le jalon du chapitre 13 reste futur.
- Réputation et moyens financiers installés vers vingt-cinq ans ; pas d’inventaire personnel intégralement +15 ou de premier sort offensif prématuré.
- **À DÉFINIR :** dates intermédiaires, âges au décès, niveaux non affichés au terme du 12, statistiques naturelles, XP et compteurs détaillés, cercles supplémentaires, inventaires personnels futurs. L’évolution de Résonance au niveau 40 de Yoon reste à suivre sans lui assigner un niveau absent de la source.

## Preuves de préservation et reprise

Contrôles éditoriaux exécutés avant la passe graphique :

1. Comparaison des 89 blocs de fenêtres antérieurs : **89/89 identiques octet pour octet**, dans le même ordre.
2. Comparaison des segments 5 à 8 : **strictement identiques**. Segment 9 antérieur conservé intégralement, jusqu’à son saut de ligne final ; seule la séparation précédant le nouveau 10 est ajoutée après lui.
3. Comparaison hors fenêtres des quatre révisions approuvées au manuscrit : **quatre narrations conformes**. Corps des quatre archives préservés intégralement ; seuls leurs en-têtes ont changé.
4. Présence unique des titres et ancres 1 à 12, absence de chapitre 13, absence de courriels/commentaires de ChatGPT/images dans les nouvelles tranches : vérifiée.
5. Hachages de `new.txt` et `old.txt` avant/après : identiques. Les sources restent intactes.

Instantanés et contrôles de session : `/tmp/opencode/arcaniste-import-1-12/` (`avant/`, `archives.sha256`, `corrections.json`, `source-transformee.json`, `controles.json`, patch d’import). Ces fichiers temporaires facilitent la reprise locale ; ils ne constituent pas un archivage durable versionné.

`git diff --check` ne signale aucun défaut dans `roman.md`. Pour les archives, Git signale la ligne vide finale de `chap4_revision.md` ; elle est volontairement préservée, identique à l’instantané antérieur à cet import, pour respecter le périmètre « en-têtes seulement ».

Aucune suite de tests applicatifs ou validation de rendu n’est revendiquée ici. Aucun changement de script, CSS, test, lore, guide d’agent ou README par ce sous-travail ; ces fichiers relèvent des autres intervenants de la session. Aucun commit, push ou déploiement.
