# Jolly Jumper

## Règles

Le but de ce programme et de déterminer si une séquence correspond aux règles suivantes :

* *n* étant le nombre d'éléments de la suite.
* Les valeurs absolues des différences successives des élements doivent faire partie de la suite 1..*n*.
* Toutes les différences successives doivent être uniques.

## Exemples

Entre parenthèses on retrouve les différences

OK => **0** (1) **1** (2) **3** (3) **6**

OK => **0** (3) **-3** (2) **-1** (1) **0**

OK => **40** (2) **42** (1) **41**

KO => **0** (2) **2** (3) **5**

KO => **0** (1) **1** (1) **0**
