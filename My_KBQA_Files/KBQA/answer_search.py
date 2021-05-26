from py2neo import Graph

class AnswerSearcher:
    def __init__(self):
        self.g = Graph("http://localhost:7474", user="neo4j", password="neo4jneo4j")
        self.num_limit = 20

    '''Cypher query'''
    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers

    '''qustion_type，answer template'''
    def answer_prettify(self, question_type, answers):
        final_answer = []
        if not answers:
            return ''
            
        elif question_type == 'heifer_breeding':
            l_ = []
            for i in answers:
                if i['m.heitype'] not in l_:
                    l_.append(i['m.heitype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.heitype'], i['m.heianswer'])
                    print(final_answer)

        elif question_type == 'heifer_feeding':
            l_ = []
            for i in answers:
                if i['m.heitype'] not in l_:
                    l_.append(i['m.heitype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.heitype'], i['m.heianswer'])
                    print(final_answer)

        elif question_type == 'heifer_health':
            l_ = []
            for i in answers:
                if i['m.heitype'] not in l_:
                    l_.append(i['m.heitype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.heitype'], i['m.heianswer'])
                    print(final_answer)

        elif question_type == 'heifer_housing':
            l_ = []
            for i in answers:
                if i['m.heitype'] not in l_:
                    l_.append(i['m.heitype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.heitype'], i['m.heianswer'])
                    print(final_answer)

        elif question_type == 'breeding':
            l_ = []
            for i in answers:
                if i['m.btype'] not in l_:
                    l_.append(i['m.btype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.btype'], i['m.banswer'])
                    print(final_answer)

        elif question_type == 'feeding':
            l_ = []
            for i in answers:
                if i['m.ftype'] not in l_:
                    l_.append(i['m.ftype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.ftype'], i['m.fanswer'])
                    print(final_answer)

        elif question_type == 'health':
            l_ = []
            for i in answers:
                if i['m.hetype'] not in l_:
                    l_.append(i['m.hetype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.hetype'], i['m.heanswer'])
                    print(final_answer)

        elif question_type == 'housing':
            l_ = []
            for i in answers:
                if i['m.hotype'] not in l_:
                    l_.append(i['m.hotype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.hotype'], i['m.hoanswer'])
                    print(final_answer)                   

        return final_answer
       

if __name__ == '__main__':
    searcher = AnswerSearcher()