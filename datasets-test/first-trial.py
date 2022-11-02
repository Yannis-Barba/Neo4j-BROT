from py2neo import *
import pandas as pd
from pandas import DataFrame

# Connexion au graphe
graph = Graph("bolt://localhost:7687", auth=("neo4j", "root"))

# petit nettoyage de la base avant de commencer
graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")

df = pd.read_csv("./datasets-test/BROT2_dat.csv", delimiter=",")
