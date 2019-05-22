import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
import gensim
import nltk
import string

from gensim.models import Word2Vec
from nltk.corpus import stopwords


#stop-words
class Word2VecCustom:
    def __init__(self,corpus,badWords,goodWords):
        print("b")

        self.badWords = badWords
        self.goodWords  = goodWords
        self.start(corpus)

    def start(self,corpus):
        print("A")
        stop_words=set(nltk.corpus.stopwords.words('english'))
        sample_text= corpus
        type(sample_text)
        sentences=nltk.sent_tokenize(sample_text)
        print("Number of sentences:",len(sentences))
        token_sent=[]
        tokenizer = {}
        for sent in sentences:
            sent.translate(string.punctuation)
            myWords = sent.split()
            for word in myWords:
                if word in tokenizer:
                    tokenizer[word] += 1
                else:
                    tokenizer[word] = 1
        for sent in sentences:
            sent.translate(string.punctuation)

            myWords2=sent.split()
            words=nltk.word_tokenize(sent)
            words=[w for w in words if w not in stop_words]
            words=[w for w in words if tokenizer.setdefault(w,"Scruffy")]


            token_sent.append(words)
        w2v_model=Word2Vec(token_sent,size=10,min_count=1,window=6,sg=1,hs=0,seed=42,workers=4)
        w2v_model.train(token_sent,total_examples=len(token_sent),epochs=10)

        vocab=list(w2v_model.wv.vocab)
        print(len(vocab))
        print(vocab)

        print(w2v_model.wv.similarity("retarded","comfy"))

        s = str(input("Enter a sentence :"))
        sentence = s.split()
        sentenceResult = 0;
        for word in sentence:
            if word in self.badWords:
                sentenceResult -= 1
            elif word in self.goodWords:
                sentenceResult += 1
        if sentenceResult > 0:
            print("Dis Gud")
        elif sentenceResult < 0:
            print("Dis Bad")
        else:
            print("Dis Neutral")
        revampedSent = s.split()
        goodSentence =""
        for word in revampedSent:
            if word not in self.badWords:
                goodSentence += word + " "
            else:
                highestNr=0
                highestWord=""
                for wrd in self.goodWords:
                    if wrd in w2v_model.wv.vocab:
                        if(w2v_model.wv.similarity(word,wrd)>highestNr):
                            highestNr=w2v_model.wv.similarity(word,wrd)
                            highestWord=wrd
                            print("Ahoy")
                goodSentence += highestWord + " "
        print(goodSentence)
        #word2vec

        # corpus
        from nltk.corpus import gutenberg
