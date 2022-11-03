#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:30:42 2022

@author: yannis
"""

from pandas import DataFrame
from py2neo import *
import matplotlib.pyplot as plt


# connexion au graphe
graph = Graph("bolt://localhost:7687", auth=("neo4j", "root"))

## Basic request 

### Get all data

rq_data = "MATCH (d:Data) return d"
data_rq = graph.run(rq_data).to_data_frame()
print(data_rq.head())
print(f"number of data : {data_rq.shape[0]}")

### Get all traits from a taxon

def allTraitsOfTaxon(taxon):
    rq = '''match(d:Data)-[:TRAIT_OF_TAXON]->(t:Taxon {taxon: $taxon}) 
        return d.trait as trait, 
               d.data as data,
               t.family as famille,
               t.genus as genre,
               t.species as espece
    '''
    return graph.run(rq, taxon=taxon).to_data_frame()

allTraits = allTraitsOfTaxon('Acanthus spinosus')
 

### Get all sources for a specific taxon

def allSourcesOfTaxon(taxon):
    rq = '''match(t:Taxon {taxon:$taxon})<-[:TRAIT_OF_TAXON]-(d:Data)-[:FROM_SOURCE]-(s:Source) 
        return d.trait as trait,
               d.data as data,
               t.taxon as taxon,
               s.fullSource as source
    '''
    return graph.run(rq, taxon=taxon).to_data_frame()

allSources = allSourcesOfTaxon("Acanthus spinosus")

### Get all taxon with a specific trait

def allTaxonsWithTrait(trait):
    rq = ''' match(t:Trait {name: $trait})<-[:TYPE_OF_TRAIT]-(d:Data)-[:TRAIT_OF_TAXON]->(tx:Taxon) 
    return t.fullName as trait, 
           d.data as data,
           t.explanation as explication,
           tx.family as famille, 
           tx.taxon as taxon    
    '''
    return graph.run(rq, trait=trait).to_data_frame()


allTaxonWithTrait = allTaxonsWithTrait("GrowthForm")
#allTaxonWithTrait.loc[0]["explication"]

## Get all taxon with specific trait and specific modality

def allTaxonWithTraitAndModality(trait, modality):
    rq = ''' match(t:Trait {name: $trait})<-[:TYPE_OF_TRAIT]-(d:Data {data: $modality})-[:TRAIT_OF_TAXON]->(tx:Taxon) 
        return t.fullName as trait, 
               d.data as data, 
               t.explanation as explication, 
               tx.family as famille, 
               tx.taxon as taxon
    '''
    return graph.run(rq, trait=trait, modality=modality).to_data_frame()

BudSourceAndRootCrown = allTaxonWithTraitAndModality("BudSource", "root crown")

## Requêtes concernant les incendies
""" Comme l'étude est notamment portée sur les traits qui permettent le développement ou non d'un taxon
après un incendie, on peut regarder requêtes concernant ces traits en particuliers"""






