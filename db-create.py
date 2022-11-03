#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:30:15 2022

@author: yannis
"""

from py2neo import *
import pandas as pd
from pandas import DataFrame

# Connexion au graphe
graph = Graph("bolt://localhost:7687", auth=("neo4j", "root"))

# petit nettoyage de la base avant de commencer
graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")

#importation des jeux de données


data_df = pd.read_csv("./datasets-test/BROT2_dat.csv", delimiter=",", encoding="ISO-8859-1")

traits_df = pd.read_csv("./datasets-test/traits.csv", delimiter=",", encoding="ISO-8859-1")

taxons_df = pd.read_csv("./datasets-test/BROT2_tax.csv", delimiter=",", encoding="ISO-8859-1")

sources_df = pd.read_csv("./datasets-test/BROT2_sou.csv", delimiter=",", encoding="ISO-8859-1")



### Noeuds TAXONS
"""
Les taxons sont les individus statistiques, pour chaque taxons, il y a plusieurs traits, et chaque trait est une donnée. 

"""
taxonsId = []
taxons = []

for index, row in taxons_df.iterrows():
    taxonsId.append(str(row["ID"]))
    taxons.append(Node("Taxon",
                  id=str(row["ID"]),
                  taxon=str(row["Genus"]+" "+row["Species"]),
                  family=str(row["Family"]),
                  genus=str(row["Genus"]),
                  species=str(row["Species"]),
                  authority1=str(row["Authority1"]),
                  infraname=str(row["Infraname"]),
                  authority2=str(row["Authority2"])
                  ))
 

### Noeuds sources 

sourcesId = []
sources = []

for index, row in sources_df.iterrows():
    sourcesId.append(row["ID"])
    sources.append(Node("Source", 
                        id=str(row["ID"]),
                        fullSource=str(row["FullSource"])
                        ))

### Noeuds traits
"""
j'ai créé la table trait afin de renseigner des informations de la doc. 
"""

traitsName = []
traits = []

for index, row in traits_df.iterrows():
    traitsName.append(row["TraitName"])
    traits.append(Node("Trait",
                  name=str(row["TraitName"]),
                  fullName=str(row["fullName"]),
                  explanation=str(row["explanation"])
                  ))

### Noeuds DATA

"""
Les traits ne sont pas une table à part entière dans le jeu de données de base, mais on extrait tout de même ces noeuds
afin d'avoir une meilleure réprésentation sous forme de graphe et pour pouvoir faciliter les requêtes.
De plus, cela nous permet d'avoir des informations sur le nombre de trait présent. 
"""

data = []

data_traits_rel = []
data_taxons_rel = []
data_sources_rel = []

for index, row in data_df.iterrows():
    data.append(Node("Data",
                                id=str(row['ID']),
                                name=str(row["Data"]+"--" +row["Trait"]),
                                data=str(row["Data"]),
                                taxonId=str(row["TaxonID"]),
                                trait=str(row["Trait"]),                                
                                units=str(row["Units"]),
                                dataType=str(row["DataType"]),
                                method=str(row["Method"]),
                                sourceId=str(row["SourceID"]),
                                region=str(row["Region"]),
                                lat=str(row["Lat"]),
                                long=str(row["Long"]),
                                alt=str(row["Alt"]),
                                accuracy=str(row["Accuracy"]),
                                comments=str(row["Comments"])
                                ))
    
    
    data_traits_rel.append(Relationship(data[index], "TYPE_OF_TRAIT", traits[traitsName.index(str(row["Trait"]))]))
    
    data_taxons_rel.append(Relationship(data[index], "TRAIT_OF_TAXON", taxons[taxonsId.index(str(row["TaxonID"]))]))
    
    data_sources_rel.append(Relationship(data[index], "FROM_SOURCE", sources[sourcesId.index(str(row["SourceID"]))]))

### Commit Nodes

#### Taxons nodes
tx = graph.begin()
for node in taxons:
    tx.create(node)
graph.commit(tx)   

#### Sources Nodes
tx=graph.begin()
for node in sources:
    tx.create(node)
graph.commit(tx)

#### Data Dodes
tx = graph.begin()
for node in data:
    tx.create(node)
graph.commit(tx)

#### Traits Nodes
tx = graph.begin()
for node in traits:
    tx.create(node)
graph.commit(tx)


### Commit Relationship

#### Data and traits relation

tx = graph.begin()
for r in data_traits_rel:
    tx.create(r)
graph.commit(tx)


#### Data and taxons relations

tx = graph.begin()
for r in data_taxons_rel:
    tx.create(r)
graph.commit(tx)


#### Data and sources relations

tx = graph.begin()
for r in data_sources_rel:
    tx.create(r)
graph.commit(tx)