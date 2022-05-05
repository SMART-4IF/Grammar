# Grammaire

## Introduction
Ce package python est un module essentiel du projet Bobby, un traducteur LSF <-> français. Une IA est chargée de reconnaitre les mots signées par une personne sourde. Une fois ces mots traduits, il s'agit de les mettre dans le bon ordre et de reconstruire la grammaire de la phrase (accords, déterminants, conjugaison, etc.). C'est l'objectif du code présent sur ce repo.

## Cahier des charges
Ce module a pour but de reconstruire la grammaire de n'importe quelle phrase LSF à condition:
- que la phrase comporte moins de 4 signes
- que la phrase LSF soit grammaticalement correcte
- que la phrase ne comporte pas d'éléments faisant appel au contexte pour décider comment former sa grammaire

La reconstruction de la grammaire d'une phrase prend en moyenne 4 dixièmes de secondes si le verbe n'a jamais été rencontré auparavant et 5 centièmes de secondes sinon.

## Commment ça marche ?
Notre algorithme reçoit en entrée la liste des mots d'une phrase LSF. Dans un premier temps, des scripts déterminent le rôle de chacun de ces mots (verbe, sujet, action, adverbe, marqueur temporel, marqueur de négation, etc.).

Une fois cette étape effectuée, d'autres scripts vont remettre les mots dans le bon ordre, appliquer les réglèes d'accords et de conjugaison de la langue française et ajouter la ponctuation.

Le projet a été développé selon la méthodologie du TDD: comme la traduction est effectuée par raffinement successifs à partir de règles, cela nous permettait de vérifier que l'ajout d'une règle ne détruisait pas le résultat des autres règles.

## Pourquoi ne pas avoir utilisé une IA pour faire cela ?
Nous avons fais le choix de ne pas utiliser une IA car les signes doivent, au préalable, être reconnus par une première IA. Mettre 2 IA l'une après l'autre pose 2 problèmes:
- les latences s'accumulent et les performances seraient très mauvaises
- les taux d'erreur des 2 IA rendraient la traduction peut fiable

Comme l'IA de reconnaissance des signes est indispensable, nous avons fait le choix de ne pas utiliser cette méthode pour effectuer la reconstruction de la grammaire.

## Installation et lancement
Pour installer notre module, vous devez cloner le repo et importer le plugin verbecc avec la commande `pip install verbecc`

A la racine, vous trouverez 2 fichier: launchScripts permet d'utiliser la traduction, launchTests permet de lancer tous les tests. Dans le résultat des tests, vous trouverez toutes les stuctures de phrases que notre module est capable de traduire.

