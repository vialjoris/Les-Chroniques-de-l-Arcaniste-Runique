# Intégration locale du livre II — chapitre 3 et progression de Yoon

## Source et périmètre

- Texte retenu : `docs/new.txt:120757–122581`, dernière version validée de **« Celle qui n’était pas dans les bois »**.
- Structure : 18 sections ; fin conservée à **12 DONG + 2 DING**.
- Exclusions : notes à partir de `122583`, variantes antérieures, chapitre 4 et illustrations narratives.
- Archive préservée dans son état utilisateur : SHA-256 avant/après à contrôler contre `5991a4ec49d20877596246c4a50c31c84490bda5cb293f5fc798b076cfb51975`.

## Raccords appliqués

- Samia : Éclaireuse commune au I ; Marcheuse du voile commune au II ; progression détaillée dans `lore/systeme.md`. Cheveux argentés raccourcis au chapitre 3, yeux bleus.
- Croissance : boss de donjon et de portail dans les vies astrales seulement ; compteur des démons sans condition de niveau. Le I reste limité aux boss de donjon.
- Œil : résultat final exact si +15 est atteint, sans garantie de réussite de la tentative.
- Bénédiction : notifications « Passif amélioré » aux niveaux 20 et 30 ; taux réels conservés dans le lore mais inconnus d’Hasol.
- Siphon : 120 % PA, 75 % des dégâts rendus en Mana, 8 m, 100 Mana, 20 s, plafond 1 200.
- XP : exigence supérieure qualitative avec la rareté de classe, sans table.
- Alpha : deux frappes, aucun niveau, PV ou dégât ajouté.
- Chapitre 2 : recommandation des gobelins rouges niveau 11 ajoutée autour des compteurs/raids.
- Yoon — DEC-185/186 : fiche initiale/Vague légendaire enrichies dans `L2-C2-F08` ; Sceau de lucidité au 10, Domaine des Entraves runiques au 20 et Marque runique au 30 dans le chapitre 2 ; évolution de Résonance runique acquise et démontrée au 40 dans le chapitre 3, sous le même nom. Tempête runique 50 et Convergence runique 60 restent dans le lore, sans scène anticipée.

## Runes et fenêtres

- Instantané raconté : 32/32 runes +15, composition 8 Vol de vie / 8 Arcanique / 8 Vitesse / 2 Énergie / 2 Gardien / 4 Fatal, neuf activations.
- Cadeaux paternels de vie 2 conservés ; anciennes Vol de vie 4★ remplacées par des exemplaires 5★/6★ distincts. Fiches complètes dans `lore/runes.md`, transitions dans `lore/personnages.md`.
- Réserve de 500 pierres : lot consommable non individualisé, sans 500 fiches artificielles.
- Fenêtres Yoon : `L2-C2-F08` modifiée ; `L2-C2-F12`, `F13`, `F14` et `L2-C3-F06` ajoutées. Le chapitre 3 compte désormais **6 fenêtres**. Total éditorial du livre II : **26 fenêtres et 26 IDs uniques**.
- Dérivés régénérés depuis les sources : **153 fenêtres/306 SVG** pour le I et **26 fenêtres/52 SVG** pour le II. Les contrôles sans écriture confirment que les deux inventaires et le lecteur local sont à jour.

## Commandes de contrôle

```sh
python3 scripts/generer_fenetres.py --check
python3 scripts/generer_fenetres.py \
  --input livre_2_le_vertige_des_vies_oubliees.md \
  --output-dir assets/fenetres-livre-2 \
  --asset-prefix assets/fenetres-livre-2 \
  --check
python3 scripts/generer_lecture.py --check
```

Contrôler avant livraison : trois chapitres et 18 sections au chapitre 3, absence de chapitre 4, 26 IDs de fenêtres uniques, correspondance des 32 IDs de runes, archive et visuels inchangés. La suite complète compte **90 tests réussis** après adaptation des contrats.

## Limites conservées

Caractéristiques naturelles et XP chiffrée d’Hasol au niveau 40, propriétés chiffrées des armes offertes, détails des 500 pierres, niveau/PV de l’alpha, dégâts des frappes et paramètres explicitement ouverts des compétences restent **À DÉFINIR**. Pour Yoon : coût/durée/réduction/portée/recharge du Sceau, paramètres du Domaine et de Marque runique, amplification de Résonance runique après son évolution, paramètres de Tempête runique et modalités/cumul de Convergence runique.
