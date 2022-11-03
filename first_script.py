from py2neo import *
import pandas as pd
from pandas import DataFrame

# Connexion au graphe
graph = Graph("bolt://localhost:7687", auth=("neo4j", "root"))

# petit nettoyage de la base avant de commencer
graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")

#importation des jeux de données


traits_df = pd.read_csv("./datasets-test/BROT2_dat.csv", delimiter=",", encoding="ISO-8859-1")

taxons_df = pd.read_csv("./datasets-test/BROT2_tax.csv", delimiter=",", encoding="latin-1")

sources_df = pd.read_csv("./datasets-test/BROT2_sou.csv", delimiter=",", encoding="latin-1")


# création des premiières tables

#table traits

data = []

traitsName = []
traits = []

taxonsId = []
taxons = []

sourcesId = []
sources = []

rel = []

for index, row in traits_df.iterrows():
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
                                accuracy=str(row["Accuracy"]),
                                comments=str(row["Comments"])
                                ))
    
    if(row["Trait"] not in traitsName):
        traitsName.append(row["Trait"])
        traits.append(Node("Trait",
                            name=str(row["Trait"]), 
                            ))
    rel.append(Relationship(data[index], "TYPE_OF_TRAIT", traits[traitsName.index(row["Trait"])]))
    
    
    if(row["TaxonID"] not in taxonsId):
        tax = taxons_df[taxons_df["ID"] == row["TaxonID"]]
        taxonsId.append(row["TaxonID"])
        taxons.append(Node("Taxon",
                           family=str(tax["Family"]),
                           genus=str(tax["Genus"]),
                           species=str(tax["Species"]),
                           name=str(row["Taxon"]),
                           id=str(row["TaxonID"]),                           
                           region=str(row["Region"]),
                           lat=str(row["Lat"]),
                           long=str(row["Long"]),
                           alt=str(row["Alt"]),
                           ))
    rel.append(Relationship(data[index], "TRAIT_OF_TAXON", taxons[taxonsId.index(row["TaxonID"])]))
    
    if(row["SourceID"] not in sourcesId):
        sourcesId.append(row["SourceID"])
        src = sources_df[sources_df["ID"] == row["SourceID"]]
        sources.append(Node("Source",
                            id=str(row["SourceID"]),
                            source=src["FullSource"]
                            ))
    rel.append(Relationship(data[index], "SOURCE", sources[sourcesId.index(row["SourceID"])]))
   
tx = graph.begin()
for node in data[0:100]:
    tx.create(node)
graph.commit(tx)

tx = graph.begin()
for node in traits:
    tx.create(node)
graph.commit(tx)

tx = graph.begin()
for node in taxons[0:100]:
    tx.create(node)
graph.commit(tx)

tx = graph.begin()
for node in sources:
    tx.create(node)
graph.commit(tx)

tx = graph.begin()
for r in rel[0:100]:
    tx.create(r)
graph.commit(tx)


# table traitType
# si besoin ultérieurement, compléter avec le nom complet issu de la doc: len(traitType) = 44

# traitType = [Node("TraitType", traitType = i) for i in pd.unique(traits_df["TraitType"])]


# tx_type = graph.begin()
# for node in traitType:
#     tx_type.create(node)
# graph.commit(tx_type)




# Relation between trait and traitType







