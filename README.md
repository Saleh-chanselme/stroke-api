Stroke data project
===================
## Prétraitement des données

### Étapes réalisées :
- Chargement du dataset.
- Imputation des valeurs manquantes pour la colonne `bmi` avec la moyenne.
- Détection des valeurs aberrantes à l’aide de l’IQR pour les colonnes `age`, `bmi`, et `avg_glucose_level`.
- Application de la transformation `log1p` sur `bmi` et `avg_glucose_level` pour réduire l’impact des outliers sans les supprimer.

### Traitement des valeurs manquantes :
- La colonne `bmi` contenait 201 valeurs manquantes. Celles-ci ont été remplacées par la moyenne.
- La colonne `smoking_status` contenait des valeurs manquantes catégorielles. Elle n’a pas été imputée à ce stade.

### Valeurs raisonnables (outliers) :
- Les bornes ont été définies à l’aide de la méthode des IQR (Interquartile Range) :
    - `age`: [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
    - `bmi`: idem
    - `avg_glucose_level`: idem

### Choix pour les valeurs aberrantes :
- Les outliers ont été **conservés** dans le dataset.
Justification :  Gestion des valeurs aberrantes (outliers)
Les valeurs extrêmes détectées par la méthode IQR ont été conservées car elles reflètent des cas médicaux plausibles et importants. Pour réduire leur impact dans l’analyse, une transformation logarithmique (log1p) a été appliquée sur certaines variables continues (bmi, avg_glucose_level). Aucune suppression ou correction n’a été effectuée afin de ne pas perdre d’information.

- Pour atténuer leur effet, une **transformation logarithmique** `log1p` a été appliquée sur `bmi` et `avg_glucose_level`.
Pourquoi appliquer la transformation log1p même si tu conserves les valeurs aberrantes ?
Les valeurs aberrantes sont conservées dans les données brutes, mais elles peuvent être très extrêmes et rendre la distribution des variables très asymétrique (skewed), c’est-à-dire avec une longue "queue" à droite.

À quoi sert la transformation log1p ?
Elle réduit la skewness (asymétrie) des variables continues en "compressant" les grandes valeurs.

Cela atténue l’impact extrême des valeurs très hautes sans les supprimer.

Elle permet d’avoir une distribution plus "normale" ou symétrique, ce qui est souvent bénéfique pour beaucoup de modèles statistiques ou ML.

Par exemple, une variable très dispersée avec de gros écarts (quelques valeurs très hautes) sera transformée en une variable plus "aplatie".


## Format Parquet

### Différences avec CSV :
- Parquet est un format **binaire** (pas lisible en texte brut) alors que CSV est un format **texte**.
- Parquet est **colonnaire**, ce qui permet de ne charger que certaines colonnes, tandis que CSV est ligne par ligne.
- Parquet **garde les types de données** (int, float…) tandis que CSV peut tout convertir en texte.

### Avantages et cas d’utilisation :
- Recommandé pour les gros volumes de données (Big Data).
- Très utilisé avec des outils comme Spark, Hive, ou pandas.
- Idéal pour les cas où l’on souhaite faire des **requêtes rapides** sur des colonnes précises ou stocker efficacement.

### Sources :
- [Pandas documentation - to_parquet](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html)
- [Apache Parquet Official Site](https://parquet.apache.org/)


Ce projet contient les fichiers nécessaires au brief Stroke data - Développement d'une API REST et visualisation.

