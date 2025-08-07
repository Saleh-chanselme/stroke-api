Stroke data project
===================

Ce projet contient les fichiers nécessaires au brief Stroke data - Développement d'une API REST et visualisation.

dgfdgfdhsh

Gestion des valeurs aberrantes (outliers)
Après détection des outliers par la méthode IQR sur les variables age, bmi et avg_glucose_level, nous avons choisi de conserver ces valeurs car elles correspondent à des cas médicaux possibles (ex : personnes très âgées ou très jeunes, patients avec fort taux de glucose).

Aucune suppression ni correction n’a été appliquée pour ne pas biaiser les données. En revanche, pour la transformation des variables, une transformation logarithmique a été appliquée pour réduire l’effet des valeurs extrêmes.

Gestion des valeurs aberrantes (outliers)
Les valeurs extrêmes détectées par la méthode IQR ont été conservées car elles reflètent des cas médicaux plausibles et importants. Pour réduire leur impact dans l’analyse, une transformation logarithmique (log1p) a été appliquée sur certaines variables continues (bmi, avg_glucose_level). Aucune suppression ou correction n’a été effectuée afin de ne pas perdre d’information.

Pourquoi appliquer la transformation log1p même si tu conserves les valeurs aberrantes ?
Les valeurs aberrantes sont conservées dans les données brutes, mais elles peuvent être très extrêmes et rendre la distribution des variables très asymétrique (skewed), c’est-à-dire avec une longue "queue" à droite.

À quoi sert la transformation log1p ?
Elle réduit la skewness (asymétrie) des variables continues en "compressant" les grandes valeurs.

Cela atténue l’impact extrême des valeurs très hautes sans les supprimer.

Elle permet d’avoir une distribution plus "normale" ou symétrique, ce qui est souvent bénéfique pour beaucoup de modèles statistiques ou ML.

Par exemple, une variable très dispersée avec de gros écarts (quelques valeurs très hautes) sera transformée en une variable plus "aplatie".