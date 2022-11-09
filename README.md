# Neo4j-BROT

Neo4j Project about mediteranean plants traits

### Contexte

Pour ce projet visant à travailler avec une base de données sous forme de graphe avec neo4j, j'ai souhaité mettre à profit cette technologie dans le domaine de l'écologie (étude des populations et des écosystèmes).

Au cours de mes recherches, j'ai découvert une base de données recensant un grand nombre d'espèce méditérranénnes ainsi que leur traits. Les traits étant des charactéristiques phénotypiques, génétiques ou morphologiques d'un organisme (1). Les auteurs de cette base de données sont Çağatay Tavşanoğlu & Juli G. Pausas. Ils ont référencé 2457 taxons méditérranéens et un total de 44 traits, pour obtenir au final 25 764 individus, un individu étant la mesure d'un trait pour un taxon donné (tous les traits ne sont pas recensés pour chaque taxons).
Les auteurs ont rédigé un article (2) accompagnant cette base de données afin d'apporter des compléments d'informations qui m'ont été fort utiles pour comprendre les données.

Cette base de données a été constituée de plusieurs manières notamment grâce à des références bibliographiques et des observations expérimentales. Ainsi, pour chaque paire taxon-trait observé, donc pour chaque ligne, il y a également une source bibliographique.

La base de données est composée en 4 fichiers csv :

- BROT2_dat.csv (toutes les paires taxon-trait observé)
- BROT2_sou.csv (toutes les sources)
- BROT2_tax.csv (toutes les informations supplémentaires sur les taxons)
- BROT2_syn.csv (tous les synonymes des taxons)

J'ai également décidé de créer un fichier **traits.csv**, permettant d'avoir le nom complet d'un trait et des explications le concernant. Ces informations sont disponibles dans l'article sur lequel j'ai basé mon projet. J'ai décidé de créer ce fichier afin d'avoir l'information directement dans le résultat de mes requêtes et ne pas avoir à me référer systématiquement à l'article pour analyser mes résultats.

## Problématique

A partir de ce jeu de données, les problématiques possibles sont très nombreuses. D'après l'article ce type de base de données (sur les traits) est très prometteur pour les biologistes afin de comprendre la répartition de populations et la formation d'écosystèmes.

Une base de donnée sous forme de graphe semble tout à fait adaptée, puisqu'elle permet de visualiser assez aisément les appartenances des taxons aux différentes familles, les taxons possédant tel ou tel trait etc. Par ailleurs au cours de mes recherhces, j'ai pu constater que les bases de données de traits étaient souvent sous forme de graphe.

Les sujets de réflexions étant vastes, j'ai décidé de me concentrer sur certaines questions que je me suis posé au premier abord en lisant l'article.

Dans un premier temps, comme l'auteur a identifié des traits en lien avec la résillience des plantes au incendie, j'ai décidé de me concentrer sur l'étude de ces traits. En effet, la présence du feu en méditérranée a eu un impact sur le développement des populations y compris végétales. Certaines espèces ont développé des traits traduisant une adaptation à cette pression environnementale particulière.

Je me suis donc demandé si l'on pouvait identifier un pattern de plantes adpatées à la présence du feu en méditérranée. Comme nous allons le voir par la suite, certains traits sont des mesures directes de l'adaptation aux incendies. Mais je voulais savoir si parmis les plantes qui possèdent ces traits, nous pouvions mettre en évidence d'autres traits qui ne serait pas directement associés à l'adaptation au feu.

## Arborescence du projet

- un fichier **_BROT_Neo4j.ipynb_** pour les analyses et le déroulé du projet

- un pdf du fichier précédent (**_BROT_Neo4j.pdf_**)

- Un Dossier **datasets-tests** avec l'ensemble des fichiers cités dans le contexte

- Un fichier **_db_create.py_** pour créer la base de données

- un fichier **_db_request.py_** pour certains fonctions de requêtes de bases

- Le PDF de l'article utilisé pour ce projet
