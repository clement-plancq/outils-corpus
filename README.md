# Outils de traitement de corpus — Master Plurital

## Pratique

~~6 séances les lundis de 9h à 12h dans l'amphi 5 de l'INALCO, PLC, 65 rue des grands moulins, 75013 Paris.~~  
6 séances les lundis de 10h à 12h sur Discord.

## Évaluation

Un devoir à rendre après chaque séance.  
6 séances, ~~6~~ 5 devoirs, ~~6~~ 5 notes. La note finale sera la moyenne des notes.

Tous vos devoirs devront m'être parvenus avant le 11 mai 2020.

Vous pouvez vérifier que j'ai bien reçu vos devoirs sur [cette page](devoirs-rendus.md)

## Séances

### 16 mars 2020

* [intro, définitions, formats d'annotations, outils de requêtes](outils_corpus-1.html)

* Devoir : trouver et renseigner, à l'aide des 6 critères vus en cours, 4 corpus dont 1 *gros* corpus. 

### 23 mars 2020
* [Mots, types, tokens](outils_corpus-2.html)
* [Extraction d'informations](outils_corpus-3.html)

* devoir : calculer le ratio type/token pour les discours sur l'état de l'Union de [2016](files/stateoftheunion2016.txt) et [2017](files/stateoftheunion2017.txt)

  Pour la tokenization, utilisez le [tokenizer de Stanford](https://nlp.stanford.edu/software/tokenizer.shtml), [NLTK](http://www.nltk.org) ou [Spacy](https://spacy.io/)
  Vous devez envoyer le résultat ainsi que la description de vos traitements (scripts, outils, …)

### 30 mars 2020

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



### 20 avril 2019

* [Notebook de prise en main de Spacy](outils_corpus-5.ipynb)

* Devoirs (*au choix*) :
  * Modifiez le script de vectorisation du cours d'[introduction à la fouille de textes](https://loicgrobol.github.io/intro-fouille-textes/) de façon à (1) utiliser la tokenisation par Spacy et (2) ajouter un trait comptant le nombre d'entités nommées par documents. Vous me rendez un script en précisant en commentaire où sont vos modifications.
  * Ré-entraînez un modèle de reconnaissance d'EN pour l'adapter à : soit deux textes sur l'actualité de l'industrie du jeu vidéo ([ici](https://www.cnews.fr/vie-numerique/2020-04-09/confinement-le-service-de-jeux-video-stadia-est-gratuit-pendant-deux-mois) et [ici](https://www.20minutes.fr/high-tech/2758007-20200409-google-stadia-lancement-version-gratuite-deux-mois-abonnement-pro-egalement-offerts)), soit deux poésies de François Villon ([ici](https://www.poetica.fr/poeme-5050/francois-villon-ballade-des-dames-du-temps-jadis/) et [ici](https://www.poetica.fr/poeme-5052/francois-villon-ballade-des-seigneurs-du-temps-jadis/)).  
  Vous pouvez utiliser d'autres textes si ça vous chante (de chansons de hip-hop, ou en français de la francophonie par exemple).  
  Vous me rendez un script ou un notebook avec des commentaires sur les résultats.

### 27 avril 2019

* [Étiquetage en POS](outils_corpus-6.html)

* Devoirs : Étiquetez manuellement puis avec l'étiqueteur de votre choix les trois textes suivants. Calculez la précision globale pour chacun des textes et commentez.
[sequoia.txt](files/sequoia.txt), [bashung.txt](files/bashung.txt), [orfeo.txt](files/orfeo.txt)

  Vous pourrez utiliser le [script d'évaluation de CoNLL 2018](http://universaldependencies.org/conll18/evaluation.html) (attention aux formats d'entrée), ce [script](https://github.com/dtuggener/ComparEval/blob/master/pos_tagging/eval_pos_tagger.py) ou vos propres calculs.



### 4 mai 2019

* [Word embeddings](outils_corpus-7.html)
* [notebook](outils_corpus-7.ipynb)

Pas de devoirs pour cette séance.

## Références

  * Tony McEnery and Andrew Wilson. Corpus  Linguistics. Edinburgh: Edinburgh University Press, 2001 (second edition).
  * Céline Poudat et Frédéric Landragin. Explorer un corpus textuel : Méthodes – pratiques – outils. De Boeck Supérieur, 2017.
  * Daniel Jurafsky and James H. Martin.Speech and Language Processing. Pearson, 2008 (second edition). [pdfs de la troisième édition en cours](https://web.stanford.edu/~jurafsky/slp3/)
  * [Lecture Slides from the Stanford Coursera course by Dan Jurafsky and Christopher Manning](https://web.stanford.edu/~jurafsky/NLPCourseraSlides.html)
  * [Site de Sébastien Ruder](http://ruder.io/)
  * [Cours interactif sur Spacy par Ines Montani](https://course.spacy.io/)
