# -*- coding: utf-8 -*-

### Exemple d'entraînement correctif de l'étiqueteur Spacy

import random
import re
import spacy
from spacy.util import minibatch, compounding
from spacy.tokens import Token
from spacy.tokenizer import Tokenizer
from spacy.symbols import POS

def create_tokenizer(nlp):                                             
    # inspired by https://stackoverflow.com/questions/43388476/how-could-spacy-tokenize-hashtag-as-a-whole
    # contains the regex to match all sorts of urls:
    from spacy.lang.tokenizer_exceptions import URL_PATTERN
    # extending the default url regex with regex for hashtags with "or" = |
    hashtag_pattern = r'''|^(#[\w_-]+)$'''
    url_and_hashtag = URL_PATTERN + hashtag_pattern
    url_and_hashtag_re = re.compile(url_and_hashtag)
     
    # set a custom extension to match if token is a hashtag
    hashtag_getter = lambda token: token.text.startswith('#')
    Token.set_extension('is_hashtag', getter=hashtag_getter, force=True)
    
    return Tokenizer(nlp.vocab, token_match=url_and_hashtag_re.match)



def main():
    TRAIN_DATA = [("Que faire quand tu as plus de build en end zone ? #Fortnite ",
     {"tags": ["PRON", "VERB", "SCONJ", "PRON", "VERB", "ADV", "ADP", "NOUN", "ADP", "NOUN", "NOUN", "PUNCT", "PROPN"]}),
    ("Pas parfait mais vraiment vraiment cool. Et ça m'a foutu la hype de folie pour #Endgame !",
     {"tags":["ADV", "ADJ", "CCONJ", "ADV", "ADV", "ADJ", "PUNCT", "CCONJ", "PRON", "PRON", "AUX", "VERB", "DET", "NOUN", "ADP", "NOUN", "ADP", "PROPN", "PUNCT"]}),
    ("#Endgame : ça va être chanmé ! ", {"tags":["PROPN", "PUNCT", "PRON", "VERB", "AUX", "ADJ", "PUNCT"]})]
    
    print("Load nlp model")
    nlp = spacy.load('fr_core_news_sm')
    # change the tokenizer in order to handle hastag properly
    nlp.tokenizer = create_tokenizer(nlp)

    tagger = nlp.create_pipe("tagger")

    for _, annotations in TRAIN_DATA:
        for tag in annotations.get("tags"):
            tagger.add_label(tag, {POS: tag})

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "tagger"]
    print("Training")
    with nlp.disable_pipes(*other_pipes):  # only train tagger
        optimizer = nlp.begin_training()
        for itn in range(100):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    sgd=optimizer,
                    losses=losses,
                )
                print("Losses", losses)

    # test the trained model
    for text, _ in TRAIN_DATA:
        doc = nlp(text)
        print([(tok.text, tok.pos_) for tok in doc])

if __name__ == "__main__":
    main()