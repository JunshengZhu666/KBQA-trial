import os
import ahocorasick

class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        #　where we match the feature words

        self.heifer_management_path = os.path.join(cur_dir, 'heifer_management.txt')

        # load the feature words
 
        self.heifer_management_wds= [i.strip() for i in open(self.heifer_management_path,encoding="utf-8") if i.strip()]

        self.region_words = set(self.heifer_management_wds)

        # to build demain actree
        self.region_tree = self.build_actree(list(self.region_words))
        # to build dictionary
        self.wdtype_dict = self.build_wdtype_dict()

        # query language

        # 1,heifer_breeding
        self.q10_qwds = ['breed', 'heat', 'mate', 'reproduction']
        # 2,heifer_feeding
        self.q11_qwds = ['feed', 'eat', 'fiber', 'grow']
        # 3,heifer_health
        self.q12_qwds = ['healthy', 'ill', 'sick', 'weak','culling']
        # 4,heifer_housing
        self.q13_qwds = ['bran', 'live', 'rest', 'keep','brans','house','housing']
        # 1,breeding
        self.q14_qwds = ['conception', 'estrus','monitoring']
        # 2,feeding
        self.q15_qwds = ['colostrum', 'feed additives', 'nutritional requirements']
        # 3,health
        self.q16_qwds = ['vaccination','parasites','diarrhea','biosecurity']
        # 4,housing
        self.q17_qwds = ['Group1','Group2','Group3-7']
        
        print('model init finished ......')

        return

    '''classification main function'''
    def classify(self, question):
        data = {}
        dairy_dict = self.check_dairy(question)
        if not dairy_dict:
            return {}
        data['args'] = dairy_dict
        #to garther the entiies in query 
        types = []
        for type_ in dairy_dict.values():
            types += type_
        question_type = 'others'

        question_types = []



        # Trial1
        if self.check_words(self.q10_qwds, question) and ('heifer_management' in types) :
            question_type = 'heifer_breeding'
            question_types.append(question_type)
        # Trial2
        if self.check_words(self.q11_qwds, question) and ('heifer_management' in types):
            question_type = 'heifer_feeding'
            question_types.append(question_type)
        # Trial3
        if self.check_words(self.q12_qwds, question) and ('heifer_management' in types):
            question_type = 'heifer_health'
            question_types.append(question_type)
        # Trial4
        if self.check_words(self.q13_qwds, question) and ('heifer_management' in types):
            question_type = 'heifer_housing'
            question_types.append(question_type)

        # Trial1
        if self.check_words(self.q14_qwds, question) and ('heifer_management' in types) :
            question_type = 'breeding'
            question_types.append(question_type)
        # Trial2
        if self.check_words(self.q15_qwds, question) and ('heifer_management' in types):
            question_type = 'feeding'
            question_types.append(question_type)
        # Trial3
        if self.check_words(self.q16_qwds, question) and ('heifer_management' in types):
            question_type = 'health'
            question_types.append(question_type)
        # Trial4
        if self.check_words(self.q17_qwds, question) and ('heifer_management' in types):
            question_type = 'housing'
            question_types.append(question_type)

        # merge into a dictionary 
        data['question_types'] = question_types

        return data

    '''build word type dict'''
    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
  
            if wd in self.heifer_management_wds:
                wd_dict[wd].append('heifer_management')               
            
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
        question = input('input an question:')
        data = handler.classify(question)
        print(data)