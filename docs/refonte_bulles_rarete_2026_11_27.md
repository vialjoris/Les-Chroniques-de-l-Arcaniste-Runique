# Bulles de rareté — accord du 27 novembre 2026

## Sources et statut

- **CANON graphique :** demande ciblée de l’auteur dans
  `docs/conversation/27_11_2026.txt:5655–6345`, puis GO explicite pour son application
  aux fenêtres des livres I et II. L’extension aux classes et la précision
  « astral violet » remplacent la première proposition limitée aux runes.
- Les réponses de conversation ne sont pas toutes des décisions : leurs valeurs
  d’exemple et leurs suggestions d’identité ne remplacent pas les références.
- Les archives consultées sont actuellement sous `docs/conversation/`. Cette note
  ne déplace aucun fichier, ne réécrit aucune provenance historique et n’effectue
  pas d’import global de la conversation.

## Contrat de présentation

La bulle arrondie ne contient que le nom d’ensemble de rune ou le nom de classe.
Le fond indique la rareté dans le rendu compact :

| Domaine | Correspondance |
|---|---|
| Runes | Commune : blanc ; peu commune : vert ; rare : bleu ; épique : violet ; légendaire : orange |
| Classes | Commune : blanc ; rare : bleu ; légendaire : orange ; astrale : violet |

Texte sombre et fine bordure grise pour le blanc ; texte blanc sur vert, bleu
et violet ; texte contrasté sur orange. Réutiliser la palette du projet, avec
contrastes à mesurer. Centraliser les styles et leur rendu SVG pour éviter une
présentation différente selon le chapitre ou le livre.

Retirer seulement du rendu compact les mentions redondantes de rareté/couleur
et les champs de grade. Conserver explicitement la rareté dans les référentiels,
les métadonnées et l’alternative accessible/transcription sans dépendance à la
couleur, y compris sur GitHub qui filtre les styles et certains attributs.
Les gabarits de `fenetres_litrpg.md` sont des contrats de présentation, pas une
preuve de prise en charge technique de chaque attribut par chaque moteur.

Cette convention remplace l’ancienne obligation d’écrire « rare (bleue) » dans
chaque fenêtre compacte, pas les explications narratives ni les données sources.
Les étoiles, améliorations, principales, secondaires, valeurs, états, provenances,
couleurs de bonus et associations sont inchangés. `data-window-id` et
`data-rune-id` restent stables et invisibles ; aucun identifiant documentaire
dans le texte visible, la transcription ou les SVG.

## Périmètre et exclusions

Traiter toutes les fenêtres concernées des deux manuscrits : identification,
obtention, expériences, comparaisons, améliorations, inventaires, équipements,
récapitulatifs de cercles présentant des runes ; Révélation, statut, fiches,
groupes/raids et progression présentant des classes. Appliquer la même convention
aux futures fenêtres, sans autoriser leur rédaction.

Préserver les données au moment et dans la vie racontés. Samia reste Éclaireuse
commune au I et Marcheuse du voile commune au II : bulles blanches dans les deux
cas. Ses cheveux argentés ne changent pas la rareté de sa classe. Ne pas modifier
les noms de classes du III dans ce lot graphique. « Marcheuse Astrale » est un
nom donné directement par l’auteur (`docs/conversation/27_11_2026.txt:43`) ; sa
synchronisation documentaire relève d’un travail séparé.

Aucun ajout de règle LitRPG, aucune acquisition ou évolution de classe, aucun
changement de points de groupe/raid, aucune scène nouvelle et aucune réécriture
hors fenêtres. La rareté reste fixe pendant une amélioration ordinaire ; le
pouvoir distinct Savoir runique ne reçoit aucune modification par ce lot.
Aucun commit, push ou déploiement n’est autorisé par cette note.

## Iseria : accord de principe, fiche non réalisée

**Accord présent de l’auteur :** un indice peut être destiné au lecteur du
livre II seulement, sous forme d’une **fiche éditoriale**, et non d’une fenêtre du
Système vue par Hasol. Le fond violet doit contraster avec sa déclaration Rare.
Cela n’apprend rien à Hasol. Les nouveaux arbitrages de fond sur Iseria sont des
déclarations directes de l’auteur (`docs/conversation/27_11_2026.txt:5104,5145,5188`),
et non de simples propositions d’assistant. Leur synchronisation dans le lore
reste un travail séparé, hors lot graphique ; ils ne doivent pas provoquer une
recoloration globale des fenêtres présentant les informations connues des
personnages.

**À DÉFINIR :** nom exact, contenu et placement. Un emplacement autour des cadeaux
écarlates est envisagé, pas fixé. Ne créer aucune fiche dans ce lot, ne modifier
ni scène ni fenêtre du livre I pour cet indice, ne changer aucune identité du
lore et ne dévoiler aucun secret supplémentaire. L’autorisation d’un indice ne
vaut pas validation de sa réalisation ni des informations qu’il contiendrait.

## Plan de contrôles avant clôture de l’intégration

1. Comparer les données avant/après par fenêtre et par rune : identifiants,
   rareté, étoiles, amélioration, affixes et valeurs, états et provenance ; pour
   les classes, nom, rareté, vie, compétences et points. Distinguer les suppressions
   de libellés autorisées d’une perte d’information.
2. Vérifier l’identité et la position des fenêtres, ainsi que la conservation
   des segments narratifs hors fenêtres et des explications de rareté.
3. Régénérer les SVG des deux livres et les exports concernés depuis leurs
   sources, puis lancer leurs contrôles `--check` et les tests. Les commandes
   et répertoires propres à chaque livre figurent dans `fenetres_github.md`.
4. Examiner les cinq couleurs de rune et les quatre couleurs de classe sur
   bureau/mobile, notamment bulles blanches, noms longs, inventaires denses,
   retours à la ligne, zoom et contraste mesuré. Ne pas confondre un test de
   génération réussi avec une revue visuelle ou une conformité RGAA complète.
5. Contrôler au clavier et avec un lecteur d’écran les alternatives et la
   transcription sans couleur ; vérifier le repli après filtrage GitHub et à
   l’impression. Les seules métadonnées ou une infobulle ne suffisent pas.
6. Vérifier Samia blanche au II, l’absence de fiche/indice Iseria créé par ce
   lot et l’absence d’identifiants documentaires visibles dans tous les dérivés.
7. Rapporter les commandes, résultats, preuves et limites réels. Ne pas renouveler
   les fixtures simplement pour faire disparaître un échec.

**État de cette note :** conventions et plan de contrôle documentés. Aucun
résultat de régénération, de test, de contraste ou de rendu de cette refonte
n’est attesté ici ; ces résultats relèvent du compte rendu d’intégration.

## Risques de maintenance

- **Accessibilité :** perte de rareté en lecture sans couleur si le repli n’est
  pas explicite ; contrôle impératif sur le HTML réellement filtré.
- **Sécurité :** conserver SVG locaux sans script, ressource distante ou
  `foreignObject` ; cette refonte ne nécessite ni secret ni service externe.
- **Performance :** surveiller poids et temps de rendu des grands inventaires,
  sans promettre de gain non mesuré ni ajouter une dépendance distante.
- **Exploitabilité :** conserver une source HTML unique par fenêtre et régénérer
  les dérivés ; ne jamais corriger une statistique directement dans une image.
