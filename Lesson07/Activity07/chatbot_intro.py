from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
import numpy as np
from os import listdir
import spacy
import en_core_web_sm


def pre_processing(sentences):
    nlp = en_core_web_sm.load()
    tokens = []
    for s in sentences:
        doc = nlp(s)
        for t in doc:
            if t.is_punct == False:
                tokens.append(t.lower_)
    return tokens


def doc_vector(tokens, model):
    feature_vec = np.zeros((50,), dtype="float32")
    for t in tokens:
         feature_vec = np.add(feature_vec, model[t])
    return np.array([np.divide(feature_vec,len(tokens))])



# doc_vectors = np.empty((0,100), dtype='f')
# for i in intents:
#     with open(intent_route + i) as f:
#         sentences = f.readlines()
#     sentences = [x.strip() for x in sentences]
#     sentences = pre_processing(sentences)
#     doc_vectors = np.append(doc_vectors,doc_vector(sentences),axis=0)




from sklearn.metrics.pairwise import cosine_similarity


def select_intent(sent_vector, doc_vector):
    index = -1
    similarity = -1 #cosine_similarity is in the range of -1 to 1
    for idx,v in zip(range(len(doc_vector)),doc_vector):
        v = v.reshape(1,-1)
        sent_vector = sent_vector.reshape(1,-1)
        aux = cosine_similarity(sent_vector, v).reshape(1,)
        if aux[0] > similarity:
            index = idx
            similarity = aux
    return index

def send_response(response_route, intent_name):
    with open(response_route + intent_name) as f:
        sentences = f.readlines()
    sentences = [x.strip() for x in sentences]
    return sentences[np.random.randint(low=0, high=len(sentences)-1)]

