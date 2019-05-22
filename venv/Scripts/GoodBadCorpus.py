import re
from Word2VecCustom import Word2VecCustom

class GoodBadCorpus:
    def __init__(self):
        self.badCorpus = open("google_twunter_lol.txt")
        self.goodCorpus = open("positive-words.txt")

        self.YTCorpus = open("YTcorpus.txt",encoding="utf8")


        self.clean(self.badCorpus,self.goodCorpus,self.YTCorpus)
    def clean(self,badCorpus,goodCorpus,YTCorpus):
        print(type(badCorpus),type(YTCorpus))
        YTc = YTCorpus.readlines()


        bC = badCorpus.readlines()
        gC = goodCorpus.readlines()

        badWords = []
        goodWords = [] #have to cite the references
        YTcomments = []
        for x  in bC:
            x = re.sub("\:1,\n","",x)
            badWords.append(x)
        for y in gC:
            y = re.sub("\n","",y)
            goodWords.append(y)
        for z in YTc:
            z=re.sub("\-"," ",z)
            z= z.encode('ascii', 'ignore').decode('ascii') #remove emojis

            v =  z.split()
            newZ = []
            for word in v:
                newZ.append(word.lower())

            z=" ".join(newZ)
            YTcomments.append(z)
        sentenceResultDictionary = {}
        for i in range(1,50000):
            print(i)
            sentence = YTcomments[i].split()
            sentenceResult=0;
            for word in sentence:
                if word in badWords:
                    sentenceResult-=1
                elif word in goodWords:
                    sentenceResult+=1
            if sentenceResult>0:
                sentenceResultDictionary[" ".join(sentence)] = 1
            elif sentenceResult<0:
                sentenceResultDictionary[" ".join(sentence)] = -1
            else:
                sentenceResultDictionary[" ".join(sentence)] = 0


        badWordsCount =0
        goodWordsCount =0
        badlist = []
        goodlist = []
        for sentence in sentenceResultDictionary:
            print(sentence, " | " ,sentenceResultDictionary[sentence])
        YTcleaned  = "\n".join(YTcomments)
        w2v = Word2VecCustom(YTcleaned,badWords,goodWords)

        #print(badWordsCount, " " , goodWordsCount)
        #print(badlist," ",goodlist)
        #if(badWordsCount>goodWordsCount):
        #    print("Dis Bad")
        #elif(goodWordsCount>badWordsCount):
        #   print("Dis Gud")
        #else:
        #    print("Dis Neutral")
        #revampedSentence = s.split()
        #goodSentence = ""
        #for word in revampedSentence:
        #    if word not in badlist:
        #        goodSentence += word + " "
        #    else:
        #        goodSentence += "not " + word
        #print(goodSentence)