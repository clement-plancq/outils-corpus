# Outils de traitement de corpus — Master Plurital

## Pratique

6 séances les lundis de 9h à 12h sur le discord plurital salon #outils-corpus-m1.  
Les lundis 15 mars, 29 mars et 3 mai nous aurons également l'amphi 7 de l'INALCO, PLC, 65 rue des grands moulins, 75013 Paris.

## Évaluation

Un devoir à rendre après chaque séance, sauf la dernière.  
6 séances, 5 devoirs, 5 notes. La note finale sera la moyenne des notes.

Tous vos devoirs devront m'être parvenus avant le 11 mai 2021.

Vous pouvez vérifier que j'ai bien reçu vos devoirs sur [cette page](devoirs-rendus.md)

## Séances

### 15 mars 2021 (amphi7)

* [intro, définitions, formats d'annotations, outils de requêtes](outils_corpus-1.html)

* Devoir : trouver et renseigner, à l'aide des 6 critères vus en cours, 4 corpus dont 1 *gros* corpus. 

### 22 mars 2021

* [Mots, types, tokens](outils_corpus-2.html)
* [Extraction d'informations](outils_corpus-3.html)

* devoir : calculer le ratio type/token pour les discours sur l'état de l'Union de [2016](files/stateoftheunion2016.txt) et [2017](files/stateoftheunion2017.txt)

  Pour la tokenization, utilisez le [tokenizer de Stanford](https://nlp.stanford.edu/software/tokenizer.shtml), [NLTK](http://www.nltk.org) ou [Spacy](https://spacy.io/)
  Vous devez envoyer le résultat ainsi que la description de vos traitements (scripts, outils, …)


### 29 mars 2021 (amphi 7)

* [Graphes, Grew, Spacy](outils_corpus-4.html)
* [notebook](outils_corpus-4.ipynb)

* devoirs : 
  - Avec [Grew-match](http://match.grew.fr/?corpus=UD_French-Sequoia@2.5#), trouvez dans le corpus UD_French-Sequoia@2.5 :
     - tous les triplets sujet, verbe, objet
     - les phrases avec sujets inversés  
  *Vous me rendez deux requêtes (dans le corps de mail ou un fichier txt)*

  - Avec l'aide du module Spacy, extrayez les triplets (sujet, verbe, objet) des phrases suivantes et commentez les éventuelles erreurs ou manques.

    « Les enfants n'aiment pas trop les asperges. »  
    « Les Français réclament moins d'impôts. »  
    « Les acacias donnent un miel ambré, limpide et fluide. »  
    « L'équipe fait porter le chapeau à l'arbitrage. »  
    « Des nuées de milliards d'insectes, venus de la péninsule Arabique, s'abattent sur la Corne de l'Afrique et dévorent les cultures, mettant en péril la sécurité alimentaire de la région. »  
  *Vous me rendez le notebook completé ou un script Python commenté*

### 12 avril 2021

* [Notebook de prise en main de Spacy](outils_corpus-5.ipynb)
* Devoir :  
  À l'aide de la bibliothèque Spacy vous relèverez les personnages mentionnés dans Le ventre de Paris.  
  Pour chacun des personnages qui apparaissent au moins trois fois, vous indiquerez les verbes dont ils sont sujet.

### 3 mai 2021 (amphi 7)
* [Notebook de prise en main de Spacy](outils_corpus-5.ipynb)
* [Étiquetage en POS](outils_corpus-6.html)

* Devoirs : Étiquetez manuellement puis avec l'étiqueteur de votre choix les trois textes suivants. Calculez la précision globale pour chacun des textes et commentez.
[sequoia.txt](files/sequoia.txt), [bashung.txt](files/bashung.txt), [orfeo.txt](files/orfeo.txt)

  Vous pourrez utiliser le [script d'évaluation de CoNLL 2018](http://universaldependencies.org/conll18/evaluation.html) (attention aux formats d'entrée), ce [script](https://github.com/dtuggener/ComparEval/blob/master/pos_tagging/eval_pos_tagger.py) ou vos propres calculs.


### 10 mai 2021

## Références

  * Tony McEnery and Andrew Wilson. Corpus  Linguistics. Edinburgh: Edinburgh University Press, 2001 (second edition).
  * Céline Poudat et Frédéric Landragin. Explorer un corpus textuel : Méthodes – pratiques – outils. De Boeck Supérieur, 2017.
  * Daniel Jurafsky and James H. Martin.Speech and Language Processing. Pearson, 2008 (second edition). [pdfs de la troisième édition en cours](https://web.stanford.edu/~jurafsky/slp3/)
  * [Lecture Slides from the Stanford Coursera course by Dan Jurafsky and Christopher Manning](https://web.stanford.edu/~jurafsky/NLPCourseraSlides.html)
  * [Site de Sébastien Ruder](http://ruder.io/)
  * [Cours interactif sur Spacy par Ines Montani](https://course.spacy.io/)
