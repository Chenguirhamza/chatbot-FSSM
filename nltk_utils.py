import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    """
        diviser la phrase en un tableau de mots/jetons
        un jeton peut être un mot ou un caractère de ponctuation, ou un nombre
     """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
        radical = trouver la forme racine du mot
        exemples:
        mots = ["organiser", "organiser", "organiser"]
        mots = [tige(w) pour w dans les mots]
        -> ["orgue", "orgue", "orgue"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    retourner le tableau de sacs de mots:
    1 pour chaque mot connu existant dans la phrase, 0 sinon
    Exemple:
    phrase = ["bonjour", "comment", "êtes", "vous"]
    mots = ["salut", "bonjour", "je", "vous", "au revoir", "merci", "cool"]
    tourbière = [ 0 , 1 , 0 , 1 , 0 , 0 , 0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag