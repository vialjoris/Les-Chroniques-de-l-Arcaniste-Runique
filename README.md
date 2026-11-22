# Les Chroniques de l’Arcaniste Runique

![Un couple en tenues de fantasy se tient la main dans une cour fleurie.](references-visuelles/hasol%20shun/couple.png)

**Auteur : Joris VIAL.**

Projet de roman de fantasy LitRPG en **trilogie**. Les livres I et II comportent chacun seize chapitres ; le découpage détaillé du livre II et le nombre de chapitres du livre III restent à définir.

## Documents de référence

- [`roman.md`](roman.md) : manuscrit unique ; chaque chapitre conserve son statut de validation propre.
- [`PLAN_DIRECTEUR.md`](PLAN_DIRECTEUR.md) : plan narratif, jalons validés et questions ouvertes.
- [`lore/decisions.md`](lore/decisions.md) : décisions de l’auteur et limites de leur validation.
- [`lore/personnages.md`](lore/personnages.md) : fiches, compétences et historique des personnages.
- [`lore/systeme.md`](lore/systeme.md) : règles LitRPG, Mana, cercles et compétences.
- [`lore/runes.md`](lore/runes.md) : inventaire runique et historique.
- [`lore/chronologie.md`](lore/chronologie.md) : événements racontés et jalons futurs, séparés.
- [`lore/pistes.md`](lore/pistes.md) : propositions non validées, dont les courbes de cercles envisagées.
- [`source.md`](source.md) : provenance des inspirations et limites de transposition.
- [`AGENTS.md`](AGENTS.md) : consignes éditoriales et contrôles avant rédaction.
- [`style.css`](style.css) : présentation des fenêtres HTML du système.

## Statuts éditoriaux

**CANON** : validé par l’auteur. **PROPOSITION** : non approuvé. **À DÉFINIR** : information manquante ou arbitrage attendu. **CONTRADICTION** : incompatibilité à résoudre.

Les fiches au niveau 60 ne remplacent pas les états de fin de livre I. Un nombre de cercles disponibles ne signifie pas autant de runes équipées. Les courbes proposées ne sont pas des gains automatiques par niveau.

## Préparation des chapitres

### Lire le manuscrit avec sa présentation locale

Ouvrir [`lecture.html`](lecture.html) dans un navigateur, en conservant [`style.css`](style.css) à côté : la feuille n’est pas copiée dans le lecteur. `roman.md` reste la source unique ; le lecteur est un dérivé à régénérer, jamais à modifier manuellement. Le rendu Markdown de GitHub ne garantit pas cette présentation.

Depuis la racine, avec Python 3 et `venv` disponibles :

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-lecture.txt
python3 scripts/generer_lecture.py
python3 scripts/generer_lecture.py --check
python3 -m unittest discover -s tests -v
```

La génération fonctionne hors ligne après installation de la dépendance ; lire le HTML déjà généré ne nécessite ni Python ni serveur. **Contrôle du 22 novembre 2026 : 110 fenêtres modernisées sur les douze chapitres, lecteur régénéré et 20 tests réussis.** Le rendu a été contrôlé avec Chromium à 1280, 390 et 320 pixels, y compris par ouverture locale sans réseau. Voir le [guide des modèles et du lecteur](docs/fenetres_litrpg.md) et l’[audit de refonte](docs/audit_refonte_fenetres.md) pour les modèles, preuves, options, sécurité, impression et limites EPUB.

Consulter le plan et les références avant toute rédaction. Vérifier notamment les disponibilités réelles du groupe, les compétences accessibles au niveau de chaque personnage, les cercles, l’équipement, les réserves disponibles et les secrets connus. Les décisions récentes et la fiche de contrôle détaillée figurent dans `AGENTS.md` et `PLAN_DIRECTEUR.md`.

`old.txt` et `new.txt` sont des traces de provenance, pas des manuscrits concurrents. Les conserver intacts et contrôler les versions avant toute intégration. Une mise à jour documentaire n’autorise ni rédaction de chapitre, ni révision d’un texte validé, ni publication Git.

### Révisions de lecture séparées

Les quatre révisions `chap1_revision.md` à `chap4_revision.md` sont **validées sans les repères du lore en début/fin** (DEC-101) et intégrées (DEC-102). Leurs narrations étaient déjà celles du manuscrit ; seules les deux fenêtres C3-F01/C4-F01 manquaient, désormais ajoutées sans écraser la présentation modernisée. Copies conservées comme provenance, pas comme un second manuscrit. Voir l’[audit d’import 1–12](docs/integration_chapitres_1_12.md) et l’[historique des fenêtres 1–4](lore/audit_fenetres_1_4.md).

Les chapitres 5 à 9 ont été validés par l'auteur dans la transmission mobile et la session du 21 novembre 2026 ; leur intégration et les retouches techniques ciblées sont suivies dans [`lore/audit_chapitres_5_9.md`](lore/audit_chapitres_5_9.md). Aucun chapitre 10 n'est autorisé par cet import.

### Dernière transmission contrôlée — 22 novembre 2026

`roman.md` comporte **douze chapitres** : 1–4 révisions validées, 5–9 validés préservés, **10 V2, 11 et 12 intégrés en lecture sans validation littéraire globale** (DEC-102). Aucune rédaction du 13. Les blocages techniques sont levés par DEC-097 à DEC-100 ; les classes proposées des vies futures restent non validées. Preuves et limites : [audit d’import 1–12](docs/integration_chapitres_1_12.md) ; [audit de réception historique](lore/audit_transmission_chapitres_10_12.md).

En fin du 12, Hasol vient d’avoir **vingt-cinq ans**, est une artisane reconnue et dispose de moyens financiers importants. Armin est mort au 11 sans cause révélée ni réconciliation ; Hasol reprend une partie de ses activités commerciales. Le groupe compte cinq membres avec Samia (**50/50 points**). Niveaux finaux, caractéristiques naturelles, XP, cercles finaux et inventaires détaillés restent **À DÉFINIR** ; les fiches au niveau 60 ne sont pas les états actuels.

Les encadrés éditoriaux de lore en début et fin de chapitre sont retirés (DEC-091), sans supprimer les vraies fenêtres du système. Une partie de lore consultable en fin de livre reste à définir. L’inspiration visuelle du design des personnages d’*Epic Seven* est déclarée dans [`source.md`](source.md).

**Roman non illustré — DEC-101 :** l’ajout d’image au chapitre 1 est annulé ; les illustrations sont destinées au manhwa. L’image du couple ci-dessus reste une présentation du projet, hors manuscrit. Les fenêtres HTML du système et leurs pictogrammes ne sont pas supprimés.

## Droits d’auteur

© 2026 Joris VIAL — Tous droits réservés.

Voir la [notice de droits d’auteur](COPYRIGHT.md) pour les textes originaux du projet et la réserve relative aux droits des tiers. Cette notice n’est pas une licence ouverte.
