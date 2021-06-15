import os
import ahocorasick
from nltk.stem import PorterStemmer

class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])

        #　where we match the feature words
        self.diseases_path = os.path.join(cur_dir, 'Diseases.txt')
        self.symptoms_path = os.path.join(cur_dir, 'Symptoms.txt')

        # load the feature words
        self.diseases_wds= [i.strip() for i in open(self.diseases_path,encoding="utf-8") if i.strip()]
        self.symptoms_wds= [i.strip() for i in open(self.symptoms_path,encoding="utf-8") if i.strip()]

        #stemmer = PorterStemmer()
        #self.stemmed_heifer_wds = stemmer.stem(self.heifer_wds)
        
        #word stemming
        #self.heifer_wds = self.process_word(self.heifer_wds)


        self.region_words = set(self.diseases_wds + self.symptoms_wds)

        # to build demain actree
        self.region_tree = self.build_actree(list(self.region_words))

        # to build dictionary
        self.wdtype_dict = self.build_wdtype_dict()
 
        # word stemming
        # self.word_clean = self.process_word()


        # query language

        
        self.symptom_qwds = ['why','symptom','show','Why']
        self.cause_qwds = ['cause', 'make','causes','made','Cause','caused']
        self.treatment_qwds = ['treat', 'Treat','treatment','cure','treatments','Treatments']
        self.prevention_qwds = ['prevent', 'prevents']
        #self.description_qwds = []
        self.name_qwds = ['name', 'call']
        self.tip_qwds = ['tip', 'suggest','advice']
        

        print('model init finished ......')

        return


    
    '''classification main function'''
    def classify(self, question):
        data = {}
        dairy_dict = self.check_dairy(question)
        if not dairy_dict:
            return {}
        data['args'] = dairy_dict
        #to garther the entities in query 
        types = []
        for type_ in dairy_dict.values():
            types += type_
        question_type = 'others'

        question_types = []



        # 
        if self.check_words(self.symptom_qwds, question) and ('symptoms' in types) :
            question_type = 'ask_symptom'
            question_types.append(question_type)

        if self.check_words(self.cause_qwds, question) and ('diseases' in types) :
            question_type = 'ask_cause'
            question_types.append(question_type)

        if self.check_words(self.treatment_qwds, question) and ('diseases' in types) :
            question_type = 'ask_treatment'
            question_types.append(question_type)

        if self.check_words(self.prevention_qwds, question) and ('diseases' in types) :
            question_type = 'ask_prevention'
            question_types.append(question_type)

        if self.check_words(self.name_qwds, question) and ('diseases' in types) :
            question_type = 'ask_name'
            question_types.append(question_type)

        if self.check_words(self.tip_qwds, question) and ('diseases' in types) :
            question_type = 'ask_tip'
            question_types.append(question_type)            

        if question_types == [] and 'diseases' in types:
            question_types = ['ask_description']
       
        # merge into a dictionary 
        data['question_types'] = question_types

        return data

    '''use word stemming to preprocess the words'''
    def process_word(self,words):
        stemmer = PorterStemmer()
        
        word_clean = []
        for word in words:
            stem_word = stemmer.stem(word)
            word_clean.append(stem_word)
        return word_clean    

    '''build word type dict'''
    def build_wdtype_dict(self):
        
        #stemmer = PorterStemmer()

        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
  
            if wd in self.diseases_wds:
                wd_dict[wd].append('diseases')

            if wd in self.symptoms_wds:
                wd_dict[wd].append('symptoms')
                              
            
        return wd_dict

    '''actree'''
    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    '''filter the query language'''
    def check_dairy(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i:self.wdtype_dict.get(i) for i in final_wds}

        return final_dict

    '''classification base on entities'''
    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False



if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        unstemmed_question = input('input an question:')
        question = PorterStemmer(unstemmed_question)
        data = handler.classify(question)
        print(data)


