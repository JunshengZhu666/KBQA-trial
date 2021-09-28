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
            if question_type == 'ask_symptom':
                sql = self.sql_transfer(question_type, entity_dict.get('symptoms'))            

            elif question_type == 'ask_cause':
                sql = self.sql_transfer(question_type, entity_dict.get('diseases'))            

            elif question_type == 'ask_treatment':
                sql = self.sql_transfer(question_type, entity_dict.get('diseases'))            

            elif question_type == 'ask_prevention':
                sql = self.sql_transfer(question_type, entity_dict.get('diseases'))            

            elif question_type == 'ask_name':
                sql = self.sql_transfer(question_type, entity_dict.get('diseases'))            

            elif question_type == 'ask_tip':
                sql = self.sql_transfer(question_type, entity_dict.get('diseases'))            

            elif question_type == 'ask_description':
                sql = self.sql_transfer(question_type, entity_dict.get('diseases'))            

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
        #if question_type == 'heifer_question':
        #    sql = ["match(m:Heifer) where m.htype=\"{0}\" return m.htype,m.hanswer".format(i) for i in entities]

        if question_type == 'ask_symptom':
            sql = ["MATCH (m:Diseases)-[r:hasSymptom]->(n:Symptoms) where n.sname=\"{0}\" return n.sname, m.dname".format(i) for i in entities]

        elif question_type == 'ask_cause':
            sql = ["MATCH (m:Diseases) where m.dname=\"{0}\" return m.dname, m.dcauses".format(i) for i in entities]            

        elif question_type == 'ask_treatment':
            sql = ["MATCH (m:Diseases) where m.dname=\"{0}\" return m.dname, m.dtreatments".format(i) for i in entities]            

        elif question_type == 'ask_prevention':
            sql = ["MATCH (m:Diseases) where m.dname=\"{0}\" return m.dname, m.dpreventions".format(i) for i in entities]            

        elif question_type == 'ask_name':
            sql = ["MATCH (m:Diseases)<-[r:hasOthername]-() where m.dname=\"{0}\" RETURN m.dname".format(i) for i in entities]            

        elif question_type == 'ask_tip':
            sql = ["MATCH (m:Diseases) where m.dname=\"{0}\" return m.dname, m.dtips".format(i) for i in entities]            

        elif question_type == 'ask_description':
            sql = ["MATCH (m:Diseases) where m.dname=\"{0}\" return m.dname, m.ddescribitions".format(i) for i in entities]            


        return sql

if __name__ == '__main__':
    handler = QuestionPaser()
