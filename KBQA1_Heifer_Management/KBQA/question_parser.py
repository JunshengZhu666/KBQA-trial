from nltk.stem import PorterStemmer

class QuestionPaser:

    '''To build entity dictionary'''
    def build_entitydict(self, args):

        entity_dict = {}
        
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)
                    #stemmed_entity_dict = stem(entity_dict)

        return entity_dict

    '''main function'''
    def parser_main(self, res_classify):
        #extract the entities
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        #extract the question types
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            
            #Trail_1
            if question_type == 'heifer_question':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer'))            

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    '''Excecute different questions with sqls'''
    def sql_transfer(self, question_type, entities):
        if not entities:
            return []

        # cypher query
        sql = []


        ###  Trail1
        if question_type == 'heifer_question':
            sql = ["match(m:Heifer) where m.htype=\"{0}\" return m.htype,m.hanswer".format(i) for i in entities]


        return sql

if __name__ == '__main__':
    handler = QuestionPaser()
