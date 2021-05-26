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
            if question_type == 'heifer_breeding':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management'))            
            #Trail_2
            elif question_type == 'heifer_feeding':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management')) 
            #Trail_3
            elif question_type == 'heifer_health':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management')) 
            #Trail_4
            elif question_type == 'heifer_housing':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management')) 
            #Trail_1
            elif question_type == 'breeding':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management'))            
            #Trail_2
            elif question_type == 'feeding':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management')) 
            #Trail_3
            elif question_type == 'health':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management')) 
            #Trail_4
            elif question_type == 'housing':
                sql = self.sql_transfer(question_type, entity_dict.get('heifer_management')) 

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
        if question_type == 'heifer_breeding':
            sql = ["match(m:Heifer_management) where m.heitype=\"{0}\" return m.heitype,m.heianswer".format(i) for i in entities]

        ###  Trail2
        elif question_type == 'heifer_feeding':
            sql = ["match(m:Heifer_management) where m.heitype=\"{0}\" return m.heitype,m.heianswer".format(i) for i in entities]

        ###  Trail3
        elif question_type == 'heifer_health':
            sql = ["match(m:Heifer_management) where m.heitype=\"{0}\" return m.heitype,m.heianswer".format(i) for i in entities]

        ###  Trail4
        elif question_type == 'heifer_housing':
            sql = ["match(m:Heifer_management) where m.heitype=\"{0}\" return m.heitype,m.heianswer".format(i) for i in entities]
        

        #######  Trail1
        elif question_type == 'breeding':
            sql = ["match(m:Breeding) where m.btype=\"{0}\" return m.btype,m.banswer".format(i) for i in entities]

        #######  Trail2
        elif question_type == 'feeding':
            sql = ["match(m:Feeding) where m.ftype=\"{0}\" return m.ftype,m.fanswer".format(i) for i in entities]

        #######  Trail3
        elif question_type == 'health':
            sql = ["match(m:Health) where m.hetype=\"{0}\" return m.hetype,m.heanswer".format(i) for i in entities]

        #######  Trail4
        elif question_type == 'housing':
            sql = ["match(m:Housing) where m.hotype=\"{0}\" return m.hotype,m.hoanswer".format(i) for i in entities]
        return sql

if __name__ == '__main__':
    handler = QuestionPaser()
