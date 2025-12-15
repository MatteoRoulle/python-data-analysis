# 📊 Analyse de résultats scolaires en Python

Ce projet propose une **analyse automatique de résultats scolaires** à partir d’un fichier CSV, en utilisant uniquement **Python**

Il a pour objectif de montrer une utilisation concrète de Python pour :

* lire des données structurées,
* effectuer des calculs statistiques simples,
* automatiser la génération d’un rapport clair et lisible.

---

## 🎯 Objectifs du projet

* Lire un fichier CSV contenant les notes d’élèves
* Calculer :

  * la moyenne en Maths
  * la moyenne en NSI
  * la moyenne générale par élève
    
* Identifier :

  * le meilleur élève
  * la matière la plus réussie
* Générer automatiquement un **rapport**

---

## 📄 Format des données

Le fichier `data.csv` contient les notes sous la forme suivante :

```csv
nom,maths,nsi
Galois,13,16
Gauss,19,12
Euler,19,15
Bachi,17,8
Prag,14,12
Oce,19,15
```

Chaque ligne correspond à un élève avec ses notes en Maths et en NSI.

---

## ⚙️ Fonctionnement du script

Le script `analysis.py` est structuré en plusieurs étapes :

1. **Lecture des données** avec le module `csv`
2. **Transformation des notes** en valeurs numériques
3. **Calcul des statistiques** (moyennes, meilleur élève)
4. **Génération automatique d’un rapport**

---

## ▶️ Lancer le projet

Python 3.0 ou plus récent installé

### Exécution

Depuis le fichier principal du projet :

```bash
python analysis.py
```

Une fois le script exécuté, un fichier `rapport.txt` est généré.

---

## 📄 Exemple de rapport généré

```
RAPPORT D'ANALYSE DES RESULTATS
-----------------------------------

Moyenne en Maths : 16.83
Moyenne en NSI   : 13.00

Moyenne générale par élève :
- Galois : 14.50
- Gauss : 15.50
- Euler : 17.00
- Bachi : 12.50
- Prag : 13.00
- Oce : 17.00

Meilleur élève : Euler (17.00)
Matière la plus réussie : Maths
```
