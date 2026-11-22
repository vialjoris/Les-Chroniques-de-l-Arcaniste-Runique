# Chapitre 13 — Continuité et suivi éditorial

## Autorisation et statut

22 novembre 2026 : « go » explicite de l’auteur après questionnaire et synthèse,
transmis dans la mission de rédaction. DEC-105 consigne les choix nouveaux
(DEC-104, ajouté pendant le travail, concerne les références visuelles).
Chapitre rédigé sur autorisation, **version de lecture non validée littérairement**.
Les chapitres 1–9 restent validés ; 10–12 restent en lecture. Aucun chapitre 14 autorisé.

## Fiche de continuité préparée avant rédaction

- **Départ :** fin du 12, quelques jours après les vingt-cinq ans d’Hasol ;
  prochaine expédition dans dix jours. Confiance avec Zio, pas encore couple déclaré.
- **Période :** premières semaines après le 12, puis scènes espacées sur plusieurs
  années jusqu’au mariage vers vingt-huit ans et à son quotidien immédiat.
- **Personnages :** groupe de cinq, 50/50 points ; Iseria et Orven. Samia amie et
  spécialiste autonome, Yoon sœur de Zio et meilleure amie de Samia ; Ray engagé
  par choix, sans effacement de sa responsabilité passée.
- **Scènes obligatoires :** préparation et mission ; jalousie d’Hasol devant les
  attentions de Samia ; reconnaissance de ses sentiments ; Samia renonce sans
  rivalité prolongée et soutient Zio ; premier pas et déclaration du Gardien ;
  confidence sur le coup de foudre secret à l’Académie ; apprentissage long,
  artisanat et responsabilités ; mariage intime ; vie commune apaisée.
- **Émotions :** peur de mal lire les autres, désir, vulnérabilité réciproque,
  amitié préservée, bonheur construit sans effacement du deuil d’Armin.
- **Combat :** mission collective ; limites de placement et de Mana de Ray,
  contrôle posé de Yoon, bouclier de Zio, autonomie tactique de Samia ; Hasol à
  l’épée, pas de premier sort offensif. Aucun boss numéroté ni centième acquis.
- **Transmission :** observation et mécanismes ordinaires avant acquis magiques ;
  même Œil runique conservant la lecture des runes, détection sans désamorçage ;
  Main active d’ouverture des coffres, sans extension universelle aux portes.
- **Données ouvertes :** niveaux/XP/statistiques/cercles/inventaires/réserves non
  chiffrés. Ne pas figer douze cercles après les ellipses, ni importer les fiches
  du 60. Aucun affixe, équipement personnel ou barème nouveau.
- **Secrets :** Hasol apprend le passé sentimental de Zio par ses confidences ;
  pas de romance établie rétroactive, pas de récompense attendue pour l’aide
  d’Académie. Motif du conflit d’Armin et cause de sa mort restent inconnus.
- **Sortie visée :** Hasol et Zio mariés, vie commune heureuse ; Œil/pièges et
  Main/coffres acquis après des années ; groupe complet et Samia pleinement
  présente. Centième boss au 14, sort offensif au 15, aucune anticipation tragique.

## Sources réellement consultées

Guides agents global et local ; `PLAN_DIRECTEUR.md` intégral ; chapitres 10–12
de `roman.md` intégralement ; `lore/systeme.md`, `personnages.md`, `runes.md`,
`chronologie.md`, `decisions.md` ; direction éditoriale DEC-083 conservée dans
`lore/conversation_direction_oeuvre_2026-11-21.md` ; `source.md`, `style.css`,
`docs/fenetres_github.md` et modèles utiles de `docs/fenetres_litrpg.md`.
Pas de nouvel import de `new.txt` ; archives non utilisées et préservées.

## Présentation finalisée dans la session principale

Deux sources HTML nouvelles : `C13-F01` (évolution d’Œil), `C13-F02` (Main).
Enveloppes GitHub et quatre SVG bureau/mobile générés depuis ces sources ;
export `lecture.html` régénéré. Les deux générateurs passent leur contrôle
`--check` : 112 fenêtres et 224 SVG au total, lecteur à jour.
Les exemples de pratique ne définissent pas de conditions universelles de
déblocage, coût, portée, récupération ou garantie d’ouverture.

## Contrôles de rédaction

- À l’issue de l’ajout du 13, **préfixe 1–12 identique octet pour octet** à la
  copie de départ `/tmp/opencode/roman-avant-c13.md`, SHA-256
  `ad1b690d57563906e9654d4c7d5b15c69da07805448e0b6c18d7efb9e98ba123`.
- Environ **10 100 mots**, dix sections, deux fenêtres, aucun chapitre 14 ajouté.
- `git diff --check` sans erreur au contrôle de rédaction. Pas de générateur
  ni de tests techniques lancés par l’agent de rédaction pendant le travail.
- **Travail concurrent distinct :** la session principale a ensuite appliqué
  DEC-106 (portraits 1/3/5 et deux raccords de coiffure dans le 13). Le fichier
  final ne doit donc plus être annoncé identique au préfixe initial : la preuve
  ci-dessus concerne l’opération d’ajout du 13, avant ces retouches autorisées.
  Les modifications de scripts/tests, `source.md`, portraits et dérivés de cette
   autre intervention ne sont pas attribuées à la rédaction du chapitre.

## Vérifications finales de l’intégration

- Relecture de continuité indépendante sur tout le 13 : aucun blocage identifié ;
  élision « lorsqu’Iseria » corrigée dans le nouveau texte.
- Lien du chapitre 13 ajouté au sommaire du manuscrit ; hors ce lien, les seuls
  écarts du préfixe 1–12 sont les quatre portraits/coiffures de DEC-106.
- Les tests acceptent les chapitres ajoutés avec leur ancre, sans renouveler la
  fixture ni les empreintes historiques. Structure et contenu HTML/SVG des deux
  nouvelles fenêtres contrôlés avec les fenêtres existantes.
- Captures Chromium hors ligne contrôlées : Œil en variante mobile et Main en
  variante bureau, textes lisibles et cadres complets. Captures temporaires dans
  `/tmp/opencode/arcaniste-chapitre13/`, sans dépendance du roman à ces preuves.
- La suite historique signale toujours les changements descriptifs de DEC-106 :
  segments narratifs 0, 31 et 40 (le segment 0 inclut aussi le nouveau lien du
  sommaire), et empreinte globale du préfixe. Ces écarts sont
  conservés visibles ; ils ne sont ni corrigés par une réécriture du manuscrit,
  ni masqués par une nouvelle fixture dans cette intervention.
- Dernière exécution : **40 tests, quatre assertions en échec dans deux tests
  historiques**, toutes expliquées par les écarts ci-dessus ; les autres tests
  réussissent. Les deux contrôles de génération `--check` et `git diff --check`
  réussissent. Aucun résultat « suite entièrement verte » revendiqué.
- Archives `new.txt` et `old.txt` préservées ; aucun commit, push ou déploiement.
