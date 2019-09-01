# PBMNet - Analysing the Brazilian Network of Mathematics Research
## Final Project for Class Fundamentos de Data Science - FGV

## Team:
* Davi Sales Barreira
* Franklin Oliveira

## Overview:
The Curriculum Lattes is a cv of the academic activities of
students and researchers of Brazil. Stored at Plataforma Lattes, 
this cv format is adopted by most academic institutions and research centers
of Brazil, therefore, constituting a rich siurce of information to study
the academic production of the country.

At Plataforma Lattes, the researchers inform their area of study, making
it possible to analyze the data by research area.

In this project, we analyze the data for the researchers in mathematics.
We also obtained and analyzed the researchers with areas listed as 
computer science, probability and statistics, since we consider them
to be part of mathematics as a whole.

## Objective:
Our aim is to get an overall understanding of how is the research network
of mathematics of the researches in Plataforma Lattes. For that we:

* Extract some fundamental statistics regarding the research in mathematics,
such as total number of researchers, total number of publications,
average number of publication per researcher.

* Generate a co-authorship network and study the properties of such network,
as the number of edges, degree distribution, number of connected components,
average shortest path.

## Graph-Tool:
In this repository, to create the images of the co-authorship networks
and estimate some parameters of the network, we used
[**graph-tool**](https://graph-tool.skewed.de/), a library for efficient
graph analysis. Note that this library uses C++ to do the heavy lifting,
therefore it needs to be compiled before using (which can take up to 4 hours).
The installation steps are present in the official website for the library.

