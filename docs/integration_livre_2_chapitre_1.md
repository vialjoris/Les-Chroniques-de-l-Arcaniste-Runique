# Livre II — intégration du chapitre 1 validé

## Autorisation et provenance

- **Auteur, session locale du 24 novembre 2026 :** « le chapitres 1 est validé mais tu as des petite modification a faire », puis nouvelle actualisation de `docs/new.txt`.
- **Archive :** 79 583 lignes. La lecture intégrale jusqu’à 77 392 est documentée dans `integration_mobile_2026_11_24.md` ; nouvelle fin lue de 77 380 à 79 583, avec reprise après troncature à 79 198.
- **Version retenue :** chapitre 1 « Une Astrale nommée Hasol », `docs/new.txt:77399–79503`, neuf sections I–IX. « Refait le chapitre » et les titres de conversation ne sont pas de la narration.
- **Correction demandée par l’auteur :** `79505`, Hasol remarque le sourire forcé de sa mère après l’annonce de sa classe et lui demande si tout va bien. Le passage ChatGPT `79510–79575` sert d’appui, sans remplacer inutilement toute la scène validée.
- **Source unique :** `../livre_2_le_vertige_des_vies_oubliees.md`. Aucun chapitre du II ajouté au I ; aucune copie concurrente.

## Fiche de continuité de réception

- **Période :** vie 2, seizième anniversaire d’Hasol et Révélation, puis premiers jours d’Académie et premières chasses extérieures encadrées.
- **Départ :** deux cercles ; niveau 1 à la Révélation ; classe affichée Arcaniste Astral, rang Astral, 25 points ; aucun sort offensif direct. Aucun gain chiffré de niveau, d’XP ou de cercle n’est établi à la fin du chapitre.
- **Compétences :** Bénédiction, Croissance, Œil/pièges, Main/coffres et portes, Aura dès le niveau 1 astral. Le seuil de dix concerne le porteur de l’arme imprégnée, pas l’accès au sort. Aucun coût, équipement ou résultat d’Aura ajouté.
- **Personnages :** parents vivants ; Ray meilleur ami ; Elric mentor, 42 ans/niveau 45/Porte-bouclier commun ; Zéphyr Claire, Ranger niveau 53, enseignant d’exploration et père de Samia ; Samia treize ans, cheveux argentés et deux cercles.
- **Secrets :** Croissance d’abord réservée aux parents, puis confiée par Hasol à Elric et au directeur ; Ray n’est pas informé. Iseria l’apprend ensuite. Son inquiétude au temple ne doit révéler ni parenté cachée ni histoire de la faille.
- **Samia :** deuxième cercle le jour des premiers portails, quatre ans auparavant, donc vers neuf ans ; cheveux devenus argentés pendant la semaine suivante. Ce sont désormais des faits du texte validé, non une adoption générale des anciennes réponses de ChatGPT.
- **Équipe :** chasse extérieure, pas donjon en duo ; aucune formation permanente déduite. Yoon/Samia passent leur Révélation trois ans plus tard, au chapitre 2.
- **Équipement et ressources :** aucune rune individuelle ni amélioration, affixe ou réserve chiffrée transmis ; ne pas recopier les cadeaux ou l’inventaire du I par défaut.
- **Mémoire :** peur résiduelle du cauchemar, pas de souvenir explicite des drames du I. Habitude inexplicable face aux moqueries conservée sans démonstration d’un mécanisme de mémoire.

## Retouches ciblées

1. Bref échange avec Iseria sur son sourire forcé ; affection et fierté sincères, cause de l’inquiétude tue.
2. Âge de Samia explicité et entrée à l’Académie à seize ans, plutôt que « bientôt ».
3. Formulations d’Aura distinguant son activation de l’usage personnel d’une arme imprégnée.
4. Titres Markdown et véritable fenêtre de Révélation en HTML ; aucune statistique ajoutée à la fenêtre.
5. « Petit salon » devient « salon », sans inventer une seconde pièce ni changer la demeure.

**Point ouvert préservé :** le chapitre prépare les chasses de volume et montre des slimes abattus, mais n’accorde aucun palier ni cercle avant le niveau dix. Il ne fixe donc pas à lui seul toutes les conditions d’admissibilité de Croissance avant dix ; pas de formule ou de seuil supplémentaire inventé.

## Limites

Validation littéraire du texte transmis enregistrée ; les retouches locales restent identifiées pour relecture. Aucun chapitre 2 rédigé ou autorisé. L’absence de Ténébria dans ce chapitre n’autorise pas à ajouter une nouvelle scène : ses secrets restent protégés. Les anciens « aucun chapitre II autorisé » décrivent l’état antérieur, sauf pour les chapitres suivants qui restent non autorisés.

Livre I et archive préservés ; empreintes avant intervention :

- Livre I : `1627a10fe2568095b7a1d551bcc5e0c9b73e8fefb987d676c7d7d187a4f102fa`.
- `docs/new.txt` : `f2a87fd8d4887da6252ce2697f3abf20b9b0b34c3ebdcbb02c3c4c9250ce407b`.

**Contrôles finaux :** `python3 -m unittest discover -s tests -v`, **60 tests réussis**, dont six nouveaux contrôles du II (structure, données de Révélation, raccords, contenu passif et dérivés idempotents). Générateur du I : **138 fenêtres/276 SVG à jour**. Fenêtre du II `L2-C1-F01` : HTML intégral et deux SVG générés avec la même fonction `produire`, isolés dans `assets/fenetres-livre-2/` pour ne pas perturber le contrôle du I ; procédure et contrôle sans écriture dans `fenetres_github.md`.

La comparaison des paragraphes avec le texte reçu confirme uniquement les retouches listées et la mise en forme ; les empreintes du I et de l’archive sont identiques avant/après. `git diff --check` réussit hors archive conservée intacte (espace final préexistant à la ligne 77253). Ces contrôles ne constituent pas une validation littéraire des retouches ni une preuve de publication ou de rendu GitHub distant.

**Formulation transmise signalée mais préservée :** « Elle favorisa un instant son imagination. » en section III ; aucune réécriture générale ou correction conjecturale n’a été faite.

Risques éditoriaux : survalidation des commentaires, révélation anticipée, confusion activation/porteur et âge de Samia. Intégration locale, sans publication, secret ni intervention en production ; aucun commit/push.
