# Kata Money Machine — distributeur automatique (version euro)

Construire la logique d'un distributeur automatique qui accepte de l'argent, rend la monnaie, gère son stock et distribue des produits.

> Adapté du kata *Vending Machine* (voir [Source et licence](#source-et-licence)) : les pièces américaines sont remplacées par des pièces en euros.

## Monnaie

| Pièce | Valeur | Acceptée ? |
|---|---|---|
| 1 centime | 0,01 € | ❌ rejetée |
| 2 centimes | 0,02 € | ❌ rejetée |
| 5 centimes | 0,05 € | ❌ rejetée |
| 10 centimes | 0,10 € | ✅ |
| 20 centimes | 0,20 € | ✅ |
| 50 centimes | 0,50 € | ✅ |
| 1 euro | 1,00 € | ✅ |
| 2 euros | 2,00 € | ✅ |

Les montants s'affichent au format français : `0,50 €`, `1,20 €`.

## Produits

| Produit | Prix |
|---|---|
| Cola | 1,00 € |
| Chips | 0,50 € |
| Bonbons | 0,70 € |

## Fonctionnalités

Développez-les une par une, en TDD.

### 1. Accepter les pièces

- La machine accepte les pièces de **10 c, 20 c, 50 c, 1 € et 2 €**.
- Elle rejette les pièces de **1 c, 2 c et 5 c**, qui partent dans le **monnayeur de retour**.
- Chaque pièce valide s'ajoute au montant inséré et l'affichage est mis à jour (ex. `0,30 €`).
- Quand aucune pièce n'a été insérée, l'affichage indique `INSERT COIN`.

### 2. Choisir un produit

- Si le montant inséré est suffisant, le produit est distribué et l'affichage indique `THANK YOU`. Au contrôle suivant de l'affichage, il revient à `INSERT COIN` et le montant est remis à `0,00 €`.
- Si le montant est insuffisant, l'affichage indique `PRICE` suivi du prix du produit (ex. `PRICE 1,00 €`). Au contrôle suivant, il affiche `INSERT COIN` ou le montant déjà inséré, selon le cas.

### 3. Rendre la monnaie

- Si le client a inséré plus que le prix du produit, la différence est placée dans le monnayeur de retour.

### 4. Rendre les pièces

- Quand le client appuie sur le bouton de retour, tout l'argent qu'il a inséré est placé dans le monnayeur de retour et l'affichage indique `INSERT COIN`.

### 5. Épuisé

- Si le produit choisi n'est plus en stock, l'affichage indique `SOLD OUT`. Au contrôle suivant, il affiche le montant restant dans la machine, ou `INSERT COIN` s'il n'y en a pas.

### 6. Monnaie exacte uniquement

- Si la machine n'est plus capable de rendre la monnaie sur un des produits qu'elle vend, elle affiche `EXACT CHANGE ONLY` au lieu de `INSERT COIN`.

## Source et licence

- Kata créé par **Guy Royse** : [guyroyse/vending-machine-kata](https://github.com/guyroyse/vending-machine-kata).
- Description d'origine publiée par [Samman Coaching](https://sammancoaching.org/kata_descriptions/vending_machine.html) sous licence [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Cette adaptation (euros, traduction française) est distribuée sous la même licence CC-BY-SA-4.0.
